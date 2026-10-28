# 02. Chalk on the Pier

**Spanish version:** [02 - Tiza en el Muelle](./02%20-%20Tiza%20en%20el%20Muelle.md)

**Course:** CSS
**Chapter:** 2 — Color & Measure
**Topic:** Named colors, rgb/hex, absolute vs relative units
**Tags:** `#css` `#tideglass` `#colors` `#units`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

At low tide the pier planks are slick with salt. Volunteers mark tide limits in chalk — quick, visible, and easy to erase when the water comes back. The Tideglass site does something similar: colors mark meaning (warnings, safe, offline), and sizes must hold up when viewed on a phone in a pocket or a chart terminal in the boathouse.

## Color with a job to do

A color is only useful if it means something. On Tideglass, storm warnings need to stand out without blinding the user, and data labels need enough contrast to read at a glance. CSS gives three common ways to write the same hue: named colors, `rgb()`, and hex.

```css
.warning {
  color: crimson;        /* named */
}

.tide-high {
  color: rgb(255, 107, 53); /* red, green, blue */
}

.offline {
  color: #7c8c92;        /* hex rrggbb */
}
```

`rgb()` takes three numbers 0-255. Hex pairs run `00`-`ff`. Shorthand `#f00` equals `#ff0000`. All three describe light; pick the one your team agrees on and be consistent.

> [!CAUTION]
> **Meaning beats aesthetics**
> "Pretty" is not a requirement for a warning label. If the text of a storm alert fails to stand out from its background, it is broken regardless of which palette looks nicer. When in doubt, lean towards higher contrast for text.

## Measuring for real surfaces

Pixels are tempting — fixed, precise. But a chart label that looks right on a wide monitor becomes cramped on a narrow screen. Units decide what flexes and what stays put. Split them into absolute and relative.

| Unit | Type | Behavior | When to use |
| :--- | :--- | :--- | :--- |
| `px` | absolute | Stays exactly that size | Borders, shadows, details that should not scale wildly |
| `pt`, `cm` | absolute | Physical units; rarely used on screens | Print styles only |
| `%` | relative | Relative to the parent element's size | Widths that should grow/shrink with a container |
| `em` | relative | Relative to the element's font size (can stack) | Local scaling inside a component |
| `rem` | relative | Relative to the root (`html`) font size | Consistent type scales across the whole page |

## Why stacking hurts

`em` compounds. If a container sets `font-size: 1.2em` and its child sets `font-size: 1.2em`, the child becomes 1.44 times the original base — easy to lose track of. `rem` anchors to `<html>`, so `1.5rem` is always 1.5 times the root regardless of nesting. For most text scales, `rem` is the one that stays honest.

```css
html {
  font-size: 16px; /* base */
}

.data-label {
  font-size: 1.25rem; /* 20px */
}

.nested .data-label {
  font-size: 1.25rem; /* still 20px */
}
```

> [!TIP]
> **Anchor to root**
> Set a sensible base on `html` if needed, and use `rem` for type. Reach for `em` only when you intentionally want local, compounding scaling (rare on a data-heavy page).

## Reading without guessing

Width is the most common place to see units in action. A percentage width fills part of its container; a pixel width ignores the container's available space. Neither is "better" — each tells the layout what to do.

```css
.instrument-panel {
  width: 80%; /* flexes with parent */
}

.gauge-divider {
  width: 1px;  /* fixed rule */
}
```

## Output

```text
warning:      crimson
tide-high:    rgb(255, 107, 53)
offline:      #7c8c92
data-label:   1.25rem (20px if root is 16px)
panel width:  80% of parent
divider:      1px fixed
```

### Task 2: Chalk marks for the readings

Build a tiny Tideglass readings list. Style three statuses (safe, rising, storm) with three different color notations. Give labels a `rem` size anchored conceptually to a 16px root. Give a panel `width: 90%` and a thin divider `width: 1px`. Do not guess — say which are absolute/relative in your head as you write.
