/* ==========================================================================
   M&G Consulting — fondo animado: sala de monitorización (NOC)
   Videowall con gráficas en vivo y puestos de operador en silueta,
   con el mismo estilo que el skyline de la portada. Canvas, sin imágenes.
   Uso: <canvas data-noc>
   ========================================================================== */
(() => {
  'use strict';
  const cv = document.querySelector('canvas[data-noc]');
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const C = { bg: '#0B1526', wall: '#0E1A2D', screen: '#101F36', bezel: '#07101E', orange: '#F98A47', amber: '#FEAF3F', sun: '#FFC35F', ok: '#3DD68C', desk: '#060D18', line: 'rgba(255,255,255,.06)' };
  const rnd = (s => () => ((s = (s * 16807) % 2147483647) - 1) / 2147483646)(7331);

  const COLS = 6, ROWS = 3;
  // Tipo de contenido de cada pantalla del videowall
  const TYPES = ['line', 'status', 'bars', 'gauge', 'line', 'log', 'bars', 'line', 'map', 'map', 'status', 'gauge', 'log', 'gauge', 'line', 'bars', 'status', 'line'];
  const screens = TYPES.map((type, i) => ({ type, seed: rnd() * 100, speed: .4 + rnd() * .8, warn: Math.floor(rnd() * 24), hue: [C.orange, C.amber, C.sun][i % 3] }));

  let W = 0, H = 0, wall = null, raf = 0, visible = true, frame = 0;

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const r = cv.getBoundingClientRect();
    W = r.width; H = r.height;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const ww = Math.min(W * .94, 1500), wh = Math.min(H * .5, ww * .36);
    wall = { x: (W - ww) / 2, y: H * .06, w: ww, h: wh, gap: Math.max(4, ww * .006) };
  }

  /* ---------- Contenido de cada pantalla ---------- */
  function drawScreen(s, x, y, w, h, t) {
    ctx.fillStyle = C.screen; ctx.fillRect(x, y, w, h);
    const pad = Math.max(6, w * .07);
    const ix = x + pad, iy = y + pad * 1.6, iw = w - pad * 2, ih = h - pad * 2.4;
    // barra de título
    ctx.fillStyle = 'rgba(255,255,255,.25)'; ctx.fillRect(ix, y + pad * .6, iw * .35, Math.max(2, h * .035));
    ctx.fillStyle = s.hue; ctx.beginPath(); ctx.arc(x + w - pad, y + pad * .7, Math.max(2, h * .025), 0, 6.28); ctx.fill();

    switch (s.type) {
      case 'line': {
        ctx.strokeStyle = C.line; ctx.lineWidth = 1;
        for (let k = 1; k < 4; k++) { const gy = iy + ih * k / 4; ctx.beginPath(); ctx.moveTo(ix, gy); ctx.lineTo(ix + iw, gy); ctx.stroke(); }
        const n = 28, pts = [];
        for (let k = 0; k <= n; k++) {
          const v = .5 + .22 * Math.sin((k + t * s.speed * 6) * .45 + s.seed) + .14 * Math.sin((k + t * s.speed * 4) * 1.3 + s.seed * 2);
          pts.push([ix + iw * k / n, iy + ih * (1 - v)]);
        }
        ctx.beginPath(); pts.forEach(([px, py], k) => (k ? ctx.lineTo(px, py) : ctx.moveTo(px, py)));
        ctx.lineTo(ix + iw, iy + ih); ctx.lineTo(ix, iy + ih); ctx.closePath();
        ctx.fillStyle = s.hue + '22'; ctx.fill();
        ctx.beginPath(); pts.forEach(([px, py], k) => (k ? ctx.lineTo(px, py) : ctx.moveTo(px, py)));
        ctx.strokeStyle = s.hue; ctx.lineWidth = Math.max(1.2, w * .008); ctx.stroke();
        break;
      }
      case 'bars': {
        const n = 9, bw = iw / n * .62;
        for (let k = 0; k < n; k++) {
          const v = .25 + .6 * (.5 + .5 * Math.sin(t * s.speed * 1.4 + k * .9 + s.seed));
          ctx.fillStyle = k % 3 === 0 ? C.orange : k % 3 === 1 ? C.amber : C.sun;
          ctx.globalAlpha = .85;
          ctx.fillRect(ix + k * iw / n, iy + ih * (1 - v), bw, ih * v);
        }
        ctx.globalAlpha = 1;
        break;
      }
      case 'status': {
        const cols = 6, rows = 4, r = Math.min(iw / cols, ih / rows) * .22;
        for (let k = 0; k < cols * rows; k++) {
          const cx = ix + (k % cols + .5) * iw / cols, cy = iy + (Math.floor(k / cols) + .5) * ih / rows;
          const warn = k === s.warn;
          const on = warn ? (reduce || Math.sin(t * 4) > 0) : true;
          ctx.fillStyle = warn ? C.sun : C.ok;
          ctx.globalAlpha = on ? .9 : .25;
          ctx.beginPath(); ctx.arc(cx, cy, r, 0, 6.28); ctx.fill();
        }
        ctx.globalAlpha = 1;
        break;
      }
      case 'gauge': {
        const cx = x + w / 2, cy = iy + ih * .78, r = Math.min(iw * .42, ih * .7);
        const v = .55 + .3 * Math.sin(t * s.speed * .8 + s.seed);
        ctx.lineCap = 'round'; ctx.lineWidth = Math.max(3, r * .18);
        ctx.strokeStyle = 'rgba(255,255,255,.08)'; ctx.beginPath(); ctx.arc(cx, cy, r, Math.PI, 2 * Math.PI); ctx.stroke();
        ctx.strokeStyle = v > .8 ? C.sun : s.hue; ctx.beginPath(); ctx.arc(cx, cy, r, Math.PI, Math.PI + Math.PI * v); ctx.stroke();
        ctx.lineCap = 'butt';
        break;
      }
      case 'log': {
        const rows = 7, rh = ih / rows, off = reduce ? 0 : (t * s.speed * 1.5) % 1;
        for (let k = 0; k < rows + 1; k++) {
          const yy = iy + (k - off) * rh;
          if (yy < iy - 1 || yy > iy + ih - rh * .4) continue;
          const len = .3 + .6 * Math.abs(Math.sin(k * 7.3 + Math.floor(t * s.speed * 1.5) * 3.1 + s.seed));
          ctx.fillStyle = (k + Math.floor(t * s.speed * 1.5)) % 5 === 0 ? C.sun : 'rgba(255,255,255,.22)';
          ctx.fillRect(ix, yy, iw * len, Math.max(1.5, rh * .32));
        }
        break;
      }
      case 'map': {
        // Mini skyline de Barcelona con nodos conectados
        const base = iy + ih;
        ctx.fillStyle = 'rgba(255,255,255,.08)';
        const blocks = [[.05, .25], [.12, .4], [.2, .3], [.28, .55], [.36, .35], [.46, .75], [.55, .4], [.62, .3], [.7, .6], [.78, .58], [.86, .35], [.93, .28]];
        blocks.forEach(([px, ph]) => ctx.fillRect(ix + iw * px, base - ih * ph, iw * .06, ih * ph));
        const nodes = blocks.filter((_, k) => k % 2).map(([px, ph]) => [ix + iw * (px + .03), base - ih * ph]);
        ctx.strokeStyle = s.hue + '88'; ctx.lineWidth = 1;
        ctx.beginPath(); nodes.forEach(([nx, ny], k) => (k ? ctx.lineTo(nx, ny) : ctx.moveTo(nx, ny))); ctx.stroke();
        nodes.forEach(([nx, ny], k) => {
          const p = reduce ? .6 : .5 + .5 * Math.sin(t * 2 + k);
          ctx.fillStyle = C.sun; ctx.globalAlpha = .5 + p * .5;
          ctx.beginPath(); ctx.arc(nx, ny, Math.max(1.5, w * .012), 0, 6.28); ctx.fill();
        });
        ctx.globalAlpha = 1;
        break;
      }
    }
  }

  /* ---------- Escena completa ---------- */
  function draw(time) {
    const t = time / 1000;
    ctx.clearRect(0, 0, W, H);
    // Sala
    const g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, C.bg); g.addColorStop(.62, C.wall); g.addColorStop(1, '#070E1A');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);

    // Resplandor del videowall
    const { x, y, w, h, gap } = wall;
    const glow = ctx.createRadialGradient(W / 2, y + h * .6, 0, W / 2, y + h * .6, w * .7);
    glow.addColorStop(0, 'rgba(249,138,71,.16)'); glow.addColorStop(1, 'rgba(249,138,71,0)');
    ctx.fillStyle = glow; ctx.fillRect(0, 0, W, H);

    // Marco y pantallas
    ctx.fillStyle = C.bezel; ctx.fillRect(x - gap * 2, y - gap * 2, w + gap * 4, h + gap * 4);
    const sw = (w - gap * (COLS - 1)) / COLS, sh = (h - gap * (ROWS - 1)) / ROWS;
    screens.forEach((s, i) => {
      const cx = i % COLS, cy = Math.floor(i / COLS);
      drawScreen(s, x + cx * (sw + gap), y + cy * (sh + gap), sw, sh, t);
    });

    // Reflejo en el suelo
    const fy = y + h + gap * 2;
    const refl = ctx.createLinearGradient(0, fy, 0, fy + H * .25);
    refl.addColorStop(0, 'rgba(254,175,63,.08)'); refl.addColorStop(1, 'rgba(254,175,63,0)');
    ctx.fillStyle = refl; ctx.fillRect(x, fy, w, H * .25);

    // Puestos de operador en silueta (dos filas, perspectiva simple)
    const rowsY = [H * .78, H * .93];
    rowsY.forEach((dy, r) => {
      const scale = r ? 1.25 : 1;
      const deskW = Math.min(W * .9, 1500) * (r ? 1.02 : .88), dx = (W - deskW) / 2;
      const n = Math.max(3, Math.round(deskW / (210 * scale)));
      // monitores sobre la mesa
      for (let k = 0; k < n; k++) {
        const mx = dx + deskW * (k + .5) / n;
        for (let m = -1; m <= 1; m += 2) {
          const mw = 46 * scale, mh = 30 * scale, px = mx + m * mw * .56 - mw / 2, py = dy - mh - 10 * scale;
          ctx.fillStyle = '#0F1D33'; ctx.fillRect(px, py, mw, mh);
          ctx.fillStyle = k % 2 ? 'rgba(249,138,71,.35)' : 'rgba(255,195,95,.3)';
          ctx.fillRect(px + 3, py + 3, mw - 6, mh - 6);
          ctx.fillStyle = C.desk; ctx.fillRect(px + mw / 2 - 2, py + mh, 4, 10 * scale);
        }
        // silla / operador
        ctx.fillStyle = '#050B15';
        const chw = 34 * scale, chh = 42 * scale;
        ctx.beginPath(); ctx.roundRect ? ctx.roundRect(mx - chw / 2, dy + 6 * scale, chw, chh, 10 * scale) : ctx.rect(mx - chw / 2, dy + 6 * scale, chw, chh); ctx.fill();
        ctx.beginPath(); ctx.arc(mx, dy + 2 * scale, 11 * scale, 0, 6.28); ctx.fill();
      }
      // mesa
      ctx.fillStyle = C.desk;
      ctx.fillRect(dx, dy - 4 * scale, deskW, 8 * scale);
      ctx.fillStyle = 'rgba(249,138,71,.25)'; ctx.fillRect(dx, dy - 4 * scale, deskW, 1);
    });
  }

  const loop = time => {
    frame++;
    if (visible && frame % 2 === 0) draw(time); // ~30 fps es suficiente para un fondo
    raf = reduce ? 0 : requestAnimationFrame(loop);
  };
  const start = () => { if (!raf && !reduce) raf = requestAnimationFrame(loop); };
  const stop = () => { cancelAnimationFrame(raf); raf = 0; };

  window.addEventListener('resize', () => { resize(); draw(performance.now()); }, { passive: true });
  resize(); draw(0);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(es => { visible = es[0].isIntersecting; visible ? start() : stop(); }).observe(cv);
  } else start();
  document.addEventListener('visibilitychange', () => (document.hidden ? stop() : visible && start()));
})();
