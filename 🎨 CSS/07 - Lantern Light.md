# 07. Lantern Light

**Spanish version:** [07 - Luz de Farol](./07%20-%20Luz%20de%20Farol.md)

**Course:** CSS
**Chapter:** 7 — Fonts & Text
**Topic:** Font families, stacks, sizing, weights, alignment, decoration
**Tags:** `#css` `#tideglass` `#typography` `#fonts`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-7-7C5CFF?style=for-the-badge" alt="Chapter 7">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

The Tideglass lantern room keeps spare lamps because fog hides the headland. In poor light, readable type matters more than decorative type. On the station site, instrument readouts, advisories, and visiting hours must be legible at a glance. Typography is not about looks alone — it is about clarity under pressure.

## Choosing a font family

`font-family` takes a list (a font stack). The browser tries the first, falls back to the second if unavailable, and ends with a generic family as a safety net. For system fonts, stacks avoid loading delays and keep things consistent.

```css
body {
  font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

code,
.data-readout {
  font-family: "JetBrains Mono", "Fira Code", monospace;
}
```

Use sans-serif for UI text, monospace for numeric readouts where alignment matters.

> [!NOTE]
> **Generics are required**
> Always end with a generic like `serif`, `sans-serif`, `monospace`, or `cursive`. If every named font fails, the browser picks something — without a generic, behavior is undefined in practice.

## Size, weight, and line height

`font-size` sets text size (use `rem` for most cases as before). `font-weight` controls boldness (common values 400, 700, or keywords like `bold`). `line-height` affects readability — too tight feels cramped, too loose feels disconnected. Unitless `line-height` (like `1.6`) scales with font size and is usually safest.

```css
body {
  font-size: 1rem;
  line-height: 1.6;
  font-weight: 400;
}

h1 {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1.2;
}

.data-readout {
  font-weight: 600;
  letter-spacing: 0.02em;
}
```

## Text alignment and decoration

`text-align` controls horizontal alignment (`left`, `right`, `center`, `justify`). `text-decoration` adds lines (`underline`, `line-through`, `none`). For links, removing underlines requires replacing them with other indicators for clarity.

```css
.advisory {
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

nav a {
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}
```

> [!TIP]
> **Clarity over cleverness**
> Uppercase can help labels stand out, but long blocks of uppercase are hard to read. Use `text-transform` sparingly for short labels like headings, tags, or advisories.

## Why it matters

Typography is part of the cascade of legibility. Poor font choices hide important data. Good font choices make the difference between reading a storm advisory quickly and missing it. On Tideglass, that difference is practical.

## Output

```text
Body:        sans-serif stack, 1rem, line-height 1.6, weight 400
Headings:    larger, weight 700, tighter line-height
Readouts:    monospace stack, weight 600, slight tracking
Advisories:  centered, uppercase, spaced
Links:       no underline by default, underline on hover
```

### Task 7: Light the readout

Style a Tideglass reading panel. Set a font stack on `body` ending with a generic. Use `rem` for `h1` and body text. Set unitless `line-height` on body. Style a `.data-readout` with a monospace stack. Center a `.storm-advisory`, uppercase it with `letter-spacing`. Remove underlines from nav links and add them back on `:hover`. Do not sacrifice focus visibility.
