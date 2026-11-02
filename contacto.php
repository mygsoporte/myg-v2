<?php
/**
 * M&G Consulting — envío del formulario de contacto
 *
 * Funciona con y sin JavaScript:
 *  - Con JS (fetch + Accept: application/json) responde JSON.
 *  - Sin JS redirige a gracias.html o de vuelta al formulario.
 *
 * RECOMENDADO: usar SMTP autenticado de Microsoft 365 con PHPMailer
 * (composer require phpmailer/phpmailer) en lugar de mail().
 */
declare(strict_types=1);

const DESTINO   = 'info@myg.consulting';
const REMITENTE = 'no-reply@myg.consulting';   // buzón o alias válido del dominio
const TIEMPO_MINIMO = 3;                      // segundos: los bots envían al instante

$wantsJson = str_contains($_SERVER['HTTP_ACCEPT'] ?? '', 'application/json');

function responder(bool $ok, string $error = ''): never {
    global $wantsJson;
    if ($wantsJson) {
        header('Content-Type: application/json; charset=utf-8');
        http_response_code($ok ? 200 : 422);
        echo json_encode(['ok' => $ok, 'error' => $error]);
    } else {
        header('Location: ' . ($ok ? 'gracias.html' : 'index.html#contacto'), true, 303);
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); header('Allow: POST'); exit; }

// Solo se acepta desde nuestro propio sitio (frena envíos cruzados) y con un tamaño razonable
$origen = $_SERVER['HTTP_ORIGIN'] ?? ($_SERVER['HTTP_REFERER'] ?? '');
if ($origen !== '' && !in_array(parse_url($origen, PHP_URL_HOST), ['myg.consulting', 'www.myg.consulting'], true)) {
    http_response_code(403); exit;
}
if ((int)($_SERVER['CONTENT_LENGTH'] ?? 0) > 20000) { http_response_code(413); exit; }

// Antispam: campo trampa y tiempo mínimo de relleno
if (!empty($_POST['web'])) responder(true);   // fingimos éxito ante bots
$ts = (int)($_POST['ts'] ?? 0);
if ($wantsJson && $ts <= 0) responder(true);  // el JS siempre envía la marca de tiempo; sin ella es un bot
if ($ts > 0 && (time() - intdiv($ts, 1000)) < TIEMPO_MINIMO) responder(true);

// Límite simple por IP: 5 envíos por hora (IP guardada solo como hash, con bloqueo de fichero)
$ipFile = sys_get_temp_dir() . '/myg_form_' . hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . date('Y-m-d'));
$fh = @fopen($ipFile, 'c+');
if ($fh && flock($fh, LOCK_EX)) {
    $hits = array_filter(explode(',', (string)stream_get_contents($fh)), fn($t) => $t && (time() - (int)$t) < 3600);
    if (count($hits) >= 5) { flock($fh, LOCK_UN); fclose($fh); responder(false, 'limite'); }
    $hits[] = time();
    ftruncate($fh, 0); rewind($fh); fwrite($fh, implode(',', $hits));
    flock($fh, LOCK_UN);
}
if ($fh) fclose($fh);

$limpiar = fn(string $k, int $max) => mb_substr(trim(strip_tags((string)($_POST[$k] ?? ''))), 0, $max);
$nombre   = $limpiar('nombre', 120);
$empresa  = $limpiar('empresa', 120);
$telefono = $limpiar('telefono', 30);
$asunto   = str_replace(["\r", "\n"], ' ', $limpiar('asunto', 80)) ?: 'Consulta web';
$mensaje  = $limpiar('mensaje', 5000);
$email    = filter_var(trim((string)($_POST['email'] ?? '')), FILTER_VALIDATE_EMAIL);

if (!$nombre || !$email || mb_strlen($mensaje) < 10 || ($_POST['consentimiento'] ?? '') !== 'si') {
    responder(false, 'validacion');
}

$cuerpo = "Nueva consulta desde la web\n\n"
        . "Nombre:   $nombre\nEmpresa:  $empresa\nCorreo:   $email\nTeléfono: $telefono\nAsunto:   $asunto\n\n"
        . "$mensaje\n\n---\nIP: " . ($_SERVER['REMOTE_ADDR'] ?? '') . ' · ' . date('d/m/Y H:i');

$headers = implode("\r\n", [
    'From: Web M&G <' . REMITENTE . '>',
    'Reply-To: ' . $email,           // $email ya validado: no admite saltos de línea
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
]);

$ok = @mail(DESTINO, '=?UTF-8?B?' . base64_encode("[Web] $asunto — $nombre") . '?=', $cuerpo, $headers, '-f' . REMITENTE);
responder($ok, $ok ? '' : 'envio');
