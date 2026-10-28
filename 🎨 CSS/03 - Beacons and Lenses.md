# 03. Beacons and Lenses

**Spanish version:** [03 - Balizas y Lentes](./03%20-%20Balizas%20y%20Lentes.md)

**Course:** CSS
**Chapter:** 3 — Selectors I
**Topic:** Type, class, id selectors; specificity basics
**Tags:** `#css` `#tideglass` `#selectors` `#specificity`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-3-7C5CFF?style=for-the-badge" alt="Chapter 3">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

On foggy nights the Tideglass beacons guide boats back to the headland. A wide beam lights an entire class of markers; a focused lens points to one exact buoy. CSS selectors work the same way: broad brushes for shared patterns, narrow lenses for specific cases. Aiming well keeps the stylesheet short and predictable.

## Three ways to aim

The most common selectors cover most station pages. Each has a different reach.

| Selector | Syntax | Aims at | Use case |
| :--- | :--- | :--- | :--- |
| Type (element) | `p { }` | All elements of that tag | Global resets or base styles |
| Class | `.alert { }` | Elements with `class="alert"` | Reusable styles shared by many elements |
| ID | `#tide-chart { }` | The element with `id="tide-chart"` | A single, unique element on the page |

```css
/* beacon: all paragraphs */
p {
  color: #dbe9f5;
}

/* lens: any element marked as a warning */
.warning {
  color: #ff6b35;
  font-weight: bold;
}

/* pinpoint: the only chart on the page */
#tide-chart {
  border: 1px solid #3a506b;
}
```

An element can have multiple classes: `class="warning data-row"`. IDs must be unique per page — treat them as one-offs, not a way to style everything.

> [!NOTE]
> **Classes are reusable, IDs are unique**
> Reach for a class when you might need the style again. Reach for an ID only when there truly is one of its kind. Overusing IDs makes future overrides harder for reasons covered in specificity.

## Specificity: which rule wins

When two rules target the same element and set the same property, the browser compares specificity. Higher specificity wins. If specificity ties, the rule that appears later in the stylesheet wins (source order).

Count roughly:
- Type selector: lowest
- Class selector: higher than type
- ID selector: higher than class

```css
p { color: #9fb3c8; }        /* type */
.warning { color: #ff6b35; }  /* class — wins over type */
#alert-main { color: #ff3b30; } /* id — wins over class */
```

If `.warning` and `p.warning` both apply, the more specific one wins. Do not guess — reason about the selectors.

> [!WARNING]
> **Avoid fighting with `!important`**
> `!important` breaks the natural cascade and makes debugging painful on a multi-page site. If a rule needs `!important` to win, the selectors are probably aimed wrong. Fix the aim first.

## Reading a foggy page

Selectors let you style the station without touching every tag. A base style for `body` sets defaults; classes handle variations; an ID handles the one critical element that must stand out no matter what.

```html
<body>
  <section id="tide-chart">
    <p class="data-row">High tide: 05:23</p>
    <p class="data-row warning">Storm surge advisory</p>
  </section>
</body>
```

The chart gets ID styling. Both rows share `data-row`. Only the advisory gets `warning` on top.

## Output

```text
Selector match:
  p                -> all paragraphs (type)
  .warning         -> elements with class warning
  #tide-chart      -> element with id tide-chart

Specificity rough order: type < class < id
Tie broken by: source order (later wins)
```

### Task 3: Aim the beacons

Style a Tideglass instrument list. Use a type selector for base text, a class for `reading` rows, a class for `advisory` (stronger), and an ID for `#last-reading` (unique). Make sure the advisory beats the base reading when both apply. Do not use `!important`. Explain by reasoning which rule wins.
