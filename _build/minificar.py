"""
Minifica css/styles.css y js/*.js → *.min.css / *.min.js (los originales no se tocan).
Uso:  py _build/minificar.py   y después   py _build/build.py
Requiere Node.js (usa npx esbuild). Si no hay Node, la web sigue funcionando con los ficheros sin minificar.
"""
import glob, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fuentes = [os.path.join(ROOT, "css", "styles.css")] + [
    f for f in glob.glob(os.path.join(ROOT, "js", "*.js")) if not f.endswith(".min.js")
]
for src in fuentes:
    root, ext = os.path.splitext(src)
    # Rutas relativas y cwd=ROOT: en Windows cmd.exe falla con rutas que contienen "&" (p. ej. "WebM&G")
    rel = os.path.relpath(src, ROOT).replace("\\", "/")
    out = os.path.splitext(rel)[0] + ".min" + ext
    subprocess.run(
        ["npx", "--yes", "esbuild@0.24.0", rel, "--minify", f"--outfile={out}", "--log-level=warning"],
        check=True, shell=(os.name == "nt"), cwd=ROOT,
    )
    print("minificado", os.path.relpath(f"{root}.min{ext}", ROOT), os.path.getsize(src), "->", os.path.getsize(f"{root}.min{ext}"))
