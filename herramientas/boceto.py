#!/usr/bin/env python3
"""Saca la captura de una pantalla de Kasa, tal como se ve en el teléfono, para un boceto.

Los bocetos de Kasa no se dibujan: son la app real con los cambios propuestos (la rama de la tanda),
capturada a 360 × 780 px con escala 3 (1080 px de ancho, como el teléfono de referencia). Con el
progreso que se le pase, la pantalla muestra el estado que se quiere aprobar.

  - Sirve la carpeta del repositorio en un puerto local y la abre en Chromium sin interfaz.
  - Simula la app instalada, para que no aparezca la tarjeta «Instalá Kasa» de la principal.
  - Bloquea el service worker, para que siempre se vea el index.html de la carpeta.
  - Espera a que pase la apertura (dos segundos) antes de capturar.

Uso:  python3 herramientas/boceto.py salida.png [ruta] [progreso]
        ruta      la pantalla, como en la dirección de la app (por defecto «#/», la principal)
        progreso  aprobadas y no aprobadas, separadas por comas: «1-1,1-2,1-v1» aprueba esas
                  lecciones; «!1-v2:65» la marca hecha sin aprobar, con su mejor resultado.
                  Sin progreso, la app arranca de cero.
Ejemplo: python3 herramientas/boceto.py docs/bocetos/B-01c-principal-repetir.png "#/" "1-1,1-2,1-3,1-ka,1-v1,!1-v2:65"

Requiere Python 3 con `pip install playwright` y `python3 -m playwright install chromium`.
"""
import asyncio
import functools
import http.server
import json
import os
import socketserver
import sys
import threading

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAVE = 'jp-curso-v1'   # STORE_KEY de index.html


class Silencioso(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def progreso(texto):
    lecciones = {}
    for parte in filter(None, (p.strip() for p in (texto or '').split(','))):
        if parte.startswith('!'):
            lid, _, nota = parte[1:].partition(':')
            lecciones[lid] = {'done': False, 'best': int(nota or 0), 'at': 2}
        else:
            lecciones[parte] = {'done': True, 'best': 90, 'at': 1}
    return {'v': 1, 'lessons': lecciones, 'kana': {}, 'hitos': {},
            'words': {'own': [], 'stats': {}, 'log': {}, 'updated': 0},
            'settings': {'romaji': True, 'slow': False, 'think': False, 'sfxVol': 0, 'sfxPrev': 80},
            'updated': 0, 'resetAt': 0}


async def capturar(puerto, salida, ruta, estado):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        nav = await p.chromium.launch()
        ctx = await nav.new_context(viewport={'width': 360, 'height': 780}, device_scale_factor=3,
                                    is_mobile=True, has_touch=True, service_workers='block')
        await ctx.add_init_script(
            "Object.defineProperty(window,'matchMedia',{value:q=>({matches:q.includes('standalone'),media:q,"
            "addListener(){},removeListener(){},addEventListener(){},removeEventListener(){}})});"
            f"localStorage.setItem({json.dumps(CLAVE)}, {json.dumps(json.dumps(estado))});")
        pag = await ctx.new_page()
        await pag.goto(f'http://localhost:{puerto}/index.html{ruta}')
        await pag.wait_for_timeout(3500)
        await pag.screenshot(path=salida)
        await nav.close()


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    salida = os.path.abspath(sys.argv[1])
    ruta = sys.argv[2] if len(sys.argv) > 2 else '#/'
    estado = progreso(sys.argv[3] if len(sys.argv) > 3 else '')
    manejador = functools.partial(Silencioso, directory=RAIZ)
    with socketserver.TCPServer(('localhost', 0), manejador) as srv:
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        asyncio.run(capturar(srv.server_address[1], salida, ruta, estado))
        srv.shutdown()
    print(salida)


if __name__ == '__main__':
    main()
