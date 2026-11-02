/* M&G Consulting — catálogo de productos y servicios */
(() => {
  'use strict';
  const root = document.querySelector('[data-catalog]');
  if (!root) return;
  const $ = s => root.querySelector(s);
  const PAGE = 12;
  const euro = new Intl.NumberFormat('es-ES', { style: 'currency', currency: 'EUR' });
  // Logo del fabricante en cada tarjeta (archivos de assets/img/fabricantes/)
  const LOGOS = { HPE: 'hpe', Synology: 'synology', QNAP: 'qnap', 'Aruba Networking': 'aruba',
    Ubiquiti: 'ubiquiti', Fortinet: 'fortinet', SonicWall: 'sonicwall' };
  const PERIOD = { mes: '/mes', 'año': '/año', 'único': '' };
  const state = { q: '', cat: 'Todas', brand: 'Todos', sort: 'destacados', shown: PAGE };
  let items = [], meta = {};
  let basket = [];
  try { basket = JSON.parse(localStorage.getItem('myg-solicitud') || '[]'); } catch { basket = []; }

  const norm = s => (s || '').toString().normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const el = (tag, cls, text) => { const n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; };

  /* ---------- Carga de datos ---------- */
  async function load() {
    if (window.__CATALOGO__) return window.__CATALOGO__;
    for (const url of [root.dataset.api, root.dataset.fallback]) {
      try { const r = await fetch(url, { headers: { Accept: 'application/json' } }); if (r.ok) return await r.json(); } catch {}
    }
    throw new Error('sin datos');
  }

  /* ---------- Filtros ---------- */
  function buildFilters() {
    const cats = ['Todas', ...new Set(items.map(i => i.categoria).filter(Boolean).sort((a, b) => a.localeCompare(b, 'es')))];
    const chips = $('[data-cats]');
    chips.innerHTML = '';
    cats.forEach(c => {
      const b = el('button', 'chip', c);
      b.type = 'button';
      b.setAttribute('aria-pressed', String(c === state.cat));
      b.addEventListener('click', () => { state.cat = c; state.shown = PAGE; sync(); });
      chips.append(b);
    });
    const sel = $('[data-brand]');
    sel.innerHTML = '';
    ['Todos', ...new Set(items.map(i => i.fabricante).filter(Boolean).sort((a, b) => a.localeCompare(b, 'es')))]
      .forEach(b => { const o = el('option', null, b === 'Todos' ? 'Todos los fabricantes' : b); o.value = b; sel.append(o); });
  }

  function filtered() {
    const q = norm(state.q);
    let list = items.filter(i =>
      (state.cat === 'Todas' || i.categoria === state.cat) &&
      (state.brand === 'Todos' || i.fabricante === state.brand) &&
      (!q || norm(`${i.nombre} ${i.fabricante} ${i.categoria} ${i.descripcion}`).includes(q)));
    const price = i => (i.precio == null ? Infinity : i.precio);
    const sorts = {
      destacados: (a, b) => (b.destacado - a.destacado) || a.nombre.localeCompare(b.nombre, 'es'),
      'precio-asc': (a, b) => price(a) - price(b),
      'precio-desc': (a, b) => (b.precio ?? -1) - (a.precio ?? -1),
      nombre: (a, b) => a.nombre.localeCompare(b.nombre, 'es'),
    };
    return list.sort(sorts[state.sort]);
  }

  /* ---------- Render ---------- */
  function card(i) {
    const c = el('article', 'product' + (i.destacado ? ' is-featured' : ''));
    const top = el('div', 'product-top');
    const brand = el('span', 'product-brand');
    const logo = LOGOS[i.fabricante];
    if (logo) {
      const img = el('img'); img.src = root.dataset.base + 'assets/img/fabricantes/' + logo + '.png'; img.alt = i.fabricante; img.loading = 'lazy';
      brand.append(img);
    } else brand.textContent = i.fabricante || '';
    top.append(brand, el('span', 'product-cat', i.categoria || ''));
    c.append(top, el('h3', null, i.nombre));
    if (i.complemento) c.append(el('span', 'product-badge', 'Complemento · requiere licencia base'));
    if (i.descripcion) c.append(el('p', 'product-desc', i.descripcion));

    const foot = el('div', 'product-foot');
    const pr = el('div', 'product-price');
    if (i.precio != null) {
      const big = el('strong', null, euro.format(i.precio));
      const per = el('span', null, [i.unidad ? '/' + i.unidad : '', PERIOD[i.periodo] || ''].join('').replace('//', '/'));
      pr.append(big, per);
      const small = el('small', null, [i.compromiso ? 'Compromiso ' + i.compromiso.toLowerCase() : '', meta.iva_incluido ? 'IVA incluido' : 'IVA no incluido'].filter(Boolean).join(' · '));
      pr.append(small);
    } else if (i.precio_tipo === 'consumo') {
      pr.append(el('strong', 'ask', 'Según consumo'));
      pr.append(el('small', null, 'Pagas solo los recursos que utilizas'));
    } else {
      pr.append(el('strong', 'ask', 'Consultar precio'));
      pr.append(el('small', null, 'Te enviamos una propuesta ajustada'));
    }
    const inBasket = basket.some(b => b.id === i.id);
    const btn = el('button', 'btn btn-sm ' + (inBasket ? 'btn-dark' : 'btn-outline'), inBasket ? 'Añadido' : 'Añadir a la solicitud');
    btn.type = 'button';
    btn.addEventListener('click', () => toggle(i));
    foot.append(pr, btn);
    c.append(foot);
    return c;
  }

  function render() {
    const list = filtered();
    const grid = $('[data-grid]');
    grid.innerHTML = '';
    if (!list.length) {
      const empty = el('div', 'catalog-empty');
      empty.append(el('h3', null, 'No hay productos con estos filtros'), el('p', null, 'Prueba con otra búsqueda o pregúntanos directamente: trabajamos con más referencias de las que aparecen aquí.'));
      const reset = el('button', 'btn btn-dark btn-sm', 'Quitar filtros');
      reset.type = 'button';
      reset.addEventListener('click', () => { Object.assign(state, { q: '', cat: 'Todas', brand: 'Todos' }); $('[data-q]').value = ''; sync(); });
      empty.append(reset);
      grid.append(empty);
    } else {
      list.slice(0, state.shown).forEach(i => grid.append(card(i)));
    }
    $('[data-count]').textContent = `${list.length} ${list.length === 1 ? 'producto' : 'productos'}`;
    const more = $('[data-more]');
    more.hidden = state.shown >= list.length;
    more.textContent = `Ver más (${list.length - state.shown})`;
    root.querySelectorAll('[data-cats] .chip').forEach(b => b.setAttribute('aria-pressed', String(b.textContent === state.cat)));
    $('[data-brand]').value = state.brand;
    $('[data-sort]').value = state.sort;
  }

  function sync() {
    render();
    const p = new URLSearchParams();
    if (state.q) p.set('q', state.q);
    if (state.cat !== 'Todas') p.set('cat', state.cat);
    if (state.brand !== 'Todos') p.set('fab', state.brand);
    history.replaceState(null, '', location.pathname + (p.toString() ? '?' + p : ''));
  }

  /* ---------- Solicitud de presupuesto ---------- */
  const tray = document.querySelector('[data-tray]');
  function save() { try { localStorage.setItem('myg-solicitud', JSON.stringify(basket)); } catch {} }
  function toggle(i) {
    const k = basket.findIndex(b => b.id === i.id);
    k >= 0 ? basket.splice(k, 1) : basket.push({ id: i.id, nombre: i.nombre, cantidad: 1 });
    save(); render(); renderTray();
  }
  function renderTray() {
    const list = tray.querySelector('[data-tray-list]');
    tray.hidden = basket.length === 0;
    tray.querySelector('[data-tray-count]').textContent = basket.length;
    list.innerHTML = '';
    basket.forEach(b => {
      const li = el('li');
      li.append(el('span', null, b.nombre));
      const q = el('input'); q.type = 'number'; q.min = 1; q.value = b.cantidad; q.setAttribute('aria-label', 'Cantidad de ' + b.nombre);
      q.addEventListener('change', () => { b.cantidad = Math.max(1, parseInt(q.value, 10) || 1); save(); });
      const x = el('button', 'tray-remove', '×'); x.type = 'button'; x.setAttribute('aria-label', 'Quitar ' + b.nombre);
      x.addEventListener('click', () => { basket = basket.filter(o => o.id !== b.id); save(); render(); renderTray(); });
      li.append(q, x); list.append(li);
    });
  }
  tray.querySelector('[data-tray-toggle]').addEventListener('click', e => {
    const open = tray.classList.toggle('open');
    e.currentTarget.setAttribute('aria-expanded', String(open));
  });
  tray.querySelector('[data-tray-send]').addEventListener('click', () => {
    const texto = 'Me gustaría recibir un presupuesto de:\n' + basket.map(b => `- ${b.cantidad} × ${b.nombre}`).join('\n');
    try { sessionStorage.setItem('myg-mensaje', texto); } catch {}
    location.href = tray.dataset.contact;
  });

  /* ---------- Eventos ---------- */
  let t;
  $('[data-q]').addEventListener('input', e => { clearTimeout(t); t = setTimeout(() => { state.q = e.target.value.trim(); state.shown = PAGE; sync(); }, 180); });
  $('[data-brand]').addEventListener('change', e => { state.brand = e.target.value; state.shown = PAGE; sync(); });
  $('[data-sort]').addEventListener('change', e => { state.sort = e.target.value; sync(); });
  $('[data-more]').addEventListener('click', () => { state.shown += PAGE; render(); });

  /* ---------- Inicio ---------- */
  load().then(d => {
    meta = d; items = (d.productos || []).map(p => ({ ...p, destacado: !!p.destacado }));
    const p = new URLSearchParams(location.search);
    state.q = p.get('q') || ''; state.cat = p.get('cat') || 'Todas'; state.brand = p.get('fab') || 'Todos';
    $('[data-q]').value = state.q;
    buildFilters();
    $('[data-updated]').textContent = d.actualizado ? 'Actualizado: ' + d.actualizado : '';
    root.querySelector('[data-demo]').hidden = d.fuente !== 'ejemplo';
    root.classList.remove('is-loading');
    render(); renderTray();
  }).catch(() => {
    root.classList.remove('is-loading');
    $('[data-grid]').innerHTML = '';
    const e = el('div', 'catalog-empty');
    e.append(el('h3', null, 'No hemos podido cargar el catálogo'), el('p', null, 'Escríbenos a info@myg.consulting y te enviamos la información que necesites.'));
    $('[data-grid]').append(e);
  });
})();
