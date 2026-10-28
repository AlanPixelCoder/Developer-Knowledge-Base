# 01. Tideglass First Light

**Spanish version:** [01 - Primer Amanecer en Tideglass](./01%20-%20Primer%20Amanecer%20en%20Tideglass.md)

**Course:** CSS
**Chapter:** 1 — Foundations
**Topic:** Cascading rules, the rule anatomy, linking stylesheets
**Tags:** `#css` `#tideglass` `#basics` `#cascade`

<p align="left">
  <img src="https://img.shields.io/badge/CSS-3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS 3">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Tideglass-1E88E5?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=1572B6&height=70&section=header" width="100%" alt="CSS blue wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #1572B6, #2DD4BF, #1572B6, transparent); margin: 24px 0;" />

Tideglass Observatory sits on a grey headland where salt eats unpainted wood. The public site needs to survive storms: high contrast, no decorative flourishes that hide warnings. HTML gave the station its structure — instrument pages, tide charts, visiting hours, a data table, a small form. CSS is what makes all of that legible when squinting into driving rain.

The job is not to decorate. The job is to keep the facts visible.

## A storm needs structure, not decoration

HTML describes what a thing is: `header`, `nav`, `main`, `section`, `table`, `form`. CSS describes how those things look. Mixing the two blurs responsibility — if a heading is hard to read, change a style, not the markup. Keeping them apart is why the station can re-skin for high-contrast mode without rewriting its tide data.

> [!NOTE]
> **Separation of concerns**
> Content belongs in HTML. Presentation belongs in CSS. Logic belongs elsewhere. Cross that line only when there is no cleaner way, and even then with caution.

## The rule as a contract

A CSS rule is a contract between a selector and declarations. The selector names targets; the declarations say what to change. No target, no effect. A broken selector is just a rule the browser never applies — silent, and easy to miss.

```css
header {
  background-color: #0f1f2b;
  color: #f0f6ff;
}

nav a {
  color: #7fc3ff;
}
```

The first rule aims at every `<header>`. The second aims at links inside `<nav>`. Each declaration ends with a semicolon. One rule can hold many declarations; one declaration changes one property.

> [!WARNING]
> **Silence is the default**
> CSS does not error on a typo. If `backgroud-color` is misspelled, the browser ignores that single declaration and moves on. When a page looks half-painted, read from the top of the file downward — the bug is often punctuation or a misspelled property above the thing that broke.

## Wiring the paint to the pages

A stylesheet must be linked to an HTML document. For a multi-page station site, an external stylesheet keeps every page consistent and easy to update.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <link href="tideglass.css" rel="stylesheet" />
  <title>Tideglass Observatory — Tide Readings</title>
</head>
<body>
  <header>Tideglass Observatory</header>
</body>
</html>
```

Keep `tideglass.css` in the same folder as the page. A relative path of `tideglass.css` is all it takes. Comments in CSS (`/* ... */`) are for humans and disappear for the browser — useful to mark storm-season overrides without deleting them.

## Why the "cascade" matters from day one

The name *Cascading Style Sheets* is not marketing. When multiple rules could apply to the same element and set the same property, the browser needs a tiebreaker. That cascade is coming in full later, but even now it is worth remembering: order, origin, and specificity all count. For a station that must be readable, predictable wins beat clever.

## Output

```text
Header background: #0f1f2b
Header text:       #f0f6ff
Nav links:         #7fc3ff
```

### Task 1: Storm-readable header

Write an external stylesheet for a Tideglass instrument page. Make the `<header>` high-contrast, give `<nav>` links a distinct color that remains readable on dark water, and add a comment marking "storm palette". Keep selectors simple and count your semicolons.

> [!TIP]
> **Test by subtraction**
> Comment out a single declaration, reload mentally, and ask what changed. That is faster than guessing — and it builds the habit of reading what the browser actually applies.
