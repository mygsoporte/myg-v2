/* ==========================================================================
   M&G Consulting — escena animada: skylines de Barcelona y Madrid + red de datos
   Dibujado en <canvas>, sin imágenes externas. Alterna entre las dos ciudades
   con un fundido, se pausa fuera de pantalla y respeta el movimiento reducido.
   Uso: <canvas data-skyline [data-variant="page"] [data-network-only]>
   API:  window.MYGScene.setMode(0-3)
         evento "myg:city" en document → detail.name ("Barcelona" | "Madrid")
   ========================================================================== */
(() => {
  'use strict';
  const canvases = document.querySelectorAll('canvas[data-skyline]');
  if (!canvases.length) return;

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const C = {
    skyTop: '#0E192B', skyLow: '#1C2F4E', glow: '249,138,71',
    far: '#1B2D4A', hill: '#16263F', near: '#0A1220',
    orange: '#F98A47', amber: '#FEAF3F', sun: '#FFC35F', win: '255,195,95',
  };
  const W0 = 1600;          // ancho lógico del skyline
  const CITY_TIME = 14000;  // ms que se muestra cada ciudad
  const FADE_TIME = 2200;   // ms del fundido

  const rng = seed => () => ((seed = (seed * 16807) % 2147483647) - 1) / 2147483646;

  /* ---------------- Utilidades comunes ---------------- */
  function genericBlocks(r, reserved, start, minH, varH) {
    const near = [];
    for (let x = start; x < W0 + 20;) {
      const w = 16 + r() * 34;
      const inRes = reserved.some(([a, b]) => x + w > a && x < b);
      near.push({ x, w, h: inRes ? 14 + r() * 18 : minH + r() * varH });
      x += w + 1 + r() * 4;
    }
    return near;
  }
  function farBlocks(r) {
    const far = [];
    for (let x = -20; x < W0 + 20;) { const w = 18 + r() * 40; far.push({ x, w, h: 50 + r() * 110 }); x += w + 2 + r() * 6; }
    return far;
  }
  function windowsFor(r, blocks, density, out) {
    blocks.forEach(b => {
      for (let y = 10; y < b.h - 8; y += 9) for (let x = b.x + 4; x < b.x + b.w - 4; x += 7)
        if (r() < density) out.push({ x, y, ph: r() * Math.PI * 2, sp: .2 + r() * .8, base: r() });
    });
  }
  const curve = (a, b) => ({ a, b, c: { x: (a.x + b.x) / 2, y: Math.max(a.y, b.y) + 40 + Math.abs(a.x - b.x) * .12 } });
  const spire = (ctx, x, w, h, base) => {
    ctx.beginPath(); ctx.moveTo(x - w / 2, base + 2);
    ctx.lineTo(x - w * .38, -h * .78); ctx.quadraticCurveTo(x - w * .2, -h * .97, x, -h);
    ctx.quadraticCurveTo(x + w * .2, -h * .97, x + w * .38, -h * .78); ctx.lineTo(x + w / 2, base + 2); ctx.closePath(); ctx.fill();
  };

  /* ======================= BARCELONA ======================= */
  function buildBarcelona() {
    const r = rng(20251);
    const far = farBlocks(r);
    const near = genericBlocks(r, [[500, 625], [840, 925], [1150, 1265], [1430, 1510]], 300, 28, 62);
    for (let x = 180; x < 300; x += 22) near.push({ x, w: 20, h: 18 + r() * 20 });
    const towers = [{ x: 1161, w: 38, h: 232, antenna: 18 }, { x: 1222, w: 38, h: 226 }];
    const windows = [];
    windowsFor(r, near, .16, windows);
    windowsFor(r, towers.map(t => ({ x: t.x - t.w / 2, w: t.w, h: t.h })), .3, windows);
    const g = { x: 882, w: 66, h: 258 };
    const leds = [];
    for (let y = 8; y < g.h - 16; y += 8) {
      const half = y > g.h - 60 ? (g.w / 2) * Math.sqrt(Math.max(0, 1 - ((y - (g.h - 60)) / 60) ** 2)) : g.w / 2;
      for (let x = -half + 5; x < half - 4; x += 7) leds.push({ x: g.x + x, y });
    }
    const nodes = [{ x: 150, y: 128 }, { x: 563, y: 282 }, { x: 882, y: 258 }, { x: 1161, y: 250 }, { x: 1222, y: 226 },
      { x: 1478, y: 196 }, { x: 1330, y: 316 }, { x: 360, y: 90 }, { x: 720, y: 96 }, { x: 1040, y: 104 }];
    const links = [[0, 7], [7, 1], [1, 8], [8, 2], [2, 9], [9, 3], [3, 4], [4, 5], [2, 6], [6, 5], [1, 6], [0, 1], [2, 4]];
    return {
      name: 'Barcelona', glowX: 880, far, near, towers, windows, leds, nodes,
      curves: links.map(([i, j]) => curve(nodes[i], nodes[j])),
      beacons: [[1330, 300], [1161, 250]],
      back(ctx) { // Tibidabo y torre de Collserola
        ctx.beginPath(); ctx.moveTo(940, 0);
        ctx.bezierCurveTo(1060, -90, 1200, -175, 1330, -178);
        ctx.bezierCurveTo(1460, -176, 1560, -110, 1660, -60); ctx.lineTo(1660, 0); ctx.closePath(); ctx.fill();
        ctx.fillRect(1328.5, -300, 3, 124); ctx.fillRect(1318, -262, 24, 6);
      },
      front(ctx) {
        // Montjuïc
        ctx.beginPath(); ctx.moveTo(-60, 0); ctx.bezierCurveTo(-10, -40, 60, -118, 150, -118);
        ctx.lineTo(138, -118); ctx.lineTo(138, -128); ctx.lineTo(162, -128); ctx.lineTo(162, -118);
        ctx.bezierCurveTo(240, -112, 300, -40, 360, 0); ctx.closePath(); ctx.fill();
        // Sagrada Família
        ctx.fillRect(512, -64, 104, 64);
        [[522, 13, 176], [538, 14, 198], [590, 14, 196], [606, 13, 172], [548, 12, 150], [580, 12, 150]].forEach(s => spire(ctx, s[0], s[1], s[2], -64));
        spire(ctx, 563, 22, 282, -64); ctx.fillRect(561.5, -296, 3, 16); ctx.fillRect(557, -290, 12, 3);
        // Torre Glòries
        ctx.beginPath(); ctx.moveTo(g.x - g.w / 2, 0); ctx.lineTo(g.x - g.w / 2, -g.h + 60);
        ctx.bezierCurveTo(g.x - g.w / 2, -g.h + 16, g.x - g.w / 4, -g.h, g.x, -g.h);
        ctx.bezierCurveTo(g.x + g.w / 4, -g.h, g.x + g.w / 2, -g.h + 16, g.x + g.w / 2, -g.h + 60);
        ctx.lineTo(g.x + g.w / 2, 0); ctx.closePath(); ctx.fill();
        // Hotel W
        ctx.beginPath(); ctx.moveTo(1444, 0); ctx.lineTo(1444, -30);
        ctx.quadraticCurveTo(1454, -168, 1484, -196); ctx.quadraticCurveTo(1500, -150, 1506, -30); ctx.lineTo(1506, 0); ctx.closePath(); ctx.fill();
      },
      detail(ctx, X, Y) { // retícula del Hotel Arts
        ctx.strokeStyle = 'rgba(255,255,255,.07)'; ctx.lineWidth = 1;
        for (let y = 20; y < 226; y += 20) { ctx.beginPath(); ctx.moveTo(X(1203), Y(y)); ctx.lineTo(X(1241), Y(y + 20)); ctx.stroke(); }
      },
    };
  }

  /* ======================= MADRID ======================= */
  function buildMadrid() {
    const r = rng(28013);
    // Bloques lejanos más bajos para que destaquen los edificios singulares
    const far = farBlocks(r).map(b => ({ ...b, h: b.h * .7 }));
    const near = genericBlocks(r, [[280, 320], [345, 545], [555, 665], [672, 755], [760, 800], [805, 905], [868, 1055], [1055, 1168], [1170, 1460]], 120, 20, 40);
    for (let x = -10; x < 120; x += 22) near.push({ x, w: 20, h: 16 + r() * 22 });
    for (let i = near.length - 1; i >= 0; i--) if (near[i].x + near[i].w > 1052 && near[i].x < 1166) near.splice(i, 1);

    // Cuerpos con ventanas (Cuatro Torres, Caleido y Plaza de España)
    const towers = [
      { x: 1200, w: 48, h: 240 },  // Torre Cepsa
      { x: 1262, w: 42, h: 270 },  // Torre PwC
      { x: 1322, w: 42, h: 268 },  // Torre de Cristal
      { x: 1382, w: 42, h: 262 },  // Torre Emperador
      { x: 1436, w: 38, h: 198 },  // Torre Caleido
      { x: 589, w: 58, h: 130 },   // Edificio España
      { x: 644, w: 32, h: 175 },   // Torre de Madrid
    ];
    const windows = [];
    windowsFor(r, near, .16, windows);
    windowsFor(r, towers.map(t => ({ x: t.x - t.w / 2, w: t.w, h: t.h })), .34, windows);

    // Corona de vidrio iluminada de la Torre de Cristal
    const leds = [];
    for (let y = 270; y < 292; y += 5) for (let x = 1304; x < 1340; x += 6) leds.push({ x, y });

    const nodes = [
      { x: 300, y: 180 }, { x: 505, y: 142 }, { x: 644, y: 226 }, { x: 715, y: 160 }, { x: 780, y: 282 },
      { x: 855, y: 142 }, { x: 937, y: 172 }, { x: 987, y: 172 }, { x: 1110, y: 98 }, { x: 1200, y: 302 },
      { x: 1322, y: 294 }, { x: 1382, y: 284 }, { x: 1436, y: 210 },
    ];
    const links = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [2, 4], [4, 9], [7, 10]];

    // Ventanas iluminadas fijas de edificios clásicos (se dibujan en coordenadas lógicas)
    const rowWindows = (x0, x1, ys, step, w = 2.4, h = 4) => {
      const out = [];
      ys.forEach(y => { for (let x = x0; x <= x1; x += step) out.push([x, y, w, h]); });
      return out;
    };
    const classicLights = [
      ...rowWindows(356, 464, [10, 24, 36], 7),          // Palacio Real
      ...rowWindows(684, 746, [14, 30, 46, 62, 78], 6),  // Metrópolis
      ...rowWindows(816, 894, [12, 28, 44], 7),          // Palacio de Cibeles
      ...rowWindows(476, 534, [14, 30, 46], 8),          // Almudena
    ];
    // Ventanas de las torres KIO, siguiendo su inclinación
    const kioLights = [];
    for (let y = 10; y < 166; y += 10) for (let i = 0; i < 4; i++) {
      const off = y * Math.tan(15 * Math.PI / 180);
      kioLights.push([877 + i * 8 + off, y], [1017 + i * 8 - off, y]);
    }

    return {
      name: 'Madrid', glowX: 1100, scaleMul: .88, focus: .62, far, near, towers, windows, leds, nodes,
      curves: links.map(([i, j]) => curve(nodes[i], nodes[j])),
      beacons: [[780, 282], [1200, 302], [644, 226], [1322, 294]],
      back(ctx) { // Sierra de Guadarrama
        ctx.beginPath(); ctx.moveTo(-40, 0);
        [[-40, 60], [80, 96], [190, 78], [320, 118], [440, 92], [580, 128], [720, 100], [880, 140], [1020, 108], [1180, 132], [1340, 98], [1480, 120], [1660, 84]]
          .forEach(([x, h]) => ctx.lineTo(x, -h));
        ctx.lineTo(1660, 0); ctx.closePath(); ctx.fill();
      },
      front(ctx) {
        // ---- Faro de Moncloa: fuste fino y mirador
        ctx.fillRect(296, -150, 8, 150);
        ctx.fillRect(284, -164, 32, 14); ctx.fillRect(288, -168, 24, 4); ctx.fillRect(299, -184, 2, 16);

        // ---- Palacio Real: fachada larga, pabellones en las esquinas y balaustrada con estatuas
        ctx.fillRect(352, -46, 116, 46);
        ctx.fillRect(348, -54, 20, 54); ctx.fillRect(452, -54, 20, 54); ctx.fillRect(398, -56, 24, 56);
        for (let x = 372; x < 450; x += 8) ctx.fillRect(x, -51, 3, 5);
        ctx.beginPath(); ctx.moveTo(398, -56); ctx.lineTo(410, -64); ctx.lineTo(422, -56); ctx.closePath(); ctx.fill();

        // ---- Catedral de la Almudena: cúpula sobre tambor, linterna y dos torres
        ctx.fillRect(472, -64, 66, 64);
        ctx.fillRect(474, -100, 12, 36); ctx.fillRect(524, -100, 12, 36);
        ctx.beginPath(); ctx.arc(480, -100, 6, Math.PI, 0); ctx.arc(530, -100, 6, Math.PI, 0); ctx.fill();
        ctx.fillRect(490, -84, 30, 20);
        ctx.beginPath(); ctx.ellipse(505, -84, 18, 26, 0, Math.PI, 0); ctx.fill();
        ctx.fillRect(501, -118, 8, 10); ctx.fillRect(503.5, -142, 3, 24); ctx.fillRect(498, -134, 14, 3);

        // ---- Plaza de España: Edificio España (escalonado) y Torre de Madrid
        ctx.fillRect(560, -130, 58, 130);
        ctx.fillRect(566, -150, 46, 20); ctx.fillRect(574, -164, 30, 14); ctx.fillRect(582, -176, 14, 12); ctx.fillRect(588, -190, 2, 14);
        ctx.fillRect(628, -175, 32, 175);
        ctx.fillRect(633, -196, 22, 21); ctx.fillRect(638, -212, 12, 16); ctx.fillRect(643, -228, 2, 16);

        // ---- Edificio Metrópolis: cuerpo, rotonda con columnas, cúpula y la Victoria alada
        ctx.fillRect(680, -94, 70, 94);
        ctx.fillRect(700, -126, 30, 32);
        ctx.beginPath(); ctx.ellipse(715, -126, 17, 22, 0, Math.PI, 0); ctx.fill();
        ctx.fillRect(713, -152, 4, 6);
        ctx.beginPath(); // alas de la estatua
        ctx.moveTo(715, -150); ctx.lineTo(702, -162); ctx.lineTo(709, -152); ctx.closePath();
        ctx.moveTo(715, -150); ctx.lineTo(728, -162); ctx.lineTo(721, -152); ctx.closePath(); ctx.fill();
        ctx.fillRect(713.5, -160, 3, 10);

        // ---- Torrespaña («el Pirulí»): fuste que se estrecha, cabeza escalonada y antena
        ctx.beginPath(); ctx.moveTo(772, 0); ctx.lineTo(788, 0); ctx.lineTo(785, -190); ctx.lineTo(775, -190); ctx.closePath(); ctx.fill();
        ctx.fillRect(760, -198, 40, 8); ctx.fillRect(766, -224, 28, 26); ctx.fillRect(762, -230, 36, 6); ctx.fillRect(771, -240, 18, 10);
        ctx.fillRect(778, -282, 4, 42);

        // ---- Palacio de Cibeles: cuerpo, torreones y torre central apuntada
        ctx.fillRect(810, -60, 90, 60);
        [[810, 12], [888, 12]].forEach(([x, w]) => {
          ctx.fillRect(x, -78, w, 18);
          ctx.beginPath(); ctx.moveTo(x, -78); ctx.lineTo(x + w / 2, -92); ctx.lineTo(x + w, -78); ctx.closePath(); ctx.fill();
        });
        ctx.fillRect(845, -122, 20, 62);
        ctx.beginPath(); ctx.moveTo(843, -122); ctx.lineTo(855, -142); ctx.lineTo(867, -122); ctx.closePath(); ctx.fill();
        ctx.fillRect(838, -100, 5, 40); ctx.fillRect(867, -100, 5, 40);
        ctx.beginPath(); ctx.moveTo(837, -100); ctx.lineTo(840.5, -110); ctx.lineTo(844, -100); ctx.moveTo(866, -100); ctx.lineTo(869.5, -110); ctx.lineTo(873, -100); ctx.fill();

        // ---- Torres KIO (Puerta de Europa): 15° de inclinación, una hacia la otra
        const lean = 170 * Math.tan(15 * Math.PI / 180);
        ctx.beginPath(); ctx.moveTo(875, 0); ctx.lineTo(909, 0); ctx.lineTo(909 + lean, -170); ctx.lineTo(875 + lean, -170); ctx.closePath(); ctx.fill();
        ctx.beginPath(); ctx.moveTo(1015, 0); ctx.lineTo(1049, 0); ctx.lineTo(1049 - lean, -170); ctx.lineTo(1015 - lean, -170); ctx.closePath(); ctx.fill();

        // ---- Puerta de Alcalá: cinco vanos, cornisa y ático con escudo y esculturas
        ctx.save(); ctx.translate(1058 - 602 * 1.2, 0); ctx.scale(1.2, 1.2);
        ctx.beginPath();
        ctx.rect(602, -52, 86, 52); ctx.rect(599, -57, 92, 5); ctx.rect(626, -70, 38, 13);
        ctx.moveTo(637, -70); ctx.lineTo(653, -70); ctx.lineTo(650, -78); ctx.lineTo(640, -78); ctx.closePath();
        [633, 645, 657].forEach(cx => { ctx.moveTo(cx - 5, 0); ctx.lineTo(cx - 5, -24); ctx.arc(cx, -24, 5, Math.PI, 0); ctx.lineTo(cx + 5, 0); ctx.closePath(); });
        ctx.rect(608, -22, 8, 22); ctx.rect(674, -22, 8, 22);
        ctx.fill('evenodd');
        ctx.beginPath(); ctx.ellipse(632, -73, 3.5, 5, 0, 0, Math.PI * 2); ctx.ellipse(658, -73, 3.5, 5, 0, 0, Math.PI * 2); ctx.fill();
        ctx.restore();

        // ---- Torre Cepsa: dos pilares unidos por arriba con el gran hueco (se ve el cielo)
        ctx.beginPath();
        ctx.rect(1176, -302, 48, 302);
        ctx.rect(1189, -290, 22, 50);   // hueco
        ctx.fill('evenodd');
        // ---- Torre PwC: cima curva
        ctx.beginPath(); ctx.moveTo(1241, 0); ctx.lineTo(1241, -270); ctx.quadraticCurveTo(1262, -290, 1283, -270); ctx.lineTo(1283, 0); ctx.closePath(); ctx.fill();
        // ---- Torre de Cristal: corona de vidrio
        ctx.beginPath(); ctx.moveTo(1301, -268); ctx.lineTo(1303, -294); ctx.lineTo(1341, -294); ctx.lineTo(1343, -268); ctx.closePath(); ctx.fill();
        // ---- Torre Emperador: coronación con marco
        ctx.beginPath(); ctx.rect(1361, -286, 42, 24); ctx.rect(1367, -280, 30, 18); ctx.fill('evenodd');
        // ---- Torre Caleido: marco abierto en lo alto
        ctx.beginPath(); ctx.rect(1417, -212, 38, 14); ctx.rect(1422, -208, 28, 10); ctx.fill('evenodd');
      },
      lights(ctx, t) {
        ctx.fillStyle = 'rgba(255,195,95,.55)';
        classicLights.forEach(([x, y, w, h], i) => { if ((i * 7) % 5) ctx.fillRect(x, -y - h, w, h); });
        ctx.fillStyle = 'rgba(255,195,95,.6)';
        kioLights.forEach(([x, y], i) => { if ((i * 11) % 4) ctx.fillRect(x, -y - 3, 3, 3); });
        // Línea de luz en la coronación de las Cuatro Torres
        ctx.fillStyle = 'rgba(249,138,71,.75)';
        ctx.fillRect(1176, -302, 48, 2); ctx.fillRect(1361, -286, 42, 2); ctx.fillRect(1417, -212, 38, 2);
      },
      detail(ctx, X, Y) {
        // Fachada iluminada de la Puerta de Alcalá y de Cibeles
        [[1052, 1166, 76], [806, 904, 70]].forEach(([x0, x1, h]) => {
          const gl = ctx.createLinearGradient(0, Y(0), 0, Y(h));
          gl.addColorStop(0, 'rgba(255,195,95,.30)'); gl.addColorStop(1, 'rgba(255,195,95,0)');
          ctx.fillStyle = gl; ctx.fillRect(X(x0), Y(h), X(x1) - X(x0), Y(0) - Y(h));
        });
        ctx.strokeStyle = 'rgba(255,195,95,.5)'; ctx.lineWidth = Math.max(1, (X(1) - X(0)) * 1.3);
        ctx.beginPath(); ctx.moveTo(X(1055), Y(68)); ctx.lineTo(X(1165), Y(68)); ctx.stroke();
        // Líneas verticales de la Torre PwC
        ctx.strokeStyle = 'rgba(255,255,255,.06)'; ctx.lineWidth = 1;
        for (let x = 1248; x < 1280; x += 8) { ctx.beginPath(); ctx.moveTo(X(x), Y(4)); ctx.lineTo(X(x), Y(266)); ctx.stroke(); }
      },
    };
  }

  const CITIES = [buildBarcelona(), buildMadrid()];

  /* ---------------- Escenas (una por canvas) ---------------- */
  const scenes = [];
  canvases.forEach(cv => {
    const s = { cv, ctx: cv.getContext('2d'), page: cv.dataset.variant === 'page', networkOnly: cv.hasAttribute('data-network-only'),
      W: 0, H: 0, sc: 1, ox: 0, visible: true, mode: 0, cityI: 0, netI: .6, packets: CITIES.map(c => []) };
    CITIES.forEach((c, k) => { for (let i = 0; i < 22; i++) s.packets[k].push(newPacket(c, true)); });
    scenes.push(s);
  });

  function newPacket(city, randomT) {
    const r = Math.random;
    return { l: Math.floor(r() * city.curves.length), t: randomT ? r() : 0, v: .0016 + r() * .0026, dir: r() < .5 ? 1 : -1, c: [C.orange, C.amber, C.sun][Math.floor(r() * 3)] };
  }

  function resize(s) {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = s.cv.getBoundingClientRect();
    s.W = rect.width; s.H = rect.height;
    s.cv.width = Math.round(s.W * dpr); s.cv.height = Math.round(s.H * dpr);
    s.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const targetH = s.page ? s.H * .6 : s.H * (s.W < 700 ? .34 : .42);
    s.sc = Math.max(s.W / W0, targetH / 300);
    s.ox = Math.min(0, (s.W - W0 * s.sc) * (s.page ? .75 : .56));
  }

  const pt = (cu, t) => { const u = 1 - t; return { x: u * u * cu.a.x + 2 * u * t * cu.c.x + t * t * cu.b.x, y: u * u * cu.a.y + 2 * u * t * cu.c.y + t * t * cu.b.y }; };

  /* ---------------- Alternancia de ciudades ---------------- */
  const cityState = { cur: 0, next: 1, fade: 0, since: 0 };
  // ?ciudad=madrid empieza por Madrid (útil para revisar el diseño)
  if (/[?&]ciudad=madrid/i.test(location.search)) { cityState.cur = 1; cityState.next = 0; }
  function announce(name) { document.dispatchEvent(new CustomEvent('myg:city', { detail: { name } })); }

  /* ---------------- Dibujo de una ciudad ---------------- */
  function drawCity(s, city, alpha, t, packets) {
    if (alpha <= 0.002) return;
    const { ctx, H, W } = s;
    // Cada ciudad puede ajustar su escala y su encuadre para que se vean sus edificios principales
    const sc = s.sc * (city.scaleMul || 1);
    const ox = Math.min(0, (W - W0 * sc) * (s.page ? .75 : (city.focus ?? .56)));
    const X = x => ox + x * sc, Y = y => H - y * sc;
    ctx.save(); ctx.globalAlpha = alpha;

    if (!s.networkOnly) {
      ctx.save(); ctx.translate(ox, H); ctx.scale(sc, sc);
      ctx.fillStyle = C.hill; city.back(ctx);
      ctx.fillStyle = C.far; city.far.forEach(b => ctx.fillRect(b.x, -b.h, b.w, b.h));
      ctx.fillStyle = C.near;
      city.near.forEach(b => ctx.fillRect(b.x, -b.h, b.w, b.h));
      city.towers.forEach(b => { ctx.fillRect(b.x - b.w / 2, -b.h, b.w, b.h); if (b.antenna) ctx.fillRect(b.x - 1, -b.h - b.antenna, 2, b.antenna); });
      city.front(ctx);
      if (city.lights) city.lights(ctx, t);
      ctx.restore();
      city.detail(ctx, X, Y);

      const lit = .45 + s.cityI * .35;
      city.windows.forEach(w => {
        const k = reduce ? w.base : (w.base + .5 * Math.sin(t * w.sp + w.ph));
        if (k < 1 - lit) return;
        ctx.fillStyle = `rgba(${C.win},${Math.min(.85, (k - (1 - lit)) * 1.6) * alpha})`;
        ctx.fillRect(X(w.x), Y(w.y), Math.max(1, 2.4 * sc), Math.max(1, 3 * sc));
      });
      city.leds.forEach(l => {
        const wave = reduce ? .6 : .5 + .5 * Math.sin(t * 1.3 - l.y * .045 + Math.sin(l.x * .08) * .8);
        ctx.globalAlpha = alpha * (.25 + wave * .6);
        ctx.fillStyle = wave > .66 ? C.sun : wave > .33 ? C.amber : C.orange;
        ctx.fillRect(X(l.x) - 1, Y(l.y), Math.max(1.2, 3 * sc), Math.max(1.2, 3 * sc));
      });
      ctx.globalAlpha = alpha;
      const blink = reduce ? 1 : (Math.sin(t * 2.4) > .2 ? 1 : .2);
      ctx.fillStyle = `rgba(255,90,70,${blink})`;
      city.beacons.forEach(([x, y]) => { ctx.beginPath(); ctx.arc(X(x), Y(y), Math.max(1.5, 2.6 * sc), 0, 6.28); ctx.fill(); });
    }

    // Red de datos
    const ni = s.netI;
    ctx.lineWidth = 1; ctx.setLineDash([3, 5]);
    city.curves.forEach(cu => {
      ctx.strokeStyle = `rgba(${C.glow},${.08 + ni * .22})`;
      ctx.beginPath(); ctx.moveTo(X(cu.a.x), Y(cu.a.y)); ctx.quadraticCurveTo(X(cu.c.x), Y(cu.c.y), X(cu.b.x), Y(cu.b.y)); ctx.stroke();
    });
    ctx.setLineDash([]);
    city.nodes.forEach((n, i) => {
      const pulse = reduce ? .5 : .5 + .5 * Math.sin(t * 2 + i);
      ctx.fillStyle = `rgba(${C.glow},${.12 * ni * pulse})`;
      ctx.beginPath(); ctx.arc(X(n.x), Y(n.y), 10 * sc + 4 * pulse, 0, 6.28); ctx.fill();
      ctx.fillStyle = C.sun; ctx.beginPath(); ctx.arc(X(n.x), Y(n.y), Math.max(1.6, 3.2 * sc), 0, 6.28); ctx.fill();
    });
    const active = Math.round(6 + ni * 16);
    packets.forEach((pk, i) => {
      if (i >= active) return;
      if (!reduce) pk.t += pk.v * (1 + ni);
      if (pk.t > 1) Object.assign(pk, newPacket(city, false));
      const cu = city.curves[pk.l];
      const q = pt(cu, pk.dir > 0 ? pk.t : 1 - pk.t);
      const tail = pt(cu, Math.max(0, Math.min(1, pk.dir > 0 ? pk.t - .04 : 1 - pk.t + .04)));
      const grd = ctx.createLinearGradient(X(tail.x), Y(tail.y), X(q.x), Y(q.y));
      grd.addColorStop(0, 'rgba(255,195,95,0)'); grd.addColorStop(1, pk.c);
      ctx.strokeStyle = grd; ctx.lineWidth = Math.max(1.5, 2.4 * sc);
      ctx.beginPath(); ctx.moveTo(X(tail.x), Y(tail.y)); ctx.lineTo(X(q.x), Y(q.y)); ctx.stroke();
      ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(X(q.x), Y(q.y), Math.max(1.2, 1.8 * sc), 0, 6.28); ctx.fill();
    });
    ctx.restore();
  }

  function draw(s, time) {
    const { ctx, W, H, sc, ox } = s;
    const t = time / 1000;
    const cityTarget = s.mode === 1 || s.mode === 3 ? 1 : 0, netTarget = s.mode === 2 || s.mode === 3 ? 1 : s.mode === 1 ? .35 : .6;
    s.cityI += (cityTarget - s.cityI) * .03;
    s.netI += (netTarget - s.netI) * .03;
    ctx.clearRect(0, 0, W, H);

    const f = cityState.fade, a = CITIES[cityState.cur], b = CITIES[cityState.next];
    if (!s.networkOnly) {
      const g = ctx.createLinearGradient(0, 0, 0, H);
      g.addColorStop(0, C.skyTop); g.addColorStop(.55, C.skyTop); g.addColorStop(1, C.skyLow);
      ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      const gx = ox + (a.glowX * (1 - f) + b.glowX * f) * sc, gy = H - 40 * sc;
      const rg = ctx.createRadialGradient(gx, gy, 0, gx, gy, 700 * sc);
      rg.addColorStop(0, `rgba(${C.glow},${.2 + s.cityI * .12})`); rg.addColorStop(1, `rgba(${C.glow},0)`);
      ctx.fillStyle = rg; ctx.fillRect(0, 0, W, H);
    }
    drawCity(s, a, 1 - f, t, s.packets[cityState.cur]);
    if (f > 0) drawCity(s, b, f, t, s.packets[cityState.next]);
  }

  /* ---------------- Bucle ---------------- */
  let raf = 0, last = 0;
  const loop = time => {
    if (!reduce) {
      const dt = last ? Math.min(100, time - last) : 0; last = time;
      cityState.since += dt;
      if (cityState.fade > 0 || cityState.since > CITY_TIME) {
        if (cityState.fade === 0) announce(CITIES[cityState.next].name);
        cityState.fade = Math.min(1, cityState.fade + dt / FADE_TIME);
        if (cityState.fade >= 1) {
          cityState.cur = cityState.next; cityState.next = (cityState.cur + 1) % CITIES.length;
          cityState.fade = 0; cityState.since = 0;
        }
      }
    }
    scenes.forEach(s => { if (s.visible) draw(s, time); });
    raf = reduce ? 0 : requestAnimationFrame(loop);
  };
  const start = () => { if (!raf && !reduce) { last = 0; raf = requestAnimationFrame(loop); } };
  const stop = () => { cancelAnimationFrame(raf); raf = 0; };

  window.addEventListener('resize', () => { scenes.forEach(resize); if (reduce) loop(0); }, { passive: true });
  scenes.forEach(resize);

  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => {
      es.forEach(e => { const s = scenes.find(x => x.cv === e.target); if (s) s.visible = e.isIntersecting; });
      scenes.some(s => s.visible) ? start() : stop();
    });
    scenes.forEach(s => io.observe(s.cv));
  }
  document.addEventListener('visibilitychange', () => (document.hidden ? stop() : start()));
  start();
  if (reduce) loop(0);
  setTimeout(() => announce(CITIES[cityState.cur].name), 0);

  window.MYGScene = {
    setMode(m) { scenes.forEach(s => { s.mode = m; }); if (reduce) loop(0); },
  };
})();
