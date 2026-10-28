# 00b. Referencia Rápida de Tideglass

**Versión original en inglés:** [00b - Tideglass Quick Reference.md](./00b%20-%20Tideglass%20Quick%20Reference.md)

**Curso:** CSS
**Capítulo:** Referencia
**Tema:** Referencia rápida de sintaxis CSS, selectores, colores, unidades, tipografía y pseudoclases/pseudoelementos
**Etiquetas:** `#css` `#tideglass` `#cheatsheet` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cubre-Capítulos_01_--_06-7C5CFF?style=for-the-badge" alt="Capítulos 01 a 06">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="Ola azul CSS" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Referencia compacta para la primera mitad de las páginas del Observatorio Tideglass. Cubre reglas, selectores, colores, unidades, tipografía y pseudoclases/pseudoelementos. Para el marco, espaciado, posicionamiento y flexbox, ver [[00c - Referencia de Maquetación de Tideglass]].

> [!TIP]
> Tenla abierta junto al editor. Los nombres correctos ganan a adivinar.

## Anatomía de una regla

```css
selector {
  propiedad: valor;
}
```

| Parte | Función |
| :--- | :--- |
| Selector | A qué apuntar |
| Declaración | `propiedad: valor;` |
| Bloque | Todas las declaraciones del selector |

## Selectores (básicos)

| Selector | Sintaxis | Apunta a |
| :--- | :--- | :--- |
| Tipo | `p {}` | Todos los elementos de esa etiqueta |
| Clase | `.aviso {}` | Elementos con clase aviso |
| ID | `#grafica {}` | Elemento único con ese id |
| Agrupación | `h1, h2 {}` | Cualquiera de los selectores |
| Hijo | `.panel > h2 {}` | Solo hijo directo |
| Encadenado | `p.aviso {}` | Elemento Y clase |

## Colores

| Forma | Ejemplo |
| :--- | :--- |
| Con nombre | `color: crimson;` |
| RGB | `color: rgb(255, 107, 53);` |
| Hex | `color: #ff6b35;` |
| Hex abreviado | `color: #f00;` |

## Unidades

| Unidad | Tipo | Notas |
| :--- | :--- | :--- |
| `px` | Absoluta | Fija, buena para bordes |
| `%` | Relativa | Relativa al padre |
| `em` | Relativa | Relativa al tamaño de fuente del elemento (se acumula) |
| `rem` | Relativa | Relativa al tamaño de fuente raíz (estable) |

## Pseudoclases/pseudoelementos

| Forma | Propósito |
| :--- | :--- |
| `:hover` | Ratón encima |
| `:focus` | Enfocado (teclado) |
| `:nth-child(even)` | Según posición |
| `:not(.archivadas)` | Negación |
| `::before`/`::after` | Contenido generado (necesita `content`) |
| `::first-letter`/`::first-line` | Estilizar parte |

> [!WARNING]
> `:focus` debe seguir visible. Nunca elimines el contorno sin un reemplazo visible.
