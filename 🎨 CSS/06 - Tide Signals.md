# 06. Tide Signals

**Spanish version:** [06 - Señales de Marea](./06%20-%20Se%C3%B1ales%20de%20Marea.md)

**Course:** CSS
**Chapter:** 6 — Pseudo-classes
**Topic:** :hover, :active, :focus, :visited, :nth-child(), :not(), LoVe/HAte
**Tags:** `#css` `#tideglass` `#pseudo-classes` `#states`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

The tide signal tower blinks different lights for different states: a buoy shows one pattern at rest, another when approached by a boat, another when being serviced. Links and interactive elements need the same clarity. Pseudo-classes let you style elements based on state or position, not just by type or class.

## States the user can trigger

`:hover` applies when the pointer is over an element. `:active` applies while the element is being activated (mouse down, for example). `:focus` applies when the element is focused via keyboard or programmatically — critical for accessibility. `:visited` styles links the user has already followed.

```css
nav a:link {
  color: #7fc3ff;
}

nav a:visited {
  color: #b39ddb;
}

nav a:hover {
  color: #ffffff;
  text-decoration: underline;
}

nav a:focus {
  outline: 2px solid #7fc3ff;
  outline-offset: 2px;
}

nav a:active {
  color: #ff6b35;
}
```

> [!CAUTION]
> **Do not remove focus outlines blindly**
> Removing `outline` without replacing it with a visible focus indicator makes keyboard navigation nearly impossible. For a public station site, focus styles are a requirement, not decoration.

## Order matters: LoVe/HAte

For link states, browsers expect a specific order to avoid conflicts. A common mnemonic is LoVe/HAte: `:link` — `:visited` — `:hover` — `:active`. If `:hover` comes before `:visited`, `:visited` might override it depending on specificity; following the order keeps behavior predictable.

## Selecting by position

`:nth-child()` selects elements based on their position among siblings. It can take numbers, keywords (`odd`, `even`), or formulas (`2n+1`). On a Tideglass tide table, striping rows improves readability in rough light.

```css
.tide-table tr:nth-child(even) {
  background-color: #0f1f2b;
}

.tide-table tr:nth-child(odd) {
  background-color: #162636;
}
```

`:not()` negates a selector — useful to style everything except a specific case.

```css
.reading-list li:not(.offline) {
  color: #dbe9f5;
}
```

> [!TIP]
> **Count siblings, not children of different types**
> `:nth-child()` counts all siblings regardless of tag. If you need to count only certain elements, there are other pseudo-classes, but for simple striping `:nth-child()` is usually what you want. Reason about which elements share the same parent.

## Reading signals

```html
<nav>
  <a href="#charts">Charts</a>
  <a href="#advisories">Advisories</a>
</nav>
<table class="tide-table">
  <tr><td>05:23</td><td>High</td></tr>
  <tr><td>11:47</td><td>Low</td></tr>
  <tr><td>17:12</td><td>High</td></tr>
</table>
```

Links change on hover/focus/active. The table rows alternate. Items not marked `offline` get the base color.

## Output

```text
Link states: link -> visited -> hover -> focus -> active
Table striping: even/odd rows alternate
:not(.offline): all list items except those with class offline
```

### Task 6: Signal the channel

Style a Tideglass navigation list. Apply states in LoVe/HAte order. Add visible `:focus` styles (do not remove outline without replacement). Stripe a `.log-list` with `:nth-child(even/odd)`. Use `:not()` to gray out only `.archived` entries while keeping others readable. Test mentally: what happens if focus order matters?
