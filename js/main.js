/* M&G Consulting — interacción */
(() => {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  /* ---------- Cabecera ---------- */
  const header = $('.site-header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 10);
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Menú móvil ---------- */
  const toggle = $('.nav-toggle');
  const nav = $('#nav');
  const setNav = open => {
    nav.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    document.body.classList.toggle('nav-open', open);
  };
  toggle.addEventListener('click', () => setNav(!nav.classList.contains('open')));
  $$('a', nav).forEach(a => a.addEventListener('click', () => setNav(false)));

  /* ---------- Menús desplegables (Servicios, Clientes) ---------- */
  const menus = $$('.has-menu').map(wrap => ({ wrap, btn: $('button', wrap), panel: $('.submenu', wrap) }));
  const setMenu = (m, open) => { m.panel.classList.toggle('open', open); m.btn.setAttribute('aria-expanded', String(open)); };
  const closeMenus = except => menus.forEach(m => { if (m !== except) setMenu(m, false); });
  menus.forEach(m => {
    m.btn.addEventListener('click', e => { e.stopPropagation(); const open = !m.panel.classList.contains('open'); closeMenus(m); setMenu(m, open); });
    m.wrap.addEventListener('focusout', e => {
      if (!m.wrap.contains(e.relatedTarget) && matchMedia('(min-width: 1181px)').matches) setMenu(m, false);
    });
  });
  document.addEventListener('click', e => { if (!e.target.closest('.has-menu')) closeMenus(); });
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    const open = menus.find(m => m.panel.classList.contains('open'));
    if (open) { setMenu(open, false); open.btn.focus(); }
    else if (nav.classList.contains('open')) { setNav(false); toggle.focus(); }
  });

  /* ---------- Enlace activo según la sección visible (portada) ---------- */
  const links = $$('.nav-link[href*="#"]');
  if ('IntersectionObserver' in window && $('.hero-scene')) {
    const map = new Map(links.map(l => [l.hash.slice(1), l]));
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => {
        const l = map.get(en.target.id);
        if (!l) return;
        if (en.isIntersecting) { links.forEach(x => x.removeAttribute('aria-current')); l.setAttribute('aria-current', 'page'); }
        else if (l.getAttribute('aria-current')) l.removeAttribute('aria-current');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) io.observe(s); });
  }

  /* ---------- Subnavegación de las landings: sección activa ---------- */
  const subLinks = $$('.subnav a');
  if (subLinks.length && 'IntersectionObserver' in window) {
    const byId = new Map(subLinks.map(a => [a.hash.slice(1), a]));
    const sio = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (!en.isIntersecting) return;
        subLinks.forEach(a => a.removeAttribute('aria-current'));
        const a = byId.get(en.target.id);
        if (a) {
          a.setAttribute('aria-current', 'true');
          // Solo se desplaza la barra horizontalmente; nunca la página
          const bar = a.closest('ul');
          if (bar && bar.scrollWidth > bar.clientWidth) bar.scrollTo({ left: a.offsetLeft - (bar.clientWidth - a.offsetWidth) / 2, behavior: reduceMotion ? 'auto' : 'smooth' });
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    byId.forEach((_, id) => { const h = document.getElementById(id); if (h) sio.observe(h.closest('section') ? h : h); });
  }

  /* ---------- Cómo trabajamos: ruta de servicio ---------- */
  $$('[data-route]').forEach(route => {
    const stage = $('.route-stage', route);
    const list = $('.route-steps', route);
    const steps = $$('.route-step', route);
    const chips = $$('.route-nav a', route);
    const setPhase = i => {
      stage.dataset.phase = i;
      steps.forEach((s, j) => s.classList.toggle('is-active', j === i));
      chips.forEach((a, j) => (j === i ? a.setAttribute('aria-current', 'step') : a.removeAttribute('aria-current')));
    };
    if ('IntersectionObserver' in window) {
      route.classList.add('is-live');
      const io = new IntersectionObserver(entries => {
        entries.forEach(en => { if (en.isIntersecting) setPhase(steps.indexOf(en.target)); });
      }, { rootMargin: '-45% 0px -45% 0px' });
      steps.forEach(s => io.observe(s));
    }
    // Relleno de la línea de progreso según el scroll
    let ticking = false;
    const progress = () => {
      ticking = false;
      const r = list.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (innerHeight * 0.5 - r.top) / r.height));
      list.style.setProperty('--p', p.toFixed(3));
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(progress); } }, { passive: true });
    progress();
    // Las animaciones del esquema (SMIL y CSS) solo corren mientras la sección está a la vista
    const svg = $('.rt-svg', route);
    if (svg && svg.pauseAnimations && 'IntersectionObserver' in window) {
      svg.pauseAnimations();
      new IntersectionObserver(([en]) => {
        route.classList.toggle('is-visible', en.isIntersecting);
        if (en.isIntersecting) svg.unpauseAnimations(); else svg.pauseAnimations();
      }, { rootMargin: '50px' }).observe(route);
    } else route.classList.add('is-visible');
    // Vídeo de fondo (Remotion): solo se descarga y reproduce cuando la sección está a la vista
    const vid = $('video[data-lazy]', route);
    if (vid && !reduceMotion && 'IntersectionObserver' in window) {
      let loaded = false;
      new IntersectionObserver(([en]) => {
        if (en.isIntersecting) {
          if (!loaded) { $$('source[data-src]', vid).forEach(s => { s.src = s.dataset.src; }); vid.load(); loaded = true; }
          vid.play().catch(() => {});
        } else vid.pause();
      }, { rootMargin: '100px' }).observe(route);
    }
  });

  /* ---------- Ciudad que se muestra en el fondo ---------- */
  const cityLabel = $('[data-city-label]');
  if (cityLabel) document.addEventListener('myg:city', e => {
    cityLabel.classList.add('swap');
    setTimeout(() => { cityLabel.textContent = e.detail.name; cityLabel.classList.remove('swap'); }, 250);
  });

  /* ---------- Carrusel del hero ---------- */
  const car = $('[data-carousel]');
  if (car) {
    const slides = $$('.slide', car);
    const tabs = $$('[data-go]', car);
    const pauseBtn = $('[data-pause]', car);
    const DURATION = 7000;
    let current = 0, elapsed = 0, last = 0, userPaused = reduceMotion, hoverPaused = false;

    const go = (i, focus = false) => {
      current = (i + slides.length) % slides.length;
      elapsed = 0;
      slides.forEach((s, k) => {
        const on = k === current;
        s.classList.toggle('is-active', on);
        s.setAttribute('aria-hidden', String(!on));
        $$('a, button', s).forEach(el => { el.tabIndex = on ? 0 : -1; });
      });
      tabs.forEach((t, k) => {
        t.setAttribute('aria-selected', String(k === current));
        t.tabIndex = k === current ? 0 : -1;
        t.classList.toggle('done', k < current);
        t.style.setProperty('--p', '0%');
      });
      if (focus) tabs[current].focus();
      if (window.MYGScene) window.MYGScene.setMode(Number(slides[current].dataset.scene || 0));
    };

    const setPaused = p => {
      userPaused = p;
      pauseBtn.classList.toggle('paused', p);
      pauseBtn.setAttribute('aria-label', p ? 'Reanudar presentación' : 'Pausar presentación');
    };

    tabs.forEach((t, k) => {
      t.addEventListener('click', () => go(k));
      t.addEventListener('keydown', e => {
        if (e.key === 'ArrowRight') { e.preventDefault(); go(current + 1, true); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); go(current - 1, true); }
      });
    });
    pauseBtn.addEventListener('click', () => setPaused(!userPaused));
    car.addEventListener('mouseenter', () => { hoverPaused = true; });
    car.addEventListener('mouseleave', () => { hoverPaused = false; });
    car.addEventListener('focusin', () => { hoverPaused = true; });
    car.addEventListener('focusout', e => { if (!car.contains(e.relatedTarget)) hoverPaused = false; });

    // Deslizar en móvil
    let x0 = null;
    car.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
    car.addEventListener('touchend', e => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) go(current + (dx < 0 ? 1 : -1));
      x0 = null;
    });

    const tick = now => {
      const dt = last ? now - last : 0; last = now;
      if (!userPaused && !hoverPaused && !document.hidden) {
        elapsed += dt;
        tabs[current].style.setProperty('--p', Math.min(100, elapsed / DURATION * 100) + '%');
        if (elapsed >= DURATION) go(current + 1);
      }
      requestAnimationFrame(tick);
    };
    setPaused(userPaused);
    go(0);
    requestAnimationFrame(tick);
  }

  /* ---------- Consola de monitorización (demostración) ---------- */
  const ago = $('[data-ago]');
  if (ago) {
    const rows = $$('[data-checks] li');
    let n = 0;
    setInterval(() => {
      n = (n + 1) % 30;
      if (n === 0 && !reduceMotion) rows.forEach((r, i) => setTimeout(() => { r.classList.remove('flash'); void r.offsetWidth; r.classList.add('flash'); }, i * 110));
      ago.textContent = n;
    }, 1000);
  }

  /* ---------- Formulario de contacto ---------- */
  const form = $('#contact-form');
  if (form) {
    const status = $('#form-status');
    // Mensaje preparado desde el catálogo o desde un caso de éxito
    try {
      const pre = sessionStorage.getItem('myg-mensaje');
      if (pre) { form.elements.mensaje.value = pre; sessionStorage.removeItem('myg-mensaje'); const opt = [...form.elements.asunto.options].find(o => o.text === 'Suministro IT'); if (opt) form.elements.asunto.value = opt.value; }
    } catch {}
    const ts = form.elements.ts;
    ts.value = Date.now();
    const setStatus = (msg, type = '') => { status.textContent = msg; status.className = 'form-status ' + type; };

    const rules = {
      nombre: v => v.trim() ? '' : 'Indica tu nombre.',
      email: (v, el) => !v.trim() ? 'Indica tu correo.' : (el.validity.valid ? '' : 'Revisa el formato del correo.'),
      mensaje: v => v.trim().length >= 10 ? '' : 'Cuéntanos un poco más (mínimo 10 caracteres).',
    };
    const check = el => {
      const rule = rules[el.name];
      if (!rule) return true;
      const msg = rule(el.value, el);
      const err = document.getElementById(el.id + '-err');
      el.setAttribute('aria-invalid', String(!!msg));
      if (err) { err.textContent = msg; el.setAttribute('aria-describedby', err.id); }
      return !msg;
    };
    Object.keys(rules).forEach(name => {
      const el = form.elements[name];
      el.addEventListener('blur', () => { if (el.value) check(el); });
      el.addEventListener('input', () => { if (el.getAttribute('aria-invalid') === 'true') check(el); });
    });

    form.addEventListener('submit', async e => {
      e.preventDefault();
      const fields = Object.keys(rules).map(n => form.elements[n]);
      const results = fields.map(check);
      const consent = form.elements.consentimiento;
      consent.closest('.consent').dataset.invalid = String(!consent.checked);
      const firstBad = fields[results.indexOf(false)] || (!consent.checked && consent);
      if (firstBad) {
        setStatus(firstBad === consent ? 'Acepta la política de privacidad para continuar.' : 'Revisa los campos marcados.', 'error');
        firstBad.focus();
        return;
      }

      const btn = form.querySelector('[type="submit"]');
      btn.setAttribute('aria-busy', 'true');
      setStatus('Enviando…');
      try {
        const res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        const json = await res.json().catch(() => ({}));
        if (!res.ok || !json.ok) throw new Error(json.error || res.status);
        form.reset();
        ts.value = Date.now();
        setStatus('Mensaje enviado. Te responderemos lo antes posible.', 'ok');
      } catch {
        setStatus('No se ha podido enviar. Escríbenos directamente a info@myg.consulting.', 'error');
      } finally {
        btn.removeAttribute('aria-busy');
      }
    });
  }
})();
