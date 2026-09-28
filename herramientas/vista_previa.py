#!/usr/bin/env python3
"""Arma la vista previa de Kasa para publicarla como artefacto en claude.ai.

La vista previa es el mismo index.html, con dos diferencias que pide el visor de artefactos:
  - las tipografías van adentro del archivo (el visor no carga archivos de fuentes sueltos);
  - sin manifiesto ni íconos (ahí no se instala nada; la fila de versión aparece sin botón).

Uso:  python3 herramientas/vista_previa.py [archivo de salida]
      (por defecto, vista-previa.html junto a la carpeta del repositorio, fuera de él)
"""
import base64
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    salida = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(RAIZ), 'vista-previa.html')
    with open(os.path.join(RAIZ, 'index.html'), encoding='utf-8') as f:
        html = f.read()

    def adentro(m):
        with open(os.path.join(RAIZ, 'fuentes', m.group(1)), 'rb') as f:
            datos = base64.b64encode(f.read()).decode('ascii')
        return f'url(data:font/woff2;base64,{datos})'

    html, n = re.subn(r'url\(fuentes/([a-z0-9-]+\.woff2)\)', adentro, html)
    html = re.sub(r'<link rel="(manifest|icon|apple-touch-icon)"[^>]*>\n', '', html)
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    with open(salida, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{salida}: {n} tipografías adentro, {os.path.getsize(salida) // 1024} KB')


if __name__ == '__main__':
    main()
