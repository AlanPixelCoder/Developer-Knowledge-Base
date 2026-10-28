# 00c. Guía de Campo de Tideglass

**Versión original en inglés:** [00c - Tideglass Field Guide](./00c%20-%20Tideglass%20Field%20Guide.md)

**Curso:** HTML
**Tema:** Guía de campo Tideglass — atributos, clases/ID, formularios, semántica, entidades
**Etiquetas:** `#html` `#web-development` `#cheatsheet` `#forms` `#semantics` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cubre-Formularios%20y%20sem%C3%A1ntica-7C5CFF?style=for-the-badge" alt="Cubre formularios y semántica">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Leyenda-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Ola Tideglass" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

Referencia de campo para formularios de admisión y páginas semánticas del Observatorio Tideglass. Úsala para mantener correctas las etiquetas, restricciones y puntos de referencia al construir el boletín del astillero y los formularios del puerto.

> [!NOTE]
> Las etiquetas son obligatorias para radios y casillas. `name` agrupa radios/casillas; `for` empareja una etiqueta con el `id` de su campo. Todos los campos relacionados deben ir dentro de un solo `<form>`.

## Fundamentos de formularios
```html
<form action="" method="">
  <label for="vessel">Nombre de la embarcación</label>
  <input type="text" id="vessel" name="vessel">
  <input type="submit" value="Enviar">
</form>
```

## Tipos de entrada comunes
| Tipo | Uso | Notas |
| :--- | :--- | :--- |
| `text` | Nombres, cadenas cortas | Combinar con `minlength`/`maxlength` |
| `email` | Correo de contacto | El navegador comprueba la `@` |
| `password` | Claves de acceso | Texto oculto |
| `number` | Cantidades/números | Usar `min`/`max`/`step` |
| `radio` | Una opción entre varias | Mismo `name`, `id` único, etiqueta con `for` |
| `checkbox` | Cero o más opciones | Mismo `name` o grupo, `id` único, etiqueta con `for` |
| `submit` | Enviar formulario | Cambiar etiqueta con `value` |

## Restricciones de validación
| Atributo | Aplica a | Propósito |
| :--- | :--- | :--- |
| `required` | La mayoría de inputs | Impide envío vacío |
| `minlength` | text/password/email | Mínimo de caracteres |
| `maxlength` | text/password | Máximo de caracteres |
| `min` / `max` | `number` | Rango |
| `step` | `number` | Incremento |

## Puntos de referencia semánticos
| Elemento | Uso |
| :--- | :--- |
| `<header>` | Banner/zona superior |
| `<nav>` | Enlaces de navegación principales |
| `<main>` | Contenido único central (uno por página) |
| `<article>` | Contenido autocontenido |
| `<section>` | Contenido relacionado que necesita contexto |
| `<aside>` | Contenido tangencial (barra lateral/notas) |
| `<figure>` / `<figcaption>` | Contenido con leyenda |
| `<time datetime="...">` | Fechas/horas (legible por máquina) |
| `<footer>` | Zona de cierre |

## Entidades (escapar en texto)
| Entidad | Se renderiza como |
| :--- | :--- |
| `&amp;` | `&` |
| `&lt;` | `<` |
| `&gt;` | `>` |
| `&quot;` | `"` |
| `&apos;` | `'` |

> [!TIP]
> Auditoría semántica: un solo `<main>`, encabezados en sections/articles, imágenes con `alt` o dentro de `<figure>`, texto de enlace descriptivo, orden correcto de encabezados, sin `&` ni `<` sin escapar en texto.

**Volver:** [[00b - Índice de Tideglass]]
