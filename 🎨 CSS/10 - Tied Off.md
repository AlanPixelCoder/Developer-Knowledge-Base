# 10. Tied Off

**Spanish version:** [10 - Amarrado](./10%20-%20Amarrado.md)

**Course:** CSS
**Chapter:** 10 — Spacing & Box Sizing
**Topic:** Padding/margin, auto centering, box-sizing: border-box, resets
**Tags:** `#css` `#tideglass` `#box-sizing` `#centering` `#reset`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-10-7C5CFF?style=for-the-badge" alt="Chapter 10">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

At the Tideglass dock, ropes are tied off with care: too much slack and gear drifts, too little and it won't fit. Spacing in CSS is the same — padding gives breathing room inside, margin gives space between. The trick is knowing which one to pull, and controlling how width is calculated so panels don't fight each other.

## Padding and margin

`padding` adds space inside the border (between content and border). `margin` adds space outside (between elements). Both can take 1-4 values (top, right, bottom, left) or shorthand like `padding: 10px 20px;` (vertical horizontal).

```css
.log-entry {
  padding: 12px 16px;
  margin: 0 0 10px 0;
}

.dock-warning {
  margin: 16px auto;
  padding: 8px 12px;
}
```

Background covers padding but not margin. Collapsing margins can happen between vertical margins of adjacent block elements — something to watch for, not panic over.

> [!NOTE]
> **Choose deliberately**
> Want space inside the box so text doesn't touch the border? Padding. Want space between this box and the next? Margin. If you can't decide, ask "is this inside the painted boundary or between boundaries?"

## Centering with margin: auto

For a block-level element with a set `width`, `margin: 0 auto;` centers it horizontally in its container. The left and right margins take up the remaining space equally.

```css
.instrument-panel {
  width: 320px;
  margin: 0 auto; /* top/bottom 0, left/right auto */
}
```

This only works for block elements with explicit width (or constrained width). It does not center inline elements or vertically center in most simple cases.

## Box sizing: the fix for predictable layouts

With `box-sizing: content-box` (default), `width: 320px` means content width only. Padding and border add to it. With `box-sizing: border-box`, `width: 320px` means content + padding + border all fit inside 320px. That is far easier for laying out panels side by side.

```css
* {
  box-sizing: border-box;
}

.instrument-panel {
  width: 320px;
  padding: 16px;
  border: 1px solid #3a506b;
  /* total rendered width = 320px */
}
```

Applying `box-sizing: border-box` to all elements with `*` is a common, pragmatic reset that makes layouts predictable. It does not remove padding/border, it includes them in the declared width.

> [!WARNING]
> **Predictable beats clever**
> Switching to `border-box` is not "cheating". It is a deliberate choice that makes the math match what you wrote down. Many modern stylesheets do this for that exact reason.

## Why rope discipline matters

Tied off properly, lines don't cross. In CSS, if width calculation matches your intent, you can build multi-panel pages without constantly subtracting padding and borders. That is the value of `border-box`.

## Output

```text
Padding: space inside border (covered by background)
Margin:  space outside border (not covered)
margin: 0 auto: centers block with set width horizontally
content-box: width = content only (add padding+border)
border-box:   width = content + padding + border (easier)
```

### Task 10: Tie off the dock

Build a Tideglass dock panel layout. Give `.dock-panel` padding, margin, and a border. Use `margin: 0 auto` to center it. Apply `box-sizing: border-box` to all elements (`* { box-sizing: border-box; }`). Show by reasoning that with border-box, a panel of `width: 300px` with padding and border still fits in 300px. Create a second panel and see spacing between them via margin.
