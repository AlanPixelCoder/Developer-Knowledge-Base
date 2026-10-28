# 04. Semántica del Astillero

**Versión original en inglés:** [04 - Slipway Semantics](./04%20-%20Slipway%20Semantics.md)

**Curso:** HTML
**Tema:** HTML semántico para Tideglass — header/main/footer, article/section/aside, nav, figure/figcaption, time, enlaces accesibles, entidades
**Etiquetas:** `#html` `#web-development` `#semantics` `#accessibility` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/M%C3%B3dulo-HTML-7C5CFF?style=for-the-badge" alt="Módulo HTML">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Ola Tideglass" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

Una página construida solo con `<div>` se renderiza correctamente, pero no le dice nada al navegador. Una página construida con elementos semánticos cuenta una historia: dónde está el banner de la estación, dónde vive el informe único, dónde van las notas y los enlaces. En el astillero público de Tideglass eso importa: lectores de pantalla, motores de búsqueda y futuros mantenedores necesitan esos puntos de referencia.

> [!NOTE]
> **Una promesa de significado**
> HTML semántico es una promesa: este elemento significa lo que dice su nombre. El cambio visual suele ser mínimo. El cambio funcional —navegación, comprensión, mantenibilidad— es la razón para usarlos.

## Puntos de referencia: Header, Main, Footer

La mayoría de las páginas de la estación siguen las mismas tres regiones. HTML tiene un elemento para cada una.

- `<header>` — zona del banner: nombre de la estación, logotipo o navegación superior. Puede estar a nivel de página o dentro de un article/section.
- `<main>` — el contenido único y central de la página. Solo debe haber uno por página.
- `<footer>` — zona de cierre: copyright, contacto, notas de licencia. Puede estar a nivel de página o dentro de un article/section.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Observatorio Tideglass</title>
  </head>
  <body>
    <header>
      <h1>Observatorio Tideglass — Greyharbor</h1>
      <p>Observaciones costeras desde el primer muelle de cristal.</p>
    </header>
    <main>
      <p>Estado del astillero hoy: abierto solo al personal hasta las 17:00.</p>
    </main>
    <footer>
      <p>© 2026 Observatorio Tideglass. Lecturas proporcionadas para conocimiento público.</p>
    </footer>
  </body>
</html>
```

> [!IMPORTANT]
> `<header>` y `<footer>` no son lo mismo que `<head>` y `<body>`. Viven dentro de `<body>`, se renderizan y cumplen roles de contenido. Un footer dentro de un article contiene la autoría y la fecha de ese artículo, no necesariamente el texto legal de todo el sitio.

## Artículos, secciones y apartados

No todo el contenido tiene el mismo peso. Algunos fragmentos se sostienen por sí solos; otros solo tienen sentido en contexto; otros son tangenciales.

- `<article>` — contenido autocontenido que tendría sentido si se extrajera y se leyera solo (un boletín de la estación, un informe de boya, una entrada del registro de reparaciones).
- `<section>` — contenido relacionado agrupado que necesita la página que lo rodea para entenderse (un conjunto de notas agrupadas bajo un mismo encabezado).
- `<aside>` — contenido relacionado tangencialmente (informes relacionados, glosario, enlaces rápidos).

```html
<main>
  <article>
    <h2>Boya NB-01: Informe de tensión del cable</h2>
    <p>Se observa un ligero aumento de tensión tras la última marejada. Se continúa el seguimiento.</p>
    <footer>
      <p>Registrado por Mora el <time datetime="2026-10-27">27 de octubre de 2026</time></p>
    </footer>
    <aside>
      <h3>Relacionado</h3>
      <ul>
        <li><a href="#nb-history">Historial de mantenimiento de NB-01</a></li>
        <li><a href="#swell-data">Datos recientes de marejada</a></li>
      </ul>
    </aside>
  </article>

  <section>
    <h2>Notas del astillero</h2>
    <p>La puerta norte del astillero requiere liberación manual en caso de marejada fuerte.</p>
  </section>
</main>
```

> [!TIP]
> Pregunta: «Si copiara esto a otra página, ¿seguiría teniendo sentido?» Si la respuesta es sí, considera `<article>`. Si es no, lo más probable es que sea `<section>`. Esa única pregunta resuelve la mayoría de las dudas.

## Navegación

Los enlaces de navegación principales van en `<nav>`. Un menú del sitio, un índice o la paginación son usos adecuados. Un grupo aleatorio de enlaces en un footer no tiene por qué ir envuelto en `<nav>`: usa el sentido común.

```html
<header>
  <h1>Observatorio Tideglass</h1>
  <nav>
    <ul>
      <li><a href="#readings">Lecturas</a></li>
      <li><a href="#buoys">Boyas</a></li>
      <li><a href="#slipway">Astillero</a></li>
      <li><a href="#intake">Admisión</a></li>
    </ul>
  </nav>
</header>
```

Pueden existir varios elementos `<nav>` —menú principal, índice de artículo, paginación—, cada uno como una región de navegación distinta.

## Figuras, leyendas y fechas

`<figure>` empareja contenido autocontenido (una imagen, un diagrama o un fragmento de código) con una leyenda opcional en `<figcaption>`. La figura es la unidad, no solo la imagen.

```html
<figure>
  <img src="https://placehold.co/320x200" alt="El muelle de cristal en bajamar, mostrando la plataforma del medidor">
  <figcaption>Figura 1: Plataforma del medidor expuesta en la bajamar más baja del Ciclo 7.</figcaption>
</figure>
```

Para fechas y horas, `<time>` con `datetime` ofrece una forma legible por máquina mientras el texto visible es comprensible para humanos.

```html
<p>Aviso de tormenta emitido el <time datetime="2026-10-27T09:00:00Z">27 de octubre de 2026 a las 09:00 UTC</time>.</p>
```

## Enlaces accesibles y entidades

El texto de un enlace debe describir a dónde va. «Hacer clic aquí» no dice nada a un lector de pantalla. Usa etiquetas específicas.

```html
<!-- Mal -->
<a href="/buoys/nb-01">Hacer clic aquí</a>

<!-- Bien -->
<a href="/buoys/nb-01">Informe de mantenimiento de la boya NB-01</a>
```

HTML usa entidades para caracteres que, de otro modo, serían interpretados como marcado o difíciles de escribir. Escapa `&`, `<`, `>`, `"` y `'` cuando aparecen como texto.

| Carácter | Entidad | Uso |
| :--- | :--- | :--- |
| `&` | `&amp;` | Ampersand en texto |
| `<` | `&lt;` | Signo menor que como texto |
| `>` | `&gt;` | Signo mayor que como texto |
| `"` | `&quot;` | Comillas dentro de atributos entre comillas |
| `'` | `&apos;` | Apóstrofes en ciertos contextos |

```html
<p>Las cartas de Mareas &amp; Oleaje muestran lecturas &lt; 0,5 m solo en bajamares extremos.</p>
<p>El cartel dice: «Restringido a <b>&quot;Solo personal&quot;</b>».</p>
```

> [!WARNING]
> Escribir `Cabo & Boya` sin escapar hará que el analizador lo interprete incorrectamente en algunos casos: siempre escapa `&` como `&amp;` en texto. Dentro de valores de atributos que contengan comillas, usa `&quot;` o rodea el atributo con comillas simples.

## Salida

Una página semántica correcta del astillero tiene puntos de referencia claros (`header`, `main`, `footer`), agrupaciones con sentido (`article`, `section`, `aside`), navegación adecuada (`nav`), figuras con leyenda, fechas significativas (`time`), enlaces descriptivos y caracteres especiales escapados. La estructura es navegable con teclado y lectores de pantalla, y mantenible para cualquiera que lea el código fuente.

## Tarea 4: Publicar el boletín del astillero

Crea `slipway-bulletin.html`. Construye una página completa con: `<header>` que contenga un `<h1>` y un `<nav>` con al menos tres enlaces a IDs internos, `<main>` con exactamente un `<article>` (boletín autocontenido) que tenga un `<h2>`, una `<figure>` con `<img>` y `<figcaption>`, un párrafo con un `<time datetime>` dentro, un `<aside>` con enlaces relacionados, y un `<footer>` con autor y fecha dentro del article o a nivel de página según corresponda; una `<section>` para «Restricciones del astillero» con un encabezado y una lista; y usa al menos una entidad HTML en el texto. Asegúrate de que todas las imágenes tengan `alt` y todos los enlaces tengan texto descriptivo.

**Por qué este orden:** la semántica es la culminación: une estructura, etiquetado y accesibilidad para que la página pública sea usable por todos, no solo por usuarios videntes con ratón.

**Siguiente:** Completar el módulo actualizando los README. No hay más lecciones.
