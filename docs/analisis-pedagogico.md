# Análisis pedagógico: la dinámica del tramo de hiragana

Cómo aprende quien recorre las unidades 1 a 3 (31 lecciones), tal como están en la 0.4.1: cuánto practica cada cosa nueva, cuándo vuelve a encontrarla y si la usa en contextos nuevos. Queda para después el análisis de la estructura del curso completo y su comparación con cursos de referencia.

**Estado: para discutir** (12/10/2026). Nada de esto está acordado. Lo que se acuerde se carga como issue y, si cambia una regla, pasa al [manifiesto](manifiesto.md) o al [registro de decisiones](decisiones.md). Este documento queda como el diagnóstico que les dio origen.

## Cómo se hizo

- Se leyeron el temario (`UNITS`), el generador de preguntas y las herramientas de práctica (Mis palabras y Repaso de kana) de `index.html`.
- Cada práctica del tramo se generó 400 veces con el código de la app, porque las preguntas salen al azar, para contar pantallas, respuestas, tipos de pregunta y cuántas veces aparece cada kana y cada palabra. Las cifras son promedios de esas corridas.
- Se buscó en qué palabras, frases y oraciones del tramo aparece cada kana, y en qué oraciones aparece cada palabra.
- Se evaluó contra lo que la investigación sobre aprendizaje respalda con más solidez (ver [Referencias](#referencias)): recuperar de memoria fija más que releer; lo que vuelve espaciado en días se retiene mucho más que lo practicado de una sola vez; lo aprendido se consolida al usarse en contextos nuevos; y lo nuevo por sesión tiene un límite.

## Resumen

- **Lo mejor del tramo es la lección de palabras.** Presenta de a dos, pregunta enseguida, mezcla con lo anterior, pide armar y repite lo fallado. Cada palabra se recupera cuatro veces.
- **Las lecciones de kana quedaron atrás.** No presentan: van directo a las preguntas. Cada kana base se recupera dos veces y cada kana con marca, una. En «は, ば y ぱ», cada kana con ゛ o ゜ sale 0,6 veces en promedio, y en cada práctica hay cuatro que no salen.
- **Hay kana que no se vuelven a leer.** 18 de los 69 kana no aparecen en ninguna palabra del tramo. La fila de ぱ entera y び, ぶ, べ y ぼ no aparecen en nada que se lea.
- **Nada vuelve por tiempo.** El curso siempre lleva hacia adelante. Los repasos de unidad no traen palabras de unidades anteriores, y Mis palabras y Repaso de kana eligen por errores, no por el tiempo que pasó. Después de su repaso, las palabras de la unidad 1 no vuelven a preguntarse en ninguna lección; solo いいえ y えいご reaparecen, dentro de oraciones.
- **Las palabras casi no se usan en oraciones.** 24 de las 72 aparecen en alguna oración; de la unidad 1, solo dos. La primera oración llega en la lección 18, aunque los kana de です están desde la 11.
- **Propuesta principal:** llevar el ciclo de la lección de palabras a las lecciones de kana, ya en la 0.5.0, y sumar un repaso que vuelva por tiempo, con kana y palabras de todo lo aprobado.

## El tramo en números

| | Lecciones de kana | Lecciones de palabras |
|---|---|---|
| Cantidad | 9 | 12 |
| Lo nuevo | 69 kana (46 formas) | 72 palabras |
| Respuestas por lección | 10 a 16 | 24 |
| Veces que se recupera cada elemento nuevo en su lección | 2 por kana base, 1 por kana con marca, 0,6 en ば y ぱ | 4, después de presentarla |

Las otras diez lecciones son dos de mapa, dos de gramática, la escucha, las frases, el diálogo y los tres repasos.

Recorrido una vez, aprobando todo a la primera, el tramo suma unas 530 respuestas puntuadas y unos 290 minutos (la suma de los `min` del temario). Algo más de la mitad de esas respuestas muestran japonés y piden el significado o la lectura; una cuarta parte pide elegir o armar el japonés a partir del español, el romaji o un dibujo; y una quinta parte arranca de un audio. Armar oraciones en japonés aparece cinco veces en todo el tramo: tres en «X は Y です» y dos en «の, これ, それ, あれ y la negación».

## Lo que funciona

Conviene conservarlo tal cual y usarlo de modelo.

1. **El ciclo de palabras.** Tandas de dos que se presentan con sonido, dibujo o dato y se preguntan enseguida; las anteriores vuelven mezcladas; el cierre combina dibujo, armar la palabra (una vez por audio), emparejar y opción múltiple hasta que cada palabra aparece al menos tres veces. Es exactamente la secuencia que la investigación recomienda: presentar, recuperar enseguida, intercalar y variar la dirección.
2. **Preguntas honestas.** Los distractores de kana salen de la misma fila o de los que se confunden a la vista, con una sola lectura por opción; en emparejar sobra un significado; las opciones de las tandas salen solo de lo visto. El acierto mide lo que se sabe, no lo que se deduce.
3. **Corrección que enseña.** Muestra la respuesta, el significado y, si la palabra lo tiene, el dibujo o la asociación. Lo fallado vuelve al final sin sumar: una segunda recuperación justo después del error, que es cuando más rinde.
4. **Alternancia de kana y palabras.** Lo que se aprende en una lección se usa en la siguiente. El kana tiene uso inmediato, y eso le da sentido.
5. **Hitos.** La recompensa es poder leer algo real, no puntos. Une la motivación con una capacidad verdadera.
6. **Aprobar con el 80 % y guardar la mejor nota.** Exige sin castigar.

## Hallazgos

### 1. Las lecciones de kana practican poco y no presentan

- Antes de la práctica, la lección muestra la grilla con cada kana y su romaji. Tocar un kana abre su ficha (audio, trazo, pronunciación y un ejemplo), pero es opcional. La práctica empieza directamente con preguntas: el primer contacto con un kana puede ser «¿Cómo se lee?».
- Cada kana base sale dos veces y cada kana con marca, una. En «は, ば y ぱ» la práctica tiene 16 preguntas para 15 sonidos: entran solo seis de los diez kana con ゛ o ゜, así que cada uno sale 0,6 veces en promedio y, en cada práctica, cuatro no salen nunca.
- La lección de palabras, en cambio, presenta cada palabra y la recupera cuatro veces. El elemento más básico del curso es el que menos se practica.
- El principio 3 dice que toda lección de kana termina leyendo algo real. Hoy la práctica termina con kana sueltos; la lectura llega en la lección siguiente, salvo en las cuatro lecciones que destraban frases. El material ya existe: cada kana base tiene en su ficha una palabra de ejemplo que se puede leer en ese punto del curso.
- El trazo, que según la decisión del 2/10 es lo que fija la forma, es opcional y queda detrás de un toque.

Por qué importa: con dos recuperaciones por kana, el 80 % se puede alcanzar sin haberlos fijado. Y el kana es la base de todo lo que sigue (principio 1): una confusión entre ぬ y め, o entre る y ろ, se arrastra a cada palabra.

### 2. Hay kana que no se vuelven a leer

- **En ninguna palabra del tramo (18):** げ, ざ, じ, ぞ, ど, の, へ, を, ろ, び, ぶ, べ, ぼ, ぱ, ぴ, ぷ, ぺ y ぽ.
- De esos, algunos aparecen en frases (ざ en ございます, じ en はじめまして, ろ en よろしく) o en la gramática (の, y ど en どれ). **En nada que se lea, fuera de su lección y los repasos (13):** げ, ぞ, へ, び, ぶ, べ, ぼ, ぱ, ぴ, ぷ, ぺ, ぽ y を (を solo aparece en la lección de mapa, con romaji).
- **En una sola palabra (15):** ぎ (かぎ), ぐ (でぐち), ず (みず), ぜ (かぜ), て (て), ぬ (いぬ), は (はな), ひ (ひと), ば (かばん), む (さむい), も (ともだち), や (やま), ゆ (ゆき), よ (よる) y ら (さくら).
- Los kana base tienen además una palabra de ejemplo en su ficha, pero abrir la ficha es opcional.

Por qué importa: leer palabras es el repaso natural de los kana. Un kana que no se vuelve a leer depende del Repaso de kana, que es voluntario. Hay palabras que cubrirían todos esos kana sin romper el principio 1 (ver P2).

### 3. Nada vuelve por tiempo

- El botón de la principal lleva siempre a la lección siguiente. Mis palabras y Repaso de kana no avisan cuándo conviene usarlos.
- Repaso de kana elige los kana según sus errores y apariciones, sin registrar cuándo se practicaron. Mis palabras hace lo mismo con las palabras y su racha de aciertos.
- Una palabra pasa a «Firme» con tres aciertos seguidos, que se pueden juntar en tres rondas el mismo minuto; desde ahí casi deja de salir. «Firme» mide lo practicado en una sesión, no lo que se recuerda días después.
- Cada repaso de unidad toma solo palabras de su unidad (dos por lección, así que cada palabra tiene una chance en tres de salir) y apenas dos kana de unidades anteriores. Después del repaso de la unidad 1, sus palabras solo vuelven como opciones incorrectas en otras preguntas, o en Mis palabras (salvo いいえ y えいご, que reaparecen en oraciones).
- Las estadísticas de palabras salen solo de Mis palabras: lo que se acierta o se falla en las lecciones y los repasos no cuenta.

Por qué importa: el efecto del espaciado es uno de los hallazgos más sólidos de la investigación sobre memoria. Kasa aspira a ser la única herramienta de aprendizaje, así que la retención tiene que resolverse adentro. Con diez unidades, sin un repaso espaciado, la unidad 1 quedaría nueve unidades atrás.

### 4. Las palabras casi no se usan en oraciones

- 24 de las 72 palabras aparecen en alguna oración del tramo (gramática, escucha o diálogo). De la unidad 1, solo いいえ y えいご.
- Las preguntas de gramática y del diálogo son listas fijas: repetir la práctica trae las mismas preguntas (10 en cada gramática, 8 en el diálogo). La escucha toma 9 de sus 12 oraciones, más 3 fijas.
- La primera oración llega en la lección 18 («X は Y です»). Los kana de «Y です» y «Y ですか» están completos desde la lección 11 (で llega con た y だ; す y か, en la unidad 1), y いいえ está desde Palabras 1.

Por qué importa: usar una palabra en una oración la recupera con su función, no solo con su significado. Además, la unidad 2 se llama «Decir qué es cada cosa», y eso se hace con oraciones.

### 5. Detalles

- La primera tanda de Palabras 1 tiene dos preguntas con dos opciones, porque solo hay dos palabras vistas. Roza el principio 6 («una sola opción conocida»).
- En las lecciones de kana, el texto dice «Tocá cada kana para escucharlo, ver cómo recordarlo y practicar el trazo con el dedo». Quedó de antes de #26, que quitó «Para recordarlo» de la ficha.
- En la unidad 3, un tercio de las preguntas de kana sigue usando el romaji como consigna («¿Cuál es este sonido?» con «ra»), y lo mismo el Repaso de kana. Es la única excepción al retiro del romaji del principio 7.
- «Pensalo primero» (recordar antes de ver las opciones) es la práctica que más fija y está apagado de fábrica.

## Propuestas

Ordenadas por impacto. Cada una dice cuándo convendría hacerla.

### P1. Un ciclo para las lecciones de kana (0.5.0)

La lógica de la lección de palabras, aplicada a los kana:

- Tandas de dos o tres kana que se presentan (kana, sonido y trazo) y se preguntan enseguida; desde la segunda tanda vuelven los anteriores.
- Los kana con marca, en una tanda propia después de su fila, presentados como lo que son: el mismo kana con una marca.
- Una dosis mínima: tres recuperaciones por kana base y dos por kana con marca. Las lecciones de kana pasarían de 10 a 16 respuestas a entre 15 y 25, como las de palabras. «は, ば y ぱ» llegaría a unas 35: conviene partirla en dos (は; ば y ぱ).
- Un cierre leyendo dos o tres palabras reales hechas con los kana nuevos, con audio para comprobar. Así se cumple el principio 3 dentro de la lección.

Pide un tipo de pantalla nuevo («presentar kana»), con boceto. La unidad 1 tiene tres lecciones de kana (vocales, か y さ), así que entra naturalmente en la 0.5.0.

### P2. Que cada kana se lea en palabras (0.5.0 para la unidad 1; el resto, en su tanda)

Criterio: todo kana enseñado aparece en al menos una palabra del tramo, idealmente en dos. を es la excepción declarada: espera a los verbos.

Hay palabras que lo resuelven sin romper el principio 1. Son ejemplos para mostrar que se puede; cada una se revisa como contenido antes de elegirla.

- Unidad 1: かぞく (familia, para ぞ), かげ (sombra, para げ), かじ (incendio, para じ), すず (cascabel, para ず) y かぐ (muebles, para ぐ).
- Unidad 2, después de «は, ば y ぱ»: げんき, かんぱい, えんぴつ, さんぽ, しんぶん, たんぽぽ, かべ, なべ, えび, へび, ぶた, ぼく y どこ.
- Unidad 3: いろ, ふろ, へや, てんぷら y ぺらぺら.

Respeta «Seis palabras por lección»: se reemplazan palabras, no se suman. Cada cambio arrastra su dibujo o su dato.

### P3. Un repaso que vuelva por tiempo (versión propia)

- Cada kana y cada palabra aprobados guardan cuándo se practicaron y cuándo deben volver. El intervalo crece al acertar (1, 3, 7, 14, 30 días…) y vuelve a empezar al fallar. Cuentan todas las respuestas: lecciones, repasos, Mis palabras y Repaso de kana.
- «Firme» pasa a significar «acertada después de una semana o más».
- Cómo aparece es una decisión de producto:
  - **a.** Un botón «Repaso de hoy» en la principal cuando hay algo pendiente. Es simple, pero depende de que se elija.
  - **b.** Un calentamiento de cuatro a seis preguntas pendientes al empezar cada lección. No suma pantallas ni decisiones: se repasa siempre que se avanza.
  - **c.** Las dos.
- Recomendación: **b**. Integra el repaso en el camino que ya existe, y lo pendiente del día también es un motivo para volver, que es la constancia que busca la prioridad 2.

Cambia el progreso guardado (cada elemento suma fecha e intervalo), y Mis palabras y Repaso de kana pasan a usarlo. Es el cambio más grande del documento y cruza toda la app: conviene una versión propia, separada de las unidades. El progreso actual se conserva; lo ya aprobado arranca como pendiente.

### P4. Repasos de unidad acumulativos (con P3, o antes)

De las veinte preguntas, unas seis de unidades anteriores, kana y palabras, elegidas entre lo pendiente o lo más fallado. Cambia el armado del repaso, no sus pantallas. Se puede hacer antes de P3, eligiendo por errores.

### P5. Oraciones antes, y generadas (tanda de la unidad 2)

- Adelantar «Y です», «Y ですか» y «はい / いいえ» a Palabras 5 y 6, donde los kana ya alcanzan. «X は Y です» sigue en su lección, ahora enfocada en は.
- Preguntas de oraciones armadas con plantillas y el vocabulario aprendido (かさですか。いいえ、いすです。), en lugar de listas fijas. Cada repetición trae oraciones distintas, y las palabras de la unidad 1 vuelven en oraciones.
- Las plantillas tienen que ser conservadoras, con combinaciones verificadas: una oración antinatural es japonés incorrecto, el error que el método trata como urgente.

Cambia la ruta (y el manifiesto) y suma un generador de oraciones. Va con la unidad 2.

### P6. Detalles (en la tanda de cada pantalla)

- Primera tanda de Palabras 1: tres palabras en lugar de dos, para que haya tres opciones; o declarar esa tanda como excepción del principio 6.
- Corregir el texto de las lecciones de kana («ver cómo recordarlo»), en la 0.5.0.
- Desde la unidad 3, reemplazar «¿Cuál es este sonido?» (del romaji al kana) por «Escuchá y elegí el kana», en las lecciones y en Repaso de kana.
- Evaluar «Pensalo primero» encendido de fábrica.

### P7. Medir cada unidad con una herramienta

Un ayudante en `herramientas/`, como `boceto.py`, que abra la app real, genere cada práctica muchas veces y verifique los criterios de abajo. Así cada unidad nueva se mide igual, la mida quien la mida.

## Criterios propuestos para cada unidad nueva

Si se aprueban, se suman al manifiesto junto a los diez principios, y P7 los verifica.

1. **Presentar antes de preguntar.** Todo elemento nuevo se muestra (forma, sonido y significado) antes de su primera pregunta.
2. **Dosis.** En su lección, cada elemento nuevo se recupera al menos tres veces (dos, los kana con marca), y al menos una de esas veces parte del significado, el sonido o un dibujo.
3. **Cobertura.** Todo kana enseñado se lee en al menos una palabra del tramo.
4. **Uso.** En cuanto los kana lo permiten, las palabras se usan en oraciones, y las oraciones de práctica se generan con el vocabulario aprendido.
5. **Espaciado.** Todo lo aprobado vuelve por tiempo, no solo por el orden del camino.
6. **Repasos acumulativos.** El repaso de una unidad incluye material de las anteriores.
7. **Variedad.** Cada unidad practica lectura, escucha y armado; ninguna habilidad queda solo en reconocer.
8. **Carga.** Hasta seis palabras nuevas por lección, y hasta seis formas de kana nuevas (sin contar las marcas).

## Decisiones previas que este análisis toca

- **Sin «Para recordarlo» en los kana** (2/10): las asociaciones se quitaron porque eran solo texto y algunas, flojas. La evidencia sobre mnemotecnias con imagen es favorable, sobre todo en el primer contacto con un sistema de escritura nuevo. Si alguna vez se retoma, sería con dibujo. No se propone reabrirlo ahora.
- **Primero kana, también en lo que se escucha** (24/9): ninguna propuesta la toca. Todo lo que se escucha sigue teniendo sus kana enseñados.
- **Seis palabras por lección** (24/9): P2 la respeta.

## Referencias

- Roediger y Karpicke (2006), «Test-enhanced learning», *Psychological Science*: recuperar de memoria fija más que volver a estudiar.
- Cepeda y otros (2006), «Distributed practice in verbal recall tasks», *Psychological Bulletin*: espaciar la práctica en días mejora la retención a largo plazo.
- Nation (2013), *Learning Vocabulary in Another Language*, 2.ª ed., Cambridge: una palabra se fija con encuentros repetidos y con su uso en contextos variados.
- Longcamp y otros (2005), *Acta Psychologica*: en chicos que aprendían letras, escribirlas a mano mejoró su reconocimiento más que tipearlas.
