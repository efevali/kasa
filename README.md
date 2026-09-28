# Kasa

Curso de japonés desde cero —primero los kana, después las palabras— hecho como app instalable (PWA) para Android.

- **App:** https://kasalearn.github.io/kasa/ (se abre en Chrome y se instala desde el menú ⋮ → «Instalar app»)
- **Vista previa:** el artefacto «Kasa» en claude.ai, donde se prueba cada cambio antes de publicarlo aquí.

## Qué hay en cada archivo

| Archivo o carpeta | Qué es |
|---|---|
| `index.html` | La app entera: textos, lecciones, dibujos, sonidos y código. Al principio del CSS está la **guía de estilo**, con todas las reglas acordadas. |
| `manifest.webmanifest` | La ficha que Android lee para instalarla: nombre, ícono, colores, que abra sin barra del navegador y en vertical. |
| `sw.js` | El *service worker*: guarda la app en el teléfono para que funcione sin conexión y maneja las versiones nuevas. |
| `fuentes/` | Klee One, Shippori Mincho y Zen Kaku Gothic New, recortadas a lo que usa el curso, con sus licencias (SIL OFL 1.1). |
| `iconos/` | El ícono (el wagasa del logo, solo, sobre crudo) en los tamaños que pide Android. |
| `herramientas/` | Ayudantes para el armado: `version.py`, `fuentes.py`, `iconos.py` y `vista_previa.py` (ver abajo). |
| `.nojekyll` | Le indica a GitHub Pages que publique los archivos tal cual, sin procesarlos. |

## Cómo se publica una versión nueva

1. Los cambios se hacen en `index.html` y se prueban en la vista previa (el artefacto «Kasa», abierto en Chrome), armada con `python3 herramientas/vista_previa.py`.
2. Si el curso sumó caracteres nuevos (por ejemplo, kanji), se regeneran las tipografías:
   `python3 herramientas/fuentes.py`
3. Se sube el número de versión, en `index.html` y en `sw.js` a la vez:
   `python3 herramientas/version.py`
4. Se guarda el cambio en el repositorio (commit) y se sube a `main` (push). GitHub Pages la publica en un minuto o dos.

En el teléfono, la app encuentra la versión nueva al abrirse, al volver a ella después de un rato o con «Buscar» en Ajustes. Aparece «Hay una versión nueva» en Ajustes y un punto verde en el engranaje; «Actualizar» la reabre ya actualizada. Si no se toca, entra sola al cerrar la app del todo y volver a abrirla.

## Progreso

Se guarda en el teléfono, dentro de los datos de Chrome para este sitio. Desinstalar la app o borrar los datos del sitio lo borra. La app le pide a Android que no lo borre por falta de espacio.

## Herramientas

Requieren Python 3 con `pip install fonttools brotli playwright` y, para los íconos, `python3 -m playwright install chromium`.

- `herramientas/version.py`: sube el número de versión y pone la fecha de hoy.
- `herramientas/fuentes.py`: baja las tipografías originales de Google Fonts y las recorta a los caracteres de `index.html`, más hiragana y katakana completos.
- `herramientas/iconos.py`: dibuja el ícono a partir del paraguas del logo que está en `index.html`.
- `herramientas/vista_previa.py`: arma la vista previa para el artefacto de claude.ai (el mismo `index.html`, con las tipografías adentro del archivo y sin manifiesto).
