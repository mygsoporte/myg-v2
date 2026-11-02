# Web M&G Consulting — HTML5, CSS y JavaScript

Sitio estático, rápido y sin WordPress. Sin dependencias ni llamadas a terceros
(tipografías autoalojadas → sin problemas de RGPD ni banner de cookies).

## Estructura
```
index.html                 Portada
servicios/*.html           Una página por servicio (SEO)
legal/*.html               Aviso legal, privacidad y cookies (BORRADORES)
gracias.html, 404.html
contacto.php               Envío del formulario (PHP 8.1+)
css/styles.css             Estilos (variables de marca al principio)
js/main.js                 Menú, carrusel de portada, panel demo, formulario
js/skyline.js              Escena animada del skyline de Barcelona (canvas)
assets/media/              Vídeo opcional de portada (ver LEEME.txt)
assets/img, assets/fonts   Logos, iconos, imagen para redes y tipografías
.htaccess                  HTTPS, redirecciones 301 desde WordPress, seguridad, caché
robots.txt, sitemap.xml, site.webmanifest, favicon.ico
_build/build.py            Generador de páginas
_build/contenido_servicios.py   Textos de los servicios (retos, incluye, tecnologías…)
_build/contenido_casos.py       Casos de éxito (anonimizados)
casos/, casos-de-exito.html     Casos de éxito
catalogo.html, js/catalogo.js   Catálogo con buscador, filtros y solicitud de presupuesto
api/catalogo.php, api/config.php   Carga del catálogo (JSON manual, CSV exportado o API del portal)
data/catalogo.json         Catálogo (ahora con DATOS DE EJEMPLO)
```

## Editar contenido
Todas las páginas comparten cabecera y pie. Edita textos en `_build/build.py`
y regenera:
```
python3 _build/build.py
```
Los estilos se cambian directamente en `css/styles.css`.

## Publicar en Nominalia
1. Copia de seguridad completa del WordPress (archivos + base de datos).
2. Comprobar en el panel que el hosting usa PHP 8.1 o superior.
3. Mover el WordPress a una carpeta de respaldo y subir este contenido a la raíz (public_html).
4. Revisar las redirecciones 301 del `.htaccess` con los slugs reales de WordPress.
5. Enviar un mensaje de prueba desde el formulario.
6. Dar de alta `sitemap.xml` en Google Search Console.

## Pendiente

- Textos legales revisados por el asesor legal y datos del Registro Mercantil.
- Teléfono de contacto, si se quiere mostrar.
- Opcional: sustituir `mail()` por PHPMailer con SMTP de Microsoft 365.

## Catálogo
`catalogo.html` muestra los productos de `api/catalogo.php`, que en `api/config.php` puede funcionar así:
- `MODO = 'json'` (actual): usa `data/catalogo.json`. Para actualizarlo con los precios del portal de licencias:
  1. En el portal: F12 > Red > Fetch/XHR, recarga y busca la petición que devuelve `getProducts`.
     Copia la respuesta y guárdala como `pagina1.json` (y más páginas si quieres).
  2. `python3 _build/importar_catalogo.py pagina1.json [pagina2.json …]`
  3. Sube `data/catalogo.json` al servidor.
- `MODO = 'arrowsphere'`: el servidor consulta el portal automáticamente (cada `CACHE_MINUTOS`).
  Hay que rellenar `ARROW` con la URL, la consulta (query) y las variables de la petición `getProducts`.
  Si el portal exige autenticación, el token va en la variable de entorno `MYG_PORTAL_TOKEN`, nunca en el código.

El precio de compra (`buy`) del portal no se publica nunca: solo se usa el precio de venta (`sell`).
Las descripciones en español de los productos habituales están en `_build/importar_catalogo.py`
(y en `api/descripciones.json` para el modo automático).

## Imágenes de las tarjetas de servicios
Cada tarjeta de la portada muestra una ilustración de marca generada en `_build/ilustraciones.py`.
Para usar una foto propia, guárdala como `assets/img/servicios/<servicio>.webp` o `.jpg`
(p. ej. `ciberseguridad.webp`, 1600×900) y ejecuta `python3 _build/build.py`.

## Cómo trabajamos
Las cuatro fases se editan en `_build/contenido_metodo.py`. Para usar fotos en lugar de las
ilustraciones, guarda `assets/img/metodo/auditoria.webp`, `plan.webp`, `implantacion.webp`
y `gestion.webp` (formato vertical, p. ej. 900×1100) y regenera.

## Equipo y fabricantes
- Equipo: `_build/contenido_equipo.py`. Para mostrar fotos reales, guarda `assets/img/equipo/<clave>.webp`
  (cuadradas, 400×400) y rellena `persona` con el nombre si se quiere mostrar.
- Logos de fabricantes: descárgalos de los portales de partners o kits de marca oficiales y guárdalos como
  `assets/img/fabricantes/<clave>.svg` (claves: microsoft, azure, google-cloud, hpe, qnap, synology,
  aruba, ubiquiti, fortinet, sonicwall). Se muestran en gris y en color al pasar el ratón.

## Casos de éxito
- Textos en `_build/contenido_casos.py`. Los cuatro últimos son **casos de ejemplo inventados**
  (`"ejemplo": True`): sus páginas llevan `noindex` y se pueden ocultar todos de golpe con
  `PUBLICAR_EJEMPLOS = False` en `build.py`. Sustitúyelos por casos reales antes de publicar.
- Imagen de cada tarjeta: ilustración según el tipo de cliente. Para usar una foto, guarda
  `assets/img/casos/<slug-del-caso>.webp` (1600×900).
