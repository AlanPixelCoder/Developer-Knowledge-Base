# 12. La Carrera de la Marea

**Versión original en inglés:** [12 - The Tide Run.md](./12%20-%20The%20Tide%20Run.md)

**Curso:** CSS
**Capítulo:** 12 — Flexbox
**Tema:** Contenedor/items flex, ejes, justify-content, align-items, propiedades flex
**Etiquetas:** `#css` `#tideglass` `#flexbox` `#layout`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-AVANZADO-FF5252?style=for-the-badge" alt="Avanzado">
  <img src="https://img.shields.io/badge/Capítulo-12-7C5CFF?style=for-the-badge" alt="Capítulo 12">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Cuando cambia la marea, los barcos corren entre boyas para llegar al canal seguro. Deben repartirse, alinearse y adaptarse al espacio disponible. Flexbox hace lo mismo: un contenedor flex distribuye sus elementos a lo largo de los ejes, dándoles margen para crecer, encogerse o alinearse sin lidiar con floats ni posicionamiento complejo.

## El contenedor y los elementos

Convierte un contenedor en flexbox con `display: flex;`. Los hijos directos se convierten en elementos flex. El eje principal es horizontal por defecto (`flex-direction: row`), el eje transversal es vertical.

```css
.fila-lecturas {
  display: flex;
  gap: 12px;
}

.fila-lecturas .elemento {
  /* elemento flex */
}
```

## Alinear a lo largo de los ejes

`justify-content` alinea los elementos a lo largo del eje principal. `align-items` alinea a lo largo del eje transversal. `gap` añade espacio entre elementos.

```css
.barra-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}
```

Valores comunes: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`.

> [!NOTE]
> **Los ejes importan**
> Si `flex-direction` pasa a `column`, el eje principal es vertical y `justify-content` actúa verticalmente mientras `align-items` actúa horizontalmente. Siempre hay que saber qué eje es cuál antes de alinear.

## Controlar el crecimiento con flex

Los elementos flex pueden crecer o encogerse. `flex: 1` hace que un elemento ocupe el espacio restante por igual. `flex-grow`, `flex-shrink`, `flex-basis` dan más control.

```css
.panel {
  display: flex;
}

.principal {
  flex: 1; /* crece para llenar el espacio */
}

.lateral {
  flex: 0 0 200px; /* no crece, no encoge, base fija */
}
```

> [!WARNING]
> **No luches contra el eje**
> Para centrar algo vertical y horizontalmente con flexbox, usa ambos ejes: `justify-content: center; align-items: center;` en el contenedor. Intentarlo solo con márgenes suele ser innecesario cuando flex está disponible.

## Construir la fila de instrumentos de Tideglass

```html
<div class="fila-instrumentos">
  <div class="medidor">Marea: 3.42m</div>
  <div class="medidor">Temp: 12°C</div>
  <div class="medidor">Viento: 18 kn</div>
</div>
```

```css
.fila-instrumentos {
  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 8px;
}

.medidor {
  flex: 1;
  text-align: center;
  padding: 12px;
  border: 1px solid #3a506b;
  background-color: #162636;
}
```

Cada medidor ocupa el mismo espacio. La fila se adapta al ancho — mucho más fácil que trucos con porcentajes y floats.

## Salida

```text
Contenedor: display: flex
Ejes: principal (fila por defecto), transversal
justify-content: eje principal
align-items: eje transversal
flex: crecer/encoger/base
gap: espacio entre elementos
```

### Tarea 12: Correr la marea

Construye una barra de navegación de Tideglass con flexbox. Usa `justify-content: space-between` y `align-items: center`. Crea una fila de tarjetas donde las tarjetas crezcan por igual con `flex: 1`. Centra una sola tarjeta vertical y horizontalmente dentro de un panel usando flexbox. Razona sobre los ejes si cambias `flex-direction: column`.
