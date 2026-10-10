# Alma Burger · demo web

Propuesta de rediseño web para **Alma Burger** (Kale Nagusia 42, Ordizia). Sitio estático, sin dependencias ni paso de compilación para verlo.

## Ver la demo
- `index.html` → selector con las dos versiones
- `opcion-1-color/` → crema + negro del logo + azul de su carta + amarillo de apoyo
- `opcion-2-fiel-logo/` → solo negro y crema, fiel al logo

Cada versión tiene: Inicio · El alma · Carta · Desayunos · Galería · Visítanos (+ 404).

## Qué incluye
- Mascota animada con 5 entradas por detrás del logo (rotan solas; los puntos permiten elegir)
- Carta interactiva (≈90 platos) con ficha de cada plato, foto completa y opciones
- Pedido **para recoger por WhatsApp** (carrito con notas, hora y alergias) y **Just Eat** destacado para pedidos a domicilio
- Menú sorpresa, reserva de mesa por WhatsApp, galería con visor, responsive y accesible

## Regenerar
El código fuente está en `_src/`. Las dos versiones se generan con:

```
python _src/build.py
```

> Demo de diseño. Las fotos y textos pertenecen a Alma Burger (web, Instagram y Just Eat). Algunas imágenes de Just Eat están marcadas por la plataforma como generadas por IA y son orientativas.
