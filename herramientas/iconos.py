#!/usr/bin/env python3
"""Genera el ícono de la app instalable a partir del paraguas del logo (index.html).

Ícono aprobado el 28/9/2026: el wagasa solo (sin grillo ni letras), con los colores del
logo, sobre fondo crudo. Va ubicado dentro de la zona segura (un círculo del 80 % del
ícono), la única que ninguna forma de recorte de Android corta.

Salida en iconos/:
  icono.svg                       fuente, cuadrado completo
  icono-maskable-192/512.png      cuadrado completo: Android lo recorta con su forma
  icono-192/512.png               círculo con esquinas transparentes, para donde no se recorta
  apple-touch-icon.png            180 px, por si se abre en un iPhone

Uso:  python3 herramientas/iconos.py
Requiere: pip install playwright && python3 -m playwright install chromium
"""
import os
import re
from playwright.sync_api import sync_playwright

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRUDO = '#F7F3EA'
# Círculo mínimo que encierra el paraguas dibujado, en unidades del símbolo "wg"
# (medido sobre el dibujo con sus contornos): centro y radio.
CX, CY, R = 61.25, 60.75, 50.73
OCUPA = 0.39   # radio del paraguas / lado del ícono (la zona segura llega a 0.40)


def paraguas():
    with open(os.path.join(RAIZ, 'index.html'), encoding='utf-8') as f:
        html = f.read()
    m = re.search(r'<symbol id="wg"[^>]*>(.*?)<g class="grillo"', html, re.S)
    if not m:
        raise SystemExit('No encontré el símbolo del paraguas (id="wg") en index.html')
    return m.group(1)


def svg(lado=512):
    s = lado * OCUPA / R
    tx, ty = lado / 2 - CX * s, lado / 2 - CY * s
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{lado}" height="{lado}" '
            f'viewBox="0 0 {lado} {lado}"><rect width="{lado}" height="{lado}" fill="{CRUDO}"/>'
            f'<g transform="translate({tx:.3f},{ty:.3f}) scale({s:.5f})">{paraguas()}</g></svg>')


def main():
    carpeta = os.path.join(RAIZ, 'iconos')
    os.makedirs(carpeta, exist_ok=True)
    fuente = svg()
    with open(os.path.join(carpeta, 'icono.svg'), 'w', encoding='utf-8') as f:
        f.write(fuente + '\n')
    trabajos = [('icono-maskable-512.png', 512, False), ('icono-maskable-192.png', 192, False),
                ('icono-512.png', 512, True), ('icono-192.png', 192, True),
                ('apple-touch-icon.png', 180, False)]
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for nombre, lado, circulo in trabajos:
            pag = nav.new_page(viewport={'width': lado, 'height': lado})
            forma = 'border-radius:50%;overflow:hidden;' if circulo else ''
            pag.set_content(f'<html><body style="margin:0;background:transparent">'
                            f'<div style="width:{lado}px;height:{lado}px;{forma}">{svg(lado)}</div></body></html>')
            pag.screenshot(path=os.path.join(carpeta, nombre), omit_background=True)
            pag.close()
            print(nombre)
        nav.close()


if __name__ == '__main__':
    main()
