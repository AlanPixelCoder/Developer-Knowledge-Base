# 04. Slipway Semantics

**Spanish version:** [04 - Semántica del Astillero](./04%20-%20Sem%C3%A1ntica%20del%20Astillero.md)

**Course:** HTML
**Topic:** Semantic HTML for Tideglass — header/main/footer, article/section/aside, nav, figure/figcaption, time, accessible links, entities
**Tags:** `#html` `#web-development` `#semantics` `#accessibility` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Module-HTML-7C5CFF?style=for-the-badge" alt="HTML Module">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Tideglass wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

A page built entirely from `<div>`s renders fine, but it tells the browser nothing. A page built from semantic elements tells a story: where the station banner is, where the unique report lives, where the notes and links belong. For the Tideglass public slipway, that story matters — screen readers, search engines, and future maintainers all need the landmarks.

> [!NOTE]
> **A promise of meaning**
> Semantic HTML is a promise: this element means what its name says. The visual change is often minimal. The functional change — navigation, comprehension, maintainability — is the reason to use them.

## Landmarks: Header, Main, Footer

Most station pages follow the same three regions. HTML gives each one a purpose-built element.

- `<header>` — banner area: station name, logo, or top navigation. Can appear at page level or inside an article/section.
- `<main>` — the unique, central content of the page. There should be only one per page.
- `<footer>` — closing area: copyright, contact, license notes. Can appear at page level or inside an article/section.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Tideglass Observatory</title>
  </head>
  <body>
    <header>
      <h1>Tideglass Observatory — Greyharbor</h1>
      <p>Coastal observations since the first glass pier.</p>
    </header>
    <main>
      <p>Today's slipway status: open for staff only until 17:00.</p>
    </main>
    <footer>
      <p>© 2026 Tideglass Observatory. Readings provided for public awareness.</p>
    </footer>
  </body>
</html>
```

> [!IMPORTANT]
> `<header>`/`<footer>` are not the same as `<head>`/`<body>`. They live inside `<body>`, render visibly, and serve content roles. A footer inside an article holds the byline and date for that article, not necessarily the whole site's legal text.

## Articles, Sections, and Asides

Not all content is equal. Some pieces stand on their own; some only make sense in context; some are tangential.

- `<article>` — self-contained content that would make sense if pulled out and read alone (a station bulletin, a buoy report, a repair log entry).
- `<section>` — related content grouped together that needs the surrounding page for context (a collection of balance notes grouped under one heading).
- `<aside>` — tangentially related content (related reports, glossary, quick links).

```html
<main>
  <article>
    <h2>Buoy NB-01: Cable Tension Report</h2>
    <p>Minor tension creep observed after the last swell. Monitoring continues.</p>
    <footer>
      <p>Logged by Mora on <time datetime="2026-10-27">October 27, 2026</time></p>
    </footer>
    <aside>
      <h3>Related</h3>
      <ul>
        <li><a href="#nb-history">NB-01 maintenance history</a></li>
        <li><a href="#swell-data">Recent swell data</a></li>
      </ul>
    </aside>
  </article>

  <section>
    <h2>Slipway Notes</h2>
    <p>The north slipway gate requires manual release during heavy surge.</p>
  </section>
</main>
```

> [!TIP]
> Ask: "If I copied this to a different page, would it still make sense?" If yes, consider `<article>`. If no, it's probably `<section>`. That single question resolves most ambiguity.

## Navigation

Major navigation links belong in `<nav>`. A site menu, a table of contents, or pagination are all reasonable uses. A random cluster of links in a footer doesn't necessarily need a `<nav>` wrapper — use judgment.

```html
<header>
  <h1>Tideglass Observatory</h1>
  <nav>
    <ul>
      <li><a href="#readings">Readings</a></li>
      <li><a href="#buoys">Buoys</a></li>
      <li><a href="#slipway">Slipway</a></li>
      <li><a href="#intake">Intake</a></li>
    </ul>
  </nav>
</header>
```

Multiple `<nav>` elements are fine — main menu, article TOC, pagination — each is a distinct navigational region.

## Figures, Captions, and Dates

`<figure>` pairs self-contained content (an image, diagram, or code snippet) with an optional caption in `<figcaption>`. The figure is the unit, not just the image.

```html
<figure>
  <img src="https://placehold.co/320x200" alt="The glass pier at low tide, showing the gauge platform">
  <figcaption>Figure 1: Gauge platform exposed at lowest tide of Cycle 7.</figcaption>
</figure>
```

For dates and times, `<time>` with `datetime` gives a machine-readable form while keeping human-readable text inside.

```html
<p>Storm advisory issued <time datetime="2026-10-27T09:00:00Z">October 27, 2026 at 09:00 UTC</time>.</p>
```

## Accessible Links and Entities

Link text must describe the destination. "Click here" tells nothing to a screen reader. Prefer specific labels.

```html
<!-- Bad -->
<a href="/buoys/nb-01">Click here</a>

<!-- Good -->
<a href="/buoys/nb-01">NB-01 buoy maintenance report</a>
```

HTML uses entities for characters that would otherwise be interpreted as markup or that are hard to type. Escape `&`, `<`, `>`, `"`, and `'` when they appear as text.

| Character | Entity | Use |
| :--- | :--- | :--- |
| `&` | `&amp;` | Ampersands in text |
| `<` | `&lt;` | Less-than as text |
| `>` | `&gt;` | Greater-than as text |
| `"` | `&quot;` | Quotes inside quoted attributes |
| `'` | `&apos;` | Apostrophes in some contexts |

```html
<p>Tide &amp; Surge charts show readings &lt; 0.5 m only during extreme low slack.</p>
<p>The sign reads "Restricted to <b>&quot;Staff Only&quot;</b>".</p>
```

> [!WARNING]
> Writing `Rope & Buoy` raw will be misread by the parser in places — always escape `&` as `&amp;` in text. Inside attribute values that contain quotes, use `&quot;` or single quotes around the attribute.

## Output

A semantically correct slipway page has clear landmarks (`header`, `main`, `footer`), purposeful grouping (`article`, `section`, `aside`), proper navigation (`nav`), captioned figures, meaningful dates (`time`), descriptive links, and escaped special characters. The structure is navigable by keyboard and screen reader, and maintainable by anyone reading the source.

## Task 4: Publish the Slipway Bulletin

Create `slipway-bulletin.html`. Build a complete page with: `<header>` containing an `<h1>` and a `<nav>` with at least three links to in-page IDs, `<main>` with exactly one `<article>` (self-contained bulletin) that has an `<h2>`, a `<figure>` with `<img>` and `<figcaption>`, a paragraph with a `<time datetime>` inside, an `<aside>` with related links, and a `<footer>` with author and date inside the article or at page level as appropriate; a `<section>` for "Slipway Restrictions" with a heading and a list; and use at least one HTML entity in the text. Ensure all images have `alt` text and all links have descriptive text.

**Why this order:** semantics are the capstone — they tie together structure, labeling, and accessibility so the public page is usable by everyone, not just sighted mouse users.

**Next:** Complete the module by updating READMEs. No more new lessons.
