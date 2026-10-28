# 00b. Índice de Tideglass

**Versión original en inglés:** [00b - Tideglass Index](./00b%20-%20Tideglass%20Index.md)

**Curso:** HTML
**Tema:** Referencia rápida de Tideglass — elementos del muelle, esqueleto, enlaces
**Etiquetas:** `#html` `#web-development` `#cheatsheet` `#reference` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cubre-Del%20muelle%20al%20astillero-7C5CFF?style=for-the-badge" alt="Cubre todas las lecciones">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Ola Tideglass" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

Una chuleta de una página para el Observatorio Tideglass. Úsala junto a las notas del muelle y el plano para recordar estructura, listas, enlaces y contenedores sin releer todo el capítulo.

> [!TIP]
> Si por defecto vas a usar `<div>`, revisa esta hoja primero. Nueve de cada diez veces hay un elemento más específico que dice más sobre el contenido.

## Esqueleto
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Nombre de la estación</title>
  </head>
  <body>
    <!-- contenido visible -->
  </body>
</html>
```

## Texto y énfasis
| Elemento | Uso |
| :--- | :--- |
| `<h1>`–`<h6>` | Encabezados (un solo `<h1>` por página) |
| `<p>` | Párrafos |
| `<br>` | Salto de línea (se cierra solo) |
| `<b>`, `<i>`, `<u>`, `<s>` | Énfasis básico (usar CSS para estilos) |

## Listas
| Elemento | Uso |
| :--- | :--- |
| `<ul>` / `<li>` | Lista desordenada (viñetas) |
| `<ol>` / `<li>` | Lista ordenada (pasos) |

## Enlaces e imágenes
| Elemento/Atributo | Uso |
| :--- | :--- |
| `<a href="...">` | Enlaces; el texto debe describir el destino |
| `<a href="..." target="_blank">` | Nueva pestaña (usar con moderación) |
| `<img src="..." alt="...">` | Imágenes; incluir siempre `alt` |

## Estructura y etiquetas
| Elemento/Atributo | Uso |
| :--- | :--- |
| `class="..."` | Agrupar elementos (reutilizable) |
| `id="..."` | Identificador único (anclas, objetivos precisos) |
| `<div>` | Contenedor genérico (usar con clase/id) |
| `<!-- ... -->` | Comentarios (explicar por qué) |

**Siguiente:** [[00c - Guía de Campo de Tideglass]]
