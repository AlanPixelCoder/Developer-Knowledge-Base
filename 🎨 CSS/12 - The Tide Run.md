# 12. The Tide Run

**Spanish version:** [12 - La Carrera de la Marea](./12%20-%20La%20Carrera%20de%20la%20Marea.md)

**Course:** CSS
**Chapter:** 12 — Flexbox
**Topic:** Flex container/items, axes, justify-content, align-items, flex properties
**Tags:** `#css` `#tideglass` `#flexbox` `#layout`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3-+?style=for-the-badge&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-ADVANCED-FF5252?style=for-the-badge" alt="Advanced">
  <img src="https://img.shields.io/badge/Chapter-12-7C5CFF?style=for-the-badge" alt="Chapter 12">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

When the tide turns, boats race between the buoys to reach the safe channel. They need to spread out, align, and adjust to the space available. Flexbox is the same idea: a flex container distributes its items along axes, giving them room to grow, shrink, or align without wrestling with floats or complex positioning.

## The container and items

Make a container a flexbox with `display: flex;`. Direct children become flex items. The main axis is horizontal by default (`flex-direction: row`), cross axis is vertical.

```css
.reading-row {
  display: flex;
  gap: 12px;
}

.reading-row .item {
  /* flex item */
}
```

## Aligning along axes

`justify-content` aligns items along the main axis. `align-items` aligns along the cross axis. `gap` adds space between items.

```css
.nav-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}
```

Common values: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`.

> [!NOTE]
> **Axes matter**
> If `flex-direction` becomes `column`, the main axis is vertical and `justify-content` works vertically while `align-items` works horizontally. Always know which axis is which before aligning.

## Controlling growth with flex

Flex items can grow or shrink. `flex: 1` makes an item take up remaining space equally. `flex-grow`, `flex-shrink`, `flex-basis` give finer control.

```css
.panel {
  display: flex;
}

.main {
  flex: 1; /* grow to fill space */
}

.sidebar {
  flex: 0 0 200px; /* don't grow, don't shrink, fixed basis */
}
```

> [!WARNING]
> **Don't fight the axis**
> If you want to center something vertically and horizontally with flexbox, use both axes: `justify-content: center; align-items: center;` on the container. Trying to do it with margins alone is often unnecessary when flex is available.

## Building the Tideglass instrument row

```html
<div class="instrument-row">
  <div class="gauge">Tide: 3.42m</div>
  <div class="gauge">Temp: 12°C</div>
  <div class="gauge">Wind: 18 kn</div>
</div>
```

```css
.instrument-row {
  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 8px;
}

.gauge {
  flex: 1;
  text-align: center;
  padding: 12px;
  border: 1px solid #3a506b;
  background-color: #162636;
}
```

Each gauge takes equal space. The row adapts to width — far easier than percentage tricks with floats.

## Output

```text
Container: display: flex
Axes: main (row default), cross
justify-content: main axis
align-items: cross axis
flex: grow/shrink/basis
gap: space between items
```

### Task 12: Run the tide

Build a Tideglass navigation bar with flexbox. Use `justify-content: space-between` and `align-items: center`. Create a card row where cards grow equally with `flex: 1`. Center a single card vertically and horizontally inside a panel using flexbox. Reason about axes if you change `flex-direction: column`.
