# Alma Burger · estado del proyecto

> Documento de traspaso: cómo está la web **a 20 de noviembre de 2026** y por dónde seguir.
> Si eres una IA (u otra persona) que retoma el proyecto, léelo entero antes de tocar nada.

## 1. Qué es

Web estática de **ALMA Burger & Breakfast**, hamburguesería y desayunos en Kale Nagusia 42, Ordizia (Gipuzkoa).
El usuario hace de intermediario con la clienta (la dueña del local): le enseña capturas, recoge sus cambios y los trae.

- Repositorio: `https://github.com/sefiro888/almaburger` (rama `main`).
- Publicada con GitHub Pages en `https://sefiro888.github.io/almaburger/`. El dominio previsto es `almaburgers.com` (aún no activo).
- Dos versiones de color, mismo contenido: **negro** (negro y crema del logo) y **azul** (azul marino y crema).
- Dos idiomas: castellano y **euskera** (`*.eu.html`); las páginas legales solo en castellano.
- Páginas: Inicio · El alma · Hamburguesas (carta) · Desayunos · Galería · Visítanos · 404 · Aviso legal · Privacidad · Cookies.
- La raíz (`index.html`) es una intro que deja elegir color e idioma; el resto de HTML de la raíz son redirecciones.

## 2. Regla de oro: se edita `_src/`, nunca lo generado

Todo lo que hay en `negro/`, `azul/`, `opcion-1-color/`, `opcion-2-fiel-logo/` y los `.html` de la raíz **lo genera el build** y se borra y se rehace cada vez.

```
python _src/build.py
```

Imprime `ok` al terminar. Después hay que commitear tanto `_src/` como las carpetas generadas (GitHub Pages sirve lo generado).

### Qué hay en `_src/`

| Fichero | Para qué |
|---|---|
| `build.py` | Genera todas las páginas. Cada página es una función (`home()`, `alma()`, `carta()`, `desayunos()`, `galeria()`, `visitanos()`, `nf()`, `lpage()`). Menú superior en `nav()` y `NAV_DOODLES`. |
| `app.js` | Todo el JavaScript: la carta (`const MENU`, al principio), filtros, destacados, horario y cartel abierto/cerrado («Horario del local»), pedido, test «¿Qué burger eres?», comentarios de la mascota, Instagram… |
| `base.css` | Estilos base. |
| `pedido-v2.css` | Estilos añadidos después; lo más reciente está al **final** del fichero. |
| `theme-fiel.css` / `theme-navy.css` | Colores del tema negro / azul. |
| `i18n_eu.py` | Traducciones al euskera (`TXT`, `ATTR`, `RAW`, `JS`). **Todo texto nuevo en castellano necesita su traducción aquí**, o saldrá en castellano en la versión `.eu`. |
| `config.json` | Enlace de pedidos de Ágora (`agora_url`), URL pública (`site_url`) y datos legales del titular. |
| `intro.html` | La intro de la raíz (elegir color e idioma). |
| `img/` | Imágenes comunes. `themes/azul/img/` sobrescribe las que cambian de color en la versión azul (mascota, logos…). |
| `imgopt.py` | Lo llama el build: genera los WebP y pone ancho y alto en los `<img>`. Usa `_cache/`. |
| `make_share.py`, `make_theme_assets.py`, `legal.py`, `update_instagram.py` | Utilidades: imagen para compartir, recolorear para el tema azul, textos legales, actualizar `data/instagram.json`. |

El CSS final de cada tema es `fonts.css + base.css + pedido-v2.css + tema`, en ese orden.

### Colores

Usar siempre las variables, nunca colores fijos: `--ink` (tinta: negro o azul marino), `--cream`, `--card` (crema claro de tarjetas), `--accent` / `--accent-fg`. Así todo funciona solo en los dos temas.
Las únicas excepciones aceptadas son el verde `#2fd16b` y el coral `#ff8f7a` del puntito del cartel abierto/cerrado.

## 3. Cómo verlo en local

Desde la raíz del proyecto:

```
python -m http.server 5180
```

y abrir `http://localhost:5180/negro/index.html` (o `/azul/…`, o `/negro/index.eu.html`).
El puerto 5173 lo suele tener ocupado otra sesión; por eso se usa el 5180. Los efectos del menú solo se ven en pantallas de más de 980 px de ancho.

## 4. Estilo y personalidad

- Estética de pegatina: bordes de tinta gruesos, sombras duras desplazadas, ligeras rotaciones, tipografía Big Shoulders Display en mayúsculas.
- **La mascota**: una hamburguesa con gafas de sol redondas, brazos y piernas de goma, guantes blancos y zapatillas, en estilo de dibujo animado de los años 30 («rubber hose»), solo trazo de tinta y relleno crema. Archivos: `mascot.png`, `mascot-body/legL/legR.png` (versión animada que anda), `mascot-sleep.png` (dormida, abrazada a una almohada), `stickers/`, `ill/` (ilustraciones de cabecera de cada página).
- Cuando hace falta una imagen nueva, se le da al usuario un **prompt en inglés** para que la genere él con su herramienta, pidiéndole que adjunte `negro/img/mascot.png` como referencia. Luego se limpia el fondo y se recolorea a los dos temas con Python y Pillow (ver el último apartado del historial).

## 5. Últimos cambios (los más recientes primero)

| Commit | Cambio |
|---|---|
| `c7f9410` | Respuestas de la clienta: Alitas teriyaki 14,00 €, Ensalada de salmón y aguacate 14,50 €, y un segundo matcha de mango, **Matcha de Mango con crema** a 6,00 € (se lleva la foto); el normal sigue a 5,20 €. |
| `dbe7b7a` | Equipo: las fotos de Jesús y Jefferson estaban cambiadas. Jesús (Plancha, Doble Dosis) es el de la foto en la plancha y Jefferson (Jefe de cocina, Hot Gordita) el que corta cebolla. Ojo: los nombres de esas fotos en `material-nuevo/` estaban al revés. |
| `a6fc685` | Ficha de un producto **sin foto**: tarjeta crema con puntitos, la mascota entera dando saltitos, el nombre en pegatina y «Foto en camino». Antes salía la mascota desmontada sobre rayas grises. |
| `8fe93e1` | **Material nuevo de la clienta (20/11)**: La Matru 15,50 €, La Reinita 18,00 €; precios nuevos de tostadas (6, 7, 9 y 11) y matchas; bebidas nuevas con ube y matcha azul; sección **Fuera de carta** con tres minibrioches (15,50 €); Alitas teriyaki y Ensalada de salmón y aguacate (sin precio todavía); fotos reales de muchos platos y bebidas; **equipo real** en El alma (Abrahan, Lidia, Maddi, Jefferson y Jesús, con su plato favorito); galería ampliada. En desayunos, dentro de cada grupo salen primero los platos con foto. |
| `d55f797` | **Menú superior con más gracia**: subrayado de rotulador que se dibuja al pasar el ratón, inclinación tipo pegatina, la página actual rodeada con un círculo a boli, y un **mini-dibujo por sección** que asoma por encima al pasar el ratón (corazón en El alma, burger en Hamburguesas, taza con humo en Desayunos, cámara con flash en Galería, pin que bota en Visítanos). SVG en `build.py` (`NAV_DOODLES`), CSS al final de `pedido-v2.css`. Ocultos en el menú del móvil. |
| `8a0f5cd` | Mascota dormida (`mascot-sleep.png`) para el cartel de cerrado. Generada con IA por el usuario, limpiada y recoloreada para cada tema. |
| `303bd21` | **Cartel abierto/cerrado** rediseñado: píldora crema con borde de tinta (antes era toda verde y chillona); solo el puntito es verde (abierto) o coral (cerrado); la mascota asoma por la derecha saludando, y dormida con «z z z» cuando está cerrado. |
| `d1264f2` | Abierto/cerrado calculado según el horario del local (hora de Madrid); la cocina tiene su horario aparte. |
| `4bf3818` | Web en euskera. |
| `29f6393` | Cambios de la reunión con la clienta del 6/11: fuera Just Eat, horarios de cocina por tramos y de reparto, La Reinita burger del mes, La Puerquita como novedad, La Matru a 14,50 €, opción vegetariana, pago en el local, tarjetas ALMA con el color de la web. |

Historial completo con `git log --oneline`.

## 6. Pendiente (por dónde seguir)

1. **Publicar**: todo lo de la tabla anterior está publicado (último envío el 20/11/2026, con el material nuevo). Para publicar cambios nuevos: `git push`, solo cuando el usuario lo diga; GitHub Pages tarda uno o dos minutos en actualizarse. Para ver qué falta por subir: `git status -sb`.
2. **Preguntas para Alma Burger**: ver el apartado 8. Cuando llegue cada respuesta, aplicarla y tacharla de la lista.
3. **Probar en un navegador ancho los mini-dibujos del menú** al pasar el ratón: los dibujos se han comprobado, pero el efecto completo a ancho de escritorio no se vio en la vista previa. Mirar que no tapen texto ni choquen con el borde superior.
4. Abrahan y Lidia siguen con ilustración en El equipo porque no hay foto suya. Ice Ube Latte, Blue Matcha Latte y Blue Paradise no tienen foto (ninguna bebida trae descripción en la carta de la clienta). Del **Blue Paradise** el usuario tiene foto: falta que la deje en `material-nuevo/`.
5. La elección de matcha verde o azul se ha puesto en Ube Matcha Latte, Matcha de Mango, Matcha Berry y Matcha goloso.
6. **Euskera**: la traducción la hizo una IA; falta que la revise alguien nativo.
7. **Dominio**: cuando `almaburgers.com` esté activo, cambiar `site_url` en `config.json` y volver a generar (lo usan las vistas previas al compartir).
8. Ideas comentadas y **no hechas** para el menú: letras que botan al pasar el ratón; la mascota paseando por el menú hasta la página actual; en el menú del móvil, que los enlaces entren escalonados con un botecito.
9. Si a la clienta no le convence la mascota dormida (la cara es algo más redonda que la original), regenerarla con un modelo de **edición** de imagen a partir de `mascot.png` («ciérrale los ojos y ponle una almohada sin cambiar nada más»).

## 7. Forma de trabajar con el usuario

- Habla en **castellano** y conviene responderle en castellano, con frases claras y sin jerga.
- Suele pedir **capturas** para enseñárselas a la clienta: hacerlas con buena resolución, sin el aviso de cookies delante, y mostrando el estado concreto (por ejemplo, simular «cerrado» desde la consola del navegador si el local está abierto).
- Cuando dice «en local» o «enséñame cómo quedaría», se monta y se enseña **sin commitear**; se commitea cuando da el visto bueno.
- Commits en castellano, que describan el cambio como lo vería la clienta. No hacer `git push` sin que lo pida.
- Si trae varios cambios de una reunión y dice que irá añadiendo más, se apuntan y se aplican todos juntos en un solo commit cuando lo pida.

## 8. Preguntas para Alma Burger

Lista de dudas que el usuario tiene que preguntar a la dueña. Entre paréntesis, cómo está la web mientras tanto.

Ya resuelto (20/11): el **horario** (local abierto todo el día, cocina por tramos); las **alitas teriyaki** (14,00 €, son otro tipo de alitas y conviven con las picantes); el precio de la **ensalada de salmón** (14,50 €); y el **matcha de mango**, que son dos: el normal a 5,20 € y el «con crema» a 6,00 € (la foto es la del de crema).

1. **Ensalada de salmón y aguacate**: ¿qué lleva exactamente? (En la web: «Rúcula, salmón, aguacate, tomate cherry, cebolla morada y nueces», sacado de la foto.)
2. **Datos legales** para el Aviso legal y la Privacidad: titular, NIF, email y datos del registro. (En la web: marcados en amarillo como pendientes.)
