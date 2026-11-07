"""Versión en euskera de la web.

TXT  : textos de las páginas (HTML tal cual aparece entre etiquetas)
ATTR : textos de atributos (alt, aria-label, placeholder, descripciones…)
RAW  : cambios literales para trozos que no son un texto completo
JS   : frases que pinta app.js (carta, horario, mascota, test, aviso de cookies…)

Traducción preparada para la demo: conviene que la revise alguien nativo antes de publicarla.
Los nombres propios de los platos (La Reinita, La Dori…) no se traducen.
"""

DAYS = {'Domingo': 'Igandea', 'Lunes': 'Astelehena', 'Martes': 'Asteartea', 'Miércoles': 'Asteazkena',
        'Jueves': 'Osteguna', 'Viernes': 'Ostirala', 'Sábado': 'Larunbata'}

# ---------------------------------------------------------------- textos de las páginas
TXT = {
    # cabecera, pie y navegación
    'Página no encontrada · Alma Burger': 'Orria ez da aurkitu · Alma Burger',
    'Saltar al contenido': 'Joan edukira',
    'El alma': 'Gure arima',
    'Hamburguesas': 'Hanburgesak',
    'Desayunos': 'Gosariak',
    'Galería': 'Galeria',
    'Visítanos': 'Bisitatu gaitzazu',
    'Pedido': 'Eskaera',
    'Pedir online ↗': 'Eskatu online ↗',
    'Pedir online': 'Eskatu online',
    'Inicio': 'Hasiera',
    'Burgers': 'Burgerrak',
    'Contacto': 'Harremana',
    'Explora': 'Arakatu',
    'No es solo comida. Es ALMA.': 'Ez da janaria bakarrik. ALMA da.',
    'Hamburguesas, desayunos, cafés especiales y postres en el corazón de Ordizia. Todo lo que somos, en cada bocado.':
        'Hanburgesak, gosariak, kafe bereziak eta postreak Ordiziaren bihotzean. Garen guztia, ahokada bakoitzean.',
    'Instagram @almaburgers': 'Instagram @almaburgers',
    '¿Desayuno o <em>hamburguesa</em>?': 'Gosaria ala <em>hanburgesa</em>?',
    'Ver la carta': 'Ikusi karta',
    'Ver la web en azul': 'Ikusi webgunea urdinez',
    'Ver la web en negro': 'Ikusi webgunea beltzez',
    'Aviso legal': 'Lege oharra',
    'Privacidad': 'Pribatutasuna',
    'Cookies': 'Cookieak',
    'Configurar cookies': 'Cookieen ezarpenak',
    'Ver mi pedido': 'Ikusi nire eskaera',
    # 404
    'Esta página se <em>ha comido</em>': 'Orri hau <em>jan egin dugu</em>',
    'No encontramos lo que buscas. Pero tenemos hamburguesas: vuelve a la carta y elige una.':
        'Ez dugu aurkitu bilatzen ari zarena. Baina hanburgesak baditugu: itzuli kartara eta aukeratu bat.',
    'Ir al inicio': 'Joan hasierara',
    # carta
    'Hamburguesas y carta · Alma Burger': 'Hanburgesak eta karta · Alma Burger',
    'Elige tu <em>perdición</em>': 'Aukeratu zure <em>tentazioa</em>',
    'Smash burgers, pollo crispy, picoteo, bocadillos, hot dogs y tartas de queso.':
        'Smash burgerrak, oilasko crispya, mokadutxoak, ogitartekoak, hot dogak eta gazta-tartak.',
    'Hamburguesas y carta': 'Hanburgesak eta karta',
    'Recoger o a domicilio': 'Jasotzeko edo etxera',
    'Filtros': 'Iragazkiak',
    '¿Qué burger eres?': 'Zein burger zara?',
    'Sorpréndeme': 'Harritu nazazu',
    'Suplemento por cada ingrediente extra. Consulta nuestra <b>carta de alérgenos</b> al personal. Algunas imágenes son ilustrativas.':
        'Osagai gehigarri bakoitzak ordaindu egiten da. Eskatu langileei <b>alergenoen karta</b>. Irudi batzuk orientagarriak dira.',
    # desayunos
    'Desayunos con pasión · Alma Burger': 'Gosariak grinaz · Alma Burger',
    'Desayunos <em>con pasión</em>': 'Gosariak <em>grinaz</em>',
    'Hasta las 12:00 (de lunes a viernes desde las 8:00; sábado y domingo desde las 9:00). Tostadas, pancakes, bowls, cafés especiales y matcha, hechos con las mismas ganas que nuestras hamburguesas.':
        '12:00ak arte (astelehenetik ostiralera 8:00etatik; larunbat eta igandeetan 9:00etatik). Txigorkiak, pancakeak, bowlak, kafe bereziak eta matcha, gure hanburgesen gogo berberarekin eginak.',
    'Para empezar bien el día': 'Eguna ondo hasteko',
    'Tostadas, pancakes <em>y matcha</em>': 'Txigorkiak, pancakeak <em>eta matcha</em>',
    'Tostadas con toppings de verdad, pancakes golosos, bowls, zumos, smoothies y unos matchas que no vas a poder dejar de pedir.':
        'Benetako toppingak dituzten txigorkiak, pancake gozoak, bowlak, zukuak, smoothieak eta eskatzeari utzi ezingo diozun matchak.',
    'Tostada de salmón y mascarpone': 'Izokin eta mascarpone txigorkia',
    'Pancakes de Ferrero': 'Ferrero pancakeak',
    'Matcha de mango': 'Mango matcha',
    'Los favoritos': 'Gogokoenak',
    'La carta de <em>desayunos</em>': 'Gosarien <em>karta</em>',
    'Desayunos de lunes a viernes de 8:00 a 12:00, y sábado y domingo de 9:00 a 12:00. Consulta nuestra <b>carta de alérgenos</b> al personal.':
        'Gosariak astelehenetik ostiralera 8:00etatik 12:00etara, eta larunbat eta igandeetan 9:00etatik 12:00etara. Eskatu langileei <b>alergenoen karta</b>.',
    # el alma
    'El alma · Alma Burger': 'Gure arima · Alma Burger',
    'No es solo comida. <em>Es ALMA.</em>': 'Ez da janaria bakarrik. <em>ALMA da.</em>',
    'La historia de quienes estamos detrás: nuestras raíces, nuestra familia y las ganas de crear algo propio.':
        'Atzean gaudenon istorioa: gure sustraiak, gure familia eta zerbait geurea sortzeko gogoa.',
    'El nombre': 'Izena',
    'El origen': 'Jatorria',
    'Más que una hamburguesería': 'Hanburgesategi bat baino gehiago',
    'Salir de lo convencional': 'Ohikotik ateratzea',
    'Detrás de todo': 'Guztiaren atzean',
    'Cómo somos': 'Nolakoak garen',
    'ALMA no es solo <em>un nombre</em>': 'ALMA ez da <em>izen bat bakarrik</em>',
    'ALMA no es simplemente el nombre de nuestra hamburguesería. Es una parte de nosotros, de nuestras raíces y de nuestra familia.':
        'ALMA ez da gure hanburgesategiaren izena besterik gabe. Gure zati bat da, gure sustraiena eta gure familiarena.',
    'Cada letra tiene un significado especial:': 'Letra bakoitzak esanahi berezia du:',
    'apellido del padre de Lidia': 'Lidiaren aitaren abizena',
    'madre de Abrahan': 'Abrahanen ama',
    'Moreno, apellido del padre de Lidia': 'Moreno, Lidiaren aitaren abizena',
    'Maritza, madre de Abrahan': 'Maritza, Abrahanen ama',
    'Nuestros nombres, <em>nuestras raíces</em>': 'Gure izenak, <em>gure sustraiak</em>',
    'De la unión de nuestros nombres y nuestras raíces nació ALMA.': 'Gure izenen eta sustraien elkarketatik jaio zen ALMA.',
    'Un proyecto que representa nuestra ilusión por emprender juntos y crear algo propio.':
        'Elkarrekin ekiteko eta zerbait geurea sortzeko dugun ilusioa adierazten duen proiektua.',
    'Un lugar con <em>personalidad</em>': '<em>Nortasuna</em> duen lekua',
    'Queríamos construir mucho más que una hamburguesería. Un lugar con personalidad, donde la creatividad, los sabores atrevidos y las ganas de sorprender estuvieran presentes en cada detalle.':
        'Hanburgesategi bat baino askoz gehiago eraiki nahi genuen. Nortasuna duen leku bat, non sormena, zapore ausartak eta harritzeko gogoa xehetasun guztietan egongo liratekeen.',
    'La creatividad': 'Sormena',
    'Los sabores atrevidos': 'Zapore ausartak',
    'Las ganas de sorprender': 'Harritzeko gogoa',
    'Presentes en cada detalle.': 'Xehetasun bakoitzean.',
    'Nuevas combinaciones, <em>experiencias diferentes</em>': 'Konbinazio berriak, <em>esperientzia desberdinak</em>',
    'En ALMA nos gusta salir de lo convencional, experimentar con nuevas combinaciones y ofrecer experiencias diferentes, desde nuestras hamburguesas más originales hasta nuestros desayunos, cafés especiales y nuevas creaciones.':
        'ALMAn ohikotik ateratzea gustatzen zaigu, konbinazio berriekin esperimentatzea eta esperientzia desberdinak eskaintzea: gure hanburgesa originalenetatik hasi eta gosari, kafe berezi eta sorkuntza berrietaraino.',
    'Hamburguesas más originales': 'Hanburgesa originalenak',
    'Cafés especiales': 'Kafe bereziak',
    'Nuevas creaciones': 'Sorkuntza berriak',
    'Detrás de todo esto': 'Honen guztiaren atzean',
    'Lo que nos <em>mueve</em>': 'Mugitzen <em>gaituena</em>',
    'Esfuerzo': 'Ahalegina',
    'Dedicación': 'Dedikazioa',
    'Ilusión': 'Ilusioa',
    'Y muchísimas ganas de seguir creciendo': 'Eta hazten jarraitzeko gogo izugarria',
    'Nuestra filosofía': 'Gure filosofia',
    'No queremos ser una hamburguesería <em>más</em>': 'Ez dugu <em>beste</em> hanburgesategi bat izan nahi',
    'Queremos que ALMA tenga identidad propia, que la gente nos recuerde por nuestros sabores, nuestra creatividad y nuestra manera de hacer las cosas.':
        'ALMAk nortasun propioa izatea nahi dugu, eta jendeak gure zaporeengatik, gure sormenagatik eta gauzak egiteko dugun moduagatik gogora gaitzan.',
    'Nuestra personalidad de marca': 'Gure marka-nortasuna',
    'Moderna': 'Modernoa',
    'Atrevida': 'Ausarta',
    'Creativa': 'Sortzailea',
    'Cercana': 'Hurbila',
    'Pero sin perder nunca nuestra esencia familiar.': 'Baina gure familia-izaera inoiz galdu gabe.',
    'Las caras de ALMA': 'ALMAren aurpegiak',
    'El <em>equipo</em>': '<em>Taldea</em>',
    'Ejemplo · pendiente de fotos y datos reales': 'Adibidea · benetako argazki eta datuen zain',
    'Quién está detrás de cada burger y cada café. Aquí irán las fotos del equipo, su puesto y su plato favorito de la carta.':
        'Nor dagoen burger eta kafe bakoitzaren atzean. Hemen joango dira taldearen argazkiak, bakoitzaren lanpostua eta kartako plater gogokoena.',
    'Cofundador · cocina': 'Sortzailekidea · sukaldea',
    'Cofundadora · desayunos y sala': 'Sortzailekidea · gosariak eta jangela',
    'Su favorita: <b>por confirmar</b>': 'Gogokoena: <b>berresteko</b>',
    'Su favorito: <b>por confirmar</b>': 'Gogokoena: <b>berresteko</b>',
    'Nombre': 'Izena',
    'Plancha y smash burgers': 'Plantxa eta smash burgerrak',
    'Barra, cafés y matcha': 'Barra, kafeak eta matcha',
    '«ALMA nació de nuestras raíces, creció con nuestros sueños y hoy queremos compartirla contigo.»':
        '«ALMA gure sustraietatik jaio zen, gure ametsekin hazi zen, eta gaur zurekin partekatu nahi dugu.»',
    'ALMA — Todo lo que somos, en cada bocado. ♥': 'ALMA — Garen guztia, ahokada bakoitzean. ♥',
    'Ver hamburguesas': 'Ikusi hanburgesak',
    'Ver desayunos': 'Ikusi gosariak',
    'hamburguesas en carta': 'hanburgesa kartan',
    'desayunos y bebidas': 'gosari eta edari',
    'abrimos con café y desayunos': 'kafearekin eta gosariekin irekitzen dugu',
    'mascota con gafas': 'betaurrekodun maskota',
    'El método': 'Metodoa',
    '¿Qué es una <em>smash burger</em>?': 'Zer da <em>smash burger</em> bat?',
    'Una bola de carne': 'Haragi-bola bat',
    'Cada burger empieza con una bola de carne que va directa a una plancha muy caliente.':
        'Burger bakoitza haragi-bola batekin hasten da, eta zuzenean plantxa oso bero batera doa.',
    'Se aplasta (smash)': 'Zanpatu egiten da (smash)',
    'Al aplastarla contra la plancha se forma una costra crujiente que concentra todo el sabor.':
        'Plantxaren kontra zanpatzean azal kurruskari bat sortzen da, zapore guztia biltzen duena.',
    'Queso y a la mesa': 'Gazta, eta mahaira',
    'Cheddar fundido, tus toppings favoritos y directa del fuego a tu plato.':
        'Cheddar urtua, zure topping gogokoenak, eta sutatik zuzenean zure platerera.',
    'Más que hamburguesas': 'Hanburgesak baino gehiago',
    'De 8:00 de la mañana <em>a la noche</em>': 'Goizeko 8:00etatik <em>gauera arte</em>',
    'Empezamos el día con café, tostadas y pancakes, seguimos con bocadillos y hot dogs, y cerramos con smash burgers, picoteo y tartas de queso.':
        'Eguna kafearekin, txigorkiekin eta pancakeekin hasten dugu, ogitarteko eta hot dogekin jarraitzen dugu, eta smash burger, mokadutxo eta gazta-tartekin amaitzen.',
    'Preguntas frecuentes': 'Ohiko galderak',
    'Lo que <em>nos preguntáis</em>': '<em>Galdetzen diguzuena</em>',
    '¿Tenéis opciones vegetarianas?': 'Aukera begetarianorik baduzue?',
    'Sí: la Gordi Deluxe tiene opción vegetariana, además de ensalada con burrata, tortilla de patata y varias tostadas. Y cualquier burger se puede adaptar a vegetariana.':
        'Bai: Gordi Deluxek aukera begetarianoa du, eta horrez gain burrata-entsalada, patata-tortilla eta hainbat txigorki ditugu. Gainera, edozein burger begetariano bihur daiteke.',
    '¿Y alérgenos?': 'Eta alergenoak?',
    'Tenemos carta de alérgenos: pídesela a nuestro equipo y te ayudamos a elegir con tranquilidad.':
        'Alergenoen karta badugu: eskatu gure taldeari eta lasai aukeratzen lagunduko dizugu.',
    '¿Hacéis entrega a domicilio?': 'Etxera eramaten duzue?',
    'Sí, por la noche: miércoles, jueves y domingo de 19:30 a 23:00, y viernes y sábado de 19:30 a 23:30. Pulsa «Pedir online», elige «A domicilio» y pon tu dirección. Los desayunos no tienen reparto.':
        'Bai, gauez: asteazken, ostegun eta igandeetan 19:30etik 23:00etara, eta ostiral eta larunbatetan 19:30etik 23:30era. Sakatu «Eskatu online», aukeratu «Etxera» eta idatzi zure helbidea. Gosariak ez dira etxera eramaten.',
    '¿Hay menú infantil?': 'Haurrentzako menurik ba al dago?',
    'Sí: pechuga empanada, lomo o hamburguesa con queso, siempre con patatas y croquetas, por 9,00€.':
        'Bai: oilasko-bular ogiztatua, solomoa edo gaztadun hanburgesa, beti patatekin eta kroketekin, 9,00 €-an.',
    '¿Hasta qué hora hay desayunos?': 'Zer ordutara arte daude gosariak?',
    'Hasta las 12:00: de lunes a viernes desde las 8:00, y sábado y domingo desde las 9:00. Los lunes y martes solo abrimos para desayunos.':
        '12:00ak arte: astelehenetik ostiralera 8:00etatik, eta larunbat eta igandeetan 9:00etatik. Astelehen eta asteartetan gosarietarako bakarrik irekitzen dugu.',
    # galería
    'Galería · Alma Burger': 'Galeria · Alma Burger',
    'Mejor verlo <em>que contarlo</em>': 'Hobe ikustea <em>kontatzea baino</em>',
    'Un paseo por nuestros platos. Pulsa en cualquier foto para verla en grande.':
        'Ibilaldi bat gure plateretan zehar. Sakatu edozein argazki handiago ikusteko.',
    'Desde la <em>cocina</em>': '<em>Sukaldetik</em> zuzenean',
    '@almaburgers en Instagram ↗': '@almaburgers Instagramen ↗',
    'Picoteo con alma': 'Arimadun mokadutxoak',
    'Queso de cabra': 'Ahuntz-gazta',
    'Patatas trufadas': 'Patata trufatuak',
    'Hasta las 12:00': '12:00ak arte',
    'Desayunos <em>en fotos</em>': 'Gosariak <em>argazkitan</em>',
    'Ver los desayunos →': 'Ikusi gosariak →',
    'Pancakes de Nutella': 'Nutella pancakeak',
    'Tostada de salmón': 'Izokin-txigorkia',
    'Matcha goloso': 'Matcha goxoa',
    'Desayuno con pasión': 'Gosaria grinaz',
    'ALMA <em>en vídeo</em>': 'ALMA <em>bideoan</em>',
    'Desde la cocina de ALMA': 'ALMAren sukaldetik',
    'Desayunos con pasión': 'Gosariak grinaz',
    'Llega el chocolate caliente': 'Txokolate beroa iritsi da',
    'Croquetas caseras': 'Etxeko kroketak',
    'This is Halloween en ALMA': 'This is Halloween ALMAn',
    'Algo muy oscuro se cocina…': 'Zerbait oso iluna ari da prestatzen…',
    '← Desliza para ver más vídeos →': '← Irristatu bideo gehiago ikusteko →',
    'Lo último en Instagram': 'Instagrameko azkenak',
    'Últimas <em>publicaciones</em>': 'Azken <em>argitalpenak</em>',
    'Seguir en Instagram ↗': 'Jarraitu Instagramen ↗',
    'Nueva tarta de queso: Nutella y Chips Ahoy': 'Gazta-tarta berria: Nutella eta Chips Ahoy',
    'Green Tropical, el matcha del momento': 'Green Tropical, uneko matcha',
    'Blue Paradise, matcha de colores': 'Blue Paradise, koloretako matcha',
    'Halloween: rasca y descubre tu sorpresa': 'Halloween: hazka eta ezagutu zure ezustekoa',
    '¿Truco o burger?': 'Trikimailua ala burgerra?',
    'Algo muy oscuro se cocina en ALMA': 'Zerbait oso iluna ari da prestatzen ALMAn',
    'Se acerca Halloween': 'Halloween gerturatzen ari da',
    'Alitas teriyaki': 'Teriyaki hegaltxoak',
    'Croquetas caseras de ALMA': 'ALMAren etxeko kroketak',
    'El picoteo también tiene ALMA': 'Mokadutxoek ere badute ALMA',
    'Para tu móvil': 'Zure mugikorrerako',
    'Stickers de <em>ALMA</em>': '<em>ALMAren</em> stickerrak',
    'Descargar todos (ZIP)': 'Deskargatu denak (ZIP)',
    'La mascota para mandar por WhatsApp: guarda la imagen y compártela, o añade los archivos <b>.webp</b> con una app de stickers como Sticker Maker.':
        'Maskota WhatsAppez bidaltzeko: gorde irudia eta partekatu, edo gehitu <b>.webp</b> fitxategiak sticker-aplikazio batekin, Sticker Maker adibidez.',
    '¡Hola!': 'Kaixo!',
    '¡Marchando!': 'Martxan!',
    'Buenos días': 'Egun on',
    '¡Esta pica!': 'Honek pikatzen du!',
    'Gracias': 'Eskerrik asko',
    'Tengo hambre': 'Gose naiz',
    '¡A comer!': 'Jatera!',
    'De cerca': 'Gertutik',
    'Las hamburguesas, <em>una a una</em>': 'Hanburgesak, <em>banan-banan</em>',
    'Ver la carta completa': 'Ikusi karta osoa',
    # portada
    'Alma Burger · Hamburguesas y desayunos en Ordizia': 'Alma Burger · Hanburgesak eta gosariak Ordizian',
    'Hamburguesería · Ordizia': 'Hanburgesategia · Ordizia',
    'No es solo comida. Es <em>ALMA</em>. Hamburguesas de recetas propias y desayunos con personalidad: dos formas de disfrutar el mismo sabor.':
        'Ez da janaria bakarrik. <em>ALMA</em> da. Geure errezetetako hanburgesak eta nortasuna duten gosariak: zapore bera gozatzeko bi modu.',
    'Buenos días. Es hora de <em>desayunar</em>: tostadas con toppings de verdad, pancakes, matcha y café de especialidad hasta las 12:00. Y a mediodía, hamburguesas con ALMA.':
        'Egun on. <em>Gosaltzeko</em> ordua da: benetako toppingak dituzten txigorkiak, pancakeak, matcha eta espezialitateko kafea 12:00ak arte. Eta eguerdian, hanburgesak ALMArekin.',
    '<b>17</b> hamburguesas': '<b>17</b> hanburgesa',
    '<b>41</b> desayunos y bebidas': '<b>41</b> gosari eta edari',
    '<b>8:00</b> abrimos con café': '<b>8:00</b> kafearekin irekitzen dugu',
    'Burger del mes · La Reinita': 'Hilabeteko burgerra · La Reinita',
    'Desayunos · hasta las 12:00': 'Gosariak · 12:00ak arte',
    'Picoteo': 'Mokadutxoak',
    'Hot dogs': 'Hot dogak',
    'Pancakes': 'Pancakeak',
    'Tostadas': 'Txigorkiak',
    'Tartas de queso': 'Gazta-tartak',
    'Café de especialidad': 'Espezialitateko kafea',
    'Dos formas de disfrutar ALMA': 'ALMA gozatzeko bi modu',
    'Hamburguesas <em>y desayunos</em>': 'Hanburgesak <em>eta gosariak</em>',
    'Del mediodía a la noche': 'Eguerditik gauera',
    'Smash burgers de recetas propias, pollo crispy, hot dogs, picoteo y tartas de queso.':
        'Geure errezetetako smash burgerrak, oilasko crispya, hot dogak, mokadutxoak eta gazta-tartak.',
    'Ver hamburguesas →': 'Ikusi hanburgesak →',
    'Tostadas con toppings de verdad, pancakes, bowls, cafés especiales y los matchas del momento.':
        'Benetako toppingak dituzten txigorkiak, pancakeak, bowlak, kafe bereziak eta uneko matchak.',
    'Ver desayunos →': 'Ikusi gosariak →',
    'Nuestra historia': 'Gure istorioa',
    'De la unión de nuestros nombres y nuestras raíces nació ALMA, un proyecto que representa nuestra ilusión por emprender juntos y crear algo propio.':
        'Gure izenen eta sustraien elkarketatik jaio zen ALMA, elkarrekin ekiteko eta zerbait geurea sortzeko dugun ilusioa adierazten duen proiektua.',
    'Queríamos construir mucho más que una hamburguesería. Un lugar con personalidad, donde la creatividad, los sabores atrevidos y las ganas de sorprender estuvieran presentes en cada detalle.':
        'Hanburgesategi bat baino askoz gehiago eraiki nahi genuen. Nortasuna duen leku bat, non sormena, zapore ausartak eta harritzeko gogoa xehetasun guztietan egongo liratekeen.',
    'ALMA nació de nuestras raíces, creció con nuestros sueños y hoy queremos compartirla contigo.':
        'ALMA gure sustraietatik jaio zen, gure ametsekin hazi zen, eta gaur zurekin partekatu nahi dugu.',
    'Seguir leyendo ↓': 'Irakurtzen jarraitu ↓',
    'Toda nuestra historia': 'Gure istorio osoa',
    'Hamburguesas · lo más pedido': 'Hanburgesak · eskatuenak',
    'Para empezar <em>fuerte</em>': '<em>Indartsu</em> hasteko',
    'Todas las hamburguesas →': 'Hanburgesa guztiak →',
    'Todos los desayunos →': 'Gosari guztiak →',
    'Más en la galería →': 'Gehiago galerian →',
    'Test de 30 segundos': '30 segundoko testa',
    '¿Qué burger <em>eres</em>?': 'Zein burger <em>zara</em>?',
    'Contesta cinco preguntas y te decimos cuál pedir. Puedes mandarle el resultado a quien quieras.':
        'Erantzun bost galderari eta zein eskatu esango dizugu. Emaitza nahi duzunari bidal diezaiokezu.',
    'Hacer el test': 'Egin testa',
    'Ver todas las burgers': 'Ikusi burger guztiak',
    'Pedir es fácil': 'Eskatzea erraza da',
    'Elige cómo <em>quieres pedir</em>': 'Aukeratu nola <em>eskatu nahi duzun</em>',
    'Recoger o domicilio': 'Jaso edo etxera',
    'Elige tus platos, para recoger o a domicilio. Llega directo a la cocina. De momento, el pago se hace en el local.':
        'Aukeratu zure platerak, jasotzeko edo etxera. Zuzenean sukaldera iristen da. Oraingoz, ordainketa lokalean egiten da.',
    'Dudas': 'Zalantzak',
    'Escríbenos': 'Idatzi iezaguzu',
    '¿Alguna pregunta sobre la carta, los alérgenos o el horario? Llámanos o mándanos un mensaje.':
        'Kartari, alergenoei edo ordutegiari buruzko galderarik? Deitu edo bidali mezu bat.',
    'Contactar': 'Harremanetan jarri',
    '1 · Elige tus platos': '1 · Aukeratu zure platerak',
    'Mira la carta y entra en «Pedir online». Allí eliges los platos con sus opciones.':
        'Begiratu karta eta sartu «Eskatu online» atalean. Han aukeratuko dituzu platerak eta haien aukerak.',
    '2 · Completa tus datos': '2 · Bete zure datuak',
    'Nombre, teléfono, si lo recoges o lo llevamos a casa, y la hora.':
        'Izena, telefonoa, zuk jasoko duzun ala etxera eramango dizugun, eta ordua.',
    '3 · Confirma y listo': '3 · Berretsi, eta kitto',
    'Terminas el pedido en nuestra página de pedidos y llega directo a la cocina.':
        'Eskaera gure eskaera-orrian amaitzen duzu, eta zuzenean sukaldera iristen da.',
    'Burger del mes 👑': 'Hilabeteko burgerra 👑',
    'Una reina con mucho carácter y sabor venezolano: carne smash jugosa, cheddar bien fundido, panceta crujiente, nuestra salsa ajonesa y la auténtica protagonista, el topping de reina pepiada, con pollo deshilachado, aguacate, cebolla morada, cilantro y una mezcla cremosa irresistible.':
        'Izaera handiko erregina, Venezuelako zaporearekin: haragi smash mamitsua, ondo urtutako cheddarra, hirugiharra kurruskaria, gure ajonesa saltsa eta benetako protagonista, reina pepiada toppinga: oilasko xehatua, ahuakatea, tipula gorria, koriandroa eta nahasketa krematsu ezin hobea.',
    'La Reinita no viene a participar, viene a reinar.': 'La Reinita ez dator parte hartzera, erreinatzera dator.',
    'Verla en Instagram ↗': 'Ikusi Instagramen ↗',
    'Y La Puerquita se queda en la carta como novedad.': 'Eta La Puerquita kartan geratzen da, berritasun gisa.',
    'Descubre': 'Ezagutu',
    'Todo Alma, <em>en un vistazo</em>': 'Alma osoa, <em>begirada batean</em>',
    'Smash burgers, picoteo, bocadillos, hot dogs y postres.': 'Smash burgerrak, mokadutxoak, ogitartekoak, hot dogak eta postreak.',
    'Tostadas, pancakes, bowls y matcha hasta las 12:00.': 'Txigorkiak, pancakeak, bowlak eta matcha 12:00ak arte.',
    'Nuestra historia.': 'Gure istorioa.',
    'Mejor verlo que contarlo.': 'Hobe ikustea kontatzea baino.',
    # visítanos
    'Visítanos · Alma Burger': 'Bisitatu gaitzazu · Alma Burger',
    'Ven a <em>vernos</em>': 'Etorri <em>gu ikustera</em>',
    'En pleno centro de Ordizia, con terraza. Pide online o déjate caer.': 'Ordiziaren erdi-erdian, terrazarekin. Eskatu online edo pasa zaitez.',
    'Dónde estamos': 'Non gauden',
    'Horario': 'Ordutegia',
    'Cómo llegar': 'Nola iritsi',
    'La hora de cierre puede variar según el día. Si vienes tarde, llámanos o escríbenos antes.':
        'Itxiera-ordua egunaren arabera alda daiteke. Berandu etortzekotan, deitu edo idatzi lehenago.',
    'Reparto a domicilio': 'Etxera banaketa',
    'Miércoles, jueves y domingo': 'Asteazkena, osteguna eta igandea',
    'Viernes y sábado': 'Ostirala eta larunbata',
    'Lunes y martes': 'Astelehena eta asteartea',
    'Sin reparto': 'Banaketarik ez',
    'Los desayunos no tienen reparto. De momento, los pedidos online se pagan en el local.':
        'Gosariak ez dira etxera eramaten. Oraingoz, online eskaerak lokalean ordaintzen dira.',
    '¿Pedir desde casa?': 'Etxetik eskatu?',
    'El mapa lo sirve OpenStreetMap. Se carga solo si lo pides.': 'Mapa OpenStreetMapek eskaintzen du. Zuk eskatzen baduzu bakarrik kargatzen da.',
    'Cargar el mapa': 'Kargatu mapa',
    'Abrir en Google Maps ↗': 'Ireki Google Mapsen ↗',
    '¿Tienes alguna <em>duda</em>?': '<em>Zalantzarik</em> baduzu?',
    'Si quieres preguntarnos algo sobre la carta, los alérgenos o el horario, llámanos o escríbenos y te respondemos lo antes posible.':
        'Kartari, alergenoei edo ordutegiari buruz zerbait galdetu nahi badiguzu, deitu edo idatzi, eta ahalik eta lasterren erantzungo dizugu.',
    'Llámanos': 'Deitu iezaguzu',
    'Escríbenos por WhatsApp': 'Idatzi WhatsAppez',
    'Para consultas y dudas': 'Kontsulta eta zalantzetarako',
    'Los pedidos se hacen en «Pedir online».': 'Eskaerak «Eskatu online» atalean egiten dira.',
}

# ---------------------------------------------------------------- atributos
ATTR = {
    'Página no encontrada': 'Orria ez da aurkitu',
    'ALMA Burger & Breakfast: hamburguesas y desayunos en Ordizia': 'ALMA Burger & Breakfast: hanburgesak eta gosariak Ordizian',
    'ALMA Burger & Breakfast, inicio': 'ALMA Burger & Breakfast, hasiera',
    'Principal': 'Nagusia',
    'Abrir menú': 'Ireki menua',
    'Migas de pan': 'Ogi-apurrak',
    'Información legal': 'Lege-informazioa',
    'Escríbenos por WhatsApp': 'Idatzi WhatsAppez',
    'Acceso rápido': 'Sarbide azkarra',
    'Carta completa de Alma Burger: smash burgers, para compartir, bocadillos, hot dogs, postres y menú infantil. Pide online.':
        'Alma Burgerren karta osoa: smash burgerrak, partekatzekoak, ogitartekoak, hot dogak, postreak eta haurrentzako menua. Eskatu online.',
    'Un perrito caliente sonriente leyendo la carta': 'Hot dog irribarretsu bat karta irakurtzen',
    'Busca: cabra, trufa, picante…': 'Bilatu: ahuntza, trufa, pikantea…',
    'Buscar en la carta': 'Bilatu kartan',
    'Categorías de la carta': 'Kartako kategoriak',
    'Filtros': 'Iragazkiak',
    'Desayunos con pasión hasta las 12:00 en Ordizia: tostadas con toppings de verdad, pancakes, bowls, cafés especiales, zumos y matcha.':
        'Gosariak grinaz 12:00ak arte Ordizian: benetako toppingak dituzten txigorkiak, pancakeak, bowlak, kafe bereziak, zukuak eta matcha.',
    'La mascota de ALMA sentada en un taburete con un café': 'ALMAren maskota aulki batean eserita, kafe batekin',
    'Pancakes de nutella con fresas': 'Nutella pancakeak marrubiekin',
    'Matcha con leche': 'Matcha esnearekin',
    'Pancakes de Ferrero Rocher': 'Ferrero Rocher pancakeak',
    'Busca: matcha, croissant, salmón…': 'Bilatu: matcha, croissanta, izokina…',
    'Buscar en desayunos': 'Bilatu gosarietan',
    'Secciones de desayuno': 'Gosari-atalak',
    'No es solo comida. Es ALMA. La historia de Alma Burger: nuestras raíces, nuestra familia y por qué hacemos hamburguesas y desayunos con identidad propia.':
        'Ez da janaria bakarrik. ALMA da. Alma Burgerren istorioa: gure sustraiak, gure familia, eta zergatik egiten ditugun nortasun propioko hanburgesak eta gosariak.',
    'La mascota de ALMA, una hamburguesa, abrazando un corazón': 'ALMAren maskota, hanburgesa bat, bihotz bat besarkatzen',
    'Capítulos de la historia': 'Istorioaren kapituluak',
    'La Puerquita, doble smash con pulled pork': 'La Puerquita, smash bikoitza pulled porkarekin',
    'Tostada de salmón con aguacate': 'Izokin-txigorkia ahuakatearekin',
    'Aros de cebolla, patatas y croquetas': 'Tipula-eraztunak, patatak eta kroketak',
    'Pancakes de Ferrero': 'Ferrero pancakeak',
    'Las mejores fotos de los platos de Alma Burger: hamburguesas, picoteo, desayunos y postres.':
        'Alma Burgerren plateren argazki onenak: hanburgesak, mokadutxoak, gosariak eta postreak.',
    'La mascota de ALMA con una cámara de fotos': 'ALMAren maskota argazki-kamera batekin',
    'Hamburguesa con queso de cabra y patatas': 'Ahuntz-gaztadun hanburgesa patatekin',
    'Patatas trufadas': 'Patata trufatuak',
    'Tostada de salmón, aguacate y hummus de remolacha': 'Izokin, ahuakate eta erremolatxa-hummus txigorkia',
    'Pancakes con crema de Ferrero Rocher': 'Pancakeak Ferrero Rocher kremarekin',
    'Matcha con leche en vaso': 'Matcha esnearekin, edalontzian',
    'Huevos revueltos con tomate, tostada y hummus de remolacha': 'Arrautza nahasiak tomatearekin, txigorkiarekin eta erremolatxa-hummusarekin',
    'Vídeos de ALMA, desliza para ver más': 'ALMAren bideoak, irristatu gehiago ikusteko',
    'Vídeo desde la cocina de ALMA: una burger con queso fundido': 'ALMAren sukaldeko bideoa: gazta urtudun burger bat',
    'Desayunos con pasión: tostada de salmón, pancakes y matcha': 'Gosariak grinaz: izokin-txigorkia, pancakeak eta matcha',
    'Chocolate caliente servido en una taza de ALMA': 'Txokolate beroa ALMAren katilu batean',
    'Croquetas caseras de ALMA, recién abiertas': 'ALMAren etxeko kroketak, ireki berriak',
    'Halloween en ALMA: calabazas, arañas y máscaras': 'Halloween ALMAn: kalabazak, armiarmak eta maskarak',
    'Algo muy oscuro: la burger negra de Halloween': 'Zerbait oso iluna: Halloweeneko burger beltza',
    'Hamburguesas y desayunos en Ordizia. No es solo comida. Es ALMA: smash burgers, tostadas, pancakes, matcha, cafés especiales y postres.':
        'Hanburgesak eta gosariak Ordizian. Ez da janaria bakarrik. ALMA da: smash burgerrak, txigorkiak, pancakeak, matcha, kafe bereziak eta postreak.',
    'Alma Burger. Logo de ALMA Burger & Breakfast. Una hamburguesa con gafas asoma por detrás del nombre y saluda':
        'Alma Burger. ALMA Burger & Breakfast-en logoa. Betaurrekodun hanburgesa bat izenaren atzetik agertu eta agurtzen du',
    'Elegir la entrada de la mascota': 'Aukeratu maskotaren sarrera',
    'La Reinita, la burger del mes: smash con panceta y topping de reina pepiada': 'La Reinita, hilabeteko burgerra: smash hirugiharrarekin eta reina pepiada toppingarekin',
    'La Reinita, smash con panceta y topping de reina pepiada': 'La Reinita, smash hirugiharrarekin eta reina pepiada toppingarekin',
    'Kale Nagusia 42, Ordizia. Horario, mapa y contacto.': 'Kale Nagusia 42, Ordizia. Ordutegia, mapa eta harremana.',
    'Un perrito caliente abriendo una puerta y saludando': 'Hot dog bat atea ireki eta agurtzen',
    'Mapa de Alma Burger en Ordizia': 'Alma Burgerren mapa, Ordizian',
}
# prefijos de atributos con una parte variable
ATTR_PREFIX = {'Ver en Instagram: ': 'Ikusi Instagramen: ', 'Sticker de la mascota: ': 'Maskotaren stickerra: '}

# trozos que no son un texto completo entre etiquetas
RAW = [
    (' · Demo de diseño web</p>', ' · Web-diseinuaren demoa</p>'),
    ('> Alma Burger · Consulta nuestra carta de alérgenos al personal</p>', '> Alma Burger · Eskatu langileei alergenoen karta</p>'),
    ('>¿Quieres trabajar con nosotros? Escríbenos por <a ', '>Gurekin lan egin nahi duzu? Idatzi iezaguzu <a '),
    ('>WhatsApp</a> o pásate por el local.</p>', '>WhatsAppez</a> edo pasa zaitez lokaletik.</p>'),
    ('>¿No sabes qué pedir? <', '>Ez dakizu zer eskatu? <'),
    ('>Horario <small id="todayLabel"', '>Ordutegia <small id="todayLabel"'),
    ('>HAMBURGUESAS · DESAYUNOS · ALMA · <', '>HANBURGESAK · GOSARIAK · ALMA · <'),
    ('>ALMA · TODO LO QUE SOMOS · EN CADA BOCADO · <', '>ALMA · GAREN GUZTIA · AHOKADA BAKOITZEAN · <'),
    ('>Pulsa <b>+</b> en cualquier plato de la carta.<', '>Sakatu <b>+</b> kartako edozein plateretan.<'),
    ('>Pedidos por WhatsApp para recoger o a domicilio.<', '>WhatsApp bidezko eskaerak, jasotzeko edo etxera.<'),
]

# ---------------------------------------------------------------- frases de app.js
JS = dict(DAYS)
JS.update({k: v for k, v in TXT.items() if '<' not in k})
JS.update({
    # carta
    'Hamburguesas': 'Hanburgesak', 'Para compartir': 'Partekatzeko', 'Bocadillos': 'Ogitartekoak', 'Hot dogs': 'Hot dogak',
    'Postres': 'Postreak', 'Menú infantil': 'Haurrentzako menua', 'Desayunos': 'Gosariak',
    'Tortillas rellenas a elegir: chistorra y queso · panceta y queso · txaka · alioli con jamón · salsa cheddar y panceta.':
        'Tortilla beteak, aukeran: txistorra eta gazta · hirugiharra eta gazta · txaka · aliolia urdaiazpikoarekin · cheddar saltsa eta hirugiharra.',
    'Desayunos hasta las 12:00 (sábado y domingo desde las 9:00).': 'Gosariak 12:00ak arte (larunbat eta igandeetan 9:00etatik).',
    'Cafés y bebidas especiales': 'Kafeak eta edari bereziak', 'Bollería': 'Gozogintza', 'Tostadas': 'Txigorkiak',
    'Pancakes': 'Pancakeak', 'Bowls': 'Bowlak', 'Zumos y smoothies': 'Zukuak eta smoothieak',
    'Suplementos: huevo 1,70€ · jamón 2,30€ · aguacate 2,00€ · salmón 2,10€ · burrata 3,50€.':
        'Gehigarriak: arrautza 1,70€ · urdaiazpikoa 2,30€ · ahuakatea 2,00€ · izokina 2,10€ · burrata 3,50€.',
    # hamburguesas
    'Carne smash jugosa, cheddar bien fundido, panceta crujiente, nuestra salsa ajonesa y topping de reina pepiada: pollo deshilachado, aguacate, cebolla morada, cilantro y una mezcla cremosa. Sabor venezolano.':
        'Haragi smash mamitsua, ondo urtutako cheddarra, hirugiharra kurruskaria, gure ajonesa saltsa eta reina pepiada toppinga: oilasko xehatua, ahuakatea, tipula gorria, koriandroa eta nahasketa krematsua. Venezuelako zaporea.',
    'Doble carne smash con queso cheddar, jugoso pulled pork en su salsa, salsa Emmy en ambas tapas y ensalada de cebolla encurtida. Todo en pan brioche.':
        'Haragi smash bikoitza cheddar gaztarekin, pulled pork mamitsua bere saltsan, Emmy saltsa bi ogi-erdietan eta tipula ozpinetako entsalada. Dena brioche ogian.',
    'Carne smash con queso cheddar y cebolla caramelizada': 'Haragi smash cheddar gaztarekin eta tipula karamelizatuarekin',
    'Doble carne smash, cheddar, panceta, cebolla caramelizada y salsa BBQ': 'Haragi smash bikoitza, cheddarra, hirugiharra, tipula karamelizatua eta BBQ saltsa',
    'Smash burger con panceta crujiente, cheddar fundido, cebolla caramelizada y un toque de crema de Lotus':
        'Smash burgerra hirugiharra kurruskariarekin, cheddar urtuarekin, tipula karamelizatuarekin eta Lotus krema ukitu batekin',
    'Smash burger con queso edam, cebolla caramelizada, panceta crujiente y crema de pistacho':
        'Smash burgerra edam gaztarekin, tipula karamelizatuarekin, hirugiharra kurruskariarekin eta pistatxo-kremarekin',
    'Smash burger con lechuga, tomate, panceta, huevo frito y nuestra salsa de pepinillos (opción vegetariana)':
        'Smash burgerra letxugarekin, tomatearekin, hirugiharrarekin, arrautza frijituarekin eta gure pepinilo-saltsarekin (aukera begetarianoa)',
    'Smash burger con queso, panceta, salsa mayonesa, chispas de bacon y MUUUUCHA salsa cheddar':
        'Smash burgerra gaztarekin, hirugiharrarekin, maionesa-saltsarekin, bacon-txinpartekin eta cheddar saltsa ASKOOOOREKIN',
    'Smash burger con queso, panceta crujiente, mayonesa de trufa y patatas paja':
        'Smash burgerra gaztarekin, hirugiharra kurruskariarekin, trufa-maionesarekin eta lasto-patatekin',
    'Doble carne smash, queso de cabra, mermelada de bacon, cebolla caramelizada, mayonesa japonesa y salsa BBQ al whisky':
        'Haragi smash bikoitza, ahuntz-gazta, bacon-marmelada, tipula karamelizatua, maionesa japoniarra eta whiskydun BBQ saltsa',
    'Doble carne smash, queso cheddar, salsa de Doritos, mermelada de bacon, Doritos crocantes y salsa de queso cheddar':
        'Haragi smash bikoitza, cheddar gazta, Doritos saltsa, bacon-marmelada, Doritos kurruskariak eta cheddar gazta-saltsa',
    'Triple carne smash, queso cheddar, panceta, salsa cheddar, mermelada de bacon y mayonesa de bacon':
        'Haragi smash hirukoitza, cheddar gazta, hirugiharra, cheddar saltsa, bacon-marmelada eta bacon-maionesa',
    'Smash burger con queso cheddar, cebolla caramelizada, pepinillo, thai chilli y salsa chipotle extra picante':
        'Smash burgerra cheddar gaztarekin, tipula karamelizatuarekin, pepinilloarekin, thai chilliarekin eta chipotle saltsa oso pikantearekin',
    'Pechuga de pollo, lechuga, cebolla morada y nuestra salsa ajonesa': 'Oilasko-bularra, letxuga, tipula gorria eta gure ajonesa saltsa',
    'Pechuga de pollo con miel y mostaza, cebolla caramelizada, bits picantes y nuestra salsa secreta picante':
        'Oilasko-bularra eztiarekin eta ziapearekin, tipula karamelizatua, bit pikanteak eta gure saltsa pikante sekretua',
    'Doble pechuga de pollo con lechuga iceberg, mayonesa, mermelada de bacon, aros de cebolla y salsa BBQ a la miel':
        'Oilasko-bular bikoitza iceberg letxugarekin, maionesarekin, bacon-marmeladarekin, tipula-eraztunekin eta eztidun BBQ saltsarekin',
    'Pollo crispy bañado en miel con un toque picante, acompañado de una ensalada coleslaw y pepinillo':
        'Oilasko crispya eztiz bainatua, ukitu pikante batekin, coleslaw entsaladarekin eta pepinilloarekin',
    # para compartir
    'Con guacamole o salsa cheddar, panceta y carne picada': 'Guakamolearekin edo cheddar saltsarekin, hirugiharrarekin eta haragi xehatuarekin',
    'Patatas': 'Patatak', 'Con queso cheddar y panceta': 'Cheddar gaztarekin eta hirugiharrarekin',
    'Con mayonesa de trufa y parmesano': 'Trufa-maionesarekin eta parmesanoarekin',
    'Patatas bravas': 'Patata brabak', 'A elegir alioli o brava': 'Aliolia edo brava saltsa, aukeran',
    'Con guasacaca': 'Guasacacarekin', 'Aros de cebolla': 'Tipula-eraztunak', 'Con salsa ajonesa': 'Ajonesa saltsarekin',
    'Croquetas': 'Kroketak', 'Chipirones (4 uds.) o de queso azul con cebolla caramelizada (6 uds.)': 'Txipiroiak (4 ale) edo gazta urdina tipula karamelizatuarekin (6 ale)',
    'Alitas picantes': 'Hegaltxo pikanteak', 'Crujientes rebozadas con salsa Buffalo': 'Kurruskariak, arraultzaztatuak, Buffalo saltsarekin',
    'Fingers de pollo': 'Oilasko-fingerrak', 'Picantes con salsa de miel y mostaza': 'Pikanteak, ezti eta ziape saltsarekin',
    'Ensalada': 'Entsalada', 'De tomate, rúcula, burrata, pesto y mermelada de tomate': 'Tomatea, errukula, burrata, pestoa eta tomate-marmelada',
    'Chopitos': 'Txopitoak', 'Acompañado de alioli y limón': 'Alioliarekin eta limoiarekin',
    # bocadillos
    'De patata o rellena': 'Patatazkoa edo betea', 'Pechuga': 'Oilasko-bularra',
    'Empanada con queso, panceta y pimiento rojo': 'Ogiztatua, gaztarekin, hirugiharrarekin eta piper gorriarekin',
    'Lomo': 'Solomoa', 'Con queso, panceta y pimiento rojo': 'Gaztarekin, hirugiharrarekin eta piper gorriarekin',
    'Panceta': 'Hirugiharra', 'Con queso y pimiento rojo': 'Gaztarekin eta piper gorriarekin',
    'Vegetal de atún': 'Atun-begetala', 'Lechuga, tomate, cebolla, huevo duro, atún y mahonesa': 'Letxuga, tomatea, tipula, arrautza egosia, atuna eta maionesa',
    'Vegetal con pechuga': 'Begetala oilasko-bularrarekin',
    'Lechuga, tomate, cebolla caramelizada, huevo duro, pechuga empanada y mahonesa': 'Letxuga, tomatea, tipula karamelizatua, arrautza egosia, oilasko-bular ogiztatua eta maionesa',
    'Carne smash con queso cheddar, panceta y salsa guasacaca': 'Haragi smash cheddar gaztarekin, hirugiharrarekin eta guasacaca saltsarekin',
    # hot dogs
    'Con ketchup, mayonesa y mostaza': 'Ketchuparekin, maionesarekin eta ziapearekin',
    'Patatas paja, cebolla crunchy, parmesano y mayonesa de trufa': 'Lasto-patatak, tipula crunchya, parmesanoa eta trufa-maionesa',
    'Con salsa cheddar, repollo, cebolla morada y panceta': 'Cheddar saltsarekin, azarekin, tipula gorriarekin eta hirugiharrarekin',
    'Panceta, chimichurri, repollo, cebolla morada, guasacaca, cebolla crunchy, queso parmesano y salsa picante de jalapeño':
        'Hirugiharra, chimichurria, aza, tipula gorria, guasacaca, tipula crunchya, parmesano gazta eta jalapeño saltsa pikantea',
    # postres
    'La de toda la vida': 'Betikoa', 'Tarta de queso clásica': 'Gazta-tarta klasikoa',
    'Tarta de queso con crema de Lotus y galleta': 'Gazta-tarta Lotus kremarekin eta gailetarekin',
    'Tarta de queso con crema de pistacho': 'Gazta-tarta pistatxo-kremarekin',
    'Tarta de queso con crema de Ferrero Rocher': 'Gazta-tarta Ferrero Rocher kremarekin',
    'Tarta de queso con crema de Kinder Bueno blanco': 'Gazta-tarta Kinder Bueno zuriaren kremarekin',
    'Coulant de chocolate': 'Txokolatezko coulanta', 'Volcán de chocolate': 'Txokolate-sumendia',
    'Helado': 'Izozkia', 'De turrón o caramelo': 'Turroizkoa edo karamelozkoa', 'Crepe': 'Krepea', 'De nutella': 'Nutellazkoa',
    # menú infantil
    'Empanada, con patatas y croquetas': 'Ogiztatua, patatekin eta kroketekin', 'Con patatas y croquetas': 'Patatekin eta kroketekin',
    'Hamburguesa': 'Hanburgesa', 'Con queso, patatas y croquetas': 'Gaztarekin, patatekin eta kroketekin',
    # desayunos
    'Cortado': 'Ebakia', 'Con leche': 'Kafesnea', 'Infusiones': 'Infusioak', 'Matcha de Mango': 'Mango matcha', 'Matcha goloso': 'Matcha goxoa',
    'Croissant': 'Croissanta', 'Croissant relleno de pistacho': 'Pistatxoz betetako croissanta', 'Croissant relleno de nutella': 'Nutellaz betetako croissanta',
    'Croissant a la plancha': 'Plantxako croissanta', 'Con mantequilla y mermelada': 'Gurinarekin eta marmeladarekin',
    'Croissant con jamón York y queso': 'Croissanta York urdaiazpikoarekin eta gaztarekin', 'Napolitana de chocolate': 'Txokolatezko napolitana',
    'Tomate y AOVE': 'Tomatea eta oliba-olioa', 'Acompañado de rúcula, germinados y sésamo': 'Errukularekin, kimuekin eta sesamoarekin',
    'Mantequilla y mermelada': 'Gurina eta marmelada', 'Arándanos, frambuesa y melocotón': 'Ahabiak, mugurdia eta mertxika',
    'Tomate, jamón ibérico y AOVE': 'Tomatea, urdaiazpiko iberikoa eta oliba-olioa', 'Burrata, pesto y tomate cherry': 'Burrata, pestoa eta cherry tomatea',
    'Queso mascarpone, nueces y miel': 'Mascarpone gazta, intxaurrak eta eztia', 'Jamón ibérico, aguacate y tomate': 'Urdaiazpiko iberikoa, ahuakatea eta tomatea',
    'Crema de cacahuete y plátano': 'Kakahuete-krema eta platanoa', 'Acompañado de pepitas y sirope de chocolate': 'Haziekin eta txokolate-siroparekin',
    'Hummus, aguacate y huevo a baja temperatura': 'Hummusa, ahuakatea eta tenperatura baxuko arrautza', 'Hummus de remolacha, sésamo y cebollino': 'Erremolatxa-hummusa, sesamoa eta tipulina',
    'Burrata, jamón ibérico y tomate seco': 'Burrata, urdaiazpiko iberikoa eta tomate lehorra', 'Hongos, tomate y huevo poché': 'Onddoak, tomatea eta arrautza poché',
    'Salmón y mascarpone': 'Izokina eta mascarponea', 'Con rúcula, hummus de remolacha, germinados y sésamo': 'Errukularekin, erremolatxa-hummusarekin, kimuekin eta sesamoarekin',
    'Acompañado de plátano': 'Platanoarekin', 'Pancakes de fruta': 'Fruta-pancakeak', 'Acompañado de fruta de temporada': 'Sasoiko frutarekin',
    'Pancakes de Oreo': 'Oreo pancakeak', 'Con una cremosa crema de chocolate': 'Txokolate-krema leun batekin', 'Pancakes de Kinder': 'Kinder pancakeak',
    'Con crema de Kinder Bueno blanco': 'Kinder Bueno zuriaren kremarekin', 'Con crema de Ferrero Rocher': 'Ferrero Rocher kremarekin',
    'Pancakes salados': 'Pancake gaziak', 'Acompañado de panceta y huevo a la plancha': 'Hirugiharrarekin eta plantxako arrautzarekin',
    'Bowl de yogurt': 'Jogurt-bowla', 'Fruta de temporada, granola y miel': 'Sasoiko fruta, granola eta eztia', 'Bowl de pancake': 'Pancake-bowla',
    'Con dulce de leche y fruta de temporada': 'Esne-gozoarekin eta sasoiko frutarekin',
    'Zumo de naranja pequeño': 'Laranja-zuku txikia', 'Zumo de naranja grande': 'Laranja-zuku handia',
    'Aguacate, plátano y leche condensada': 'Ahuakatea, platanoa eta esne kondentsatua', 'Naranja, limón, jengibre, zanahoria y miel': 'Laranja, limoia, jengibrea, azenarioa eta eztia',
    'Remolacha, zanahoria y manzana': 'Erremolatxa, azenarioa eta sagarra', 'Piña y mango': 'Anana eta mangoa',
    # etiquetas y carta
    'Pollo': 'Oilaskoa', 'Picante': 'Pikantea', 'Dulce': 'Gozoa', 'Vegetariano': 'Begetarianoa', 'Trufa': 'Trufa', 'Nuevo': 'Berria',
    'Burger del mes': 'Hilabeteko burgerra', 'Clásica': 'Klasikoa', 'Consultar': 'Galdetu', 'Ver': 'Ikusi', 'Todo': 'Dena',
    'Nada por aquí con “{q}”. Prueba con otra palabra.': 'Ezer ez “{q}” bilaketarekin. Saiatu beste hitz batekin.',
    'Nada con esos filtros.': 'Ezer ez iragazki horiekin.', 'Ningún plato de esta sección cumple los filtros.': 'Atal honetako platerik ez dator bat iragazkiekin.',
    # horario
    '(solo desayunos)': '(gosariak bakarrik)', 'hoy, ': 'gaur, ',
    'Abierto ahora · hasta las {h}': 'Irekita orain · {h} arte', 'Cerrado ahora · abrimos {x}': 'Itxita orain · irekiera: {x}',
    'hoy a las {h}': 'gaur, {h}', 'mañana a las {h}': 'bihar, {h}',
    # ficha del plato
    'Imagen orientativa generada por IA': 'AAk sortutako irudi orientagarria', 'Plato anterior': 'Aurreko platera', 'Plato siguiente': 'Hurrengo platera',
    'Cerrar': 'Itxi', 'Menos': 'Gutxiago', 'Más': 'Gehiago',
    'Sin descripción. Pregúntanos en el local si tienes dudas.': 'Deskribapenik gabe. Galdetu lokalean zalantzarik baduzu.',
    'Pide online para recoger o a domicilio (reparto solo por la noche, de miércoles a domingo). De momento, el pago se hace en el local.<br>Consulta nuestra carta de alérgenos al personal. Las imágenes son orientativas.':
        'Eskatu online, jasotzeko edo etxera (banaketa gauez bakarrik, asteazkenetik igandera). Oraingoz, ordainketa lokalean egiten da.<br>Eskatu langileei alergenoen karta. Irudiak orientagarriak dira.',
    'Leer menos ↑': 'Irakurri gutxiago ↑', 'Foto ampliada': 'Argazki handitua', 'Anterior': 'Aurrekoa', 'Siguiente': 'Hurrengoa',
    # mascota del logo
    'Salto sorpresa': 'Ezusteko jauzia', 'Desde la izquierda': 'Ezkerretik', 'Giro desde la derecha': 'Biraka eskuinetik',
    'Tres rebotes': 'Hiru errebote', 'Arco y reverencia': 'Arkua eta agurra', 'Entrada {n}: {t}': '{n}. sarrera: {t}',
    # mascota que habla
    '¡La burger del mes! Viene a reinar.': 'Hilabeteko burgerra! Erreinatzera dator.',
    'Reina pepiada con sabor venezolano.': 'Reina pepiada, Venezuelako zaporearekin.',
    'Pulled pork y salsa Emmy. Potente.': 'Pulled pork eta Emmy saltsa. Indartsua.', '¡Novedad en la carta!': 'Berritasuna kartan!',
    'Tres carnes. Ven con hambre.': 'Hiru haragi. Etorri goseak.', 'Con Doritos. Sí, con Doritos.': 'Doritosekin. Bai, Doritosekin.',
    'Queso de cabra, ¿te atreves?': 'Ahuntz-gazta, ausartzen zara?', 'Mucho cheddar. MUCHO.': 'Cheddar asko. ASKO.',
    'Doble de carne, doble de todo.': 'Haragi bikoitza, dena bikoitza.', 'Burger y postre a la vez.': 'Burgerra eta postrea batera.',
    'Pistacho en una burger. Confía.': 'Pistatxoa burger batean. Fidatu.', 'Con huevo frito. Siempre gana.': 'Arrautza frijituarekin. Beti irabazten du.',
    'Patatas paja y trufa. Un vicio.': 'Lasto-patatak eta trufa. Bizio hutsa.', 'Un clásico de las mañanas.': 'Goizetako klasiko bat.',
    'Ferrero para desayunar. Sin culpa.': 'Ferreroa gosaltzeko. Errurik gabe.', 'Con fresas, que son fruta.': 'Marrubiekin, fruta direlako.',
    'Verde que te quiero verde.': 'Berdea, berde-berdea.', 'Matcha con mango. Atrévete.': 'Matcha mangoarekin. Ausartu.',
    'Para despertar.': 'Esnatzeko.', 'Huelen a trufa desde aquí.': 'Hemendik usaintzen da trufa.',
    '¡La burger del mes! Pídela antes de que se acabe.': 'Hilabeteko burgerra! Eskatu amaitu baino lehen.', '¡Novedad!': 'Berritasuna!',
    'Ojo, que pica. Ten agua cerca.': 'Kontuz, pikatzen du. Izan ura gertu.', 'Huele a trufa desde aquí.': 'Hemendik usaintzen da trufa.',
    'Para los golosos.': 'Gozozaleentzat.', 'Uy, qué dulce pinta.': 'Ui, zein itxura gozoa.',
    'Crujiente por fuera, jugoso por dentro.': 'Kanpotik kurruskaria, barrutik mamitsua.', 'Esta también es para ti.': 'Hau ere zuretzat da.',
    '¡Buena elección!': 'Aukera ona!', 'Esta tiene buena pinta.': 'Honek itxura ona du.', 'Para compartir. O no.': 'Partekatzeko. Edo ez.',
    'Clásico y siempre acierta.': 'Klasikoa, eta beti asmatzen du.', 'Un hot dog con alma.': 'Arima duen hot dog bat.',
    'Siempre hay hueco para el postre.': 'Postrearentzat beti dago tokia.', 'Para los peques.': 'Txikientzat.',
    'Buenos días con ganas.': 'Egun on, gogotsu.', 'Así sí empieza el día.': 'Horrela bai hasten dela eguna.',
    'Callar': 'Isildu', 'Callar a la mascota': 'Isilarazi maskota', 'Mascota: activar o silenciar los comentarios': 'Maskota: aktibatu edo isildu iruzkinak',
    'Mascota': 'Maskota', '¡Hola otra vez! Te voy contando.': 'Kaixo berriro! Kontatzen joango natzaizu.',
    '¡Hola! Pasa el ratón o toca un plato.': 'Kaixo! Pasa sagua edo ukitu plater bat.', 'Dime qué te apetece.': 'Esadazu zer nahi duzun.',
    '¿Desayuno o hamburguesa?': 'Gosaria ala hanburgesa?', '¡Anotado!': 'Apuntatuta!', 'Buena elección.': 'Aukera ona.',
    '¡Buenos días! ¿Te apetece un desayuno?': 'Egun on! Gosari bat nahi?', '¡Buenos días! ¿Desayuno o hamburguesa?': 'Egun on! Gosaria ala hanburgesa?',
    '¡Hola! ¿Qué te apetece comer?': 'Kaixo! Zer jan nahi duzu?', '¡Buenas noches! Hoy toca burger.': 'Gabon! Gaur burgerra tokatzen da.',
    'Toca un plato y te cuento algo.': 'Ukitu plater bat eta zerbait kontatuko dizut.',
    'Buenos días. Café, tostada… ¿qué te apetece?': 'Egun on. Kafea, txigorkia… zer nahi duzu?',
    'Los desayunos son hasta las 12:00, pero mira, mira.': 'Gosariak 12:00ak arte dira, baina begira, begira.',
    '¡Te esperamos en Kale Nagusia 42!': 'Kale Nagusia 42n zain zaitugu!',
    'Vídeo de Instagram': 'Instagrameko bideoa', 'Abrir en Instagram ↗': 'Ireki Instagramen ↗',
    # test
    '¿Cuánta hambre tienes?': 'Zenbat gose duzu?', 'Un picoteo': 'Mokadutxo bat', 'La normal': 'Normala', 'Mucha': 'Asko', '¡Bestial!': 'Izugarria!',
    '¿Qué te tira más?': 'Zerk erakartzen zaitu gehien?', 'Lo clásico': 'Klasikoak', 'Queso fundido': 'Gazta urtua', 'Dulce y salado': 'Gozoa eta gazia', 'Algo diferente': 'Zerbait desberdina',
    '¿Y el picante?': 'Eta pikantea?', 'Nada': 'Batere ez', 'Un poquito': 'Pixka bat', 'Dale fuerte': 'Gogor eman',
    '¿Carne o pollo?': 'Haragia ala oilaskoa?', 'Carne': 'Haragia', 'Me da igual': 'Berdin zait',
    '¿Cómo vienes hoy?': 'Nola zatoz gaur?', 'Tranquilo, de siempre': 'Lasai, betiko moduan', 'Con ganas de fiesta': 'Jai-gogoarekin', 'Curioso': 'Jakin-minez', 'Goloso': 'Gozozale',
    'Clásico de los de siempre. Sabes lo que te gusta.': 'Betiko klasikoa. Badakizu zer gustatzen zaizun.',
    'Quien tiene hambre no se corta. Doble de todo.': 'Gose denak ez du lotsarik. Dena bikoitza.',
    'Dulce y salado, sin remordimientos.': 'Gozoa eta gazia, kontzientzia-zamarik gabe.',
    'Curioso y con pistacho. Te gusta sorprender.': 'Jakin-minez eta pistatxoarekin. Harritzea gustatzen zaizu.',
    'Equilibrado y con huevo frito. Buen gusto.': 'Orekatua eta arrautza frijituarekin. Gustu ona.',
    'Del equipo del queso. Cuanto más, mejor.': 'Gaztaren taldekoa. Zenbat eta gehiago, hobe.',
    'Con un punto de trufa y elegancia.': 'Trufa eta dotorezia puntu batekin.',
    'Atrevido y con carácter. Aquí no se viene a hacer amigos.': 'Ausarta eta izaeraduna. Hona ez da lagunak egitera etortzen.',
    'Divertido: nada de ser aburrido. Con Doritos, claro.': 'Dibertigarria: aspergarri izatea ez doa zurekin. Doritosekin, noski.',
    'Vas a por todas. Triple y sin miedo.': 'Guztiaren bila zoaz. Hirukoitza eta beldurrik gabe.',
    'Valiente. El picante no te asusta.': 'Ausarta. Pikanteak ez zaitu beldurtzen.',
    'Fresco y crujiente. Te gusta lo ligero con sabor.': 'Freskoa eta kurruskaria. Arina eta zaporetsua gustatzen zaizu.',
    'Pícaro y con chispa. Un poco travieso.': 'Maltzurra eta txinpartaduna. Bihurri samarra.',
    'Hambre con carácter y mucho crujiente.': 'Izaeradun gosea eta kurruskari asko.',
    'Dulce y picante a la vez. No te decides y está bien.': 'Gozoa eta pikantea batera. Ez zara erabakitzen, eta ondo dago.',
    'Nueva en la carta. Potente y cremosa.': 'Berria kartan. Indartsua eta krematsua.',
    'Una reina con carácter. No vienes a participar, vienes a reinar.': 'Izaeradun erregina. Ez zatoz parte hartzera, erreinatzera zatoz.',
    'Pregunta {n} de {t}': '{n}. galdera ({t}etik)', '← Volver': '← Itzuli', 'Tu resultado': 'Zure emaitza', 'Eres <em>{x}</em>': '<em>{x}</em> zara',
    ' · con versión vegetariana': ' · bertsio begetarianoarekin', 'Ver la ficha': 'Ikusi fitxa', 'También te pegan': 'Hauek ere ondo datozkizu',
    'Compartir mi resultado': 'Partekatu nire emaitza', 'Repetir el test': 'Errepikatu testa',
    '¡Soy {x}! {l}\n¿Y tú, qué burger eres? Haz el test de Alma Burger: {u}': '{x} naiz! {l}\nEta zu, zein burger zara? Egin Alma Burgerren testa: {u}',
    # pedir online
    'Abriendo la página de pedidos…': 'Eskaera-orria irekitzen…',
    # cookies
    'Aviso de cookies': 'Cookie-oharra', 'Cookies, las justas.': 'Cookieak, behar-beharrezkoak.',
    ' No usamos cookies de publicidad ni de análisis. Solo guardamos en tu navegador lo necesario (como el color elegido). Si aceptas, también cargamos el mapa de OpenStreetMap. ':
        ' Ez dugu publizitate- edo analisi-cookierik erabiltzen. Zure nabigatzailean beharrezkoa bakarrik gordetzen dugu (adibidez, aukeratutako kolorea eta hizkuntza). Onartzen baduzu, OpenStreetMapeko mapa ere kargatuko dugu. ',
    'Más información sobre cookies': 'Cookieei buruzko informazio gehiago (gaztelaniaz)', 'Rechazar': 'Ukatu', 'Aceptar': 'Onartu',
})
