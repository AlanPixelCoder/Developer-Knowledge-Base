# 06. Señales de Marea

**Versión original en inglés:** [06 - Tide Signals.md](./06%20-%20Tide%20Signals.md)

**Curso:** CSS
**Capítulo:** 6 — Pseudoclases
**Tema:** :hover, :active, :focus, :visited, :nth-child(), :not(), LoVe/HAte
**Etiquetas:** `#css` `#tideglass` `#pseudo-classes` `#states`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Capítulo-6-7C5CFF?style=for-the-badge" alt="Capítulo 6">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

La torre de señales de marea muestra luces distintas según el estado: una boya tiene un patrón en reposo, otro cuando se le acerca un barco, otro cuando está en mantenimiento. Los enlaces y elementos interactivos necesitan la misma claridad. Las pseudoclases permiten estilizar elementos según su estado o posición, no solo por tipo o clase.

## Estados que el usuario puede provocar

`:hover` se aplica cuando el puntero está sobre el elemento. `:active` se aplica mientras se activa (al pulsar con el ratón, por ejemplo). `:focus` se aplica cuando el elemento recibe el foco por teclado o programáticamente — fundamental para la accesibilidad. `:visited` estiliza los enlaces que el usuario ya ha visitado.

```css
nav a:link {
  color: #7fc3ff;
}

nav a:visited {
  color: #b39ddb;
}

nav a:hover {
  color: #ffffff;
  text-decoration: underline;
}

nav a:focus {
  outline: 2px solid #7fc3ff;
  outline-offset: 2px;
}

nav a:active {
  color: #ff6b35;
}
```

> [!CAUTION]
> **No elimines los contornos de foco sin reemplazarlos**
> Quitar `outline` sin poner un indicador de foco visible hace que la navegación por teclado sea casi imposible. En un sitio público como Tideglass, los estilos de foco son un requisito, no un adorno.

## El orden importa: LoVe/HAte

Para los estados de los enlaces, los navegadores esperan un orden concreto para evitar conflictos. Un mnemotécnico común es LoVe/HAte: `:link` — `:visited` — `:hover` — `:active`. Si `:hover` va antes que `:visited`, este último podría sobrescribirlo según la especificidad; seguir el orden mantiene el comportamiento predecible.

## Seleccionar por posición

`:nth-child()` selecciona elementos según su posición entre hermanos. Puede recibir números, palabras clave (`odd`, `even`) o fórmulas (`2n+1`). En una tabla de mareas de Tideglass, alternar filas mejora la lectura con poca luz.

```css
.tabla-mareas tr:nth-child(even) {
  background-color: #0f1f2b;
}

.tabla-mareas tr:nth-child(odd) {
  background-color: #162636;
}
```

`:not()` niega un selector — útil para estilizar todo excepto un caso concreto.

```css
.lista-lecturas li:not(.sin-conexion) {
  color: #dbe9f5;
}
```

> [!TIP]
> **Cuenta hermanos, no hijos de distinto tipo**
> `:nth-child()` cuenta todos los hermanos sin importar la etiqueta. Si necesitas contar solo ciertos elementos, hay otras pseudoclases, pero para alternar filas simple `:nth-child()` suele ser lo correcto. Razona qué elementos comparten el mismo padre.

## Leer las señales

```html
<nav>
  <a href="#graficas">Gráficas</a>
  <a href="#avisos">Avisos</a>
</nav>
<table class="tabla-mareas">
  <tr><td>05:23</td><td>Marea alta</td></tr>
  <tr><td>11:47</td><td>Marea baja</td></tr>
  <tr><td>17:12</td><td>Marea alta</td></tr>
</table>
```

Los enlaces cambian con hover/focus/active. Las filas se alternan. Los elementos sin clase `sin-conexion` reciben el color base.

## Salida

```text
Estados de enlace: link -> visited -> hover -> focus -> active
Filas alternadas: las filas pares/impares se alternan
:not(.sin-conexion): todos los elementos de lista excepto los que tengan esa clase
```

### Tarea 6: Señalar el canal

Estila una lista de navegación de Tideglass. Aplica los estados en orden LoVe/HAte. Añade estilos visibles para `:focus` (no elimines el outline sin reemplazarlos). Alterna las filas de `.lista-registro` con `:nth-child(even/odd)`. Usa `:not()` para poner en gris solo las entradas `.archivadas` manteniendo las demás legibles. Piensa mentalmente: ¿qué pasa si el orden de foco importa?
