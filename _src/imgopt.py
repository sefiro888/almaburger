"""Optimización de imágenes al generar la web (los originales de _src/img no se tocan).

- Cada JPG pasa a WebP (misma calidad visual, bastante menos peso) en varios anchos:
  480, 800 y el ancho original. Los <img> llevan srcset/sizes y el navegador elige
  el tamaño justo para la pantalla (en un móvil de alta densidad sigue cogiendo el grande).
- Las portadas de los vídeos pasan a WebP y se cargan al acercarse (data-poster).
Las versiones se guardan en _src/_cache para no recalcularlas en cada build.
"""
import hashlib, pathlib, re, shutil
from PIL import Image

SRC = pathlib.Path(__file__).parent
CACHE = SRC / '_cache' / 'webp'
WIDTHS = (480, 800)
Q = 82


DIMS = {}


def _variants(f, rel):
    key = hashlib.md5(f.read_bytes()).hexdigest()[:10]
    with Image.open(f) as im0:
        W = im0.width
        DIMS[rel] = im0.size
    ws = [w for w in WIDTHS if w < W * 0.9] + [W]
    res, im = [], None
    for w in ws:
        name = rel[:-4] + ('' if w == W else f'-{w}') + '.webp'
        c = CACHE / key / name
        if not c.exists():
            if im is None:
                im = Image.open(f).convert('RGB')
            c.parent.mkdir(parents=True, exist_ok=True)
            r = im if w == W else im.resize((w, round(im.height * w / W)), Image.LANCZOS)
            r.save(c, 'WEBP', quality=Q, method=6)
        res.append((w, name, c))
    return res


def build(out_dir, html_files, js_files):
    img_src = SRC / 'img'
    table = {}
    for f in img_src.rglob('*.jpg'):
        rel = f.relative_to(img_src).as_posix()
        table[rel] = _variants(f, rel)
        for _, name, c in table[rel]:
            dst = out_dir / 'img' / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(c, dst)

    def img_tag(m):
        tag, rel = m.group(0), m.group(1)
        vs = table.get(rel)
        if not vs:
            return tag
        ss = ', '.join(f'img/{n} {w}w' for w, n, _ in vs)
        tag = tag.replace(f'src="img/{rel}"', f'src="img/{vs[-1][1]}" srcset="{ss}"')
        # sizes="auto" hace que Chrome reserve 300x150 si el <img> no trae width/height
        # (la foto salía aplastada): siempre ponemos las medidas reales
        if ' width=' not in tag and rel in DIMS:
            w, h = DIMS[rel]
            tag = tag.replace('<img ', f'<img width="{w}" height="{h}" ', 1)
        if 'sizes=' not in tag:
            sizes = '(max-width: 700px) 92vw, 40vw'
            if 'loading="lazy"' in tag:
                sizes = 'auto, ' + sizes          # Chrome calcula el tamaño real; el resto usa la regla
            tag = tag.replace('<img ', f'<img sizes="{sizes}" ', 1)
        return tag

    def poster(m):
        rel = m.group(1)
        return f'data-poster="img/{table[rel][-1][1]}"' if rel in table else m.group(0)

    for p in html_files:
        s = p.read_text(encoding='utf-8')
        s = re.sub(r'<img\b[^>]*?\bsrc="img/([^"]+?\.jpg)"[^>]*>', img_tag, s)
        s = re.sub(r'poster="img/([^"]+?\.jpg)"', poster, s)
        p.write_text(s, encoding='utf-8')
    for p in js_files:
        s = p.read_text(encoding='utf-8')
        s = re.sub(r'(img/dishes/(?:s/)?\$\{[^}]+\})\.jpg', r'\1.webp', s)
        p.write_text(s, encoding='utf-8')
