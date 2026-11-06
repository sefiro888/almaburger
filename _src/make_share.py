"""Imagen para compartir el enlace (WhatsApp, Instagram, Facebook…): 1200×630.
   python _src/make_share.py  ->  _src/img/share.jpg"""
import pathlib
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

SRC = pathlib.Path(__file__).parent
IMG = SRC / 'img'
W, H = 1200, 630
CREAM, INK, NAVY = (251, 236, 216), (11, 11, 11), (3, 33, 100)
font = lambda s: ImageFont.truetype(str(SRC / 'fonts' / 'bigshoulders-900.ttf'), s)

im = Image.new('RGB', (W, H), CREAM)
d = ImageDraw.Draw(im)
# trama de puntos suave de fondo
for y in range(10, H, 26):
    for x in range(10 + (y // 26 % 2) * 13, W, 26):
        d.ellipse((x - 1.6, y - 1.6, x + 1.6, y + 1.6), fill=(236, 218, 194))


def card(path, w, h, angle, xy):
    """Foto con borde negro grueso, esquinas redondeadas y sombra dura (el estilo de la web)."""
    ph = ImageOps.fit(Image.open(path).convert('RGB'), (w, h), Image.LANCZOS, centering=(0.5, 0.45))
    b, r = 9, 34
    c = Image.new('RGBA', (w + 2 * b, h + 2 * b), (0, 0, 0, 0))
    m = Image.new('L', c.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, c.width - 1, c.height - 1), r + b, fill=255)
    c.paste(INK + (255,), (0, 0), m)
    mi = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mi).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255)
    c.paste(ph, (b, b), mi)
    sh = Image.new('RGBA', (c.width + 16, c.height + 16), (0, 0, 0, 0))
    sh.paste(INK + (255,), (16, 16), m)
    sh.alpha_composite(c, (0, 0))
    sh = sh.rotate(angle, resample=Image.BICUBIC, expand=True)
    im.paste(sh, xy, sh)


card(IMG / 'tostada.jpg', 250, 330, 7, (930, 150))
card(IMG / 'burger.jpg', 300, 390, -5, (690, 70))

# logo nuevo
logo = Image.open(SRC / 'themes' / 'negro' / 'img' / 'logo-big.png').convert('RGBA')
logo.thumbnail((560, 420), Image.LANCZOS)
im.paste(logo, (58, 52), logo)

# textos
y = 52 + logo.height + 22
d.text((64, y), 'BURGERS CON ALMA · DESAYUNOS CON PASIÓN', font=font(38), fill=INK)
pill = 'KALE NAGUSIA 42 · ORDIZIA'
f2 = font(30)
tw = d.textlength(pill, font=f2)
d.rounded_rectangle((60, y + 62, 60 + tw + 44, y + 62 + 52), 26, fill=INK)
d.text((82, y + 69), pill, font=f2, fill=CREAM)
f3 = font(30)
d.text((60 + tw + 66, y + 69), 'ABRIMOS A LAS 8:00', font=f3, fill=INK)

# mascota delante de las fotos
m = Image.open(IMG / 'mascot.png').convert('RGBA')
m = m.resize((250, round(m.height * 250 / m.width)), Image.LANCZOS)
im.paste(m, (850, H - m.height - 6), m)
dog = Image.open(IMG / 'hotdog.png').convert('RGBA')
dog.thumbnail((170, 170), Image.LANCZOS)
im.paste(dog, (W - dog.width - 18, H - dog.height - 8), dog)

im.save(IMG / 'share.jpg', quality=86, optimize=True, progressive=True)
print('share.jpg', (IMG / 'share.jpg').stat().st_size // 1024, 'KB')
