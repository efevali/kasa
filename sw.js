/* Service worker de Kasa.
   Guarda la app entera en el teléfono para que funcione sin conexión, y maneja las versiones:
   cuando se publica una versión nueva, el teléfono la baja en segundo plano y queda esperando
   hasta que se toca «Actualizar» en Ajustes (o hasta que la app se cierra del todo).

   VERSION tiene que coincidir con KASA_VERSION de index.html: herramientas/version.py sube las dos.
   Cualquier cambio en este archivo es lo que le avisa al teléfono que hay algo nuevo: el teléfono no
   compara números, toma lo último que se publica. El número (MAYOR.MENOR.PARCHE) es para ordenarnos. */
const VERSION = '0.4.0';
const CACHE = 'kasa-v' + VERSION;
const ARCHIVOS = [
  './',
  'index.html',
  'manifest.webmanifest',
  'fuentes/klee-one-400.woff2',
  'fuentes/klee-one-600.woff2',
  'fuentes/shippori-mincho-600.woff2',
  'fuentes/shippori-mincho-700.woff2',
  'fuentes/zen-kaku-gothic-new-400.woff2',
  'fuentes/zen-kaku-gothic-new-500.woff2',
  'fuentes/zen-kaku-gothic-new-700.woff2',
  'iconos/icono-192.png',
  'iconos/icono-512.png',
  'iconos/icono-maskable-192.png',
  'iconos/icono-maskable-512.png',
  'iconos/apple-touch-icon.png'
];

// Instalar: bajar todo de nuevo del servidor (sin copias viejas intermedias) y guardarlo junto
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ARCHIVOS.map(u => new Request(u, {cache: 'reload'})))));
});

// Activar: borrar lo guardado por versiones anteriores y tomar la app abierta
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(ks => Promise.all(ks.filter(k => k.startsWith('kasa-') && k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// «Actualizar» en Ajustes: la versión que espera pasa a ser la activa
self.addEventListener('message', e => { if (e.data === 'actualizar') self.skipWaiting(); });

// Todo sale de lo guardado; la red solo si falta algo
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (req.mode === 'navigate'){
    e.respondWith(
      caches.open(CACHE)
        .then(c => c.match('index.html').then(r => r || c.match('./')))
        .then(r => r || fetch(req))
    );
    return;
  }
  e.respondWith(caches.match(req, {ignoreSearch: true}).then(r => r || fetch(req)));
});
