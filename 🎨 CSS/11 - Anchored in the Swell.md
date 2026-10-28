# 11. Anchored in the Swell

**Spanish version:** [11 - Anclado en la Marejada](./11%20-%20Anclado%20en%20la%20Marejada.md)

**Course:** CSS
**Chapter:** 11 — Display & Positioning
**Topic:** block/inline/inline-block, static/relative/absolute/fixed/sticky, z-index
**Tags:** `#css` `#tideglass` `#display` `#positioning` `#z-index`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-11-7C5CFF?style=for-the-badge" alt="Chapter 11">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

In a swell, buoys drift with the flow unless anchored. Elements in CSS flow naturally unless you change how they behave or anchor them to different contexts. Understanding `display` and `position` lets you build stable layouts even when the page content shifts like the tide.

## Display: how elements sit in flow

Every element has a default `display` value. The main ones:
- `block` - takes full width available, starts on a new line (e.g. `div`, `p`, `h1`)
- `inline` - flows with text, ignores width/height (e.g. `span`, `a`)
- `inline-block` - flows like inline but accepts width/height and padding/margin (e.g. useful for buttons)
- `none` - removed from flow entirely

```css
.nav-link {
  display: inline-block;
  padding: 8px 12px;
}

.hidden-alert {
  display: none; /* not visible, not in layout */
}
```

Changing display is powerful, but be careful not to break semantics. A link should stay a link.

> [!TIP]
> **Inline vs inline-block**
> If you need to give a link vertical padding so it looks clickable on a small screen, `inline-block` or changing padding behavior matters. Justify the change by what you're trying to achieve.

## Position: anchoring in different contexts

`position` controls how an element is placed:
- `static` - default, normal flow
- `relative` - positioned relative to its normal position; offset does not remove it from flow
- `absolute` - positioned relative to the nearest positioned ancestor (anything except static); removed from flow
- `fixed` - positioned relative to the viewport; removed from flow, stays put on scroll
- `sticky` - toggles between relative and fixed depending on scroll position

```css
.status-badge {
  position: absolute;
  top: 8px;
  right: 8px;
}

.back-to-top {
  position: fixed;
  bottom: 16px;
  right: 16px;
}

.advisory-bar {
  position: sticky;
  top: 0;
}
```

> [!WARNING]
> **Absolute needs a anchor**
> If an element is `position: absolute` and none of its ancestors are positioned (relative/absolute/fixed/sticky), it will be positioned relative to the viewport or initial containing block. Always create a positioning context with `position: relative` on the parent when you want absolute positioning inside it.

## Z-index: stacking order

When elements overlap (from absolute/fixed/relative), `z-index` controls which one sits on top. Higher values win. `z-index` only works on positioned elements (not `static`).

```css
.modal-overlay {
  position: fixed;
  z-index: 1000;
}

.modal-content {
  position: relative;
  z-index: 1001;
}
```

## Building a Tideglass layout mentally

Imagine a station page: a sticky advisory bar at top, a nav that stays put, a chart with a badge positioned absolutely inside a panel (anchored by relative on the panel). The logic holds: flow for normal content, anchor for exceptions.

## Output

```text
Display: block/inline/inline-block/none
Position: static(relative default) | relative | absolute | fixed | sticky
Absolute: needs positioned ancestor for predictable anchoring
Fixed: relative to viewport
Sticky: relative then fixed
Z-index: only on positioned elements, higher wins
```

### Task 11: Anchor the swell

Build a Tideglass station layout fragment. Make a `.nav-bar` `position: sticky` at top. Create a `.gauge-panel` with `position: relative`. Put a `.alert-badge` inside with `position: absolute` anchored to the panel. Add a `.dock-status` as `position: fixed`. Use `display: inline-block` on nav links. Reason about which elements leave the flow.
