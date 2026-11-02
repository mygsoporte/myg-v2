"""
Tipos de clientes (sectores) de M&G Consulting — descripciones genéricas
por tipo de empresa, sin detallar la actividad concreta de ningún cliente.

Cada sector tiene su página en /clientes/<slug>.html.
  group    → columna del menú Clientes
  icon     → clave del diccionario ICON de build.py
  services → servicios recomendados (slugs de contenido_servicios.py)
  cases    → casos de éxito relacionados (slugs de contenido_casos.py)
"""

GROUPS = ["Servicios profesionales", "Industria y logística", "Comercio y servicios"]

SECTORS = [
    # ------------------------------------------------------------ SERVICIOS PROFESIONALES
    {
        "slug": "notarias", "group": "Servicios profesionales", "name": "Notarías", "icon": "stamp",
        "short": "Despachos notariales con atención diaria al público.",
        "title": "Tecnología para notarías",
        "lead": "Sistemas fiables, información protegida y soporte cercano para que la notaría atienda a sus clientes sin interrupciones.",
        "challenges": [
            ("Disponibilidad", "Supervisión continua de los sistemas para detectar los problemas antes de que afecten a la atención."),
            ("Protección de la información", "Copias de seguridad verificadas y accesos controlados."),
            ("Soporte cercano", "Un equipo que conoce vuestro entorno y responde cuando lo necesitáis."),
        ],
        "services": ["mgcare", "ciberseguridad", "proyectos-it"],
        "cases": ["notaria-monitorizacion"],
    },
    {
        "slug": "gestorias", "group": "Servicios profesionales", "name": "Gestorías y asesorías", "icon": "calculator",
        "short": "Gestorías, asesorías y despachos profesionales.",
        "title": "Tecnología para gestorías, asesorías y despachos",
        "lead": "Despachos que trabajan con información de sus clientes y necesitan que su tecnología esté a punto en los momentos de más carga.",
        "challenges": [
            ("Información de clientes", "Accesos seguros, correo protegido y copias de seguridad."),
            ("Picos de trabajo", "Equipos y sistemas revisados para que todo funcione cuando más se necesita."),
            ("Trabajo en remoto", "Acceso seguro a la información desde cualquier lugar."),
        ],
        "services": ["mgcare", "ciberseguridad", "microsoft-365"],
        "cases": ["despacho-servicio-gestionado"],
    },
    {
        "slug": "corredurias-seguros", "group": "Servicios profesionales", "name": "Corredurías de seguros", "icon": "umbrella",
        "short": "Corredurías y agencias de seguros.",
        "title": "Tecnología para corredurías de seguros",
        "lead": "Empresas que gestionan datos de sus clientes y trabajan a diario con herramientas online y equipos comerciales.",
        "challenges": [
            ("Datos personales", "Protección de la información con permisos, cifrado y copias."),
            ("Seguridad del correo", "Protección frente al fraude y la suplantación."),
            ("Equipos en movilidad", "Portátiles y móviles gestionados y seguros."),
        ],
        "services": ["mgcare", "ciberseguridad", "microsoft-365"],
        "cases": ["correduria-seguridad"],
    },

    # ------------------------------------------------------------ INDUSTRIA Y LOGÍSTICA
    {
        "slug": "industria", "group": "Industria y logística", "name": "Industria y fabricación", "icon": "factory",
        "short": "Empresas con plantas de producción.",
        "title": "Tecnología para empresas industriales",
        "lead": "Empresas de fabricación que necesitan una infraestructura estable para que la producción y la gestión no se detengan.",
        "challenges": [
            ("Continuidad", "Servidores, red y copias pensados para que un fallo no pare la actividad."),
            ("Redes de planta y oficina", "Redes separadas y seguras para cada entorno."),
            ("Crecimiento", "Infraestructura que se amplía al ritmo de la empresa."),
        ],
        "services": ["proyectos-it", "mgcare", "ciberseguridad"],
        "cases": ["industria-continuidad"],
    },
    {
        "slug": "maquinaria", "group": "Industria y logística", "name": "Maquinaria y equipos", "icon": "gear",
        "short": "Distribución y servicio técnico de maquinaria.",
        "title": "Tecnología para empresas de maquinaria y equipos",
        "lead": "Empresas de venta y servicio técnico con equipos en la calle, varias sedes y sistemas de gestión que tienen que estar siempre disponibles.",
        "challenges": [
            ("Técnicos en movilidad", "Dispositivos gestionados y acceso seguro desde cualquier lugar."),
            ("Varias sedes", "Conexión segura entre oficinas, talleres y almacenes."),
            ("Sistemas de gestión", "Infraestructura fiable para la operativa diaria."),
        ],
        "services": ["mgcare", "proyectos-it", "suministro-it"],
        "cases": [],
    },
    {
        "slug": "logistica", "group": "Industria y logística", "name": "Logística y distribución", "icon": "conveyor",
        "short": "Empresas de logística, distribución y automatización.",
        "title": "Tecnología para logística y distribución",
        "lead": "Empresas con almacenes, equipos desplazados y proyectos con plazos exigentes, que necesitan un soporte ágil y cercano.",
        "challenges": [
            ("Equipos desplazados", "Soporte y acceso seguro allí donde trabaje cada persona."),
            ("Almacenes conectados", "Redes y wifi profesionales en naves y almacenes."),
            ("Estándares corporativos", "Implantación alineada con las políticas de cada empresa o grupo."),
        ],
        "services": ["mgcare", "suministro-it", "ciberseguridad"],
        "cases": ["logistica-equipos"],
    },

    # ------------------------------------------------------------ COMERCIO Y SERVICIOS
    {
        "slug": "moda", "group": "Comercio y servicios", "name": "Moda y textil", "icon": "shirt",
        "short": "Fabricación y venta de ropa.",
        "title": "Tecnología para empresas de moda y textil",
        "lead": "Empresas de moda con oficinas, almacenes y tiendas que necesitan una tecnología homogénea, segura y fácil de ampliar.",
        "challenges": [
            ("Tiendas y oficinas conectadas", "Red y soporte homogéneos en todas las ubicaciones."),
            ("Crecimiento ágil", "Nuevos puntos de venta y puestos preparados en poco tiempo."),
            ("Información protegida", "Copias, accesos seguros y protección frente a amenazas."),
        ],
        "services": ["mgcare", "proyectos-it", "suministro-it"],
        "cases": ["moda-red-tiendas"],
    },
    {
        "slug": "alimentacion", "group": "Comercio y servicios", "name": "Alimentación", "icon": "basket",
        "short": "Empresas del sector alimentario.",
        "title": "Tecnología para empresas de alimentación",
        "lead": "Empresas del sector alimentario que necesitan que su actividad y sus sistemas de gestión funcionen sin interrupciones.",
        "challenges": [
            ("Sistemas de gestión", "Servidores, copias y supervisión para los sistemas críticos."),
            ("Instalaciones conectadas", "Cobertura y red fiables en oficinas, naves y almacenes."),
            ("Continuidad", "Soporte y supervisión para que un fallo no pare la actividad."),
        ],
        "services": ["proyectos-it", "mgcare", "ciberseguridad"],
        "cases": [],
    },
    {
        "slug": "pymes", "group": "Comercio y servicios", "name": "Pymes y otros sectores", "icon": "building",
        "short": "Empresas de cualquier sector sin departamento IT propio.",
        "title": "Tecnología para pymes de cualquier sector",
        "lead": "Trabajamos con empresas de muchos ámbitos. Si tu tecnología tiene que funcionar cada día y no quieres ocuparte de ella, podemos ser tu departamento IT.",
        "challenges": [
            ("Sin departamento IT propio", "Soporte a usuarios y gestión de sistemas con un equipo que conoce tu entorno."),
            ("Coste previsible", "Una cuota mensual clara y recomendaciones para no pagar lo que no se usa."),
            ("Seguridad desde el primer día", "Copias, accesos seguros y protección frente a amenazas."),
        ],
        "services": ["mgcare", "microsoft-365", "ciberseguridad"],
        "cases": ["migracion-dominio-m365", "salesforce-microsoft-365"],
    },
]
