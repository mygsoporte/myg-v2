"""
Casos de éxito de M&G Consulting.

IMPORTANTE: los clientes aparecen anonimizados por sector. Antes de publicar
el nombre de un cliente, su logo o una cita, pide su autorización por escrito.
Revisa también que el estado y los resultados descritos sean los actuales.
"""

CASES = [
    {
        "slug": "notaria-monitorizacion", "sector_key": "notarias",
        "sector": "Notaría", "place": "Barcelona",
        "title": "Monitorización 24/7 de la infraestructura de una notaría",
        "summary": "Una plataforma de monitorización que avisa antes de que los problemas afecten a la atención al público.",
        "services": ["Proyectos IT", "Ciberseguridad", "MGCare"],
        "challenge": "La notaría depende por completo de sus sistemas para atender a sus clientes: servidores virtualizados, almacenamiento, red y copias de seguridad. Los problemas se detectaban cuando un usuario llamaba porque algo no funcionaba.",
        "solution": [
            "Plataforma de monitorización basada en Zabbix 7.0 LTS con un servidor central y un proxy en la oficina del cliente.",
            "El proxy trabaja en modo activo, por lo que no ha sido necesario abrir puertos de entrada en el firewall de la notaría.",
            "Supervisión de servidores VMware ESXi, almacenamiento HPE, switches, firewall SonicWall y equipos Windows.",
            "Paneles de control con el estado de las copias de seguridad de Veeam y Acronis.",
            "Acceso a los paneles con la cuenta de Microsoft 365 (inicio de sesión único).",
        ],
        "results": [
            "Más de 25 equipos supervisados de forma continua.",
            "Alertas tempranas de disco, rendimiento, hardware y copias fallidas.",
            "Una vista única del estado de toda la infraestructura para el equipo de M&G.",
        ],
        "stack": ["Zabbix", "Grafana", "VMware ESXi", "HPE", "SonicWall", "Veeam", "Acronis", "Microsoft 365"],
    },
    {
        "slug": "despacho-servicio-gestionado", "sector_key": "gestorias",
        "sector": "Despacho jurídico", "place": "Barcelona",
        "title": "HelpDesk y administración de sistemas para un despacho de abogados",
        "summary": "Un departamento IT externo con un alcance claro, para que el despacho se centre en sus clientes.",
        "services": ["MGCare", "Ciberseguridad", "Microsoft 365"],
        "challenge": "El despacho combina un entorno híbrido —directorio local sincronizado con Microsoft Entra ID, servidores virtualizados, escritorio remoto y doble factor— y necesitaba un único proveedor responsable de la infraestructura y del soporte a los usuarios.",
        "solution": [
            "Documento de alcances que define con precisión qué cubre el servicio y qué queda fuera, como las aplicaciones de negocio de terceros.",
            "HelpDesk para los usuarios y administración de servidores, identidad, acceso remoto y firewall.",
            "Plan para incorporar la monitorización centralizada como proyecto independiente.",
        ],
        "results": [
            "Un interlocutor único para la infraestructura y los usuarios.",
            "Responsabilidades claras entre el despacho, M&G y los proveedores de software.",
            "Base documentada para evolucionar el entorno con seguridad.",
        ],
        "stack": ["Microsoft Entra ID", "Active Directory", "Escritorio remoto", "Doble factor", "Virtualización"],
    },
    {
        "slug": "migracion-dominio-m365", "sector_key": "pymes",
        "sector": "Pyme", "place": "España",
        "title": "Cambio de dominio y migración de correo a Microsoft 365",
        "summary": "Nueva marca, nuevo dominio y todo el correo en Microsoft 365 sin perder mensajes.",
        "services": ["Microsoft 365"],
        "challenge": "La empresa cambiaba de nombre comercial y necesitaba trasladar su correo, alojado en otro proveedor, a Microsoft 365 con el nuevo dominio, manteniendo el histórico y sin interrumpir la comunicación con sus clientes.",
        "solution": [
            "Auditoría de la configuración DNS y alta del nuevo dominio en el tenant.",
            "Migración de buzones por IMAP desde el proveedor anterior.",
            "Cambio de registros MX, SPF, DKIM, DMARC y Autodiscover en una ventana planificada.",
            "Actualización de direcciones de usuarios y listas de distribución.",
        ],
        "results": [
            "Correo unificado en Microsoft 365 con el nuevo dominio.",
            "Dominio protegido frente a suplantaciones con SPF, DKIM y DMARC.",
            "Transición transparente para los clientes de la empresa.",
        ],
        "stack": ["Microsoft 365", "Exchange Online", "DNS", "SPF · DKIM · DMARC"],
    },
    {
        "slug": "salesforce-microsoft-365", "sector_key": "pymes", "image": "svc:microsoft-365",
        "sector": "Empresa comercial", "place": "España",
        "title": "Integración de Salesforce con Microsoft 365 a través de Microsoft Graph",
        "summary": "La sincronización de correo y calendario con Salesforce, adaptada a la retirada de EWS por parte de Microsoft.",
        "services": ["Microsoft 365", "Transformación digital e IA"],
        "challenge": "Microsoft retira Exchange Web Services (EWS), la tecnología que usaba Salesforce para sincronizar el correo y el calendario de los comerciales. Sin actuar, la integración dejaría de funcionar.",
        "solution": [
            "Migración de la sincronización de Lightning Sync a Einstein Activity Capture sobre Microsoft Graph.",
            "Pruebas completas en un entorno de test de Salesforce antes de tocar producción.",
            "Permisos mínimos para la aplicación de integración en Microsoft Entra ID.",
            "Revisión posterior de la integración de Outlook con Salesforce.",
        ],
        "results": [
            "Integración preparada para la retirada de EWS.",
            "Cambio validado en test antes de afectar al equipo comercial.",
            "Menor superficie de riesgo gracias a los permisos mínimos.",
        ],
        "stack": ["Salesforce", "Microsoft Graph", "Microsoft Entra ID", "Outlook"],
    },
]

# ----------------------------------------------------------------------------
# CASOS DE EJEMPLO (inventados). Sustituir por casos reales antes de publicar.
# Mientras "ejemplo" sea True, la página del caso lleva noindex y en
# build.py se pueden ocultar todos con PUBLICAR_EJEMPLOS = False.
# ----------------------------------------------------------------------------
CASES += [
    {
        "slug": "moda-red-tiendas", "sector_key": "moda", "ejemplo": True,
        "sector": "Moda y textil", "place": "Barcelona",
        "title": "Red y soporte homogéneos para una cadena de tiendas de moda",
        "summary": "Todas las tiendas con la misma red, la misma seguridad y un único punto de soporte.",
        "services": ["Proyectos IT", "Ciberseguridad", "MGCare"],
        "challenge": "Cada tienda se había montado en un momento distinto, con equipos y configuraciones diferentes. Las incidencias de conexión eran difíciles de diagnosticar y cada apertura exigía empezar de cero.",
        "solution": [
            "Diseño de una tienda tipo con firewall, switch y wifi estándar.",
            "Conexión segura de cada tienda con la oficina central.",
            "Redes separadas para el personal, los puntos de venta y los clientes.",
            "Monitorización de la conectividad de todas las tiendas.",
            "Plantilla de apertura para preparar nuevas tiendas con antelación.",
        ],
        "results": [
            "Una configuración común en todas las tiendas.",
            "Problemas de red detectados antes de que afecten a las ventas.",
            "Aperturas más rápidas y previsibles.",
        ],
        "stack": ["Fortinet", "Aruba Networking", "Microsoft 365", "Zabbix"],
    },
    {
        "slug": "industria-continuidad", "sector_key": "industria", "ejemplo": True,
        "sector": "Industria y fabricación", "place": "Cataluña",
        "title": "Continuidad y redes separadas en una planta de producción",
        "summary": "Una infraestructura renovada para que un fallo en la oficina no pare la producción.",
        "services": ["Proyectos IT", "Ciberseguridad", "MGCare"],
        "challenge": "La red de la planta y la de las oficinas compartían infraestructura, los servidores estaban al final de su vida útil y no existía un plan probado para recuperar los sistemas tras una avería.",
        "solution": [
            "Renovación de servidores y almacenamiento con virtualización.",
            "Separación de la red de planta y la de oficina con reglas de acceso controladas.",
            "Copias de seguridad en local y fuera de la empresa, con pruebas de restauración.",
            "Supervisión continua de servidores, red y copias.",
        ],
        "results": [
            "Redes de planta y oficina separadas y documentadas.",
            "Plan de recuperación probado.",
            "Infraestructura preparada para crecer.",
        ],
        "stack": ["HPE", "Synology", "Fortinet", "Veeam"],
    },
    {
        "slug": "logistica-equipos", "sector_key": "logistica", "ejemplo": True,
        "sector": "Logística y distribución", "place": "España",
        "title": "Equipos listos para trabajar desde cualquier ubicación",
        "summary": "Portátiles que llegan configurados y seguros a cada persona, esté donde esté.",
        "services": ["Suministro IT", "Microsoft 365", "MGCare"],
        "challenge": "Buena parte del equipo trabaja fuera de la oficina, en almacenes e instalaciones de clientes. Preparar cada portátil llevaba tiempo y era difícil mantener todos los equipos actualizados y protegidos.",
        "solution": [
            "Alta automática de equipos con Windows Autopilot e Intune.",
            "Políticas de seguridad y actualizaciones aplicadas de forma remota.",
            "Protección de equipos con Microsoft Defender.",
            "Soporte remoto a usuarios a través del HelpDesk.",
        ],
        "results": [
            "Equipos entregados listos para usar.",
            "Todos los dispositivos con la misma configuración de seguridad.",
            "Soporte allí donde trabaja cada persona.",
        ],
        "stack": ["Microsoft Intune", "Windows Autopilot", "Microsoft Defender", "Microsoft 365"],
    },
    {
        "slug": "correduria-seguridad", "sector_key": "corredurias-seguros", "ejemplo": True,
        "sector": "Corredurías de seguros", "place": "Barcelona",
        "title": "Protección del correo y de los datos de los asegurados",
        "summary": "Doble factor, correo protegido y un dominio que nadie puede suplantar.",
        "services": ["Ciberseguridad", "Microsoft 365"],
        "challenge": "La correduría recibía intentos de suplantación por correo cada vez más elaborados y gestionaba datos personales de sus asegurados sin una política clara de accesos.",
        "solution": [
            "Doble factor de autenticación para todos los usuarios.",
            "Filtros antiphishing y antimalware en el correo.",
            "Configuración de SPF, DKIM y DMARC para proteger el dominio.",
            "Revisión de permisos sobre la documentación de clientes.",
            "Formación práctica para reconocer correos fraudulentos.",
        ],
        "results": [
            "Cuentas protegidas con doble factor.",
            "Dominio protegido frente a suplantaciones.",
            "Un equipo más preparado ante el fraude.",
        ],
        "stack": ["Microsoft 365", "Microsoft Defender", "Microsoft Entra ID", "SPF · DKIM · DMARC"],
    },
]
