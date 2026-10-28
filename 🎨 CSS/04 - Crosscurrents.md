# 04. Crosscurrents

**Spanish version:** [04 - Contracorrientes](./04%20-%20Contracorrientes.md)

**Course:** CSS
**Chapter:** 4 — Selectors II
**Topic:** Grouping, child combinator, chaining
**Tags:** `#css` `#tideglass` `#selectors` `#combinators`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

At the narrows of Tideglass Bay, currents cross and push in different directions. A careless boat gets caught in both. A careful one picks a channel. Selectors have their own currents: grouping shares rules, combinators follow relationships in the markup, and chaining demands elements satisfy all parts at once.

## Sharing the load with grouping

When several different selectors need exactly the same declarations, grouping saves lines and cuts mistakes. Separate selectors with a comma.

```css
h1,
h2,
.instrument-title {
  color: #f0f6ff;
  font-family: "Inter", system-ui, sans-serif;
}
```

The comma means "or". There is no relationship required — just shared styles. If one selector is invalid, the whole grouped rule can misbehave in some older cases, but in practice keep groups small and clear.

## Following the tide with combinators

Sometimes you only want to style elements that sit in a specific place in the HTML tree. The child combinator (`>`) only matches direct children. That precision matters on instrument pages where nested lists appear.

```css
.tide-panel > h2 {
  margin-top: 0;
  border-bottom: 1px solid #3a506b;
}
```

Only an `h2` that is a direct child of `.tide-panel` gets that treatment. An `h2` deeper inside a subpanel is not affected. This avoids unintended styling of reused components.

> [!TIP]
> **Be explicit when depth matters**
> If a style is meant for "the heading of this panel", use `>`. If it truly means "any heading inside this panel", descendent selectors exist, but reach for precision first to keep surprises down.

## Chaining for a narrow catch

Chaining means putting selectors together with no space: `p.warning` means "a paragraph that also has class warning". Both conditions must hold. That is different from a descendent.

```css
p.warning {
  background-color: #2a1f0f;
  border-left: 3px solid #ff6b35;
  padding: 0.5rem 0.75rem;
}
```

A `div.warning` would not match. A `p` without `warning` would not match. Chaining is perfect for variants that only make sense on certain elements.

> [!WARNING]
> **No space changes everything**
> `.panel .warning` (space) means "a warning inside a panel". `.panel.warning` (no space) means "a panel that is also a warning". Read left to right, but watch for the space — it is the difference between relationship and combined conditions.

## Reading the crosscurrent

Put together on a station data card:

```html
<section class="tide-panel">
  <h2>Boathouse Readings</h2>
  <ul class="reading-list">
    <li>Water temp: 12°C</li>
    <li class="warning">Salinity drop: check intake</li>
  </ul>
  <p class="warning">General advisory: secure loose gear</p>
</section>
```

```css
h1, h2, .instrument-title { color: #f0f6ff; }
.tide-panel > h2 { margin-top: 0; }
p.warning { border-left: 3px solid #ff6b35; }
```

The panel's direct `h2` gets the rule. The `li.warning` is not a `p`, so `p.warning` does not style it. The `p.warning` does get styled. Small details, big difference when the page grows.

## Output

```text
Crosscurrent map:
  h1, h2, .title        -> grouped (or)
  .panel > h2           -> direct child only
  p.warning             -> element AND class
  .panel .warning       -> warning inside panel
  .panel.warning        -> panel element that has warning class
```

### Task 4: Navigate the narrows

Style a Tideglass visit board. Group `h1` and `h2` for a shared color. Use `>` to style only the direct `h3` of `.visit-panel`. Chain `p.notice` for a notice paragraph style that does not affect `li.notice`. Make sure you can say why each rule hits or misses given sample markup. Change one comma to test grouping.
