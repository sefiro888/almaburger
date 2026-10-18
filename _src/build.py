"""Genera las dos versiones de la web (multipágina) a partir de la misma base.
   python _src/build.py  ->  opcion-1-color/  y  opcion-2-fiel-logo/  (+ index.html selector en la raíz)"""
import shutil, pathlib, json

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
THEMES = {
    'opcion-1-color':     dict(css='theme-color.css', name='Opción 1 · Color', other='opcion-2-fiel-logo', tcolor='#1a00ad'),
    'opcion-2-fiel-logo': dict(css='theme-fiel.css',  name='Opción 2 · Fiel al logo', other='opcion-1-color', tcolor='#0b0b0b'),
}
PAGES = [('el-alma.html', 'El alma', 'alma'), ('carta.html', 'Carta', 'carta'), ('desayunos.html', 'Desayunos', 'desayunos'),
         ('galeria.html', 'Galería', 'galeria'), ('visitanos.html', 'Visítanos', 'visitanos')]
JE = 'https://www.just-eat.es/restaurants-alma-burger-ordizia/menu'
import time
VER = str(int(time.time()))


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
  <a class="nav__logo" href="index.html" aria-label="Alma Burger, inicio">{rig(46, 'rig--still')}<span>Alma Burger</span></a>
  <nav class="nav__links" aria-label="Principal">{links}</nav>
  <div class="nav__actions">
    <button class="cartbtn" id="cartOpen" aria-label="Abrir mi pedido "><span class="cartbtn__t">Pedido</span><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 8h14l-1.2 11H6.2L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><span class="cartbtn__n" id="cartCount">0</span></button>
    <a class="btn btn--je btn--sm nav__je" href="{JE}" target="_blank" rel="noopener"><span class="long">Pedir en Just Eat</span><span class="short">Just Eat</span> ↗</a>
    <button class="btn btn--solid btn--sm nav__wa" type="button" data-wa-order>Pedir por WhatsApp</button>
    <button class="burger" id="burgerBtn" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>'''


CTA = f'''<section class="sec cta" style="padding-bottom:140px;border-top:var(--bw) solid var(--ink)">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:26px;justify-content:space-between;align-items:center">
    <h2 class="sec__title reveal" style="margin:0">¿Te entra <em>el hambre</em>?</h2>
    <div class="btnrow reveal" style="margin:0">
      <a class="btn btn--je" href="{JE}" target="_blank" rel="noopener">Pedir en Just Eat ↗</a>
      <button class="btn btn--solid" type="button" data-wa-order>Pedir por WhatsApp</button>
      <a class="btn" href="visitanos.html#reservar">Reservar mesa</a>
      <a class="btn" href="carta.html">Ver la carta</a>
    </div>
  </div>
</section>'''

FOOT = f'''<footer class="foot">
  {walker(96, 30)}
  <img class="foot__word" src="img/wordmark-cream.png" alt="Alma Burger">
  <div class="foot__grid">
    <div><h4>Donde el sabor tiene alma</h4><p>Smash burgers, picoteo, hot dogs, postres y desayunos en el corazón de Ordizia.</p></div>
    <div><h4>Explora</h4><ul><li><a href="index.html">Inicio</a></li>{''.join(f'<li><a href="{h}">{t}</a></li>' for h, t, k in PAGES)}</ul></div>
    <div><h4>Contacto</h4><ul><li>Kale Nagusia 42, 20240 Ordizia</li><li><a href="tel:+34747486092">747 48 60 92</a></li>
      <li><a href="https://wa.me/34747486092" target="_blank" rel="noopener">WhatsApp</a></li>
      <li><a href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">Instagram @almaburgers</a></li>
      <li><a href="{JE}" target="_blank" rel="noopener">Just Eat</a></li></ul></div>
  </div>
  <div class="foot__row"><p>© <span class="yr"></span> Alma Burger · Consulta nuestra carta de alérgenos al personal</p><p>Demo de diseño web</p></div>
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
    <div class="cart__alt"><button class="lnk" id="cartClear" type="button">Vaciar pedido</button><span>·</span><a href="{JE}" target="_blank" rel="noopener">¿Prefieres Just Eat? ↗</a></div>
    <p><b>Pago por Bizum:</b> el local te confirmará el pedido y el total, y te indicará cómo hacer el Bizum. Se abrirá WhatsApp con tu pedido ya escrito.</p>
  </div>
</aside>
<div class="scrim" id="scrim"></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<button class="orderbar" id="orderbar" type="button" hidden><span class="orderbar__n" id="orderbarN">0</span><span>Ver mi pedido</span><b id="orderbarT">0,00€</b></button>
<div class="progress" id="progress" aria-hidden="true"></div>
<a class="wa" href="https://wa.me/34747486092" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21l1.6-4.8A9 9 0 1 1 8 19.5L3 21Z"/><path d="M9 10c0 2.800 2.200 5 5 5l1.200-1.300-1.800-1-.8.700a4 4 0 0 1-1.700-1.700l.7-.8-1-1.800L9 10Z" fill="currentColor" stroke="none"/></svg></a>'''



def shell(active, title, desc, body, tcolor, og='img/burger.jpg'):
    HOMEA = ' aria-current="page"' if active == 'home' else ''
    CARTAA = ' aria-current="page"' if active == 'carta' else ''
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{tcolor}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=Unbounded:wght@800;900&family=Anton&family=Syne:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;700&family=Barlow:wght@400;500;600;700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Instrument+Serif:ital@0;1&family=Fraunces:opsz,wght@9..144,400;9..144,700;9..144,800;9..144,900&family=Dela+Gothic+One&family=Shrikhand&family=Big+Shoulders+Display:wght@800;900&family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,700;12..96,800&display=swap" rel="stylesheet">
<script>try{{var f=new URLSearchParams(location.search).get('font')||localStorage.getItem('alma-font');if(f&&f!=='bagel')document.documentElement.dataset.font=f;document.documentElement.dataset.all=localStorage.getItem('alma-all')||'on'}}catch(e){{}}</script>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;700;800&family=Outfit:wght@400;500;700;800&family=Gabarito:wght@400;500;700;900&family=Geist:wght@400;500;700;800&family=Funnel+Display:wght@400;500;700;800&family=Host+Grotesk:wght@400;500;700;800&family=Parkinsans:wght@400;500;700;800&family=Familjen+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
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
  <a href="index.html"{HOMEA}><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/></svg><span>Inicio</span></a>
  <a href="carta.html"{CARTAA}><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16M4 12h16M4 19h10"/></svg><span>Carta</span></a>
  <button type="button" id="bnavCart"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 8h14l-1.2 11H6.2L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><span id="bnavT">Pedido</span><i id="bnavN" hidden>0</i></button>
  <a class="bnav__jeat" href="{JE}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h10l2-5h4"/><circle cx="6" cy="17" r="2.5"/><circle cx="18" cy="17" r="2.5"/><path d="M8.5 17h7"/></svg><span>Just Eat</span></a>
  <a href="visitanos.html#reservar"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg><span>Reservar</span></a>
</nav>
<script src="app.js?v={VER}"></script>
</body>
</html>'''


def phero(crumb, h1, lead, pic=None, pic_alt='', dark=False):
    p = f'<figure class="phero__pic reveal"><img src="img/{pic}" alt="{pic_alt}"></figure>' if pic else ''
    return f'''<section class="phero{' phero--dark' if dark else ''}{' phero--pic' if pic else ''}">
  <div class="wrap">
    <nav class="crumbs" aria-label="Migas de pan"><a href="index.html">Inicio</a><span>/</span><span>{crumb}</span></nav>
    <h1 class="reveal">{h1}</h1>
    <p class="lead reveal">{lead}</p>
  </div>
  {p}
  <div class="phero__line"></div>
  {walker(104, 24)}
</section>'''


# ---------------------------------------------------------------- páginas
STAGE = (SRC / 'stage.svg.html').read_text(encoding='utf-8')


IG = ''.join(f'<a class="ig reveal" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><img src="img/{f}" alt="" loading="lazy"></a>' for f in ['burger.jpg', 'picoteo.jpg', 'pancake.jpg', 'trufadas.jpg', 'matcha.jpg', 'tostada.jpg'])


def home():
    marq = ''.join(f'<span>{t}</span><i>✶</i>' for t in ['Smash burgers', 'Picoteo', 'Hot dogs', 'Desayunos hasta las 12:00', 'Tartas de queso', 'Matcha'])
    return f'''<section class="hero">
  <div class="hero__copy">
    <p class="eyebrow reveal"><span class="dot"></span><span id="openStatus">Hamburguesería · Ordizia</span></p>
    <h1 class="sr-only">Alma Burger</h1>
    <div class="stagewrap reveal">{STAGE}<div class="stage__dots" id="stageDots" role="group" aria-label="Elegir la entrada de la mascota"></div></div>
    <p class="hero__lead reveal">Donde el sabor tiene <em>alma</em>. Smash burgers de recetas propias, picoteo para compartir y desayunos de los que invitan a volver.</p>
    <div class="hero__cta reveal">
      <a class="btn btn--je" href="{JE}" target="_blank" rel="noopener">Pedir en Just Eat ↗</a>
      <button class="btn btn--solid" type="button" data-wa-order>Pedir por WhatsApp</button>
      <a class="btn" href="visitanos.html#reservar">Reservar mesa</a>
    </div>
    <p class="hero__alt reveal"><a href="visitanos.html#reservar">Reservar mesa</a> · <a href="carta.html">Ver la carta</a> · <a href="tel:+34747486092">747 48 60 92</a></p>
    <ul class="hero__facts reveal"><li><b>16</b> hamburguesas</li><li><b>8:00</b> desayunos</li><li><b>Kale Nagusia</b> 42</li></ul>
  </div>
  <div class="hero__visual" id="heroVisual">
    <div class="blob"></div>
    <figure class="hero__photo"><img src="img/burger.jpg" alt="La Puerquita, la burger del mes: doble smash con pulled pork" fetchpriority="high"><a class="hero__tag" href="carta.html#hamburguesas">Burger del mes · La Puerquita</a></figure>
    <figure class="hero__photo hero__photo--b"><img src="img/trufadas.jpg" alt="Patatas trufadas con parmesano y mayonesa de trufa"></figure>
    <svg class="sticker" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="circ" d="M100,100 m-72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"/></defs><circle cx="100" cy="100" r="96"/><text><textPath href="#circ" font-size="17" font-weight="800" textLength="440" lengthAdjust="spacing">SMASH BURGERS · AL MOMENTO · SIN ATAJOS · </textPath></text><text x="100" y="118" text-anchor="middle" font-size="62" font-family="Bagel Fat One">✶</text></svg>
  </div>
  <div class="heroline" aria-hidden="true">{walker(112, 22)}</div>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee__track">{marq}{marq}</div></div>

<section class="sec sec--dark hstory" id="historia">
  <div class="wrap hstory__grid">
    <div class="hstory__pics">
      <figure class="hp hp--1 reveal"><img src="img/dishes/la-puerquita.jpg" alt="La Puerquita, doble smash con pulled pork" loading="lazy"></figure>
      <figure class="hp hp--2 reveal"><img src="img/dishes/la-dori.jpg" alt="La Dori con doritos y cheddar" loading="lazy"></figure>
      <figure class="hp hp--3 reveal"><img src="img/dishes/me-derrito.jpg" alt="Me Derrito, smash con salsa cheddar" loading="lazy"></figure>
      <svg class="hp__stamp" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="c2" d="M100,100 m-72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"/></defs><circle cx="100" cy="100" r="96"/><text><textPath href="#c2" font-size="17" font-weight="800" textLength="440" lengthAdjust="spacing">ALMA BURGER · ORDIZIA · DESDE EL PRIMER DÍA · </textPath></text><text x="100" y="116" text-anchor="middle" font-size="58" font-family="Bagel Fat One">A</text></svg>
    </div>
    <div class="hstory__text">
      <p class="kicker kicker--dark reveal">Nuestra historia</p>
      <h2 class="sec__title reveal">Donde cada hamburguesa <em>tiene alma</em></h2>
      <p class="hstory__lead reveal">Todo comenzó con una idea sencilla: crear un lugar donde disfrutar de hamburguesas auténticas, elaboradas con ingredientes de calidad y mucho cariño.</p>
      <p class="reveal">En Alma Burger creemos que una buena hamburguesa es mucho más que una comida. Es compartir momentos, reunirse con amigos y disfrutar de sabores que dejan huella.</p>
      <div class="hstory__more" id="hmore"><p>Por eso seleccionamos cuidadosamente cada ingrediente, desde la carne hasta el pan, para ofrecer una experiencia única en cada bocado.</p>
        <p>Cada hamburguesa que sale de nuestra cocina está preparada al momento, con dedicación y pasión por hacer las cosas bien.</p>
        <p>Hoy seguimos creciendo con la misma ilusión del primer día: convertir Alma Burger en un lugar donde nuestros clientes se sientan como en casa y siempre quieran volver.</p>
        <p class="hstory__end">Bienvenidos a Alma Burger.</p></div>
      <div class="btnrow reveal" style="margin-top:22px"><button class="btn btn--cream" type="button" id="hmoreBtn" aria-expanded="false" aria-controls="hmore">Seguir leyendo ↓</button><a class="btn btn--line" href="el-alma.html">Todo sobre nosotros</a></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Los destacados</p><h2 class="sec__title reveal">Para empezar <em>fuerte</em></h2></div>
      <a class="btn btn--solid reveal" href="carta.html">Toda la carta →</a></div>
    <div class="rail" id="featured"></div>
  </div>
</section>

<section class="sec sec--ink" id="como-pedir">
  <div class="wrap">
    <p class="kicker kicker--dark reveal">Pedir es fácil</p><h2 class="sec__title reveal">Elige cómo <em>quieres pedir</em></h2>
    <div class="paths">
      <div class="path path--main reveal"><span class="path__tag">A domicilio</span><b>En Just Eat</b><span>La forma habitual de recibir tu pedido en casa. Se abre nuestra página de Just Eat: eliges tus platos y pagas allí.</span><a class="btn btn--je" href="{JE}" target="_blank" rel="noopener">Pedir en Just Eat ↗</a></div>
      <div class="path path--main path--wa reveal"><span class="path__tag">Recoger o domicilio</span><b>Por WhatsApp</b><span>Arma tu pedido aquí y envíalo en un toque. El local te confirma el total y cómo pagar por Bizum.</span><button class="btn btn--solid" type="button" data-wa-order>Empezar mi pedido</button></div>
      <div class="path reveal"><span class="path__tag">Mesa</span><b>Reserva tu mesa</b><span>Elige día, hora y personas y te preparamos el mensaje de WhatsApp.</span><a class="btn btn--line" href="visitanos.html#reservar">Reservar mesa</a></div>
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
    <div class="split__pic reveal"><figure class="ph" style="inset:0 8% 8% 0;transform:rotate(-3deg)"><img src="img/burger.jpg" alt="La Puerquita" loading="lazy"></figure>
      <figure class="ph" style="width:38%;aspect-ratio:1;right:0;bottom:0;transform:rotate(5deg)"><img src="img/cabrona.jpg" alt="Hamburguesa con queso de cabra y patatas" loading="lazy"></figure></div>
    <div>
      <p class="kicker reveal">Burger del mes</p>
      <h2 class="sec__title reveal">La <em>Puerquita</em></h2>
      <p class="reveal" style="font-size:1.15rem;max-width:30em">Doble carne smash con queso cheddar, jugoso pulled pork en su salsa, salsa Emmy en ambas tapas y ensalada de cebolla encurtida. Todo en pan brioche. Potente, cremosa y tremendamente puerquita.</p>
      <div class="btnrow reveal" style="margin-top:26px"><span class="price" style="font-size:2rem;font-family:var(--display)">18,50€</span>
        <button class="btn btn--solid" type="button" data-add="hamburguesas|La Puerquita">Añadir a mi pedido +</button></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="kicker reveal">Descubre</p><h2 class="sec__title reveal">Todo Alma, <em>en un vistazo</em></h2>
    <div class="tease" style="margin-top:30px">
      <a class="tz tz--wide reveal" href="carta.html"><img src="img/dishes/la-triplona.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>La carta</h3><p>Hamburguesas, picoteo, bocadillos, hot dogs y postres.</p></div></a>
      <a class="tz tz--wide reveal" href="desayunos.html"><img src="img/tostada.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>Desayunos</h3><p>Tostadas, pancakes, bowls y matcha hasta las 12:00.</p></div></a>
      <a class="tz reveal" href="el-alma.html"><img src="img/cabrona.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>El alma</h3><p>Nuestra historia.</p></div></a>
      <a class="tz reveal" href="galeria.html"><img src="img/picoteo.jpg" alt="" loading="lazy"><span class="tz__go">→</span><div class="tz__in"><h3>Galería</h3><p>Mejor verlo que contarlo.</p></div></a>
      <a class="tz tz--plain reveal" href="visitanos.html"><span class="tz__go">→</span><div class="tz__in"><h3>Visítanos</h3><p>Kale Nagusia 42, Ordizia.</p></div>{rig(110, 'rig--still')}</a>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="sec__head"><div><p class="kicker reveal">Síguenos</p><h2 class="sec__title reveal" style="margin:0">@almaburgers <em>en Instagram</em></h2></div>
      <div class="btnrow reveal" style="margin:0"><a class="btn btn--solid btn--sm" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">Instagram ↗</a><a class="btn btn--sm" href="https://www.tiktok.com/@almaburgerss" target="_blank" rel="noopener">TikTok @almaburgerss ↗</a></div></div>
    <div class="igrow">{IG}</div>
  </div>
</section>'''


def alma():
    return phero('El alma', 'Donde cada hamburguesa tiene <em>alma</em>', 'Ingredientes seleccionados, recetas únicas y el sabor que te hará volver.', 'dishes/la-cabrona.jpg', 'La Cabrona, doble smash con queso de cabra') + f'''
<section class="sec">
  <div class="wrap story">
    <aside class="story__side"><p class="kicker reveal">Nuestra historia</p>
      <figure class="story__pic reveal"><img src="img/dishes/me-derrito.jpg" alt="Una smash burger con salsa cheddar, preparada al momento" loading="lazy"></figure></aside>
    <div class="story__text">
      <p class="story__lead reveal">Todo comenzó con una idea sencilla: crear un lugar donde disfrutar de hamburguesas auténticas, elaboradas con ingredientes de calidad y mucho cariño.</p>
      <p class="reveal">En Alma Burger creemos que una buena hamburguesa es mucho más que una comida. Es compartir momentos, reunirse con amigos y disfrutar de sabores que dejan huella.</p>
      <p class="reveal">Por eso seleccionamos cuidadosamente cada ingrediente, desde la carne hasta el pan, para ofrecer una experiencia única en cada bocado.</p>
      <p class="reveal">Cada hamburguesa que sale de nuestra cocina está preparada al momento, con dedicación y pasión por hacer las cosas bien.</p>
      <p class="reveal">Hoy seguimos creciendo con la misma ilusión del primer día: convertir Alma Burger en un lugar donde nuestros clientes se sientan como en casa y siempre quieran volver.</p>
      <p class="story__end reveal">Bienvenidos a Alma Burger.</p>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="pillars">
      <article class="pillar reveal"><span class="pillar__n">01</span><h3>Ingredientes seleccionados</h3><p>Elegimos cuidadosamente cada ingrediente, desde la carne hasta el pan, para ofrecer una experiencia única en cada bocado.</p></article>
      <article class="pillar reveal"><span class="pillar__n">02</span><h3>Preparada al momento</h3><p>Cada hamburguesa que sale de nuestra cocina se prepara al momento, con dedicación y pasión por hacer las cosas bien.</p></article>
      <article class="pillar reveal"><span class="pillar__n">03</span><h3>Como en casa</h3><p>Un lugar donde nuestros clientes se sientan como en casa y siempre quieran volver. Bienvenidos a Alma Burger.</p></article>
    </div>
  </div>
</section>

<section class="sec sec--ink">
  <div class="wrap">
    <div class="stats">
      <div class="stat reveal"><b data-stat="burgers"></b><span>hamburguesas en carta</span></div>
      <div class="stat reveal"><b data-stat="dishes"></b><span>platos y bebidas</span></div>
      <div class="stat reveal"><b data-stat="8:00"></b><span>abrimos con desayunos</span></div>
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
      <figure class="ph ph--2 reveal"><img src="img/matcha.jpg" alt="Matcha helado" loading="lazy"></figure>
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
      <details class="reveal"><summary>¿Tenéis opciones vegetarianas?</summary><p>Sí: la Gordi Deluxe tiene opción vegetariana, además de ensalada con burrata, tortilla de patata y varias tostadas.</p></details>
      <details class="reveal"><summary>¿Y alérgenos?</summary><p>Tenemos carta de alérgenos: pídesela a nuestro equipo y te ayudamos a elegir con tranquilidad.</p></details>
      <details class="reveal"><summary>¿Hacéis entrega a domicilio?</summary><p>Sí. Haz tu pedido en la web, elige «A domicilio» y se enviará por WhatsApp. El local te confirmará si llegamos a tu dirección y el coste del envío. También puedes pedir en Just Eat.</p></details>
      <details class="reveal"><summary>¿Puedo reservar mesa?</summary><p>Claro. Desde la página <a href="visitanos.html#reserva"><b>Visítanos</b></a> te preparamos el mensaje de WhatsApp en un momento.</p></details>
      <details class="reveal"><summary>¿Hay menú infantil?</summary><p>Sí: pechuga empanada, lomo o hamburguesa con queso, siempre con patatas y croquetas, por 9,00€.</p></details>
      <details class="reveal"><summary>¿Hasta qué hora hay desayunos?</summary><p>Servimos desayunos desde que abrimos hasta las 12:00.</p></details>
    </div>
  </div>
</section>'''


JEBANNER = f'''
<div class="jebar"><div class="wrap jebar__in"><a class="btn btn--je btn--sm" href="{JE}" target="_blank" rel="noopener">Pedir en Just Eat ↗</a><span class="jebar__sep"></span><button class="btn btn--solid btn--sm" type="button" data-wa-order>Pedir por WhatsApp</button><span class="jebar__txt">Recoger o a domicilio · pago por Bizum</span></div></div>'''


def carta():
    return phero('Carta', 'Elige tu <em>perdición</em>', 'Smash burgers, picoteo, bocadillos, hot dogs y tartas de queso.') + JEBANNER + '''
<section class="sec sec--dark carta" style="padding-top:30px">
  <div class="wrap">
    <div class="toolbar reveal">
      <label class="search"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input id="q" type="search" placeholder="Busca: cabra, trufa, picante…" aria-label="Buscar en la carta" autocomplete="off"></label>
      <button class="btn btn--line btn--sm" type="button" id="filtersBtn" aria-expanded="false" aria-controls="chips">Filtros</button>
      <button class="btn btn--cream btn--sm" type="button" data-surprise>Sorpréndeme</button>
    </div>
    <div class="tabs" id="tabs" role="tablist" aria-label="Categorías de la carta"></div>
    <div class="chips" id="chips" aria-label="Filtros"></div>
    <div id="menu" class="menu" data-mode="all" aria-live="polite"></div>
    <p class="carta__note">Suplemento por cada ingrediente extra. Consulta nuestra <b>carta de alérgenos</b> al personal. Algunas imágenes son ilustrativas.</p>
  </div>
</section>'''


def desayunos():
    return phero('Desayunos', 'Desayunos <em>con alma</em>', 'De 8:00 a 12:00. Donde el café tiene alma y los desayunos también.', 'tostada.jpg', 'Tostada de salmón, aguacate y hummus de remolacha') + '''
<section class="sec">
  <div class="wrap split">
    <div class="split__pic"><figure class="ph ph--1 reveal"><img src="img/desayuno-capricho.jpg" alt="Pancakes de nutella con fresas" loading="lazy"></figure>
      <figure class="ph ph--2 reveal"><img src="img/matcha.jpg" alt="Matcha helado" loading="lazy"></figure>
      <figure class="ph ph--3 reveal"><img src="img/pancake.jpg" alt="Pancakes de Ferrero Rocher" loading="lazy"></figure></div>
    <div><p class="kicker reveal">Para empezar bien el día</p><h2 class="sec__title reveal">Tostadas, pancakes <em>y matcha</em></h2>
      <p class="reveal">Tostadas con toppings de verdad, pancakes golosos, bowls, zumos, smoothies y unos matchas que no vas a poder dejar de pedir.</p>
      <ul class="dots reveal"><li><span>Espresso</span><i></i><b>1,70€</b></li><li><span>Tostada de salmón y mascarpone</span><i></i><b>7,50€</b></li><li><span>Pancakes de Ferrero</span><i></i><b>6,30€</b></li><li><span>Matcha de mango</span><i></i><b>4,00€</b></li></ul>
    </div>
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
    <p class="carta__note">Desayunos de 8:00 a 12:00. Consulta nuestra <b>carta de alérgenos</b> al personal.</p>
  </div>
</section>'''


def galeria():
    ig = [('burger.jpg', 'La Puerquita', 'La Puerquita, burger del mes'), ('picoteo.jpg', 'Picoteo con alma', 'Aros de cebolla, patatas y croquetas'),
          ('cabrona.jpg', 'Queso de cabra', 'Hamburguesa con queso de cabra y patatas'), ('trufadas.jpg', 'Patatas trufadas', 'Patatas trufadas'),
          ('tostada.jpg', 'Tostada de salmón', 'Tostada de salmón, aguacate y hummus de remolacha'), ('matcha.jpg', 'Matcha', 'Matcha helado'),
          ('pancake.jpg', 'Pancakes de Ferrero', 'Pancakes con Ferrero Rocher'), ('matcha-2.jpg', 'Un poquito de matcha', 'Matcha con leche'),
          ('desayuno-capricho.jpg', '¿Desayuno o capricho?', 'Pancakes de nutella con fresas')]
    a = ''.join(f'<figure class="mi reveal"><img src="img/{f}" alt="{alt}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c, alt in ig)
    bur = [('la-dori', 'La Dori'), ('la-triplona', 'La Triplona'), ('furia-de-pollo', 'Furia de Pollo'), ('la-matru', 'La Matru'),
           ('la-cabrona', 'La Cabrona'), ('me-derrito', 'Me Derrito'), ('tarta-lotus', 'La Lotus'), ('doble-dosis', 'Doble Dosis'), ('dulce-y-verde', 'Dulce y Verde'), ('gordi-deluxe', 'Gordi Deluxe'), ('picantona', 'Picantona'), ('chickenesa', 'Chickenesa')]
    b = ''.join(f'<figure class="mi reveal"><img src="img/dishes/{s}.jpg" alt="{n}" loading="lazy"><figcaption>{n}</figcaption></figure>' for s, n in bur)
    return phero('Galería', 'Mejor verlo <em>que contarlo</em>', 'Un paseo por nuestros platos. Pulsa en cualquier foto para verla en grande.', 'trufadas.jpg', 'Patatas trufadas') + f'''
<section class="sec sec--band">
  <div class="wrap">
    <div class="sec__head"><h2 class="sec__title reveal" style="margin:0">Desde la <em>cocina</em></h2>
      <a class="btn btn--solid reveal" href="https://www.instagram.com/almaburgers/" target="_blank" rel="noopener">@almaburgers en Instagram ↗</a></div>
    <div class="masonry">{a}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <p class="kicker reveal">De cerca</p><h2 class="sec__title reveal">Las hamburguesas, <em>una a una</em></h2>
    <div class="masonry" style="margin-top:30px">{b}</div>
    <div class="btnrow" style="margin-top:20px"><a class="btn btn--solid" href="carta.html">Ver la carta completa</a></div>
  </div>
</section>'''


def visitanos():
    return phero('Visítanos', 'Ven a <em>vernos</em>', 'En pleno centro de Ordizia, con terraza. Reserva mesa, pide por WhatsApp o déjate caer.') + f'''
<section class="sec sec--ink">
  <div class="wrap visit__grid">
    <div>
      <p class="kicker kicker--dark reveal">Dónde estamos</p>
      <h2 class="visit__title reveal">Kale Nagusia, 42<br>Ordizia</h2>
      <p class="eyebrow reveal" style="color:var(--ink);margin-bottom:26px"><span class="dot"></span><span id="openStatus">Horario</span></p>
      <div class="btnrow reveal">
        <a class="btn btn--cream" href="https://www.google.com/maps/dir/?api=1&destination=43.054023,-2.178607" target="_blank" rel="noopener">Cómo llegar</a>
        <a class="btn btn--line" href="tel:+34747486092">747 48 60 92</a>
        <a class="btn btn--line" href="https://wa.me/34747486092" target="_blank" rel="noopener">WhatsApp</a>
      </div>
      <h3 class="h reveal">Horario <small id="todayLabel" style="font-weight:500;opacity:.7;font-size:.9rem;margin-left:8px"></small></h3>
      <ul class="hours reveal" id="hours"></ul>
      <p class="fine">Horario orientativo: confirma por teléfono o WhatsApp antes de venir.</p>
      <div class="delivery reveal"><b>¿Pedir desde casa?</b><button class="lnk" type="button" data-wa-order style="color:var(--dark-pop);font-size:1rem">Por WhatsApp →</button><a href="{JE}" target="_blank" rel="noopener">Just Eat ↗</a></div>
    </div>
    <div class="map reveal"><iframe title="Mapa de Alma Burger en Ordizia" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.openstreetmap.org/export/embed.html?bbox=-2.1836%2C43.0515%2C-2.1736%2C43.0565&amp;layer=mapnik&amp;marker=43.054023%2C-2.178607"></iframe></div>
  </div>
</section>
<section class="sec" id="reservar">
  <div class="wrap split">
    <div><p class="kicker reveal">Reserva</p><h2 class="sec__title reveal">Guárdanos <em>tu mesa</em></h2>
      <p class="reveal" style="font-size:1.1rem;max-width:28em">Rellena los datos y se abrirá WhatsApp con tu solicitud lista para enviar. Te confirmamos lo antes posible.</p></div>
    <form class="form reveal" id="reserva">
      <label>Nombre<input name="nombre" required autocomplete="name" placeholder="Tu nombre"></label>
      <div class="form__row">
        <label>Personas<select name="personas">{''.join(f'<option>{n}</option>' for n in range(1, 13))}</select></label>
        <label>Día<input type="date" name="fecha" required></label>
      </div>
      <div class="form__row">
        <label>Hora<input type="time" name="hora" required value="21:00"></label>
        <label>Terraza o interior<select name="nota"><option value="">Me da igual</option><option>Terraza</option><option>Interior</option></select></label>
      </div>
      <button class="btn btn--solid btn--block" type="submit">Enviar solicitud por WhatsApp</button>
    </form>
  </div>
</section>'''


def nf():
    return phero('404', 'Esta página se <em>ha comido</em>', 'No encontramos lo que buscas. Pero tenemos hamburguesas: vuelve a la carta y elige una.') + """
<section class="sec" style="text-align:center"><div class="btnrow" style="justify-content:center"><a class="btn btn--solid" href="index.html">Ir al inicio</a><a class="btn" href="carta.html">Ver la carta</a></div></section>"""


TITLES = {
    'index': ('Alma Burger · Hamburguesas y desayunos en Ordizia', 'Smash burgers, picoteo, hot dogs, postres y desayunos en el corazón de Ordizia. Donde el sabor tiene alma.'),
    'alma': ('El alma · Alma Burger', 'Donde cada hamburguesa tiene alma. Ingredientes seleccionados, recetas únicas y el sabor que te hará volver. La historia de Alma Burger en Ordizia.'),
    'carta': ('La carta · Alma Burger', 'Carta completa de Alma Burger: smash burgers, para compartir, bocadillos, hot dogs, postres y menú infantil. Pide por WhatsApp.'),
    'desayunos': ('Desayunos · Alma Burger', 'Desayunos hasta las 12:00 en Ordizia: tostadas, pancakes, bowls, bollería, zumos y matcha.'),
    'galeria': ('Galería · Alma Burger', 'Las mejores fotos de los platos de Alma Burger: hamburguesas, picoteo, desayunos y postres.'),
    'visitanos': ('Visítanos · Alma Burger', 'Kale Nagusia 42, Ordizia. Horario, mapa, contacto y reserva de mesa por WhatsApp.'),
}
BODIES = {'index': home, 'alma': alma, 'carta': carta, 'desayunos': desayunos, 'galeria': galeria, 'visitanos': visitanos}
FILES = {'index': 'index.html', 'alma': 'el-alma.html', 'carta': 'carta.html', 'desayunos': 'desayunos.html', 'galeria': 'galeria.html', 'visitanos': 'visitanos.html'}

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


def main():
    for d, t in THEMES.items():
        out = ROOT / d
        if out.exists():
            shutil.rmtree(out)
        out.mkdir()
        shutil.copytree(SRC / 'img', out / 'img')
        (out / 'styles.css').write_text((SRC / 'base.css').read_text(encoding='utf-8') + '\n' + (SRC / 'pedido-v2.css').read_text(encoding='utf-8') + '\n' + (SRC / t['css']).read_text(encoding='utf-8'), encoding='utf-8')
        shutil.copy(SRC / 'app.js', out / 'app.js')
        for k, fn in BODIES.items():
            title, desc = TITLES[k]
            active = {'index': 'home', 'alma': 'alma', 'carta': 'carta', 'desayunos': 'desayunos', 'galeria': 'galeria', 'visitanos': 'visitanos'}[k]
            (out / FILES[k]).write_text(shell(active, title, desc, fn(), t['tcolor']), encoding='utf-8')
        (out / '404.html').write_text(shell('', 'Página no encontrada · Alma Burger', 'Página no encontrada', nf(), t['tcolor']), encoding='utf-8')
    (ROOT / 'index.html').write_text(SELECTOR, encoding='utf-8')
    print('ok')


main()
