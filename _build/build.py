#!/usr/bin/env python3
"""
Generador de la web de M&G Consulting.

Todas las páginas comparten cabecera, pie y estilos. El contenido de los
servicios está en SERVICES. Para cambiar un texto:
  1. Edita este archivo.
  2. Ejecuta:  python3 _build/build.py
  3. Sube al hosting los .html generados (la carpeta _build no hace falta subirla).
"""
import html, json, os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://myg.consulting"
EMAIL = "info@myg.consulting"
MCLOUD_URL = "https://clientes.myg.consulting/login"   # acceso de clientes a MCloud
ADDRESS = "Ronda de Sant Pere, 17, 08010 Barcelona"
MADRID = "Técnicos en Madrid y clientes en la Comunidad de Madrid"
TODAY = date.today().isoformat()
e = html.escape

# --------------------------------------------------------------------------
# Iconos (trazo, heredan color)
# --------------------------------------------------------------------------
ICON = {
    "arrow": '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10h11m-4-4 4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "chev": '<svg class="chev" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="m3 4.5 3 3 3-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="m4 7 8 6 8-6" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21Z" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="9.5" r="2.5" stroke="currentColor" stroke-width="1.6"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/><path d="M12 7.5V12l3 2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "scale": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 4v16M7 20h10M5 8h14M5 8l-2.5 6a2.5 2.5 0 0 0 5 0L5 8Zm14 0-2.5 6a2.5 2.5 0 0 0 5 0L19 8Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "stamp": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M9 4h6v4a3 3 0 0 1-1 2.2L13 11v2h5a2 2 0 0 1 2 2v2H4v-2a2 2 0 0 1 2-2h5v-2l-1-.8A3 3 0 0 1 9 8V4ZM5 20h14" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "building": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 20V6l8-3v17M12 8h8v12M3 20h18M7.5 9h1M7.5 12.5h1M7.5 16h1M15.5 12h1M15.5 15.5h1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "network": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="9" y="3" width="6" height="5" rx="1.2" stroke="currentColor" stroke-width="1.6"/><rect x="3" y="16" width="6" height="5" rx="1.2" stroke="currentColor" stroke-width="1.6"/><rect x="15" y="16" width="6" height="5" rx="1.2" stroke="currentColor" stroke-width="1.6"/><path d="M12 8v4M6 16v-2h12v2" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.6 3.1 8.2 7.5 9.5 4.4-1.3 7.5-4.9 7.5-9.5V6L12 3Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="m8.8 12 2.2 2.2 4.2-4.4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 18.5h10.5a4 4 0 0 0 .6-7.95A6 6 0 0 0 6.6 9.1 4.7 4.7 0 0 0 7 18.5Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "apps": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="4" y="4" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.6"/><rect x="13" y="4" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.6"/><rect x="4" y="13" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.6"/><rect x="13" y="13" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.6"/></svg>',
    "server": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="4" y="4" width="16" height="6.5" rx="1.6" stroke="currentColor" stroke-width="1.6"/><rect x="4" y="13.5" width="16" height="6.5" rx="1.6" stroke="currentColor" stroke-width="1.6"/><path d="M8 7.25h.01M8 16.75h.01M12 7.25h4M12 16.75h4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "box": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="m12 3 8 4.2v9.6L12 21l-8-4.2V7.2L12 3Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="m4.3 7.4 7.7 4.1 7.7-4.1M12 11.5V21" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "sparkle": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M10 4.5 11.6 9a2 2 0 0 0 1.3 1.3L17.5 12l-4.6 1.6a2 2 0 0 0-1.3 1.3L10 19.5l-1.6-4.6a2 2 0 0 0-1.3-1.3L2.5 12l4.6-1.6A2 2 0 0 0 8.4 9L10 4.5ZM18 3v4M16 5h4M19 16v3M17.5 17.5h3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "headset": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4.5 14v-2a7.5 7.5 0 0 1 15 0v2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><rect x="3.5" y="13" width="4" height="6" rx="1.5" stroke="currentColor" stroke-width="1.6"/><rect x="16.5" y="13" width="4" height="6" rx="1.5" stroke="currentColor" stroke-width="1.6"/><path d="M18.5 19c0 1.2-1.3 2-3 2H13" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "radar": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="12" r="4.5" stroke="currentColor" stroke-width="1.6" stroke-opacity=".6"/><path d="M12 12 18 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="15.5" cy="9.5" r="1.4" fill="currentColor"/></svg>',
    "ticket": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 7.5A1.5 1.5 0 0 1 5.5 6h13A1.5 1.5 0 0 1 20 7.5V10a2 2 0 0 0 0 4v2.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 16.5V14a2 2 0 0 0 0-4V7.5Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 10h6M9 14h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 20h16M7 16v-4M11.5 16V8M16 16v-6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="m6 9 4-3 3 2 5-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "calculator": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><rect x="8" y="6" width="8" height="3.5" rx="1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M8.5 13h.01M12 13h.01M15.5 13h.01M8.5 16.5h.01M12 16.5h.01M15.5 16.5h.01" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "umbrella": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12a9 9 0 0 1 18 0H3ZM12 3v1M12 12v6.5a2 2 0 0 1-4 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "factory": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 20V10l5 3V10l5 3V10l5 3V5h3v15H3ZM7 16.5h2M11.5 16.5h2M16 16.5h2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "forklift": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 17V9h6l3 5v3M9 9V5H5v4M15 4v14h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="6" cy="18" r="2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="18" r="2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "conveyor": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="5" y="5" width="6" height="6" rx="1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><rect x="13" y="7" width="5" height="4" rx="1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><rect x="3" y="14" width="18" height="4" rx="2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M7 16h.01M12 16h.01M17 16h.01M6 18v3M18 18v3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M13 3 5 13.5h6L10 21l8-10.5h-6L13 3Z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "bag": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 8h14l-1 12.5H6L5 8ZM9 10V7a3 3 0 0 1 6 0v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "basket": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 10h18l-2 10H5L3 10ZM7.5 10 11 4M16.5 10 13 4M9 14v3M12 14v3M15 14v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "parking": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 17V7h3.5a3 3 0 0 1 0 6H10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="12" r="6.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "shirt": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M9 3.5 4 6l-1.5 4.5L6 12v8.5h12V12l3.5-1.5L20 6l-5-2.5a3 3 0 0 1-6 0Z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "check": '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="m4 8.5 2.6 2.5L12 5.5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "school": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="m2.5 9 9.5-5 9.5 5-9.5 5-9.5-5ZM6.5 11v5c3 2.5 8 2.5 11 0v-5M21.5 9v5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "laptop": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="4.5" y="5" width="15" height="10.5" rx="1.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M2.5 19h19l-1.5-3.5H4Z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 3h7l4 4v14H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1ZM14 3v4h4M9.5 12h5M9.5 15.5h5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "migrate": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 8h13l-3-3M20 16H7l3 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "trophy": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M8 4h8v5a4 4 0 0 1-8 0V4ZM8 6H5v1.5A3 3 0 0 0 8 10.5M16 6h3v1.5a3 3 0 0 1-3 3M12 13v4M8.5 20h7M10 17h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}

GEM = {"orange": "gem", "amber": "gem gem-amber", "sun": "gem gem-sun"}


def isotipo(uid, interactive=False, cls=""):
    """Isotipo de M&G en SVG: rombo redondeado de cuatro piezas."""
    tiles = [  # (x, y, color, pilar, etiqueta, posición etiqueta)
        (30, 30, "#F98A47", "seguridad", "Seguridad", (100, 62)),
        (100, 30, "#FEAF3F", "cloud", "Cloud", (138, 100)),
        (100, 100, "#FFC35F", "m365", "M365", (100, 138)),
        (30, 100, "#FDA83B", "soporte", "Soporte", (62, 100)),
    ]
    rects, labels = [], []
    for x, y, c, key, label, (lx, ly) in tiles:
        if interactive:
            rects.append(f'<rect class="tile" data-pillar="{key}" tabindex="0" role="button" aria-label="{e(label)}" x="{x}" y="{y}" width="70" height="70" fill="{c}" stroke="#101C30" stroke-width="1.5"/>')
            labels.append(f'<text class="tile-label" x="{lx}" y="{ly}" text-anchor="middle" dominant-baseline="middle">{e(label)}</text>')
        else:
            rects.append(f'<rect x="{x}" y="{y}" width="70" height="70" fill="{c}"/>')
    hidden = '' if interactive else ' aria-hidden="true" focusable="false"'
    return (f'<svg class="{cls}" viewBox="0 0 200 200"{hidden}><defs><clipPath id="clip-{uid}">'
            f'<rect x="30" y="30" width="140" height="140" rx="24"/></clipPath></defs>'
            f'<g transform="rotate(45 100 100)" clip-path="url(#clip-{uid})">{"".join(rects)}</g>'
            f'{"".join(labels)}</svg>')


# --------------------------------------------------------------------------
# Contenido de servicios
# --------------------------------------------------------------------------
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contenido_servicios import SERVICES, PROBLEMS, RELATED_CASE, MODALITIES  # noqa: E402
from contenido_casos import CASES  # noqa: E402
# Casos de ejemplo (inventados): False para ocultarlos al publicar la web
PUBLICAR_EJEMPLOS = True
if not PUBLICAR_EJEMPLOS:
    CASES[:] = [c for c in CASES if not c.get("ejemplo")]
from contenido_clientes import SECTORS, GROUPS  # noqa: E402
from contenido_noticias import NEWS  # noqa: E402
import ilustraciones as ilus  # noqa: E402
from contenido_metodo import METHOD  # noqa: E402
from contenido_equipo import TEAM, VENDORS  # noqa: E402
CASE_BY_SLUG = {c['slug']: c for c in CASES}

# Equipo con LinkedIn: se edita solo data/equipo.json (ver "personas" y "empresa.linkedin")
MOSTRAR_ESTADOS = False   # estados "Disponible / En visita…" del panel de equipo: eran de ejemplo, no datos reales
with open(os.path.join(ROOT, "data", "equipo.json"), encoding="utf-8") as _f:
    EQUIPO = json.load(_f)

HOME_FAQS = [
    ("¿Qué incluye el servicio gestionado MGCare?", "Soporte a usuarios, monitorización de servidores y servicios, gestión de parches, revisión de copias y administración de Microsoft 365 y cloud, con informes de actividad y estado cuando los necesites. El alcance se ajusta a cada empresa."),
    ("¿Trabajáis solo en Barcelona?", "No. Nuestra oficina está en Barcelona y además contamos con técnicos en Madrid, donde también tenemos clientes. La mayor parte del soporte se presta en remoto, así que podemos atender a empresas de toda España, y organizamos visitas presenciales en Barcelona y Madrid cuando hace falta."),
    ("¿Cómo se abre una incidencia?", "Tus usuarios pueden escribir un correo, llamar o usar el portal. Cada petición queda registrada en nuestro sistema de tickets con su seguimiento."),
    ("¿Tengo que firmar una permanencia?", "Cada propuesta detalla sus condiciones. Preferimos que te quedes porque el servicio funciona, no por un contrato."),
    ("¿Podéis trabajar junto a nuestro equipo IT interno?", "Sí. Podemos cubrir áreas concretas, dar soporte de segundo nivel o reforzar a tu equipo en proyectos puntuales."),
]

# --------------------------------------------------------------------------
# Plantilla común
# --------------------------------------------------------------------------
SVC_ICON = {
    "mgcare": "headset", "ciberseguridad": "shield", "cloud": "cloud", "microsoft-365": "apps",
    "proyectos-it": "server", "suministro-it": "box", "transformacion-digital": "sparkle",
}
TONE = {"orange": "tone-orange", "amber": "tone-amber", "sun": "tone-sun"}


def svc_icon(s):
    return f'<span class="svc-icon {TONE[s["gem"]]}" aria-hidden="true">{ICON[SVC_ICON[s["slug"]]]}</span>'


def sector_icon(sec, tone="tone-amber"):
    return f'<span class="svc-icon {tone}" aria-hidden="true">{ICON[sec["icon"]]}</span>'


def nav(base, current):
    def link(href, label, key):
        cur = ' aria-current="page"' if current == key else ''
        return f'<a class="nav-link" href="{href}"{cur}>{label}</a>'

    def cur(key):
        return ' aria-current="page"' if current == key else ''

    servs = "".join(
        f'<a href="{base}servicios/{s["slug"]}.html">{svc_icon(s)}<span><strong>{e(s["name"])}</strong><small>{e(s["short"])}</small></span></a>'
        for s in SERVICES)
    def sector_link(c):
        return f'<a href="{base}clientes/{c["slug"]}.html">{sector_icon(c)}<span><strong>{e(c["name"])}</strong><small>{e(c["short"])}</small></span></a>'
    sectors = "".join(
        f'<div class="mega-col"><p class="submenu-title">{e(g)}</p>{"".join(sector_link(c) for c in SECTORS if c["group"] == g)}</div>'
        for g in GROUPS)
    return f'''
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{base}index.html"><img src="{base}assets/img/logo-myg-blanco.png" width="448" height="164" alt="M&amp;G Consulting, inicio"></a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Abrir menú"><span></span><span></span></button>
      <nav id="nav" class="nav" aria-label="Principal">
        <div class="has-menu">
          <button class="nav-link" aria-expanded="false" aria-controls="menu-servicios"{cur("servicios")}>Servicios {ICON["chev"]}</button>
          <div class="submenu" id="menu-servicios">
            <p class="submenu-title">Servicios</p>
            {servs}
            <a class="submenu-all" href="{base}index.html#servicios">Ver todos los servicios {ICON["arrow"]}</a>
          </div>
        </div>
        <div class="has-menu">
          <button class="nav-link" aria-expanded="false" aria-controls="menu-clientes"{cur("clientes")}>Clientes {ICON["chev"]}</button>
          <div class="submenu submenu-mega" id="menu-clientes">
            <div class="mega-grid">{sectors}</div>
            <div class="mega-foot">
              <a href="{base}casos-de-exito.html"><span class="svc-icon tone-orange" aria-hidden="true">{ICON["trophy"]}</span><span><strong>Casos de éxito</strong><small>Proyectos reales de M&amp;G y sus resultados.</small></span></a>
              <a class="submenu-all" href="{base}clientes.html">Ver todos los clientes {ICON["arrow"]}</a>
            </div>
          </div>
        </div>
        {link(base + "nosotros.html", "Nosotros", "nosotros")}
        {link(base + "noticias.html", "Noticias", "noticias")}
        {link(base + "catalogo.html", "Catálogo", "catalogo")}
        <div class="nav-actions">
          <a class="btn btn-outline-light btn-sm" href="{MCLOUD_URL}" rel="noopener">Acceso MCloud</a>
          <a class="btn btn-primary btn-sm" href="{base}contacto.html#formulario">Hablemos</a>
        </div>
      </nav>
    </div>
  </header>'''


def footer(base):
    servs = "".join(f'<li><a href="{base}servicios/{s["slug"]}.html">{e(s["name"])}</a></li>' for s in SERVICES)
    secs = "".join(f'<li><a href="{base}clientes/{c["slug"]}.html">{e(c["name"])}</a></li>' for c in SECTORS)
    return f'''
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="{base}assets/img/logo-myg-blanco.png" width="448" height="164" alt="M&amp;G Consulting" loading="lazy">
          <p>Consultoría tecnológica y servicios IT gestionados para empresas y despachos profesionales.</p>
          <p><a class="footer-legal" href="mailto:{EMAIL}">{EMAIL}</a><br>{e(ADDRESS)}<br>Técnicos en Madrid</p>
        </div>
        <div class="footer-col"><h2>Servicios</h2><ul>{servs}</ul></div>
        <div class="footer-col"><h2>Clientes</h2><ul><li><a href="{base}casos-de-exito.html">Casos de éxito</a></li>{secs}</ul></div>
        <div class="footer-col"><h2>Empresa</h2><ul>
          <li><a href="{base}nosotros.html">Nosotros</a></li>
          <li><a href="{base}noticias.html">Noticias</a></li>
          <li><a href="{base}catalogo.html">Catálogo</a></li>
          <li><a href="{MCLOUD_URL}" rel="noopener">Acceso MCloud</a></li>
          <li><a href="{base}contacto.html">Contacto</a></li>
        </ul></div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year>{date.today().year}</span> M&amp;G Corporate Consulting S.L. · CIF B22878243</span>
        <span><a class="footer-legal" href="{base}legal/aviso-legal.html">Aviso legal</a> · <a class="footer-legal" href="{base}legal/privacidad.html">Privacidad</a> · <a class="footer-legal" href="{base}legal/cookies.html">Cookies</a></span>
      </div>
    </div>
  </footer>'''


def asset(base, rel):
    """URL de css/js con versión por contenido (rompe la caché al cambiar) y versión .min si existe (ver minificar.py)."""
    import hashlib
    root, ext = os.path.splitext(rel)
    if os.path.exists(os.path.join(ROOT, f"{root}.min{ext}")):
        rel = f"{root}.min{ext}"
    with open(os.path.join(ROOT, rel), "rb") as f:
        v = hashlib.sha1(f.read()).hexdigest()[:8]
    return f"{base}{rel}?v={v}"


def fit_title(t, limit=60):
    """Título de buscador ≤ limit caracteres: acorta la marca y, si hace falta, el complemento geográfico."""
    for a, b in ((" | M&G Consulting", " | M&G"), (" para empresas en Barcelona y Madrid", " para empresas"),
                 (" en Barcelona y Madrid", ""), (" | Casos de éxito M&G", " | M&G"), (" | M&G", "")):
        if len(t) <= limit:
            break
        t = t.replace(a, b)
    return t


def fit_desc(d, limit=160):
    """Descripción ≤ limit caracteres, cortada en el final de frase o palabra más cercano."""
    if len(d) <= limit:
        return d
    cut = d[:limit - 1]
    for sep in (". ", "; "):
        i = cut.rfind(sep)
        if i > 90:
            return cut[:i + 1].strip()
    return cut[:cut.rfind(" ")].rstrip(",;: ") + "…"


def crumbs_ld(*items):
    """BreadcrumbList a partir de pares (nombre, url relativa a SITE)."""
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "item": SITE + "/" + u} for i, (n, u) in enumerate(items, 1)]}


def page(path, title, desc, body, current="", base="", jsonld=None, noindex=False, scripts=()):
    title, desc = fit_title(title), fit_desc(desc)
    extra_js = "".join(f'\n  <script src="{asset(base, "js/" + s)}" defer></script>' for s in scripts)
    url = f"{SITE}/{path}" if path != "index.html" else f"{SITE}/"
    ld = "".join(f'\n  <script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ''
    out = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">{robots}
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#101C30">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="M&amp;G Consulting">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="M&amp;G Consulting: consultoría IT y servicios gestionados">
  <meta property="og:locale" content="es_ES">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(desc)}">
  <meta name="twitter:image" content="{SITE}/assets/img/og-image.jpg">
  <link rel="icon" href="{base}favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="{base}assets/img/icon-32.png">
  <link rel="apple-touch-icon" href="{base}assets/img/icon-180.png">
  <link rel="manifest" href="{base}site.webmanifest">
  <link rel="preload" href="{base}assets/fonts/sora.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{base}assets/fonts/plex-400.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{asset(base, "css/styles.css")}">{ld}
</head>
<body>
  <a class="skip" href="#main">Saltar al contenido</a>
{nav(base, current)}
  <main id="main">
{body}
  </main>
{footer(base)}
  <script src="{asset(base, "js/skyline.js")}" defer></script>
  <script src="{asset(base, "js/main.js")}" defer></script>{extra_js}
</body>
</html>
'''
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8", newline="\n").write(out)
    return path


def cta_band(base, title="¿Hablamos de tu infraestructura?", text="Cuéntanos cómo trabajáis hoy y te proponemos los siguientes pasos."):
    return f'''
    <section class="section">
      <div class="wrap">
        <div class="cta-band">
          {isotipo("cta", cls="deco")}
          <div><h2>{e(title)}</h2><p>{e(text)}</p></div>
          <div class="cta-actions">
            <a class="btn btn-primary" href="{base}contacto.html#formulario">Solicitar reunión {ICON["arrow"]}</a>
            <a class="btn btn-outline-light" href="mailto:{EMAIL}">{EMAIL}</a>
          </div>
        </div>
      </div>
    </section>'''


def faq_block(faqs, heading, intro, white=False):
    items = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faqs)
    return f'''
    <section class="section{' section-white' if white else ''}" aria-labelledby="faq-title">
      <div class="wrap faq">
        <div><h2 id="faq-title">{e(heading)}</h2><p>{intro}</p></div>
        <div class="faq-list">{items}</div>
      </div>
    </section>'''


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}



# --------------------------------------------------------------------------
# Fondo del hero: vídeo propio (opcional) + skylines animados de Barcelona y Madrid
#   Para usar un vídeo, copia los archivos a assets/media/ y rellena:
#   HERO_VIDEO = {"mp4": "assets/media/hero.mp4", "webm": "assets/media/hero.webm", "poster": "assets/media/hero.jpg"}
# --------------------------------------------------------------------------
HERO_VIDEO = None


def hero_media():
    canvas = '<canvas class="scene-canvas" data-skyline aria-hidden="true"></canvas>'
    if not HERO_VIDEO:
        return canvas
    srcs = ""
    if HERO_VIDEO.get("webm"): srcs += f'<source src="{HERO_VIDEO["webm"]}" type="video/webm">'
    if HERO_VIDEO.get("mp4"): srcs += f'<source src="{HERO_VIDEO["mp4"]}" type="video/mp4">'
    poster = f' poster="{HERO_VIDEO["poster"]}"' if HERO_VIDEO.get("poster") else ""
    return f'<video class="scene-video" autoplay muted loop playsinline preload="metadata"{poster} aria-hidden="true" data-video>{srcs}</video>' + canvas.replace("data-skyline", "data-skyline data-network-only")



# --------------------------------------------------------------------------
# Ayudas visuales comunes (iconos por concepto, checks, logos)
# --------------------------------------------------------------------------
ICON_RULES = [
    (("monitoriz", "supervis", "alerta"), "radar"),
    (("copia", "recuperaci", "réplica"), "server"),
    (("formaci", "concienciaci", "acompañamiento", "adopci"), "school"),
    (("auditor", "diagnóstico"), "radar"),
    (("correo", "phishing", "dkim", "dmarc"), "mail"),
    (("licencia", "suscripci"), "ticket"),
    (("copilot", " ia", "agente", "automatiz", "inteligencia"), "sparkle"),
    (("firewall", "perimetral", "seguridad", "protecci", "identidad", "mfa", "acceso condicional"), "shield"),
    (("vpn", "remoto", "escritorio", "sedes", "entornos híbridos", "conexión"), "network"),
    (("redes", "red ", "wifi", "switch", "segmentaci", "cableada"), "network"),
    (("auditor", "diagnóstico", "análisis", "inventario", "revisión"), "radar"),
    (("azure", "google cloud", "mcloud", "nube", "cloud"), "cloud"),
    (("servidor", "almacenamiento", "nas", "virtualiz"), "server"),
    (("migraci", "traslado"), "migrate"),
    (("teams", "sharepoint", "onedrive", "integraci", "aplicaciones"), "apps"),
    (("coste", "presupuesto"), "calculator"),
    (("helpdesk", "soporte", "usuario"), "headset"),
    (("puestos", "equipos", "dispositivos", "portátil", "preparaci"), "laptop"),
    (("informe",), "chart"),
    (("hoja de ruta", "plan"), "chart"),
    (("documenta", "documental"), "doc"),
]


def pick_icon(text, extra=""):
    """Busca primero en el título y, si no hay coincidencia, en la descripción."""
    for chunk in (text, extra):
        low = " " + chunk.lower()
        for keys, icon in ICON_RULES:
            if any(k in low for k in keys):
                return icon
    return "check"


def mcheck():
    return f'<span class="mcheck">{ICON["check"]}</span>'


# Nombre exacto (en minúsculas) → archivo en assets/img/fabricantes/
LOGO_BY_NAME = {
    "fortinet": "fortinet", "fortinet fortigate": "fortinet", "sonicwall": "sonicwall",
    "hpe": "hpe", "hpe proliant": "hpe", "qnap": "qnap", "synology": "synology",
    "aruba networking": "aruba", "ubiquiti": "ubiquiti", "ubiquiti unifi": "ubiquiti",
    "microsoft azure": "azure", "google cloud": "google-cloud", "microsoft 365": "microsoft",
    "microsoft intune": "intune", "azure backup": "azure-backup",
    "microsoft entra id": "entra", "microsoft defender": "defender",
}
TALL_LOGOS = {"intune", "azure-backup", "entra", "defender"}


def img_size(rel):
    """width/height reales del fichero para evitar saltos de maquetación (CLS)."""
    try:
        from PIL import Image
        with Image.open(os.path.join(ROOT, rel)) as im:
            return f' width="{im.width}" height="{im.height}"'
    except Exception:
        return ""


def tech_item(name, base):
    low = name.lower().strip()
    key = LOGO_BY_NAME.get(low)
    if key:
        for ext in ("svg", "png", "webp"):
            rel = f"assets/img/fabricantes/{key}.{ext}"
            if os.path.exists(os.path.join(ROOT, rel)):
                tall = " tech-logo-tall" if key in TALL_LOGOS else ""
                return f'<li class="tech-logo{tall}" title="{e(name)}"><img src="{base}{rel}" alt="{e(name)}"{img_size(rel)} loading="lazy"></li>'
    if low == "mcloud":
        return f'<li class="tech-logo tech-own" title="MCloud">{isotipo("tech-mcloud-" + str(abs(hash(base + name)) % 9999))}<span>MCloud</span></li>'
    return f"<li>{e(name)}</li>"

# --------------------------------------------------------------------------
# Cómo trabajamos: ruta de servicio (esquema de infraestructura que cambia con el scroll)
# --------------------------------------------------------------------------
ROUTE_HUB = (300, 250)
ROUTE_NODES = [  # clave, x, y, etiqueta, ¿con hallazgos en la auditoría? (esquema ilustrativo)
    ("srv", 110, 112, "Servidores", False),
    ("red", 492, 104, "Red y wifi", False),
    ("m365", 536, 276, "Microsoft 365", False),
    ("bak", 468, 418, "Copias", True),
    ("pc", 132, 410, "Equipos", False),
    ("sec", 62, 262, "Seguridad", True),
]


def route_stage(base):
    hx, hy = ROUTE_HUB
    links, draws, packets, nodes = [], [], [], []
    for i, (key, x, y, label, risk) in enumerate(ROUTE_NODES):
        d = f"M{hx} {hy} L{x} {y}"
        links.append(f'<path class="rt-link" d="{d}"/>')
        draws.append(f'<path class="rt-draw" d="{d}" pathLength="1" data-i="{i}"/>')
        pd = d if i % 2 == 0 else f"M{x} {y} L{hx} {hy}"
        packets.append(f'<circle class="rt-packet" r="4"><animateMotion dur="{2.6 + i * .35:.2f}s" begin="{i * .5:.1f}s" repeatCount="indefinite" path="{pd}"/></circle>')
        prio = {"sec": "1", "bak": "2"}.get(key, "")
        badge = (f'<g class="rt-badge" transform="translate({x + 22} {y - 22})"><circle r="11"/><text y="4" text-anchor="middle">{prio}</text></g>' if prio else "")
        tick = f'<path class="rt-tick" d="M{x - 6} {y} l4.5 4.5 l8 -9"/>' if risk else ""
        # La etiqueta se coloca en el lado exterior del nodo (lejos del centro) para no pisar los enlaces
        vx, vy = x - hx, y - hy
        norm = (vx * vx + vy * vy) ** .5
        ux, uy = vx / norm, vy / norm
        if .75 < abs(ux) <= .9:
            lx, ly, anchor = x + ux * 38, y + 5, "start" if ux > 0 else "end"
        elif uy < -.05:
            lx, ly, anchor = x, y - 38, "middle"
        else:
            lx, ly, anchor = x, y + 46, "middle"
        nodes.append(f'''<g class="rt-node{' is-risk' if risk else ''}">
            <circle class="rt-ring" cx="{x}" cy="{y}" r="26"/><circle class="rt-core" cx="{x}" cy="{y}" r="17"/>{tick}{badge}
            <text class="rt-label" x="{lx:.0f}" y="{ly:.0f}" text-anchor="{anchor}">{e(label)}</text></g>''')
    return f'''<svg class="rt-svg" viewBox="0 0 600 500" focusable="false">
          <defs>
            <linearGradient id="rt-scan-g" x1="0" x2="1"><stop offset="0" stop-color="#F98A47" stop-opacity="0"/><stop offset=".85" stop-color="#F98A47" stop-opacity=".35"/><stop offset=".97" stop-color="#FFC35F" stop-opacity=".75"/><stop offset="1" stop-color="#FFC35F" stop-opacity="0"/></linearGradient>
            <radialGradient id="rt-glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#F98A47" stop-opacity=".35"/><stop offset="1" stop-color="#F98A47" stop-opacity="0"/></radialGradient>
          </defs>
          <circle class="rt-halo" cx="{hx}" cy="{hy}" r="150" fill="url(#rt-glow)"/>
          <g>{"".join(links)}</g>
          <g>{"".join(draws)}</g>
          <g class="rt-packets">{"".join(packets)}</g>
          <circle class="rt-pulse" cx="{hx}" cy="{hy}" r="40"/><circle class="rt-pulse rt-pulse-2" cx="{hx}" cy="{hy}" r="40"/>
          <g class="rt-hub"><circle cx="{hx}" cy="{hy}" r="40"/><rect x="{hx - 14}" y="{hy - 15}" width="28" height="9" rx="2.5"/><rect x="{hx - 14}" y="{hy - 3}" width="28" height="9" rx="2.5"/><rect x="{hx - 14}" y="{hy + 9}" width="28" height="9" rx="2.5"/>
            <text x="{hx}" y="{hy + 70}" text-anchor="middle">Tu infraestructura</text></g>
          {"".join(nodes)}
          <rect class="rt-scan" x="-120" y="0" width="120" height="500" fill="url(#rt-scan-g)"/>
        </svg>'''


def route_video(base):
    """Vídeo de fondo del escenario (Remotion, ver video/). Solo se enlaza si existe; carga diferida."""
    mp4, webm, poster = "assets/media/ruta-red.mp4", "assets/media/ruta-red.webm", "assets/media/ruta-red.jpg"
    if not os.path.exists(os.path.join(ROOT, mp4)):
        return ""
    src = ""
    if os.path.exists(os.path.join(ROOT, webm)):
        src += f'<source data-src="{base}{webm}" type="video/webm">'
    src += f'<source data-src="{base}{mp4}" type="video/mp4">'
    pst = f' poster="{base}{poster}"' if os.path.exists(os.path.join(ROOT, poster)) else ""
    return f'<video class="rt-video" muted loop playsinline preload="none" data-lazy width="1280" height="720"{pst}>{src}</video>'


def method_block(base, white=False):
    steps, chips = [], []
    for i, m in enumerate(METHOD):
        n = f"{i + 1:02d}"
        pid = f"fase-{m['key']}"
        pts = "".join(f'<li><span class="mcheck">{ICON["check"]}</span>{e(p)}</li>' for p in m["points"])
        label, href = m["link"]
        a, bold = m["headline"]
        steps.append(f'''
          <li class="route-step{' is-active' if i == 0 else ''}" id="{pid}" aria-labelledby="{pid}-t">
            <span class="route-num" aria-hidden="true">{n}</span>
            <h3 id="{pid}-t">{e(m["verb"])}</h3>
            <p class="route-kicker">{e(m["kicker"])}</p>
            <p class="route-headline">{e(a)}<strong>{e(bold)}</strong></p>
            <p class="route-text">{e(m["text"])}</p>
            <ul class="mstep-points">{pts}</ul>
            <a class="service-more" href="{base}{href}">{e(label)} {ICON["arrow"]}</a>
          </li>''')
        chips.append(f'<li><a href="#{pid}"{' aria-current="step"' if i == 0 else ''}><span>{n}</span>{e(m["verb"])}</a></li>')
    return f'''
    <section class="section{' section-white' if white else ''}" id="metodo" aria-labelledby="metodo-title">
      <div class="wrap route" data-route>
        <div class="route-head">
          <h2 id="metodo-title">Cómo trabajamos</h2>
          <p>Cuatro fases para empezar con buen pie y mantener tu tecnología al día, sea cual sea el tamaño de tu empresa.</p>
        </div>
        <div class="route-grid">
          <div class="route-sticky">
            <div class="route-stage" data-phase="0" aria-hidden="true">
              {route_video(base)}
              {route_stage(base)}
              <span class="route-caption">Esquema ilustrativo</span>
            </div>
            <nav class="route-nav" aria-label="Fases del método"><ol>{"".join(chips)}</ol></nav>
          </div>
          <ol class="route-steps">{"".join(steps)}
          </ol>
        </div>
      </div>
    </section>'''


# --------------------------------------------------------------------------
# Equipo (avatares ilustrados) y fabricantes
# --------------------------------------------------------------------------
LOOKS = [  # (fondo, piel, pelo, peinado)
    ("#F98A47", "#F1C9A5", "#2B1D14", "short"),
    ("#FEAF3F", "#C98E6A", "#1A1A1A", "long"),
    ("#22385C", "#E8B793", "#5A3A22", "beard"),
    ("#FFC35F", "#8D5B3E", "#141414", "bun"),
    ("#F98A47", "#F3D2B8", "#7A4A28", "wavy"),
]


def avatar(look, uid):
    bg, skin, hair, style = LOOKS[look % len(LOOKS)]
    hair_shape = {
        "short": f'<path d="M22 27c0-8 6-13 12-13s12 5 12 13c-3-4-7-6-12-6s-9 2-12 6Z" fill="{hair}"/>',
        "long": f'<path d="M20 44V28c0-9 6-14 14-14s14 5 14 14v16c-2-4-3-10-3-15-4-2-18-2-22 0 0 5-1 11-3 15Z" fill="{hair}"/>',
        "beard": f'<path d="M22 26c0-7 5-12 12-12s12 5 12 12c-4-3-8-4-12-4s-8 1-12 4Z" fill="{hair}"/><path d="M25 33c1 7 5 10 9 10s8-3 9-10c-2 3-5 4-9 4s-7-1-9-4Z" fill="{hair}"/>',
        "bun": f'<circle cx="34" cy="11" r="6" fill="{hair}"/><path d="M22 28c0-8 5-13 12-13s12 5 12 13c-3-5-7-7-12-7s-9 2-12 7Z" fill="{hair}"/>',
        "wavy": f'<path d="M21 30c-1-10 5-16 13-16s14 6 13 16c-2-2-2-6-5-7-2 3-6 3-8 1-2 2-6 2-8-1-3 1-3 5-5 7Z" fill="{hair}"/>',
    }[style]
    return f'''<svg viewBox="0 0 68 68" aria-hidden="true" focusable="false"><defs><clipPath id="av-{uid}"><circle cx="34" cy="34" r="34"/></clipPath></defs>
<g clip-path="url(#av-{uid})"><rect width="68" height="68" fill="{bg}"/>
<path d="M10 68c1-12 11-19 24-19s23 7 24 19Z" fill="#101C30"/><path d="M29 47h10v5a5 5 0 0 1-10 0Z" fill="{skin}"/>
<ellipse cx="34" cy="31" rx="11" ry="13" fill="{skin}"/>{hair_shape}
<path d="M18 30a16 16 0 0 1 32 0" fill="none" stroke="#101C30" stroke-width="2.4"/><rect x="15" y="28" width="6" height="9" rx="3" fill="#101C30"/><rect x="47" y="28" width="6" height="9" rx="3" fill="#101C30"/>
<path d="M50 36c0 6-4 9-9 9" fill="none" stroke="#101C30" stroke-width="2"/></g></svg>'''


def team_panel(base):
    rows = []
    for i, m in enumerate(TEAM):
        photo = None
        for ext in ("webp", "jpg", "png"):
            rel = f"assets/img/equipo/{m['key']}.{ext}"
            if os.path.exists(os.path.join(ROOT, rel)):
                photo = f'<img src="{base}{rel}" alt="" width="68" height="68" loading="lazy">'
        who = f'<strong>{e(m["persona"])}</strong><span>{e(m["role"])}</span>' if m["persona"] else f'<strong>{e(m["role"])}</strong><span>{e(m["area"])}</span>'
        state, label = m["status"]
        skills = "".join(f"<li>{e(s)}</li>" for s in m["skills"])
        rows.append(f'''
            <li class="member">
              <span class="member-avatar">{photo or avatar(m["look"], m["key"])}{f'<i class="presence presence-{state}"></i>' if MOSTRAR_ESTADOS else ''}</span>
              <span class="member-who">{who}</span>
              {f'<span class="member-state">{e(label)}</span>' if MOSTRAR_ESTADOS else ''}
              <ul class="member-skills">{skills}</ul>
            </li>''')
    return f'''
        <div class="team-panel">
          <div class="team-head">
            <span class="team-title">Tu equipo en M&amp;G</span>
            <span class="team-live"><i></i>Barcelona · Madrid</span>
          </div>
          <ul class="team-list">{"".join(rows)}
          </ul>
          <div class="team-foot">{ICON["headset"]}<span>Un interlocutor para cada área y un único punto de contacto para ti.</span></div>
        </div>'''


def _linkedin_ok(url):
    return isinstance(url, str) and url.startswith("https://") and "linkedin.com/" in url.split("/")[2] + "/"


def people_cards(base):
    """Tarjetas de personas y datos de soporte, generadas desde data/equipo.json.
    Sin personas aprobadas no se pinta el bloque de personas (solo soporte y enlace a la empresa)."""
    cards = []
    for p in EQUIPO.get("personas", []):
        nombre, cargo = p["nombre"], p["cargo"]
        iniciales = "".join(w[0] for w in nombre.split()[:2]).upper()
        foto = p.get("foto")
        avatar_html = (f'<img src="{base}{foto}" alt="" width="64" height="64" loading="lazy">'
                       if foto and os.path.exists(os.path.join(ROOT, foto))
                       else f'<span class="initials" aria-hidden="true">{e(iniciales)}</span>')
        link = ""
        if _linkedin_ok(p.get("linkedin")):
            link = (f'<a class="person-link" href="{e(p["linkedin"])}" target="_blank" rel="noopener noreferrer">'
                    f'<span class="sr-only">Perfil de LinkedIn de {e(nombre)}</span>'
                    f'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.5h4V21H3V9.5Zm6.5 0h3.8v1.6h.1c.5-1 1.8-1.9 3.7-1.9 4 0 4.7 2.6 4.7 6V21h-4v-5c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4V9.5Z"/></svg>'
                    f'<span aria-hidden="true">LinkedIn</span></a>')
        cards.append(f'<li class="person"><span class="person-av">{avatar_html}</span>'
                     f'<span class="person-who"><strong>{e(nombre)}</strong>{f"<span>{e(cargo)}</span>" if cargo else ""}</span>{link}</li>')
    people = f'<ul class="people">{"".join(cards)}</ul>' if cards else ""
    empresa = EQUIPO.get("empresa", {})
    empresa_link = ""
    if _linkedin_ok(empresa.get("linkedin")):
        empresa_link = (f'<a class="btn btn-outline btn-sm" href="{e(empresa["linkedin"])}" target="_blank" rel="noopener noreferrer">'
                        f'Página de M&amp;G en LinkedIn</a>')
    # El correo, la oficina y el horario ya están en el bloque «¿Hablamos…?» y en Contacto: aquí solo el enlace a LinkedIn
    barra = f'<div class="team-social">{empresa_link}</div>' if empresa_link else ""
    return people + barra


def vendor_strip(base, heading=True):
    tiles = []
    for key, name in VENDORS:
        logo = None
        for ext in ("svg", "png", "webp"):
            rel = f"assets/img/fabricantes/{key}.{ext}"
            if os.path.exists(os.path.join(ROOT, rel)):
                logo = f'<img src="{base}{rel}" alt="{e(name)}"{img_size(rel)} loading="lazy">'
        if not logo and key == "mcloud":
            logo = f'<span class="vendor-own">{isotipo("mcloud-" + str(len(tiles)))}<span>MCloud</span></span>'
        tiles.append(f'<li class="vendor{" has-logo" if logo else ""}" title="{e(name)}">{logo or f"<span>{e(name)}</span>"}</li>')
    head = '''<div class="vendors-head"><h3>Fabricantes y plataformas</h3><p>Tecnología que implantamos y gestionamos a diario.</p></div>''' if heading else ""
    return f'''
        <div class="vendors">{head}<ul class="vendor-grid">{"".join(tiles)}</ul></div>'''


def about_home():
    return f'''
    <section class="section section-white" id="nosotros" aria-labelledby="nosotros-title">
      <div class="wrap">
        <div class="about-v2">
          <div class="about-copy">
            <p class="eyebrow">Nosotros</p>
            <h2 id="nosotros-title">Un equipo técnico cercano, en Barcelona y Madrid</h2>
            <p>M&amp;G Corporate Consulting es una consultora tecnológica especializada en la gestión externalizada de sistemas: ciberseguridad, operación y auditoría de infraestructuras IT.</p>
            <p>Tenemos oficina en Barcelona y técnicos en Madrid, donde también trabajamos con clientes. Conocemos a cada cliente por su nombre, sabemos cómo está montado su entorno y respondemos nosotros, sin intermediarios.</p>
            <ul class="about-facts">
              <li><span class="care-ico">{ICON["pin"]}</span><span><small>Oficina en Barcelona</small>{e(ADDRESS)}</span></li>
              <li><span class="care-ico">{ICON["pin"]}</span><span><small>Madrid</small>{e(MADRID)}</span></li>
              <li><span class="care-ico">{ICON["building"]}</span><span><small>Especialidad</small>Servicios IT gestionados para empresas y despachos</span></li>
              <li><span class="care-ico">{ICON["cloud"]}</span><span><small>Ámbito</small>Infraestructura local, cloud (Azure, Google Cloud y MCloud) y Microsoft 365</span></li>
            </ul>
            <a class="btn btn-dark" href="nosotros.html">Conoce M&amp;G {ICON["arrow"]}</a>
          </div>
          {team_panel("")}
        </div>
        {vendor_strip("")}
      </div>
    </section>'''

# --------------------------------------------------------------------------
# Portada
# --------------------------------------------------------------------------
def build_home():
    def media(s):
        for ext in ("webp", "jpg", "png"):
            rel = f'assets/img/servicios/{s["slug"]}.{ext}'
            if os.path.exists(os.path.join(ROOT, rel)):
                return f'<img src="{rel}" alt="" loading="lazy" width="800" height="450">'
        return ilus.art(s["slug"])

    services = "".join(f'''
          <a class="svc-card" href="servicios/{s["slug"]}.html">
            <div class="svc-card-media">{media(s)}<span class="svc-card-tag">{e(ilus.TAG[s["slug"]])}</span></div>
            <div class="svc-card-body">
              <h3>{e(s["name"])}</h3>
              <p>{e(s["short"])}</p>
              <ul class="svc-card-chips">{"".join(f"<li>{e(x)}</li>" for x in [i for _, items in s["tech"] for i in items][:3])}</ul>
              <span class="service-more">Ver servicio {ICON["arrow"]}</span>
            </div>
          </a>''' for s in SERVICES)

    body = f'''
    <section class="hero-scene" aria-roledescription="carrusel" aria-label="Presentación de M&amp;G" data-carousel>
      {hero_media()}
      <div class="hero-shade" aria-hidden="true"></div>
      <div class="wrap hero-inner">
        <div class="slides" aria-live="off">
          <div class="slide is-active" role="group" aria-roledescription="diapositiva" aria-label="1 de 4" data-scene="0">
            <h1 class="slide-title">Tecnología y servicios diseñados para tu negocio</h1>
            <p class="hero-lead">Somos el equipo IT de tu empresa: diseñamos, implantamos y gestionamos tu infraestructura para que funcione cada día, esté protegida y crezca contigo.</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="contacto.html#formulario">Solicitar una auditoría {ICON["arrow"]}</a>
              <a class="btn btn-outline-light" href="#servicios">Ver servicios</a>
            </div>
          </div>
          <div class="slide" role="group" aria-roledescription="diapositiva" aria-label="2 de 4" data-scene="1">
            <h2 class="slide-title">Soporte cercano, sin intermediarios</h2>
            <p class="hero-lead">Técnicos que conocen tu entorno y atienden a tus usuarios desde Barcelona y Madrid, en remoto y en persona cuando hace falta.</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="contacto.html#formulario">Hablemos {ICON["arrow"]}</a>
              <a class="btn btn-outline-light" href="#nosotros">Conócenos</a>
            </div>
          </div>
          <div class="slide" role="group" aria-roledescription="diapositiva" aria-label="3 de 4" data-scene="2">
            <h2 class="slide-title">Tu infraestructura vigilada las 24 horas</h2>
            <p class="hero-lead">Monitorizamos servidores, copias, red y Microsoft 365 para actuar antes de que notes un problema.</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="#mgcare">Descubrir MGCare {ICON["arrow"]}</a>
              <a class="btn btn-outline-light" href="contacto.html#formulario">Pedir propuesta</a>
            </div>
          </div>
          <div class="slide" role="group" aria-roledescription="diapositiva" aria-label="4 de 4" data-scene="3">
            <h2 class="slide-title">Cloud e inteligencia artificial sin riesgos</h2>
            <p class="hero-lead">Azure, Google Cloud o nuestro cloud privado MCloud, y Copilot en Microsoft 365 con tus datos protegidos y los permisos en orden.</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="servicios/cloud.html">Descubrir Cloud {ICON["arrow"]}</a>
              <a class="btn btn-outline-light" href="servicios/transformacion-digital.html">IA con Microsoft</a>
            </div>
          </div>
        </div>

        <div class="carousel-bar">
          <div class="carousel-tabs" role="tablist" aria-label="Elegir diapositiva">
            <button role="tab" aria-selected="true" data-go="0"><span>Consultoría IT</span><i class="progress"><b></b></i></button>
            <button role="tab" aria-selected="false" data-go="1" tabindex="-1"><span>Soporte cercano</span><i class="progress"><b></b></i></button>
            <button role="tab" aria-selected="false" data-go="2" tabindex="-1"><span>MGCare 24/7</span><i class="progress"><b></b></i></button>
            <button role="tab" aria-selected="false" data-go="3" tabindex="-1"><span>Cloud e IA</span><i class="progress"><b></b></i></button>
          </div>
          <span class="city-chip" aria-hidden="true"><i></i><b data-city-label>Barcelona</b></span>
          <button class="carousel-pause" type="button" aria-label="Pausar presentación" data-pause>
            <svg class="i-pause" viewBox="0 0 16 16" aria-hidden="true"><rect x="4" y="3" width="2.6" height="10" rx="1"/><rect x="9.4" y="3" width="2.6" height="10" rx="1"/></svg>
            <svg class="i-play" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.2v9.6a.6.6 0 0 0 .9.5l7.4-4.8a.6.6 0 0 0 0-1L5.9 2.7a.6.6 0 0 0-.9.5Z"/></svg>
          </button>
        </div>
      </div>
    </section>

    <section class="section" id="servicios" aria-labelledby="servicios-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="servicios-title">Todo lo que tu empresa necesita en IT</h2>
          <p>Desde un proyecto concreto hasta la gestión completa de tus sistemas. Cada servicio se puede contratar por separado o combinado.</p>
        </header>
        <div class="svc-cards">{services}
        </div>
      </div>
    </section>

    <section class="section section-dark noc-section" id="mgcare" aria-labelledby="mgcare-title">
      <canvas class="noc-canvas" data-noc aria-hidden="true"></canvas>
      <div class="noc-shade" aria-hidden="true"></div>
      <div class="wrap">
        <div class="care-top">
          <div>
            <h2 id="mgcare-title">MGCare, tu departamento IT externo</h2>
            <p>Una cuota mensual que cubre el soporte a tus usuarios y la gestión continua de tus sistemas, estén en tu oficina, en la nube o en Microsoft 365.</p>
            <ul class="care-points">
              <li><span class="care-ico">{ICON["radar"]}</span><span><strong>Detección temprana</strong>Detectamos los problemas antes de que los notes.</span></li>
              <li><span class="care-ico">{ICON["ticket"]}</span><span><strong>Todo registrado</strong>Cada incidencia queda registrada y con seguimiento.</span></li>
              <li><span class="care-ico">{ICON["chart"]}</span><span><strong>Informes a demanda</strong>Informes de actividad y estado cuando los necesites.</span></li>
            </ul>
          </div>
          <div>
            <div class="console" role="img" aria-label="Ejemplo de panel de monitorización: cuatro servicios correctos y un aviso de disco con ticket abierto automáticamente">
              <div class="console-bar"><span class="console-title">Estado de la infraestructura</span><span class="console-live"><i></i>En vivo</span></div>
              <ul class="checks" data-checks>
                <li data-state="ok"><span class="dot"></span><span class="check-name">Servidores</span><span class="check-meta">12/12 activos</span></li>
                <li data-state="ok"><span class="dot"></span><span class="check-name">Copias de seguridad</span><span class="check-meta">Última: 03:00</span></li>
                <li data-state="ok"><span class="dot"></span><span class="check-name">Microsoft 365</span><span class="check-meta">Sin incidencias</span></li>
                <li data-state="warn"><span class="dot"></span><span class="check-name">Disco NAS-01</span><span class="check-meta">82 % ocupado</span></li>
                <li data-state="ok"><span class="dot"></span><span class="check-name">Firewall y VPN</span><span class="check-meta">Operativo</span></li>
              </ul>
              <div class="console-foot"><span class="console-ticket">Ticket abierto automáticamente</span><span>Comprobado hace <b data-ago>0</b> s</span></div>
            </div>
            <p class="console-caption">Panel de ejemplo con datos ilustrativos.</p>
          </div>
        </div>

        <div class="scopes">
          <div class="scope"><h3><span class="care-ico">{ICON["building"]}</span>En tu oficina</h3><p>Servidores, red, copias y puestos de trabajo.</p>
            <ul><li>Monitorización 24/7 con alertas</li><li>Parches y actualizaciones planificadas</li><li>Revisión periódica de copias</li><li>Inventario de equipos</li></ul></div>
          <div class="scope"><h3><span class="care-ico">{ICON["cloud"]}</span>En la nube</h3><p>Servidores y servicios alojados en cloud.</p>
            <ul><li>Rendimiento y disponibilidad</li><li>Accesos y seguridad</li><li>Control de costes mensual</li><li>Recuperación ante desastres</li></ul></div>
          <div class="scope"><h3><span class="care-ico">{ICON["apps"]}</span>En Microsoft 365</h3><p>Correo, Teams, SharePoint y OneDrive.</p>
            <ul><li>Usuarios y licencias</li><li>Políticas de seguridad</li><li>Resolución de incidencias</li><li>Informes de uso</li></ul></div>
        </div>

        <div class="helpdesk">
          <span class="helpdesk-ico">{ICON["headset"]}</span><div><h3>HelpDesk para todo tu equipo</h3><p>Tus usuarios abren una petición por correo, teléfono o portal y un técnico la atiende con tiempos de respuesta acordados.</p></div>
          <a class="btn btn-dark" href="contacto.html#formulario">Pedir una propuesta</a>
        </div>
      </div>
    </section>

    <section class="section section-white" aria-labelledby="sectores-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="sectores-title">Para quién trabajamos</h2>
          <p>Empresas de sectores muy distintos que necesitan que su tecnología funcione siempre. <a class="link" href="clientes.html">Ver todos los clientes</a></p>
        </header>
        <div class="sector-tiles">{"".join(f'<a class="sector-tile" href="clientes/{c["slug"]}.html">{sector_icon(c)}<span><strong>{e(c["name"])}</strong><small>{e(c["short"])}</small></span></a>' for c in SECTORS)}</div>
      </div>
    </section>

{method_block("")}

{about_home()}
    <section class="section" aria-labelledby="casos-home-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="casos-home-title">Casos de éxito</h2>
          <p>Proyectos reales de M&amp;G para notarías, despachos y empresas. <a class="link" href="casos-de-exito.html">Ver todos los casos</a></p>
        </header>
        <div class="cases-grid">{"".join(case_card(c, "") for c in (sorted(CASES, key=lambda c: ["notaria-monitorizacion", "moda-red-tiendas", "industria-continuidad", "despacho-servicio-gestionado"].index(c["slug"]) if c["slug"] in ["notaria-monitorizacion", "moda-red-tiendas", "industria-continuidad", "despacho-servicio-gestionado"] else 99))[:4])}</div>
      </div>
    </section>
{faq_block(HOME_FAQS, "Preguntas frecuentes", 'Si no encuentras tu respuesta, <a class="link" href="contacto.html#formulario">escríbenos</a>.')}

{cta_band("")}
'''

    org = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "M&G Consulting", "legalName": "M&G Corporate Consulting S.L.",
        "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "image": SITE + "/assets/img/og-image.jpg",
        "@id": SITE + "/#organization", "email": EMAIL, "taxID": "B22878243",
        "sameAs": ["https://www.linkedin.com/company/myg-corporate-consulting/"],
        "address": {"@type": "PostalAddress", "streetAddress": "Ronda de Sant Pere, 17", "postalCode": "08010", "addressLocality": "Barcelona", "addressCountry": "ES"},
        "areaServed": [{"@type": "City", "name": "Barcelona"}, {"@type": "City", "name": "Madrid"}, {"@type": "Country", "name": "España"}],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servicios IT",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f'{SITE}/servicios/{s["slug"]}.html'}} for s in SERVICES]},
    }
    return page("index.html", "M&G Consulting | Consultoría IT y servicios gestionados en Barcelona y Madrid",
                "Diseñamos, implantamos y gestionamos la infraestructura IT de tu empresa: ciberseguridad, cloud, Microsoft 365, soporte y monitorización. Barcelona y Madrid.",
                body, jsonld=[org, {"@context": "https://schema.org", "@type": "WebSite", "name": "M&G Consulting", "url": SITE + "/", "inLanguage": "es-ES", "publisher": {"@id": SITE + "/#organization"}}, faq_ld(HOME_FAQS)], scripts=("noc.js",))


# --------------------------------------------------------------------------
# Páginas de servicio
# --------------------------------------------------------------------------
def build_service(s):
    b = "../"
    g = GEM[s["gem"]]
    overview = "".join(f"<p>{e(p)}</p>" for p in s["overview"])
    fit = "".join(f'<li>{mcheck()}{e(f)}</li>' for f in s["fit"])
    tone = TONE[s["gem"]]
    inc = "".join(f'<li><span class="svc-icon {tone}" aria-hidden="true">{ICON[pick_icon(t, d)]}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in s["includes"])
    tech = "".join(
        f'<div class="tech-group"><h3>{e(title)}</h3><ul>{"".join(tech_item(x, b) for x in items)}</ul></div>'
        for title, items in s["tech"])
    steps = "".join(f"<li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d in s["process"])
    deliv = "".join(f'<li>{mcheck()}{e(d)}</li>' for d in s["deliverables"])
    rel = "".join(f'<a href="{o["slug"]}.html">{svc_icon(o)}{e(o["name"].split(" · ")[0])}</a>' for o in SERVICES if o is not s)
    hero_chips = "".join(f"<li>{e(x)}</li>" for _, items in s["tech"] for x in items[:2])
    probs = "".join(f'<li><p class="prob">{e(p)}</p><p class="sol"><span class="sol-ico">{ICON["arrow"]}</span>{e(r)}</p></li>' for p, r in PROBLEMS.get(s["slug"], []))
    mod_icons = ["chart", "headset", "radar"]
    mods = "".join(f'<div class="mode"><span class="care-ico">{ICON[mod_icons[i % 3]]}</span><h3>{e(m)}</h3><p>{e(d)}</p></div>' for i, (m, d) in enumerate(MODALITIES))
    case = CASE_BY_SLUG.get(RELATED_CASE.get(s["slug"], ""))
    case_html = ""
    if case:
        case_html = f"""
    <section class="section" aria-labelledby="caso-title">
      <div class="wrap">
        <a class="case-feature" href="{b}casos/{case["slug"]}.html">
          <div class="case-feature-media">{case_media(case, b, "-feat")}<span class="svc-card-tag">{e(case["sector"])}</span></div>
          <div class="case-feature-body">
            <p class="eyebrow">Caso de éxito</p>
            <h2 id="caso-title">{e(case["title"])}</h2>
            <p>{e(case["summary"])}</p>
            <ul class="case-tags">{"".join(f"<li>{e(x)}</li>" for x in case["services"])}</ul>
            <span class="service-more">Leer el caso {ICON["arrow"]}</span>
          </div>
        </a>
      </div>
    </section>"""
    catalog_cta = ""
    if s["slug"] in ("suministro-it", "microsoft-365", "cloud"):
        catalog_cta = f'<a class="btn btn-outline-light" href="{b}catalogo.html">Ver catálogo y precios</a>'
    subnav = """
    <nav class="subnav" aria-label="En esta página"><div class="wrap"><ul>
      <li><a href="#resumen-title">Resumen</a></li><li><a href="#retos-title">Retos</a></li><li><a href="#incluye-title">Qué incluye</a></li>
      <li><a href="#tech-title">Tecnologías</a></li><li><a href="#proceso-title">Método</a></li><li><a href="#contratar-title">Cómo contratar</a></li><li><a href="#faq-title">Preguntas</a></li>
    </ul></div></nav>"""

    spot = ""
    sp = s.get("spotlight")
    if sp:
        pts = "".join(f'<li><span class="care-ico">{ICON[pick_icon(p)]}</span>{e(p)}</li>' for p in sp["points"])
        cta = ""
        if sp.get("cta"):
            label, href = sp["cta"]
            cta = f'<a class="btn btn-primary" href="{MCLOUD_URL if href == "MCLOUD" else href}" rel="noopener">{e(label)} {ICON["arrow"]}</a>'
        spot = f'''
    <section class="section section-dark spotlight-section" aria-labelledby="spot-title">
      <div class="wrap spotlight">
        <div>
          <h2 id="spot-title">{e(sp["title"])}</h2>
          <p>{e(sp["text"])}</p>
          {cta}
        </div>
        <ul class="spot-points">{pts}</ul>
      </div>
    </section>'''

    body = f'''
    <section class="page-hero page-hero-split" aria-labelledby="page-title" data-scene-host>
      <canvas class="page-canvas" data-skyline data-variant="page" aria-hidden="true"></canvas>
      <div class="wrap">
        <div class="hero-split-copy">
        <ol class="crumbs"><li><a href="{b}index.html">Inicio</a></li><li><a href="{b}index.html#servicios">Servicios</a></li><li aria-current="page">{e(s["name"])}</li></ol>
        <h1 id="page-title">{e(s["title"])}</h1>
        <p class="hero-lead">{e(s["lead"])}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{b}contacto.html#formulario">Solicitar información {ICON["arrow"]}</a>
          {catalog_cta or '<a class="btn btn-outline-light" href="#incluye-title">Qué incluye</a>'}
        </div>
        <ul class="hero-chips" aria-label="Tecnologías principales">{hero_chips}</ul>
        </div>
        <div class="hero-art" aria-hidden="true">{ilus.art(s["slug"]).replace('svc-' + s["slug"], 'hero-' + s["slug"])}<span class="svc-card-tag">{e(ilus.TAG[s["slug"]])}</span></div>
      </div>
    </section>
{subnav}

    <section class="section section-white" aria-labelledby="resumen-title">
      <div class="wrap detail">
        <div class="overview">
          <h2 id="resumen-title">{e(s["name"])} en M&amp;G</h2>
          {overview}
        </div>
        <aside class="aside-card" aria-labelledby="encaja-title">
          <h2 id="encaja-title">Te encaja si…</h2>
          <ul>{fit}</ul>
          <a class="btn btn-dark" href="{b}contacto.html#formulario">Hablar con un técnico</a>
        </aside>
      </div>
    </section>

    <section class="section section-dark" aria-labelledby="retos-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="retos-title">Retos que resolvemos</h2>
          <p>Situaciones que vemos a menudo y cómo las abordamos.</p>
        </header>
        <ul class="problems">{probs}</ul>
      </div>
    </section>

    <section class="section" aria-labelledby="incluye-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="incluye-title">Qué incluye</h2>
          <p>Puedes contratar el servicio completo o solo las partes que necesites.</p>
        </header>
        <ul class="includes{" includes-3" if len(s["includes"]) % 3 == 0 and len(s["includes"]) % 4 else ""}">{inc}</ul>
      </div>
    </section>
{spot}
    <section class="section section-white" aria-labelledby="tech-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="tech-title">Tecnologías con las que trabajamos</h2>
          <p>Fabricantes y plataformas que implantamos y gestionamos a diario en este servicio.</p>
        </header>
        <div class="tech-groups">{tech}</div>
      </div>
    </section>

    <section class="section" aria-labelledby="proceso-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="proceso-title">Cómo lo hacemos</h2>
          <p>Un método claro, con un responsable técnico de principio a fin.</p>
        </header>
        <ol class="steps steps-cards">{steps}</ol>
        <div class="deliverables">
          <h3>Qué recibes</h3>
          <ul>{deliv}</ul>
        </div>
      </div>
    </section>
    <section class="section section-white" aria-labelledby="contratar-title">
      <div class="wrap">
        <header class="section-head">
          <h2 id="contratar-title">Cómo contratarlo</h2>
          <p>Elige la fórmula que mejor encaja con tu empresa. Se pueden combinar.</p>
        </header>
        <div class="modes">{mods}</div>
      </div>
    </section>
{case_html}
{faq_block(s["faqs"], "Preguntas frecuentes", "Sobre " + e(s["name"]) + ". Si tienes otra duda, " + f'<a class="link" href="{b}contacto.html#formulario">escríbenos</a>.', white=True)}

    <section class="section" aria-labelledby="otros-title">
      <div class="wrap">
        <h2 id="otros-title">Otros servicios</h2>
        <div class="related">{rel}</div>
      </div>
    </section>
{cta_band(b)}'''
    ld = [
        {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["lead"],
         "serviceType": s["name"],
         "provider": {"@type": "ProfessionalService", "name": "M&G Consulting", "url": SITE + "/"}, "areaServed": "ES",
         "url": f'{SITE}/servicios/{s["slug"]}.html',
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": s["name"],
             "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "description": d}} for t, d in s["includes"]]}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Servicios", "item": SITE + "/#servicios"},
            {"@type": "ListItem", "position": 3, "name": s["name"], "item": f'{SITE}/servicios/{s["slug"]}.html'}]},
        faq_ld(s["faqs"]),
    ]
    return page(f'servicios/{s["slug"]}.html', f'{s["name"]} para empresas en Barcelona y Madrid | M&G Consulting', s["lead"], body,
                current="servicios", base=b, jsonld=ld)



# --------------------------------------------------------------------------
# Casos de éxito
# --------------------------------------------------------------------------
def case_media(c, base, uid=""):
    for ext in ("webp", "jpg", "png"):
        rel = f'assets/img/casos/{c["slug"]}.{ext}'
        if os.path.exists(os.path.join(ROOT, rel)):
            return f'<img src="{base}{rel}" alt="" loading="lazy" width="800" height="450">'
    img = c.get("image", "")
    if img.startswith("svc:"):
        return ilus.ART[img[4:]]("case-" + c["slug"] + uid)
    return ilus.sector_art(c.get("sector_key", "pymes"), "case-" + c["slug"] + uid)


_card_n = [0]


def case_card(c, base):
    _card_n[0] += 1
    tags = "".join(f"<li>{e(x)}</li>" for x in c["services"])
    return f'''
          <a class="case-card" href="{base}casos/{c["slug"]}.html">
            <div class="case-card-media">{case_media(c, base, "-" + str(_card_n[0]))}<span class="svc-card-tag">{e(c["sector"])}</span></div>
            <div class="case-card-body">
            <span class="case-meta">{e(c["place"])}</span>
            <h3>{e(c["title"])}</h3>
            <p>{e(c["summary"])}</p>
            <ul class="case-tags">{tags}</ul>
            <span class="service-more">Leer el caso {ICON["arrow"]}</span>
            </div>
          </a>'''


def build_cases():
    body = f'''
    <section class="page-hero" aria-labelledby="page-title" data-scene-host>
      <canvas class="page-canvas" data-skyline data-variant="page" aria-hidden="true"></canvas>
      <div class="wrap">
        <ol class="crumbs"><li><a href="index.html">Inicio</a></li><li><a href="clientes.html">Clientes</a></li><li aria-current="page">Casos de éxito</li></ol>
        <h1 id="page-title">Casos de éxito</h1>
        <p class="hero-lead">Así ayudamos a notarías, despachos y empresas a trabajar con una tecnología más segura, ordenada y fiable.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap"><div class="cases-grid">{"".join(case_card(c, "") for c in CASES)}</div></div>
    </section>
{cta_band("", "¿Quieres que tu proyecto sea el siguiente?", "Cuéntanos tu situación y te proponemos cómo abordarla.")}'''
    out = [page("casos-de-exito.html", "Casos de éxito de consultoría IT y servicios gestionados | M&G",
                "Proyectos reales de M&G Consulting: monitorización, servicio gestionado, Microsoft 365 e integraciones para notarías, despachos y empresas.",
                body, current="clientes")]
    for c in CASES:
        out.append(build_case(c))
    return out


def build_case(c):
    b = "../"
    sol = "".join(f'<li>{mcheck()}{e(x)}</li>' for x in c["solution"])
    res = "".join(f"<li>{mcheck()}{e(x)}</li>" for x in c["results"])
    stack = "".join(tech_item(x, b) for x in c["stack"])
    chips = "".join(f"<li>{e(x)}</li>" for x in c["services"])
    others = "".join(case_card(o, b) for o in CASES if o is not c)
    body = f'''
    <section class="page-hero page-hero-split" aria-labelledby="page-title" data-scene-host>
      <canvas class="page-canvas" data-skyline data-variant="page" aria-hidden="true"></canvas>
      <div class="wrap">
        <div class="hero-split-copy">
        <ol class="crumbs"><li><a href="{b}index.html">Inicio</a></li><li><a href="{b}clientes.html">Clientes</a></li><li><a href="{b}casos-de-exito.html">Casos de éxito</a></li><li aria-current="page">{e(c["sector"])}</li></ol>
        <p class="case-meta case-meta-light">{e(c["sector"])} · {e(c["place"])}</p>
        <h1 id="page-title">{e(c["title"])}</h1>
        <p class="hero-lead">{e(c["summary"])}</p>
        <ul class="hero-chips">{chips}</ul>
        </div>
        <div class="hero-art" aria-hidden="true">{case_media(c, b, "-hero")}<span class="svc-card-tag">{e(c["sector"])}</span></div>
      </div>
    </section>
    <section class="section section-white">
      <div class="wrap case-body">
        <div class="case-main">
          <h2>El reto</h2>
          <p>{e(c["challenge"])}</p>
          <h2>Qué hicimos</h2>
          <ul class="case-list">{sol}</ul>
        </div>
        <aside class="case-side">
          <div class="case-results">
            <h2>Resultados</h2>
            <ul>{res}</ul>
          </div>
          <div class="case-stack">
            <h2>Tecnologías</h2>
            <ul>{stack}</ul>
          </div>
        </aside>
      </div>
    </section>
    <section class="section" aria-labelledby="otros-casos">
      <div class="wrap">
        <h2 id="otros-casos">Otros casos</h2>
        <div class="cases-grid">{others}</div>
      </div>
    </section>
{cta_band(b)}'''
    return page(f'casos/{c["slug"]}.html', f'{c["title"]} | Casos de éxito M&G', c["summary"], body, current="clientes", base=b,
                noindex=bool(c.get("ejemplo")),
                jsonld=[crumbs_ld(("Inicio", ""), ("Casos de éxito", "casos-de-exito.html"), (c["title"], f'casos/{c["slug"]}.html'))])


# --------------------------------------------------------------------------
# Catálogo
# --------------------------------------------------------------------------
def build_catalog():
    skeletons = "<div class='product skeleton' aria-hidden='true'></div>" * 6
    body = f'''
    <section class="page-hero page-hero-compact" aria-labelledby="page-title" data-scene-host>
      <canvas class="page-canvas" data-skyline data-variant="page" aria-hidden="true"></canvas>
      <div class="wrap">
        <ol class="crumbs"><li><a href="index.html">Inicio</a></li><li aria-current="page">Catálogo</li></ol>
        <h1 id="page-title">Catálogo de productos y servicios</h1>
        <p class="hero-lead">Licencias, cloud, seguridad, redes y equipos con los que trabajamos. Añade lo que te interese y te enviamos un presupuesto a medida.</p>
      </div>
    </section>

    <section class="section catalog-section">
      <div class="wrap catalog is-loading" data-catalog data-base="" data-api="api/catalogo.php" data-fallback="data/catalogo.json">
        <p class="catalog-demo" data-demo hidden>Precios y productos de ejemplo. Se sustituirán por los del catálogo real de M&amp;G.</p>
        <div class="catalog-tools">
          <label class="search"><span class="visually-hidden">Buscar en el catálogo</span>
            <svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m14 14 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <input type="search" placeholder="Buscar: Microsoft 365, firewall, NAS…" data-q autocomplete="off">
          </label>
          <label class="select"><span class="visually-hidden">Fabricante</span><select data-brand></select></label>
          <label class="select"><span class="visually-hidden">Ordenar</span>
            <select data-sort>
              <option value="destacados">Destacados</option>
              <option value="precio-asc">Precio: de menor a mayor</option>
              <option value="precio-desc">Precio: de mayor a menor</option>
              <option value="nombre">Nombre</option>
            </select></label>
        </div>
        <div class="chips" data-cats role="group" aria-label="Categorías"></div>
        <div class="catalog-status"><span data-count aria-live="polite">Cargando…</span><span data-updated></span></div>
        <div class="product-grid" data-grid>{skeletons}</div>
        <div class="catalog-more"><button type="button" class="btn btn-outline" data-more hidden>Ver más</button></div>
        <p class="catalog-note">Precios sin IVA, por usuario y mes salvo que se indique otra cosa. Los precios de los fabricantes pueden variar; confirmamos siempre el importe final en la propuesta.</p>
      </div>
    </section>

    <aside class="tray" data-tray data-contact="contacto.html#formulario" hidden aria-label="Tu solicitud de presupuesto">
      <button type="button" class="tray-toggle" data-tray-toggle aria-expanded="false">Tu solicitud <b data-tray-count>0</b></button>
      <div class="tray-panel">
        <ul data-tray-list></ul>
        <button type="button" class="btn btn-primary" data-tray-send>Solicitar presupuesto {ICON["arrow"]}</button>
      </div>
    </aside>'''
    return page("catalogo.html", "Catálogo de productos y precios | M&G Consulting",
                "Catálogo de licencias Microsoft 365, cloud y MCloud, seguridad, redes, almacenamiento y servidores de M&G Consulting.",
                body, current="catalogo", scripts=("catalogo.js",))


# --------------------------------------------------------------------------
# Formulario de contacto (reutilizable)
# --------------------------------------------------------------------------
def contact_section(base, heading="Hablemos de tu infraestructura", white=True):
    topics = "".join(f"<option>{e(s['name'])}</option>" for s in SERVICES)
    return f'''
    <section class="section{' section-white' if white else ''}" id="formulario" aria-labelledby="contacto-title">
      <div class="wrap contact">
        <div class="contact-copy">
          <h2 id="contacto-title">{e(heading)}</h2>
          <p>Cuéntanos qué necesitas y te propondremos una reunión para conocer tu entorno.</p>
          <ul class="contact-list">
            <li>{ICON["mail"]}<span>Correo</span><a class="link" href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{ICON["pin"]}<span>Oficina en Barcelona</span>{e(ADDRESS)}</li>
            <li>{ICON["pin"]}<span>Madrid</span>{e(MADRID)}</li>
            <li>{ICON["clock"]}<span>Horario</span>Lunes a viernes</li>
          </ul>
        </div>
        <form class="form" id="contact-form" action="{base}contacto.php" method="post" novalidate>
          <div class="field"><label for="f-name">Nombre</label><input id="f-name" name="nombre" type="text" autocomplete="name" required maxlength="120"><span class="field-error" id="f-name-err"></span></div>
          <div class="field"><label for="f-company">Empresa <span class="opt">(opcional)</span></label><input id="f-company" name="empresa" type="text" autocomplete="organization" maxlength="120"></div>
          <div class="field"><label for="f-email">Correo electrónico</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="160"><span class="field-error" id="f-email-err"></span></div>
          <div class="field"><label for="f-phone">Teléfono <span class="opt">(opcional)</span></label><input id="f-phone" name="telefono" type="tel" autocomplete="tel" maxlength="30"></div>
          <div class="field field-full"><label for="f-topic">¿En qué podemos ayudarte?</label>
            <select id="f-topic" name="asunto"><option>Auditoría de infraestructura</option>{topics}<option>Catálogo y presupuesto</option><option>Otro</option></select></div>
          <div class="field field-full"><label for="f-msg">Mensaje</label><textarea id="f-msg" name="mensaje" rows="5" required maxlength="5000" placeholder="Número de usuarios, sedes, qué te preocupa…"></textarea><span class="field-error" id="f-msg-err"></span></div>
          <div class="hp" aria-hidden="true"><label for="f-web">No rellenar</label><input id="f-web" name="web" type="text" tabindex="-1" autocomplete="off"></div>
          <input type="hidden" name="ts" value="">
          <label class="consent field-full"><input type="checkbox" id="f-consent" name="consentimiento" value="si" required><span>He leído y acepto la <a class="link" href="{base}legal/privacidad.html">política de privacidad</a>.</span></label>
          <div class="form-foot field-full">
            <button type="submit" class="btn btn-primary">Enviar mensaje {ICON["arrow"]}</button>
            <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
          </div>
        </form>
      </div>
    </section>'''


def page_hero(base, crumbs, title, lead="", extra="", compact=False, art="", tag=""):
    items = "".join(f'<li><a href="{base}{href}">{e(label)}</a></li>' for label, href in crumbs[:-1])
    items += f'<li aria-current="page">{e(crumbs[-1][0])}</li>'
    return f'''
    <section class="page-hero{' page-hero-compact' if compact else ''}{' page-hero-split' if art else ''}" aria-labelledby="page-title" data-scene-host>
      <canvas class="page-canvas" data-skyline data-variant="page" aria-hidden="true"></canvas>
      <div class="wrap">
        <div class="hero-split-copy">
        <ol class="crumbs"><li><a href="{base}index.html">Inicio</a></li>{items}</ol>
        <h1 id="page-title">{e(title)}</h1>
        {f'<p class="hero-lead">{e(lead)}</p>' if lead else ''}
        {extra}
        </div>
        {f'<div class="hero-art" aria-hidden="true">{art}{f"<span class=svc-card-tag>{e(tag)}</span>" if tag else ""}</div>' if art else ''}
      </div>
    </section>'''


def build_contact():
    body = page_hero("", [("Contacto", "")], "Contacto",
                     "Escríbenos o ven a vernos a nuestra oficina de Barcelona. También tenemos técnicos en Madrid. Te responderemos lo antes posible.", compact=True)
    body += contact_section("", "Cuéntanos qué necesitas")
    return page("contacto.html", "Contacto y solicitud de auditoría IT | M&G Consulting",
                "Cuéntanos qué necesita tu empresa y te respondemos con una propuesta. Consultoría IT y servicios gestionados en Barcelona y Madrid.", body, current="contacto",
                jsonld=[{"@context": "https://schema.org", "@type": "ContactPage", "name": "Contacto", "url": SITE + "/contacto.html",
                         "about": {"@type": "ProfessionalService", "name": "M&G Consulting", "url": SITE + "/", "email": EMAIL}},
                        crumbs_ld(("Inicio", ""), ("Contacto", "contacto.html"))])


# --------------------------------------------------------------------------
# Nosotros
# --------------------------------------------------------------------------
def build_about():
    vendors = ["Microsoft 365", "Azure", "Google Cloud", "MCloud", "HPE", "QNAP", "Synology",
               "Aruba Networking", "Ubiquiti", "Fortinet", "SonicWall", "Microsoft Copilot"]
    body = page_hero("", [("Nosotros", "")], "Un equipo técnico cercano, en Barcelona y Madrid",
                     "Somos una consultora tecnológica especializada en la gestión externalizada de sistemas: ciberseguridad, operación y auditoría de infraestructuras IT.")
    body += f'''
    <section class="section section-white">
      <div class="wrap about">
        <div>
          <h2>Tecnología con visión de negocio</h2>
          <p>No solo implantamos tecnología: la alineamos con los objetivos de cada cliente. Combinamos experiencia en cloud, ciberseguridad e infraestructura para optimizar costes, mejorar la eficiencia y permitir que las empresas crezcan con seguridad.</p>
          <p>Desde nuestra oficina de Barcelona y con técnicos en Madrid atendemos a clientes en las dos ciudades y, en remoto, en toda España. Conocemos a nuestros clientes por su nombre, sabemos cómo está montado cada entorno y respondemos nosotros, sin intermediarios.</p>
        </div>
        <dl class="facts">
          <div><dt>Oficina en Barcelona</dt><dd>{e(ADDRESS)}</dd></div>
          <div><dt>Madrid</dt><dd>{e(MADRID)}</dd></div>
          <div><dt>Especialidad</dt><dd>Servicios IT gestionados para pymes y despachos profesionales</dd></div>
          <div><dt>Ámbito</dt><dd>Infraestructura local, cloud (Azure, Google Cloud y MCloud) y Microsoft 365</dd></div>
        </dl>
      </div>
      <div class="wrap">
        <figure class="office-photo">
          <img src="assets/img/edificio-barcelona.webp" alt="Edificio de oficinas en la Ronda de Sant Pere, Barcelona, donde está la oficina de M&amp;G" width="1024" height="683" loading="lazy">
          <figcaption><span class="care-ico">{ICON["pin"]}</span><span><strong>Nuestra oficina en Barcelona</strong>{e(ADDRESS)}</span></figcaption>
          <small class="photo-credit">Foto: <a href="https://www.flickr.com/photos/yeagovc/25351097037/" target="_blank" rel="noopener noreferrer">yeagov_c / Flickr</a></small>
        </figure>
      </div>
    </section>

    <section class="section" aria-labelledby="valores-title">
      <div class="wrap">
        <header class="section-head"><h2 id="valores-title">Cómo entendemos nuestro trabajo</h2><p>Tres ideas que guían cada proyecto y cada servicio.</p></header>
        <div class="modes">
          <div class="mode"><span class="care-ico">{ICON["chart"]}</span><h3>Enfoque en el negocio</h3><p>Cada recomendación parte de cómo trabaja tu empresa y de lo que quiere conseguir.</p></div>
          <div class="mode"><span class="care-ico">{ICON["shield"]}</span><h3>Seguridad y escalabilidad</h3><p>Diseñamos entornos que protegen la información y crecen contigo sin rehacerlo todo.</p></div>
          <div class="mode"><span class="care-ico">{ICON["headset"]}</span><h3>Acompañamiento continuo</h3><p>No desaparecemos tras el proyecto: seguimos a tu lado para operar y mejorar.</p></div>
        </div>
      </div>
    </section>

{method_block("", white=True)}

    <section class="section" aria-labelledby="fab-title">
      <div class="wrap">
        <header class="section-head"><h2 id="fab-title">Nuestro equipo</h2><p>Especialistas por área y un único punto de contacto para ti.</p></header>
        {"" if EQUIPO.get("personas") else f'<div class="team-wide">{team_panel("")}</div>'}
        {people_cards("")}
        {vendor_strip("")}
      </div>
    </section>
{cta_band("")}'''
    return page("nosotros.html", "Sobre M&G Consulting: equipo IT en Barcelona y Madrid",
                "M&G Consulting es una consultora tecnológica con oficina en Barcelona y técnicos en Madrid, especializada en servicios IT gestionados, ciberseguridad y cloud.",
                body, current="nosotros",
                jsonld=[{"@context": "https://schema.org", "@type": "AboutPage", "name": "Sobre M&G Consulting", "url": SITE + "/nosotros.html",
                         "about": {"@type": "ProfessionalService", "name": "M&G Consulting", "url": SITE + "/"}},
                        crumbs_ld(("Inicio", ""), ("Nosotros", "nosotros.html"))])


# --------------------------------------------------------------------------
# Clientes: portada de clientes y páginas por sector
# --------------------------------------------------------------------------
def sector_card(sec, base):
    return f'''
          <a class="sector-card" href="{base}clientes/{sec["slug"]}.html">
            {sector_icon(sec)}
            <h3>{e(sec["name"])}</h3>
            <p>{e(sec["short"])}</p>
            <span class="service-more">Ver más {ICON["arrow"]}</span>
          </a>'''


def build_clients():
    body = page_hero("", [("Clientes", "")], "Nuestros clientes",
                     "Servicios profesionales, industria, logística, moda, alimentación y pymes de cualquier sector: empresas que necesitan que su tecnología funcione siempre.")
    body += f'''
    <section class="section" aria-labelledby="tipos-title">
      <div class="wrap">
        <header class="section-head"><h2 id="tipos-title">Tipos de clientes</h2><p>Cada sector tiene sus propias exigencias. Así las abordamos.</p></header>
        {"".join(f'<h3 class="group-title">{e(g)}</h3><div class="sector-grid">{"".join(sector_card(s, "") for s in SECTORS if s["group"] == g)}</div>' for g in GROUPS)}

      </div>
    </section>
    <section class="section section-white" aria-labelledby="casos-title">
      <div class="wrap">
        <header class="section-head"><h2 id="casos-title">Casos de éxito</h2><p><a class="link" href="casos-de-exito.html">Ver todos los casos</a></p></header>
        <div class="cases-grid">{"".join(case_card(c, "") for c in CASES)}</div>
      </div>
    </section>
{cta_band("")}'''
    out = [page("clientes.html", "Consultoría IT para notarías, gestorías, industria y pymes | M&G",
                "Consultoría IT para notarías, gestorías, corredurías de seguros, industria, maquinaria, logística, moda y textil, alimentación y pymes de cualquier sector.", body, current="clientes")]
    for sec in SECTORS:
        out.append(build_sector(sec))
    return out


def build_sector(sec):
    b = "../"
    by = {s["slug"]: s for s in SERVICES}
    ch = "".join(f'<li><p class="prob">{e(t)}</p><p class="sol"><span class="sol-ico">{ICON["arrow"]}</span>{e(d)}</p></li>' for t, d in sec["challenges"])
    svcs = "".join(
        f'<a class="svc-row" href="{b}servicios/{slug}.html">{svc_icon(by[slug])}<span><strong>{e(by[slug]["name"])}</strong><small>{e(by[slug]["short"])}</small></span>{ICON["arrow"]}</a>'
        for slug in sec["services"] if slug in by)
    cases = "".join(case_card(CASE_BY_SLUG[c], b) for c in sec["cases"] if c in CASE_BY_SLUG)
    cases_block = (f'<div class="cases-grid">{cases}</div>' if cases else
                   f'<p class="other-sectors">Consulta nuestros <a class="link" href="{b}casos-de-exito.html">casos de éxito</a> en otros sectores o <a class="link" href="{b}contacto.html#formulario">cuéntanos tu proyecto</a>.</p>')
    body = page_hero(b, [("Clientes", "clientes.html"), (sec["name"], "")], sec["title"], sec["lead"],
                     art=ilus.sector_art(sec["slug"], "hero-sec-" + sec["slug"]), tag=sec["name"])
    body += f'''
    <section class="section section-dark" aria-labelledby="retos-title">
      <div class="wrap">
        <header class="section-head"><h2 id="retos-title">Lo que más importa en tu sector</h2><p>Y cómo lo resolvemos.</p></header>
        <ul class="problems plain">{ch}</ul>
      </div>
    </section>
    <section class="section section-white" aria-labelledby="svc-title">
      <div class="wrap">
        <header class="section-head"><h2 id="svc-title">Servicios recomendados</h2><p>Los que más utilizan clientes como tú.</p></header>
        <div class="svc-list">{svcs}</div>
      </div>
    </section>
    <section class="section" aria-labelledby="casos-title">
      <div class="wrap">
        <header class="section-head"><h2 id="casos-title">Casos de éxito</h2><p><a class="link" href="{b}casos-de-exito.html">Ver todos los casos</a></p></header>
        {cases_block}
      </div>
    </section>
{cta_band(b)}'''
    return page(f'clientes/{sec["slug"]}.html', f'{sec["title"]} en Barcelona y Madrid | M&G Consulting', sec["lead"], body,
                current="clientes", base=b,
                jsonld=[crumbs_ld(("Inicio", ""), ("Clientes", "clientes.html"), (sec["name"], f'clientes/{sec["slug"]}.html'))])


# --------------------------------------------------------------------------
# Noticias
# --------------------------------------------------------------------------
MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fdate(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} de {MONTHS[int(m) - 1]} de {y}"


def news_card(n, base):
    return f'''
          <a class="news-card" href="{base}noticias/{n["slug"]}.html">
            <span class="case-meta">{e(n["category"])} · <time datetime="{n["date"]}">{fdate(n["date"])}</time></span>
            <h3>{e(n["title"])}</h3>
            <p>{e(n["summary"])}</p>
            <span class="service-more">Leer más {ICON["arrow"]}</span>
          </a>'''


def build_news():
    body = page_hero("", [("Noticias", "")], "Noticias",
                     "Novedades tecnológicas que afectan a tu empresa, explicadas en lenguaje claro.", compact=True)
    body += f'''
    <section class="section">
      <div class="wrap"><div class="news-grid">{"".join(news_card(n, "") for n in NEWS)}</div></div>
    </section>'''
    out = [page("noticias.html", "Noticias de Microsoft 365, ciberseguridad y cloud | M&G",
                "Artículos y novedades sobre Microsoft 365, ciberseguridad, cloud e inteligencia artificial para empresas.", body, current="noticias")]
    for n in NEWS:
        b = "../"
        paras = "".join(f"<p>{e(p)}</p>" for p in n["body"])
        more = "".join(news_card(o, b) for o in NEWS if o is not n)[:]
        art = page_hero(b, [("Noticias", "noticias.html"), (n["category"], "")], n["title"], n["summary"],
                        extra=f'<p class="case-meta case-meta-light"><time datetime="{n["date"]}">{fdate(n["date"])}</time></p>')
        art += f'''
    <section class="section section-white">
      <div class="wrap"><article class="prose article">{paras}
        <p><a class="btn btn-dark" href="{b}contacto.html#formulario">Hablar con un técnico</a></p></article></div>
    </section>
    <section class="section" aria-labelledby="mas-title">
      <div class="wrap"><h2 id="mas-title">Más noticias</h2><div class="news-grid">{more}</div></div>
    </section>'''
        ld = [{"@context": "https://schema.org", "@type": "NewsArticle", "headline": n["title"], "datePublished": n["date"],
               "description": n["summary"], "publisher": {"@type": "Organization", "name": "M&G Consulting",
               "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/icon-512.png"}}}]
        out.append(page(f'noticias/{n["slug"]}.html', f'{n["title"]} | M&G Consulting', n["summary"], art,
                        current="noticias", base=b, jsonld=ld + [crumbs_ld(("Inicio", ""), ("Noticias", "noticias.html"), (n["title"], f'noticias/{n["slug"]}.html'))]))
    return out


# --------------------------------------------------------------------------
# Páginas simples: legales, gracias, 404
# --------------------------------------------------------------------------
LEGAL_NOTE = '<p><em>Borrador para revisar por el asesor legal de M&amp;G antes de publicar.</em></p>'
TITULAR = f'<p>Titular: M&amp;G Corporate Consulting S.L. · CIF B22878243 · {e(ADDRESS)} · <a href="mailto:{EMAIL}">{EMAIL}</a></p>'

LEGAL = {
    "aviso-legal": ("Aviso legal", f'''{LEGAL_NOTE}
      <h2>Datos identificativos</h2>{TITULAR}
      <p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se facilitan los datos del titular de este sitio web. Añadir aquí los datos de inscripción en el Registro Mercantil.</p>
      <h2>Condiciones de uso</h2><p>El acceso a este sitio web es gratuito y atribuye la condición de usuario, que acepta estas condiciones. El usuario se compromete a hacer un uso adecuado de los contenidos.</p>
      <h2>Propiedad intelectual</h2><p>Los contenidos, marcas y logotipos de este sitio son propiedad de M&amp;G Corporate Consulting S.L. o de terceros que han autorizado su uso. Las marcas de terceros citadas pertenecen a sus respectivos titulares.</p>
      <h2>Responsabilidad</h2><p>M&amp;G no se hace responsable del mal uso de los contenidos ni de los daños derivados del acceso a sitios de terceros enlazados desde esta web.</p>
      <h2>Legislación aplicable</h2><p>Este aviso se rige por la legislación española.</p>'''),
    "privacidad": ("Política de privacidad", f'''{LEGAL_NOTE}
      <h2>Responsable del tratamiento</h2>{TITULAR}
      <h2>Qué datos tratamos y para qué</h2><p>Los datos que nos envías mediante el formulario de contacto (nombre, empresa, correo, teléfono y mensaje) se usan únicamente para responder a tu consulta y, si procede, enviarte una propuesta.</p>
      <h2>Base legal</h2><p>Tu consentimiento, que otorgas al marcar la casilla del formulario, y la aplicación de medidas precontractuales a petición tuya.</p>
      <h2>Conservación</h2><p>Conservamos los datos mientras sea necesario para atender tu solicitud y durante los plazos legales aplicables.</p>
      <h2>Destinatarios</h2><p>No cedemos tus datos a terceros salvo obligación legal. Nuestro proveedor de alojamiento y correo actúa como encargado del tratamiento.</p>
      <h2>Tus derechos</h2><p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. También puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>'''),
    "cookies": ("Política de cookies", f'''{LEGAL_NOTE}
      <h2>¿Usa cookies esta web?</h2><p>Esta web no utiliza cookies de análisis, publicidad ni de terceros. Las tipografías se sirven desde nuestro propio servidor, sin conexiones a servicios externos.</p>
      <p>Si en el futuro se incorpora alguna herramienta de analítica, se actualizará esta política y se solicitará tu consentimiento antes de instalar cualquier cookie no técnica.</p>'''),
}


def simple(path, title, h1, lead, inner, base, noindex=False, desc=None):
    body = f'''
    <section class="page-hero" data-scene-host>
      <canvas class="page-canvas" data-skyline data-variant="page" aria-hidden="true"></canvas>
      <div class="wrap"><h1>{e(h1)}</h1>{f'<p class="hero-lead">{lead}</p>' if lead else ''}</div>
    </section>
    <section class="section section-white"><div class="wrap prose">{inner}</div></section>'''
    return page(path, title, desc or h1, body, base=base, noindex=noindex)


def build_misc():
    out = []
    for slug, (t, inner) in LEGAL.items():
        out.append(simple(f"legal/{slug}.html", f"{t} | M&G Consulting", t, "", inner, "../", noindex=True))
    out.append(simple("gracias.html", "Mensaje enviado | M&G Consulting", "Mensaje enviado",
                      "Gracias por escribirnos. Te responderemos lo antes posible.",
                      '<p><a class="btn btn-dark" href="index.html">Volver al inicio</a></p>', "", noindex=True))
    out.append(simple("404.html", "Página no encontrada | M&G Consulting", "No encontramos esta página",
                      "Puede que la dirección haya cambiado con la nueva web.",
                      '<p>Prueba desde la <a href="/index.html">página de inicio</a> o revisa nuestros <a href="/index.html#servicios">servicios</a>.</p>', "/", noindex=True))
    return out


def build_sitemap(paths):
    urls = "".join(
        f'\n  <url><loc>{SITE}/{"" if p == "index.html" else p}</loc><lastmod>{TODAY}</lastmod></url>'
        for p in paths)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}\n</urlset>\n')


if __name__ == "__main__":
    public = [build_home()] + [build_service(s) for s in SERVICES] + build_cases() + [build_catalog(), build_contact(), build_about()] + build_clients() + build_news()
    build_misc()
    build_sitemap(public)
    print("Generadas:", len(public), "páginas públicas + legales, gracias y 404")
