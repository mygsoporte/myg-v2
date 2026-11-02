#!/usr/bin/env python3
"""
Importa productos del portal de licencias (ArrowSphere / mycloudportal) al catálogo de la web.

Uso manual (sin API):
  1. En el portal, F12 > Red > Fetch/XHR, recarga y localiza la petición que devuelve
     "getProducts". Clic derecho > Copiar > Copiar respuesta, y guárdala como archivo .json
     (puedes guardar varias páginas: pagina1.json, pagina2.json…).
  2. Ejecuta:  python3 _build/importar_catalogo.py pagina1.json [pagina2.json …]
  3. Se genera data/catalogo.json. Súbelo al servidor junto con la web.

IMPORTANTE: el precio de compra ("buy") NUNCA se copia al catálogo público.
"""
import json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARGEN = 0.0   # 0.10 = +10 % sobre el precio de venta del portal (normalmente 0)

# Descripciones en español para los productos más habituales (por nombre exacto)
DESCRIPCIONES = {
    "Microsoft 365 Business Basic": "Correo profesional, Teams, SharePoint y OneDrive con 1 TB por usuario. Aplicaciones de Office en versión web y móvil.",
    "Microsoft 365 Business Standard": "Todo lo de Business Basic más las aplicaciones de escritorio de Office: Word, Excel, PowerPoint y Outlook.",
    "Microsoft 365 Business Premium": "Business Standard más seguridad avanzada: Defender for Business, Intune y acceso condicional.",
    "Microsoft 365 Apps for business": "Aplicaciones de escritorio de Office y 1 TB en OneDrive, sin correo de Exchange.",
    "Exchange Online (Plan 1)": "Buzón de correo profesional de 50 GB con calendario y contactos.",
    "Exchange Online (Plan 2)": "Buzón de 100 GB con archivo de gran capacidad y funciones avanzadas de cumplimiento.",
    "Microsoft 365 Copilot": "Asistente de IA integrado en Word, Excel, PowerPoint, Outlook y Teams.",
    "Microsoft 365 Copilot Business": "Copilot para empresas de hasta 300 usuarios, integrado en las aplicaciones de Microsoft 365.",
    "Microsoft Defender for Office 365 (Plan 1)": "Protección avanzada del correo frente a phishing, enlaces y adjuntos maliciosos.",
    "Power BI Pro": "Informes y paneles interactivos para analizar y compartir los datos de la empresa.",
    "Planner and Project Plan 3": "Gestión de proyectos con planificación, recursos y seguimiento.",
    "Office 365 E3": "Aplicaciones de Office, correo de 100 GB, Teams y herramientas de cumplimiento, sin límite de usuarios.",
    "Windows Server 2025 Standard - 16 Core License Pack": "Licencia perpetua para servidores físicos o virtuales (paquete de 16 núcleos).",
    "Microsoft Azure Subscription (Azure Plan)": "Suscripción de Azure con pago por uso: solo pagas los recursos que consumes.",
    "AWS End-Customer Account Model (ECAM)": "Cuenta de Amazon Web Services gestionada, con facturación según consumo.",
}

# Categoría según palabras del nombre o la familia (el primer acierto manda)
CATEGORIAS = [
    (r"copilot", "IA"),
    (r"defender|security|entra|purview|intune", "Seguridad"),
    (r"power bi|fabric", "Datos y análisis"),
    (r"azure|aws|amazon", "Cloud"),
    (r"windows server|sql server|cal\b|core license", "Licencias de servidor"),
    (r"project|planner|visio", "Productividad"),
    (r"365|office|exchange|teams|sharepoint|onedrive", "Microsoft 365"),
]


def categoria(nombre, familia, clasificacion):
    texto = f"{nombre} {familia}".lower()
    for patron, cat in CATEGORIAS:
        if re.search(patron, texto):
            return cat
    return {"IaaS": "Cloud", "PSW": "Licencias de servidor"}.get(clasificacion, "Otras licencias")


def convertir(producto):
    """Convierte un producto de ArrowSphere al formato del catálogo. Nunca incluye el precio de compra."""
    if not producto.get("isEnabled") or producto.get("isTrial"):
        return None
    banda = producto.get("defaultPriceBand") or {}
    if not banda.get("isBuyable", True):
        return None
    nombre = producto.get("name") or banda.get("name")
    if not nombre:
        return None
    familia = (banda.get("family") or {}).get("name", "")
    clasificacion = producto.get("classification", "")
    billing = banda.get("billing") or {}
    ciclo, plazo = billing.get("cycle", 0), billing.get("term", 0)

    venta = (banda.get("prices") or {}).get("sell")
    try:
        venta = float(venta)
    except (TypeError, ValueError):
        venta = None
    consumo = venta == 0 and clasificacion == "IaaS"
    precio = round(venta * (1 + MARGEN), 2) if venta else None

    periodo = "mes" if ciclo == 720 else "año" if ciclo == 8640 else "único"
    compromiso = {8640: "Anual", 720: "Mensual"}.get(plazo, "")
    unidad = {"SaaS": "usuario", "PSW": "licencia", "IaaS": ""}.get(clasificacion, "")

    return {
        "id": producto.get("id") or (producto.get("identifiers") or {}).get("vendor", {}).get("sku"),
        "nombre": nombre,
        "fabricante": ((producto.get("identifiers") or {}).get("vendor") or {}).get("name", ""),
        "categoria": categoria(nombre, familia, clasificacion),
        "familia": familia,
        "descripcion": DESCRIPCIONES.get(nombre, familia),
        "precio": None if consumo else precio,
        "precio_tipo": "consumo" if consumo else ("fijo" if precio else "consultar"),
        "periodo": periodo,
        "unidad": unidad,
        "compromiso": compromiso,
        "complemento": bool(producto.get("isAddon")),
        "sku": ((producto.get("identifiers") or {}).get("vendor") or {}).get("sku", ""),
        "destacado": False,
    }


def main(archivos):
    productos, vistos = [], set()
    for ruta in archivos:
        datos = json.load(open(ruta, encoding="utf-8"))
        lista = (((datos.get("data") or {}).get("getProducts") or {}).get("products")) or []
        for p in lista:
            item = convertir(p)
            if item and item["id"] not in vistos:
                vistos.add(item["id"])
                productos.append(item)
    # Los primeros (más vendidos en el portal) con precio fijo se marcan como destacados
    for item in [p for p in productos if p["precio"]][:6]:
        item["destacado"] = True
    # Hardware, MCloud y otros productos propios (precio a consultar)
    extra = os.path.join(ROOT, "data", "catalogo-extra.json")
    if os.path.exists(extra):
        for item in json.load(open(extra, encoding="utf-8")).get("productos", []):
            if item["id"] not in vistos:
                vistos.add(item["id"]); productos.append(item)
    salida = {
        "actualizado": date.today().isoformat(),
        "fuente": "portal",
        "moneda": "EUR",
        "iva_incluido": False,
        "productos": productos,
    }
    destino = os.path.join(ROOT, "data", "catalogo.json")
    json.dump(salida, open(destino, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(productos)} productos guardados en {destino}")
    assert all("buy" not in json.dumps(p) for p in productos)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
