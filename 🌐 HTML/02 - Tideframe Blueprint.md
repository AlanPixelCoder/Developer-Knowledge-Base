# 02. Tideframe Blueprint

**Spanish version:** [02 - Plano de Mareas](./02%20-%20Plano%20de%20Mareas.md)

**Course:** HTML
**Topic:** Tideglass page skeleton, tide tree, comments, attributes, class/id, divs, inline and block styles
**Tags:** `#html` `#web-development` `#structure` `#attributes` `#tideglass`

<p align="left">
  <img src="https://img.shields.io/badge/HTML-5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML 5">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Module-HTML-7C5CFF?style=for-the-badge" alt="HTML Module">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Tideglass-00B4D8?style=for-the-badge" alt="Tideglass">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00B4D8&height=70&section=header" width="100%" alt="Tideglass wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00B4D8, #90E0EF, #00B4D8, transparent); margin: 24px 0;" />

A rough log on a single page works for a morning note, but the observatory needs a standard blueprint for every public page. The tideframe is that blueprint: a document skeleton, a way to label parts of it for future styling, and a method of leaving notes without printing them to the water-stained board. Everything added here is in service of one goal — making pages findable by other code later.

> [!NOTE]
> **Labels are handles**
> `class` and `id` are not decorations. They are handles that CSS, JavaScript, and accessibility tools grab to act on specific elements. An unlabeled element is an element nothing can reliably target.

## The Tideframe Skeleton

Every published observatory page starts the same way. `<!DOCTYPE html>` tells the browser it's HTML5. `<html>` wraps the whole document. Inside it, `<head>` holds metadata the visitor does not see (like the tab title), and `<body>` holds everything visible on the glass pier board.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Tideglass Observatory — Station Status</title>
  </head>
  <body>
    <h1>Station Status</h1>
    <p>All buoys reporting nominal readings.</p>
  </body>
</html>
```

The `<title>` is the first thing a tidewatcher sees in a browser tab. If it's missing, the tab shows a file path — unhelpful when multiple station pages are open. Keep it short and specific to the page, not to the whole archive.

> [!WARNING]
> `<head>` is not the same as `<header>`. `<head>` is metadata; `<header>` is visible content. Mixing those up is one of the most common blueprint mistakes and it has real consequences for assistive tech.

## The Tide Tree

HTML elements form a tree. A parent can hold children, children can hold grandchildren, and siblings share the same parent. Understanding this tree is essential when writing nested lists or grouping instrument cards.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Tideglass Crew</title>
  </head>
  <body>
    <h1>Watch Rotation</h1>
    <p>Night shift crew for <i>Cycle 7</i>.</p>
  </body>
</html>
```

In the structure above, `<html>` is parent to `<head>` and `<body>`. `<head>` is parent to `<title>`. `<body>` is parent to `<h1>` and `<p>`. `<i>` is child of `<p>`. `<h1>` and `<p>` are siblings. This nesting is exactly what styles and DOM traversal follow.

### Nested duty rosters

A duty roster often nests responsibilities under a role. A list inside a list mirrors that hierarchy naturally.

```html
<ul>
  <li>Tidewatcher — Mora
    <ul>
      <li>Gauge readings</li>
      <li>Slack tide timing</li>
    </ul>
  </li>
  <li>Radio Operator — Finch
    <ul>
      <li>Coastwatch liaison</li>
      <li>Storm channel monitoring</li>
    </ul>
  </li>
</ul>
```

> [!TIP]
> If you can sketch the parent/child lines on paper and they match what you wrote, indentation is correct. If the tree makes sense, CSS selectors will be easier to write later.

## Comments and Intent

Tidewatchers leave field notes for each other. In HTML, `<!-- ... -->` comments do the same — ignored by the browser, visible to anyone reading the source. The rule: explain *why*, not *what*. The tags already say what they are.

```html
<!-- Restrict this panel to staff until the south jetty reopens. -->
<div class="restricted-panel">
  <p>Jetty access code: TIDE-772</p>
</div>
```

Comments can be multi-line and can temporarily hide broken markup while debugging.

```html
<!-- 
  Temporary block for testing layout.
  <p>Old copy retained for comparison.</p>
-->
```

> [!NOTE]
> Over-commenting clutters the source. A good comment answers a question a future tidewatcher would actually ask: "Why is this hidden?" or "This depends on the 03:00 slack reading."

## Attributes, Classes and IDs

Attributes configure elements. They live in the opening tag as `name="value"`. Some change behavior (like `href` on links or `src` on images), others label for reuse and targeting.

Classes group elements for shared treatment: any number of elements can share the same class. IDs identify a single element uniquely on the page: each ID should appear only once, and it cannot contain spaces.

```html
<h2 class="panel-title">Gauge Status</h2>
<p id="gauge-reading">+2.4 m and rising slowly</p>
<p class="panel-title">Buoy Status</p>
```

An ID can also link to a section of the same page. The anchor's `href` uses `#` followed by the ID.

```html
<a href="#restricted-zone">Jump to restricted zone notice</a>
<h2 id="restricted-zone">Restricted Zone</h2>
<p>South jetty closed until further notice.</p>
```

> [!IMPORTANT]
> A single element can have both a class and an ID: `class="instrument-card"` and `id="north-gauge"`. The ID gives it a unique anchor and a precise target; the class puts it in a group that shares styling rules.

## The Generic Container: `<div>`

`<div>` is a generic block container with no semantic meaning. It exists purely to group elements for layout and styling. Used well, it creates cards and panels. Used as a substitute for everything, it creates impenetrable "div soup".

```html
<div class="instrument-card">
  <h3>North Gauge</h3>
  <p>Height: +2.4 m</p>
  <p>Trend: Rising</p>
</div>

<div class="instrument-card">
  <h3>South Gauge</h3>
  <p>Height: +1.8 m</p>
  <p>Trend: Falling</p>
</div>
```

## Styling in Place

For quick experiments, the `style` attribute applies CSS directly to a single element. For consistent styling across many elements, `<style>` in `<head>` uses selectors: element names, `.class`, and `#id`.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Tideglass Palette Test</title>
    <style>
      .instrument-card {
        border: 1px solid #00B4D8;
        padding: 8px;
        margin: 6px;
        width: 260px;
      }
      #north-gauge {
        background-color: #E0FBFC;
      }
    </style>
  </head>
  <body>
    <div class="instrument-card" id="north-gauge">
      <h3>North Gauge</h3>
      <p>+2.4 m — Rising</p>
    </div>
    <div class="instrument-card">
      <h3>South Gauge</h3>
      <p>+1.8 m — Falling</p>
    </div>
  </body>
</html>
```

> [!CAUTION]
> Inline styles (`style="..."`) override most other styles, which makes them hard to change globally. Treat them as a last resort for one-off checks, not a default. The goal is to keep structure in HTML and presentation in CSS.

## Output

The tideframe blueprint produces a consistent skeleton: doctype, html, head with title, body with labeled containers. The tree is predictable, classes group cards, IDs mark anchors, and comments record intent. Even with minimal styling, the page reads as a station board rather than a random pile of paragraphs.

## Task 2: Build the Instrument Bay

Create `instrument-bay.html` with a complete HTML5 skeleton. Add a title in `<head>`. In `<body>`, build a header section labeled with classes/IDs, a "Gauge Bank" made of at least two `<div class="instrument-card">` elements each with a heading and two paragraphs, a nested duty roster using lists, a comment explaining why one card is marked restricted, and in-page anchors using IDs. Optionally add a small `<style>` block in `<head>` to visually distinguish cards.

**Why this order:** labels and structure are the scaffolding — once the tree is sound, adding more sections never requires untangling a pile of unlabeled `<div>`s.

**Next:** [[03 - Harbor Intake Forms]]
