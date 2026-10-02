# Kasa

Curso de japonés desde cero —primero los kana, después las palabras— hecho como app instalable (PWA) para Android.

- **App:** https://efevali.github.io/kasa/ (se abre en Chrome y se instala con el botón «Instalar» de la principal, o desde el menú ⋮ → «Instalar app»)
- **Vista previa:** el artefacto «Kasa» en claude.ai, donde se prueba cada cambio antes de publicarlo aquí.
- **Cómo se trabaja:** issues, milestones, bocetos y pull requests, en [CONTRIBUTING.md](CONTRIBUTING.md). Lo publicado, en [CHANGELOG.md](CHANGELOG.md).

## Dónde vive

El repositorio está en la cuenta personal **efevali**, donde Kasa es uno de sus proyectos. Hasta el 1/10/2026 la cuenta se llamaba **kasalearn** y la app estaba en `kasalearn.github.io/kasa`: GitHub redirige los enlaces viejos al repositorio, pero no los de GitHub Pages, así que esa dirección ya no existe. Una app instalada desde ella sigue abriendo sin conexión, con la 0.2.1 y su progreso, pero ya no recibe versiones nuevas; el progreso no pasa a la dirección nueva, porque el teléfono lo guarda por dirección.

**kasalearn** quedó como organización de GitHub de la cuenta efevali, sin publicar nada, para que nadie más pueda tomar ese nombre: quien lo tuviera podría publicar en la dirección vieja, y las apps instaladas desde allá lo tomarían como una versión nueva. Por eso se conserva.

La única dirección escrita en los archivos es la del manifiesto (`related_applications`, con la que la tarjeta de instalación reconoce que Kasa ya está instalada). Si la cuenta vuelve a cambiar de nombre, se cambia ahí, en este README y en la guía de estilo de `index.html`.

## Qué hay en cada archivo

| Archivo o carpeta | Qué es |
|---|---|
| `index.html` | La app entera: textos, lecciones, dibujos, sonidos y código. Al principio del CSS está la **guía de estilo**, con todas las reglas acordadas. |
| `manifest.webmanifest` | La ficha que Android lee para instalarla: nombre, ícono, colores, que abra sin barra del navegador y en vertical. |
| `sw.js` | El *service worker*: guarda la app en el teléfono para que funcione sin conexión y maneja las versiones nuevas. |
| `fuentes/` | Klee One, Shippori Mincho y Zen Kaku Gothic New, recortadas a lo que usa el curso, con sus licencias (SIL OFL 1.1). |
| `iconos/` | El ícono (el wagasa del logo, solo, sobre crudo) en los tamaños que pide Android. |
| `herramientas/` | Ayudantes para el armado: `version.py`, `fuentes.py`, `iconos.py`, `vista_previa.py` y `boceto.py` (ver abajo). |
| `docs/` | El manifiesto del curso, el registro de decisiones, los bocetos aprobados y el muestrario de sonidos (ver su [índice](docs/README.md)). |
| `CONTRIBUTING.md` | El método de trabajo: issues, etiquetas, bocetos, ramas y commits. |
| `CHANGELOG.md` | El registro de las versiones publicadas. |
| `.github/` | Las plantillas de issue y de pull request. |
| `.nojekyll` | Le indica a GitHub Pages que publique los archivos tal cual, sin procesarlos. |

## Cómo se publica una versión nueva

1. Los cambios se hacen en `index.html` y se prueban en la vista previa (el artefacto «Kasa», abierto en Chrome), armada con `python3 herramientas/vista_previa.py`.
2. Si el curso sumó caracteres nuevos (por ejemplo, kanji), se regeneran las tipografías:
   `python3 herramientas/fuentes.py`
3. Se sube el número de versión (ver «Versiones»), en `index.html` y en `sw.js` a la vez:
   `python3 herramientas/version.py parche|menor|mayor`
4. Se suma la versión a `CHANGELOG.md`.
5. Se une el pull request de la versión a `main` en un solo commit cuyo título empieza con el número de versión («0.4.0: …»); un parche urgente puede ir directo. GitHub Pages la publica en un minuto o dos.

En el teléfono, la app encuentra la versión nueva al abrirse, al volver a ella después de un rato o con «Buscar» en Ajustes. Aparece «Hay una versión nueva» en Ajustes y un punto verde en el engranaje; «Actualizar» la reabre ya actualizada. Si no se toca, entra sola al cerrar la app del todo y volver a abrirla.

## Versiones

Kasa usa **versionado semántico**: tres números, MAYOR.MENOR.PARCHE.

- **Parche** (0.2.0 → 0.2.1): arreglos que no suman nada nuevo.
- **Menor** (0.2.1 → 0.3.0): algo nuevo que no rompe lo anterior, como una función o una unidad del curso.
- **Mayor** (0.x → 1.0.0): mientras el primer número es 0, la app está en desarrollo. La **1.0.0** es la versión estable y revisada, sin pendientes ni dudas. Después de la 1.0, el mayor sube solo cuando algo rompe lo anterior (por ejemplo, si el progreso guardado dejara de ser compatible).

Cada versión publicada se encuentra en el historial del repositorio («Commits») por su número: el título de su commit empieza con él. El registro está en [CHANGELOG.md](CHANGELOG.md). El teléfono no compara números: toma lo último que se publica. Para volver a una versión anterior se publica su contenido con un número nuevo (por ejemplo, una 0.2.1 que deshace la 0.2.0); el historial conserva todo.

## Progreso

Se guarda en el teléfono, dentro de los datos de Chrome para este sitio. Desinstalar la app o borrar los datos del sitio lo borra. La app le pide a Android que no lo borre por falta de espacio.

## Herramientas

Requieren Python 3 con `pip install fonttools brotli playwright` y, para los íconos, `python3 -m playwright install chromium`.

- `herramientas/version.py`: sube la versión (`parche`, `menor` o `mayor`) y pone la fecha de hoy.
- `herramientas/fuentes.py`: baja las tipografías originales de Google Fonts y las recorta a los caracteres de `index.html`, más hiragana y katakana completos.
- `herramientas/iconos.py`: dibuja el ícono a partir del paraguas del logo que está en `index.html`.
- `herramientas/vista_previa.py`: arma la vista previa para el artefacto de claude.ai (el mismo `index.html`, con las tipografías adentro del archivo y sin manifiesto).
- `herramientas/boceto.py`: captura una pantalla tal como se ve en el teléfono, con el progreso que se le indique, para los bocetos (ver [CONTRIBUTING.md](CONTRIBUTING.md#bocetos)).
