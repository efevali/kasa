# Bocetos

Bocetos aprobados de Kasa. Cada uno es la app real con los cambios propuestos, capturada con `herramientas/boceto.py` a 1080 px de ancho; su código está en la rama de la versión, en un commit «B-xx: …». Las reglas están en [CONTRIBUTING.md](../../CONTRIBUTING.md#bocetos).

| Boceto | Pantalla | Imágenes | Issues | Aprobado | Estado |
|---|---|---|---|---|---|
| B-01 | Principal | [a · primera vez](B-01a-principal-inicio.png), [b · con avance](B-01b-principal-avance.png), [c · repetir lección](B-01c-principal-repetir.png) | #1, #2, #3, #4 | 2/10/2026 | Vigente (0.4.0) |
| B-02 | Mis palabras | [a · primera vez, vacía](B-02a-mis-palabras-primera-vez.png), [b · con palabras](B-02b-mis-palabras.png), [c · cuaderno tapado](B-02c-mis-palabras-tapado.png) | #20, #21, #22, #23, #24 | 2/10/2026 | Superado por B-03 (mostraba palabras propias) |
| B-03 | Mis palabras | [a · primera vez, vacía](B-03a-mis-palabras-primera-vez.png), [b · con Palabras 1](B-03b-mis-palabras.png), [c · cuaderno tapado](B-03c-mis-palabras-tapado.png) | #20, #21, #22, #23, #24, #25 | 2/10/2026 | Vigente (0.4.0) |
| B-04 | Tabla de kana y ficha de kana | [a · tabla con avance](B-04a-tabla-de-kana.png), [b · ficha de か](B-04b-ficha.png), [c · ficha de が, modelo apagado](B-04c-ficha-dakuten-sin-modelo.png) | #5, #26, #27 | 2/10/2026 | Vigente (0.4.0) |
| B-05 | Repaso de kana | [a · sin kana aprobados](B-05a-repaso-sin-kana.png), [b · con kana, sin repasos](B-05b-repaso-sin-repasos.png), [c · con un repaso hecho](B-05c-repaso-con-repaso.png) | #28 | 2/10/2026 | Vigente (0.4.0) |
| B-06 | Ajustes, Borrar y Créditos | [a · Ajustes](B-06a-ajustes.png), [b · borrar el progreso](B-06b-borrar.png), [c · créditos](B-06c-creditos.png) | #30, #33, #34, #35 | 6/10/2026 | Vigente (0.4.1) |
| B-07 | Lección de kana en ciclo | [a · presentar un kana](B-07a-presentar-kana.png), [b · presentar la fila con marca](B-07b-fila-con-marca.png), [c · leer una palabra](B-07c-leer.png), [d · la palabra, abierta](B-07d-leer-abierta.png) | #7 | 9/11/2026 | Vigente (0.5.0); c y d, reemplazados por B-10a |
| B-08 | Pantalla de la unidad | [el resultado en su renglón y una sola lección trabada con el aviso](B-08-pantalla-de-la-unidad.png) | #52, #53 | 9/11/2026 | Vigente (0.5.0) |
| B-09 | Tabla del hiragana en la lección 1 | [las vocales arriba, la consonante de cada fila a la izquierda y las filas de la unidad resaltadas](B-09-tabla-del-hiragana.png) | #54 | 10/11/2026 | Vigente (0.5.0) |
| B-10 | Ejemplos e hitos, sin esperar la lectura en voz alta | [a · los tres ejemplos en una pantalla](B-10a-ejemplos.png), [b · la frase del hito, de una vez](B-10b-hito.png) | #7 | 10/11/2026 | Vigente (0.5.0) |

Desde B-02, las pantallas que se desplazan se capturan enteras, de arriba abajo (`--entera`), como la captura desplazada del teléfono. El progreso de ejemplo que no se puede escribir en la línea de comandos (palabras propias, estadísticas) va en un archivo junto a las imágenes, como [B-03.json](B-03.json) o [B-05.json](B-05.json).

Desde B-04, si una acción toca un botón, la captura le quita el foco antes de sacarla: en el teléfono, al tocar, no aparece el anillo de foco, que en la captura achicaba a la vista el espacio alrededor del botón.

Desde B-07, las pantallas del medio de una práctica (a las que no se llega con una dirección) se capturan desde una copia temporal de la carpeta, con una línea agregada a `index.html` después de `const app = …`: `window.__ev = c => eval(c);`. Con ella, una `--accion` puede saltar al paso que se quiere mostrar (`__ev("Q.i = Q.items.findIndex(q => q.type === 'presentrow'); app.innerHTML = renderQuizScreen(); onShow(Q.items[Q.i]);")`). Esa línea no entra en la app. En las capturas también se quita el aviso «No se pudo reproducir el audio», que aparece porque el navegador sin interfaz no tiene voz japonesa.
