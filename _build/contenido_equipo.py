"""
Equipo y fabricantes de M&G Consulting.

EQUIPO: tarjetas por área. Para mostrar la foto real de una persona, guarda
  assets/img/equipo/<clave>.webp (cuadrada, p. ej. 400×400) y añade su
  nombre en "persona". Si no hay foto se dibuja un avatar ilustrado.

FABRICANTES: los logotipos oficiales se descargan de los portales de partners
  o de los kits de marca de cada fabricante. Guarda cada logo como
  assets/img/fabricantes/<clave>.svg (o .png) y regenera. Mientras no exista
  el archivo, se muestra el nombre del fabricante en texto.
"""

TEAM = [
    {"key": "direccion", "role": "Dirección técnica", "area": "Arquitectura y proyectos", "persona": "",
     "skills": ["Auditorías", "Proyectos IT"], "status": ("online", "Disponible"), "look": 0},
    {"key": "sistemas", "role": "Sistemas y cloud", "area": "Servidores, virtualización y nube", "persona": "",
     "skills": ["Azure", "MCloud", "HPE"], "status": ("online", "Disponible"), "look": 1},
    {"key": "seguridad", "role": "Ciberseguridad y redes", "area": "Perímetro, redes y wifi", "persona": "",
     "skills": ["Fortinet", "SonicWall", "Aruba"], "status": ("away", "En visita a cliente"), "look": 2},
    {"key": "m365", "role": "Microsoft 365", "area": "Identidad, colaboración e IA", "persona": "",
     "skills": ["Intune", "SharePoint", "Copilot"], "status": ("online", "Disponible"), "look": 3},
    {"key": "helpdesk", "role": "HelpDesk", "area": "Soporte a usuarios", "persona": "",
     "skills": ["Tickets", "Soporte remoto"], "status": ("online", "Atendiendo peticiones"), "look": 4},
]

VENDORS = [
    ("microsoft", "Microsoft 365"), ("azure", "Microsoft Azure"), ("google-cloud", "Google Cloud"),
    ("mcloud", "MCloud"), ("hpe", "HPE"), ("qnap", "QNAP"), ("synology", "Synology"),
    ("aruba", "Aruba Networking"), ("ubiquiti", "Ubiquiti"), ("fortinet", "Fortinet"), ("sonicwall", "SonicWall"),
]
