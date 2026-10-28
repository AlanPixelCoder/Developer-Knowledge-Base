# 00c. Tideglass Field Guide

**Spanish version:** [00c - Guía de Campo de Tideglass](./00c%20-%20Gu%C3%ADa%20de%20Campo%20de%20Tideglass.md)

**Course:** HTML
**Topic:** Tideglass field guide — attributes, classes/IDs, forms, semantics, entities
**Tags:** `#html` `#web-development` `#cheatsheet` `#forms` `#semantics` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Covers-Forms%20%26%20Semantics-7C5CFF?style=for-the-badge" alt="Covers forms and semantics">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Tideglass wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

Field reference for intake forms and semantic pages at the Tideglass Observatory. Keep labels, constraints, and landmarks straight when building the slipway bulletin and harbor intake forms.

> [!NOTE]
> Labels are required for radios and checkboxes. `name` groups radios/checkboxes; `for` pairs a label with its input's `id`. Put all related inputs inside a single `<form>`.

## Forms Basics
```html
<form action="" method="">
  <label for="vessel">Vessel Name</label>
  <input type="text" id="vessel" name="vessel">
  <input type="submit" value="Submit">
</form>
```

## Common Input Types
| Type | Use | Notes |
| :--- | :--- | :--- |
| `text` | Names, short strings | Pair with `minlength`/`maxlength` |
| `email` | Contact email | Browser checks for `@` |
| `password` | Passcodes | Hidden text |
| `number` | Counts/quantities | Use `min`/`max`/`step` |
| `radio` | One choice from group | Same `name`, unique `id`, label with `for` |
| `checkbox` | Zero or more choices | Same or related `name`, unique `id`, label with `for` |
| `submit` | Send form | Change label with `value` |

## Validation Constraints
| Attribute | Applies to | Purpose |
| :--- | :--- | :--- |
| `required` | Most inputs | Blocks empty submission |
| `minlength` | text/password/email-like | Minimum characters |
| `maxlength` | text/password | Maximum characters |
| `min` / `max` | `number` | Range |
| `step` | `number` | Increment |

## Semantic Landmarks
| Element | Use |
| :--- | :--- |
| `<header>` | Banner/top region |
| `<nav>` | Major navigation links |
| `<main>` | Unique central content (one per page) |
| `<article>` | Self-contained content |
| `<section>` | Related content needing context |
| `<aside>` | Tangential content (sidebar/notes) |
| `<figure>` / `<figcaption>` | Captioned content |
| `<time datetime="...">` | Dates/times (machine-readable) |
| `<footer>` | Closing region |

## Entities (escape as text)
| Entity | Renders |
| :--- | :--- |
| `&amp;` | `&` |
| `&lt;` | `<` |
| `&gt;` | `>` |
| `&quot;` | `"` |
| `&apos;` | `'` |

> [!TIP]
> Semantic audit: one `<main>`, headings on sections/articles, images with `alt` or in `<figure>`, descriptive link text, correct heading order, no raw `&` or `<` in text.

**Back:** [[00b - Tideglass Index]]
