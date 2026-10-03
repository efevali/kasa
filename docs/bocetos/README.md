# Bocetos

Bocetos aprobados de Kasa. Cada uno es la app real con los cambios propuestos, capturada con `herramientas/boceto.py` a 1080 px de ancho; su código está en la rama de la versión, en un commit «B-xx: …». Las reglas están en [CONTRIBUTING.md](../../CONTRIBUTING.md#bocetos).

| Boceto | Pantalla | Imágenes | Issues | Aprobado | Estado |
|---|---|---|---|---|---|
| B-01 | Principal | [a · primera vez](B-01a-principal-inicio.png), [b · con avance](B-01b-principal-avance.png), [c · repetir lección](B-01c-principal-repetir.png) | #1, #2, #3, #4 | 2/10/2026 | Vigente (0.4.0) |
| B-02 | Mis palabras | [a · primera vez, vacía](B-02a-mis-palabras-primera-vez.png), [b · con palabras](B-02b-mis-palabras.png), [c · cuaderno tapado](B-02c-mis-palabras-tapado.png) | #20, #21, #22, #23, #24 | 2/10/2026 | Superado por B-03 (mostraba palabras propias) |
| B-03 | Mis palabras | [a · primera vez, vacía](B-03a-mis-palabras-primera-vez.png), [b · con Palabras 1](B-03b-mis-palabras.png), [c · cuaderno tapado](B-03c-mis-palabras-tapado.png) | #20, #21, #22, #23, #24, #25 | 2/10/2026 | Vigente (0.4.0) |
| B-04 | Tabla de kana y ficha de kana | [a · tabla con avance](B-04a-tabla-de-kana.png), [b · ficha de か](B-04b-ficha.png), [c · ficha de が, modelo apagado](B-04c-ficha-dakuten-sin-modelo.png) | #5, #26, #27 | 2/10/2026 | Vigente (0.4.0) |
| B-05 | Repaso de kana | [a · sin kana aprobados](B-05a-repaso-sin-kana.png), [b · con kana, sin repasos](B-05b-repaso-sin-repasos.png), [c · con un repaso hecho](B-05c-repaso-con-repaso.png) | #28 | 2/10/2026 | Vigente (0.4.0) |

Desde B-02, las pantallas que se desplazan se capturan enteras, de arriba abajo (`--entera`), como la captura desplazada del teléfono. El progreso de ejemplo que no se puede escribir en la línea de comandos (palabras propias, estadísticas) va en un archivo junto a las imágenes, como [B-03.json](B-03.json) o [B-05.json](B-05.json).

Desde B-04, si una acción toca un botón, la captura le quita el foco antes de sacarla: en el teléfono, al tocar, no aparece el anillo de foco, que en la captura achicaba a la vista el espacio alrededor del botón.
