"""
Genera data/equipo.json a partir de un CSV que rellenan los propios compañeros.

Uso:   py _build/importar_equipo.py equipo.csv      y después   py _build/build.py
CSV (UTF-8, separado por comas o punto y coma), con cabecera:
    nombre,cargo,linkedin,foto,consentimiento
  - foto: ruta a una imagen (jpg/png/webp) en tu PC; se recorta cuadrada y se guarda en assets/img/equipo/
  - consentimiento: debe valer "si". Las filas sin consentimiento NO se publican.
  - linkedin: URL https de linkedin.com (si queda vacía, la tarjeta sale sin enlace)
La empresa (empresa.linkedin) se conserva del equipo.json actual.
"""
import csv, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "data", "equipo.json")


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def procesar_foto(origen, nombre):
    from PIL import Image, ImageOps
    rel = f"assets/img/equipo/{slug(nombre)}.webp"
    with Image.open(origen) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        im = ImageOps.fit(im, (400, 400), Image.LANCZOS, centering=(0.5, 0.35))
        os.makedirs(os.path.join(ROOT, "assets", "img", "equipo"), exist_ok=True)
        im.save(os.path.join(ROOT, rel), quality=85)
    return rel


def main(ruta):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        muestra = f.read(2048)
        f.seek(0)
        filas = list(csv.DictReader(f, delimiter=";" if muestra.count(";") > muestra.count(",") else ","))
    with open(DEST, encoding="utf-8") as f:
        datos = json.load(f)
    personas, omitidas = [], []
    for r in filas:
        nombre = (r.get("nombre") or "").strip()
        if not nombre:
            continue
        if (r.get("consentimiento") or "").strip().lower() not in ("si", "sí"):
            omitidas.append(nombre)
            continue
        p = {"nombre": nombre, "cargo": (r.get("cargo") or "").strip()}
        url = (r.get("linkedin") or "").strip()
        if url.startswith("https://") and "linkedin.com/" in url:
            p["linkedin"] = url
        elif url:
            print(f"AVISO {nombre}: URL de LinkedIn no válida, se omite el enlace")
        foto = (r.get("foto") or "").strip().strip('"')
        if foto:
            if os.path.exists(foto):
                p["foto"] = procesar_foto(foto, nombre)
            else:
                print(f"AVISO {nombre}: no existe la foto {foto}")
        personas.append(p)
    datos["personas"] = personas
    with open(DEST, "w", encoding="utf-8", newline="\n") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"{len(personas)} personas publicadas; sin consentimiento (no publicadas): {omitidas or 'ninguna'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
