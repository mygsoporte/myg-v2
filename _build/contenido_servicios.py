"""
Contenido de las páginas de servicio de M&G Consulting.

Cada servicio tiene:
  slug, name, gem           → URL, nombre y color del marcador
  short                     → frase para menú y portada
  title, lead               → cabecera de la página
  overview                  → 2 párrafos de presentación
  fit                       → "Te encaja si…"
  includes                  → (título, descripción) de lo que incluye
  spotlight (opcional)      → bloque destacado (MCloud, Copilot…)
  tech                      → grupos de tecnologías y fabricantes
  process                   → pasos (título, descripción)
  deliverables              → lo que recibe el cliente
  faqs                      → preguntas frecuentes
"""

SERVICES = [
    # ------------------------------------------------------------------ CIBERSEGURIDAD
    {
        "slug": "ciberseguridad", "name": "Ciberseguridad", "gem": "orange",
        "short": "Firewalls, protección de equipos, identidad y copias para que tu empresa no pare.",
        "title": "Ciberseguridad para empresas que no pueden parar",
        "lead": "Evaluamos cómo está expuesta tu empresa, cerramos primero lo que más riesgo supone y mantenemos la protección al día, mes a mes.",
        "overview": [
            "La mayoría de incidentes en pymes y despachos no empiezan con un ataque sofisticado, sino con una contraseña robada, un correo fraudulento o una copia de seguridad que nadie había comprobado. Por eso trabajamos por capas: perímetro, equipos, identidad, datos y personas.",
            "Combinamos firewalls de Fortinet y SonicWall, la seguridad incluida en Microsoft 365 y copias verificadas en NAS y en la nube. Todo queda documentado y revisado periódicamente, para que la protección no dependa de que alguien se acuerde.",
        ],
        "fit": [
            "Manejas datos confidenciales de clientes",
            "No sabes si tus copias funcionarían tras un ataque",
            "Tu equipo trabaja en remoto o desde varias sedes",
            "Necesitas cumplir con el RGPD o demostrar controles de seguridad",
        ],
        "includes": [
            ("Auditoría de seguridad", "Revisión de red, firewall, equipos, cuentas, permisos y copias, con un informe de riesgos priorizado."),
            ("Firewall de nueva generación", "Implantación y gestión de FortiGate y SonicWall: filtrado web, IPS, antivirus perimetral y control de aplicaciones."),
            ("VPN y acceso remoto", "Acceso seguro desde casa o desde otras sedes, con doble factor y permisos por usuario."),
            ("Segmentación de red", "Redes separadas para servidores, usuarios, invitados y dispositivos, para contener cualquier incidente."),
            ("Protección de equipos", "Microsoft Defender (EDR) en puestos y servidores, con parches de Windows y aplicaciones aplicados de forma planificada."),
            ("Identidad y acceso", "MFA, acceso condicional y revisión de cuentas con privilegios en Microsoft Entra ID."),
            ("Protección del correo", "Filtros antiphishing y antimalware, y configuración de SPF, DKIM y DMARC para evitar suplantaciones de tu dominio."),
            ("Copias y recuperación", "Estrategia 3-2-1 con copias inmutables en NAS QNAP o Synology y en la nube, con pruebas de restauración periódicas."),
            ("Concienciación", "Formación práctica y simulaciones de phishing para que tu equipo reconozca el fraude."),
        ],
        "spotlight": {
            "title": "Tu firewall, gestionado y al día",
            "text": "Un firewall mal configurado o sin suscripciones activas da una falsa sensación de seguridad. Nos encargamos de las reglas, las actualizaciones de firmware, las renovaciones de licencias de seguridad y la revisión de alertas, para que siempre esté protegiendo.",
            "points": ["Fortinet FortiGate", "SonicWall", "Suscripciones de seguridad", "Informes de actividad"],
        },
        "tech": [
            ("Seguridad perimetral", ["Fortinet FortiGate", "SonicWall"]),
            ("Equipos e identidad", ["Microsoft Defender", "Microsoft Entra ID", "Microsoft Intune"]),
            ("Copias de seguridad", ["QNAP", "Synology", "Azure Backup"]),
        ],
        "process": [
            ("Diagnóstico", "Auditoría técnica y entrevista para entender cómo trabajáis y qué datos son críticos."),
            ("Plan de mejora", "Medidas ordenadas por riesgo y coste, con alcance y presupuesto cerrados."),
            ("Implantación", "Aplicamos los cambios por fases, fuera de horario cuando es necesario, y formamos a los usuarios."),
            ("Revisión continua", "Supervisión de alertas, parches y copias, con revisiones periódicas del estado de seguridad."),
        ],
        "deliverables": ["Informe de riesgos priorizado", "Plan de acción con presupuesto", "Documentación de la configuración", "Plan de recuperación ante incidentes"],
        "faqs": [
            ("¿Por dónde empezamos?", "Por una auditoría. Nos da una foto real del estado de tu seguridad y permite priorizar las medidas con mejor relación entre riesgo y coste."),
            ("¿Qué firewall nos conviene, Fortinet o SonicWall?", "Ambos son sólidos. Recomendamos uno u otro según el número de usuarios, las sedes, el tipo de conexión y lo que ya tengáis instalado, para no cambiar equipos sin necesidad."),
            ("¿Las medidas afectan al día a día de los usuarios?", "Buscamos el mínimo impacto. Los cambios se planifican, se comunican con antelación y se acompañan de instrucciones claras, por ejemplo para activar el doble factor."),
            ("¿Qué pasa si sufrimos un incidente?", "Si tienes contratado el servicio gestionado, actuamos para aislar el problema, recuperar los datos desde las copias y analizar qué ocurrió para que no se repita."),
        ],
    },

    # ------------------------------------------------------------------ CLOUD
    {
        "slug": "cloud", "name": "Cloud", "gem": "amber",
        "short": "Azure, Google Cloud o nuestro cloud privado MCloud: lo que tenga sentido para ti.",
        "title": "Cloud a la medida de tu negocio",
        "lead": "Analizamos tus aplicaciones y servidores y diseñamos la combinación adecuada de nube pública, cloud privado y equipos propios, con costes previsibles.",
        "overview": [
            "No todas las cargas de trabajo deben ir a la nube, ni a la misma nube. Una aplicación de gestión antigua, un servidor de archivos o un entorno de escritorio remoto tienen necesidades distintas de rendimiento, coste y cumplimiento normativo.",
            "Trabajamos con Microsoft Azure, Google Cloud y MCloud, nuestra plataforma de cloud privado. Así podemos recomendarte la opción más adecuada para cada caso, y combinarlas con tu infraestructura local cuando convenga.",
        ],
        "fit": [
            "Tus servidores se acercan al final de su vida útil",
            "Quieres trabajar con seguridad desde cualquier lugar",
            "La factura de la nube crece sin control",
            "Necesitas continuidad ante una avería o un desastre",
        ],
        "includes": [
            ("Análisis y diseño", "Qué conviene migrar, qué mantener en local y cuánto costará cada opción a tres años vista."),
            ("Migración a Azure", "Servidores, aplicaciones y archivos trasladados con un plan de pruebas y de vuelta atrás."),
            ("Google Cloud", "Despliegue y administración de máquinas virtuales y almacenamiento en Google Cloud."),
            ("Cloud privado MCloud", "Servidores alojados y gestionados por M&G, con un interlocutor directo y costes fijos."),
            ("Entornos híbridos", "Conexión segura entre tus oficinas y la nube, con identidad y red unificadas."),
            ("Escritorios remotos", "Acceso a aplicaciones y escritorios desde cualquier dispositivo con Azure Virtual Desktop o escritorio remoto."),
            ("Copias y recuperación", "Copia de seguridad en la nube y réplica de servidores para volver a trabajar rápido tras una caída."),
            ("Control de costes", "Revisión mensual del consumo, ajuste de tamaños y reservas para evitar sorpresas en la factura."),
        ],
        "spotlight": {
            "title": "MCloud, nuestro cloud privado",
            "text": "MCloud es la plataforma de M&G para alojar servidores y servicios de clientes. Es una alternativa a la nube pública para empresas que prefieren un coste mensual estable y un equipo técnico cercano que conoce su entorno.",
            "points": ["Servidores virtuales gestionados", "Copias de seguridad incluidas", "Coste mensual previsible", "Soporte directo del equipo de M&G"],
            "cta": ("Acceso MCloud", "MCLOUD"),
        },
        "tech": [
            ("Nube pública", ["Microsoft Azure", "Google Cloud"]),
            ("Cloud privado", ["MCloud"]),
            ("Servicios", ["Azure Virtual Desktop", "Azure Backup", "Azure Site Recovery", "Azure Files"]),
        ],
        "process": [
            ("Inventario", "Revisamos servidores, aplicaciones, volúmenes de datos y dependencias."),
            ("Propuesta", "Comparamos opciones y costes, y elegimos contigo la plataforma de destino."),
            ("Migración", "Trasladamos por fases, con pruebas previas y ventanas fuera del horario laboral."),
            ("Operación", "Supervisamos rendimiento, seguridad, copias y costes cada mes."),
        ],
        "deliverables": ["Comparativa de costes por opción", "Diseño de la arquitectura", "Plan de migración y de vuelta atrás", "Informe mensual de consumo"],
        "faqs": [
            ("¿Es siempre más barato ir a la nube?", "No siempre. Por eso empezamos comparando el coste total de cada opción antes de recomendar una migración."),
            ("¿Azure, Google Cloud o MCloud?", "Depende de tus aplicaciones, de lo que ya uses y de cómo prefieras pagar. Azure encaja muy bien con Microsoft 365; MCloud es ideal si buscas un coste fijo y un trato directo."),
            ("¿Cuánto tiempo sin servicio implica una migración?", "Planificamos las ventanas de cambio fuera del horario laboral para que el impacto sea mínimo o nulo."),
            ("¿Podemos volver atrás si algo no funciona?", "Sí. Cada migración incluye un plan de vuelta atrás y no retiramos los sistemas originales hasta validar el nuevo entorno."),
        ],
    },

    # ------------------------------------------------------------------ MICROSOFT 365
    {
        "slug": "microsoft-365", "name": "Microsoft 365", "gem": "sun",
        "short": "Correo, Teams, SharePoint, seguridad y Copilot bien configurados y aprovechados.",
        "title": "Microsoft 365 ordenado, seguro y aprovechado",
        "lead": "Sacamos partido a las licencias que ya pagas: estructura documental clara, seguridad bien configurada, usuarios que saben trabajar con sus herramientas e inteligencia artificial con Copilot.",
        "overview": [
            "Muchas empresas usan Microsoft 365 solo como correo y paquete Office, mientras pagan por funciones de seguridad, gestión de dispositivos y colaboración que nadie ha configurado. Nuestro trabajo es que cada licencia rinda lo que cuesta.",
            "Nos ocupamos de todo el ciclo: elegir las licencias adecuadas, migrar el correo y los archivos, organizar SharePoint y Teams, proteger cuentas y dispositivos y, cuando tu entorno está listo, poner en marcha Copilot con garantías.",
        ],
        "fit": [
            "Los archivos están repartidos sin orden entre equipos y carpetas",
            "Pagas licencias que nadie usa o no sabes cuáles tienes",
            "Vas a cambiar de dominio o de proveedor de correo",
            "Quieres empezar a usar Copilot en tu empresa",
        ],
        "includes": [
            ("Licencias", "Elección y ajuste de planes Business Basic, Standard, Premium o Enterprise según cada puesto."),
            ("Migraciones", "Cambio de correo, dominios o tenant desde otros proveedores o desde Google, sin perder información."),
            ("SharePoint y OneDrive", "Sites por departamento, estructura documental, permisos coherentes y migración desde servidores de archivos."),
            ("Teams", "Equipos y canales organizados, reuniones, telefonía y políticas de uso."),
            ("Seguridad", "MFA, acceso condicional, Defender para Office 365 y políticas de protección de datos."),
            ("Gestión de dispositivos", "Alta automática y gestión de portátiles y móviles con Intune y Autopilot."),
            ("Copilot", "Preparación del entorno, licencias, activación y formación para Microsoft 365 Copilot."),
            ("Integraciones", "Conexión con aplicaciones de negocio como Salesforce y automatizaciones con Power Automate."),
        ],
        "spotlight": {
            "title": "Copilot, con tu información en orden",
            "text": "Copilot responde con la información a la que cada usuario tiene acceso. Si los permisos de SharePoint o OneDrive están desordenados, puede mostrar documentos que no debería. Antes de activarlo, revisamos permisos y etiquetas de confidencialidad, y después formamos a tu equipo con casos de uso reales.",
            "points": ["Revisión de permisos", "Activación por fases", "Formación práctica", "Seguimiento de la adopción"],
        },
        "tech": [
            ("Productividad", ["Microsoft 365", "Exchange Online", "Teams", "SharePoint", "OneDrive"]),
            ("Seguridad y dispositivos", ["Microsoft Entra ID", "Microsoft Intune", "Microsoft Defender", "Microsoft Purview"]),
            ("IA y automatización", ["Microsoft 365 Copilot", "Power Automate"]),
        ],
        "process": [
            ("Revisión del tenant", "Analizamos licencias, configuración de seguridad, almacenamiento y uso actual."),
            ("Diseño", "Definimos estructura documental, permisos, políticas y plan de licencias."),
            ("Implantación", "Migramos y configuramos por fases, sin interrumpir el trabajo diario."),
            ("Adopción", "Formamos a los usuarios y administramos el entorno de forma continua."),
        ],
        "deliverables": ["Informe del estado del tenant", "Plan de licencias optimizado", "Mapa de sites y permisos", "Guías para usuarios"],
        "faqs": [
            ("¿Podéis migrar el correo desde otro proveedor?", "Sí, incluido Google Workspace y otros servidores de correo. Planificamos la migración de buzones y dominios para que los usuarios sigan trabajando durante el proceso."),
            ("¿Necesito cambiar mis licencias?", "Revisamos lo que tienes y te decimos si te sobra o te falta algo. A menudo se puede ahorrar o ganar seguridad con el mismo presupuesto."),
            ("¿Qué necesito para usar Copilot?", "Una licencia compatible de Microsoft 365, la licencia de Copilot y, sobre todo, un entorno con los permisos bien configurados. Te ayudamos con las tres cosas."),
            ("¿Podemos sustituir el servidor de archivos por SharePoint?", "En muchos casos sí. Analizamos el volumen, la estructura y las aplicaciones que dependen de esas carpetas antes de proponerlo."),
        ],
    },

    # ------------------------------------------------------------------ PROYECTOS IT
    {
        "slug": "proyectos-it", "name": "Proyectos IT", "gem": "orange",
        "short": "Servidores, almacenamiento, redes y wifi planificados, ejecutados y documentados.",
        "title": "Proyectos de infraestructura sin sorpresas",
        "lead": "Servidores, almacenamiento, redes y wifi diseñados a tu medida. Cada proyecto tiene un responsable técnico, un calendario claro y una documentación final que te pertenece.",
        "overview": [
            "Una infraestructura que crece sin planificación acaba siendo lenta, frágil y difícil de mantener. Diseñamos cada proyecto a partir de cómo trabaja tu empresa hoy y de cómo prevés que crezca en los próximos años.",
            "Trabajamos con fabricantes consolidados: HPE para servidores, QNAP y Synology para almacenamiento y copias, Aruba Networking y Ubiquiti para redes y wifi, y Fortinet y SonicWall para la seguridad perimetral.",
        ],
        "fit": [
            "Vas a cambiar de oficina o abrir una nueva sede",
            "Tus servidores o tu red se han quedado pequeños",
            "La wifi no llega bien o se corta",
            "Nadie tiene documentado cómo está montado todo",
        ],
        "includes": [
            ("Servidores", "Diseño e instalación de servidores HPE ProLiant, con virtualización y alta disponibilidad cuando hace falta."),
            ("Almacenamiento y NAS", "Servidores de archivos y repositorios de copias en QNAP y Synology, con instantáneas y réplica."),
            ("Redes cableadas", "Switches gestionables Aruba Networking o Ubiquiti UniFi, con VLAN y cableado estructurado."),
            ("Wifi profesional", "Estudio de cobertura y puntos de acceso Aruba o UniFi, con red de invitados separada."),
            ("Seguridad perimetral", "Firewalls Fortinet o SonicWall integrados en el diseño de red."),
            ("Traslados y nuevas sedes", "Mudanza tecnológica completa y conexión entre oficinas por VPN."),
            ("Monitorización", "Despliegue de monitorización con Zabbix para detectar problemas antes de que afecten al trabajo."),
            ("Auditoría on-premise", "Informe completo del estado de tu infraestructura local y un plan de renovación."),
        ],
        "spotlight": None,
        "tech": [
            ("Servidores", ["HPE ProLiant"]),
            ("Almacenamiento", ["QNAP", "Synology", "HPE"]),
            ("Redes y wifi", ["Aruba Networking", "Ubiquiti UniFi"]),
            ("Seguridad y monitorización", ["Fortinet", "SonicWall", "Zabbix"]),
        ],
        "process": [
            ("Toma de requisitos", "Visita técnica, inventario y necesidades de cada departamento."),
            ("Diseño y presupuesto", "Arquitectura, equipos, calendario y coste cerrados."),
            ("Ejecución", "Instalación y migración con un responsable técnico y el mínimo impacto."),
            ("Entrega", "Pruebas, documentación y, si lo deseas, paso a servicio gestionado."),
        ],
        "deliverables": ["Diseño de arquitectura", "Planificación por fases", "Diagramas de red e inventario", "Procedimientos de operación"],
        "faqs": [
            ("¿Cómo se presupuesta un proyecto?", "Tras una visita o reunión técnica entregamos una propuesta con alcance, equipos, plazos y coste cerrados."),
            ("¿Trabajáis con los equipos que ya tenemos?", "Sí. Reutilizamos lo que esté en buen estado y sea compatible, y solo proponemos sustituir lo necesario."),
            ("¿QNAP o Synology?", "Ambos fabricantes ofrecen NAS muy fiables. Elegimos según el uso (archivos, copias, virtualización), el crecimiento previsto y las herramientas de copia que necesites."),
            ("¿Qué pasa cuando termina el proyecto?", "Recibes toda la documentación y, si quieres, el entorno pasa a nuestro servicio gestionado MGCare."),
        ],
    },

    # ------------------------------------------------------------------ SUMINISTRO IT
    {
        "slug": "suministro-it", "name": "Suministro IT", "gem": "amber",
        "short": "Equipos, electrónica de red y licencias entregados configurados y listos.",
        "title": "Suministro IT y licencias, sin complicaciones",
        "lead": "Te asesoramos en la compra, entregamos cada equipo configurado e inventariado, y gestionamos tus licencias y suscripciones para que nada caduque sin aviso.",
        "overview": [
            "Comprar tecnología a varios proveedores, sin un criterio común, termina en equipos distintos, garantías sin controlar y licencias que vencen en el peor momento. Centralizamos las compras y te recomendamos solo lo que encaja con tu entorno.",
            "Suministramos servidores, almacenamiento, electrónica de red, firewalls y puestos de trabajo, además de licencias de Microsoft y suscripciones de seguridad. Todo llega configurado y queda registrado en tu inventario.",
        ],
        "fit": [
            "Incorporas personas con frecuencia",
            "Compras equipos a distintos proveedores",
            "No controlas garantías ni vencimientos de licencias",
            "Quieres equipos homogéneos y fáciles de mantener",
        ],
        "includes": [
            ("Puestos de trabajo", "Portátiles, sobremesas, monitores, periféricos y accesorios."),
            ("Servidores y almacenamiento", "Servidores HPE y NAS QNAP y Synology, con discos y ampliaciones."),
            ("Redes y wifi", "Switches y puntos de acceso Aruba Networking y Ubiquiti."),
            ("Firewalls", "Equipos Fortinet y SonicWall con sus suscripciones de seguridad."),
            ("Licencias Microsoft", "Microsoft 365, Windows, Windows Server y Copilot, ajustadas a cada usuario."),
            ("Otras licencias", "Antivirus, copias de seguridad y software de terceros, con renovaciones controladas."),
            ("Preparación y entrega", "Equipos configurados con aplicaciones, cuentas y políticas de seguridad."),
            ("Inventario y garantías", "Registro de cada equipo, usuario asignado, garantía y fecha de renovación."),
        ],
        "spotlight": {
            "title": "Licencias bajo control",
            "text": "Revisamos todas tus licencias y suscripciones —Microsoft, firewalls, antivirus, copias— y te avisamos antes de cada vencimiento. Así evitas pagar por licencias que no se usan y quedarte sin protección por una renovación olvidada.",
            "points": ["Inventario de licencias", "Aviso de vencimientos", "Ajuste al número real de usuarios", "Renovaciones gestionadas"],
        },
        "tech": [
            ("Servidores y almacenamiento", ["HPE", "QNAP", "Synology"]),
            ("Redes y seguridad", ["Aruba Networking", "Ubiquiti", "Fortinet", "SonicWall"]),
            ("Licencias", ["Microsoft 365", "Windows Server", "Microsoft 365 Copilot", "Suscripciones de seguridad"]),
        ],
        "process": [
            ("Necesidad", "Nos cuentas qué necesitas o lo detectamos en la revisión de tu entorno."),
            ("Propuesta", "Te recomendamos el equipo o la licencia adecuada, con precio y plazo."),
            ("Preparación", "Configuramos, instalamos y probamos antes de la entrega."),
            ("Seguimiento", "Inventario, garantías y renovaciones controladas."),
        ],
        "deliverables": ["Propuesta con precio y plazo", "Equipos listos para usar", "Inventario actualizado", "Calendario de renovaciones"],
        "faqs": [
            ("¿Trabajáis con marcas concretas?", "Trabajamos habitualmente con HPE, QNAP, Synology, Aruba Networking, Ubiquiti, Fortinet y SonicWall, pero recomendamos siempre lo que mejor encaja con tu uso y presupuesto."),
            ("¿Os encargáis de preparar los equipos?", "Sí. Llegan con las aplicaciones, cuentas y políticas de seguridad configuradas, listos para que el usuario empiece a trabajar."),
            ("¿Podéis gestionar nuestras licencias de Microsoft?", "Sí. Revisamos las que tienes, ajustamos el número y el tipo a cada usuario y gestionamos altas, bajas y renovaciones."),
            ("¿Qué pasa si un equipo se avería en garantía?", "Gestionamos la incidencia con el fabricante y, si es necesario, te facilitamos un equipo de sustitución mientras tanto."),
        ],
    },

    # ------------------------------------------------------------------ TRANSFORMACIÓN DIGITAL E IA
    {
        "slug": "transformacion-digital", "name": "Transformación digital e IA", "gem": "sun",
        "short": "Menos tareas manuales con automatización e inteligencia artificial de Microsoft.",
        "title": "Transformación digital e IA con los pies en el suelo",
        "lead": "Identificamos tareas manuales y papeleo que se pueden simplificar, incorporamos la inteligencia artificial de Microsoft donde aporta valor y te acompañamos para que el cambio funcione en el día a día.",
        "overview": [
            "La transformación digital no consiste en comprar más herramientas, sino en usar mejor las que tienes. Empezamos por entender los procesos que más tiempo consumen y buscamos la forma más sencilla de mejorarlos.",
            "Trabajamos sobre el ecosistema Microsoft que muchas empresas ya tienen: automatizaciones con Power Automate, gestión documental en SharePoint y asistentes de IA con Microsoft 365 Copilot y Copilot Studio, siempre con los datos protegidos.",
        ],
        "fit": [
            "Tu equipo repite tareas manuales a diario",
            "La información está en hojas de cálculo y correos sueltos",
            "Quieres probar la IA en tu empresa con seguridad",
            "Buscas un plan tecnológico a varios años",
        ],
        "includes": [
            ("Diagnóstico", "Análisis de procesos, herramientas actuales y puntos donde se pierde tiempo."),
            ("Hoja de ruta", "Plan tecnológico a medio plazo, priorizado por impacto y esfuerzo."),
            ("Automatización", "Flujos con Power Automate para aprobaciones, avisos, formularios y traspaso de datos entre aplicaciones."),
            ("Gestión documental", "Digitalización y organización de documentos en SharePoint, con búsqueda y control de versiones."),
            ("Microsoft 365 Copilot", "Activación y casos de uso prácticos en Outlook, Word, Excel, Teams y PowerPoint."),
            ("Agentes con Copilot Studio", "Asistentes que responden con la información de tu empresa, por ejemplo para procedimientos internos."),
            ("Aplicaciones de negocio", "Implantación e integración de CRM y otras herramientas con Microsoft 365."),
            ("Formación y acompañamiento", "Sesiones prácticas y seguimiento para asegurar que el cambio se adopta."),
        ],
        "spotlight": {
            "title": "Inteligencia artificial, con criterio",
            "text": "Empezamos con pilotos pequeños y medibles: resumir reuniones, redactar respuestas, buscar información en tus documentos o automatizar tareas repetitivas. Antes de ampliar, comprobamos que ahorra tiempo de verdad y que la información está protegida.",
            "points": ["Microsoft 365 Copilot", "Copilot Studio", "Power Automate", "Protección de datos"],
        },
        "tech": [
            ("Inteligencia artificial", ["Microsoft 365 Copilot", "Copilot Studio"]),
            ("Automatización", ["Power Automate", "Microsoft Forms"]),
            ("Colaboración y datos", ["SharePoint", "Teams", "Salesforce"]),
        ],
        "process": [
            ("Diagnóstico", "Entrevistas y análisis para detectar dónde se pierde más tiempo."),
            ("Priorización", "Elegimos las mejoras con más impacto y menos esfuerzo."),
            ("Piloto", "Probamos con un equipo reducido y medimos el resultado."),
            ("Despliegue", "Extendemos a toda la empresa con formación y seguimiento."),
        ],
        "deliverables": ["Mapa de procesos y mejoras", "Hoja de ruta priorizada", "Automatizaciones documentadas", "Resultados del piloto"],
        "faqs": [
            ("¿Necesito cambiar todas mis herramientas?", "No. Empezamos aprovechando lo que ya tienes y solo proponemos cambios cuando aportan una mejora clara."),
            ("¿Es segura la IA de Microsoft para los datos de mi empresa?", "Microsoft 365 Copilot trabaja dentro de tu tenant y respeta los permisos de cada usuario. Por eso revisamos y ordenamos los permisos antes de activarlo."),
            ("¿Qué tareas se pueden automatizar?", "Aprobaciones, avisos, recogida de datos con formularios, generación de documentos o traspaso de información entre aplicaciones, entre otras."),
            ("¿Cuánto dura un proyecto de transformación?", "Depende del alcance. Trabajamos por fases cortas para que veas resultados desde el principio."),
        ],
    },
]


# ----------------------------------------------------------------------------
# Problemas habituales que resuelve cada servicio: (problema, cómo lo resolvemos)
# ----------------------------------------------------------------------------
PROBLEMS = {
    "ciberseguridad": [
        ("Nadie sabe si las copias se podrían restaurar", "Programamos pruebas de restauración periódicas y te enviamos el resultado."),
        ("Un usuario pica en un correo fraudulento", "Doble factor, filtros antiphishing y formación para que un clic no se convierta en un incidente."),
        ("El firewall lleva años sin revisarse", "Revisamos reglas, firmware y suscripciones, y lo dejamos documentado y bajo supervisión."),
    ],
    "cloud": [
        ("El servidor de la oficina está al final de su vida", "Comparamos renovarlo con migrarlo a Azure, Google Cloud o MCloud, con números a tres años."),
        ("La factura de la nube no para de crecer", "Revisamos tamaños, horarios y reservas para pagar solo lo que se usa."),
        ("Si cae la oficina, nadie puede trabajar", "Réplica y copias en la nube para recuperar el servicio en otra ubicación."),
    ],
    "microsoft-365": [
        ("Los documentos están repartidos sin orden", "Estructura de SharePoint por departamentos con permisos claros y migración ordenada."),
        ("Pagamos licencias que no sabemos si usamos", "Inventario de licencias y ajuste del plan de cada usuario."),
        ("Queremos Copilot pero nos preocupan los datos", "Revisamos permisos antes de activarlo y lo desplegamos por fases."),
    ],
    "proyectos-it": [
        ("La wifi no llega bien y se corta", "Estudio de cobertura y puntos de acceso profesionales Aruba o UniFi."),
        ("El almacenamiento se ha quedado pequeño", "NAS o almacenamiento HPE dimensionado para los próximos años, con copias integradas."),
        ("Abrimos una nueva sede", "Red, seguridad y conexión entre oficinas listas antes del primer día."),
    ],
    "suministro-it": [
        ("Cada equipo es de una marca y una configuración", "Estandarizamos modelos y configuraciones para simplificar el soporte."),
        ("Una licencia caducó sin que nadie lo viera", "Calendario de renovaciones con aviso previo."),
        ("Un nuevo empleado tarda días en poder trabajar", "Equipos preparados con cuentas, aplicaciones y seguridad antes de su llegada."),
    ],
    "transformacion-digital": [
        ("Perdemos horas en tareas repetitivas", "Automatizaciones con Power Automate para aprobaciones, avisos y traspaso de datos."),
        ("La información está en Excel y correos sueltos", "Procesos y documentos centralizados en SharePoint y Teams."),
        ("Queremos probar la IA sin riesgos", "Pilotos con Copilot en un equipo reducido, midiendo el tiempo ahorrado."),
    ],
}

# Caso de éxito relacionado con cada servicio (slug del caso en contenido_casos.py)
RELATED_CASE = {
    "ciberseguridad": "notaria-monitorizacion",
    "cloud": "notaria-monitorizacion",
    "microsoft-365": "migracion-dominio-m365",
    "proyectos-it": "notaria-monitorizacion",
    "suministro-it": "despacho-servicio-gestionado",
    "transformacion-digital": "salesforce-microsoft-365",
}

# Formas de contratar (comunes a todos los servicios)
MODALITIES = [
    ("Proyecto cerrado", "Un alcance, un calendario y un presupuesto definidos desde el inicio. Ideal para migraciones, renovaciones o implantaciones concretas."),
    ("Servicio gestionado MGCare", "Una cuota mensual que incluye la gestión continua, la supervisión y el soporte a tus usuarios."),
    ("Auditoría y consultoría", "Un análisis independiente con recomendaciones priorizadas, para decidir con datos antes de invertir."),
]


# ----------------------------------------------------------------------------
# MGCare — servicio gestionado (se inserta el primero en la lista de servicios)
# ----------------------------------------------------------------------------
MGCARE = {
    "slug": "mgcare", "name": "MGCare · Servicio gestionado", "gem": "orange",
    "short": "Tu departamento IT externo: soporte a usuarios, monitorización 24/7 y gestión continua.",
    "title": "MGCare, tu departamento IT externo",
    "lead": "Una cuota mensual que cubre el soporte a tus usuarios y la gestión continua de tus sistemas, estén en tu oficina, en la nube o en Microsoft 365.",
    "overview": [
        "Muchas empresas no necesitan un informático en plantilla, pero sí a alguien que responda cuando algo falla y que se ocupe de que no falle. MGCare es ese equipo: técnicos que conocen tu entorno, lo supervisan cada día y atienden a tus usuarios.",
        "Cada servicio parte de un documento de alcances que define qué está incluido, con qué tiempos de respuesta y qué queda fuera. Así no hay sorpresas: sabes qué pagas y qué recibes cada mes.",
    ],
    "fit": [
        "No tienes departamento IT propio o está desbordado",
        "Los problemas se detectan cuando ya afectan al trabajo",
        "Quieres un coste mensual previsible",
        "Necesitas un interlocutor único para toda la tecnología",
    ],
    "includes": [
        ("HelpDesk para usuarios", "Atención por correo, teléfono o portal, con cada petición registrada y con seguimiento."),
        ("Monitorización 24/7", "Supervisión de servidores, almacenamiento, red, firewall y copias con alertas automáticas."),
        ("Gestión de parches", "Actualizaciones de Windows, servidores y aplicaciones aplicadas de forma planificada."),
        ("Copias de seguridad", "Revisión diaria del estado de las copias y pruebas de restauración periódicas."),
        ("Administración de sistemas", "Servidores, virtualización, directorio activo, permisos y accesos remotos."),
        ("Microsoft 365 y cloud", "Usuarios, licencias, seguridad y servicios en Azure, Google Cloud o MCloud."),
        ("Inventario y documentación", "Equipos, licencias, contraseñas de servicio y procedimientos siempre al día."),
        ("Informes de actividad", "Actividad, incidencias, estado de la infraestructura y recomendaciones, cuando los necesites."),
    ],
    "spotlight": {
        "title": "Un alcance claro, por escrito",
        "text": "Antes de empezar, definimos contigo el documento de alcances: sistemas cubiertos, horario de atención, tiempos de respuesta y lo que queda fuera, como las aplicaciones de negocio de terceros. Es la base de una relación sin malentendidos.",
        "points": ["Sistemas incluidos", "Horario y tiempos de respuesta", "Exclusiones explícitas", "Revisión periódica del alcance"],
    },
    "tech": [
        ("Soporte y tickets", ["Autotask", "Portal de soporte"]),
        ("Monitorización", ["Zabbix", "Grafana"]),
        ("Copias de seguridad", ["Acronis", "Veeam", "Azure Backup"]),
        ("Gestión de equipos", ["Microsoft Intune", "Microsoft Defender"]),
    ],
    "process": [
        ("Auditoría inicial", "Revisamos tu entorno y detectamos lo que hay que corregir antes de empezar."),
        ("Alcance", "Definimos por escrito qué cubre el servicio, horarios y tiempos de respuesta."),
        ("Puesta en marcha", "Instalamos la monitorización, documentamos el entorno y presentamos el equipo."),
        ("Gestión continua", "Soporte diario, supervisión y revisiones periódicas contigo."),
    ],
    "deliverables": ["Documento de alcances", "Inventario y documentación del entorno", "Acceso al portal de soporte", "Informes de actividad y estado a demanda"],
    "faqs": [
        ("¿Qué horario tiene el soporte?", "El horario de atención y los tiempos de respuesta se fijan en el documento de alcances de cada cliente. La monitorización funciona las 24 horas."),
        ("¿Cómo se calcula la cuota?", "Depende del número de usuarios, servidores y servicios incluidos. Tras la auditoría inicial te enviamos una propuesta cerrada."),
        ("¿Qué pasa con las aplicaciones de gestión que usamos?", "Nos ocupamos de la infraestructura sobre la que funcionan. El soporte funcional de aplicaciones de terceros queda a cargo de su fabricante, y coordinamos con él cuando hace falta."),
        ("¿Podemos combinar MGCare con proyectos?", "Sí. Los proyectos de mejora se presupuestan aparte y, al terminar, pasan a formar parte del servicio gestionado."),
    ],
}
SERVICES.insert(0, MGCARE)
PROBLEMS["mgcare"] = [
    ("Nadie se entera de que algo falla hasta que alguien llama", "Monitorización con alertas que nos avisan antes de que el problema afecte al trabajo."),
    ("Cada incidencia se pierde entre correos y llamadas", "Todas las peticiones quedan registradas en el sistema de tickets, con seguimiento."),
    ("Nadie sabe cómo está montado todo", "Documentamos el entorno y lo mantenemos al día como parte del servicio."),
]
RELATED_CASE["mgcare"] = "despacho-servicio-gestionado"
