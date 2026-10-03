# Registro de decisiones

Las decisiones de diseño y de producto de Kasa, agrupadas por tema, con su fecha, su motivo y lo que se descartó. Sirve para no volver a discutir lo resuelto y para entender por qué la app es como es.

- Las **reglas vigentes** de interfaz, dibujos, zonas, enriquecimientos, sonidos y transiciones están en la guía de estilo, al principio del CSS de `index.html`. Acá figura por qué se decidieron y qué se descartó, sin repetir cada regla.
- Los **principios** están en el [manifiesto](manifiesto.md).
- Una decisión nueva se suma en su tema con la fecha. Si reemplaza a otra, la anterior se tacha o se aclara «reemplazada el …», no se borra.

Las fechas son de 2026.

## Producto y método

- **Kasa como única herramienta digital de aprendizaje** (24/9). En principio, para uso personal. Duolingo queda como punto de comparación, no como complemento.
- **Meta: la 1.0.0** (25/9). Una versión estable y revisada, sin pendientes ni dudas. Mientras tanto, 0.x.
- **Primero se conversa, después se boceta, después se arma.** El plan se acuerda sin implementar; lo visual se aprueba sobre escenas o pantallas renderizadas; recién después se escribe el código. Se consulta ante cualquier duda.
- **Implementación integral** (24/9). Lo acordado se implementa completo: no se publica nada aislado ni se dejan cabos sueltos.
- **No se guardan cosas duplicadas** (28/9). Lo que ya está en la app no se conserva aparte; por eso se borró la copia «Prueba de transiciones».
- **Revisión completa por tandas** (2/10). Se recorre la app entera desde la principal. Cada observación se discute y se registra; se implementa y publica una tanda por unidad del curso (reemplazado el mismo 2/10: ver «Tandas más cortas»). Lo que impide avanzar o enseña japonés incorrecto va como parche inmediato.
- **Tandas más cortas** (2/10). Con once issues acumulados, se implementa antes: la 0.4.0 reúne las pantallas generales (principal, Mis palabras, Tabla y Repaso de kana, Ajustes y apertura) y se publica al terminar de revisarlas, sin esperar a la unidad 1. El temario va con la unidad 1, en la 0.5.0, porque es la puerta de sus lecciones. Motivo: probar en el teléfono pocos cambios por vez.
- **Bocetos con su código** (2/10). Si el cambio es visual, se aprueba sobre un boceto que es la app real con el cambio aplicado, y su código se guarda para implementarlo tal cual. Para cambios de texto no hace falta.
- **GitHub como única fuente de verdad** (2/10). Backlog, método, bocetos, manifiesto y decisiones viven en este repositorio, con la metodología habitual de la industria, para que un tercero pueda trabajar en el proyecto. Se aceptó que todo sea público (el código ya lo era). Reemplazó al documento «Kasa — Backlog» de claude.ai, que se usó solo ese día.
- **Licencia: pendiente.** Hoy el repositorio no tiene licencia (rigen los derechos de autor por defecto). Se evalúa antes de invitar a un tercero.

## Ruta y contenido

- **Primero kana, después palabras** (24/9). Surgió al revisar la lección Saludos: こんにちは usaba un kana que el curso todavía no había enseñado. Una auditoría encontró catorce lugares con el mismo problema (lecciones, preguntas, ejemplos, fichas de kana, datos y notas), y se arreglaron todos. La regla cubre también lo que se escucha: «no le veo lo positivo al audio sin sustento». La implementación (25/9) se verificó con una auditoría automática de 115.250 preguntas generadas y de todas las páginas, sin progreso y con todo aprobado, más un recorrido real desde cero hasta el primer hito.
- **Frases como hitos** (24/9, opción A). Las diez frases de todos los días se destraban al aprobar la lección de kana que las completa y se consolidan en «Frases de todos los días», después de Palabras 12. *Descartado:* las lecciones Saludos y Cortesía, y cualquier franja de frases «de oído».
- **ん se adelanta a la lección de な** (24/9). Destraba mucho: con ella, さん y なん se pueden usar desde «X は Y です». El resto del orden de filas no cambia.
- **«Cómo funciona el japonés» se parte en dos lecciones de mapa** (24/9): I, cómo se ve y cómo suena; II, cómo se arma una oración. Presentar la lógica general al inicio da curiosidad. Son la única excepción a la regla: romaji en todo, también en preguntas y respuestas, y ninguna pregunta de lectura de kana. Llevan marcas «→» que dicen cuándo se retoma cada idea, en unidades o en lo que la persona va a hacer, nunca con títulos de lecciones.
- **Tonos sin audio** (24/9). El par あめ (lluvia/caramelo) va como texto: la voz sintetizada no respeta el tono.
- **Negación con では ありません** (24/9), en la lección de の y en el Diálogo. La forma coloquial (じゃないです) usa la ゃ pequeña de la unidad 4: se anuncia sin mostrarla.
- **ぢ y づ** (25/9). Se mencionan en «た y だ» como información, sin práctica. Aceptado.
- **Los textos no filtran el desarrollo** (25/9; principio 10). Explicaciones que solo tienen sentido para quien hizo el camino sobran. Ejemplo: «Los saludos no se memorizan de oído…» respondía a una pregunta que nadie hizo. Con este criterio se revisaron todos los textos de la app el 25/9. Los que se redactaron al implementar la ruta quedan por revisar (#18).
- **Cómo funciona el japonés II: «perro grande»** (25/9). La pregunta lleva la traducción literal junto al romaji, porque mide el orden y no el vocabulario. *Descartado:* aclarar el adjetivo al final («el perro es grande»): «un detalle muy fino para incluir al principio».
- **Ejercicios de armar la estructura con bloques en español** (25/9), en Cómo funciona el japonés II: «Yo como sushi» (con verbo) y «El perro de Tanaka» (sin verbo, suma variedad), de tres piezas. *Descartado:* uno de cinco piezas: nadie que recién leyó un párrafo sobre estructura puede armarlo.
- **Seis palabras por lección de palabras** (desde la unidad 1; se sumaron いけ, すいか, たこ, くつ y おかね para completarlas).

## Lección de palabras

- **Un solo flujo, todo puntuado.** Tandas de dos palabras: se presentan y se reconocen enseguida. Desde la segunda tanda vuelven palabras anteriores, con audio y producción.
- **Emparejar.** Dos ejercicios de cinco pares: el primero al cerrar la última tanda y el segundo en medio del cierre. A la derecha sobra un significado, para que el último par no salga por descarte. Cada par cuenta como una respuesta.
- **Cierre.** Dos preguntas con dibujo, tres de armar la palabra (una por audio) y opción múltiple hasta que cada palabra aparezca al menos tres veces. En total, unas 22 pantallas y 24 respuestas.
- **Opciones honestas.** En las tandas, las opciones salen solo de palabras ya presentadas o de lecciones anteriores.
- **Las falladas se repiten al final, sin sumar.**
- **«Para recordarla» al fallar** (24/9). Solo aparece si la palabra tiene asociación, dibujo o kanji; los datos culturales siguen en la presentación, pero no al fallar.

## Puntaje, bloqueo y llave de prueba

- **80 % para aprobar** en todo el curso (kana, palabras, gramática). Aprobar destraba la lección siguiente. Se guarda la mejor nota. Lo aprobado antes de la regla sigue aprobado.
- **Llave de prueba.** Cinco toques al paraguas de la principal destraban todo, solo en ese dispositivo y con un aviso en rojo. Abre lecciones pero no las aprueba: no destraba frases.

## Hitos de frases

Diseño aprobado el 24/9, sobre bocetos con los estilos de la app.

- **La lección anuncia la cantidad**, no las frases: «Al aprobar, destrabás N frases».
- **Tarjeta «¡Ya podés leer!» en dos momentos.** Primero la frase sola, con la llave (el kana que la completó) en verde y la invitación a leerla en voz alta. Al tocar «Ver cómo se lee», la tarjeta crece en el lugar: audio, romaji, significado, «¿Cuándo se usa?» (máximo 170 caracteres) y, si hace falta, una nota de lectura. En la unidad 3 el romaji sigue detrás de su botón aun después de revelar: la comprobación de la lectura es el audio.
- **Una pregunta de uso por hito.** No suma al puntaje (la lección ya está aprobada) y no vuelve si se falla.
- **Cierre** con la barra de diez frases agrupada por hito y las próximas anunciadas sin mostrarlas.
- **Después**, las frases viven en la sección «Frases» de Mis palabras y al pie de cada lección de kana aprobada.
- **Casos borde.** La secuencia se ve solo la primera vez; el progreso anterior al cambio destraba las frases solo; si alguien sale del resultado sin verla, la lección la ofrece hasta que la vea.
- *Descartado:* la lista de cada kana con la lección donde se aprendió, debajo de la tarjeta. Informaba pero no enseñaba, repetía kana recién leídos y obligaba a desplazarse.
- *Descartado en las preguntas de situación:* los distractores que serían correctos en japonés real (すみません para agradecer un regalo, こんにちは para abrir una presentación, ありがとう ございます antes de comer).
- *Límite conocido:* en un teléfono chico (360 × 640) la tarjeta de よろしく おねがいします necesita desplazarse (#19).

## Repasos

Diseño aprobado el 24/9; la misma lógica en las tres unidades.

- **Veinte preguntas, todas puntuadas**, que se aprueban con 16. Las falladas se repiten al final sin sumar.
- **Kana con ゛ y ゜ incluidos** (se corrigió un error que los dejaba afuera).
- **Dos palabras de cada lección de palabras**, con los tipos del ciclo. El repaso prioriza cubrir la unidad; la práctica ponderada vive en Repaso de kana y Mis palabras.
- **Nunca preguntas de las lecciones de mapa.** Sus ideas vuelven en el repaso de la unidad 1 como preguntas puente, hechas con palabras que ya se leen.
- **Cada error indica de qué lección viene.**

## Mis palabras

- **Solo entran las palabras de lecciones de palabras aprobadas** (24/9). Los ejemplos de las fichas de kana (え, きく, せかい…) no se suman: «es la más honesta», sin complejizar las reglas. Hasta el 2/10 entraban también las palabras propias (ver «Sin palabras propias»).
- ~~**Las palabras propias conservan su kanji**~~ (reemplazada el 2/10: ya no hay palabras propias). En las listas del curso el kanji de referencia está oculto.
- **Pantalla ordenada** (2/10, boceto B-02, superado por B-03; #20 a #24). Hay dos usos de las palabras y cada uno lleva sus controles: arriba las tarjetas (el botón, «Pensalo primero», que las modifica, y las estadísticas) y abajo un solo cuaderno, con los controles agrupados en Tapar y Orden. La explicación pasa a una ayuda «?» que se abre sola la primera vez, porque «pierde sentido que esté ahí luego de la primera lectura» (regla en la guía de estilo). Las frases pendientes se agrupan por lección. *Descartado:* el «?» a la izquierda del título, un globo flotante y nombrar a Duolingo en la app.
- **Sin palabras propias** (2/10, boceto B-03; #25). Se quita la posibilidad de agregar palabras: no había cómo controlar que el japonés y el significado fueran correctos, era la única vía por la que entraba contenido que rompe el principio 1 (kana no enseñados, katakana, kanji), una palabra mal cargada contaminaba las opciones de las tarjetas del curso y nació para sumar palabras de Duolingo, un uso que no existe desde que Kasa es la única herramienta. «Me importa mucho que Kasa sea sólido, aunque eso signifique que sea más simple o tenga menos funciones.» Con ellas se van el conversor de romaji y el modo katakana; «Borrar» en Ajustes ya no conserva las estadísticas de las palabras. *Descartado:* validar o sugerir con un diccionario abierto (JMdict, CC BY-SA 4.0, con pocas glosas en español), un traductor automático o Claude por API: el significado no se puede validar del todo (homófonos como かみ o はし) y cada opción suma datos de terceros, un servidor o dependencia de la conexión. Si alguna vez vuelve, se diseña como proyecto propio, después del katakana.

## Tabla de kana y ficha de kana

- **«Tabla de kana»** (2/10; #5). El nombre cubre los dos silabarios. El katakana se suma con dos pestañas arriba, ひらがな | カタカナ, cuando el curso lo enseñe (#15). *Descartado:* agregar la tabla de katakana al final de la de hiragana, porque las dos tienen la misma forma y duplicaría un desplazamiento que ya es largo.
- **La tabla vacía queda como está** (2/10). La primera vez todo se ve en gris y el texto explica que los kana aparecen en tinta al aprobar sus lecciones.
- **Sin «Para recordarlo» en los kana** (2/10, boceto B-04; #26). «No me parece que sume.» Las asociaciones eran solo texto, sin dibujo, algunas flojas, y en la ficha competían con el trazo, que es lo que fija la forma. Se quitan de la ficha y del comentario al fallar en las lecciones de kana, y se borran sus 46 frases. En los kana con ゛ y ゜ queda una línea propia, «Es か con las dos rayitas (dakuten): el mismo kana con una marca», porque es un dato y no una asociación: explica que no es un kana nuevo. No cambia «Para recordarla» de las palabras, que sigue al fallar. *Descartado:* conservarlo solo al fallar.
- **Ficha ordenada** (2/10, boceto B-04; #27). El kana y su lectura, más grandes y en tinta, porque identifican la ficha. «Escuchar» y «Borrar trazo» en una fila; «Ocultar modelo» pasa a un interruptor, «Modelo de fondo», porque solo en la segunda fila se veía desprolijo. El mismo aire arriba y abajo del cuadro de trazo.
- **Orden de trazos animado: queda como está** (2/10). La ficha sigue con la regla general («de arriba hacia abajo y de izquierda a derecha»). Si se retoma: los trazos salen de KanjiVG (los 71 hiragana son 208 trazos, unos 21 KB; el katakana, del mismo lugar), con licencia CC BY-SA 3.0, que pide nombrarlo y compartir esos datos con la misma licencia; irían en un archivo aparte del resto de la app. Los trazos de KanjiVG son de grosor parejo y no coinciden del todo con la letra del modelo.

## Repaso de kana

- **Pantalla propia antes de la práctica** (2/10, boceto B-05; #28). Hasta entonces la herramienta entraba directo a la ronda. La pantalla dice qué entra (cuántas preguntas y cuántos kana, «por ahora» mientras falten), el último repaso con su fecha en palabras (hoy, ayer, hace N días; desde la semana, la fecha) y su puntaje, y abajo «Empezar repaso». *Descartado:* «Iniciar lección», porque no es una lección; «Empezar repaso» ya se usaba en la app.
- **Se guarda el último repaso** (2/10; #28): fecha, aciertos y total. Antes no se guardaba nada de los repasos, solo los aciertos y errores de cada kana. El progreso anterior no lo tiene, así que la primera vez dice «Todavía no hiciste ningún repaso». «Borrar» en Ajustes también lo borra.
- **«Los que más te cuestan»** (2/10; #28). Hasta tres kana tocables, que abren su ficha: los que aparecieron al menos tres veces y tienen errores, primero los de más errores por aparición. Cuentan todas las prácticas, no solo los repasos, y la cuenta no tiene fecha, así que un kana que costó al principio baja de a poco. Sin datos suficientes, la sección no aparece.
- **Al terminar se vuelve a la pantalla del repaso** (2/10; #28), con «Volver al repaso», como Mis palabras con sus tarjetas, para ver el puntaje nuevo.

## Dibujos y preguntas con dibujo

La regla completa está en la guía de estilo («Dibujos» y «Preguntas con dibujo: zona marcada»).

- **Una lógica general, sin particularidades por caso** (24/9). La pregunta marca una zona del dibujo y el enunciado es siempre el mismo. Una escena sirve para varias palabras.
- **Palabras de cualidad o de momento** (colores, adjetivos, momentos del día, estaciones) nunca salen como opciones en un dibujo.
- **Si una zona deja otra palabra defendible, esa palabra va con dato en vez de dibujo** (うみ, さくら).
- **Cada escena declara lo que muestra sin zona propia** (25/9): かお en el rostro, いけ en el jardín. Eso nunca sale como opción en sus preguntas.
- **Estilo:** ícono plano con contorno índigo, lo más japonés posible.
- **Ajustes pedidos al revisar las escenas:** la llave más chica (quedó al 60 %), la mano del chico a la altura del mentón con el brazo vertical, el perro sobre el pasto detrás del estanque.

## Enriquecimientos y asociaciones

- **Uno por palabra, de hasta 170 caracteres:** dibujo, dato cultural o asociación de sonido. El límite es para que la presentación entre sin desplazarse.
- **Nada de kanji mientras el curso no los enseñe**, ni en enriquecimientos ni en asociaciones.
- **Asociaciones solo donde salen naturales.** Mejor dejar una palabra sin asociación que forzarla. Se sacaron las de あお, かお, うえ y あき.
- **El dato del semáforo azul (あお) quedó con duda:** ver el issue #12.

## Identidad: nombre, logo y apertura

- **Kasa** (かさ, paraguas), por la asociación casa/paraguas. Que no aluda a aprender no preocupa.
- **Logo: el paraguas solo.** La casa ya está en el nombre. Un wagasa en perspectiva tres cuartos, con 18 varillas, índigo con anillo crudo y centro sakura, sobre crudo. Referencia: una figura de espaldas en yukata con un wagasa janome, «algo así pero simplificado». *Descartados:* el sello, el rojo (transmite alerta, como una señal de tránsito) y la figura de espaldas.
- **El grillo bajo el paraguas** (25/9). Genérico, chico y sentado, «algo sutil y suave», nada derivado de personajes conocidos. Esquina inferior izquierda; contorno y cabeza índigo, cuerpo gris azulado, franjas del ala en el azul del paraguas. Va en la apertura y en la barra superior, no en el ícono.
- **Apertura.** かさ en vertical con «Kasa» debajo, en Shippori Mincho, y el wagasa a la izquierda con la misma altura que el texto. Dura dos segundos y pasa sola a la principal.
- **Ícono de la app** (28/9): el paraguas solo, sin grillo ni letras.

## Principal, navegación y ajustes

- **Principal, boceto A** («barra discreta», elegido sin dudas). Sin desplazamiento: arriba la barra con el paraguas y el engranaje; al centro la tarjeta de la unidad actual (abre el temario) y el botón de la lección siguiente; abajo la caja de herramientas. El espacio vacío no preocupa: «para cortar, siempre hay tiempo». La 0.4.0 cambia el botón, la tarjeta y el contador de Mis palabras (#2, #3, #4) y el nombre de la tabla (#5).
- **Barra superior en todo el curso** (27/9). La de la principal se repite en todas las pantallas, con el «X de Y» de las prácticas. Engranaje solo en la principal; casita en el resto. Altura B (intermedia), elegida sobre bocetos: «me gusta mucho cómo quedó».
- **Salir de una práctica empezada pide confirmación** (27/9), con la casita, «Salir» o el gesto de volver, porque se pierde lo hecho.
- **«Volver» abajo a la derecha** (24/9, opción C, sobre bocetos). Barra inferior fija con un nombre corto («‹ Unidad 1»), igual en todas las pantallas; la principal no la lleva.
- **El gesto de volver del teléfono también navega** (25/9), y se mantiene el botón propio.
- **Indicador de «hay más abajo».** Degradé y una flecha centrada que salta tres veces, se va al llegar al final y, al tocarla, baja.
- **Tarjetas con un dato largo** (p. ej. あお). Si solo una fracción de «Seguir» queda bajo la barra de «Salir», la tarjeta se compacta (espacios, nunca letras, y solo lo necesario); si hay más contenido debajo, se mantiene la flecha.
- **Ajustes en pantalla propia:** romaji, velocidad del audio, audio, efectos de sonido, progreso, llave de prueba (visible si está activa) y versión.
- **Modo oscuro:** al final (issue #16). La paleta está guardada en el CSS.

## Sonidos

La regla completa está en la guía de estilo («Sonidos»). Las alternativas probadas y descartadas, y los insectos de Japón, se pueden escuchar en el [muestrario](sonidos/muestrario.html).

- **Todo hecho en casa** (26/9). Síntesis en el momento, sin grabaciones de terceros ni derechos ajenos, con timbres acústicos japoneses.
- **Elegidos** (26/9): acierto, koto; error, madera; emparejar, campanitas; armar la palabra, pieza de shōgi; lección aprobada, koto; no aprobada, nota neutra; hito, fūrin de hierro. *Descartados:* campanita y pinpon para el acierto, koto grave para el error, piedra de go para las fichas, silencio para la lección no aprobada, fūrin de vidrio para el hito.
- **La voz espera al efecto** (26/9): 0,55 s después del acierto y 0,4 s después del error; la madera, unos dB por debajo del acierto.
- **Volumen** (26/9): deslizador en Ajustes, solo para los efectos, con mute a la izquierda y una muestra al soltar: «muy prolijo».
- **Verano de Evangelion** (26/9): una minminzemi rehecha a partir de grabaciones reales de referencia. Suena en la apertura, sigue sobre la principal («le da continuidad al ingreso a la app») y al tocar el paraguas de la barra; tocar mientras suena no la reinicia.
- **Tema cerrado** (27/9): «Sonidos listos». Quedan para más adelante el volumen de la pieza de shōgi (#11) y el uso de los insectos (#10).

## Transiciones

La regla completa está en la guía de estilo («Transiciones entre pantallas»).

- **Algo simple** (28/9): laterales para avanzar o retroceder por el camino; verticales para lo que se abre y se cierra.
- **La barra superior no se anima** (28/9): «no tiene sentido animar una barra que es una constante a lo largo de todo el curso».
- **Elegidas sobre pruebas en el teléfono** (28/9): flecha ⌄ en lo que se cierra bajando, barra de volver quieta y duración rápida (0,2 s). En el visor de claude.ai aparece un destello negro, que es del visor y no de Kasa.

## App instalable y publicación

- **App instalable (PWA) publicada con GitHub Pages** (28/9). Funciona sin conexión, con ícono propio. El progreso queda en el teléfono, sin sincronizar.
- **Versionado semántico** (28/9). Ver el [README](../README.md#versiones).
- **Aviso de versión nueva** (28/9). Fila «Versión» en Ajustes con «Buscar» o «Actualizar» y un punto verde en el engranaje. Sin conexión, «Buscar» lo avisa.
- **Instalación guiada** (28/9), «lo más amable y simple posible». Tarjeta «Instalá Kasa en tu teléfono» en la principal, solo en el navegador. Para compartir la app alcanza con el enlace y tocar «Instalar».
- **Samsung Internet → Chrome** (28/9, 0.2.1). Android bloquea el paquete que arma Samsung, así que la app ofrece abrirse en Chrome.
- **Cuenta personal efevali** (1/10, 0.2.2). Kasa es uno de sus proyectos. kasalearn quedó como organización vacía de efevali para que nadie más tome el nombre.
- *Descartado:* llevar el progreso de la dirección vieja a la nueva (0.3.0, quitado en la 0.3.1): no hacía falta conservar ese progreso.
- **Pantalla de carga de Android antes de la apertura** (28/9): «no está nada mal», por ahora queda así (#13).
