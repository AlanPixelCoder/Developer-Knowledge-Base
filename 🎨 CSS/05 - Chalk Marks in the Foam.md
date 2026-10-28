# 05. Chalk Marks in the Foam

**Spanish version:** [05 - Marcas de Tiza en la Espuma](./05%20-%20Marcas%20de%20Tiza%20en%20la%20Espuma.md)

**Course:** CSS
**Chapter:** 5 — Pseudo-elements
**Topic:** ::first-line, ::first-letter, ::before, ::after, content
**Tags:** `#css` `#tideglass` `#pseudo-elements` `#generated-content`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

When the tide recedes, volunteers mark warnings on the wet concrete with chalk. The marks are not part of the permanent text — they are added for emphasis at that moment: an initial drop cap, a "CAUTION" tag, a tiny marker before a buoy number. CSS pseudo-elements do the same thing: they let you style parts of existing content or add generated content without editing the HTML.

## Styling parts of text

`::first-letter` styles the first character of a block. `::first-line` styles the first line depending on width — it is fluid, not fixed to a character count.

```css
.tide-notice::first-letter {
  font-size: 2rem;
  color: #ff6b35;
  float: left;
  margin-right: 0.4rem;
}

.tide-notice::first-line {
  font-weight: bold;
  letter-spacing: 0.02em;
}
```

These are for typographic touches on existing paragraphs. Keep them restrained — a station page needs to stay readable in poor light.

## Adding marks before and after

`::before` and `::after` create pseudo-elements that are treated as children of the selected element. To actually show content, `content` is required. Without `content`, they render nothing.

```css
.buoy::before {
  content: "⚓ ";
  color: #7fc3ff;
}

.advisory::after {
  content: " [STORM WATCH]";
  color: #ff6b35;
  font-weight: bold;
}
```

The text comes from CSS, not HTML. That is useful for labels that are purely presentational or for consistent markers across many items.

> [!WARNING]
> **Generated content is not in the DOM**
> Screen readers may or may not announce `content`. Treat `::before`/`::after` as decorative or as clearly redundant labels. Never put critical information (like a phone number) only in generated content — it must exist in the HTML if it must be found.

## Why this exists

Pseudo-elements avoid "empty" HTML elements just for styling hooks. A paragraph keeps its natural text; CSS adds the chalk mark. That keeps markup semantic and styling flexible. But it also means the source text in HTML is not the whole visual story — something to remember when copying content.

## Reading foam marks

```html
<p class="tide-notice">Rising water is pushing debris across the lower ramp. Secure gear and avoid the seawall edge until the advisory lifts.</p>
<p class="buoy">Buoy 4 - West Channel</p>
<p class="advisory">Lower landing closed</p>
```

The notice gets a drop-like first letter and emphasized first line. The buoy gets an anchor mark. The advisory gets a tag. None of those symbols exist in the HTML.

## Output

```text
.tide-notice
  ::first-letter -> enlarged, orange, floated
  ::first-line    -> bold, slightly spaced

.buoy::before     -> "⚓ " inserted before text
.advisory::after  -> " [STORM WATCH]" inserted after text
```

### Task 5: Mark the receding tide

Add chalk marks to a Tideglass log entry. Style `::first-letter` and `::first-line` on a notice paragraph. Use `::before` on a `.marker` to add `"» "`. Use `::after` on a `.status` to add `" — checked"`. Keep `content` present. Remember: generated content is not a substitute for real data in the HTML.
