<?php
/**
 * Configuración del catálogo — M&G Consulting
 *
 * MODO:
 *   'json'        → la web usa data/catalogo.json tal cual (generado con _build/importar_catalogo.py)
 *   'arrowsphere' → el servidor consulta el portal de licencias (API GraphQL) y guarda una copia en caché
 *
 * Las credenciales del portal se leen de variables de entorno del servidor y nunca llegan al navegador.
 * El precio de compra ("buy") del portal NUNCA se publica.
 */
// Token del portal (solo si la API lo exige). Se busca, por este orden:
//  1) variable de entorno MYG_PORTAL_TOKEN (servidor propio / Docker)
//  2) archivo FUERA de la carpeta pública: ../privado/portal-token.txt (hosting compartido, p. ej. Nominalia)
$TOKEN_PORTAL = getenv('MYG_PORTAL_TOKEN') ?: trim((string)@file_get_contents(dirname(__DIR__, 2) . '/privado/portal-token.txt'));

return [
    'MODO' => 'json',

    'MARGEN'        => 0.0,   // 0.10 = +10 % sobre el precio de venta del portal
    'CACHE_MINUTOS' => 360,   // cada cuánto se vuelve a consultar el portal

    // ---------------- Modo 'arrowsphere' ----------------
    // Datos que se copian de la petición "getProducts" en F12 > Red (pestañas Encabezados y Carga útil)
    'ARROW' => [
        'URL'      => '',          // "URL de solicitud" de la petición
        'QUERY'    => <<<'GQL'
# Pega aquí el valor de "query" de la carga útil (empieza por "query getProducts…")
GQL,
        // Pega aquí el objeto "variables" de la carga útil. Usa "__PAGINA__" y "__POR_PAGINA__"
        // donde aparezcan el número de página y los productos por página.
        'VARIABLES' => [],
        'HEADERS'  => [
            'Content-Type: application/json',
            'Accept: application/json',
            // Si la petición lleva autenticación, descomenta la cabecera que use el portal:
            // 'Authorization: Bearer ' . $TOKEN_PORTAL,
            // 'apiKey: ' . $TOKEN_PORTAL,
        ],
        'PAGINAS'     => 5,    // páginas a leer (ordenadas por más vendidos) → 5 × 50 = 250 productos
        'POR_PAGINA'  => 50,
        'SOLO_FABRICANTES' => [],             // p. ej. ['Microsoft'] para mostrar solo Microsoft
        'EXCLUIR'     => '/trial|education|student|faculty|charity|nonprofit|gov/i',  // por nombre
    ],
];
