# 09. El Marco de Mareas

**Versión original en inglés:** [09 - The Tideframe.md](./09%20-%20The%20Tideframe.md)

**Curso:** CSS
**Capítulo:** 9 — Modelo de Caja y Bordes
**Tema:** Contenido, padding, borde, margen; inspección de cajas
**Etiquetas:** `#css` `#tideglass` `#box-model` `#borders`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Capítulo-9-7C5CFF?style=for-the-badge" alt="Capítulo 9">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Cada instrumento de Tideglass lleva un marco sellado para protegerlo de la humedad. El marco tiene capas: el cristal y la lectura (contenido), una junta (padding), la carcasa metálica (borde) y el hueco con la siguiente unidad en el bastidor (margen). Las cajas CSS funcionan igual. Si no se ven las capas, no se pueden arreglar los errores de espaciado.

## Las cuatro capas

De dentro hacia fuera:
1. **Contenido** - el texto/imagen real, con tamaño por `width`/`height` por defecto
2. **Relleno (padding)** - espacio entre contenido y borde, dentro del elemento
3. **Borde (border)** - el borde alrededor del relleno
4. **Margen (margin)** - espacio fuera del borde, entre elementos

```css
.marco-datos {
  width: 280px;
  padding: 16px;
  border: 2px solid #3a506b;
  margin: 12px;
}
```

El color de fondo rellena contenido y padding, pero no el margen. El borde queda entre padding y margen.

> [!NOTE]
> **Los fondos se detienen en el borde**
> `background-color` cubre el contenido y el padding. No cubre el área transparente del margen. Es intencional — el margen es espacio entre elementos, no parte de la superficie pintada del elemento.

## Bordes en detalle

Los bordes necesitan al menos un estilo para verse. `border-width`, `border-style`, `border-color` se pueden poner por lado o con abreviatura.

```css
.marco-aviso {
  border-top: 3px solid #ff6b35;
  border-right: 1px solid #3a506b;
  border-bottom: 1px solid #3a506b;
  border-left: 1px solid #3a506b;
}
```

Las esquinas redondeadas vienen con `border-radius`. Incluso un redondeo pequeño suaviza aristas duras en una página de tormenta.

```css
.indicador {
  border-radius: 6px;
}
```

## Inspeccionar para estar seguros

No se puede adivinar el tamaño de una caja a ojo. Razonar ayuda, pero el tamaño renderizado depende de cómo se trate `width`. Aun así, el concepto es el mismo. Con content-box (por defecto), `width` es solo el contenido; el padding y el borde se suman al ancho total.

```css
/* content-box por defecto */
.caja {
  width: 200px;
  padding: 20px;
  border: 5px solid #3a506b;
  /* ancho total aproximado 200 + 40 + 10 = 250px */
}
```

> [!WARNING]
> **El modelo de caja por defecto suma**
> Con `box-sizing: content-box` (por defecto), añadir padding y borde aumenta el ancho renderizado por encima de `width`. Eso sorprende al poner paneles uno al lado de otro. Lo arreglaremos deliberadamente en la siguiente lección.

## Por qué importa

Los errores de espaciado son los más comunes en CSS. Si dos paneles no se colocan donde se espera, la respuesta casi siempre está en padding, borde o margen. Aprender a leer las capas convierte el misterio en cálculo.

## Salida

```text
Capas (de dentro hacia fuera): contenido | padding | borde | margen
Fondo: cubre contenido + padding únicamente
Ancho total (content-box): width + padding*2 + border*2
```

### Tarea 9: Enmarcar el medidor de mareas

Construye un marco para un medidor de Tideglass. Pon `width`, `padding`, `border`, `margin` en `.medidor`. Estila bordes distintos por lado. Añade `border-radius`. Calcula por razonamiento el ancho total si se usa content-box (por defecto). No adivines — escribe el cálculo. Asegúrate de que el color de fondo se vea en contenido+padding pero no cruce el hueco del margen.
