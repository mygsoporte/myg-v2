"""
Noticias y artículos del blog de M&G.
Para publicar una nueva: añade un diccionario al principio de la lista y regenera.
El cuerpo admite párrafos (lista de textos). Fecha en formato AAAA-MM-DD.
"""

NEWS = [
    {
        "slug": "retirada-ews-exchange-online",
        "date": "2026-09-30", "category": "Microsoft 365",
        "title": "Retirada de EWS en Exchange Online: revisa tus integraciones",
        "summary": "Microsoft retira Exchange Web Services en Exchange Online. Las aplicaciones que todavía lo usan para leer correo o calendario deben pasar a Microsoft Graph.",
        "body": [
            "Exchange Web Services (EWS) ha sido durante años la forma en que muchas aplicaciones se conectaban al correo, el calendario y los contactos de Exchange. Microsoft ha anunciado su retirada en Exchange Online y recomienda migrar esas integraciones a Microsoft Graph.",
            "Afecta sobre todo a integraciones de CRM, como la sincronización de correo y calendario de Salesforce, a herramientas de archivado y copia de buzones, y a aplicaciones desarrolladas a medida.",
            "Nuestra recomendación es hacer inventario de las aplicaciones registradas en Microsoft Entra ID, identificar las que usan EWS y planificar su migración, probando primero en un entorno de test y aplicando permisos mínimos.",
            "Si no sabes si tu empresa está afectada, podemos revisarlo contigo.",
        ],
    },
    {
        "slug": "copilot-permisos-antes-de-activar",
        "date": "2026-09-15", "category": "Inteligencia artificial",
        "title": "Antes de activar Copilot, ordena los permisos",
        "summary": "Microsoft 365 Copilot muestra la información a la que cada usuario tiene acceso. Si los permisos están desordenados, también lo estarán sus respuestas.",
        "body": [
            "Microsoft 365 Copilot trabaja con los documentos, correos y chats a los que cada usuario puede acceder. No se salta los permisos, pero sí hace mucho más fácil encontrar información que estaba compartida de más.",
            "Por eso, antes de activarlo, conviene revisar los sites de SharePoint y las carpetas compartidas de OneDrive, retirar los enlaces abiertos a toda la organización y aplicar etiquetas de confidencialidad a la información sensible.",
            "Después, lo ideal es empezar con un grupo piloto, medir el tiempo que ahorra en tareas concretas y ampliar el despliegue con formación práctica.",
        ],
    },
    {
        "slug": "copias-de-seguridad-3-2-1",
        "date": "2026-09-01", "category": "Ciberseguridad",
        "title": "Copias de seguridad 3-2-1: la regla que te salva de un ransomware",
        "summary": "Tres copias, en dos soportes distintos y una fuera de la oficina. Y, sobre todo, comprobar que se pueden restaurar.",
        "body": [
            "La regla 3-2-1 es sencilla: mantén tres copias de tus datos, en dos tipos de soporte distintos, y guarda al menos una fuera de la oficina.",
            "Frente al ransomware conviene añadir una copia inmutable, que no se pueda modificar ni borrar durante un periodo de tiempo, aunque un atacante consiga credenciales de administrador.",
            "Pero la parte más olvidada es la prueba de restauración. Una copia que nunca se ha restaurado es una suposición. Programar pruebas periódicas es lo que convierte las copias en un plan de recuperación.",
        ],
    },
]
