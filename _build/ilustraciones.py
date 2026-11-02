"""
Ilustraciones SVG de cada servicio (cabecera de las tarjetas de la portada).
Estilo de marca: fondo azul marino y piezas en naranja, ámbar y amarillo.

Para usar una FOTO en lugar de la ilustración, guarda la imagen como
assets/img/servicios/<slug>.jpg (o .webp) y regenera: se usará la foto.
"""

O, A, S, N, N2, N3, W = "#F98A47", "#FEAF3F", "#FFC35F", "#101C30", "#16263F", "#22385C", "#FFFFFF"


def _frame(uid, inner):
    return f'''<svg viewBox="0 0 400 225" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="bg-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{N}"/><stop offset="1" stop-color="{N2}"/></linearGradient>
  <radialGradient id="gl-{uid}" cx=".72" cy=".35" r=".6"><stop offset="0" stop-color="{O}" stop-opacity=".28"/><stop offset="1" stop-color="{O}" stop-opacity="0"/></radialGradient>
  <pattern id="pt-{uid}" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M14 2 26 14 14 26 2 14Z" fill="none" stroke="#fff" stroke-opacity=".05"/></pattern>
</defs>
<rect width="400" height="225" fill="url(#bg-{uid})"/>
<rect width="400" height="225" fill="url(#pt-{uid})"/>
<rect width="400" height="225" fill="url(#gl-{uid})"/>
{inner}
</svg>'''


def mgcare(u):
    bars = "".join(f'<rect x="{150 + i * 16}" y="{128 - h}" width="10" height="{h}" rx="2" fill="{c}"/>'
                   for i, (h, c) in enumerate([(22, A), (34, O), (28, A), (46, S), (38, O), (52, S), (30, A)]))
    return _frame(u, f'''
<rect x="118" y="46" width="164" height="112" rx="10" fill="{N3}" stroke="#fff" stroke-opacity=".12"/>
<rect x="132" y="60" width="60" height="6" rx="3" fill="#fff" fill-opacity=".5"/>
<circle cx="258" cy="63" r="4" fill="#3DD68C"/><circle cx="244" cy="63" r="4" fill="#3DD68C"/><circle cx="230" cy="63" r="4" fill="{S}"/>
<line x1="132" y1="132" x2="268" y2="132" stroke="#fff" stroke-opacity=".15"/>
{bars}
<rect x="186" y="158" width="28" height="14" fill="{N3}"/><rect x="166" y="172" width="68" height="6" rx="3" fill="{N3}"/>
<g transform="translate(290 118)"><circle r="30" fill="{O}"/>
<path d="M-13 3v-4a13 13 0 0 1 26 0v4" fill="none" stroke="{N}" stroke-width="3.2" stroke-linecap="round"/>
<rect x="-16" y="1" width="7" height="12" rx="2.5" fill="{N}"/><rect x="9" y="1" width="7" height="12" rx="2.5" fill="{N}"/></g>
<g transform="translate(62 96)"><rect width="74" height="44" rx="8" fill="#fff"/>
<rect x="10" y="10" width="36" height="5" rx="2.5" fill="{N}" fill-opacity=".7"/><rect x="10" y="20" width="54" height="4" rx="2" fill="{N}" fill-opacity=".25"/>
<rect x="10" y="29" width="22" height="7" rx="3.5" fill="{S}"/></g>''')


def ciberseguridad(u):
    bricks = "".join(f'<rect x="{x}" y="{y}" width="38" height="14" rx="2" fill="{N3}" stroke="#fff" stroke-opacity=".08"/>'
                     for y, off in [(172, 0), (188, 19), (204, 0)] for x in range(-20 + off, 420, 40))
    return _frame(u, f'''
{bricks}
<path d="M200 38 142 60v38c0 36 25 62 58 72 33-10 58-36 58-72V60Z" fill="{O}"/>
<path d="M200 38v132c33-10 58-36 58-72V60Z" fill="{A}"/>
<path d="m176 104 17 17 33-35" fill="none" stroke="{N}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
<g fill="none" stroke="{S}" stroke-opacity=".6" stroke-width="1.5" stroke-dasharray="3 5">
<path d="M142 80H70M258 80h72M150 128H90M250 128h60"/></g>
<g fill="{S}"><circle cx="66" cy="80" r="5"/><circle cx="334" cy="80" r="5"/><circle cx="86" cy="128" r="5"/><circle cx="314" cy="128" r="5"/></g>
<g transform="translate(318 44)"><rect x="-12" y="-2" width="24" height="18" rx="3" fill="#fff"/><path d="M-7 -2v-5a7 7 0 0 1 14 0v5" fill="none" stroke="#fff" stroke-width="3"/></g>''')


def cloud(u):
    servers = "".join(f'''<g transform="translate({x} 150)"><rect width="56" height="40" rx="6" fill="{N3}" stroke="#fff" stroke-opacity=".12"/>
<rect x="8" y="9" width="40" height="7" rx="2" fill="#fff" fill-opacity=".14"/><rect x="8" y="23" width="40" height="7" rx="2" fill="#fff" fill-opacity=".14"/>
<circle cx="42" cy="12.5" r="2" fill="#3DD68C"/><circle cx="42" cy="26.5" r="2" fill="{c}"/></g>'''
                      for x, c in [(96, S), (172, "#3DD68C"), (248, S)])
    return _frame(u, f'''
<path d="M140 118h128a30 30 0 0 0 4-59.7A44 44 0 0 0 188 48a34 34 0 0 0-50 26 22 22 0 0 0 2 44Z" fill="{A}"/>
<path d="M168 118h100a30 30 0 0 0 4-59.7A44 44 0 0 0 214 36a44 44 0 0 1-8 82Z" fill="{O}"/>
<g stroke="{S}" stroke-width="2" stroke-dasharray="3 5" fill="none"><path d="M124 150v-14h76v-18M200 150v-32M276 150v-14h-76"/></g>
{servers}
<circle cx="330" cy="60" r="22" fill="{S}"/><text x="330" y="65" text-anchor="middle" font-family="Sora, sans-serif" font-weight="700" font-size="13" fill="{N}">M</text>''')


def microsoft365(u):
    tiles = "".join(f'<rect x="{x}" y="{y}" width="42" height="42" rx="10" fill="{c}"/>'
                    for x, y, c in [(118, 58, O), (166, 58, A), (118, 106, A), (166, 106, S)])
    return _frame(u, f'''
{tiles}
<g transform="translate(232 54)"><rect width="84" height="104" rx="8" fill="#fff"/>
<rect x="12" y="14" width="44" height="6" rx="3" fill="{N}" fill-opacity=".75"/>
<rect x="12" y="30" width="60" height="4" rx="2" fill="{N}" fill-opacity=".2"/><rect x="12" y="40" width="54" height="4" rx="2" fill="{N}" fill-opacity=".2"/>
<rect x="12" y="50" width="60" height="4" rx="2" fill="{N}" fill-opacity=".2"/><rect x="12" y="66" width="40" height="22" rx="4" fill="{S}" fill-opacity=".6"/></g>
<g transform="translate(62 128)"><rect width="66" height="40" rx="12" fill="{N3}" stroke="#fff" stroke-opacity=".15"/><path d="M14 40l-4 12 16-12" fill="{N3}"/>
<circle cx="20" cy="20" r="3.5" fill="#fff"/><circle cx="33" cy="20" r="3.5" fill="#fff"/><circle cx="46" cy="20" r="3.5" fill="#fff"/></g>
<path d="M326 44l4 11 11 4-11 4-4 11-4-11-11-4 11-4z" fill="{S}"/>''')


def proyectos(u):
    units = "".join(f'''<g transform="translate(150 {y})"><rect width="100" height="20" rx="3" fill="{N3}" stroke="#fff" stroke-opacity=".12"/>
<rect x="8" y="7" width="46" height="6" rx="2" fill="#fff" fill-opacity=".14"/>
<circle cx="80" cy="10" r="2.5" fill="{c1}"/><circle cx="89" cy="10" r="2.5" fill="{c2}"/></g>'''
                    for y, c1, c2 in [(52, "#3DD68C", S), (76, "#3DD68C", "#3DD68C"), (100, S, "#3DD68C"), (124, "#3DD68C", "#3DD68C"), (148, "#3DD68C", S)])
    return _frame(u, f'''
<rect x="140" y="40" width="120" height="146" rx="8" fill="none" stroke="{O}" stroke-width="3"/>
{units}
<rect x="146" y="186" width="12" height="10" fill="{O}"/><rect x="242" y="186" width="12" height="10" fill="{O}"/>
<g transform="translate(318 96)" fill="none" stroke-linecap="round" stroke-width="4">
<path d="M-26-8a38 38 0 0 1 52 0" stroke="{S}"/><path d="M-16 4a24 24 0 0 1 32 0" stroke="{A}"/><circle cy="16" r="4" fill="{O}" stroke="none"/></g>
<g transform="translate(58 104)"><rect width="56" height="22" rx="4" fill="{A}"/>
<g fill="{N}">{"".join(f'<rect x="{6 + i * 9}" y="12" width="5" height="5" rx="1"/>' for i in range(5))}</g></g>
<g stroke="{S}" stroke-width="2" stroke-dasharray="3 5"><path d="M114 115h36M250 115h38"/></g>''')


def suministro(u):
    return _frame(u, f'''
<g transform="translate(64 112)"><rect width="70" height="54" rx="4" fill="{A}"/><rect x="-4" width="78" height="16" rx="3" fill="{O}"/>
<rect x="27" y="16" width="16" height="38" fill="{S}" fill-opacity=".7"/></g>
<g transform="translate(82 66)"><rect width="54" height="42" rx="4" fill="{S}"/><rect x="-3" width="60" height="12" rx="3" fill="{A}"/></g>
<g transform="translate(164 64)"><rect width="140" height="90" rx="8" fill="{N3}" stroke="#fff" stroke-opacity=".15"/>
<rect x="10" y="10" width="120" height="70" rx="4" fill="{N}"/>
<rect x="22" y="24" width="50" height="6" rx="3" fill="#fff" fill-opacity=".6"/><rect x="22" y="38" width="80" height="4" rx="2" fill="#fff" fill-opacity=".2"/>
<rect x="22" y="48" width="70" height="4" rx="2" fill="#fff" fill-opacity=".2"/><circle cx="112" cy="60" r="8" fill="#3DD68C"/>
<path d="m108 60 3 3 5-6" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>
<path d="M150 154h168l10 12H140z" fill="#3A5178"/>
<g transform="translate(300 40) rotate(8)"><rect width="66" height="42" rx="6" fill="#fff"/><rect x="8" y="9" width="28" height="5" rx="2.5" fill="{N}" fill-opacity=".7"/>
<rect x="8" y="20" width="46" height="4" rx="2" fill="{N}" fill-opacity=".2"/><circle cx="52" cy="30" r="6" fill="{O}"/></g>''')


def transformacion(u):
    nodes = [(92, 70, O), (92, 150, A), (200, 110, S), (308, 70, A), (308, 150, O)]
    lines = "".join(f'<path d="M{x1 + 24} {y1}C{(x1 + x2) / 2} {y1} {(x1 + x2) / 2} {y2} {x2 - 24} {y2}" fill="none" stroke="{S}" stroke-width="2" stroke-dasharray="3 5"/>'
                    for (x1, y1, _), (x2, y2, _) in [(nodes[0], nodes[2]), (nodes[1], nodes[2]), (nodes[2], nodes[3]), (nodes[2], nodes[4])])
    boxes = "".join(f'<rect x="{x - 24}" y="{y - 20}" width="48" height="40" rx="10" fill="{c}"/>' for x, y, c in nodes if (x, y) != (200, 110))
    return _frame(u, f'''
{lines}
{boxes}
<g fill="{N}"><rect x="80" y="64" width="24" height="4" rx="2"/><rect x="80" y="72" width="16" height="4" rx="2"/>
<rect x="80" y="144" width="24" height="4" rx="2"/><rect x="80" y="152" width="16" height="4" rx="2"/>
<path d="m298 70 6 6 12-12" fill="none" stroke="{N}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="m298 150 6 6 12-12" fill="none" stroke="{N}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></g>
<circle cx="200" cy="110" r="36" fill="{N3}" stroke="{S}" stroke-width="2"/>
<path d="M200 88l6 16 16 6-16 6-6 16-6-16-16-6 16-6z" fill="{S}"/>
<path d="M226 80l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="{O}"/>''')


ART = {
    "mgcare": mgcare, "ciberseguridad": ciberseguridad, "cloud": cloud, "microsoft-365": microsoft365,
    "proyectos-it": proyectos, "suministro-it": suministro, "transformacion-digital": transformacion,
}

TAG = {
    "mgcare": "Servicio gestionado", "ciberseguridad": "Seguridad", "cloud": "Cloud",
    "microsoft-365": "Productividad", "proyectos-it": "Infraestructura",
    "suministro-it": "Equipos y licencias", "transformacion-digital": "IA y automatización",
}


def art(slug):
    return ART[slug]("svc-" + slug)


# ----------------------------------------------------------------------------
# Ilustraciones de las fases de "Cómo trabajamos"
# ----------------------------------------------------------------------------
def fase_auditoria(u):
    rows = "".join(f'''<g transform="translate(0 {i * 26})"><rect x="152" y="78" width="14" height="14" rx="3" fill="{c}"/>
<rect x="176" y="81" width="{w}" height="8" rx="4" fill="{N}" fill-opacity=".25"/></g>''' for i, (c, w) in enumerate([("#3DD68C", 70), ("#3DD68C", 56), (S, 76), (O, 48)]))
    return _frame(u, f'''
<rect x="136" y="46" width="128" height="160" rx="12" fill="#fff"/>
<rect x="176" y="38" width="48" height="16" rx="6" fill="{A}"/>
<rect x="152" y="60" width="60" height="8" rx="4" fill="{N}" fill-opacity=".75"/>
{rows}
<g transform="translate(278 132)"><circle r="34" fill="none" stroke="{O}" stroke-width="8"/><circle r="26" fill="{O}" fill-opacity=".15"/>
<path d="M24 24 44 44" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M-12 4l-4 0 6-14 6 22 6-12h10" fill="none" stroke="{S}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>
<g transform="translate(64 120)"><rect width="52" height="18" rx="4" fill="{N3}" stroke="#fff" stroke-opacity=".15"/><rect y="24" width="52" height="18" rx="4" fill="{N3}" stroke="#fff" stroke-opacity=".15"/>
<circle cx="42" cy="9" r="2.5" fill="#3DD68C"/><circle cx="42" cy="33" r="2.5" fill="{S}"/></g>''')


def fase_plan(u):
    ms = [(80, O, "Fase 1"), (170, A, "Fase 2"), (260, S, "Fase 3")]
    stones = "".join(f'''<g transform="translate({x} 112)"><circle r="16" fill="{c}"/><path d="m-6 0 4 4 8-8" fill="none" stroke="{N}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="-34" y="30" width="68" height="44" rx="8" fill="#fff"/><rect x="-24" y="40" width="30" height="6" rx="3" fill="{N}" fill-opacity=".7"/>
<rect x="-24" y="52" width="46" height="4" rx="2" fill="{N}" fill-opacity=".2"/><rect x="-24" y="60" width="36" height="4" rx="2" fill="{N}" fill-opacity=".2"/></g>''' for x, c, _ in ms)
    return _frame(u, f'''
<path d="M40 112H360" stroke="{S}" stroke-width="3" stroke-dasharray="6 7" stroke-linecap="round"/>
{stones}
<g transform="translate(340 112)"><circle r="18" fill="{N3}" stroke="{S}" stroke-width="2"/><path d="M-5-9v18M-5-9h12l-3 5 3 5H-5" fill="{O}" stroke="{O}" stroke-width="2" stroke-linejoin="round"/></g>
<g transform="translate(150 30)"><rect width="100" height="44" rx="8" fill="{N3}" stroke="#fff" stroke-opacity=".12"/>
<text x="14" y="28" font-family="Sora, sans-serif" font-size="15" font-weight="700" fill="{S}">€</text>
<rect x="34" y="14" width="50" height="6" rx="3" fill="#fff" fill-opacity=".55"/><rect x="34" y="26" width="36" height="5" rx="2.5" fill="#fff" fill-opacity=".2"/></g>''')


def fase_implantacion(u):
    return _frame(u, f'''
<g transform="translate(120 48)"><rect width="110" height="132" rx="8" fill="none" stroke="{O}" stroke-width="3"/>
{"".join(f'<g transform="translate(9 {10 + i * 24})"><rect width="92" height="18" rx="3" fill="{N3}" stroke="#fff" stroke-opacity=".12"/><rect x="8" y="6" width="40" height="6" rx="2" fill="#fff" fill-opacity=".15"/><circle cx="80" cy="9" r="2.5" fill="{c}"/></g>' for i, c in enumerate(["#3DD68C", "#3DD68C", "#3DD68C", S, "#3DD68C"]))}</g>
<g transform="translate(252 64)"><rect width="104" height="70" rx="10" fill="#fff"/>
<rect x="12" y="14" width="54" height="7" rx="3.5" fill="{N}" fill-opacity=".75"/>
<rect x="12" y="32" width="80" height="10" rx="5" fill="{N}" fill-opacity=".1"/><rect x="12" y="32" width="58" height="10" rx="5" fill="{O}"/>
<text x="12" y="60" font-family="Sora, sans-serif" font-size="10" font-weight="600" fill="{N}" fill-opacity=".6">72 %</text></g>
<g transform="translate(300 170) rotate(-35)"><rect x="-4" y="-26" width="8" height="40" rx="3" fill="{A}"/><path d="M-14-30a14 14 0 0 1 28 0l-7 4v6h-14v-6z" fill="{S}"/></g>
<g stroke="{S}" stroke-width="2" stroke-dasharray="3 5"><path d="M230 100h22"/></g>''')


FASES = {"auditoria": fase_auditoria, "plan": fase_plan, "implantacion": fase_implantacion, "gestion": mgcare}


# ----------------------------------------------------------------------------
# Ilustraciones por tipo de cliente (cabecera de los casos de éxito)
# ----------------------------------------------------------------------------
def _doc(x, y, w=70, h=90, lines=4):
    ls = "".join(f'<rect x="{x + 10}" y="{y + 22 + i * 12}" width="{w - 20 - (i % 2) * 14}" height="4" rx="2" fill="{N}" fill-opacity=".2"/>' for i in range(lines))
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#fff"/><rect x="{x + 10}" y="{y + 10}" width="{w * .5}" height="6" rx="3" fill="{N}" fill-opacity=".7"/>{ls}'


def sec_notarias(u):
    return _frame(u, f'''
{_doc(120, 50, 92, 120, 5)}
<g transform="translate(196 146)"><circle r="26" fill="{O}"/><circle r="18" fill="none" stroke="{N}" stroke-width="2.5" stroke-dasharray="4 3"/><path d="m-7 0 5 5 9-10" fill="none" stroke="{N}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>
<g transform="translate(250 66)"><rect width="70" height="22" rx="4" fill="{N3}" stroke="#fff" stroke-opacity=".15"/><rect y="28" width="70" height="22" rx="4" fill="{N3}" stroke="#fff" stroke-opacity=".15"/><rect y="56" width="70" height="22" rx="4" fill="{N3}" stroke="#fff" stroke-opacity=".15"/>
<circle cx="58" cy="11" r="3" fill="#3DD68C"/><circle cx="58" cy="39" r="3" fill="#3DD68C"/><circle cx="58" cy="67" r="3" fill="{S}"/></g>
<path d="M212 110h38" stroke="{S}" stroke-width="2" stroke-dasharray="3 5"/>''')


def sec_gestorias(u):
    return _frame(u, f'''
{_doc(96, 62, 70, 92)}{_doc(112, 50, 70, 92)}
<g transform="translate(206 70)"><rect width="104" height="80" rx="8" fill="{A}"/><rect x="36" y="-12" width="32" height="16" rx="5" fill="none" stroke="{A}" stroke-width="5"/>
<rect y="30" width="104" height="8" fill="{O}"/><rect x="44" y="26" width="16" height="16" rx="3" fill="{S}"/></g>
<g transform="translate(316 60)"><rect width="38" height="50" rx="6" fill="{N3}" stroke="#fff" stroke-opacity=".15"/><rect x="6" y="6" width="26" height="10" rx="2" fill="{S}" fill-opacity=".8"/>
{"".join(f'<circle cx="{11 + (i % 3) * 8}" cy="{26 + (i // 3) * 9}" r="2.4" fill="#fff" fill-opacity=".5"/>' for i in range(6))}</g>''')


def sec_corredurias(u):
    return _frame(u, f'''
<g transform="translate(150 60)"><path d="M0 50a60 60 0 0 1 120 0Z" fill="{O}"/><path d="M60 -10v10M60 50v52a12 12 0 0 1-24 0" fill="none" stroke="{S}" stroke-width="5" stroke-linecap="round"/>
<path d="M0 50c10-8 20-8 30 0 10-8 20-8 30 0 10-8 20-8 30 0 10-8 20-8 30 0" fill="{A}"/></g>
<g transform="translate(64 120)"><rect width="66" height="44" rx="6" fill="#fff"/><path d="m6 8 27 18 27-18" fill="none" stroke="{N}" stroke-opacity=".5" stroke-width="3"/></g>
<g transform="translate(300 128)"><path d="M0-30 24-20v16c0 16-11 28-24 32-13-4-24-16-24-32v-16Z" fill="{N3}" stroke="{S}" stroke-width="2"/><path d="m-8 0 6 6 11-12" fill="none" stroke="{S}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>''')


def sec_industria(u):
    gear = lambda cx, cy, r, c: f'<g transform="translate({cx} {cy})"><circle r="{r}" fill="{c}"/>' + "".join(f'<rect x="{-r * .18}" y="{-r * 1.25}" width="{r * .36}" height="{r * .4}" rx="2" fill="{c}" transform="rotate({a})"/>' for a in range(0, 360, 45)) + f'<circle r="{r * .38}" fill="{N}"/></g>'
    return _frame(u, f'''
<path d="M70 190V110l50 28v-28l50 28v-28l50 28V70h30v120Z" fill="{N3}" stroke="#fff" stroke-opacity=".15"/>
{"".join(f'<rect x="{88 + i * 42}" y="160" width="18" height="12" rx="2" fill="{S}" fill-opacity=".8"/>' for i in range(4))}
<rect x="226" y="52" width="18" height="22" fill="{N3}"/><circle cx="235" cy="42" r="8" fill="#fff" fill-opacity=".12"/><circle cx="246" cy="28" r="11" fill="#fff" fill-opacity=".08"/>
{gear(300, 90, 28, O)}{gear(336, 140, 18, A)}''')


def sec_maquinaria(u):
    return _frame(u, f'''
<g transform="translate(110 70)"><rect x="0" y="40" width="90" height="56" rx="6" fill="{A}"/><path d="M14 40V8h40l18 32" fill="none" stroke="{O}" stroke-width="7" stroke-linejoin="round"/>
<rect x="96" y="-6" width="8" height="110" rx="3" fill="{S}"/><rect x="104" y="80" width="46" height="8" rx="3" fill="{S}"/>
<circle cx="22" cy="104" r="16" fill="{N}" stroke="{S}" stroke-width="5"/><circle cx="72" cy="104" r="16" fill="{N}" stroke="{S}" stroke-width="5"/></g>
<g transform="translate(300 70) rotate(40)"><rect x="-5" y="0" width="10" height="70" rx="4" fill="#fff" fill-opacity=".85"/><path d="M-16 -4a16 16 0 1 1 32 0l-8 4V8h-16V0Z" fill="#fff" fill-opacity=".85"/></g>''')


def sec_logistica(u):
    boxes = "".join(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="3" fill="{c}"/><path d="M{x + s / 2} {y}v{s * .35}" stroke="{N}" stroke-opacity=".35" stroke-width="3"/>' for x, y, s, c in [(92, 96, 40, A), (140, 104, 32, O), (180, 92, 44, S), (232, 100, 36, A)])
    return _frame(u, f'''
{boxes}
<rect x="76" y="138" width="232" height="16" rx="8" fill="{N3}" stroke="#fff" stroke-opacity=".2"/>
{"".join(f'<circle cx="{92 + i * 40}" cy="146" r="4" fill="#fff" fill-opacity=".4"/>' for i in range(6))}
<path d="M100 154v28M284 154v28" stroke="{N3}" stroke-width="6"/>
<g transform="translate(296 60)"><rect width="56" height="34" rx="6" fill="#fff"/><rect x="8" y="9" width="24" height="5" rx="2.5" fill="{N}" fill-opacity=".7"/>
<rect x="8" y="20" width="38" height="4" rx="2" fill="{N}" fill-opacity=".2"/><circle cx="46" cy="11" r="4" fill="#3DD68C"/></g>''')


def sec_moda(u):
    return _frame(u, f'''
<path d="M70 70h120M90 70v-6a10 10 0 1 1 10-10" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="3" stroke-linecap="round"/>
<g transform="translate(100 74)"><path d="M14 0 0 8l-6 20 14 6v54h56V34l14-6-6-20L58 0a14 14 0 0 1-44 0Z" fill="{O}"/>
<path d="M14 0a14 14 0 0 0 44 0" fill="none" stroke="{N}" stroke-opacity=".3" stroke-width="3"/></g>
<g transform="translate(224 64)"><rect width="122" height="110" rx="6" fill="{N3}" stroke="#fff" stroke-opacity=".15"/>
<path d="M0 0h122v22c-10 8-20 8-30 0-10 8-20 8-31 0-10 8-20 8-30 0-10 8-21 8-31 0Z" fill="{A}"/>
<rect x="14" y="40" width="44" height="70" rx="3" fill="{S}" fill-opacity=".85"/><rect x="70" y="40" width="38" height="34" rx="3" fill="#fff" fill-opacity=".2"/>
<circle cx="50" cy="76" r="3" fill="{N}"/></g>''')


def sec_alimentacion(u):
    return _frame(u, f'''
<g transform="translate(120 84)"><path d="M0 22h120l-12 74H12Z" fill="{A}"/><path d="M30 22 52-12M90 22 68-12" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<circle cx="34" cy="10" r="14" fill="{O}"/><circle cx="60" cy="4" r="16" fill="{S}"/><circle cx="88" cy="12" r="13" fill="#3DD68C" fill-opacity=".85"/>
{"".join(f'<path d="M{30 + i * 20} 40v40" stroke="{N}" stroke-opacity=".25" stroke-width="4" stroke-linecap="round"/>' for i in range(4))}</g>
<g transform="translate(286 70)"><rect width="66" height="44" rx="6" fill="#fff"/><rect x="8" y="9" width="30" height="5" rx="2.5" fill="{N}" fill-opacity=".7"/>
<path d="M8 32h8l5-10 6 16 5-8h26" fill="none" stroke="{O}" stroke-width="2.5" stroke-linejoin="round"/></g>''')


def sec_pymes(u):
    return _frame(u, f'''
<g transform="translate(90 54)"><rect width="96" height="140" rx="6" fill="{N3}" stroke="#fff" stroke-opacity=".15"/>
{"".join(f'<rect x="{14 + (i % 3) * 26}" y="{16 + (i // 3) * 26}" width="16" height="14" rx="2" fill="{(S if i % 4 == 0 else "#fff")}" fill-opacity="{.9 if i % 4 == 0 else .14}"/>' for i in range(12))}
<rect x="36" y="114" width="24" height="26" rx="2" fill="{A}"/></g>
<g transform="translate(210 88)"><rect width="130" height="82" rx="8" fill="#fff"/><rect x="10" y="10" width="110" height="52" rx="4" fill="{N}"/>
<rect x="20" y="22" width="44" height="6" rx="3" fill="#fff" fill-opacity=".6"/><rect x="20" y="34" width="70" height="4" rx="2" fill="#fff" fill-opacity=".2"/><circle cx="104" cy="48" r="7" fill="{O}"/>
<rect x="-10" y="82" width="150" height="8" rx="4" fill="#3A5178"/></g>''')


SECTOR_ART = {
    "notarias": sec_notarias, "gestorias": sec_gestorias, "corredurias-seguros": sec_corredurias,
    "industria": sec_industria, "maquinaria": sec_maquinaria, "logistica": sec_logistica,
    "moda": sec_moda, "alimentacion": sec_alimentacion, "pymes": sec_pymes,
}


def sector_art(slug, uid):
    return SECTOR_ART.get(slug, sec_pymes)(uid)
