"""Genera los recursos de cada color a partir del logo nuevo y de la mascota.
   python _src/make_theme_assets.py  ->  _src/themes/{negro,azul}/img/..."""
import pathlib
import numpy as np
from PIL import Image, ImageFilter

SRC = pathlib.Path(__file__).parent
IMG = SRC / 'img'
OUT = SRC / 'themes'
CREAM = (251, 236, 216)
INKS = {'negro': (11, 11, 11), 'azul': (3, 33, 100)}

alpha = Image.open(IMG / 'logo-black.png').getchannel('A')      # forma del logo (1115x810)
alpha = alpha.point(lambda v: 0 if v < 28 else min(255, int((v - 28) * 255 / 200)))   # limpia restos del fondo


def occluder(ink, scale=1200):
    """Logo + contorno crema: tapa a la mascota cuando pasa por detrás de las letras."""
    k = scale / alpha.width
    a = alpha.resize((scale, int(alpha.height * k)), Image.LANCZOS)
    pad = 24
    big = Image.new('L', (a.width + pad * 2, a.height + pad * 2), 0)
    big.paste(a, (pad, pad))
    halo = big.filter(ImageFilter.MaxFilter(25)).filter(ImageFilter.GaussianBlur(1.2))
    im = Image.new('RGBA', big.size, CREAM + (0,))
    im.putalpha(halo)
    ink_l = Image.new('RGBA', big.size, ink + (0,))
    ink_l.putalpha(big)
    im.alpha_composite(ink_l)
    return im, pad / k                                            # imagen y margen en unidades del logo original


def save_q(im, path):
    """PNG con paleta (el logo tiene muy pocos colores): pesa mucho menos y se ve igual."""
    im.quantize(colors=48, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(path, optimize=True)


def tint(path, ink):
    """Pasa un dibujo en negro/crema a tinta/crema conservando la transparencia."""
    im = Image.open(path).convert('RGBA')
    a = np.asarray(im).astype(float)
    lum = a[..., :3].mean(2, keepdims=True) / 255.0
    ink_a, cream_a = np.array(ink, float), np.array(CREAM, float)
    rgb = ink_a + (cream_a - ink_a) * lum
    a[..., :3] = rgb
    return Image.fromarray(a.clip(0, 255).astype('uint8'), 'RGBA')


for theme, ink in INKS.items():
    d = OUT / theme / 'img'
    d.mkdir(parents=True, exist_ok=True)
    occ, pad = occluder(ink)
    save_q(occ, d / 'logo-stage.png')
    lg = Image.new('RGBA', alpha.size, ink + (0,)); lg.putalpha(alpha)
    small = lg.copy(); small.thumbnail((560, 560), Image.LANCZOS); save_q(small, d / 'logo.png')
    big = lg.copy(); big.thumbnail((1100, 1100), Image.LANCZOS); save_q(big, d / 'logo-big.png')
    if theme == 'azul':
        for f in ('mascot.png', 'mascot-body.png', 'mascot-legL.png', 'mascot-legR.png', 'favicon.png'):
            tint(IMG / f, ink).save(d / f, optimize=True)
        (d / 'ill').mkdir(exist_ok=True)
        for f in ('alma', 'carta', 'desayunos', 'galeria', 'visitanos'):
            tint(IMG / 'ill' / f'{f}.png', ink).save(d / 'ill' / f'{f}.png', optimize=True)
        tint(IMG / 'hotdog.png', ink).save(d / 'hotdog.png', optimize=True)
    print(theme, occ.size, round(pad, 1))
cr = Image.new('RGBA', alpha.size, CREAM + (0,)); cr.putalpha(alpha); cr.thumbnail((900, 900), Image.LANCZOS)
save_q(cr, IMG / 'logo-cream.png')
