# Cómo se trabaja en Kasa

Kasa se desarrolla con el flujo habitual de GitHub: **issues** para lo que hay que cambiar, **milestones** para agrupar cada versión, **pull requests** para el código y un **registro de cambios** para lo publicado. Este repositorio es la única fuente de verdad del proyecto: lo que no está acá no está acordado.

Este archivo explica el método. Qué es la app, qué hay en cada archivo y cómo se publica están en el [README](README.md).

## Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Lo que falta cambiar (errores, mejoras, contenido, ideas) | [Issues](https://github.com/efevali/kasa/issues) |
| Qué entra en cada versión | [Milestones](https://github.com/efevali/kasa/milestones): uno por versión |
| Lo que todavía no tiene versión asignada (el *backlog*) | Issues abiertos sin milestone |
| El código de la versión en preparación | El [pull request](https://github.com/efevali/kasa/pulls) en borrador de su rama |
| Bocetos aprobados | [`docs/bocetos/`](docs/bocetos/) |
| Qué salió en cada versión | [`CHANGELOG.md`](CHANGELOG.md) |
| Reglas de interfaz, dibujos, sonidos y transiciones | La **guía de estilo**, al principio del CSS de `index.html` |

Pendiente: el manifiesto del curso (principios, ruta de lecciones) y el registro de decisiones van a sumarse en `docs/`.

## El ciclo

1. **Revisión.** Se recorre la app en el teléfono, pantalla por pantalla y lección por lección. Cada observación (una captura con un comentario) se discute antes de registrarla.
2. **Issue.** Lo acordado se carga como issue con la plantilla «Observación». Se redacta para que alguien pueda implementarlo sin haber visto la conversación ni la captura.
3. **Boceto.** Si el cambio es visual, se aprueba sobre un boceto (ver «Bocetos») y su código entra en la rama de la versión.
4. **Tanda.** Los issues acordados se agrupan en el milestone de la versión en preparación. Hay una tanda por unidad del curso: la primera suma las pantallas generales (principal, apertura, temario, ajustes, herramientas).
5. **Implementación.** Al cerrar la revisión de la unidad se completa el pull request: lo que los bocetos no cubren se hace según el texto de cada issue. Se prueba en la vista previa y se compara con los bocetos.
6. **Publicación.** Con el ok, se sube la versión, se une el pull request a `main`, se borra la rama y se suma la versión a `CHANGELOG.md`. Los issues de la tanda se cierran solos.

**Excepción:** lo que impide avanzar en el curso o enseña japonés incorrecto no espera la tanda. Se arregla en una rama propia y se publica enseguida como parche (0.x.**y**); después, la rama de la tanda se actualiza sobre `main`.

## Issues

Cada issue lleva:

- **Título:** el cambio, en una línea.
- **Dónde:** unidad, lección y pantalla.
- **Qué se observó.**
- **Cambio acordado:** concreto, sin depender de la conversación.
- **Cómo se verifica:** qué mirar en la vista previa para darlo por bueno.
- **Boceto**, si tiene: la imagen, qué fija y qué es solo un ejemplo.

### Etiquetas

| Etiqueta | Cuándo |
|---|---|
| `tipo: error` | Algo no funciona como debe |
| `tipo: mejora` | Funciona, pero puede ser mejor |
| `tipo: contenido` | Textos, palabras, japonés |
| `tipo: idea` | Algo nuevo, todavía sin forma |
| `prioridad: alta` | Confunde o estorba el aprendizaje |
| `prioridad: media` | Conviene resolverlo en la tanda |
| `prioridad: baja` | Detalle |
| `por discutir` | Falta acordar el cambio |
| `boceto` | Tiene boceto aprobado |

### Estados

| Estado del issue | Significa |
|---|---|
| Abierto, con `por discutir` | Registrado, falta acordar |
| Abierto, sin `por discutir` | Acordado; si tiene milestone, va en esa versión |
| Cerrado como completado | Publicado: la versión es la de su milestone |
| Cerrado como *not planned* | Descartado. El motivo queda en un comentario, para no volver a discutirlo |

## Bocetos

Un boceto no se dibuja: es la app real con los cambios propuestos, capturada a 360 × 780 px con escala 3 (1080 px de ancho, como el teléfono de referencia) con `herramientas/boceto.py`. Lo que muestra es lo que va a quedar.

- Hay boceto cuando el cambio es visual: disposición, tamaños, elementos que aparecen o desaparecen. Si es solo texto o comportamiento, alcanza con el issue.
- Se numeran B-01, B-02… Un boceto puede tener varias imágenes (B-01a, B-01b…), una por estado de la pantalla. Van en `docs/bocetos/` y se listan en su [índice](docs/bocetos/README.md), con los issues que cubren.
- En el issue, cada boceto dice **qué fija** y **qué es solo ejemplo** (el progreso simulado, una cantidad, la lección elegida).
- Su código entra en la rama de la versión como un commit propio, «B-01: …». Cada boceto se hace sobre los anteriores de la misma tanda, para que los cambios se sumen en orden.
- Si el texto del issue y el boceto no coinciden, manda el texto. Si un cambio posterior toca una pantalla con boceto, se hace uno nuevo y el anterior se marca como superado en el índice.

## Ramas, commits y pull requests

- **`main`** es lo publicado: GitHub Pages publica lo que está ahí. Solo recibe cambios de documentación y versiones terminadas.
- **Una rama por versión**, `tanda/0.4.0`, con su pull request en borrador desde el primer boceto. Vive mientras dura la tanda y se borra al unirse a `main`.
- **Commits**, en español: «B-01: …» para el código de un boceto, «#12: …» para lo que implementa un issue y «0.4.0: …» para el que sube la versión.
- **Al unir**, el pull request se aplasta en un solo commit (*squash*) cuyo título empieza con el número de versión, como pide el [README](README.md#cómo-se-publica-una-versión-nueva). Su descripción lleva «Closes #n» por cada issue, para que se cierren solos.

## Vista previa y pruebas

- La vista previa de cada cambio es el artefacto «Kasa» en claude.ai, armado con `python3 herramientas/vista_previa.py` y abierto en Chrome.
- Sin claude.ai, sirve cualquier servidor local: `python3 -m http.server` en la carpeta del repositorio y abrir `http://localhost:8000` en Chrome con la vista de teléfono de las herramientas de desarrollo.
- **Llave de prueba:** cinco toques al paraguas de la principal destraban todas las lecciones, solo en ese dispositivo y con un aviso en rojo. Se desactiva en Ajustes.
- Cada lección que cambia se prueba completa antes de publicar.

## Idioma

La app, los issues, los commits y la documentación van en español rioplatense (con voseo, como en la app). El japonés sigue las reglas del curso: nada de kanji mientras el curso no los enseñe, y kana antes que palabras.
