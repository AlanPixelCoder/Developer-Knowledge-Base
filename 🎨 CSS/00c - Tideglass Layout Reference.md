# 00c. Tideglass Layout Reference

**Spanish version:** [00c - Referencia de Maquetación de Tideglass](./00c%20-%20Referencia%20de%20Maquetaci%C3%B3n%20de%20Tideglass.md)

**Course:** CSS
**Chapter:** Reference
**Topic:** Box model, spacing, display, positioning, z-index, flexbox
**Tags:** `#css` `#tideglass` `#cheatsheet` `#layout` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-F7DF1E?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Covers-Chapters_07_--_12-7C5CFF?style=for-the-badge" alt="Chapters 07 to 12">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Compact reference for the second half of Tideglass. Covers the box model, spacing, display, positioning, stacking, and flexbox. For syntax and selectors, see [[00b - Tideglass Quick Reference]].

> [!TIP]
> When layout breaks, trace the layers: content -> padding -> border -> margin.

## Box model

From inside out: **content | padding | border | margin**  
Background covers **content + padding** only.

| Box sizing | Effect |
| :--- | :--- |
| `content-box` (default) | `width` = content only; padding/border add |
| `border-box` | `width` = content + padding + border |

## Display

| Value | Behavior |
| :--- | :--- |
| `block` | New line, full width |
| `inline` | Flows with text, no width/height |
| `inline-block` | Flows inline, accepts width/height/padding/margin |
| `none` | Removed from flow |

## Position

| Value | Context |
| :--- | :--- |
| `static` | Normal flow |
| `relative` | Relative to normal position; stays in flow |
| `absolute` | Relative to positioned ancestor; removed from flow |
| `fixed` | Relative to viewport; removed from flow |
| `sticky` | Relative then fixed on scroll |

## Flexbox

| Property | Use |
| :--- | :--- |
| `display: flex` | Create container |
| `justify-content` | Main axis alignment |
| `align-items` | Cross axis alignment |
| `flex-direction` | Axis direction |
| `flex: 1` | Grow to fill |
| `gap` | Space between items |
