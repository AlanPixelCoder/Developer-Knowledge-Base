# 00b. Tideglass Quick Reference

**Spanish version:** [00b - Referencia Rápida de Tideglass](./00b%20-%20Referencia%20R%C3%A1pida%20de%20Tideglass.md)

**Course:** CSS
**Chapter:** Reference
**Topic:** Quick reference for CSS syntax, selectors, colors, units, typography and pseudo-classes/elements
**Tags:** `#css` `#tideglass` `#cheatsheet` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Covers-Chapters_01_--_06-7C5CFF?style=for-the-badge" alt="Chapters 01 to 06">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

A compact reference for the first half of the Tideglass Observatory pages. Covers rules, selectors, colors, units, typography, and pseudo-classes/elements. For the frame, spacing, positioning, and flexbox, see [[00c - Tideglass Layout Reference]].

> [!TIP]
> Keep it open beside the editor. Correct names beat guessing.

## Rule anatomy

```css
selector {
  property: value;
}
```

| Part | Role |
| :--- | :--- |
| Selector | What to target |
| Declaration | `property: value;` |
| Block | All declarations for the selector |

## Selectors (core)

| Selector | Syntax | Targets |
| :--- | :--- | :--- |
| Type | `p {}` | All elements of that tag |
| Class | `.warning {}` | Elements with class warning |
| ID | `#chart {}` | Unique element with that id |
| Group | `h1, h2 {}` | Either selector |
| Child | `.panel > h2 {}` | Direct child only |
| Chain | `p.warning {}` | Element AND class |

## Colors

| Form | Example |
| :--- | :--- |
| Named | `color: crimson;` |
| RGB | `color: rgb(255, 107, 53);` |
| Hex | `color: #ff6b35;` |
| Shorthand hex | `color: #f00;` |

## Units

| Unit | Type | Notes |
| :--- | :--- | :--- |
| `px` | Absolute | Fixed, good for borders |
| `%` | Relative | Relative to parent |
| `em` | Relative | Relative to element font size (stacks) |
| `rem` | Relative | Relative to root font size (stable) |

## Pseudo-classes/elements

| Form | Purpose |
| :--- | :--- |
| `:hover` | Pointer over |
| `:focus` | Focused (keyboard) |
| `:nth-child(even)` | Position-based |
| `:not(.archived)` | Negation |
| `::before`/`::after` | Generated content (needs `content`) |
| `::first-letter`/`::first-line` | Part styling |

> [!WARNING]
> `:focus` must remain visible. Never remove outlines without a visible replacement.
