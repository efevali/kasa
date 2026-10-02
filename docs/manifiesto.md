# Manifiesto y ruta del curso

Qué es Kasa, qué principios gobiernan cada lección y por qué camino avanza el curso. Ante una duda de diseño, se resuelve contra este documento. Las decisiones puntuales, con su fecha y su motivo, están en el [registro de decisiones](decisiones.md); las reglas de interfaz, dibujos y sonidos, en la guía de estilo, al principio del CSS de `index.html`.

## Qué es Kasa

Un curso de japonés desde cero, hecho como app para el teléfono. En principio es de uso personal y apunta a ser **la única herramienta digital de aprendizaje**: coherente, con una estructura lógica y un camino decidido. Duolingo queda como punto de comparación.

Dos prioridades, en este orden:

1. **Primero kana, después palabras.** Es innegociable y cubre también lo que se escucha: no hay frases de oído antes de sus kana.
2. **Que sea ameno.** Que atraiga y genere constancia sin romper la primera prioridad: el curso no puede expulsar a quien lo usa.

La meta de desarrollo es la **versión 1.0.0**: estable y revisada, sin pendientes ni dudas.

## Los diez principios

Aprobados el 24/9/2026. Valen para todas las lecciones.

1. **Primero kana, después palabras.** Nada se muestra ni se escucha antes de que se hayan enseñado sus kana, y nada se evalúa sobre lo no enseñado. Hay dos excepciones declaradas, las dos de mapa: las lecciones de mapa del inicio, con romaji en todo, que presentan el idioma sin pedir leerlo, y la navegación (la tabla de kana, el temario y los títulos de las lecciones), que muestra kana sin pedir leerlos ni evaluarlos.
2. **Útil, interesante y abarcable.** La velocidad no es criterio. Cada lección tiene que sentirse útil, despertar interés y poder terminarse sin agobio.
3. **Cada kana es una llave.** Toda lección de kana termina leyendo algo real. Cuando se completan los kana de una frase, la frase se destraba como hito.
4. **Orden por utilidad, mapa tradicional.** Las filas pueden adelantarse si destraban mucho, como ん (n). La tabla completa se muestra siempre en su orden clásico.
5. **Lo aprendido vuelve.** Palabras, kana y frases reaparecen en lecciones posteriores y en los repasos.
6. **Preguntas honestas.** Ninguna pregunta se resuelve por descarte, por el romaji o porque hay una sola opción conocida.
7. **El romaji es andamio.** Ayuda al principio y se retira.
8. **Una lógica por tipo de pantalla.** Las mismas reglas valen para todas las lecciones del mismo tipo.
9. **Anunciar sin adelantar.** Cuando algo tiene una forma más avanzada o se retoma más adelante, se avisa cuándo llega, sin mostrarlo antes de tiempo. El aviso habla de lo que la persona va a vivir («en la unidad 2»), no de títulos de lecciones que todavía no conoce, y va solo donde aporta.
10. **Los textos hablan del japonés y de lo que va a hacer quien estudia.** Nunca explican cómo está armado el curso, ni justifican sus decisiones, ni responden a alternativas que el usuario no conoce. Prueba: si una frase responde a una pregunta que solo haría quien conoce el diseño, sobra.

## Ruta del curso

La lista vigente de unidades y lecciones vive en el código (`UNITS`, en `index.html`). Este resumen explica su lógica; si alguna vez no coinciden, manda el código y se corrige este documento.

### Tramo de hiragana: unidades 1 a 3 (31 lecciones)

El hiragana se completa en la lección 26. El único cambio respecto del orden tradicional de filas es adelantar ん (n) a la lección de な (na). Cada unidad alterna lecciones de kana con lecciones de palabras escritas solo con los kana ya enseñados, y cierra con un repaso.

| Unidad | Kana | Lecciones | Frases que se destraban (hitos) |
|---|---|---|---|
| 1 · Primeros pasos | あ〜そ | Cómo funciona el japonés I (mapa) · Las cinco vocales · Cómo funciona el japonés II (mapa) · か y が · Palabras 1 y 2 · さ y ざ · Palabras 3 y 4 · Repaso | — |
| 2 · Decir qué es cada cosa | た〜ほ, ん | た y だ · Palabras 5 y 6 · な y ん · Palabras 7 · は, ば y ぱ · Palabras 8 · X は Y です · Escucha · Repaso | Con は: こんにちは, こんばんは |
| 3 · Cosas y personas | ま〜を | ま · Palabras 9 · や, わ y を · Palabras 10 y 11 · ら · Palabras 12 · Frases de todos los días · の, これ, それ, あれ y la negación · Diálogo · Repaso | Con ま: すみません, はじめまして, いただきます. Con や, わ y を: おはよう ございます, おやすみなさい. Con ら: さようなら, ありがとう ございます, よろしく おねがいします |

- Las vocales van entre las dos lecciones de mapa, para alternar teoría y práctica en la primera sesión.
- Cada lección de palabras presenta seis palabras.
- Las frases no tienen lección propia: se destraban como hitos al aprobar por primera vez la lección de kana que las completa, y se consolidan juntas en «Frases de todos los días».
- La negación se enseña primero como では ありません (dewa arimasen); la forma coloquial se anuncia sin mostrarla hasta que lleguen los kana combinados (unidad 4).

### Unidades en preparación

| Unidad | Contenido previsto |
|---|---|
| 4 · Sonidos combinados | Combinaciones con ゃ, ゅ y ょ, consonantes dobles con っ y vocales largas. Números del 1 al 100 y la edad. |
| 5 · Katakana I | La mitad del katakana y las palabras prestadas. Adjetivos: たかい, きれい y cómo usarlos. |
| 6 · Katakana II | El resto del katakana y los sonidos extranjeros. Comida y gustos: すき y きらい. |
| 7 · Primeros verbos | La forma ます: presente, negativo y pasado. Partículas を, に y で. |
| 8 · El tiempo | La hora, los días de la semana y la rutina diaria. |
| 9 · Dónde está cada cosa | あります e います, ubicaciones (うえ, した, なか) y ここ, そこ, あそこ. |
| 10 · Primeros kanji | Números, 日, 月, 人, 山 y otros kanji básicos: lectura y uso. |

Cada unidad nueva se diseña contra los diez principios antes de armarse: primero el plan (lecciones, palabras, frases, dibujos), después los bocetos, después el código.
