# 02. Plano de Mareas

**Versión original en inglés:** [02 - Tideframe Blueprint](./02%20-%20Tideframe%20Blueprint.md)

**Curso:** HTML
**Tema:** Esqueleto de página Tideglass, árbol de mareas, comentarios, atributos, clases/ID, divs, estilos en línea y en bloque
**Etiquetas:** `#html` `#web-development` `#structure` `#attributes` `#tideglass`

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

Un registro breve en una sola página sirve para una nota matinal, pero el observatorio necesita un plano estándar para todas sus páginas públicas. Ese plano es el *tideframe*: un esqueleto de documento, una forma de etiquetar sus partes para estilos futuros y un modo de dejar notas sin imprimirlas en el tablero mojado por la marea. Todo lo que se añade aquí tiene un único objetivo: hacer que las páginas sean localizables por otro código más adelante.

> [!NOTE]
> **Las etiquetas son asas**
> `class` y `id` no son decoraciones. Son asas que CSS, JavaScript y las herramientas de accesibilidad usan para actuar sobre elementos concretos. Un elemento sin etiqueta es un elemento al que no se puede apuntar de forma fiable.

## El esqueleto del tideframe

Toda página publicada por el observatorio empieza igual. `<!DOCTYPE html>` indica al navegador que es HTML5. `<html>` envuelve todo el documento. Dentro, `<head>` contiene metadatos que el visitante no ve (como el título de la pestaña), y `<body>` contiene todo lo visible en el tablero del muelle de cristal.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Observatorio Tideglass — Estado de la estación</title>
  </head>
  <body>
    <h1>Estado de la estación</h1>
    <p>Todas las boyas informan lecturas nominales.</p>
  </body>
</html>
```

El `<title>` es lo primero que ve un vigilante en la pestaña del navegador. Si falta, la pestaña muestra la ruta del archivo, lo cual resulta poco práctico cuando hay varias páginas abiertas. Debe ser breve y específico para esa página, no para todo el archivo.

> [!WARNING]
> `<head>` no es lo mismo que `<header>`. `<head>` son metadatos; `<header>` es contenido visible. Confundirlos es uno de los errores más comunes y tiene consecuencias reales para las tecnologías de asistencia.

## El árbol de mareas

Los elementos HTML forman un árbol. Un padre puede contener hijos, los hijos pueden contener nietos y los hermanos comparten el mismo padre. Entender este árbol es fundamental al escribir listas anidadas o agrupar tarjetas de instrumentos.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Tripulación de Tideglass</title>
  </head>
  <body>
    <h1>Turnos de vigilancia</h1>
    <p>Tripulación de guardia nocturna — <i>Ciclo 7</i>.</p>
  </body>
</html>
```

En esa estructura, `<html>` es padre de `<head>` y `<body>`. `<head>` es padre de `<title>`. `<body>` es padre de `<h1>` y `<p>`. `<i>` es hijo de `<p>`. `<h1>` y `<p>` son hermanos. Este anidamiento es exactamente el que siguen los estilos y el recorrido del DOM.

### Listas de guardia anidadas

Una lista de guardia suele anidar responsabilidades bajo cada rol. Una lista dentro de otra refleja esa jerarquía de forma natural.

```html
<ul>
  <li>Vigilante de mareas — Mora
    <ul>
      <li>Lecturas del medidor</li>
      <li>Cálculo de las mareas muertas</li>
    </ul>
  </li>
  <li>Operador de radio — Finch
    <ul>
      <li>Enlace con Coastwatch</li>
      <li>Seguimiento del canal de tormentas</li>
    </ul>
  </li>
</ul>
```

> [!TIP]
> Si puedes trazar las líneas padre/hijo sobre el papel y coinciden con lo que escribiste, la indentación es correcta. Si el árbol tiene sentido, los selectores CSS serán mucho más fáciles de escribir después.

## Comentarios e intención

Los vigilantes dejan notas de campo entre ellos. En HTML, los comentarios `<!-- ... -->` hacen lo mismo: los ignora el navegador y son visibles para quien lea el código fuente. La regla: explica *por qué*, no *qué*. Las etiquetas ya dicen qué son.

```html
<!-- Restringir este panel al personal hasta que se reabra el espigón sur. -->
<div class="restricted-panel">
  <p>Código de acceso al espigón: TIDE-772</p>
</div>
```

Los comentarios pueden ocupar varias líneas y sirven para ocultar temporalmente código roto durante la depuración.

```html
<!-- 
  Bloque temporal para probar el diseño.
  <p>Texto antiguo conservado para comparación.</p>
-->
```

> [!NOTE]
> Comentar en exceso ensucia el código fuente. Un buen comentario responde a una pregunta que un vigilante futuro se haría realmente: «¿Por qué está oculto esto?» o «Esto depende de la pleamar de las 03:00».

## Atributos, clases e ID

Los atributos configuran los elementos. Van en la etiqueta de apertura como `nombre="valor"`. Algunos cambian el comportamiento (como `href` en enlaces o `src` en imágenes), otros sirven para etiquetar y reutilizar.

Las clases agrupan elementos para darles un tratamiento común: cualquier número de elementos puede compartir la misma clase. Los ID identifican un solo elemento de forma única en la página: cada ID debe aparecer solo una vez y no puede contener espacios.

```html
<h2 class="panel-title">Estado del medidor</h2>
<p id="gauge-reading">+2,4 m y subiendo lentamente</p>
<p class="panel-title">Estado de las boyas</p>
```

Un ID también puede enlazar a una sección de la misma página. El `href` del ancla usa `#` seguido del ID.

```html
<a href="#restricted-zone">Ir a la zona restringida</a>
<h2 id="restricted-zone">Zona restringida</h2>
<p>Espigón sur cerrado hasta nuevo aviso.</p>
```

> [!IMPORTANT]
> Un elemento puede tener clase e ID al mismo tiempo: `class="instrument-card"` e `id="north-gauge"`. El ID le da un ancla único y un objetivo preciso; la clase lo incluye en un grupo que comparte reglas de estilo.

## El contenedor genérico: `<div>`

`<div>` es un contenedor en bloque genérico sin significado semántico. Sirve únicamente para agrupar elementos con fines de diseño y estilo. Bien usado crea tarjetas y paneles. Usado como sustituto de todo crea una «sopa de divs» impenetrable.

```html
<div class="instrument-card">
  <h3>Medidor norte</h3>
  <p>Altura: +2,4 m</p>
  <p>Tendencia: Subiendo</p>
</div>

<div class="instrument-card">
  <h3>Medidor sur</h3>
  <p>Altura: +1,8 m</p>
  <p>Tendencia: Bajando</p>
</div>
```

## Estilos en línea y en bloque

Para pruebas rápidas, el atributo `style` aplica CSS directamente a un solo elemento. Para estilos consistentes en muchos elementos, `<style>` en `<head>` usa selectores: nombres de elementos, `.clase` y `#id`.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Prueba de paleta Tideglass</title>
    <style>
      .instrument-card {
        border: 1px solid #00B4D8;
        padding: 8px;
        margin: 6px;
        width: 260px;
      }
      #north-gauge {
        background-color: #E0FBFC;
      }
    </style>
  </head>
  <body>
    <div class="instrument-card" id="north-gauge">
      <h3>Medidor norte</h3>
      <p>+2,4 m — Subiendo</p>
    </div>
    <div class="instrument-card">
      <h3>Medidor sur</h3>
      <p>+1,8 m — Bajando</p>
    </div>
  </body>
</html>
```

> [!CAUTION]
> Los estilos en línea (`style="..."`) anulan la mayoría de los demás estilos, lo que dificulta cambiarlos globalmente. Úsalos solo como último recurso para comprobaciones puntuales, nunca como norma. El objetivo es mantener la estructura en HTML y la presentación en CSS.

## Salida

El plano tideframe produce un esqueleto coherente: doctype, html, head con título, body con contenedores etiquetados. El árbol es predecible, las clases agrupan tarjetas, los ID marcan anclas y los comentarios registran la intención. Incluso con un estilo mínimo, la página se lee como un tablero de estación, no como un montón aleatorio de párrafos.

## Tarea 2: Construir la sala de instrumentos

Crea `instrument-bay.html` con un esqueleto HTML5 completo. Añade un título en `<head>`. En `<body>`, construye una cabecera etiquetada con clases/ID, un «Banco de medidores» con al menos dos `<div class="instrument-card">` cada uno con un encabezado y dos párrafos, una lista de guardia anidada, un comentario que explique por qué una tarjeta está marcada como restringida y anclas internas usando IDs. Opcionalmente añade un bloque `<style>` pequeño en `<head>` para distinguir las tarjetas visualmente.

**Por qué este orden:** las etiquetas y la estructura son el andamiaje: una vez que el árbol está sólido, añadir más secciones nunca requiere desenredar una sopa de `<div>` sin etiquetar.

**Siguiente:** [[03 - Formularios del Puerto]]
