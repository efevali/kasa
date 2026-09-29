#!/usr/bin/env python3
"""Sube la versión de Kasa: el número y la fecha en index.html y el número en sw.js.

Kasa usa versionado semántico, MAYOR.MENOR.PARCHE:
  parche  0.2.0 → 0.2.1   arreglos que no suman nada nuevo
  menor   0.2.1 → 0.3.0   algo nuevo que no rompe lo anterior (una función, una unidad)
  mayor   0.9.0 → 1.0.0   el salto grande. Mientras el primero es 0, la app está en desarrollo;
                          la 1.0.0 es la versión estable y revisada. Después de la 1.0, el mayor
                          sube solo cuando algo rompe lo anterior (por ejemplo, el progreso guardado).

Se corre antes de cada publicación. El título del commit empieza con el número («0.2.1: …») y se
suma una fila a la tabla de versiones del README.
Cambiar sw.js es lo que le avisa al teléfono que hay una versión nueva (aparece «Hay una versión
nueva» en Ajustes y el punto verde en el engranaje). El teléfono no compara números: toma lo último
que se publica. Volver atrás es publicar el contenido viejo con un número nuevo.

Uso:  python3 herramientas/version.py parche|menor|mayor [fecha]
      (la fecha, D/M/AAAA, por defecto la de hoy)
"""
import datetime
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('parche', 'menor', 'mayor'):
        raise SystemExit(__doc__)
    tipo = sys.argv[1]
    hoy = datetime.date.today()
    fecha = sys.argv[2] if len(sys.argv) > 2 else f'{hoy.day}/{hoy.month}/{hoy.year}'
    ruta_html = os.path.join(RAIZ, 'index.html')
    ruta_sw = os.path.join(RAIZ, 'sw.js')
    with open(ruta_html, encoding='utf-8') as f:
        html = f.read()
    with open(ruta_sw, encoding='utf-8') as f:
        sw = f.read()
    m = re.search(r"const KASA_VERSION = \{v: '(\d+)\.(\d+)\.(\d+)', fecha: '[^']*'\};", html)
    s = re.search(r"const VERSION = '(\d+\.\d+\.\d+)';", sw)
    if not m or not s:
        raise SystemExit('No encontré KASA_VERSION en index.html o VERSION en sw.js')
    actual = '.'.join(m.groups())
    if actual != s.group(1):
        raise SystemExit(f'Las versiones no coinciden: index.html {actual}, sw.js {s.group(1)}')
    mayor, menor, parche = (int(x) for x in m.groups())
    if tipo == 'mayor':
        mayor, menor, parche = mayor + 1, 0, 0
    elif tipo == 'menor':
        menor, parche = menor + 1, 0
    else:
        parche += 1
    nueva = f'{mayor}.{menor}.{parche}'
    html = html[:m.start()] + f"const KASA_VERSION = {{v: '{nueva}', fecha: '{fecha}'}};" + html[m.end():]
    sw = sw[:s.start()] + f"const VERSION = '{nueva}';" + sw[s.end():]
    with open(ruta_html, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(ruta_sw, 'w', encoding='utf-8') as f:
        f.write(sw)
    print(f'{actual} → {nueva}, del {fecha}')


if __name__ == '__main__':
    main()
