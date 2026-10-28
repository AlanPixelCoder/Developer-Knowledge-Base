# 08. Salt Spray

**Spanish version:** [08 - Rocío Salino](./08%20-%20Roc%C3%ADo%20Salino.md)

**Course:** CSS
**Chapter:** 8 — Backgrounds & Shorthands
**Topic:** background-color, background-image, shorthand, border/font shorthands
**Tags:** `#css` `#tideglass` `#backgrounds` `#shorthands`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Salt spray coats the Tideglass walls: it dulls paint but leaves behind stark marks. On the instrument site, backgrounds separate panels from the page, give subtle cues without clutter, and need enough contrast for text. Shorthands let you write compact rules, but compact only works if you know what each part means.

## Background color and image

`background-color` fills the element's background. `background-image` adds an image. By default images repeat; for simple panels you usually want a solid color with enough contrast for text on top.

```css
.instrument-panel {
  background-color: #162636;
  color: #f0f6ff;
}

.chart-frame {
  background-image: url("grid-overlay.png");
  background-repeat: no-repeat;
  background-size: cover;
}
```

Keep decorative backgrounds subtle. If text becomes hard to read over an image, add a solid color behind it or increase contrast.

> [!WARNING]
> **Contrast is non-negotiable**
> Text on a busy background fails the job. If the advisory is the thing that matters in a storm, it must remain readable. Test by imagining the page in grey drizzle, not just in full sun.

## Shorthands: write less, know more

A shorthand sets multiple properties at once. The order can matter and omitted values fall back to defaults. Two common ones are `background` and `border`.

```css
/* longhand */
.panel {
  background-color: #0f1f2b;
  background-image: none;
}

/* shorthand */
.panel {
  background: #0f1f2b none;
}
```

For `border`: width, style, color.

```css
.warning-strip {
  border: 2px solid #ff6b35;
}

/* equivalent to: border-width: 2px; border-style: solid; border-color: #ff6b35; */
```

> [!CAUTION]
> **Shorthand resets defaults**
> When you use `border: 2px solid #ff6b35;` on an element that had other border properties set elsewhere, the shorthand can reset unspecified parts depending on context. If you only want to change one side, use the longhand for that side (`border-left`, etc.).

## Font shorthand

`font` is a compact way to set several font properties at once. It usually requires `font-size` and `font-family`, and can include `font-weight`, `font-style`, `line-height`, and more. Order is strict in practice.

```css
/* longhand vs shorthand */
body {
  font: 400 1rem/1.6 "Inter", system-ui, sans-serif;
}
```

This sets weight, size/line-height, and family. If omitted, unspecified values go to defaults. For clarity on a station page, longhand is often easier to read; shorthand is fine when you know exactly what you're doing.

> [!TIP]
> **Read before you compress**
> Before replacing longhand with shorthand, trace each property. A small compression that hides an unexpected reset is worse than a few extra lines.

## Putting it together

```html
<section class="instrument-panel">
  <h2>Tide Gauge</h2>
  <p class="reading">Water level: 3.42m</p>
  <div class="warning-strip">Storm surge advisory</div>
</section>
```

```css
body {
  font: 400 1rem/1.6 "Inter", system-ui, sans-serif;
  background-color: #0a1520;
  color: #f0f6ff;
}

.instrument-panel {
  background: #162636;
  border: 1px solid #3a506b;
}

.warning-strip {
  border-left: 4px solid #ff6b35;
  background-color: #2a1f0f;
}
```

## Output

```text
body:            font shorthand + dark background
.instrument-panel: solid bg + border
.warning-strip:   left accent border + tinted bg
```

### Task 8: Coat against the spray

Style a Tideglass instrument panel. Set a dark `background-color` on `body`. Give `.panel` a background with `background` shorthand or longhand (justify). Add a `border` with shorthand. Use `font` shorthand on `body` or explain why you chose longhand. Add a `.alert-strip` with a left border accent and a tinted background. Ensure text contrast remains high.
