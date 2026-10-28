# 00b. Tideglass Index

**Spanish version:** [00b - Índice de Tideglass](./00b%20-%20%C3%8Dndice%20de%20Tideglass.md)

**Course:** HTML
**Topic:** Tideglass quick reference — pier elements, skeleton, links
**Tags:** `#html` `#web-development` `#cheatsheet` `#reference` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Covers-Glass%20Pier%20to%20Slipway-7C5CFF?style=for-the-badge" alt="Covers all lessons">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Tideglass wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

A single-page index for the Tideglass Observatory. Use it beside the pier log and blueprint notes to recall structure, lists, links, and containers without re-reading the whole chapter.

> [!TIP]
> If you reach for `<div>` by default, scan this sheet first. Nine times out of ten there is a more specific element that says more about the content.

## Skeleton
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Station Name</title>
  </head>
  <body>
    <!-- visible content -->
  </body>
</html>
```

## Text & Emphasis
| Element | Use |
| :--- | :--- |
| `<h1>`–`<h6>` | Outline headings (one `<h1>` per page) |
| `<p>` | Paragraphs |
| `<br>` | Line break (self-closing) |
| `<b>`, `<i>`, `<u>`, `<s>` | Basic emphasis (prefer CSS for styling) |

## Lists
| Element | Use |
| :--- | :--- |
| `<ul>` / `<li>` | Unordered list (bullets) |
| `<ol>` / `<li>` | Ordered list (steps) |

## Links & Images
| Element/Attr | Use |
| :--- | :--- |
| `<a href="...">` | Links; text must describe destination |
| `<a href="..." target="_blank">` | New tab (use sparingly, say so if needed) |
| `<img src="..." alt="...">` | Images; always include `alt` |

## Structure & Labels
| Element/Attr | Use |
| :--- | :--- |
| `class="..."` | Group elements (reusable) |
| `id="..."` | Unique identifier (anchors, precise targets) |
| `<div>` | Generic container (use with class/id) |
| `<!-- ... -->` | Comments (explain why) |

**Next:** [[00c - Tideglass Field Guide]]
