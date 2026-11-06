(() => {
'use strict';

/* ---------- Datos (carta oficial de almaburgers.com + fotos de Just Eat / Instagram) ---------- */
const P = (n, d, p, t = [], i = '') => ({ n, d, p, t, i });
const MENU = {
  hamburguesas: { label: 'Hamburguesas', items: [
    P('La Puerquita', 'Doble carne smash con queso cheddar, jugoso pulled pork en su salsa, salsa Emmy en ambas tapas y ensalada de cebolla encurtida. Todo en pan brioche.', 18.5, ['mes'], 'la-puerquita'),
    P('La Básica', 'Carne smash con queso cheddar y cebolla caramelizada', 10, ['clásica'], 'la-basica'),
    P('Doble Dosis', 'Doble carne smash, cheddar, panceta, cebolla caramelizada y salsa BBQ', 15.5, [], 'doble-dosis'),
    P('La Golosa', 'Smash burger con panceta crujiente, cheddar fundido, cebolla caramelizada y un toque de crema de Lotus', 17.5, ['dulce'], 'la-golosa'),
    P('Dulce y Verde', 'Smash burger con queso edam, cebolla caramelizada, panceta crujiente y crema de pistacho', 17.5, ['dulce'], 'dulce-y-verde'),
    P('Gordi Deluxe', 'Smash burger con lechuga, tomate, panceta, huevo frito y nuestra salsa de pepinillos (opción vegetariana)', 14.5, ['veg'], 'gordi-deluxe'),
    P('Me Derrito', 'Smash burger con queso, panceta, salsa mayonesa, chispas de bacon y MUUUUCHA salsa cheddar', 15.5, [], 'me-derrito'),
    P('La Matru', 'Smash burger con queso, panceta crujiente, mayonesa de trufa y patatas paja', 14, ['trufa'], 'la-matru'),
    P('La Cabrona', 'Doble carne smash, queso de cabra, mermelada de bacon, cebolla caramelizada, mayonesa japonesa y salsa BBQ al whisky', 16.5, [], 'la-cabrona'),
    P('La Dori', 'Doble carne smash, queso cheddar, salsa de Doritos, mermelada de bacon, Doritos crocantes y salsa de queso cheddar', 17.5, [], 'la-dori'),
    P('La Triplona', 'Triple carne smash, queso cheddar, panceta, salsa cheddar, mermelada de bacon y mayonesa de bacon', 19.5, [], 'la-triplona'),
    P('Picantona', 'Smash burger con queso cheddar, cebolla caramelizada, pepinillo, thai chilli y salsa chipotle extra picante', 16, ['picante'], 'picantona'),
    P('Chickenesa', 'Pechuga de pollo, lechuga, cebolla morada y nuestra salsa ajonesa', 15.5, ['pollo'], 'chickenesa'),
    P('La Diabla', 'Pechuga de pollo con miel y mostaza, cebolla caramelizada, bits picantes y nuestra salsa secreta picante', 16.5, ['pollo', 'picante'], 'la-diabla'),
    P('Furia de Pollo', 'Doble pechuga de pollo con lechuga iceberg, mayonesa, mermelada de bacon, aros de cebolla y salsa BBQ a la miel', 17, ['pollo'], 'furia-de-pollo'),
    P('La Picosita', 'Pollo crispy bañado en miel con un toque picante, acompañado de una ensalada coleslaw y pepinillo', 17, ['pollo', 'picante', 'nuevo'])
  ]},
  compartir: { label: 'Para compartir', items: [
    P('Totopos', 'Con guacamole o salsa cheddar, panceta y carne picada', 13.8),
    P('Patatas', 'Con queso cheddar y panceta', 8.8, [], 'patatas'),
    P('Patatas trufadas', 'Con mayonesa de trufa y parmesano', 9.5, ['trufa'], 'patatas-trufadas'),
    P('Patatas bravas', 'A elegir alioli o brava', 8.5, [], 'patatas-bravas'),
    P('Tequeños', 'Con guasacaca', 9.5, [], 'tequenos'),
    P('Aros de cebolla', 'Con salsa ajonesa', 5.5, [], 'aros'),
    P('Croquetas', 'Chipirones (4 uds.) o de queso azul con cebolla caramelizada (6 uds.)', 6, [], 'croquetas'),
    P('Alitas picantes', 'Crujientes rebozadas con salsa Buffalo', 12, ['picante', 'pollo'], 'alitas'),
    P('Fingers de pollo', 'Picantes con salsa de miel y mostaza', 9.5, ['pollo', 'picante'], 'fingers'),
    P('Ensalada', 'De tomate, rúcula, burrata, pesto y mermelada de tomate', 13.5, ['veg'], 'ensalada'),
    P('Chopitos', 'Acompañado de alioli y limón', 9.5)
  ]},
  bocadillos: { label: 'Bocadillos', note: 'Tortillas rellenas a elegir: chistorra y queso · panceta y queso · txaka · alioli con jamón · salsa cheddar y panceta.', items: [
    P('Tortilla', 'De patata o rellena', 8.7, ['veg'], 'tortilla'),
    P('Pechuga', 'Empanada con queso, panceta y pimiento rojo', 9.7, ['pollo'], 'pechuga'),
    P('Lomo', 'Con queso, panceta y pimiento rojo', 7.7, [], 'lomo'),
    P('Panceta', 'Con queso y pimiento rojo', 7.4, [], 'panceta'),
    P('Vegetal de atún', 'Lechuga, tomate, cebolla, huevo duro, atún y mahonesa', 8, [], 'vegetal-atun'),
    P('Vegetal con pechuga', 'Lechuga, tomate, cebolla caramelizada, huevo duro, pechuga empanada y mahonesa', 9.8, ['pollo'], 'vegetal-pechuga'),
    P('Alma Burger', 'Carne smash con queso cheddar, panceta y salsa guasacaca', 8.5)
  ]},
  hotdogs: { label: 'Hot dogs', items: [
    P('Hot Clásica', 'Con ketchup, mayonesa y mostaza', 7, [], 'hot-clasica'),
    P('Hot Gordita', 'Patatas paja, cebolla crunchy, parmesano y mayonesa de trufa', 10.5, ['trufa'], 'hot-gordita'),
    P('Hot Quesuda', 'Con salsa cheddar, repollo, cebolla morada y panceta', 10.5, [], 'hot-quesuda'),
    P('Hot Picantona', 'Panceta, chimichurri, repollo, cebolla morada, guasacaca, cebolla crunchy, queso parmesano y salsa picante de jalapeño', 10.5, ['picante'], 'hot-picantona')
  ]},
  postres: { label: 'Postres', items: [
    P('La de toda la vida', 'Tarta de queso clásica', 7, ['dulce'], 'tarta-clasica'),
    P('La Lotus', 'Tarta de queso con crema de Lotus y galleta', 8.5, ['dulce'], 'tarta-lotus'),
    P('La Pistacha', 'Tarta de queso con crema de pistacho', 8.5, ['dulce'], 'tarta-pistacha'),
    P('La Ferrero', 'Tarta de queso con crema de Ferrero Rocher', 8.7, ['dulce'], 'tarta-ferrero'),
    P('La Kinder', 'Tarta de queso con crema de Kinder Bueno blanco', 8.5, ['dulce'], 'tarta-kinder'),
    P('Coulant de chocolate', 'Volcán de chocolate', 6.5, ['dulce'], 'coulant'),
    P('Helado', 'De turrón o caramelo', 3.5, ['dulce']),
    P('Crepe', 'De nutella', 5.5, ['dulce'], 'crepe')
  ]},
  infantil: { label: 'Menú infantil', items: [
    P('Pechuga', 'Empanada, con patatas y croquetas', 9),
    P('Lomo', 'Con patatas y croquetas', 9),
    P('Hamburguesa', 'Con queso, patatas y croquetas', 9)
  ]},
  desayunos: { label: 'Desayunos', note: 'Desayunos de 8:00 a 12:00.', groups: [
    { g: 'Cafés y bebidas especiales', items: [
      P('Espresso', '', 1.7), P('Cortado', '', 1.8), P('Con leche', '', 1.9), P('Cola Cao', '', 2.2), P('Infusiones', '', 1.9),
      P('Ice Caramel Latte', '', 3.5), P('Ice Vainilla Latte', '', 3.5),
      P('Matcha de Mango', '', 4), P('Matcha Berry', '', 4), P('Matcha goloso', '', 4, [], 'matcha-2')
    ]},
    { g: 'Bollería', items: [
      P('Croissant', '', 3), P('Croissant relleno de pistacho', '', 3.5, ['dulce']), P('Croissant relleno de nutella', '', 3.5, ['dulce']),
      P('Croissant a la plancha', 'Con mantequilla y mermelada', 4), P('Croissant con jamón York y queso', '', 4.4), P('Napolitana de chocolate', '', 3, ['dulce'])
    ]},
    { g: 'Tostadas', items: [
      P('Tomate y AOVE', 'Acompañado de rúcula, germinados y sésamo', 3, ['veg']),
      P('Mantequilla y mermelada', 'Arándanos, frambuesa y melocotón', 3.4, ['veg']),
      P('Tomate, jamón ibérico y AOVE', '', 4.3),
      P('Burrata, pesto y tomate cherry', 'Acompañado de rúcula, germinados y sésamo', 7.3, ['veg']),
      P('Queso mascarpone, nueces y miel', '', 5.3, ['veg']),
      P('Jamón ibérico, aguacate y tomate', 'Acompañado de rúcula, germinados y sésamo', 5.9),
      P('Crema de cacahuete y plátano', 'Acompañado de pepitas y sirope de chocolate', 4.5, ['dulce']),
      P('Hummus, aguacate y huevo a baja temperatura', 'Hummus de remolacha, sésamo y cebollino', 6.5),
      P('Burrata, jamón ibérico y tomate seco', 'Acompañado de rúcula, germinados y sésamo', 7.9),
      P('Hongos, tomate y huevo poché', 'Acompañado de rúcula, germinados y sésamo', 7.2),
      P('Salmón y mascarpone', 'Con rúcula, hummus de remolacha, germinados y sésamo', 7.5, [], 'tostada-salmon')
    ], note: 'Suplementos: huevo 1,70€ · jamón 2,30€ · aguacate 2,00€ · salmón 2,10€ · burrata 3,50€.' },
    { g: 'Pancakes', items: [
      P('Pancakes de Nutella', 'Acompañado de plátano', 6, ['dulce'], 'pancakes-nutella'),
      P('Pancakes de fruta', 'Acompañado de fruta de temporada', 6.2, ['dulce']),
      P('Pancakes de Oreo', 'Con una cremosa crema de chocolate', 6.5, ['dulce']),
      P('Pancakes de Kinder', 'Con crema de Kinder Bueno blanco', 6.3, ['dulce']),
      P('Pancakes de Ferrero', 'Con crema de Ferrero Rocher', 6.3, ['dulce'], 'pancakes-ferrero'),
      P('Pancakes salados', 'Acompañado de panceta y huevo a la plancha', 7)
    ]},
    { g: 'Bowls', items: [
      P('Bowl de yogurt', 'Fruta de temporada, granola y miel', 6.4),
      P('Bowl de pancake', 'Con dulce de leche y fruta de temporada', 7.5, ['dulce'])
    ]},
    { g: 'Zumos y smoothies', items: [
      P('Zumo de naranja pequeño', '', 2.85), P('Zumo de naranja grande', '', 3.85),
      P('Avocado Paradise', 'Aguacate, plátano y leche condensada', 5.4),
      P('Sun Power', 'Naranja, limón, jengibre, zanahoria y miel', 5.4),
      P('Vital Red', 'Remolacha, zanahoria y manzana', 5.5),
      P('Yellow Bliss', 'Piña y mango', 5.5)
    ]}
  ]}
};
const TAGLABEL = { pollo: 'Pollo', picante: 'Picante', dulce: 'Dulce', veg: 'Vegetariano', trufa: 'Trufa', nuevo: 'Nuevo', mes: 'Burger del mes', 'clásica': 'Clásica' };
const FILTERS = ['pollo', 'picante', 'dulce', 'veg', 'trufa'];
const RIG = '<div class="rig rig--still"><img src="img/mascot-legL.png" alt=""><img src="img/mascot-legR.png" alt=""><img src="img/mascot-body.png" alt=""></div>';

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const eur = n => n.toFixed(2).replace('.', ',') + '€';
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');

const OPTS = {
  'compartir|Totopos': ['Con guacamole', 'Con salsa cheddar'],
  'compartir|Patatas bravas': ['Con alioli', 'Con brava'],
  'compartir|Croquetas': ['Chipirones (4 uds.)', 'Queso azul y cebolla caramelizada (6 uds.)'],
  'bocadillos|Tortilla': ['De patata', 'Rellena de chistorra y queso', 'Rellena de panceta y queso', 'Rellena de txaka', 'Rellena de alioli con jamón', 'Rellena de salsa cheddar y panceta'],
  'postres|Helado': ['De turrón', 'De caramelo'],
  'hamburguesas|Gordi Deluxe': ['Normal', 'Versión vegetariana']
};
const allItems = [];
const catPhotos = {}, catCount = {};
Object.entries(MENU).forEach(([k, c]) => {
  (c.groups ? c.groups.flatMap(g => g.items) : c.items).forEach(i => { i.cat = k; i.id = k + '|' + i.n; i.o = OPTS[k + '|' + i.n] || null; allItems.push(i); catCount[k] = (catCount[k] || 0) + 1; if (i.i) catPhotos[k] = (catPhotos[k] || 0) + 1; });
});
Object.keys(catCount).forEach(k => { catPhotos[k] = (catPhotos[k] || 0) / catCount[k] >= .5; });
const byId = id => allItems.find(i => i.id === id);

function card(i, idx) {
  const flag = i.t.filter(t => ['mes', 'nuevo', 'picante', 'veg', 'trufa'].includes(t)).slice(0, 2);
  const flags = flag.length ? `<div class="flags">${flag.map(t => `<span class="flag ${t === 'mes' || t === 'nuevo' ? 'flag--hot' : ''}">${TAGLABEL[t]}</span>`).join('')}</div>` : '';
  const btn = `<button class="add" data-add="${esc(i.id)}" aria-label="Añadir ${esc(i.n)} al pedido">+<span class="add__n"></span></button>`;
  const delay = `style="animation-delay:${Math.min(idx, 10) * 35}ms"`;
  if (i.i) return `<article class="item" data-open="${esc(i.id)}" tabindex="0" aria-label="Ver ${esc(i.n)}" ${delay}>
    <div class="item__img"><img src="img/dishes/s/${i.i}.jpg" alt="${esc(i.n)}" loading="lazy" width="640" height="640">${flags}<span class="pill">${eur(i.p)}</span>${btn}</div>
    <div class="item__body"><h3>${esc(i.n)}</h3>${i.d ? `<p>${esc(i.d)}</p>` : ''}</div></article>`;
  return `<article class="item item--row" data-open="${esc(i.id)}" tabindex="0" aria-label="Ver ${esc(i.n)}" ${delay}>
    <div class="item__body"><h3>${esc(i.n)}</h3>${i.d ? `<p>${esc(i.d)}</p>` : ''}${flags}</div><span class="price">${eur(i.p)}</span>${btn}</article>`;
}

/* ---------- Carta / desayunos ---------- */
const menuEl = $('#menu');
if (menuEl) {
  const mode = menuEl.dataset.mode || 'all';
  const state = { tab: mode === 'desayunos' ? 'todo' : 'hamburguesas', filters: new Set(), q: '' };
  const tabsEl = $('#tabs'), chipsEl = $('#chips'), qEl = $('#q');
  const groups = MENU.desayunos.groups;
  const pool = mode === 'desayunos' ? groups.flatMap(g => g.items) : allItems;
  const hash = decodeURIComponent(location.hash.slice(1));
  if (mode !== 'desayunos' && MENU[hash]) state.tab = hash;

  const tabList = mode === 'desayunos'
    ? [['todo', 'Todo'], ...groups.map((g, k) => ['g' + k, g.g])]
    : Object.entries(MENU).filter(([k]) => k !== 'desayunos').map(([k, c]) => [k, c.label]);
  const matches = i => {
    if (state.filters.size && ![...state.filters].every(f => i.t.includes(f))) return false;
    return state.q ? norm(i.n + ' ' + i.d + ' ' + i.t.join(' ')).includes(norm(state.q)) : true;
  };
  const filters = mode === 'desayunos' ? ['dulce', 'veg'] : FILTERS;
  const render = () => {
    tabsEl.innerHTML = tabList.map(([k, l]) => `<button class="tab" role="tab" data-tab="${k}" aria-selected="${!state.q && k === state.tab}">${esc(l)}${catCount[k] ? `<small>${catCount[k]}</small>` : ''}</button>`).join('');
    chipsEl.innerHTML = filters.map(f => `<button class="chip" data-f="${f}" aria-pressed="${state.filters.has(f)}">${TAGLABEL[f]}</button>`).join('');
    let html = '', n = 0;
    if (state.q) {
      const res = pool.filter(matches);
      html = res.length ? res.map((i, k) => card(i, k)).join('') : `<div class="empty">Nada por aquí con “${esc(state.q)}”. Prueba con otra palabra.</div>`;
    } else if (mode === 'desayunos') {
      groups.forEach((g, k) => {
        if (state.tab !== 'todo' && state.tab !== 'g' + k) return;
        const its = g.items.filter(matches); if (!its.length) return;
        html += `<h3 class="menu__group">${g.g}</h3>` + its.map(i => card(i, n++)).join('');
        if (g.note) html += `<div class="menu__note">${esc(g.note)}</div>`;
      });
      if (!n) html = `<div class="empty">Nada con esos filtros.</div>`;
    } else {
      const c = MENU[state.tab];
      if (c.note) html += `<div class="menu__note">${esc(c.note)}</div>`;
      const its = c.items.filter(matches);
      html += its.length ? its.map((i, k) => card(i, k)).join('') : `<div class="empty">Ningún plato de esta sección cumple los filtros.</div>`;
    }
    menuEl.innerHTML = html; dispatchEvent(new Event('menu-render'));
  };
  tabsEl.addEventListener('click', e => { const b = e.target.closest('[data-tab]'); if (!b) return; state.tab = b.dataset.tab; state.q = ''; qEl.value = ''; render(); });
  chipsEl.addEventListener('click', e => { const b = e.target.closest('[data-f]'); if (!b) return; state.filters.has(b.dataset.f) ? state.filters.delete(b.dataset.f) : state.filters.add(b.dataset.f); render(); });
  const ft = $('#filtersBtn'); if (ft) ft.addEventListener('click', () => { const o = chipsEl.classList.toggle('open'); ft.setAttribute('aria-expanded', o); });
  qEl.addEventListener('input', e => { state.q = e.target.value.trim(); render(); });
  render();
}

/* ---------- Destacados (los que Just Eat marca como destacados) ---------- */
const feat = $('#featured');
const featB = $('#featuredB');
if (featB) featB.innerHTML = ['Salmón y mascarpone', 'Pancakes de Ferrero', 'Pancakes de Nutella', 'Matcha goloso'].map((n, k) => { const it = allItems.find(i => i.n === n && i.cat === 'desayunos'); return it ? card(it, k) : ''; }).join('');
if (feat) feat.innerHTML = ['Doble Dosis', 'La Puerquita', 'La Dori', 'La Triplona', 'Gordi Deluxe', 'Patatas trufadas']
  .map((n, k) => card(allItems.find(i => i.n === n), k)).join('');

/* ---------- Contadores ---------- */
$$('[data-stat]').forEach(el => {
  const k = el.dataset.stat;
  el.textContent = k === 'burgers' ? MENU.hamburguesas.items.length : k === 'desa' ? MENU.desayunos.groups.flatMap(g => g.items).length : k === 'dishes' ? allItems.length : k;
});

/* ---------- Horario y estado (orientativo, según Toppings & Salads) ---------- */
const DAYS = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
const HOURS = { 0: [9, 23.5], 1: [8, 23], 2: [8, 23], 3: [8, 23], 4: [8, 23], 5: [8, 24], 6: [9, 24] };
const fmt = h => `${String(Math.floor(h) % 24).padStart(2, '0')}:${h % 1 ? '30' : '00'}`;
const now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/Madrid' }));
const today = now.getDay(), hr = now.getHours() + now.getMinutes() / 60;
const hoursEl = $('#hours');
if (hoursEl) {
  hoursEl.innerHTML = [1, 2, 3, 4, 5, 6, 0].map(d => `<li class="${d === today ? 'today' : ''}"><span>${DAYS[d]}</span><span>${fmt(HOURS[d][0])} – ${fmt(HOURS[d][1])}</span></li>`).join('');
  $('#todayLabel').textContent = 'hoy, ' + DAYS[today].toLowerCase();
}
const st = $('#openStatus');
if (st) {
  const [o, c] = HOURS[today], open = hr >= o && hr < c;
  st.textContent = open ? `Abierto ahora · hasta las ${fmt(c)}` : `Cerrado ahora · abrimos ${hr < o ? 'hoy' : 'mañana'} a las ${fmt(hr < o ? o : HOURS[(today + 1) % 7][0])}`;
  st.previousElementSibling.classList.toggle('on', open);
}
$$('.yr').forEach(e => e.textContent = new Date().getFullYear());

/* ---------- Pedido por WhatsApp ---------- */
const WA = '34747486092';
const openNow = (() => { const [o, c] = HOURS[today]; return hr >= o && hr < c; })();
const nextOpen = (() => { const [o] = HOURS[today]; return hr < o ? `hoy a las ${fmt(o)}` : `mañana a las ${fmt(HOURS[(today + 1) % 7][0])}`; })();
let cart = [];
try { cart = JSON.parse(localStorage.getItem('alma-cart2') || '[]'); } catch (e) { cart = []; }
cart = Array.isArray(cart) ? cart.filter(l => byId(l.id)) : [];
const persist = () => { try { localStorage.setItem('alma-cart2', JSON.stringify(cart)); } catch (e) {} };
const lineTotal = l => byId(l.id).p * l.qty;
const total = () => cart.reduce((s, l) => s + lineTotal(l), 0);
const count = () => cart.reduce((s, l) => s + l.qty, 0);
const countOf = id => cart.filter(l => l.id === id).reduce((s, l) => s + l.qty, 0);

const cartEl = $('#cart'), scrim = $('#scrim'), toastEl = $('#toast'), bar = $('#orderbar');
let editing = null, toastT;
function toast(msg) {
  toastEl.innerHTML = `<span>${msg}</span><button type="button" data-view>Ver pedido</button>`;
  toastEl.classList.add('on'); clearTimeout(toastT); toastT = setTimeout(() => toastEl.classList.remove('on'), 3200);
}
toastEl.addEventListener('click', e => { if (e.target.closest('[data-view]')) { toastEl.classList.remove('on'); openCart(true); } });
const lock = o => document.documentElement.classList.toggle('lock', !!o);
function openCart(o) {
  cartEl.classList.toggle('open', o); if (o) toastEl.classList.remove('on'); scrim.classList.toggle('on', o); cartEl.setAttribute('aria-hidden', !o); lock(o);
  if (o) setTimeout(() => $('#cartClose').focus(), 50);
}
function push(id, opt = '', qty = 1) {
  const l = cart.find(x => x.id === id && x.opt === opt);
  if (l) l.qty += qty; else cart.push({ id, opt, note: '', qty });
  persist(); draw();
  const b = $('#cartOpen'); b.classList.remove('bump'); void b.offsetWidth; b.classList.add('bump');
}
function addItem(id) {
  const it = byId(id);
  if (it.o) return openOpt(it);
  push(id); toast(`<b>${esc(it.n)}</b> añadido ✓`);
}

/* modal de opciones */
const om = document.createElement('div'); om.className = 'modal'; om.id = 'optModal';
om.innerHTML = `<div class="modal__box" role="dialog" aria-modal="true" aria-labelledby="omT"><button class="modal__x" type="button" aria-label="Cerrar">✕</button>
  <h3 id="omT"></h3><p class="modal__s" id="omS"></p><div class="choices" id="omChoices"></div>
  <button class="btn btn--solid btn--block" id="omOk" type="button">Añadir al pedido</button></div>`;
document.body.appendChild(om);
let omItem = null;
function openOpt(it) {
  omItem = it; $('#omT').textContent = it.n; $('#omS').textContent = `${eur(it.p)} · Elige una opción`;
  $('#omChoices').innerHTML = it.o.map((c, k) => `<label class="choice"><input type="radio" name="opt" value="${esc(c)}" ${k ? '' : 'checked'}><span>${esc(c)}</span></label>`).join('');
  om.classList.add('on'); lock(true);
}
const closeModals = () => { $$('.modal').forEach(m => m.classList.remove('on')); lock(cartEl.classList.contains('open')); };
om.addEventListener('click', e => {
  if (e.target === om || e.target.closest('.modal__x')) closeModals();
  if (e.target.closest('#omOk')) {
    const v = $('input[name=opt]:checked', om).value; push(omItem.id, v); closeModals(); toast(`<b>${esc(omItem.n)}</b> (${esc(v.toLowerCase())}) añadido ✓`);
  }
});

/* dibujar carrito */
function draw() {
  const n = count(), t = total();
  $('#cartCount').textContent = n;
  $('#cartTotal').textContent = eur(t);
  $('#cartEmpty').hidden = n > 0; $('#checkout').hidden = !n; $('#cartList').hidden = !n; $('#cartFoot').hidden = !n;
  $('#cartList').innerHTML = cart.map((l, k) => { const i = byId(l.id); return `<li>
    <div class="ln"><b>${l.qty}× ${esc(i.n)}</b><span>${eur(lineTotal(l))}</span></div>
    ${l.opt ? `<small>${esc(l.opt)}</small>` : ''}
    <div class="qty"><button type="button" data-dec="${k}" aria-label="Quitar uno">−</button><span>${l.qty}</span><button type="button" data-inc="${k}" aria-label="Añadir uno">+</button>
      <button type="button" class="lnk" data-note="${k}">${l.note ? 'Editar nota' : 'Añadir nota'}</button><button type="button" class="lnk" data-rm="${k}">Quitar</button></div>
    ${editing === k ? `<input class="noteinp" data-ni="${k}" maxlength="120" value="${esc(l.note)}" placeholder="Sin cebolla, poco hecha…">` : (l.note ? `<small class="note">“${esc(l.note)}”</small>` : '')}</li>`; }).join('');
  if (editing !== null) { const inp = $('[data-ni]'); if (inp) inp.focus(); }
  $('#orderbarN').textContent = n; $('#orderbarT').textContent = eur(t);
  const bn = $('#bnavN'); if (bn) { bn.hidden = !n; bn.textContent = n; if (!window.ALMA_AGORA) $('#bnavT').textContent = n ? eur(t) : 'Pedido'; }
  bar.hidden = !n || cartEl.classList.contains('open'); document.body.classList.toggle('has-bar', !!n);
  sync();
}
function sync() {
  $$('[data-add]').forEach(b => { const n = countOf(b.dataset.add); b.classList.toggle('in', n > 0); const s = $('.add__n', b); if (s) s.textContent = n || ''; });
}
addEventListener('menu-render', sync);
document.addEventListener('click', e => { const b = e.target.closest('[data-add]'); if (b) addItem(b.dataset.add); });
$('#cartList').addEventListener('click', e => {
  const g = a => { const x = e.target.closest(`[${a}]`); return x ? +x.getAttribute(a) : null; };
  const inc = g('data-inc'), dec = g('data-dec'), rm = g('data-rm'), nt = g('data-note');
  if (inc !== null) cart[inc].qty++;
  if (dec !== null) { cart[dec].qty--; if (cart[dec].qty <= 0) cart.splice(dec, 1); }
  if (rm !== null) cart.splice(rm, 1);
  if (nt !== null) { editing = editing === nt ? null : nt; }
  persist(); draw();
});
const saveNote = e => { const inp = e.target.closest('[data-ni]'); if (!inp) return; cart[+inp.dataset.ni].note = inp.value.trim(); editing = null; persist(); draw(); };
$('#cartList').addEventListener('focusout', saveNote);
$('#cartList').addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.matches('[data-ni]')) { e.preventDefault(); saveNote(e); } });
$('#cartClear').addEventListener('click', () => { if (!cart.length || confirm('¿Vaciar el pedido?')) { cart = []; persist(); draw(); } });
$('#cartOpen').addEventListener('click', () => openCart(true));
const bc = $('#bnavCart'); if (bc) bc.addEventListener('click', () => openCart(true));
$('#cartClose').addEventListener('click', () => openCart(false));
bar.addEventListener('click', () => openCart(true));
scrim.addEventListener('click', () => openCart(false));
document.addEventListener('keydown', e => { if (e.key === 'Escape') { openCart(false); closeModals(); pm && pm.classList.remove('on'); } });

/* formulario de pedido */
const ck = $('#checkout');
$('#closedNote').hidden = openNow;
$('#closedNote').textContent = `Ahora estamos cerrados. Puedes enviar el pedido y lo prepararemos al abrir (${nextOpen}).`;
try { const c = JSON.parse(localStorage.getItem('alma-cust') || '{}'); if (c.nombre) ck.nombre.value = c.nombre; if (c.tel) ck.tel.value = c.tel; if (c.dir) ck.direccion.value = c.dir; } catch (e) {}
const syncForm = () => {
  const dom = ck.tipo.value === 'domicilio';
  $('#fDir').hidden = !dom; ck.direccion.required = dom; $('#domNote').hidden = !dom;
  $('#lCuando').firstChild.textContent = dom ? '¿Para cuándo lo quieres?' : '¿Cuándo lo recoges?';
  $('#fHora').hidden = ck.cuando.value !== 'hora'; ck.hora.required = ck.cuando.value === 'hora';
};
ck.addEventListener('change', syncForm); syncForm();
ck.addEventListener('submit', e => {
  e.preventDefault(); if (!cart.length) return;
  const v = Object.fromEntries(new FormData(ck));
  try { localStorage.setItem('alma-cust', JSON.stringify({ nombre: v.nombre, tel: v.tel, dir: v.direccion || '' })); } catch (er) {}
  const cuando = v.cuando === 'hora' ? `a las ${v.hora}` : 'lo antes posible';
  const lines = cart.map(l => `• ${l.qty}x ${byId(l.id).n}${l.opt ? ` (${l.opt})` : ''} — ${eur(lineTotal(l))}${l.note ? `\n   ↳ ${l.note}` : ''}`);
  const dom = v.tipo === 'domicilio';
  const info = [`*Nombre:* ${v.nombre}`, `*Teléfono:* ${v.tel}`, `*Tipo:* ${dom ? 'A domicilio' : 'Recoger en el local'}`, dom && `*Dirección:* ${v.direccion}`, `*${dom ? 'Entrega' : 'Recogida'}:* ${cuando}`].filter(Boolean);
  const extra = [v.alergias && `*Alergias/intolerancias:* ${v.alergias}`, v.notas && `*Notas:* ${v.notas}`].filter(Boolean);
  const msg = [`¡Hola Alma Burger! Quiero hacer un pedido ${dom ? 'a domicilio' : 'para recoger'} 🍔`, '', ...info, '', '*Pedido:*', ...lines, '', `*Total:* ${eur(total())} (IVA incluido)`, ...(extra.length ? ['', ...extra] : []), '', '¿Me confirmáis el total y cómo pagar por Bizum? ¡Gracias!'].join('\n');
  window.open(`https://wa.me/${WA}?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
});

/* menú «Pedir» de la cabecera */
const pb = $('#pedirBtn'), pm = $('#pedirMenu');
if (pb) {
  pb.addEventListener('click', e => { e.stopPropagation(); const o = pm.classList.toggle('on'); pb.setAttribute('aria-expanded', o); });
  document.addEventListener('click', e => { if (!e.target.closest('.pedir')) { pm.classList.remove('on'); pb.setAttribute('aria-expanded', false); } });
}
const goOrder = () => {
  pm && pm.classList.remove('on');
  if (count()) return openCart(true);
  if (menuEl && menuEl.dataset.mode === 'all') { menuEl.scrollIntoView({ behavior: 'smooth', block: 'start' }); toast('Pulsa <b>+</b> en los platos que quieras'); }
  else location.href = 'carta.html#pedir';
};
document.addEventListener('click', e => { if (e.target.closest('[data-wa-order]')) { e.preventDefault(); goOrder(); } });
if (location.hash === '#pedir' && menuEl) setTimeout(() => toast('Pulsa <b>+</b> en los platos que quieras'), 600);

/* menú sorpresa */
const sm = document.createElement('div'); sm.className = 'modal'; sm.id = 'surprise';
sm.innerHTML = `<div class="modal__box modal__box--wide" role="dialog" aria-modal="true" aria-labelledby="smT"><button class="modal__x" type="button" aria-label="Cerrar">✕</button>
  <h3 id="smT">Tu menú sorpresa</h3><p class="modal__s">Una burger, algo para compartir y un postre. Si no te gusta, otra tirada.</p>
  <div class="reels" id="reels"></div><div class="modal__row"><span class="price" id="smTotal"></span><button class="btn" type="button" id="smAgain">Otra tirada</button><button class="btn btn--solid" type="button" id="smAdd">Añadir los 3 al pedido</button></div></div>`;
document.body.appendChild(sm);
const rnd = a => a[Math.floor(Math.random() * a.length)];
let picks = [], spinning = false;
const pools = [['Burger', MENU.hamburguesas.items], ['Para compartir', MENU.compartir.items], ['Postre', MENU.postres.items]];
function spin() {
  if (spinning) return; spinning = true;
  picks = pools.map(([l, p]) => { const it = rnd(p); return { it, opt: it.o ? rnd(it.o) : '' }; });
  const rs = $('#reels'); rs.innerHTML = pools.map(([l]) => `<div class="reel spin"><small>${l}</small><div class="reel__v">…</div></div>`).join('');
  $('#smTotal').textContent = ''; $('#smAdd').disabled = true;
  const els = $$('.reel', rs);
  els.forEach((el, k) => {
    const v = $('.reel__v', el), t0 = Date.now(), dur = 900 + k * 450;
    const iv = setInterval(() => {
      if (Date.now() - t0 > dur) {
        clearInterval(iv); const { it, opt } = picks[k]; el.classList.remove('spin'); el.classList.add('done');
        v.innerHTML = `${it.i ? `<img src="img/dishes/s/${it.i}.jpg" alt="">` : ''}<b>${esc(it.n)}</b>${opt ? `<em>${esc(opt)}</em>` : ''}<span>${eur(it.p)}</span>`;
        if (k === 2) { spinning = false; $('#smAdd').disabled = false; $('#smTotal').textContent = 'Total ' + eur(picks.reduce((s, p) => s + p.it.p, 0)); }
      } else v.textContent = rnd(pools[k][1]).n;
    }, 70);
  });
}
const openSurprise = () => { sm.classList.add('on'); lock(true); spin(); };
document.addEventListener('click', e => { if (e.target.closest('[data-surprise]')) { pm && pm.classList.remove('on'); openSurprise(); } });
sm.addEventListener('click', e => {
  if (e.target === sm || e.target.closest('.modal__x')) closeModals();
  if (e.target.closest('#smAgain')) spin();
  if (e.target.closest('#smAdd') && !spinning) { picks.forEach(p => push(p.it.id, p.opt)); closeModals(); openCart(true); }
});

/* progreso de lectura */
const prog = $('#progress');
const onScroll = () => { const h = document.documentElement.scrollHeight - innerHeight; prog.style.transform = `scaleX(${h > 0 ? scrollY / h : 0})`; };
addEventListener('scroll', onScroll, { passive: true }); onScroll();
draw();

/* ---------- Reserva por WhatsApp ---------- */
const rf = $('#reserva');
if (rf) {
  const d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset());
  rf.fecha.min = d.toISOString().slice(0, 10);
  rf.addEventListener('submit', e => {
    e.preventDefault();
    const v = Object.fromEntries(new FormData(rf));
    const f = new Date(v.fecha + 'T00:00').toLocaleDateString('es-ES', { weekday: 'long', day: 'numeric', month: 'long' });
    const msg = `¡Hola Alma Burger! Quisiera reservar mesa:\n• Nombre: ${v.nombre}\n• Personas: ${v.personas}\n• Día: ${f}\n• Hora: ${v.hora}${v.nota ? '\n• Nota: ' + v.nota : ''}\n\n¿Me confirmáis? ¡Gracias!`;
    window.open('https://wa.me/34747486092?text=' + encodeURIComponent(msg), '_blank', 'noopener');
  });
}

/* ---------- Lightbox ---------- */
const mis = $$('.mi');
if (mis.length) {
  const lb = document.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-label', 'Foto ampliada');
  lb.innerHTML = '<button class="x" aria-label="Cerrar">✕</button><button class="p" aria-label="Anterior">‹</button><img alt="" hidden><button class="n" aria-label="Siguiente">›</button><p></p>';
  document.body.appendChild(lb);
  let cur = 0;
  const show = k => { cur = (k + mis.length) % mis.length; const im = $('img', mis[cur]); $('img', lb).hidden = false; $('img', lb).src = im.currentSrc || im.src; $('img', lb).alt = im.alt; $('p', lb).textContent = $('figcaption', mis[cur])?.textContent || im.alt; lb.classList.add('on'); };
  mis.forEach((m, k) => m.addEventListener('click', () => show(k)));
  lb.addEventListener('click', e => { if (e.target === lb || e.target.matches('.x')) lb.classList.remove('on'); if (e.target.matches('.p')) show(cur - 1); if (e.target.matches('.n')) show(cur + 1); });
  document.addEventListener('keydown', e => { if (!lb.classList.contains('on')) return; if (e.key === 'Escape') lb.classList.remove('on'); if (e.key === 'ArrowLeft') show(cur - 1); if (e.key === 'ArrowRight') show(cur + 1); });
}

/* ---------- Nav, reveal, parallax ---------- */
const nav = $('#nav'), links = $('.nav__links'), burger = $('#burgerBtn');
const stuck = () => nav.classList.toggle('is-stuck', scrollY > 30);
addEventListener('scroll', stuck, { passive: true }); stuck();
burger.addEventListener('click', () => { const o = links.classList.toggle('open'); burger.setAttribute('aria-expanded', o); });
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12 });
$$('.reveal').forEach((el, i) => { el.style.transitionDelay = (i % 4) * 70 + 'ms'; io.observe(el); });
const revealNow = () => $$('.reveal:not(.in)').forEach(el => { if (el.getBoundingClientRect().top < innerHeight * 1.05) el.classList.add('in'); });
revealNow(); setTimeout(revealNow, 350); addEventListener('load', revealNow); addEventListener('scroll', revealNow, { passive: true });
const hv = $('#heroVisual');
if (hv && matchMedia('(hover:hover)').matches && !matchMedia('(prefers-reduced-motion:reduce)').matches) {
  const ph = $$('.hero__photo', hv);
  hv.addEventListener('mousemove', e => {
    const r = hv.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
    ph[0].style.transform = `rotate(${-3 + x * 3}deg) translate(${x * 10}px,${y * 10}px)`;
    ph[1].style.transform = `rotate(${5 - x * 4}deg) translate(${-x * 16}px,${-y * 16}px)`;
  });
}

/* ---------- Ficha del plato (ventana con la foto completa) ---------- */
const JE = 'https://www.just-eat.es/restaurants-alma-burger-ordizia/menu';
const AI_SLUGS = new Set(['la-basica', 'la-golosa', 'la-diabla', 'tequenos', 'alitas', 'ensalada', 'panceta', 'hot-clasica', 'hot-gordita', 'hot-quesuda', 'hot-picantona', 'tarta-pistacha', 'tarta-ferrero', 'coulant', 'crepe']);
const dm = document.createElement('div'); dm.className = 'modal dish'; dm.id = 'dishModal';
dm.innerHTML = `<div class="dish__box" role="dialog" aria-modal="true" aria-labelledby="dishT">
  <button class="modal__x" type="button" aria-label="Cerrar">✕</button>
  <div class="dish__media" id="dishMedia"><div class="dish__bg" id="dishBg"></div><img id="dishImg" alt="" decoding="async" hidden><div class="dish__none" id="dishNone"></div>
    <span class="dish__ai" id="dishAi" hidden>Imagen orientativa generada por IA</span>
    <button class="dish__nav dish__nav--p" type="button" aria-label="Plato anterior">‹</button><button class="dish__nav dish__nav--n" type="button" aria-label="Plato siguiente">›</button>
    <span class="dish__count" id="dishCount"></span></div>
  <div class="dish__info"><span class="dish__cat" id="dishCat"></span><h3 id="dishT"></h3><div class="tags" id="dishTags"></div><p class="dish__desc" id="dishDesc"></p>
    <div class="choices" id="dishOpts"></div>
    <div class="dish__foot"><div class="dish__buy"><span class="price" id="dishPrice"></span><div class="stepper"><button type="button" data-q="-1" aria-label="Menos">−</button><span id="dishQ">1</span><button type="button" data-q="1" aria-label="Más">+</button></div></div>
    <button class="btn btn--solid btn--block" type="button" id="dishAdd"></button><a class="btn btn--solid btn--block dish__agora" id="dishAgora" target="_blank" rel="noopener">Pedir online ↗</a></div>
    <p class="dish__fine" id="dishFine">Pedido por WhatsApp, para recoger o a domicilio. Pago por Bizum, que confirma el local. <a href="${JE}" target="_blank" rel="noopener">¿Prefieres Just Eat? ↗</a><br>Consulta nuestra carta de alérgenos al personal. Las imágenes son orientativas.</p></div></div>`;
document.body.appendChild(dm);
const D = { list: [], k: 0, qty: 1, from: null };
const dq = s => $(s, dm);
function renderDish(dir) {
  const it = byId(D.list[D.k]); if (!it) return;
  const box = dq('.dish__box');
  const m = dq('#dishMedia');
  m.classList.remove('swap-l', 'swap-r'); void m.offsetWidth; if (dir) m.classList.add(dir > 0 ? 'swap-r' : 'swap-l');
  const img = dq('#dishImg'), bg = dq('#dishBg'), none = dq('#dishNone');
  if (it.i) {
    img.hidden = false; none.hidden = true; img.alt = it.n;
    bg.style.backgroundImage = `url(img/dishes/s/${it.i}.jpg)`;
    img.src = `img/dishes/${it.i}.jpg`;
  } else { img.hidden = true; none.hidden = false; none.innerHTML = RIG; bg.style.backgroundImage = 'none'; }
  dq('#dishAi').hidden = !(it.i && AI_SLUGS.has(it.i));
  dq('#dishCat').textContent = MENU[it.cat].label;
  dq('#dishT').textContent = it.n;
  dq('#dishTags').innerHTML = it.t.map(t => `<span class="tag ${t === 'nuevo' || t === 'mes' ? 'tag--new' : ''}">${TAGLABEL[t]}</span>`).join('');
  dq('#dishDesc').textContent = it.d || 'Sin descripción. Pregúntanos en el local si tienes dudas.';
  dq('#dishOpts').innerHTML = it.o ? `<p class="choices__t">Elige una opción</p>` + it.o.map((c, k) => `<label class="choice"><input type="radio" name="dopt" value="${esc(c)}" ${k ? '' : 'checked'}><span>${esc(c)}</span></label>`).join('') : '';
  dq('#dishPrice').textContent = eur(it.p);
  D.qty = 1; dq('#dishQ').textContent = 1; dishBtn();
  dq('#dishCount').textContent = D.list.length > 1 ? `${D.k + 1} / ${D.list.length}` : '';
  $$('.dish__nav', dm).forEach(b => b.hidden = D.list.length < 2);
  box.scrollTop = 0; dq('.dish__info').scrollTop = 0;
  [1, -1].forEach(d => { const o = byId(D.list[(D.k + d + D.list.length) % D.list.length]); if (o && o.i) new Image().src = `img/dishes/${o.i}.jpg`; });
}
if (window.ALMA_AGORA) { const da = document.querySelector('#dishAgora'); if (da) da.href = window.ALMA_AGORA; const df = document.querySelector('#dishFine'); if (df) df.innerHTML = 'Pide online para recoger o a domicilio. <a href="' + JE + '" target="_blank" rel="noopener">¿Prefieres Just Eat? ↗</a><br>Consulta nuestra carta de alérgenos al personal. Las imágenes son orientativas.'; }
const dishBtn = (done) => { const it = byId(D.list[D.k]); dq('#dishAdd').textContent = done ? 'Añadido ✓' : `Añadir al pedido · ${eur(it.p * D.qty)}`; };
function openDish(id, from) {
  const vis = $$('.item[data-open]').filter(e => e.offsetParent !== null).map(e => e.dataset.open);
  D.list = vis.includes(id) ? [...new Set(vis)] : [id]; D.k = D.list.indexOf(id); D.from = from || null;
  renderDish(0); dm.classList.add('on'); lock(true); setTimeout(() => dq('.modal__x').focus(), 60);
}
const stepDish = d => { D.k = (D.k + d + D.list.length) % D.list.length; renderDish(d); };
document.addEventListener('click', e => {
  const it = e.target.closest('.item[data-open]');
  if (it && !e.target.closest('.add')) openDish(it.dataset.open, it);
});
document.addEventListener('keydown', e => {
  const it = e.target.closest && e.target.closest('.item[data-open]');
  if (it && e.target === it && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); openDish(it.dataset.open, it); }
  if (!dm.classList.contains('on')) return;
  if (e.key === 'ArrowLeft') stepDish(-1);
  if (e.key === 'ArrowRight') stepDish(1);
});
dm.addEventListener('click', e => {
  if (e.target === dm || e.target.closest('.modal__x')) { closeModals(); if (D.from) D.from.focus({ preventScroll: true }); return; }
  if (e.target.closest('.dish__nav--p')) stepDish(-1);
  if (e.target.closest('.dish__nav--n')) stepDish(1);
  const q = e.target.closest('[data-q]');
  if (q) { D.qty = Math.max(1, Math.min(20, D.qty + +q.dataset.q)); dq('#dishQ').textContent = D.qty; dishBtn(); }
  if (e.target.closest('#dishAdd')) {
    const it = byId(D.list[D.k]); const o = $('input[name=dopt]:checked', dm);
    push(it.id, o ? o.value : '', D.qty); dishBtn(true); setTimeout(() => dm.classList.contains('on') && dishBtn(), 1400);
    toast(`<b>${esc(it.n)}</b>${D.qty > 1 ? ` ×${D.qty}` : ''} añadido ✓`);
  }
});
// deslizar la foto para cambiar de plato
(() => {
  const m = dq('#dishMedia'); let x0 = null, y0 = 0;
  m.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
  m.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0; x0 = null; if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.4 && D.list.length > 1) stepDish(dx < 0 ? 1 : -1); }, { passive: true });
})();

const hb = $('#hmoreBtn');
if (hb) hb.addEventListener('click', () => { const o = $('#hmore').classList.toggle('open'); hb.setAttribute('aria-expanded', o); hb.textContent = o ? 'Leer menos ↑' : 'Seguir leyendo ↓'; });

/* ---------- Mascota del hero: cinco entradas por detrás del logo ---------- */
const stageEl = $('#stage');
if (stageEl) {
  const get = id => document.getElementById(id), set = (id, n, v) => get(id).setAttribute(n, v);
  const smooth = x => { x = Math.max(0, Math.min(1, x)); return x * x * (3 - 2 * x); }, mix = (a, b, u) => a + (b - a) * u;
  const TITLES = ['Salto sorpresa', 'Desde la izquierda', 'Giro desde la derecha', 'Tres rebotes', 'Arco y reverencia'];
  let mode = 0, time = 0, previous = null, auto = true, paused = false;
  function limbs(v) {
    const { lx = 386, ly = 567, rx = 624, ry = 652, leftAngle = 0, rightAngle = 0, flx = 474, fly = 762, frx = 539, fry = 762, footAngleL = 0, footAngleR = 0, knee = 9 } = v;
    set('legLeft', 'd', `M480 665 Q${(480 + flx) / 2 + knee} ${(665 + fly) / 2} ${flx} ${fly - 12}`); set('legRight', 'd', `M528 665 Q${(528 + frx) / 2 - knee} ${(665 + fry) / 2} ${frx} ${fry - 12}`);
    set('footLeft', 'transform', `translate(${flx} ${fly}) rotate(${footAngleL})`); set('footRight', 'transform', `translate(${frx} ${fry}) rotate(${footAngleR}) scale(-1 1)`);
    set('armLeft', 'd', `M435 612 Q${398 + (lx - 386) * .55} ${603 + (ly - 567) * .55} ${lx} ${ly}`); set('armRight', 'd', `M590 612 Q${600 + (rx - 624) * .5} ${641 + (ry - 652) * .6} ${rx} ${ry}`);
    set('handLeft', 'transform', `translate(${lx - 386} ${ly - 567}) rotate(${leftAngle} 386 567)`); set('handRight', 'transform', `translate(${rx - 624} ${ry - 652}) rotate(${rightAngle} 624 652)`);
  }
  function pose(t) {
    const c = t % 10; let x = 510, y = 286, scale = .65, angle = 0, stretch = 1, wide = 1, alpha = smooth((c - .2) / .35), raise = 0, hello = 0, bend = 0;
    if (mode === 1) { x = 380; y = 282; } else if (mode === 2) { x = 640; y = 280; } else if (mode === 3) { scale = .58; y = 284; } else if (mode === 4) { x = 540; y = 280; scale = .62; }
    const hidden = { x, y, scale };
    if (c < 2) { const p = smooth((c - .45) / .85), look = Math.sin(Math.max(0, c - .8) * Math.PI * 3) * 3; y -= 58 * p; angle = look; hello = mode === 4 ? p * Math.sin(c * 9) : 0; if (mode === 1) x -= 52 * p; if (mode === 2) x += 46 * p; }
    else if (c < 3.7) {
      const u = (c - 2) / 1.7, e = smooth(u), lift = Math.sin(Math.PI * u); let startX = hidden.x, startY = hidden.y - 58;
      if (mode === 1) startX -= 52; if (mode === 2) startX += 46;
      x = mix(startX, 510, e); y = mix(startY, 725, e) - (mode === 4 ? 135 : mode === 1 ? 95 : 110) * lift; scale = mix(hidden.scale, 1, e); raise = lift;
      if (mode === 0) { angle = -8 * lift; x += 15 * Math.sin(u * Math.PI * 2); }
      if (mode === 1) { x -= 42 * lift; angle = 18 * lift; }
      if (mode === 2) { x += 35 * lift; angle = -360 * e; }
      if (mode === 3) { angle = 5 * Math.sin(u * Math.PI * 2); stretch = 1 + .08 * lift; wide = 1 - .04 * lift; }
      if (mode === 4) { x += 135 * Math.sin(Math.PI * u); angle = -16 * Math.sin(Math.PI * u); }
    } else {
      scale = 1; x = 510; y = 725; angle = mode === 2 ? -360 : 0;
      if (c < 4.15) { const settle = Math.sin(Math.PI * (c - 3.7) / .45); stretch = 1 - .13 * settle; wide = 1 + .08 * settle; y = 822 - 97 * stretch; bend = settle; }
      if (mode === 3 && c >= 4.2 && c < 6.2) { const q = (c - 4.2) % 1, h = Math.sin(Math.PI * q); y = 725 - (c < 5.2 ? 45 : 27) * h; raise = h * .7; stretch = 1 + .025 * h; }
      if (mode === 4 && c >= 4.5 && c < 6.6) { const bow = Math.sin(Math.PI * (c - 4.5) / 2.1); angle = 14 * bow; bend = bow * .2; }
      if (c >= 6.2 && c < 7.8) { hello = Math.sin((c - 6.2) * Math.PI * 4); angle += (mode === 2 ? 0 : Math.sin((c - 6.2) * 4) * 1.5); }
    }
    // vuelve detrás de las letras antes de repetir
    if (c >= 8.3) { const u = smooth((c - 8.3) / 1.1); x = mix(x, hidden.x, u); y = mix(y, hidden.y, u) - 55 * Math.sin(Math.PI * u); scale = mix(scale, hidden.scale, u); alpha = 1 - smooth((c - 9.05) / .5); hello = 0; raise = .4 * Math.sin(Math.PI * u); angle *= 1 - u; }
    set('traveler', 'opacity', alpha); set('traveler', 'transform', `translate(${x} ${y}) rotate(${angle}) scale(${scale * wide} ${scale * stretch}) translate(-510 -665)`);
    const distance = Math.abs(725 - y), sa = Math.max(0, 1 - distance / 140) * .12 * alpha; set('shadow', 'opacity', sa); set('shadow', 'rx', 78 - Math.min(45, distance * .3));
    limbs({ lx: 386 + raise * 20 + hello * 11, ly: 567 - raise * 45 - Math.abs(hello) * 5, rx: 624 + raise * 25, ry: 652 - raise * 100, leftAngle: hello * 16 - raise * 14, rightAngle: -raise * 35, flx: 474 - bend * 10, frx: 539 + bend * 10, fly: 762, fry: 762, knee: 9 + bend * 20 });
  }
  const dots = $('#stageDots');
  if (dots) dots.innerHTML = TITLES.map((t, k) => `<button type="button" data-m="${k}" aria-label="Entrada ${k + 1}: ${t}" title="${t}"></button>`).join('');
  const mark = () => $$('#stageDots button').forEach((b, k) => b.setAttribute('aria-pressed', String(k === mode)));
  const choose = (n, manual) => { mode = n; time = 0; if (manual) auto = false; mark(); pose(0); };
  if (dots) dots.addEventListener('click', e => { const b = e.target.closest('[data-m]'); if (b) choose(+b.dataset.m, true); });
  let lastCycle = 0;
  const tick = now => {
    if (previous !== null && !paused) time += Math.min(.1, (now - previous) / 1000);
    previous = now;
    if (auto && Math.floor(time / 10) !== lastCycle) { lastCycle = Math.floor(time / 10); mode = (mode + 1) % 5; mark(); }
    pose(time); requestAnimationFrame(tick);
  };
  document.addEventListener('visibilitychange', () => { previous = null; });
  window.AlmaStage = { seek: (t, m) => { paused = true; auto = false; if (m !== undefined) mode = m; time = t; mark(); pose(t); } };
  mark();
  if (matchMedia('(prefers-reduced-motion:reduce)').matches) { paused = true; auto = false; time = 7; pose(time); } else { pose(0); requestAnimationFrame(tick); }
}



/* ---------- índice de capítulos: marca el que estás leyendo ---------- */
(() => {
  const nav = $('.chapnav'); if (!nav) return;
  const links = $$('a', nav), secs = links.map(a => $(a.getAttribute('href')));
  const mark = () => {
    let cur = 0; secs.forEach((s, i) => { if (s && s.getBoundingClientRect().top < innerHeight * .4) cur = i; });
    links.forEach((a, i) => a.setAttribute('aria-current', String(i === cur)));
    const on = links[cur]; if (on && nav.firstElementChild.scrollWidth > nav.firstElementChild.clientWidth) { const w = nav.firstElementChild; w.scrollTo({ left: on.offsetLeft - 20, behavior: 'smooth' }); }
  };
  addEventListener('scroll', mark, { passive: true }); mark();
})();

/* ---------- La mascota comenta la carta ---------- */
(() => {
  const page = location.pathname.split('/').pop().replace('.html', '') || 'index';
  const hasItems = !!document.querySelector('[data-open], #menu, #featured, #featuredB');
  if (!hasItems && !['index', 'visitanos'].includes(page)) return;
  const BY_NAME = {
    'La Puerquita': ['Pulled pork y salsa Emmy. Potente.', '¡La burger del mes!'],
    'La Triplona': ['Tres carnes. Ven con hambre.'],
    'La Dori': ['Con Doritos. Sí, con Doritos.'],
    'La Cabrona': ['Queso de cabra, ¿te atreves?'],
    'Me Derrito': ['Mucho cheddar. MUCHO.'],
    'Doble Dosis': ['Doble de carne, doble de todo.'],
    'La Golosa': ['Burger y postre a la vez.'],
    'Dulce y Verde': ['Pistacho en una burger. Confía.'],
    'Gordi Deluxe': ['Con huevo frito. Siempre gana.'],
    'La Matru': ['Patatas paja y trufa. Un vicio.'],
    'Salmón y mascarpone': ['Un clásico de las mañanas.'],
    'Pancakes de Ferrero': ['Ferrero para desayunar. Sin culpa.'],
    'Pancakes de Nutella': ['Con fresas, que son fruta.'],
    'Matcha goloso': ['Verde que te quiero verde.'],
    'Matcha de Mango': ['Matcha con mango. Atrévete.'],
    'Espresso': ['Para despertar.'],
    'Patatas trufadas': ['Huelen a trufa desde aquí.']
  };
  const BY_TAG = [['mes', ['¡La burger del mes! Pídela antes de que se acabe.']], ['nuevo', ['¡Novedad!']], ['picante', ['¡Esta pica!', 'Ojo, que pica. Ten agua cerca.']], ['trufa', ['Huele a trufa desde aquí.']],
    ['dulce', ['Para los golosos.', 'Uy, qué dulce pinta.']], ['pollo', ['Crujiente por fuera, jugoso por dentro.']], ['veg', ['Esta también es para ti.']]];
  const BY_CAT = { hamburguesas: ['¡Buena elección!', 'Esta tiene buena pinta.'], compartir: ['Para compartir. O no.'], bocadillos: ['Clásico y siempre acierta.'], hotdogs: ['Un hot dog con alma.'], postres: ['Siempre hay hueco para el postre.'], infantil: ['Para los peques.'], desayunos: ['Buenos días con ganas.', 'Así sí empieza el día.'] };
  const pick = a => a[Math.floor(Math.random() * a.length)];
  let last = '';
  const lineFor = it => {
    let pool = BY_NAME[it.n];
    if (!pool) for (const [t, p] of BY_TAG) if (it.t.includes(t)) { pool = p; break; }
    pool = pool || BY_CAT[it.cat] || ['¡Buena elección!'];
    let l = pick(pool); if (pool.length > 1 && l === last) l = pick(pool.filter(x => x !== last)); return l;
  };
  let muted = false; try { muted = localStorage.getItem('alma-mascota') === 'off'; } catch (e) {}
  const el = document.createElement('div'); el.className = 'mtalk' + (muted ? ' off' : '');
  el.innerHTML = `<div class="mtalk__b" id="mtalkB" role="status" aria-live="polite"><span id="mtalkT"></span><button type="button" class="mtalk__x" aria-label="Callar a la mascota">Callar</button></div>
    <button type="button" class="mtalk__m" aria-label="Mascota: activar o silenciar los comentarios" title="Mascota">${RIG}</button>`;
  document.body.appendChild(el);
  const rig = $('.rig', el), bub = $('#mtalkB', el), txt = $('#mtalkT', el);
  let hideT, cool = 0, firstT;
  const say = (msg, ms = 3400, force) => {
    if (muted && !force) return;
    if (document.documentElement.classList.contains('lock') || $('#cart.open')) return;
    const n = Date.now(); if (!force && n - cool < 3600) return; cool = n; last = msg;
    txt.textContent = msg; el.classList.add('on'); rig.classList.remove('rig--still');
    clearTimeout(hideT); hideT = setTimeout(() => { el.classList.remove('on'); rig.classList.add('rig--still'); }, ms);
  };
  const setMuted = m => { muted = m; el.classList.toggle('off', m); try { localStorage.setItem('alma-mascota', m ? 'off' : 'on'); } catch (e) {} if (m) { el.classList.remove('on'); rig.classList.add('rig--still'); } };
  el.addEventListener('click', e => {
    if (e.target.closest('.mtalk__x')) { setMuted(true); return; }
    if (e.target.closest('.mtalk__m')) { if (muted) { setMuted(false); say('¡Hola otra vez! Te voy contando.', 3200, true); } else say(pick(['¡Hola! Pasa el ratón o toca un plato.', 'Dime qué te apetece.', '¿Desayuno o hamburguesa?']), 3200, true); }
  });
  rig.classList.add('rig--still');
  const itOf = n => { const id = n.dataset.open; return id && byId(id); };
  // escritorio: al pasar por encima
  let ht;
  document.addEventListener('mouseover', e => { const c = e.target.closest('.item[data-open]'); if (!c || !matchMedia('(hover:hover)').matches) return; clearTimeout(ht); ht = setTimeout(() => { const it = itOf(c); if (it) say(lineFor(it)); }, 380); });
  document.addEventListener('mouseout', e => { if (e.target.closest('.item[data-open]')) clearTimeout(ht); });
  // móvil: al llegar a mitad de pantalla
  if (!matchMedia('(hover:hover)').matches && 'IntersectionObserver' in window) {
    const io2 = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { const it = itOf(en.target); if (it) say(lineFor(it)); } }), { rootMargin: '-42% 0px -42% 0px', threshold: 0 });
    const watch = () => $$('.item[data-open]').forEach(c => { if (!c._w) { c._w = 1; io2.observe(c); } });
    addEventListener('menu-render', watch); watch(); new MutationObserver(watch).observe(document.body, { childList: true, subtree: true });
  }
  // al añadir al pedido
  document.addEventListener('click', e => { if (e.target.closest('[data-add]')) setTimeout(() => say(pick(['¡Anotado!', '¡Marchando!', 'Buena elección.']), 2400), 150); });
  // saludo según la página y la hora
  const morning = document.documentElement.dataset.momento === 'desayuno';
  const hello = { index: morning ? '¡Buenos días! ¿Te apetece un desayuno?' : hr < 12 ? '¡Buenos días! ¿Desayuno o hamburguesa?' : hr < 20 ? '¡Hola! ¿Qué te apetece comer?' : '¡Buenas noches! Hoy toca burger.', carta: 'Toca un plato y te cuento algo.', desayunos: morning || hr < 12 ? 'Buenos días. Café, tostada… ¿qué te apetece?' : 'Los desayunos son hasta las 12:00, pero mira, mira.', visitanos: '¡Te esperamos en Kale Nagusia 42!' }[page];
  if (hello) firstT = setTimeout(() => say(hello, 4200), 2600);
})();

/* ---------- Reels de Instagram (se cargan al pulsar) ---------- */
(() => {
  const links = $$('[data-ig]'); if (!links.length) return;
  const rm = document.createElement('div'); rm.className = 'modal'; rm.id = 'reelModal';
  rm.innerHTML = `<div class="modal__box modal__box--reel" role="dialog" aria-modal="true" aria-label="Vídeo de Instagram"><button class="modal__x" type="button" aria-label="Cerrar">✕</button><div class="reelbox" id="reelBox"></div><p class="reelfoot"><a id="reelOpen" target="_blank" rel="noopener">Abrir en Instagram ↗</a></p></div>`;
  document.body.appendChild(rm);
  links.forEach(a => a.addEventListener('click', e => {
    e.preventDefault(); const p = a.dataset.ig;
    $('#reelBox').innerHTML = `<iframe src="https://www.instagram.com/${p}/embed/" title="Instagram" loading="lazy" allowfullscreen allow="encrypted-media; autoplay"></iframe>`;
    $('#reelOpen').href = a.href; rm.classList.add('on'); lock(true);
  }));
  rm.addEventListener('click', e => { if (e.target === rm || e.target.closest('.modal__x')) { $('#reelBox').innerHTML = ''; closeModals(); } });
})();

/* ---------- Test: ¿Qué burger eres? ---------- */
(() => {
  const Q = [
    { q: '¿Cuánta hambre tienes?', o: [['Un picoteo', { size: 1 }], ['La normal', { size: 2 }], ['Mucha', { size: 3 }], ['¡Bestial!', { size: 3, big: 1 }]] },
    { q: '¿Qué te tira más?', o: [['Lo clásico', { style: 'clasica' }], ['Queso fundido', { style: 'queso' }], ['Dulce y salado', { style: 'dulce' }], ['Algo diferente', { style: 'original' }]] },
    { q: '¿Y el picante?', o: [['Nada', { spice: 0 }], ['Un poquito', { spice: 1 }], ['Dale fuerte', { spice: 2 }]] },
    { q: '¿Carne o pollo?', o: [['Carne', { meat: 'carne' }], ['Pollo', { meat: 'pollo' }], ['Vegetariano', { meat: 'veg' }], ['Me da igual', { meat: 'any' }]] },
    { q: '¿Cómo vienes hoy?', o: [['Tranquilo, de siempre', { mood: 'clasica' }], ['Con ganas de fiesta', { mood: 'queso' }], ['Curioso', { mood: 'original' }], ['Goloso', { mood: 'dulce' }]] }
  ];
  const PR = {
    'La Básica': [1, 'clasica', 0, 'carne', 'Clásico de los de siempre. Sabes lo que te gusta.'],
    'Doble Dosis': [3, 'clasica', 0, 'carne', 'Quien tiene hambre no se corta. Doble de todo.'],
    'La Golosa': [2, 'dulce', 0, 'carne', 'Dulce y salado, sin remordimientos.'],
    'Dulce y Verde': [2, 'dulce', 0, 'carne', 'Curioso y con pistacho. Te gusta sorprender.'],
    'Gordi Deluxe': [2, 'clasica', 0, 'veg', 'Equilibrado y con huevo frito. Buen gusto.'],
    'Me Derrito': [2, 'queso', 0, 'carne', 'Del equipo del queso. Cuanto más, mejor.'],
    'La Matru': [2, 'original', 0, 'carne', 'Con un punto de trufa y elegancia.'],
    'La Cabrona': [3, 'original', 0, 'carne', 'Atrevido y con carácter. Aquí no se viene a hacer amigos.'],
    'La Dori': [3, 'queso', 0, 'carne', 'Divertido: nada de ser aburrido. Con Doritos, claro.'],
    'La Triplona': [3, 'queso', 0, 'carne', 'Vas a por todas. Triple y sin miedo.'],
    'Picantona': [2, 'original', 2, 'carne', 'Valiente. El picante no te asusta.'],
    'Chickenesa': [2, 'clasica', 0, 'pollo', 'Fresco y crujiente. Te gusta lo ligero con sabor.'],
    'La Diabla': [2, 'original', 2, 'pollo', 'Pícaro y con chispa. Un poco travieso.'],
    'Furia de Pollo': [3, 'queso', 0, 'pollo', 'Hambre con carácter y mucho crujiente.'],
    'La Picosita': [2, 'dulce', 1, 'pollo', 'Dulce y picante a la vez. No te decides y está bien.'],
    'La Puerquita': [3, 'original', 0, 'carne', 'La estrella del mes. Potente y cremosa.']
  };
  const burgers = () => MENU.hamburguesas.items.filter(i => PR[i.n]);
  let step = 0, ans = [];
  const m = document.createElement('div'); m.className = 'modal'; m.id = 'quizModal';
  m.innerHTML = `<div class="modal__box modal__box--wide quiz" role="dialog" aria-modal="true" aria-labelledby="qT"><button class="modal__x" type="button" aria-label="Cerrar">✕</button><div id="qBody"></div></div>`;
  document.body.appendChild(m);
  const body = $('#qBody', m);
  function score(it) {
    const [size, style, spice, meat] = PR[it.n]; let s = 0; const a = Object.assign({}, ...ans);
    s += 3 - Math.abs(size - (a.size || 2)); if (a.big && it.n === 'La Triplona') s += 3; if (a.big && it.n === 'Doble Dosis') s += 1.5;
    if (a.style === style) s += 3; if (a.mood === style) s += 2;
    const w = a.spice ?? 0; if (w === 0) s += spice === 0 ? 2 : spice === 2 ? -3 : 0; else if (w === 1) s += spice === 1 ? 3 : spice === 2 ? 1 : 0; else s += spice === 2 ? 3 : spice === 1 ? 1 : -1;
    const mt = a.meat || 'any'; if (mt === 'carne') s += meat === 'carne' || meat === 'veg' ? 2 : -2; else if (mt === 'pollo') s += meat === 'pollo' ? 3 : -3; else if (mt === 'veg') s += meat === 'veg' ? 8 : -6;
    return s;
  }
  function ask() {
    const q = Q[step];
    body.innerHTML = `<div class="qprog"><i style="width:${(step / Q.length) * 100}%"></i></div><p class="qn">Pregunta ${step + 1} de ${Q.length}</p><h3 id="qT">${esc(q.q)}</h3>
      <div class="qopts">${q.o.map((o, k) => `<button type="button" class="qopt" data-k="${k}">${esc(o[0])}</button>`).join('')}</div>
      ${step ? '<button type="button" class="lnk qback">← Volver</button>' : ''}`;
  }
  function result() {
    const ranked = burgers().map(it => ({ it, s: score(it) + Math.random() * .01 })).sort((a, b) => b.s - a.s);
    const top = ranked[0].it, others = ranked.slice(1, 3).map(r => r.it); const veg = (Object.assign({}, ...ans).meat) === 'veg';
    const [, , , , line] = PR[top.n]; const agora = !!window.ALMA_AGORA;
    body.innerHTML = `<p class="qn">Tu resultado</p><div class="qres">
      ${top.i ? `<img src="img/dishes/s/${top.i}.jpg" alt="${esc(top.n)}">` : ''}
      <div><h3 id="qT">Eres <em>${esc(top.n)}</em></h3><p class="qline">${esc(line)}</p><p class="qdesc">${esc(top.d)}</p><p class="qprice">${eur(top.p)}${veg ? ' · con versión vegetariana' : ''}</p>
      <div class="btnrow" style="margin:12px 0 0">${agora ? `<a class="btn btn--solid" href="${esc(window.ALMA_AGORA)}" target="_blank" rel="noopener">Pedir online ↗</a>` : `<button type="button" class="btn btn--solid" data-qadd="${esc(top.id)}">Añadir al pedido</button>`}<button type="button" class="btn" data-qview="${esc(top.id)}">Ver la ficha</button></div></div></div>
      ${others.length ? `<p class="qn" style="margin-top:18px">También te pegan</p><div class="qchips">${others.map(o => `<button type="button" class="chip" data-qview="${esc(o.id)}">${esc(o.n)}</button>`).join('')}</div>` : ''}
      <div class="btnrow" style="margin-top:16px"><a class="btn btn--sm" id="qShare" target="_blank" rel="noopener">Compartir mi resultado</a><button type="button" class="btn btn--sm btn--ghost" data-qrestart>Repetir el test</button></div>`;
    const base = new URL('carta.html', location.href).href.split('#')[0] + '#test';
    $('#qShare', m).href = 'https://wa.me/?text=' + encodeURIComponent(`¡Soy ${top.n}! ${line}\n¿Y tú, qué burger eres? Haz el test de Alma Burger: ${base}`);
    m._top = top; m._veg = veg;
  }
  const open = () => { step = 0; ans = []; ask(); m.classList.add('on'); lock(true); };
  document.addEventListener('click', e => { if (e.target.closest('[data-quiz]')) { e.preventDefault(); open(); } });
  if (location.hash === '#test' && $('[data-quiz]')) setTimeout(open, 500);
  m.addEventListener('click', e => {
    if (e.target === m || e.target.closest('.modal__x')) { closeModals(); return; }
    const o = e.target.closest('.qopt'); if (o) { ans[step] = Q[step].o[+o.dataset.k][1]; step++; step < Q.length ? ask() : result(); return; }
    if (e.target.closest('.qback')) { step--; ans.length = step; ask(); return; }
    if (e.target.closest('[data-qrestart]')) { open(); return; }
    const ad = e.target.closest('[data-qadd]'); if (ad) { const it = byId(ad.dataset.qadd); closeModals(); if (m._veg && it.o) { push(it.id, 'Versión vegetariana'); toast(`<b>${esc(it.n)}</b> (versión vegetariana) añadido ✓`); } else addItem(it.id); return; }
    const vw = e.target.closest('[data-qview]'); if (vw) { closeModals(); setTimeout(() => openDish(vw.dataset.qview), 60); }
  });
})();

/* ---------- Vídeo propio en el móvil: se reproduce al verlo ---------- */
(() => {
  const figs = $$('.phone--own'); if (!figs.length) return;
  const reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
  figs.forEach(fig => {
    const v = $('video', fig); let userPaused = false;
    const play = () => { if (userPaused) return; v.preload = 'auto'; const p = v.play(); if (p && p.catch) p.catch(() => {}); };
    const sync = () => fig.classList.toggle('paused', v.paused);
    v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
    if ('IntersectionObserver' in window) new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting && !reduce) play(); else v.pause(); }), { threshold: .45 }).observe(fig);
    $('.phone__screen', fig).addEventListener('click', e => { if (v.paused) { userPaused = false; v.preload = 'auto'; v.play().catch(() => {}); } else { userPaused = true; v.pause(); } });
  });
})();
})();

/* ---------- De 8:00 a 12:00 la portada pone delante los desayunos ---------- */
(() => {
  if (document.documentElement.dataset.momento !== 'desayuno') return;
  const q = s => document.querySelector(s);
  const a = q('.hero__photo:not(.hero__photo--b)'), b = q('.hero__photo--b');
  if (a && b) {
    const ia = a.querySelector('img'), ib = b.querySelector('img'), ta = a.querySelector('a'), tb = b.querySelector('a');
    [ia.src, ib.src] = [ib.src, ia.src]; [ia.alt, ib.alt] = [ib.alt, ia.alt];
    [ta.textContent, tb.textContent] = [tb.textContent, ta.textContent]; [ta.href, tb.href] = [tb.href, ta.href];
  }
  const fb = q('#featuredB'), fa = q('#featured');
  if (fa && fb) fa.closest('section').before(fb.closest('section'));
})();

/* ---------- «Pedir online»: la burger saluda y se abre la página de pedidos ---------- */
(() => {
  const target = window.ALMA_AGORA; if (!target) return;
  let url; try { url = new URL(target, location.href).href; } catch (e) { return; }
  const reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
  const ov = document.createElement('div'); ov.className = 'goorder'; ov.setAttribute('role', 'status'); ov.setAttribute('aria-live', 'polite');
  ov.innerHTML = '<div class="goorder__in"><div class="goorder__rig" aria-hidden="true"><div class="rig" style="--w:150px"><div class="bob"><img class="legL" src="img/mascot-legL.png" alt=""><img class="legR" src="img/mascot-legR.png" alt=""><img class="body" src="img/mascot-body.png" alt=""></div></div></div><p class="goorder__t">¡Marchando!</p><p class="goorder__s">Abriendo la página de pedidos…</p></div>';
  document.body.appendChild(ov);
  let busy = false;
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href]');
    if (!a || a.href !== url || busy || e.ctrlKey || e.metaKey || e.shiftKey || e.button) return;
    if (reduce) return;                       // sin animaciones: se abre directamente
    e.preventDefault(); busy = true; ov.classList.add('on');
    setTimeout(() => {
      const w = window.open(url, '_blank', 'noopener');
      if (!w) location.href = url;            // si el navegador bloquea la pestaña nueva, vamos en esta
      setTimeout(() => { ov.classList.remove('on'); busy = false; }, 400);
    }, 850);
  });
})();

/* ---------- Aviso de cookies: solo pide permiso para el contenido externo (mapa) ---------- */
(() => {
  const KEY = 'alma-consent', MAX = 365 * 864e5;
  const $$ = s => Array.from(document.querySelectorAll(s));
  let c = null; try { c = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) {}
  if (c && !(Date.now() - c.t < MAX)) c = null;
  const loadExt = () => $$('[data-ext-src]').forEach(el => {
    if (el.querySelector('iframe')) return;
    const f = document.createElement('iframe'); f.src = el.dataset.extSrc; f.title = el.dataset.extTitle || ''; f.loading = 'lazy'; f.referrerPolicy = 'no-referrer';
    const ph = el.querySelector('.extph'); if (ph) ph.remove(); el.appendChild(f);
  });
  const bar = document.createElement('div'); bar.className = 'ckbar'; bar.setAttribute('role', 'dialog'); bar.setAttribute('aria-label', 'Aviso de cookies');
  bar.innerHTML = '<div class="ckbar__in"><p><b>Cookies, las justas.</b> No usamos cookies de publicidad ni de análisis. Solo guardamos en tu navegador lo necesario (tu pedido, el color elegido). Si aceptas, también cargamos el mapa de OpenStreetMap. <a href="cookies.html">Más información sobre cookies</a></p>'
    + '<div class="ckbar__b"><button type="button" class="btn btn--sm" data-ck="0">Rechazar</button><button type="button" class="btn btn--sm" data-ck="1">Aceptar</button></div></div>';
  document.body.appendChild(bar);
  const show = () => { bar.classList.add('on'); const b = bar.querySelector('[data-ck="1"]'); setTimeout(() => b && b.focus({ preventScroll: true }), 50); };
  const save = ext => {
    const before = c && c.ext; c = { ext, t: Date.now(), v: 1 };
    try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {}
    bar.classList.remove('on');
    if (ext) loadExt(); else if (before) location.reload();   // al retirar el permiso se quita el mapa
  };
  bar.addEventListener('click', e => { const b = e.target.closest('[data-ck]'); if (b) save(b.dataset.ck === '1'); });
  document.addEventListener('click', e => {
    if (e.target.closest('[data-cookies]')) { e.preventDefault(); show(); }
    if (e.target.closest('[data-ext-load]')) loadExt();        // cargar solo esta vez, sin guardar nada
  });
  if (!c) setTimeout(show, 900); else if (c.ext) loadExt();
})();
