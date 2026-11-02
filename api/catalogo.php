<?php
/**
 * Catálogo de M&G Consulting — endpoint JSON
 * GET /api/catalogo.php → { actualizado, fuente, moneda, iva_incluido, productos: [...] }
 */
declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$cfg   = require __DIR__ . '/config.php';
$data  = dirname(__DIR__) . '/data';
$cache = $data . '/cache-catalogo.json';

function salir(array $out): never {
    header('Cache-Control: public, max-age=300');
    echo json_encode($out, JSON_UNESCAPED_UNICODE);
    exit;
}
function leer_json(string $f): array { return is_file($f) ? (json_decode((string)file_get_contents($f), true) ?: []) : []; }

if ($cfg['MODO'] === 'json') salir(leer_json($data . '/catalogo.json') ?: ['productos' => []]);

if (is_file($cache) && (time() - filemtime($cache)) < $cfg['CACHE_MINUTOS'] * 60) salir(leer_json($cache));

/* ---------------- ArrowSphere (GraphQL) ---------------- */
const CATEGORIAS = [
    '/copilot/i' => 'IA',
    '/defender|security|entra|purview|intune/i' => 'Seguridad',
    '/power bi|fabric/i' => 'Datos y análisis',
    '/azure|aws|amazon/i' => 'Cloud',
    '/windows server|sql server|\bcal\b|core license/i' => 'Licencias de servidor',
    '/project|planner|visio/i' => 'Productividad',
    '/365|office|exchange|teams|sharepoint|onedrive/i' => 'Microsoft 365',
];

function categoria(string $texto, string $clasif): string {
    foreach (CATEGORIAS as $re => $cat) if (preg_match($re, $texto)) return $cat;
    return ['IaaS' => 'Cloud', 'PSW' => 'Licencias de servidor'][$clasif] ?? 'Otras licencias';
}

function convertir(array $p, array $cfg, array $desc): ?array {
    if (empty($p['isEnabled']) || !empty($p['isTrial'])) return null;
    $b = $p['defaultPriceBand'] ?? [];
    if (isset($b['isBuyable']) && !$b['isBuyable']) return null;
    $nombre = $p['name'] ?? ($b['name'] ?? '');
    if ($nombre === '' || preg_match($cfg['ARROW']['EXCLUIR'], $nombre)) return null;
    $fab = $p['identifiers']['vendor']['name'] ?? '';
    if ($cfg['ARROW']['SOLO_FABRICANTES'] && !in_array($fab, $cfg['ARROW']['SOLO_FABRICANTES'], true)) return null;

    $familia = $b['family']['name'] ?? '';
    $clasif  = $p['classification'] ?? '';
    $ciclo   = (int)($b['billing']['cycle'] ?? 0);
    $plazo   = (int)($b['billing']['term'] ?? 0);
    $venta   = isset($b['prices']['sell']) ? (float)$b['prices']['sell'] : null;   // nunca 'buy'
    $consumo = $venta === 0.0 && $clasif === 'IaaS';
    $precio  = $venta ? round($venta * (1 + (float)$cfg['MARGEN']), 2) : null;

    return [
        'id'          => (string)($p['id'] ?? ''),
        'nombre'      => strip_tags($nombre),
        'fabricante'  => strip_tags($fab),
        'categoria'   => categoria("$nombre $familia", $clasif),
        'familia'     => strip_tags($familia),
        'descripcion' => $desc[$nombre] ?? strip_tags($familia),
        'precio'      => $consumo ? null : $precio,
        'precio_tipo' => $consumo ? 'consumo' : ($precio ? 'fijo' : 'consultar'),
        'periodo'     => $ciclo === 720 ? 'mes' : ($ciclo === 8640 ? 'año' : 'único'),
        'unidad'      => ['SaaS' => 'usuario', 'PSW' => 'licencia'][$clasif] ?? '',
        'compromiso'  => [8640 => 'Anual', 720 => 'Mensual'][$plazo] ?? '',
        'complemento' => !empty($p['isAddon']),
        'sku'         => (string)($p['identifiers']['vendor']['sku'] ?? ''),
        'destacado'   => false,
    ];
}

function reemplazar($v, int $pag, int $por) {
    if (is_array($v)) { foreach ($v as $k => $x) $v[$k] = reemplazar($x, $pag, $por); return $v; }
    if ($v === '__PAGINA__') return $pag;
    if ($v === '__POR_PAGINA__') return $por;
    return $v;
}

try {
    $a = $cfg['ARROW'];
    if (!$a['URL']) throw new RuntimeException('Falta la URL del portal en api/config.php');
    $desc = leer_json(__DIR__ . '/descripciones.json');
    $productos = []; $vistos = [];
    for ($pag = 1; $pag <= $a['PAGINAS']; $pag++) {
        $ch = curl_init($a['URL']);
        curl_setopt_array($ch, [
            CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 30,
            CURLOPT_HTTPHEADER => $a['HEADERS'],
            CURLOPT_POSTFIELDS => json_encode(['query' => $a['QUERY'], 'variables' => reemplazar($a['VARIABLES'], $pag, $a['POR_PAGINA'])]),
        ]);
        $raw = curl_exec($ch); $code = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
        if (!$raw || $code >= 400) throw new RuntimeException("El portal respondió $code en la página $pag");
        $json = json_decode($raw, true);
        $lista = $json['data']['getProducts']['products'] ?? null;
        if ($lista === null) throw new RuntimeException('Respuesta inesperada: ' . substr($raw, 0, 200));
        foreach ($lista as $p) {
            $item = convertir($p, $cfg, $desc);
            if ($item && !isset($vistos[$item['id']])) { $vistos[$item['id']] = true; $productos[] = $item; }
        }
        $total = (int)($json['data']['getProducts']['pagination']['totalPage'] ?? $pag);
        if ($pag >= $total) break;
    }
    $n = 0;
    foreach ($productos as &$p) { if ($p['precio'] && $n < 6) { $p['destacado'] = true; $n++; } }
    unset($p);
    // Hardware, MCloud y otros productos propios (precio a consultar)
    foreach ((leer_json($data . '/catalogo-extra.json')['productos'] ?? []) as $x) {
        if (!isset($vistos[$x['id']])) { $vistos[$x['id']] = true; $productos[] = $x; }
    }
    $out = ['actualizado' => date('Y-m-d H:i'), 'fuente' => 'portal', 'moneda' => 'EUR', 'iva_incluido' => false, 'productos' => $productos];
    file_put_contents($cache, json_encode($out, JSON_UNESCAPED_UNICODE), LOCK_EX);
    salir($out);
} catch (Throwable $e) {
    error_log('Catálogo M&G: ' . $e->getMessage());
    salir(leer_json($cache) ?: (leer_json($data . '/catalogo.json') ?: ['productos' => []]));
}
