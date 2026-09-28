#!/usr/bin/env python3
"""Sube la versión de Kasa: el número y la fecha en index.html y el número en sw.js.

Se corre antes de cada publicación. El número nuevo en sw.js es lo que le avisa al teléfono
que hay una versión nueva (aparece «Hay una versión nueva» en Ajustes y el punto en el engranaje).

Uso:  python3 herramientas/version.py          (fecha de hoy)
      python3 herramientas/version.py 29/9/2026 (fecha a mano)
"""
import datetime
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    hoy = datetime.date.today()
    fecha = sys.argv[1] if len(sys.argv) > 1 else f'{hoy.day}/{hoy.month}/{hoy.year}'
    ruta_html = os.path.join(RAIZ, 'index.html')
    ruta_sw = os.path.join(RAIZ, 'sw.js')
    with open(ruta_html, encoding='utf-8') as f:
        html = f.read()
    with open(ruta_sw, encoding='utf-8') as f:
        sw = f.read()
    m = re.search(r"const KASA_VERSION = \{n: (\d+), fecha: '[^']*'\};", html)
    s = re.search(r'const VERSION = (\d+);', sw)
    if not m or not s:
        raise SystemExit('No encontré KASA_VERSION en index.html o VERSION en sw.js')
    if m.group(1) != s.group(1):
        raise SystemExit(f'Las versiones no coinciden: index.html {m.group(1)}, sw.js {s.group(1)}')
    n = int(m.group(1)) + 1
    html = html[:m.start()] + f"const KASA_VERSION = {{n: {n}, fecha: '{fecha}'}};" + html[m.end():]
    sw = sw[:s.start()] + f'const VERSION = {n};' + sw[s.end():]
    with open(ruta_html, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(ruta_sw, 'w', encoding='utf-8') as f:
        f.write(sw)
    print(f'Versión {n}, del {fecha}')


if __name__ == '__main__':
    main()
