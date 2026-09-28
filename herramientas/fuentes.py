#!/usr/bin/env python3
"""Recorta las tres tipografías de Kasa a lo que usa el curso y las deja en fuentes/.

Kasa lleva sus tipografías dentro de la app para que se vean igual sin conexión.
Las originales pesan muchísimo (miles de kanji), así que se recortan a:
  - todos los caracteres que aparecen en index.html (textos, palabras, frases);
  - hiragana y katakana completos, signos japoneses y latinos, para que el curso
    pueda crecer sin regenerar a cada rato.

Cuándo correrlo: cada vez que index.html sume caracteres nuevos (por ejemplo,
cuando el curso empiece a enseñar kanji). Si falta un carácter, el teléfono lo
dibuja con su letra de sistema: no se rompe nada, pero se nota.

Uso:  python3 herramientas/fuentes.py
Requiere: pip install fonttools brotli
Las originales se bajan del repositorio de Google Fonts (licencia SIL OFL 1.1)
a una carpeta temporal; no se guardan en el repositorio.
"""
import os
import sys
import urllib.request
from fontTools import subset

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(os.path.expanduser('~'), '.cache', 'kasa-fuentes')
BASE = 'https://raw.githubusercontent.com/google/fonts/main/ofl/'

# (archivo original en Google Fonts, archivo recortado en fuentes/)
FUENTES = [
    ('kleeone/KleeOne-Regular.ttf', 'klee-one-400.woff2'),
    ('kleeone/KleeOne-SemiBold.ttf', 'klee-one-600.woff2'),
    ('shipporimincho/ShipporiMincho-SemiBold.ttf', 'shippori-mincho-600.woff2'),
    ('shipporimincho/ShipporiMincho-Bold.ttf', 'shippori-mincho-700.woff2'),
    ('zenkakugothicnew/ZenKakuGothicNew-Regular.ttf', 'zen-kaku-gothic-new-400.woff2'),
    ('zenkakugothicnew/ZenKakuGothicNew-Medium.ttf', 'zen-kaku-gothic-new-500.woff2'),
    ('zenkakugothicnew/ZenKakuGothicNew-Bold.ttf', 'zen-kaku-gothic-new-700.woff2'),
]
LICENCIAS = [('kleeone/OFL.txt', 'OFL-Klee-One.txt'),
             ('shipporimincho/OFL.txt', 'OFL-Shippori-Mincho.txt'),
             ('zenkakugothicnew/OFL.txt', 'OFL-Zen-Kaku-Gothic-New.txt')]

# Bloques fijos, además de lo que aparece en index.html
RANGOS = [
    (0x0020, 0x007E),  # latín básico
    (0x00A0, 0x00FF),  # latín con acentos, «», ¿¡, º
    (0x2010, 0x206F),  # guiones, comillas, puntos suspensivos, ‹ ›
    (0x2190, 0x21FF),  # flechas
    (0x3000, 0x303F),  # signos japoneses (、。「」〜)
    (0x3040, 0x309F),  # hiragana
    (0x30A0, 0x30FF),  # katakana
    (0xFF01, 0xFF60),  # formas de ancho completo (！？（）)
]


def bajar(ruta, destino):
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        return
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    print('Bajando', ruta)
    urllib.request.urlretrieve(BASE + ruta, destino)


def main():
    with open(os.path.join(RAIZ, 'index.html'), encoding='utf-8') as f:
        texto = f.read()
    cps = {ord(c) for c in texto if ord(c) >= 0x20}
    for a, b in RANGOS:
        cps.update(range(a, b + 1))
    salida = os.path.join(RAIZ, 'fuentes')
    os.makedirs(salida, exist_ok=True)
    for ruta, nombre in FUENTES:
        original = os.path.join(CACHE, os.path.basename(ruta))
        bajar(ruta, original)
        opciones = subset.Options()
        opciones.flavor = 'woff2'
        # las funciones tipográficas por defecto incluyen las formas verticales (かさ del logo, escrito en vertical)
        opciones.name_IDs = ['*']
        opciones.name_languages = ['*']
        opciones.notdef_outline = True
        opciones.hinting = False
        fuente = subset.load_font(original, opciones)
        recorte = subset.Subsetter(opciones)
        recorte.populate(unicodes=cps)
        recorte.subset(fuente)
        destino = os.path.join(salida, nombre)
        subset.save_font(fuente, destino, opciones)
        print(f'{nombre}: {os.path.getsize(destino) // 1024} KB')
    for ruta, nombre in LICENCIAS:
        bajar(ruta, os.path.join(CACHE, nombre))
        with open(os.path.join(CACHE, nombre), encoding='utf-8') as f:
            contenido = f.read()
        with open(os.path.join(salida, nombre), 'w', encoding='utf-8') as f:
            f.write(contenido)


if __name__ == '__main__':
    sys.exit(main())
