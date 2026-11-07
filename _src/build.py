"""Genera las dos versiones de la web (multipágina) a partir de la misma base.
   python _src/build.py  ->  opcion-1-color/  y  opcion-2-fiel-logo/  (+ index.html selector en la raíz)"""
import shutil, pathlib, json, os, subprocess

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
THEMES = {
    'opcion-1-color':     dict(css='theme-color.css', name='Opción 1 · Color', other='opcion-2-fiel-logo', tcolor='#1a00ad'),
    'opcion-2-fiel-logo': dict(css='theme-fiel.css',  name='Opción 2 · Fiel al logo', other='opcion-1-color', tcolor='#0b0b0b'),
}
PAGES = [('el-alma.html', 'El alma', 'alma'), ('carta.html', 'Hamburguesas', 'carta'), ('desayunos.html', 'Desayunos', 'desayunos'),
         ('galeria.html', 'Galería', 'galeria'), ('visitanos.html', 'Visítanos', 'visitanos')]
JE = 'https://www.just-eat.es/restaurants-alma-burger-ordizia/menu'
import hashlib
# versión para evitar la caché: cambia solo si cambian los estilos o el JS
VER = hashlib.md5(b''.join((SRC / f).read_bytes() for f in ('app.js', 'base.css', 'pedido-v2.css', 'theme-fiel.css', 'theme-navy.css'))).hexdigest()[:8]


def rig(w=150, extra=''):
    return (f'<div class="rig {extra}" style="--w:{w}px" aria-hidden="true"><div class="bob">'
            '<img class="legL" src="img/mascot-legL.png" alt=""><img class="legR" src="img/mascot-legR.png" alt="">'
            '<img class="body" src="img/mascot-body.png" alt=""></div></div>')


def walker(w=100, t=26):
    return (f'<div class="walker" aria-hidden="true" style="--w:{w}px;--t:{t}s"><div class="walker__x">'
            f'<div class="walker__flip">{rig(w)}</div></div></div>')


def nav(active):
    links = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{t}</a>' for h, t, k in PAGES)
    return f'''<header class="nav" id="nav">
  <a class="nav__logo" href="index.html" aria-label="ALMA Burger &amp; Breakfast, inicio">{rig(46, 'rig--still')}<img class="nav__logoimg" src="img/logo.png" alt="ALMA Burger &amp; Breakfast" width="112" height="81"></a>
  <nav class="nav__links" aria-label="Principal">{links}</nav>
  <div class="nav__actions">
    <button class="cartbtn" id="cartOpen" aria-label="Abrir mi pedido "><span class="cartbtn__t">Pedido</span><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 8h14l-1.2 11H6.2L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><span class="cartbtn__n" id="cartCount">0</span></button>
    <button class="btn btn--solid btn--sm nav__wa" type="button" data-wa-order>Pedir por WhatsApp</button>
    <a class="langbtn" href="__LANGHREF__" hreflang="__LANGCODE__" lang="__LANGCODE__" aria-label="__LANGLABEL__" title="__LANGLABEL__"><span aria-hidden="true">__LANGFROM__</span><b>__LANGTXT__</b></a>
    <button class="burger" id="burgerBtn" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>'''


CTA = f'''<section class="sec cta" style="padding-bottom:140px;border-top:var(--bw) solid var(--ink)">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:26px;justify-content:space-between;align-items:center">
    <h2 class="sec__title reveal" style="margin:0">¿Desayuno o <em>hamburguesa</em>?</h2>
    <div class="btnrow reveal" style="margin:0">
      <button class="btn btn--solid" type="button" data-wa-order>Pedir por WhatsApp</button>
      <a class="btn" href="carta.html">Hamburguesas</a>
      <a class="btn" href="desayunos.html">Desayunos</a>
    </div>
  </div>
</section>'''

FOOT = f'''<footer class="foot">
  {walker(96, 30)}
  <img class="foot__word" src="img/logo-cream.png" alt="ALMA Burger &amp; Breakfast">
  <div class="foot__grid">
    <div><h3>No es solo comida. Es ALMA.</h3><p>Hamburguesas, desayunos, cafés especiales y postres en el corazón de Ordizia. Todo lo que somos, en cada bocado.</p></div>
    <div><h3>Explora</h3><ul><li><a href="index.html">Inicio</a></li>{''.join(f'<li><a href="{h}">{t}</a></li>' for h, t, k in PAGES)}</ul></div>
    <div><h3>Contacto</h3><ul><li>Kale Nagusia 42, 20240 Ordizia</li><li><a href="tel:+34747486092">747 48 60 92</a></li>
      <li><a href="https://wa.me/34747486092" target="_blank" rel="noopener">WhatsApp</a></li>
      <li><a href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">Instagram @almaburgers</a></li></ul></div>
  </div>
  <div class="foot__row"><p>© <span class="yr"></span> Alma Burger · Consulta nuestra carta de alérgenos al personal</p><p><a href="__SWAP__">__SWAPNAME__</a> · Demo de diseño web</p></div>
  <nav class="foot__legal" aria-label="Información legal"><a href="aviso-legal.html">Aviso legal</a><a href="privacidad.html">Privacidad</a><a href="cookies.html">Cookies</a><button type="button" class="lnk" data-cookies>Configurar cookies</button></nav>
</footer>'''

CART = f'''<aside class="cart" id="cart" aria-hidden="true" aria-label="Mi pedido">
  <div class="cart__head"><h2>Mi pedido</h2><button id="cartClose" type="button" aria-label="Cerrar pedido">✕</button></div>
  <div class="cart__scroll">
    <div class="cart__empty" id="cartEmpty"><img src="img/mascot.png" alt="" width="110"><p><b>Tu pedido está vacío</b></p><p>Pulsa <b>+</b> en cualquier plato de la carta.</p>
      <div class="btnrow" style="justify-content:center;margin:14px 0 0"><a class="btn btn--solid btn--sm" href="carta.html">Ver la carta</a><button class="btn btn--sm" type="button" data-surprise>Sorpréndeme</button></div>
      <p class="hint" style="margin-top:14px">Pedidos por WhatsApp para recoger o a domicilio.</p></div>
    <ul class="cart__list" id="cartList" hidden></ul>
    <form class="checkout" id="checkout" hidden>
      <h3>Tus datos</h3>
      <fieldset class="seg seg--2"><legend>¿Cómo lo quieres?</legend>
        <label><input type="radio" name="tipo" value="recoger" checked><span>Recoger en el local</span></label>
        <label><input type="radio" name="tipo" value="domicilio"><span>A domicilio</span></label></fieldset>
      <div class="form__row"><label>Nombre<input name="nombre" required autocomplete="name" placeholder="Tu nombre"></label><label>Teléfono<input name="tel" type="tel" required autocomplete="tel" inputmode="tel" placeholder="6XX XX XX XX"></label></div>
      <label id="fDir" hidden>Dirección de entrega<input name="direccion" autocomplete="street-address" placeholder="Calle, número, piso"></label>
      <p class="hint" id="domNote" hidden>El local te confirmará por WhatsApp si llegamos a tu dirección y el coste del envío.</p>
      <div class="form__row"><label id="lCuando">¿Cuándo lo recoges?<select name="cuando"><option value="asap">Lo antes posible</option><option value="hora">A una hora concreta</option></select></label>
        <label id="fHora" hidden>Hora<input type="time" name="hora"></label></div>
      <label>Alergias o intolerancias<input name="alergias" maxlength="140" placeholder="Gluten, lactosa, frutos secos…"></label>
      <label>Notas del pedido<textarea name="notas" rows="2" maxlength="240" placeholder="Algo más que debamos saber"></textarea></label>
      <p class="hint warn" id="closedNote" hidden></p>
    </form>
  </div>
  <div class="cart__foot" id="cartFoot" hidden>
    <div class="cart__total"><span>Total</span><b id="cartTotal">0,00€</b></div>
    <button class="btn btn--solid btn--block" type="submit" form="checkout">Enviar pedido por WhatsApp</button>
    <div class="cart__alt"><button class="lnk" id="cartClear" type="button">Vaciar pedido</button></div>
    <p><b>Pago por Bizum:</b> el local te confirmará el pedido y el total, y te indicará cómo hacer el Bizum. Se abrirá WhatsApp con tu pedido ya escrito.</p>
  </div>
</aside>
<div class="scrim" id="scrim"></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<button class="orderbar" id="orderbar" type="button" hidden><span class="orderbar__n" id="orderbarN">0</span><span>Ver mi pedido</span><b id="orderbarT">0,00€</b></button>
<div class="progress" id="progress" aria-hidden="true"></div>
<a class="wa" href="https://wa.me/34747486092" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.6-4.8A9 9 0 1 1 8 19.5L3 21Z"/><path d="M9 10c0 2.800 2.200 5 5 5l1.200-1.300-1.800-1-.8.700a4 4 0 0 1-1.700-1.700l.7-.8-1-1.800L9 10Z" fill="currentColor" stroke="none"/></svg></a>'''




import re as _re
CFG = json.loads((SRC / 'config.json').read_text(encoding='utf-8')) if (SRC / 'config.json').exists() else {}
DEMO = os.environ.get('ALMA_DEMO') == '1'
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('legal', SRC / 'legal.py'); LEGAL = _ilu.module_from_spec(_spec); _spec.loader.exec_module(LEGAL)
AGORA = 'simulacion.html' if DEMO else (CFG.get('agora_url') or '').strip()
_spec3 = _ilu.spec_from_file_location('i18n_eu', SRC / 'i18n_eu.py'); EUD = _ilu.module_from_spec(_spec3); _spec3.loader.exec_module(EUD)
_spec2 = _ilu.spec_from_file_location('imgopt', SRC / 'imgopt.py'); IMGOPT = _ilu.module_from_spec(_spec2); _spec2.loader.exec_module(IMGOPT)
LCFG = dict(CFG.get('legal', {}), _agora=bool(AGORA))


def agora(html):
    """Con enlace de Ágora: los botones de pedir pasan a «Pedir online» y apuntan a Ágora."""
    if not AGORA:
        return html
    u = AGORA.replace('&', '&amp;').replace('"', '&quot;')
    html = _re.sub(r'<button class="([^"]*)" type="button" data-wa-order[^>]*>.*?</button>',
                   lambda m: f'<a class="{m.group(1)}" href="{u}" target="_blank" rel="noopener">Pedir online ↗</a>', html, flags=_re.S)
    html = _re.sub(r'<button class="([^"]*)" type="button" data-add="[^"]*">[^<]*</button>', lambda m: f'<a class="{m.group(1)}" href="{u}" target="_blank" rel="noopener">Pedir online ↗</a>', html)
    html = _re.sub(r'<button class="lnk"[^>]*data-wa-order[^>]*>.*?</button>', f'<a class="lnk" href="{u}" target="_blank" rel="noopener" style="color:var(--dark-pop);font-size:1rem">Pedir online ↗</a>', html, flags=_re.S)
    rep = [
        ('<span class="path__tag">Recoger o domicilio</span><b>Por WhatsApp</b><span>Arma tu pedido aquí y envíalo en un toque. El local te confirma el total y cómo pagar por Bizum.</span>',
         '<span class="path__tag">Recoger o domicilio</span><b>Pedir online</b><span>Elige tus platos, para recoger o a domicilio. Llega directo a la cocina. De momento, el pago se hace en el local.</span>'),
        ('<h3>3 · Envía y paga por Bizum</h3><p>Se abre WhatsApp con el pedido escrito. Te confirmamos el total, haces el Bizum y lo preparamos.</p>',
         '<h3>3 · Confirma y listo</h3><p>Terminas el pedido en nuestra página de pedidos y llega directo a la cocina.</p>'),
        ('<h3>2 · Completa tus datos</h3><p>Nombre, teléfono, si lo recoges o lo llevamos a casa, y tus alergias. Puedes añadir notas a cada plato.</p>',
         '<h3>2 · Completa tus datos</h3><p>Nombre, teléfono, si lo recoges o lo llevamos a casa, y la hora.</p>'),
        ('Pulsa <b>+</b> en la carta. Si un plato tiene opciones (salsa, relleno…), te las preguntamos.', 'Mira la carta y entra en «Pedir online». Allí eliges los platos con sus opciones.'),
        ('<span class="jebar__txt">Recoger o a domicilio · pago por Bizum</span>', '<span class="jebar__txt">Recoger o a domicilio</span>'),
        ('Sí. Haz tu pedido en la web, elige «A domicilio» y se enviará por WhatsApp. El local te confirmará si llegamos a tu dirección y el coste del envío. También puedes pedir en Just Eat.',
         'Sí, por la noche: miércoles, jueves y domingo de 19:30 a 23:00, y viernes y sábado de 19:30 a 23:30. Pulsa «Pedir online», elige «A domicilio» y pon tu dirección. Los desayunos no tienen reparto.'),
    ]
    rep.append(('Pide por WhatsApp.', 'Pide online.'))
    for a, b in rep:
        html = html.replace(a, b)
    # el acceso «Pedido» de la barra inferior pasa a enlazar con Ágora
    html = _re.sub(r'<button type="button" id="bnavCart">(.*?)</button>', lambda m: f'<a id="bnavCart" href="{u}" target="_blank" rel="noopener">' + m.group(1).replace('id="bnavT">Pedido', 'id="bnavT">Pedir online') + '</a>', html, flags=_re.S)
    if DEMO:
        html = html.replace('<body>', '<body>\n<div class="demobar">PRUEBA · Así funcionará con Ágora. «Pedir online» lleva a una simulación del pedido.</div>', 1)
    html = html.replace('<head>', '<head>\n<script>window.ALMA_AGORA="' + AGORA.replace('"', '') + '";document.documentElement.dataset.agora="on"</script>', 1)
    return html




def chapters(html):
    """Cada título de sección lleva su número en contorno, como en «El alma»."""
    pat = _re.compile(r'(<p class="kicker[^"]*">(?:(?!</p>).)*</p>\s*)?(<h2 class="sec__title[^>]*>.*?</h2>)', _re.S)
    n = [html.count('class="chap__n')]
    html = html.replace('<h2 class="sec__title reveal" style="margin:0">¿Desayuno o <em>hamburguesa</em>?</h2>', '<h2 class="sec__title reveal" data-nonum="1" style="margin:0">¿Desayuno o <em>hamburguesa</em>?</h2>')

    def sub(m):
        if 'chap__n' in html[max(0, m.start() - 90):m.start()] or 'data-nonum' in m.group(2) or 'class="cta"' in html[max(0, m.start() - 400):m.start()]:
            return m.group(0)
        n[0] += 1
        return f'<div class="chap__head chap__head--auto"><span class="chap__n reveal" aria-hidden="true">{n[0]:02d}</span><div>{m.group(1) or ""}{m.group(2)}</div></div>'
    return pat.sub(sub, html)

def shell(*a, **k):
    return agora(chapters(_shell(*a, **k)))


def _shell(active, title, desc, body, tcolor, og='img/burger.jpg'):
    HOMEA = ' aria-current="page"' if active == 'home' else ''
    CARTAA = ' aria-current="page"' if active == 'carta' else ''
    DESAA = ' aria-current="page"' if active == 'desayunos' else ''
    return f'''<!doctype html>
<html lang="es" data-font="shoulders" data-all="on">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{tcolor}">
__OGBLOCK__
<link rel="icon" type="image/png" href="img/favicon.png">
<script>/* momento del día en Ordizia: desayunos hasta las 12:00 (de lunes a viernes desde las 8, fin de semana desde las 9; para probar: ?hora=9) */try{{var d=new Date(new Date().toLocaleString("en-US",{{timeZone:"Europe/Madrid"}})),h=d.getHours(),w=d.getDay(),q=location.search.match(/[?&]hora=(\\d+)/);if(q)h=+q[1];document.documentElement.dataset.momento=h>=(w%6?8:9)&&h<12?"desayuno":"burger"}}catch(e){{}}</script>
<link rel="preload" href="fonts/bigshoulders-latin.woff2" as="font" type="font/woff2" crossorigin>
{'<link rel="preload" href="img/logo-stage.png" as="image" fetchpriority="high">' if active == 'home' else ''}
<link rel="stylesheet" href="styles.css?v={VER}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Restaurant","name":"Alma Burger","url":"https://almaburgers.com","telephone":"+34747486092","servesCuisine":["Hamburguesas","Desayunos","Postres"],"priceRange":"€€","address":{{"@type":"PostalAddress","streetAddress":"Kale Nagusia 42","postalCode":"20240","addressLocality":"Ordizia","addressRegion":"Gipuzkoa","addressCountry":"ES"}},"geo":{{"@type":"GeoCoordinates","latitude":43.054023,"longitude":-2.178607}},"sameAs":["https://www.instagram.com/almaburgers/"]}}</script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{nav(active)}
<main id="contenido">
{body}
</main>
{CTA}
{FOOT}
{CART}
<nav class="bnav" aria-label="Acceso rápido">
  <a href="carta.html"{CARTAA}><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11a8 6 0 0 1 16 0Z"/><path d="M3 15h18"/><path d="M5 19h14a2 2 0 0 0 2-2H3a2 2 0 0 0 2 2Z"/></svg><span>Burgers</span></a>
  <a href="desayunos.html"{DESAA}><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5Z"/><path d="M17 11h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 3v3M12 3v3"/></svg><span>Desayunos</span></a>
  <button type="button" id="bnavCart"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 8h14l-1.2 11H6.2L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><span id="bnavT">Pedido</span><i id="bnavN" hidden>0</i></button>
  <a href="visitanos.html#contacto"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4Z"/><path d="M8 9h8M8 12h5"/></svg><span>Contacto</span></a>
</nav>
<script src="app.js?v={VER}"></script>
</body>
</html>'''


def phero(crumb, h1, lead, pic=None, pic_alt='', dark=False, ill=None, ill_alt=''):
    if ill:
        pic = None
    p = f'<figure class="phero__pic reveal"><img src="img/{pic}" alt="{pic_alt}"></figure>' if pic else ''
    if ill:
        p = f'<figure class="phero__ill reveal"><img src="img/ill/{ill}.png" alt="{ill_alt}"></figure>'
    return f'''<section class="phero{' phero--dark' if dark else ''}{' phero--pic' if pic or ill else ''}{' phero--ill' if ill else ''}">
  <div class="wrap">
    <nav class="crumbs" aria-label="Migas de pan"><a href="index.html">Inicio</a><span>/</span><span>{crumb}</span></nav>
    <h1 class="reveal">{h1}</h1>
    <p class="lead reveal">{lead}</p>
    {p if ill else ''}
  </div>
  {'' if ill else p}
  <div class="phero__line"></div>
  {walker(104, 24)}
</section>'''


# ---------------------------------------------------------------- páginas
STAGE = (SRC / 'stage.svg.html').read_text(encoding='utf-8')


IG = ''.join(f'<a class="ig reveal" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><img src="img/{f}" alt="" loading="lazy"></a>' for f in ['burger.jpg', 'picoteo.jpg', 'pancake.jpg', 'trufadas.jpg', 'matcha-2.jpg', 'tostada.jpg'])




VIDEOS = [  # (archivo, descripción accesible, pie)
    ('burger', 'Vídeo desde la cocina de ALMA: una burger con queso fundido', 'Desde la cocina de ALMA'),
    ('desayunos', 'Desayunos con pasión: tostada de salmón, pancakes y matcha', 'Desayunos con pasión'),
    ('chocolate', 'Chocolate caliente servido en una taza de ALMA', 'Llega el chocolate caliente'),
    ('croquetas', 'Croquetas caseras de ALMA, recién abiertas', 'Croquetas caseras'),
    ('halloween', 'Halloween en ALMA: calabazas, arañas y máscaras', 'This is Halloween en ALMA'),
    ('oscuro', 'Algo muy oscuro: la burger negra de Halloween', 'Algo muy oscuro se cocina…'),
]


def phones(n=None):
    def one(f, label, cap):
        return (f'''<figure class="phone phone--own reveal"><div class="phone__bezel"><span class="phone__notch" aria-hidden="true"></span><div class="phone__screen">
      <video class="phone__video" muted loop playsinline preload="none" poster="img/video/{f}-poster.jpg" aria-label="{label}"><source src="img/video/{f}.mp4" type="video/mp4"></video>
      <span class="phone__play" aria-hidden="true">▶</span></div><span class="phone__bar" aria-hidden="true"></span></div>
      <figcaption>{cap}</figcaption></figure>''')
    vs = VIDEOS[:n] if n else VIDEOS
    return (f'<div class="phones phones--rail" tabindex="0" aria-label="Vídeos de ALMA, desliza para ver más">{"".join(one(*v) for v in vs)}</div>'
            '<p class="phones__hint" aria-hidden="true">← Desliza para ver más vídeos →</p>')


IGDATA = json.loads((SRC / 'data' / 'instagram.json').read_text(encoding='utf-8'))


def igposts(n=12):
    """Últimas publicaciones de Instagram (data/instagram.json, se actualiza con update_instagram.py)."""
    def esc(t):
        return t.replace('&', '&amp;').replace('<', '&lt;').replace('"', '&quot;')
    out = ''
    for p in IGDATA['publicaciones'][:n]:
        kind = '<span class="igp__k">▶ Reel</span>' if p['tipo'] == 'reel' else ''
        out += (f'<a class="igp reveal" href="{esc(p["url"])}" target="_blank" rel="noopener" aria-label="Ver en Instagram: {esc(p["texto"])}">'
                f'<img src="{esc(p["img"])}" alt="" loading="lazy" width="540" height="675">{kind}<span class="igp__t">{esc(p["texto"])}</span></a>')
    return f'<div class="igposts">{out}</div>'


def home():
    marq = ''.join(f'<span>{t}</span><i>✶</i>' for t in ['Smash burgers', 'Desayunos', 'Picoteo', 'Tostadas', 'Hot dogs', 'Pancakes', 'Tartas de queso', 'Matcha', 'Café de especialidad'])
    return f'''<section class="hero">
  <div class="hero__copy">
    <p class="eyebrow"><span class="dot"></span><span id="openStatus">Hamburguesería · Ordizia</span></p>
    <h1 class="sr-only">Alma Burger</h1>
    <div class="stagewrap">{STAGE}<div class="stage__dots" id="stageDots" role="group" aria-label="Elegir la entrada de la mascota"></div></div>
    <p class="hero__lead m-bur">No es solo comida. Es <em>ALMA</em>. Hamburguesas de recetas propias y desayunos con personalidad: dos formas de disfrutar el mismo sabor.</p>
    <p class="hero__lead m-des">Buenos días. Es hora de <em>desayunar</em>: tostadas con toppings de verdad, pancakes, matcha y café de especialidad hasta las 12:00. Y a mediodía, hamburguesas con ALMA.</p>
    <div class="hero__cta">
      <button class="btn btn--solid" type="button" data-wa-order>Pedir por WhatsApp</button>
      <a class="btn" href="carta.html">Ver la carta</a>
    </div>
    <p class="hero__alt"><a href="carta.html">Ver hamburguesas</a> · <a href="desayunos.html">Ver desayunos</a> · <a href="tel:+34747486092">747 48 60 92</a></p>
    <ul class="hero__facts"><li><b>17</b> hamburguesas</li><li><b>41</b> desayunos y bebidas</li><li><b>8:00</b> abrimos con café</li></ul>
  </div>
  <div class="hero__visual" id="heroVisual">
    <div class="blob"></div>
    <figure class="hero__photo hero__photo--white"><img src="img/dishes/la-reinita.jpg" alt="La Reinita, la burger del mes: smash con panceta y topping de reina pepiada" fetchpriority="high"><a class="hero__tag" href="carta.html#hamburguesas">Burger del mes · La Reinita</a></figure>
    <figure class="hero__photo hero__photo--b"><img src="img/tostada.jpg" alt="Tostada de salmón, aguacate y hummus de remolacha"><a class="hero__tag hero__tag--b" href="desayunos.html">Desayunos · hasta las 12:00</a></figure>
    <svg class="sticker" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="circ" d="M100,100 m-72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"/></defs><circle cx="100" cy="100" r="96"/><text><textPath href="#circ" font-size="17" font-weight="800" textLength="440" lengthAdjust="spacing">HAMBURGUESAS · DESAYUNOS · ALMA · </textPath></text><text x="100" y="118" text-anchor="middle" font-size="62" font-family="Bagel Fat One">✶</text></svg>
  </div>
  <div class="heroline" aria-hidden="true">{walker(112, 22)}</div>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee__track">{marq}{marq}</div></div>

<section class="sec duosec" id="dos-caras">
  <div class="wrap">
    <p class="kicker reveal">Dos formas de disfrutar ALMA</p>
    <h2 class="sec__title reveal">Hamburguesas <em>y desayunos</em></h2>
    <div class="duo">
      <a class="dcard dcard--b reveal" href="carta.html">
        <img src="img/dishes/la-puerquita.jpg" alt="La Puerquita, doble smash con pulled pork" loading="lazy">
        <div class="dcard__in"><span class="dcard__tag">Del mediodía a la noche</span><h3>Hamburguesas</h3>
          <p>Smash burgers de recetas propias, pollo crispy, hot dogs, picoteo y tartas de queso.</p><span class="dcard__go">Ver hamburguesas →</span></div>
      </a>
      <a class="dcard dcard--d reveal" href="desayunos.html">
        <img src="img/tostada.jpg" alt="Tostada de salmón, aguacate y hummus de remolacha" loading="lazy">
        <div class="dcard__in"><span class="dcard__tag">Hasta las 12:00</span><h3>Desayunos</h3>
          <p>Tostadas con toppings de verdad, pancakes, bowls, cafés especiales y los matchas del momento.</p><span class="dcard__go">Ver desayunos →</span></div>
      </a>
    </div>
  </div>
</section>

<section class="sec sec--dark hstory" id="historia">
  <div class="wrap hstory__grid">
    <div class="hstory__pics">
      <figure class="hp hp--1 reveal"><img src="img/dishes/la-puerquita.jpg" alt="La Puerquita, doble smash con pulled pork" loading="lazy"></figure>
      <figure class="hp hp--2 reveal"><img src="img/dishes/tostada-salmon.jpg" alt="Tostada de salmón con aguacate" loading="lazy"></figure>
      <figure class="hp hp--3 reveal"><img src="img/dishes/pancakes-ferrero.jpg" alt="Pancakes con crema de Ferrero Rocher" loading="lazy"></figure>
      <svg class="hp__stamp" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="c2" d="M100,100 m-72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"/></defs><circle cx="100" cy="100" r="96"/><text><textPath href="#c2" font-size="17" font-weight="800" textLength="440" lengthAdjust="spacing">ALMA · TODO LO QUE SOMOS · EN CADA BOCADO · </textPath></text><text x="100" y="116" text-anchor="middle" font-size="58" font-family="Bagel Fat One">A</text></svg>
    </div>
    <div class="hstory__text">
      <p class="kicker kicker--dark reveal">Nuestra historia</p>
      <h2 class="sec__title reveal">No es solo comida. <em>Es ALMA.</em></h2>
      <p class="hstory__lead reveal">ALMA no es simplemente el nombre de nuestra hamburguesería. Es una parte de nosotros, de nuestras raíces y de nuestra familia.</p>
      <p class="reveal">Cada letra tiene un significado especial:</p>
      <div class="letters reveal"><div><b>A</b><span>Abrahan</span></div><div><b>L</b><span>Lidia</span></div><div><b>M</b><span>Moreno, apellido del padre de Lidia</span></div><div><b>MA</b><span>Maritza, madre de Abrahan</span></div></div>
      <div class="hstory__more" id="hmore"><p>De la unión de nuestros nombres y nuestras raíces nació ALMA, un proyecto que representa nuestra ilusión por emprender juntos y crear algo propio.</p>
        <p>Queríamos construir mucho más que una hamburguesería. Un lugar con personalidad, donde la creatividad, los sabores atrevidos y las ganas de sorprender estuvieran presentes en cada detalle.</p>
        <p>En ALMA nos gusta salir de lo convencional, experimentar con nuevas combinaciones y ofrecer experiencias diferentes, desde nuestras hamburguesas más originales hasta nuestros desayunos, cafés especiales y nuevas creaciones.</p>
        <p class="hstory__end">ALMA nació de nuestras raíces, creció con nuestros sueños y hoy queremos compartirla contigo.</p></div>
      <div class="btnrow reveal" style="margin-top:22px"><button class="btn btn--cream" type="button" id="hmoreBtn" aria-expanded="false" aria-controls="hmore">Seguir leyendo ↓</button><a class="btn btn--line" href="el-alma.html">Toda nuestra historia</a></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Hamburguesas · lo más pedido</p><h2 class="sec__title reveal">Para empezar <em>fuerte</em></h2></div>
      <a class="btn btn--solid reveal" href="carta.html">Todas las hamburguesas →</a></div>
    <div class="rail" id="featured"></div>
  </div>
</section>

<section class="sec sec--band">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Desayunos · hasta las 12:00</p><h2 class="sec__title reveal">Desayunos <em>con pasión</em></h2></div>
      <a class="btn btn--solid reveal" href="desayunos.html">Todos los desayunos →</a></div>
    <div class="rail" id="featuredB"></div>
  </div>
</section>

<section class="sec sec--band" id="videos">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Instagram</p><h2 class="sec__title reveal" style="margin:0">ALMA <em>en vídeo</em></h2></div>
      <a class="btn btn--solid reveal" href="galeria.html#reels">Más en la galería →</a></div>
    {phones(4)}
  </div>
</section>

<section class="sec quizband" id="test">
  <div class="wrap quizband__in">
    <div class="quizband__txt"><p class="kicker reveal">Test de 30 segundos</p>
      <h2 class="sec__title reveal">¿Qué burger <em>eres</em>?</h2>
      <p class="reveal">Contesta cinco preguntas y te decimos cuál pedir. Puedes mandarle el resultado a quien quieras.</p>
      <div class="btnrow reveal" style="margin-top:20px"><button class="btn btn--solid" type="button" data-quiz>Hacer el test</button><a class="btn" href="carta.html">Ver todas las burgers</a></div></div>
    <div class="quizband__pic reveal"><img src="img/mascot.png" alt="" loading="lazy"><span>?</span></div>
  </div>
</section>

<section class="sec sec--ink" id="como-pedir">
  <div class="wrap">
    <p class="kicker kicker--dark reveal">Pedir es fácil</p><h2 class="sec__title reveal">Elige cómo <em>quieres pedir</em></h2>
    <div class="paths">
      <div class="path path--main path--wa reveal"><span class="path__tag">Recoger o domicilio</span><b>Por WhatsApp</b><span>Arma tu pedido aquí y envíalo en un toque. El local te confirma el total y cómo pagar por Bizum.</span><button class="btn btn--solid" type="button" data-wa-order>Empezar mi pedido</button></div>
      <div class="path reveal"><span class="path__tag">Dudas</span><b>Escríbenos</b><span>¿Alguna pregunta sobre la carta, los alérgenos o el horario? Llámanos o mándanos un mensaje.</span><a class="btn btn--line" href="visitanos.html#contacto">Contactar</a></div>
    </div>
    <div class="steps" style="margin-top:52px">
      <div class="step reveal"><h3>1 · Elige tus platos</h3><p>Pulsa <b>+</b> en la carta. Si un plato tiene opciones (salsa, relleno…), te las preguntamos.</p></div>
      <div class="step reveal"><h3>2 · Completa tus datos</h3><p>Nombre, teléfono, si lo recoges o lo llevamos a casa, y tus alergias. Puedes añadir notas a cada plato.</p></div>
      <div class="step reveal"><h3>3 · Envía y paga por Bizum</h3><p>Se abre WhatsApp con el pedido escrito. Te confirmamos el total, haces el Bizum y lo preparamos.</p></div>
    </div>
    <p class="reveal" style="margin-top:26px;text-align:center">¿No sabes qué pedir? <button class="lnk" type="button" data-surprise style="color:var(--dark-pop);font-size:1rem">Sorpréndeme</button></p>
  </div>
</section>

<section class="sec sec--band">
  <div class="wrap split">
    <div class="split__pic reveal"><figure class="ph ph--white" style="inset:0 8% 8% 0;transform:rotate(-3deg)"><img src="img/dishes/la-reinita.jpg" alt="La Reinita, smash con panceta y topping de reina pepiada" loading="lazy"></figure>
      <figure class="ph" style="width:38%;aspect-ratio:1;right:0;bottom:0;transform:rotate(5deg)"><img src="img/dishes/la-puerquita.jpg" alt="La Puerquita, doble smash con pulled pork" loading="lazy"></figure></div>
    <div>
      <p class="kicker reveal">Burger del mes 👑</p>
      <h2 class="sec__title reveal">La <em>Reinita</em></h2>
      <p class="reveal" style="font-size:1.15rem;max-width:30em">Una reina con mucho carácter y sabor venezolano: carne smash jugosa, cheddar bien fundido, panceta crujiente, nuestra salsa ajonesa y la auténtica protagonista, el topping de reina pepiada, con pollo deshilachado, aguacate, cebolla morada, cilantro y una mezcla cremosa irresistible.</p>
      <p class="reveal" style="font-weight:800;margin-top:10px">La Reinita no viene a participar, viene a reinar.</p>
      <div class="btnrow reveal" style="margin-top:26px">
        <button class="btn btn--solid" type="button" data-add="hamburguesas|La Reinita">Añadir a mi pedido +</button>
        <a class="btn" href="https://www.instagram.com/p/DfaM2nTjbD5/" target="_blank" rel="noopener">Verla en Instagram ↗</a></div>
      <p class="fine reveal" style="margin-top:12px;opacity:.75">Y La Puerquita se queda en la carta como novedad.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="kicker reveal">Descubre</p><h2 class="sec__title reveal">Todo Alma, <em>en un vistazo</em></h2>
    <div class="tease" style="margin-top:30px">
      <a class="tz tz--wide reveal" href="carta.html"><img src="img/dishes/la-triplona.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>Hamburguesas y carta</h3><p>Smash burgers, picoteo, bocadillos, hot dogs y postres.</p></div></a>
      <a class="tz tz--wide reveal" href="desayunos.html"><img src="img/tostada.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>Desayunos</h3><p>Tostadas, pancakes, bowls y matcha hasta las 12:00.</p></div></a>
      <a class="tz reveal" href="el-alma.html"><img src="img/cabrona.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>El alma</h3><p>Nuestra historia.</p></div></a>
      <a class="tz reveal" href="galeria.html"><img src="img/picoteo.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>Galería</h3><p>Mejor verlo que contarlo.</p></div></a>
      <a class="tz tz--plain reveal" href="visitanos.html"><span class="tz__go">→</span><div class="tz__in"><h3>Visítanos</h3><p>Kale Nagusia 42, Ordizia.</p></div>{rig(110, 'rig--still')}</a>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Lo último en Instagram</p><h2 class="sec__title reveal" style="margin:0">Últimas <em>publicaciones</em></h2></div>
      <div class="btnrow reveal" style="margin:0"><a class="btn btn--solid btn--sm" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">Instagram ↗</a><a class="btn btn--sm" href="https://www.tiktok.com/@almaburgerss" target="_blank" rel="noopener">TikTok @almaburgerss ↗</a></div></div>
    {igposts(6)}
  </div>
</section>'''


def alma():
    return phero('El alma', 'No es solo comida. <em>Es ALMA.</em>', 'La historia de quienes estamos detrás: nuestras raíces, nuestra familia y las ganas de crear algo propio.', 'dishes/la-cabrona.jpg', 'La Cabrona, doble smash con queso de cabra', ill='alma', ill_alt='La mascota de ALMA, una hamburguesa, abrazando un corazón') + f'''
<nav class="chapnav" aria-label="Capítulos de la historia"><div class="wrap">
  <a href="#nombre">El nombre</a><a href="#origen">El origen</a><a href="#mas">Más que una hamburguesería</a><a href="#convencional">Salir de lo convencional</a><a href="#detras">Detrás de todo</a><a href="#filosofia">Cómo somos</a>
</div></nav>

<section class="chap sec" id="nombre">
  <div class="wrap">
    <div class="chap__head"><span class="chap__n reveal">01</span><div><p class="kicker reveal">El nombre</p>
      <h2 class="sec__title reveal">ALMA no es solo <em>un nombre</em></h2></div></div>
    <p class="chap__lead reveal">ALMA no es simplemente el nombre de nuestra hamburguesería. Es una parte de nosotros, de nuestras raíces y de nuestra familia.</p>
    <p class="chap__p reveal">Cada letra tiene un significado especial:</p>
    <div class="lx">
      <article class="lx__c reveal"><b>A</b><h3>Abrahan</h3></article>
      <article class="lx__c reveal"><b>L</b><h3>Lidia</h3></article>
      <article class="lx__c reveal"><b>M</b><h3>Moreno</h3><p>apellido del padre de Lidia</p></article>
      <article class="lx__c reveal"><b>MA</b><h3>Maritza</h3><p>madre de Abrahan</p></article>
    </div>
  </div>
</section>

<section class="chap sec sec--band" id="origen">
  <div class="wrap chap__split">
    <div>
      <div class="chap__head"><span class="chap__n reveal">02</span><div><p class="kicker reveal">El origen</p>
        <h2 class="sec__title reveal">Nuestros nombres, <em>nuestras raíces</em></h2></div></div>
      <blockquote class="pullq reveal">De la unión de nuestros nombres y nuestras raíces nació ALMA.</blockquote>
      <p class="chap__p reveal">Un proyecto que representa nuestra ilusión por emprender juntos y crear algo propio.</p>
    </div>
    <div class="chap__pics">
      <figure class="ph ph--1 reveal"><img src="img/dishes/la-puerquita.jpg" alt="La Puerquita, doble smash con pulled pork" loading="lazy"></figure>
      <figure class="ph ph--2 reveal"><img src="img/dishes/tostada-salmon.jpg" alt="Tostada de salmón con aguacate" loading="lazy"></figure>
    </div>
  </div>
</section>

<section class="chap sec" id="mas">
  <div class="wrap">
    <div class="chap__head"><span class="chap__n reveal">03</span><div><p class="kicker reveal">Más que una hamburguesería</p>
      <h2 class="sec__title reveal">Un lugar con <em>personalidad</em></h2></div></div>
    <p class="chap__lead reveal">Queríamos construir mucho más que una hamburguesería. Un lugar con personalidad, donde la creatividad, los sabores atrevidos y las ganas de sorprender estuvieran presentes en cada detalle.</p>
    <div class="trio">
      <div class="trio__c reveal"><span>01</span><b>La creatividad</b></div>
      <div class="trio__c reveal"><span>02</span><b>Los sabores atrevidos</b></div>
      <div class="trio__c reveal"><span>03</span><b>Las ganas de sorprender</b></div>
    </div>
    <p class="chap__p reveal" style="text-align:center;margin-inline:auto">Presentes en cada detalle.</p>
  </div>
</section>

<section class="chap sec sec--dark" id="convencional">
  <div class="wrap">
    <div class="chap__head"><span class="chap__n chap__n--l reveal">04</span><div><p class="kicker kicker--dark reveal">Salir de lo convencional</p>
      <h2 class="sec__title reveal">Nuevas combinaciones, <em>experiencias diferentes</em></h2></div></div>
    <p class="chap__lead reveal">En ALMA nos gusta salir de lo convencional, experimentar con nuevas combinaciones y ofrecer experiencias diferentes, desde nuestras hamburguesas más originales hasta nuestros desayunos, cafés especiales y nuevas creaciones.</p>
    <div class="tiles4">
      <a class="t4 reveal" href="carta.html"><img src="img/dishes/la-dori.jpg" alt="" loading="lazy"><span>Hamburguesas más originales</span></a>
      <a class="t4 reveal" href="desayunos.html"><img src="img/dishes/tostada-salmon.jpg" alt="" loading="lazy"><span>Desayunos</span></a>
      <a class="t4 reveal" href="desayunos.html#menu-desayunos"><img src="img/dishes/matcha-2.jpg" alt="" loading="lazy"><span>Cafés especiales</span></a>
      <a class="t4 reveal" href="carta.html#postres"><img src="img/dishes/me-derrito.jpg" alt="" loading="lazy"><span>Nuevas creaciones</span></a>
    </div>
  </div>
</section>

<section class="chap sec" id="detras">
  <div class="wrap">
    <div class="chap__head"><span class="chap__n reveal">05</span><div><p class="kicker reveal">Detrás de todo esto</p>
      <h2 class="sec__title reveal">Lo que nos <em>mueve</em></h2></div></div>
    <div class="words">
      <span class="reveal">Esfuerzo</span><span class="reveal w--o">Dedicación</span><span class="reveal">Ilusión</span><span class="reveal w--o">Y muchísimas ganas de seguir creciendo</span>
    </div>
  </div>
</section>

<section class="chap sec sec--band" id="filosofia">
  <div class="wrap philo">
    <div class="reveal"><p class="kicker">Nuestra filosofía</p>
      <h2 class="sec__title">No queremos ser una hamburguesería <em>más</em></h2>
      <p class="philo__p">Queremos que ALMA tenga identidad propia, que la gente nos recuerde por nuestros sabores, nuestra creatividad y nuestra manera de hacer las cosas.</p></div>
    <div class="reveal"><p class="kicker">Nuestra personalidad de marca</p>
      <ul class="traits"><li>Moderna</li><li>Atrevida</li><li>Creativa</li><li>Cercana</li></ul>
      <p class="philo__p">Pero sin perder nunca nuestra esencia familiar.</p></div>
  </div>
</section>

<section class="sec team" id="equipo">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Las caras de ALMA</p><h2 class="sec__title reveal" style="margin:0">El <em>equipo</em></h2></div>
      <span class="team__demo reveal">Ejemplo · pendiente de fotos y datos reales</span></div>
    <p class="chap__p reveal" style="max-width:40em">Quién está detrás de cada burger y cada café. Aquí irán las fotos del equipo, su puesto y su plato favorito de la carta.</p>
    <div class="team__grid">
      <article class="tm reveal"><figure class="tm__pic"><img src="img/ill/carta.png" alt="" loading="lazy"></figure><h3>Abrahan</h3><p class="tm__role">Cofundador · cocina</p><p class="tm__fav">Su favorita: <b>por confirmar</b></p></article>
      <article class="tm reveal"><figure class="tm__pic"><img src="img/ill/desayunos.png" alt="" loading="lazy"></figure><h3>Lidia</h3><p class="tm__role">Cofundadora · desayunos y sala</p><p class="tm__fav">Su favorito: <b>por confirmar</b></p></article>
      <article class="tm reveal"><figure class="tm__pic"><img src="img/ill/galeria.png" alt="" loading="lazy"></figure><h3>Nombre</h3><p class="tm__role">Plancha y smash burgers</p><p class="tm__fav">Su favorita: <b>por confirmar</b></p></article>
      <article class="tm reveal"><figure class="tm__pic"><img src="img/ill/visitanos.png" alt="" loading="lazy"></figure><h3>Nombre</h3><p class="tm__role">Barra, cafés y matcha</p><p class="tm__fav">Su favorito: <b>por confirmar</b></p></article>
    </div>
    <p class="fine reveal" style="opacity:.7;margin-top:18px">¿Quieres trabajar con nosotros? Escríbenos por <a href="https://wa.me/34747486092" target="_blank" rel="noopener">WhatsApp</a> o pásate por el local.</p>
  </div>
</section>

<section class="sec sec--dark finale">
  <div class="wrap quote">
    <p class="quote__t reveal">«ALMA nació de nuestras raíces, creció con nuestros sueños y hoy queremos compartirla contigo.»</p>
    <p class="quote__s reveal">ALMA — Todo lo que somos, en cada bocado. ♥</p>
    <div class="btnrow reveal" style="justify-content:center;margin-top:26px"><a class="btn btn--cream" href="carta.html">Ver hamburguesas</a><a class="btn btn--line" href="desayunos.html">Ver desayunos</a></div>
  </div>
</section>
''' + f'''
<section class="sec sec--ink">
  <div class="wrap">
    <div class="stats">
      <div class="stat reveal"><b data-stat="burgers"></b><span>hamburguesas en carta</span></div>
      <div class="stat reveal"><b data-stat="desa"></b><span>desayunos y bebidas</span></div>
      <div class="stat reveal"><b data-stat="8:00"></b><span>abrimos con café y desayunos</span></div>
      <div class="stat reveal"><b data-stat="1"></b><span>mascota con gafas</span></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="kicker reveal">El método</p><h2 class="sec__title reveal">¿Qué es una <em>smash burger</em>?</h2>
    <div class="steps" style="margin-top:40px">
      <div class="step reveal"><h3>Una bola de carne</h3><p>Cada burger empieza con una bola de carne que va directa a una plancha muy caliente.</p></div>
      <div class="step reveal"><h3>Se aplasta (smash)</h3><p>Al aplastarla contra la plancha se forma una costra crujiente que concentra todo el sabor.</p></div>
      <div class="step reveal"><h3>Queso y a la mesa</h3><p>Cheddar fundido, tus toppings favoritos y directa del fuego a tu plato.</p></div>
    </div>
  </div>
</section>

<section class="sec sec--band">
  <div class="wrap split">
    <div class="split__pic"><figure class="ph ph--1 reveal"><img src="img/picoteo.jpg" alt="Aros de cebolla, patatas y croquetas" loading="lazy"></figure>
      <figure class="ph ph--2 reveal"><img src="img/matcha-2.jpg" alt="Matcha con leche" loading="lazy"></figure>
      <figure class="ph ph--3 reveal"><img src="img/pancake.jpg" alt="Pancakes de Ferrero" loading="lazy"></figure></div>
    <div><p class="kicker reveal">Más que hamburguesas</p><h2 class="sec__title reveal">De 8:00 de la mañana <em>a la noche</em></h2>
      <p class="reveal" style="font-size:1.1rem;max-width:30em">Empezamos el día con café, tostadas y pancakes, seguimos con bocadillos y hot dogs, y cerramos con smash burgers, picoteo y tartas de queso.</p>
      <div class="btnrow reveal" style="margin-top:24px"><a class="btn btn--solid" href="desayunos.html">Ver desayunos</a><a class="btn" href="carta.html">Ver la carta</a></div></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="kicker reveal">Preguntas frecuentes</p><h2 class="sec__title reveal">Lo que <em>nos preguntáis</em></h2>
    <div class="faq" style="margin-top:30px">
      <details class="reveal"><summary>¿Tenéis opciones vegetarianas?</summary><p>Sí: la Gordi Deluxe tiene opción vegetariana, además de ensalada con burrata, tortilla de patata y varias tostadas. Y cualquier burger se puede adaptar a vegetariana.</p></details>
      <details class="reveal"><summary>¿Y alérgenos?</summary><p>Tenemos carta de alérgenos: pídesela a nuestro equipo y te ayudamos a elegir con tranquilidad.</p></details>
      <details class="reveal"><summary>¿Hacéis entrega a domicilio?</summary><p>Sí. Haz tu pedido en la web, elige «A domicilio» y se enviará por WhatsApp. El local te confirmará si llegamos a tu dirección y el coste del envío. También puedes pedir en Just Eat.</p></details>
      <details class="reveal"><summary>¿Hay menú infantil?</summary><p>Sí: pechuga empanada, lomo o hamburguesa con queso, siempre con patatas y croquetas, por 9,00€.</p></details>
      <details class="reveal"><summary>¿Hasta qué hora hay desayunos?</summary><p>Hasta las 12:00: de lunes a viernes desde las 8:00, y sábado y domingo desde las 9:00. Los lunes y martes solo abrimos para desayunos.</p></details>
    </div>
  </div>
</section>'''


JEBANNER = f'''
<div class="jebar"><div class="wrap jebar__in"><button class="btn btn--solid btn--sm" type="button" data-wa-order>Pedir por WhatsApp</button><span class="jebar__txt">Recoger o a domicilio · pago por Bizum</span></div></div>'''


def carta():
    return phero('Hamburguesas', 'Elige tu <em>perdición</em>', 'Smash burgers, pollo crispy, picoteo, bocadillos, hot dogs y tartas de queso.', ill='carta', ill_alt='Un perrito caliente sonriente leyendo la carta') + '''<div class="duo-switch"><div class="wrap"><a href="carta.html" aria-current="page">Hamburguesas y carta</a><a href="desayunos.html">Desayunos</a></div></div>''' + JEBANNER + '''
<section class="sec sec--dark carta" style="padding-top:30px">
  <div class="wrap">
    <div class="toolbar reveal">
      <label class="search"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input id="q" type="search" placeholder="Busca: cabra, trufa, picante…" aria-label="Buscar en la carta" autocomplete="off"></label>
      <button class="btn btn--line btn--sm" type="button" id="filtersBtn" aria-expanded="false" aria-controls="chips">Filtros</button>
      <button class="btn btn--cream btn--sm" type="button" data-quiz>¿Qué burger eres?</button>
      <button class="btn btn--cream btn--sm" type="button" data-surprise>Sorpréndeme</button>
    </div>
    <div class="tabs" id="tabs" role="tablist" aria-label="Categorías de la carta"></div>
    <div class="chips" id="chips" aria-label="Filtros"></div>
    <div id="menu" class="menu" data-mode="all" aria-live="polite"></div>
    <p class="carta__note">Suplemento por cada ingrediente extra. Consulta nuestra <b>carta de alérgenos</b> al personal. Algunas imágenes son ilustrativas.</p>
  </div>
</section>'''


def desayunos():
    return phero('Desayunos', 'Desayunos <em>con pasión</em>', 'Hasta las 12:00 (de lunes a viernes desde las 8:00; sábado y domingo desde las 9:00). Tostadas, pancakes, bowls, cafés especiales y matcha, hechos con las mismas ganas que nuestras hamburguesas.', 'tostada.jpg', 'Tostada de salmón, aguacate y hummus de remolacha', ill='desayunos', ill_alt='La mascota de ALMA sentada en un taburete con un café') + '''<div class="duo-switch"><div class="wrap"><a href="carta.html">Hamburguesas y carta</a><a href="desayunos.html" aria-current="page">Desayunos</a></div></div>''' + '''
<section class="sec">
  <div class="wrap split">
    <div class="split__pic"><figure class="ph ph--1 reveal"><img src="img/desayuno-capricho.jpg" alt="Pancakes de nutella con fresas" loading="lazy"></figure>
      <figure class="ph ph--2 reveal"><img src="img/matcha-2.jpg" alt="Matcha con leche" loading="lazy"></figure>
      <figure class="ph ph--3 reveal"><img src="img/pancake.jpg" alt="Pancakes de Ferrero Rocher" loading="lazy"></figure></div>
    <div><p class="kicker reveal">Para empezar bien el día</p><h2 class="sec__title reveal">Tostadas, pancakes <em>y matcha</em></h2>
      <p class="reveal">Tostadas con toppings de verdad, pancakes golosos, bowls, zumos, smoothies y unos matchas que no vas a poder dejar de pedir.</p>
      <ul class="dots reveal"><li><span>Espresso</span><i></i><b>1,70€</b></li><li><span>Tostada de salmón y mascarpone</span><i></i><b>7,50€</b></li><li><span>Pancakes de Ferrero</span><i></i><b>6,30€</b></li><li><span>Matcha de mango</span><i></i><b>4,00€</b></li></ul>
    </div>
  </div>
</section>
<section class="sec sec--band">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Los favoritos</p><h2 class="sec__title reveal">Desayunos <em>con pasión</em></h2></div></div>
    <div class="rail" id="featuredB"></div>
  </div>
</section>
<section class="sec sec--dark" style="padding-top:34px" id="menu-desayunos">
  <div class="wrap">
    <div class="carta__head reveal"><h2 class="sec__title" style="margin:0">La carta de <em>desayunos</em></h2>
      <label class="search"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input id="q" type="search" placeholder="Busca: matcha, croissant, salmón…" aria-label="Buscar en desayunos" autocomplete="off"></label></div>
    <div class="tabs" id="tabs" role="tablist" aria-label="Secciones de desayuno"></div>
    <div class="chips" id="chips" aria-label="Filtros"></div>
    <div id="menu" class="menu" data-mode="desayunos" aria-live="polite"></div>
    <p class="carta__note">Desayunos de lunes a viernes de 8:00 a 12:00, y sábado y domingo de 9:00 a 12:00. Consulta nuestra <b>carta de alérgenos</b> al personal.</p>
  </div>
</section>'''


def galeria():
    ig = [('burger.jpg', 'La Puerquita', 'La Puerquita, doble smash con pulled pork'), ('picoteo.jpg', 'Picoteo con alma', 'Aros de cebolla, patatas y croquetas'),
          ('cabrona.jpg', 'Queso de cabra', 'Hamburguesa con queso de cabra y patatas'), ('trufadas.jpg', 'Patatas trufadas', 'Patatas trufadas')]
    des = [('desayuno-capricho.jpg', 'Pancakes de Nutella', 'Pancakes de nutella con fresas'), ('tostada.jpg', 'Tostada de salmón', 'Tostada de salmón, aguacate y hummus de remolacha'),
           ('pancake.jpg', 'Pancakes de Ferrero', 'Pancakes con crema de Ferrero Rocher'), ('matcha-2.jpg', 'Matcha goloso', 'Matcha con leche en vaso'),
           ('desayuno-revuelto.jpg', 'Desayuno con pasión', 'Huevos revueltos con tomate, tostada y hummus de remolacha')]
    d = ''.join(f'<figure class="mi reveal"><img src="img/{f}" alt="{alt}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c, alt in des)
    a = ''.join(f'<figure class="mi reveal"><img src="img/{f}" alt="{alt}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c, alt in ig)
    bur = [('la-reinita', 'La Reinita'), ('la-dori', 'La Dori'), ('la-triplona', 'La Triplona'), ('furia-de-pollo', 'Furia de Pollo'), ('la-matru', 'La Matru'),
           ('la-cabrona', 'La Cabrona'), ('me-derrito', 'Me Derrito'), ('tarta-lotus', 'La Lotus'), ('doble-dosis', 'Doble Dosis'), ('dulce-y-verde', 'Dulce y Verde'), ('gordi-deluxe', 'Gordi Deluxe'), ('picantona', 'Picantona'), ('chickenesa', 'Chickenesa')]

    stk = [('hola', '¡Hola!'), ('marchando', '¡Marchando!'), ('buenos-dias', 'Buenos días'), ('esta-pica', '¡Esta pica!'), ('nam', 'Ñam'), ('gracias', 'Gracias'), ('hambre', 'Tengo hambre'), ('a-comer', '¡A comer!')]
    sk = ''.join(f'<figure class="sk reveal"><img src="img/stickers/{n}.png" alt="Sticker de la mascota: {t}" loading="lazy" width="256" height="256"><figcaption>{t}</figcaption><span><a href="img/stickers/{n}.png" download>PNG</a> · <a href="img/stickers/{n}.webp" download>WEBP</a></span></figure>' for n, t in stk)
    b = ''.join(f'<figure class="mi reveal"><img src="img/dishes/{s}.jpg" alt="{n}" loading="lazy"><figcaption>{n}</figcaption></figure>' for s, n in bur)
    return phero('Galería', 'Mejor verlo <em>que contarlo</em>', 'Un paseo por nuestros platos. Pulsa en cualquier foto para verla en grande.', 'trufadas.jpg', 'Patatas trufadas', ill='galeria', ill_alt='La mascota de ALMA con una cámara de fotos') + f'''
<section class="sec sec--band">
  <div class="wrap">
    <div class="sec__head"><h2 class="sec__title reveal" style="margin:0">Desde la <em>cocina</em></h2>
      <a class="btn btn--solid reveal" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">@almaburgers en Instagram ↗</a></div>
    <div class="masonry">{a}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Hasta las 12:00</p><h2 class="sec__title reveal" style="margin:0">Desayunos <em>en fotos</em></h2></div>
      <a class="btn btn--solid reveal" href="desayunos.html">Ver los desayunos →</a></div>
    <div class="photogrid">{d}</div>
  </div>
</section>
<section class="sec sec--band" id="reels">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Instagram</p><h2 class="sec__title reveal" style="margin:0">ALMA <em>en vídeo</em></h2></div>
      <a class="btn btn--solid reveal" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">@almaburgers ↗</a></div>
    {phones()}
  </div>
</section>
<section class="sec" id="ultimas">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Lo último en Instagram</p><h2 class="sec__title reveal" style="margin:0">Últimas <em>publicaciones</em></h2></div>
      <a class="btn btn--solid reveal" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">Seguir en Instagram ↗</a></div>
    {igposts(12)}
  </div>
</section>
<section class="sec" id="stickers">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Para tu móvil</p><h2 class="sec__title reveal" style="margin:0">Stickers de <em>ALMA</em></h2></div>
      <a class="btn btn--solid reveal" href="img/stickers/stickers-alma.zip" download>Descargar todos (ZIP)</a></div>
    <p class="chap__p reveal" style="margin:0 0 22px">La mascota para mandar por WhatsApp: guarda la imagen y compártela, o añade los archivos <b>.webp</b> con una app de stickers como Sticker Maker.</p>
    <div class="sgrid">{sk}</div>
  </div>
</section>
<section class="sec sec--band">
  <div class="wrap">
    <p class="kicker reveal">De cerca</p><h2 class="sec__title reveal">Las hamburguesas, <em>una a una</em></h2>
    <div class="masonry" style="margin-top:30px">{b}</div>
    <div class="btnrow" style="margin-top:20px"><a class="btn btn--solid" href="carta.html">Ver la carta completa</a></div>
  </div>
</section>'''


def visitanos():
    return phero('Visítanos', 'Ven a <em>vernos</em>', 'En pleno centro de Ordizia, con terraza. Pide online o déjate caer.', ill='visitanos', ill_alt='Un perrito caliente abriendo una puerta y saludando') + f'''
<section class="sec sec--ink">
  <div class="wrap visit__grid">
    <div>
      <div class="chap__head chap__head--auto visit__head"><span class="chap__n reveal" aria-hidden="true">01</span><div><p class="kicker kicker--dark reveal">Dónde estamos</p>
      <h2 class="visit__title reveal">Kale Nagusia, 42<br>Ordizia</h2></div></div>
      <p class="eyebrow reveal" style="color:var(--ink);margin-bottom:26px"><span class="dot"></span><span id="openStatus">Horario</span></p>
      <div class="btnrow reveal">
        <a class="btn btn--cream" href="https://www.google.com/maps/dir/?api=1&destination=43.054023,-2.178607" target="_blank" rel="noopener">Cómo llegar</a>
        <a class="btn btn--line" href="tel:+34747486092">747 48 60 92</a>
        <a class="btn btn--line" href="https://wa.me/34747486092" target="_blank" rel="noopener">WhatsApp</a>
      </div>
      <h3 class="h reveal" id="horario">Horario <small id="todayLabel" style="font-weight:500;opacity:.7;font-size:.9rem;margin-left:8px"></small></h3>
      <ul class="hours reveal" id="hours"></ul>
      <p class="fine">La hora de cierre puede variar según el día. Si vienes tarde, llámanos o escríbenos antes.</p>
      <h3 class="h reveal" id="reparto">Reparto a domicilio</h3>
      <ul class="hours reveal"><li><span>Miércoles, jueves y domingo</span><span>19:30 – 23:00</span></li><li><span>Viernes y sábado</span><span>19:30 – 23:30</span></li><li><span>Lunes y martes</span><span>Sin reparto</span></li></ul>
      <p class="fine">Los desayunos no tienen reparto. De momento, los pedidos online se pagan en el local.</p>
      <div class="delivery reveal"><b>¿Pedir desde casa?</b><button class="lnk" type="button" data-wa-order style="color:var(--dark-pop);font-size:1rem">Por WhatsApp →</button></div>
    </div>
    <div class="map reveal" data-ext-src="https://www.openstreetmap.org/export/embed.html?bbox=-2.1836%2C43.0515%2C-2.1736%2C43.0565&amp;layer=mapnik&amp;marker=43.054023%2C-2.178607" data-ext-title="Mapa de Alma Burger en Ordizia">
      <div class="extph"><img src="img/ill/visitanos.png" alt="" loading="lazy"><p><b>Kale Nagusia 42, Ordizia</b></p><p class="extph__s">El mapa lo sirve OpenStreetMap. Se carga solo si lo pides.</p>
        <button class="btn btn--solid btn--sm" type="button" data-ext-load>Cargar el mapa</button><a class="lnk" href="https://www.google.com/maps/search/?api=1&amp;query=Alma+Burger+Kale+Nagusia+42+Ordizia" target="_blank" rel="noopener">Abrir en Google Maps ↗</a></div></div>
  </div>
</section>
<section class="sec" id="contacto">
  <div class="wrap split">
    <div><p class="kicker reveal">Contacto</p><h2 class="sec__title reveal">¿Tienes alguna <em>duda</em>?</h2>
      <p class="reveal" style="font-size:1.1rem;max-width:28em">Si quieres preguntarnos algo sobre la carta, los alérgenos o el horario, llámanos o escríbenos y te respondemos lo antes posible.</p></div>
    <div class="contact reveal">
      <a class="contact__it" href="tel:+34747486092"><b>Llámanos</b><span>747 48 60 92</span></a>
      <a class="contact__it" href="https://wa.me/34747486092" target="_blank" rel="noopener"><b>Escríbenos por WhatsApp</b><span>Para consultas y dudas</span></a>
      <a class="contact__it" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener"><b>Instagram</b><span>@almaburgers</span></a>
      <p class="fine" style="opacity:.75">Los pedidos se hacen en «Pedir online».</p>
    </div>
  </div>
</section>'''


def nf():
    return phero('404', 'Esta página se <em>ha comido</em>', 'No encontramos lo que buscas. Pero tenemos hamburguesas: vuelve a la carta y elige una.') + """
<section class="sec" style="text-align:center"><div class="btnrow" style="justify-content:center"><a class="btn btn--solid" href="index.html">Ir al inicio</a><a class="btn" href="carta.html">Ver la carta</a></div></section>"""


TITLES = {
    'index': ('Alma Burger · Hamburguesas y desayunos en Ordizia', 'Hamburguesas y desayunos en Ordizia. No es solo comida. Es ALMA: smash burgers, tostadas, pancakes, matcha, cafés especiales y postres.'),
    'alma': ('El alma · Alma Burger', 'No es solo comida. Es ALMA. La historia de Alma Burger: nuestras raíces, nuestra familia y por qué hacemos hamburguesas y desayunos con identidad propia.'),
    'carta': ('Hamburguesas y carta · Alma Burger', 'Carta completa de Alma Burger: smash burgers, para compartir, bocadillos, hot dogs, postres y menú infantil. Pide online.'),
    'desayunos': ('Desayunos con pasión · Alma Burger', 'Desayunos con pasión hasta las 12:00 en Ordizia: tostadas con toppings de verdad, pancakes, bowls, cafés especiales, zumos y matcha.'),
    'galeria': ('Galería · Alma Burger', 'Las mejores fotos de los platos de Alma Burger: hamburguesas, picoteo, desayunos y postres.'),
    'visitanos': ('Visítanos · Alma Burger', 'Kale Nagusia 42, Ordizia. Horario, mapa y contacto.'),
    'aviso': ('Aviso legal · Alma Burger', 'Aviso legal y condiciones de uso de la web de ALMA Burger & Breakfast.'),
    'privacidad': ('Política de privacidad · Alma Burger', 'Cómo trata ALMA Burger & Breakfast tus datos personales en pedidos, consultas y en la web.'),
    'cookies': ('Política de cookies · Alma Burger', 'Qué guarda la web de ALMA Burger & Breakfast en tu navegador y cómo cambiarlo.'),
}
def lpage(kind):
    h = {'aviso': ('Aviso <em>legal</em>', 'Quién está detrás de esta web y las condiciones para usarla.', LEGAL.aviso),
         'privacidad': ('Política de <em>privacidad</em>', 'Qué datos tuyos usamos, para qué y cómo puedes controlarlos.', LEGAL.privacidad),
         'cookies': ('Política de <em>cookies</em>', 'Lo que guarda esta web en tu navegador. Spoiler: muy poco.', LEGAL.cookies)}[kind]
    crumb = {'aviso': 'Aviso legal', 'privacidad': 'Privacidad', 'cookies': 'Cookies'}[kind]
    return phero(crumb, h[0], h[1]) + h[2](LCFG)


BODIES = {'index': home, 'alma': alma, 'carta': carta, 'desayunos': desayunos, 'galeria': galeria, 'visitanos': visitanos,
          'aviso': lambda: lpage('aviso'), 'privacidad': lambda: lpage('privacidad'), 'cookies': lambda: lpage('cookies')}
FILES = {'index': 'index.html', 'alma': 'el-alma.html', 'carta': 'carta.html', 'desayunos': 'desayunos.html', 'galeria': 'galeria.html', 'visitanos': 'visitanos.html',
         'aviso': 'aviso-legal.html', 'privacidad': 'privacidad.html', 'cookies': 'cookies.html'}

SELECTOR = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Alma Burger · Elige versión</title>
<link href="https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=Bricolage+Grotesque:wght@500;800&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box;margin:0}body{font-family:'Bricolage Grotesque',sans-serif;background:#faf9f5;color:#0b0b0b;min-height:100vh;display:grid;place-items:center;padding:30px}
main{max-width:980px;width:100%;text-align:center}h1{font-family:'Bagel Fat One';font-weight:400;font-size:clamp(2rem,5vw,3.4rem);margin:10px 0 6px}p.s{opacity:.7;margin-bottom:30px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:22px}@media(max-width:700px){.g{grid-template-columns:1fr}}
a{display:block;text-decoration:none;color:inherit;border:3px solid #0b0b0b;border-radius:28px;padding:26px;background:#fff;box-shadow:7px 7px 0 #0b0b0b;transition:transform .2s,box-shadow .2s}
a:hover{transform:translate(-3px,-4px);box-shadow:11px 12px 0 #0b0b0b}h2{font-family:'Bagel Fat One';font-weight:400;font-size:1.7rem;margin-bottom:8px}
.sw{display:flex;gap:8px;justify-content:center;margin:14px 0}.sw i{width:44px;height:44px;border-radius:50%;border:3px solid #0b0b0b}
span.b{display:inline-block;margin-top:10px;background:#0b0b0b;color:#faf9f5;border-radius:99px;padding:8px 20px;font-weight:800}img{height:90px;margin:0 auto}</style></head><body><main>
<img src="opcion-1-color/img/mascot.png" alt=""><h1>Alma Burger · demo web</h1><p class="s">Dos versiones del mismo sitio. Elige cuál ver.</p>
<div class="g"><a href="opcion-1-color/index.html"><h2>Opción 1 · Color</h2><p>Crema + negro del logo, con el azul eléctrico de su carta y un amarillo cheddar de apoyo.</p>
<div class="sw"><i style="background:#faf8f0"></i><i style="background:#0b0b0b"></i><i style="background:#1a00ad"></i><i style="background:#ffc62e"></i></div><span class="b">Ver opción 1</span></a>
<a href="opcion-2-fiel-logo/index.html"><h2>Opción 2 · Fiel al logo</h2><p>Solo los colores del logo: negro y crema. Sin ningún color añadido.</p>
<div class="sw"><i style="background:#faf9f5"></i><i style="background:#0b0b0b"></i></div><span class="b">Ver opción 2</span></a></div></main></body></html>'''


COLORS = {
    'negro': dict(css='theme-fiel.css', tcolor='#0b0b0b', name='Negro y crema', other='azul', swap='Ver la web en azul'),
    'azul': dict(css='theme-navy.css', tcolor='#032164', name='Azul y crema', other='negro', swap='Ver la web en negro'),
}


SITE = (CFG.get('site_url') or '').strip()
if SITE and not SITE.endswith('/'):
    SITE += '/'


def og_block(title, desc, url, img):
    """Vista previa al compartir (WhatsApp, Instagram, Facebook, Telegram...)."""
    tags = [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="ALMA Burger &amp; Breakfast">',
        '<meta property="og:locale" content="es_ES">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{img}">',
        f'<meta property="og:image:secure_url" content="{img}">',
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="ALMA Burger &amp; Breakfast: hamburguesas y desayunos en Ordizia">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{img}">',
        f'<link rel="canonical" href="{url}">',
    ]
    return chr(10).join(tags)


EU_PAGES = ['index.html', 'el-alma.html', 'carta.html', 'desayunos.html', 'galeria.html', 'visitanos.html', '404.html']


def eu_name(name):
    return name[:-5] + '.eu.html'


def to_eu(html):
    """Página en euskera a partir de la página en castellano ya generada."""
    for a, b in EUD.RAW:
        html = html.replace(a, b)
    for k in sorted(EUD.TXT, key=len, reverse=True):
        html = html.replace('>' + k + '<', '>' + EUD.TXT[k] + '<')
    q = lambda x: x.replace('&', '&amp;').replace('"', '&quot;')
    plain = {k: v for k, v in EUD.TXT.items() if '<' not in k}
    plain.update(EUD.ATTR)
    for k in sorted(plain, key=len, reverse=True):
        for a in ('alt', 'aria-label', 'placeholder', 'title', 'content', 'data-ext-title'):
            html = html.replace(f'{a}="{q(k)}"', f'{a}="{q(plain[k])}"')
    for pre, tr in EUD.ATTR_PREFIX.items():
        html = _re.sub(r'(alt|aria-label)="' + _re.escape(q(pre)) + r'([^"]*)"',
                       lambda m: f'{m.group(1)}="{q(tr)}' + q(plain.get(m.group(2).replace('&amp;', '&').replace('&quot;', '"'), m.group(2))) + '"', html)
    # enlaces entre páginas: a la versión en euskera (las páginas legales siguen en castellano)
    html = _re.sub(r'href="(' + '|'.join(_re.escape(n[:-5]) for n in EU_PAGES) + r')\.html', r'href="\1.eu.html', html)
    html = html.replace('<html lang="es"', '<html lang="eu"', 1).replace('content="es_ES"', 'content="eu_ES"')
    html = html.replace('<script src="app.js', '<script src="eu.js?v=' + VER + '"></script>\n<script src="app.js', 1)
    html = html.replace('>Aviso legal</a>', '>Lege oharra</a>').replace('>Privacidad</a>', '>Pribatutasuna</a>')
    html = html.replace('<nav class="foot__legal" aria-label="Lege-informazioa">', '<nav class="foot__legal" aria-label="Lege-informazioa"><span>(gaztelaniaz)</span>')
    return html


def redirect(dest):
    return (f'<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><title>ALMA Burger &amp; Breakfast</title>'
            f'<script>var c="negro",l="";try{{c=localStorage.getItem("alma-color")||"negro";l=localStorage.getItem("alma-lang")==="eu"?".eu":""}}catch(e){{}}var d="{dest}".replace("{{c}}",c);if(l&&/(index|el-alma|carta|desayunos|galeria|visitanos|404)\\.html$/.test(d))d=d.replace(/\\.html$/,".eu.html");location.replace(d)</script>'
            f'<meta http-equiv="refresh" content="1;url={dest.replace("{c}", "negro")}"><a href="{dest.replace("{c}", "negro")}">Entrar en ALMA</a>')


def _small_pngs(out):
    """Favicon a 96 px y la imagen de la animación con paleta de grises: mismo aspecto, menos peso."""
    from PIL import Image
    fv = out / 'img' / 'favicon.png'
    im = Image.open(fv)
    if im.width > 96:
        im.convert('RGBA').resize((96, round(im.height * 96 / im.width)), Image.LANCZOS).save(fv, optimize=True)
    la = out / 'img' / 'logo-anim.png'
    Image.open(la).convert('L').quantize(colors=24, dither=Image.Dither.NONE).save(la, optimize=True)


def main():
    pages = list(FILES.values()) + ['404.html']
    for theme, t in COLORS.items():
        out = ROOT / theme
        if out.exists():
            shutil.rmtree(out)
        out.mkdir()
        shutil.copytree(SRC / 'img', out / 'img')
        shutil.copytree(SRC / 'themes' / theme / 'img', out / 'img', dirs_exist_ok=True)
        shutil.copytree(SRC / 'fonts', out / 'fonts')
        css = (SRC / 'fonts' / 'fonts.css').read_text(encoding='utf-8') + chr(10) + (SRC / 'base.css').read_text(encoding='utf-8') + '\n' + (SRC / 'pedido-v2.css').read_text(encoding='utf-8') + '\n' + (SRC / t['css']).read_text(encoding='utf-8')
        (out / 'styles.css').write_text(css, encoding='utf-8')
        shutil.copy(SRC / 'app.js', out / 'app.js')
        built = {}
        for k, fn in BODIES.items():
            title, desc = TITLES[k]
            active = {'index': 'home', 'alma': 'alma', 'carta': 'carta', 'desayunos': 'desayunos', 'galeria': 'galeria', 'visitanos': 'visitanos'}.get(k, '')
            built[FILES[k]] = shell(active, title, desc, fn(), t['tcolor'])
        built['404.html'] = shell('', 'Página no encontrada · Alma Burger', 'Página no encontrada', nf(), t['tcolor'])
        written = []
        for name, html0 in built.items():
            for lang in ('es', 'eu'):
                if lang == 'eu' and name not in EU_PAGES:
                    continue
                fname = name if lang == 'es' else eu_name(name)
                html = html0.replace('<html lang="es"', f'<html lang="es" data-theme="{theme}"', 1)
                html = html.replace('__SWAP__', f'../{t["other"]}/{fname}').replace('__SWAPNAME__', t['swap'])
                alt = (eu_name(name) if name in EU_PAGES else 'index.eu.html') if lang == 'es' else './' + name  # './' para que no se cambie a .eu
                html = (html.replace('__LANGHREF__', alt).replace('__LANGCODE__', 'eu' if lang == 'es' else 'es')
                        .replace('__LANGLABEL__', 'Euskaraz' if lang == 'es' else 'En castellano')
                        .replace('__LANGFROM__', 'ES' if lang == 'es' else 'EU').replace('__LANGTXT__', 'EU' if lang == 'es' else 'ES'))
                if lang == 'eu':
                    html = to_eu(html)
                m = _re.search(r'<title>(.*?)</title>', html); dm = _re.search(r'<meta name="description" content="([^"]*)">', html)
                url = SITE + theme + '/' + ('' if fname == 'index.html' else fname)
                og = og_block(m.group(1), dm.group(1), url, SITE + theme + '/img/share.jpg')
                if lang == 'eu':
                    og = og.replace('content="es_ES"', 'content="eu_ES"').replace('hamburguesas y desayunos en Ordizia', 'hanburgesak eta gosariak Ordizian')
                if name in EU_PAGES:
                    og += chr(10) + f'<link rel="alternate" hreflang="es" href="{SITE + theme + "/" + name}">' + chr(10) + f'<link rel="alternate" hreflang="eu" href="{SITE + theme + "/" + eu_name(name)}">'
                html = html.replace('__OGBLOCK__', og, 1)
                html = html.replace('<head>', '<head>\n<script>try{localStorage.setItem("alma-color","' + theme + '");localStorage.setItem("alma-lang","' + lang + '")}catch(e){}</script>', 1)
                (out / fname).write_text(html, encoding='utf-8')
                written.append(fname)
        (out / 'eu.js').write_text('window.ALMA_EU=' + json.dumps(EUD.JS, ensure_ascii=False) + ';' + chr(10), encoding='utf-8')
        IMGOPT.build(out, [out / n for n in written], [out / 'app.js'])
        _small_pngs(out)
    # raíz: intro con selector de color + redirecciones de los enlaces antiguos
    (ROOT / 'index.html').write_text((SRC / 'intro.html').read_text(encoding='utf-8').replace('__SITE__', SITE), encoding='utf-8')
    for name in pages:
        if name != 'index.html':
            (ROOT / name).write_text(redirect('{c}/' + name), encoding='utf-8')
    for old, col in (('opcion-1-color', 'azul'), ('opcion-2-fiel-logo', 'negro')):
        (ROOT / old).mkdir(exist_ok=True)
        for name in pages:
            (ROOT / old / name).write_text(redirect(f'../{col}/' + name), encoding='utf-8')
    print('ok')


main()
