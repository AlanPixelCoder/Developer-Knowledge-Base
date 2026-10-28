# 01. Cimiento del Muelle de Cristal

**Versión original en inglés:** [01 - Glass Pier Primer](./01%20-%20Glass%20Pier%20Primer.md)

**Curso:** HTML
**Tema:** Fundamentos del Observatorio Tideglass — marcar lecturas del muelle, mareas y boyas
**Etiquetas:** `#html` `#web-development` `#basics` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/M%C3%B3dulo-HTML-7C5CFF?style=for-the-badge" alt="Módulo HTML">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Ola Tideglass" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

El Observatorio Tideglass se encuentra al borde de Greyharbor, construido sobre un muelle de cristal para que los vigilantes de mareas puedan leer el agua sin pisar las resbaladizas piedras. Antes de que el tablero de mareas o los instrumentos meteorológicos estén en línea, el personal necesita una página pública para publicar las lecturas del día. HTML es el lenguaje que da a esa página sus cimientos — no su pintura, ni su lógica, solo sus etiquetas.

> [!NOTE]
> **Estructura antes de estilo**
> HTML no dibuja ni anima. Etiqueta el contenido: esto es un encabezado para el medidor de mareas, esto es una lista de boyas, esto es un enlace al pronóstico por horas. CSS y JavaScript vendrán después; si las etiquetas son incorrectas, nada posterior podrá arreglarlo limpiamente.

## Leer el muelle

Un vigilante de mareas nunca escribe un informe completo de golpe. Registra una observación por línea: la altura del medidor, el viento, la visibilidad. HTML refleja ese hábito con **elementos**. Un elemento combina una etiqueta de apertura, contenido y una etiqueta de cierre para indicar qué es cada fragmento de texto.

```html
<p>El muelle de cristal marca +2,4 m en la pleamar.</p>
```

El elemento `<p>` le dice al navegador que se trata de un párrafo. Los encabezados indican la estructura del informe, no el tamaño del texto. Tideglass mantiene exactamente un `<h1>` por página, ya que ese encabezado es el título de todo el registro de la estación del día.

```html
<h1>Observatorio Tideglass — Greyharbor</h1>
<h2>Lecturas matinales del medidor</h2>
<h3>Grupo de boyas del norte</h3>
```

> [!WARNING]
> **Estructura por encima de decoración**
> Usar seis etiquetas `<h1>` no crea seis títulos: rompe la estructura que los lectores de pantalla usan para navegar. Elige un solo `<h1>` y baja un nivel a la vez a medida que el informe se vuelve más específico.

## Marcar notas de marea

Las notas de marea son breves, pero a veces una línea necesita un salto. Pulsar intro dentro de HTML se colapsa en un espacio, así que en el muelle se usa `<br>` para forzar un salto de línea sin crear un nuevo párrafo.

```html
<p>Se mantiene el aviso de marejada ciclónica.<br>Revisa el espigón sur en la siguiente bajamar.</p>
```

No todas las palabras tienen el mismo peso en el tablero de mareas. Para dar énfasis en un registro bruto, `<b>`, `<i>`, `<u>` y `<s>` son útiles. Son herramientas de aprendizaje, no un sistema de estilos: la presentación real corresponde a CSS, pero en un registro sencillo marcan la intención con claridad.

```html
<p>El <b>espigón sur</b> está <i>parcialmente sumergido</i>; <u>solo permitido al personal</u>. El marcador antiguo aparece como <s>aún abierto</s>.</p>
```

> [!TIP]
> Si te encuentras poniendo negrita en cada tercera palabra, lo normal es usar un encabezado mejor o una lista, no más etiquetas de formato. La estructura aporta más énfasis que la decoración.

## Inventario de boyas

Cuando el observatorio lista su equipamiento, el orden rara vez importa: una boya es una boya. Una lista desordenada con `<ul>` y `<li>` las muestra como un conjunto.

```html
<h2>Boyas activas</h2>
<ul>
  <li>NB-01 — Canal norte</li>
  <li>SB-02 — Aproximación sur</li>
  <li>GB-03 — Entrada a Greyharbor</li>
</ul>
```

Cuando los vigilantes necesitan seguir una secuencia, como una lista de verificación antes de una tormenta, una lista ordenada con `<ol>` deja los pasos claros.

```html
<h2>Lista de verificación antes de tormenta</h2>
<ol>
  <li>Asegurar las amarras sueltas en el muelle de cristal.</li>
  <li>Registrar la altura actual del medidor y la tendencia barométrica.</li>
  <li>Izar la bandera de zona restringida en el espigón sur.</li>
  <li>Confirmar que el turno de radio está activo.</li>
</ol>
```

## Enlazar el tablero de mareas

Ningún observatorio es una isla. La página pública necesita enlaces al pronóstico por horas e imágenes de los instrumentos. La etiqueta `<a>` apunta a otros sitios con `href`, y el texto debe decir a dónde lleva, no suplicar que se haga clic.

```html
<a href="https://example.org/greyharbor/forecast">Pronóstico de mareas por horas de Greyharbor</a>
```

Para mostrar los instrumentos se usa `<img>`. Toda imagen debe llevar texto `alt`: si se pierde la conexión con el muelle o si se usa un lector de pantalla, ese texto es lo que quedará.

```html
<img src="https://placehold.co/320x200" alt="El muelle de cristal del Observatorio Tideglass en bajamar, mostrando la carcasa del medidor">
```

## Salida

Una página mínima del muelle se renderiza como un registro legible de la estación: un título, un encabezado de lecturas, una nota breve, una lista de boyas y un enlace al pronóstico. En el navegador aparece sencilla por diseño: el valor está en la estructura, no en la decoración.

> [!CAUTION]
> Los espacios en blanco en HTML se colapsan. Docenas de saltos de línea en el editor se convierten en un solo espacio entre palabras. Usa `<br>` para saltos intencionales y `<p>` para nuevos bloques de texto. Si una línea parece unirse a la anterior, lo más probable es que sea el colapso de espacios en blanco.

## Tarea 1: Publicar el registro matinal

Crea `pier-log.html` para el Observatorio Tideglass. Debe incluir un solo `<h1>` con el nombre de Greyharbor, un `<h2>` para las lecturas matinales, un párrafo con al menos un `<br>` y al menos dos tipos de formato de texto, una lista desordenada con tres boyas, una lista ordenada con tres pasos de la lista de verificación, una imagen con texto `alt` significativo y un enlace al pronóstico con texto descriptivo.

**Por qué este orden:** marcar la estructura primero permite publicar un registro legible incluso en un navegador muy básico, y añadir CSS después sin reescribir el significado de la página.

**Siguiente:** [[02 - Plano de Mareas]]
