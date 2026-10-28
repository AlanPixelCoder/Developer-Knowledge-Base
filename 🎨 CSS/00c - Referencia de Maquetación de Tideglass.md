# 00c. Referencia de Maquetación de Tideglass

**Versión original en inglés:** [00c - Tideglass Layout Reference.md](./00c%20-%20Tideglass%20Layout%20Reference.md)

**Curso:** CSS
**Capítulo:** Referencia
**Tema:** Modelo de caja, espaciado, display, posicionamiento, z-index, flexbox
**Etiquetas:** `#css` `#tideglass` `#cheatsheet` `#layout` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-F7DF1E?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Cubre-Capítulos_07_--_12-7C5CFF?style=for-the-badge" alt="Capítulos 07 a 12">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Referencia compacta para la segunda mitad de Tideglass. Cubre el modelo de caja, espaciado, display, posicionamiento, apilamiento y flexbox. Para sintaxis y selectores, ver [[00b - Referencia Rápida de Tideglass]].

> [!TIP]
> Cuando el layout falle, traza las capas: contenido -> padding -> borde -> margen.

## Modelo de caja

De dentro hacia fuera: **contenido | padding | borde | margen**  
El fondo cubre **contenido + padding** únicamente.

| box-sizing | Efecto |
| :--- | :--- |
| `content-box` (por defecto) | `width` = solo contenido; padding/borde se suman |
| `border-box` | `width` = contenido + padding + borde |

## Display

| Valor | Comportamiento |
| :--- | :--- |
| `block` | Nueva línea, ancho completo |
| `inline` | Flujo con texto, sin width/height |
| `inline-block` | Flujo inline, acepta width/height/padding/margin |
| `none` | Eliminado del flujo |

## Position

| Valor | Contexto |
| :--- | :--- |
| `static` | Flujo normal |
| `relative` | Relativo a posición normal; permanece en flujo |
| `absolute` | Relativo a ancestro posicionado; sale del flujo |
| `fixed` | Relativo a ventana; sale del flujo |
| `sticky` | Relativo hasta hacer scroll, luego fijo |

## Flexbox

| Propiedad | Uso |
| :--- | :--- |
| `display: flex` | Crear contenedor |
| `justify-content` | Alineación eje principal |
| `align-items` | Alineación eje transversal |
| `flex-direction` | Dirección del eje |
| `flex: 1` | Crecer para llenar |
| `gap` | Espacio entre elementos |
