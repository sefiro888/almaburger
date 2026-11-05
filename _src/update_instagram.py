"""Actualiza «Últimas publicaciones» con lo último de @almaburgers.

Necesita un token de la API de Instagram (Instagram API with Instagram Login) de la cuenta
del restaurante, que solo puede generar el propio restaurante desde Meta for Developers.

    IG_TOKEN=xxxx python _src/update_instagram.py && python _src/build.py

Qué hace:
  1. Renueva el token (los tokens largos duran 60 días; renovarlo alarga otros 60).
  2. Lee las 12 últimas publicaciones (foto, reel o carrusel).
  3. Descarga cada portada a _src/img/ig/<id>.jpg (recortada a 4:5).
  4. Escribe _src/data/instagram.json, que build.py convierte en la cuadrícula.

Sin IG_TOKEN no toca nada: la web sigue con las publicaciones que ya tiene.
En GitHub lo lanza .github/workflows/instagram.yml una vez al día.
"""
import datetime, io, json, os, pathlib, re, sys, urllib.parse, urllib.request

SRC = pathlib.Path(__file__).parent
API = 'https://graph.instagram.com'
N = 12


def get(url, **params):
    q = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f'{url}?{q}', timeout=30) as r:
        return json.load(r)


def short(caption):
    """Primera frase del texto de la publicación, sin hashtags ni emojis sueltos al final."""
    t = (caption or '').strip().split('\n')[0]
    t = re.sub(r'#\w+', '', t).strip(' ·-|')
    if len(t) > 70:
        t = t[:67].rsplit(' ', 1)[0] + '…'
    return t or 'Ver en Instagram'


def main():
    token = os.environ.get('IG_TOKEN', '').strip()
    if not token:
        print('Sin IG_TOKEN: no se actualiza Instagram.')
        return 0
    try:
        new = get(f'{API}/refresh_access_token', grant_type='ig_refresh_token', access_token=token).get('access_token')
        if new and new != token:
            print('Token renovado (guárdalo si lo gestionas a mano).')
            token = new
    except Exception as e:
        print('No se pudo renovar el token:', e)
    data = get(f'{API}/me/media', fields='id,caption,media_type,media_url,thumbnail_url,permalink,timestamp',
               limit=N, access_token=token).get('data', [])
    if not data:
        print('La API no devolvió publicaciones; se deja todo como estaba.')
        return 1
    from PIL import Image
    imgdir = SRC / 'img' / 'ig'
    imgdir.mkdir(parents=True, exist_ok=True)
    posts = []
    for m in data[:N]:
        pic = m.get('thumbnail_url') if m.get('media_type') == 'VIDEO' else m.get('media_url')
        if not pic:
            continue
        name = re.sub(r'[^\w-]', '', m['permalink'].rstrip('/').rsplit('/', 1)[-1]) or m['id']
        with urllib.request.urlopen(pic, timeout=60) as r:
            im = Image.open(io.BytesIO(r.read())).convert('RGB')
        w, h = im.size
        th = int(w * 5 / 4)
        if h > th:
            top = (h - th) // 2
            im = im.crop((0, top, w, top + th))
        im.thumbnail((540, 675))
        im.save(imgdir / f'{name}.jpg', quality=78, optimize=True, progressive=True)
        posts.append(dict(id=name, tipo='reel' if m.get('media_type') == 'VIDEO' else 'p', url=m['permalink'],
                          img=f'img/ig/{name}.jpg', texto=short(m.get('caption')), fecha=m.get('timestamp', '')[:10]))
    keep = {p['id'] for p in posts}
    for f in imgdir.glob('*.jpg'):
        if f.stem not in keep:
            f.unlink()
    out = dict(actualizado=datetime.date.today().isoformat(), cuenta='almaburgers', publicaciones=posts)
    (SRC / 'data' / 'instagram.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{len(posts)} publicaciones actualizadas.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
