"""Textos legales: Aviso legal (LSSI-CE), Política de privacidad (RGPD y LOPDGDD) y Política de cookies.
Los datos del titular salen de config.json → "legal". Lo que esté vacío se marca como pendiente."""


def _v(L, key, label):
    val = (L.get(key) or '').strip()
    return val if val else f'<mark class="ph">[{label}]</mark>'


def _page(body):
    return f'<section class="sec legal"><div class="wrap legal__in">{body}</div></section>'


def aviso(L):
    t, nif, dom, mail, tel = _v(L, 'titular', 'Nombre y apellidos o razón social'), _v(L, 'nif', 'NIF / CIF'), _v(L, 'domicilio', 'Domicilio'), _v(L, 'email', 'Email de contacto'), _v(L, 'telefono', 'Teléfono')
    reg = (L.get('registro') or '').strip()
    reg_li = f'<li><b>Datos registrales:</b> {reg}</li>' if reg else '<li><b>Datos registrales:</b> <mark class="ph">[solo si es sociedad: Registro Mercantil de Gipuzkoa, tomo, folio y hoja]</mark></li>'
    dominio = _v(L, 'dominio', 'dominio')
    return _page(f'''
<p class="legal__date">Última actualización: {_v(L, 'fecha', 'fecha')}</p>
<h2>1. Quiénes somos</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), te informamos de que el sitio web <b>{dominio}</b> pertenece a:</p>
<ul><li><b>Titular:</b> {t}</li><li><b>NIF:</b> {nif}</li><li><b>Nombre comercial:</b> ALMA Burger &amp; Breakfast</li><li><b>Domicilio:</b> {dom}</li>
<li><b>Teléfono:</b> {tel}</li><li><b>Email:</b> {mail}</li>{reg_li}</ul>

<h2>2. Para qué sirve esta web</h2>
<p>Esta web informa sobre el restaurante ALMA Burger &amp; Breakfast: su carta, sus desayunos, horarios, ubicación y formas de pedir o reservar. Al navegar por ella aceptas estas condiciones de uso.</p>

<h2>3. Carta, precios y pedidos</h2>
<p>Los precios de la carta incluyen el IVA y pueden cambiar sin previo aviso; el precio que vale es el que se confirma en el momento del pedido. Las fotos de los platos son orientativas.</p>
<p>Los pedidos online se hacen en la plataforma de pedidos del restaurante (Ágora) o en Just Eat. Cada plataforma tiene sus propias condiciones, que aceptas al usarla. Las reservas de mesa se gestionan por WhatsApp o por teléfono y quedan confirmadas cuando el restaurante responde.</p>
<p><b>Alérgenos:</b> tienes a tu disposición la información sobre alérgenos de cada plato (Reglamento UE 1169/2011). Pídela al personal antes de pedir, o indícalo en tu pedido.</p>

<h2>4. Uso de la web</h2>
<p>Te comprometes a usar la web de forma lícita y a no dañar su funcionamiento ni el de los sistemas que la alojan. Podemos cambiar sus contenidos, su diseño o estas condiciones cuando lo necesitemos.</p>

<h2>5. Propiedad intelectual</h2>
<p>Los textos, fotografías, vídeos, el logotipo de ALMA, la mascota, las ilustraciones y el diseño de esta web pertenecen a su titular o se usan con permiso. No puedes copiarlos, distribuirlos ni modificarlos con fines comerciales sin autorización. Los stickers de la mascota se ofrecen para uso personal (por ejemplo, en WhatsApp).</p>

<h2>6. Enlaces a otras webs</h2>
<p>La web enlaza con servicios de terceros (Ágora, Just Eat, WhatsApp, Instagram, TikTok, OpenStreetMap y Google Maps). No controlamos esos servicios ni respondemos de sus contenidos o de cómo tratan tus datos; consulta sus condiciones y políticas.</p>

<h2>7. Responsabilidad</h2>
<p>Cuidamos que la información sea correcta y esté al día, pero puede haber errores o cambios de última hora (horarios, platos fuera de carta, precios). Ante cualquier duda, llámanos o escríbenos antes de venir.</p>

<h2>8. Ley aplicable</h2>
<p>Estas condiciones se rigen por la ley española. Si eres consumidor, cualquier conflicto se resolverá en los juzgados de tu domicilio. En el local tienes hojas de reclamaciones a tu disposición, y también puedes dirigirte a Kontsumobide, el Instituto Vasco de Consumo (<a href="https://www.kontsumobide.euskadi.eus" target="_blank" rel="noopener">kontsumobide.euskadi.eus</a>).</p>
''')


def privacidad(L):
    t, nif, dom, mail = _v(L, 'titular', 'Nombre y apellidos o razón social'), _v(L, 'nif', 'NIF / CIF'), _v(L, 'domicilio', 'Domicilio'), _v(L, 'email', 'Email de contacto')
    return _page(f'''
<p class="legal__date">Última actualización: {_v(L, 'fecha', 'fecha')}</p>
<p class="legal__lead">Te contamos, sin letra pequeña, qué datos tuyos usamos, para qué y qué puedes hacer con ellos. Cumplimos el Reglamento General de Protección de Datos (RGPD, UE 2016/679) y la Ley Orgánica 3/2018 (LOPDGDD).</p>

<h2>1. Responsable</h2>
<ul><li><b>Responsable:</b> {t} (ALMA Burger &amp; Breakfast)</li><li><b>NIF:</b> {nif}</li><li><b>Dirección:</b> {dom}</li><li><b>Email para temas de privacidad:</b> {mail}</li></ul>

<h2>2. Qué datos usamos y para qué</h2>
<div class="legal__tbl"><table>
<thead><tr><th>Cuándo</th><th>Qué datos</th><th>Para qué</th><th>Base legal</th><th>Cuánto tiempo</th></tr></thead>
<tbody>
<tr><td>Reservas y consultas por WhatsApp o teléfono</td><td>Nombre, teléfono, día, hora, número de personas y lo que nos escribas</td><td>Gestionar tu reserva o responderte</td><td>Tu petición y la reserva (art. 6.1.b RGPD)</td><td>Hasta atender tu reserva o consulta; como máximo 12 meses</td></tr>
<tr><td>Pedidos online (plataforma Ágora)</td><td>Nombre, teléfono, dirección de entrega, pedido y datos del pago</td><td>Preparar y entregar tu pedido y cobrarlo</td><td>El contrato de compra (art. 6.1.b) y obligaciones legales (art. 6.1.c)</td><td>Lo que exija la ley fiscal y mercantil (hasta 6 años para las facturas)</td></tr>
<tr><td>Pedido por WhatsApp desde la web</td><td>Nombre, teléfono, dirección, alergias y el pedido</td><td>Preparar tu pedido y confirmarte el total</td><td>Tu petición (art. 6.1.b)</td><td>Hasta entregar el pedido, salvo obligaciones legales</td></tr>
<tr><td>Si nos mandas tu candidatura</td><td>Los datos de tu mensaje o CV</td><td>Valorarte para un puesto</td><td>Tu consentimiento (art. 6.1.a)</td><td>Como máximo 12 meses</td></tr>
<tr><td>Al visitar la web</td><td>Dirección IP y datos técnicos del navegador</td><td>Servir la web y protegerla</td><td>Interés legítimo en la seguridad (art. 6.1.f)</td><td>Lo que guarde el proveedor de alojamiento, normalmente pocos días</td></tr>
</tbody></table></div>
<p>No usamos tus datos para enviarte publicidad sin tu permiso, no hacemos perfiles y no vendemos tus datos a nadie.</p>
<p>Los datos de un pedido por WhatsApp hecho desde la web se guardan antes en tu propio navegador (para no tener que escribirlos otra vez). Puedes borrarlos cuando quieras desde la configuración del navegador. Lo explicamos en la <a href="cookies.html">política de cookies</a>.</p>

<h2>3. Quién más ve tus datos</h2>
<ul>
<li><b>Plataforma de pedidos Ágora:</b> trata los datos de los pedidos online por cuenta del restaurante, como encargado del tratamiento.</li>
<li><b>Just Eat:</b> si pides allí, Just Eat es responsable de tus datos según su propia política de privacidad.</li>
<li><b>WhatsApp (Meta):</b> si nos escribes por WhatsApp, el servicio lo presta WhatsApp Ireland Ltd. con su propia política de privacidad.</li>
<li><b>Instagram y TikTok:</b> si visitas o interactúas con nuestros perfiles, se aplican las políticas de esas redes.</li>
<li><b>Alojamiento de la web:</b> <mark class="ph">[proveedor de alojamiento definitivo]</mark>. Si el proveedor está fuera de la UE, la transferencia se ampara en el Marco de Privacidad de Datos UE-EE. UU. o en cláusulas contractuales tipo.</li>
<li><b>Administraciones públicas</b>, cuando la ley nos obligue (por ejemplo, Hacienda).</li>
</ul>

<h2>4. Tus derechos</h2>
<p>Puedes pedirnos en cualquier momento <b>ver</b> tus datos, <b>corregirlos</b>, <b>borrarlos</b>, <b>oponerte</b> a que los usemos, <b>limitar</b> su uso o <b>llevártelos</b> a otro sitio (portabilidad). Si nos diste tu consentimiento, puedes retirarlo cuando quieras.</p>
<p>Escríbenos a {mail} o pásate por {dom} e indica qué derecho quieres ejercer. Te responderemos en un mes como máximo. Si crees que no hemos tratado bien tus datos, puedes reclamar ante la Agencia Española de Protección de Datos: <a href="https://www.aepd.es" target="_blank" rel="noopener">www.aepd.es</a>.</p>

<h2>5. Menores</h2>
<p>Los menores de 14 años necesitan el permiso de su padre, madre o tutor para darnos sus datos.</p>

<h2>6. Seguridad</h2>
<p>Aplicamos medidas técnicas y organizativas razonables para proteger tus datos: la web se sirve cifrada (HTTPS) y solo accede a los pedidos y reservas el personal que los necesita.</p>
''')


def cookies(L):
    return _page(f'''
<p class="legal__date">Última actualización: {_v(L, 'fecha', 'fecha')}</p>
<p class="legal__lead"><b>Cookies, las justas.</b> Esta web no usa cookies de publicidad ni de análisis, y no te sigue por internet. Solo guarda en tu navegador lo necesario para que funcione, y carga el mapa si tú lo aceptas.</p>

<h2>1. Qué son</h2>
<p>Las cookies y el almacenamiento local son pequeños datos que una web guarda en tu navegador para recordar cosas, como tu pedido o el color con el que prefieres ver la web.</p>

<h2>2. Lo que guarda esta web</h2>
<p>Todo es propio, se queda en tu navegador y nunca se envía a nadie. Al ser técnico o elegido por ti, no necesita tu consentimiento (artículo 22.2 de la LSSI-CE).</p>
<div class="legal__tbl"><table>
<thead><tr><th>Nombre</th><th>Tipo</th><th>Para qué</th><th>Duración</th></tr></thead>
<tbody>
<tr><td><code>alma-color</code></td><td>Preferencia</td><td>Recordar si ves la web en azul o en negro</td><td>Hasta que lo borres</td></tr>
<tr><td><code>alma-cart2</code></td><td>Técnica</td><td>Guardar los platos de tu pedido mientras navegas</td><td>Hasta que lo vacíes o lo borres</td></tr>
<tr><td><code>alma-cust</code></td><td>Técnica</td><td>Recordar tu nombre, teléfono y dirección para tu próximo pedido por WhatsApp</td><td>Hasta que lo borres</td></tr>
<tr><td><code>alma-mascota</code></td><td>Preferencia</td><td>Recordar si has silenciado a la mascota</td><td>Hasta que lo borres</td></tr>
<tr><td><code>alma-consent</code></td><td>Técnica</td><td>Recordar lo que elegiste en el aviso de cookies</td><td>12 meses; luego te lo volvemos a preguntar</td></tr>
</tbody></table></div>

<h2>3. Contenido de otras webs</h2>
<div class="legal__tbl"><table>
<thead><tr><th>Servicio</th><th>Para qué</th><th>Cuándo se carga</th></tr></thead>
<tbody>
<tr><td>Mapa de OpenStreetMap (OpenStreetMap Foundation)</td><td>Mostrar dónde estamos en la página Visítanos</td><td>Solo si aceptas en el aviso, o si pulsas «Cargar el mapa»</td></tr>
</tbody></table></div>
<p>La tipografía, las fotos y los vídeos se sirven desde esta misma web: no conectamos con Google Fonts ni con Instagram mientras navegas.</p>
<p>Los botones de Ágora, Just Eat, WhatsApp, Instagram, TikTok y Google Maps son enlaces normales: no cargan nada hasta que los pulsas. Al pulsarlos sales de esta web y se aplican las cookies de ese servicio.</p>

<h2>4. Cambiar de opinión</h2>
<p>Puedes cambiar lo que elegiste cuando quieras:</p>
<p><button class="btn btn--solid" type="button" data-cookies>Configurar cookies</button></p>
<p>También puedes borrar todo lo guardado desde tu navegador, en Configuración → Privacidad → Borrar datos de navegación (o «Datos de sitios web» en Safari).</p>
<!-- Nota: si algún día se añade analítica (Google Analytics, píxel de Meta…), hay que añadir esa categoría al aviso y no cargarla hasta que se acepte. -->
''')
