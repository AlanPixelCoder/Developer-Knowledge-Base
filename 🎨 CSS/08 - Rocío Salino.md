# 08. Rocío Salino

**Versión original en inglés:** [08 - Salt Spray.md](./08%20-%20Salt%20Spray.md)

**Curso:** CSS
**Capítulo:** 8 — Fondos y Abreviaturas
**Tema:** background-color, background-image, abreviaturas, border/font shorthand
**Etiquetas:** `#css` `#tideglass` `#backgrounds` `#shorthands`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-8-7C5CFF?style=for-the-badge" alt="Capítulo 8">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

El rocío salino cubre las paredes de Tideglass: desgasta la pintura pero deja marcas duras. En el sitio de instrumentos, los fondos separan paneles de la página, dan pistas sutiles sin saturar y deben mantener el contraste suficiente para el texto. Las abreviaturas permiten escribir reglas compactas, pero solo funcionan si se sabe qué significa cada parte.

## Color e imagen de fondo

`background-color` rellena el fondo del elemento. `background-image` añade una imagen. Por defecto las imágenes se repiten; para paneles simples lo habitual es un color sólido con contraste suficiente para el texto encima.

```css
.panel-instrumentos {
  background-color: #162636;
  color: #f0f6ff;
}

.marco-grafica {
  background-image: url("reja-superpuesta.png");
  background-repeat: no-repeat;
  background-size: cover;
}
```

Los fondos decorativos deben ser sutiles. Si el texto se vuelve difícil de leer sobre una imagen, añade un color sólido detrás o aumenta el contraste.

> [!WARNING]
> **El contraste es innegociable**
> El texto sobre un fondo recargado falla en su función. Si el aviso es lo importante en una tormenta, debe seguir siendo legible. Piensa en la página bajo una llovizna gris, no solo con sol.

## Abreviaturas: escribir menos, saber más

Una abreviatura establece varias propiedades a la vez. El orden puede importar y los valores omitidos vuelven a sus valores por defecto. Dos comunes son `background` y `border`.

```css
/* largo */
.panel {
  background-color: #0f1f2b;
  background-image: none;
}

/* abreviado */
.panel {
  background: #0f1f2b none;
}
```

Para `border`: grosor, estilo, color.

```css
.franja-aviso {
  border: 2px solid #ff6b35;
}

/* equivalente a: border-width: 2px; border-style: solid; border-color: #ff6b35; */
```

> [!CAUTION]
> **La abreviatura reinicia valores por defecto**
> Al usar `border: 2px solid #ff6b35;` en un elemento que ya tenía otros bordes definidos, la abreviatura puede reiniciar partes no especificadas según el contexto. Si solo quieres cambiar un lado, usa la forma larga para ese lado (`border-left`, etc.).

## Abreviatura de fuente

`font` permite establecer varias propiedades tipográficas de golpe. Suele requerir `font-size` y `font-family`, y puede incluir `font-weight`, `font-style`, `line-height` y más. El orden es estricto en la práctica.

```css
/* largo vs abreviado */
body {
  font: 400 1rem/1.6 "Inter", system-ui, sans-serif;
}
```

Esto fija peso, tamaño/line-height y familia. Lo que se omita vuelve a los valores por defecto. Para claridad en una página de estación, la forma larga suele leerse mejor; la abreviatura sirve si sabes exactamente lo que haces.

> [!TIP]
> **Lee antes de comprimir**
> Antes de cambiar de forma larga a abreviatura, traza cada propiedad. Una compresión que oculte un reinicio inesperado es peor que unas líneas extra.

## Juntándolo todo

```html
<section class="panel-instrumentos">
  <h2>Medidor de Marea</h2>
  <p class="lectura">Nivel del agua: 3.42m</p>
  <div class="franja-aviso">Aviso de marejada ciclónica</div>
</section>
```

```css
body {
  font: 400 1rem/1.6 "Inter", system-ui, sans-serif;
  background-color: #0a1520;
  color: #f0f6ff;
}

.panel-instrumentos {
  background: #162636;
  border: 1px solid #3a506b;
}

.franja-aviso {
  border-left: 4px solid #ff6b35;
  background-color: #2a1f0f;
}
```

## Salida

```text
body:                abreviatura font + fondo oscuro
.panel-instrumentos: fondo sólido + borde
.franja-aviso:       acento izquierdo + fondo teñido
```

### Tarea 8: Recubrir contra el rocío

Estila un panel de instrumentos de Tideglass. Pon un `background-color` oscuro en `body`. Dale a `.panel` un fondo con abreviatura `background` o forma larga (justifícalo). Añade un `border` con abreviatura. Usa `font` abreviado en `body` o explica por qué elegiste la forma larga. Añade `.franja-alerta` con borde izquierdo de acento y fondo teñido. Asegura que el contraste del texto siga siendo alto.
