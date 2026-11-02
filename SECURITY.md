# Seguridad

## Cómo informar de una vulnerabilidad
Escribe a **info@myg.consulting** con el asunto «Seguridad web». Incluye pasos para reproducirla y, si es posible, una captura. No publiques el fallo antes de que lo hayamos corregido y no accedas a datos de terceros.

## Política de seguridad del sitio
- Sitio estático (HTML/CSS/JS) sin dependencias de terceros ni cookies. Las tipografías están autoalojadas.
- CSP estricta (`default-src 'self'`, sin `unsafe-inline`), HSTS, `nosniff`, COOP/CORP y `frame-ancestors 'none'` en `.htaccess`.
- Único código de servidor: `contacto.php` (formulario) y `api/catalogo.php` (catálogo).
- No se guardan secretos en el repositorio. El token del portal de licencias, si se usa, va en la variable de entorno `MYG_PORTAL_TOKEN` o en `../privado/portal-token.txt` (fuera de la carpeta pública).

## Para quien despliega
- Comprobar tras subir: `/README.md`, `/docs/`, `/_build/build.py` y `/.backup-originales/` deben devolver 403/404.
- No subir `.backup-originales/`, `docs/`, `video/` ni `*.zip`.
- Revisar SPF, DKIM y DMARC del dominio para el correo del formulario.
