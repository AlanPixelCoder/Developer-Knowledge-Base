# 09. The Tideframe

**Spanish version:** [09 - El Marco de Mareas](./09%20-%20El%20Marco%20de%20Mareas.md)

**Course:** CSS
**Chapter:** 9 — Box Model & Borders
**Topic:** Content, padding, border, margin; box inspection
**Tags:** `#css` `#tideglass` `#box-model` `#borders`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-9-7C5CFF?style=for-the-badge" alt="Chapter 9">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Every Tideglass instrument gets a sealed frame to keep moisture out. The frame has layers: the glass and readout (content), a gasket (padding), the metal housing (border), and the gap to the next unit on the rack (margin). CSS boxes work exactly like that. If you do not see the layers, you cannot fix spacing bugs.

## The four layers

From inside out:
1. **Content** - the actual text/image, sized by `width`/`height` by default
2. **Padding** - space between content and border, inside the element
3. **Border** - the edge around padding
4. **Margin** - space outside the border, between elements

```css
.data-frame {
  width: 280px;
  padding: 16px;
  border: 2px solid #3a506b;
  margin: 12px;
}
```

Background color fills content and padding, but not margin. The border sits between padding and margin.

> [!NOTE]
> **Backgrounds stop at the edge**
> `background-color` covers padding. It does not cover the transparent margin area. That is by design — margin is spacing between elements, not part of the element's painted surface.

## Borders in detail

Borders need at least a style to show. `border-width`, `border-style`, `border-color` can be set per side or with shorthand.

```css
.advisory-frame {
  border-top: 3px solid #ff6b35;
  border-right: 1px solid #3a506b;
  border-bottom: 1px solid #3a506b;
  border-left: 1px solid #3a506b;
}
```

Rounded corners come from `border-radius`. Even small rounding can soften harsh edges on a stormy page.

```css
.gauge {
  border-radius: 6px;
}
```

## Inspecting to be sure

You cannot guess box sizes by eye. Reasoning helps, but the actual rendered size depends on how you treat width. Still, the concept is the same: see the box diagram mentally. For content-box (default), `width` is content only; padding and border add to the total width.

```css
/* content-box default */
.box {
  width: 200px;
  padding: 20px;
  border: 5px solid #3a506b;
  /* total width roughly 200 + 40 + 10 = 250px */
}
```

> [!WARNING]
> **Default box model adds up**
> With `box-sizing: content-box` (default), adding padding and border increases the element's rendered width beyond `width`. That catches people off guard when laying out panels side by side. We'll fix this deliberately in the next lesson.

## Why this matters

Spacing bugs are the most common in CSS. If two panels don't sit where expected, the answer is almost always in padding, border, or margin. Learning to read the layers turns mystery into calculation.

## Output

```text
Layers (inside out): content | padding | border | margin
Background: covers content + padding only
Total width (content-box): width + padding*2 + border*2
```

### Task 9: Frame the tide gauge

Build a Tideglass gauge frame. Set `width`, `padding`, `border`, `margin` on `.gauge`. Style different borders per side. Add `border-radius`. Calculate by reasoning the total width if using content-box (default). Do not guess — write the calculation. Make sure the background color shows on content+padding but not across the margin gap.
