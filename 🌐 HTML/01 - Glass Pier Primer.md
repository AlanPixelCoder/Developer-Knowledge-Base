# 01. Glass Pier Primer

**Spanish version:** [01 - Cimiento del Muelle de Cristal](./01%20-%20Cimiento%20del%20Muelle%20de%20Cristal.md)

**Course:** HTML
**Topic:** Tideglass Observatory foundations — marking pier readings, tides and buoys
**Tags:** `#html` `#web-development` `#basics` `#tideglass`

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

The Tideglass Observatory sits at the very edge of Greyharbor, built over a glass pier so the tidewatchers can read the water below without ever stepping onto the slick stones. Before the tide board or the weather instruments go online, the staff need a public page to publish today's readings. HTML is the language that gives that page its bones — not its paint, not its logic, just its labels.

> [!NOTE]
> **Structure before style**
> HTML does not draw or animate. It marks content: this is a heading for the tide gauge, this is a list of buoys, this is a link to the hourly forecast. CSS and JavaScript come later; if the labels are wrong, nothing downstream can fix them cleanly.

## Reading the Pier

A tidewatcher never writes a full report at once. They log one observation per line: the gauge height, the wind, the visibility. HTML mirrors that habit with **elements**. An element pairs an opening tag, content, and a closing tag to say what a piece of text is.

```html
<p>The glass pier reads +2.4 m at high slack.</p>
```

The `<p>` element tells the browser this is a paragraph. Headings tell the outline of the report, not how big the text should look. Tideglass keeps exactly one `<h1>` per page, because that heading is the title of the whole station log for the day.

```html
<h1>Tideglass Observatory — Greyharbor</h1>
<h2>Morning Gauge Readings</h2>
<h3>North Buoy Cluster</h3>
```

> [!WARNING]
> **Outline over decoration**
> Using six `<h1>` tags does not make six titles — it breaks the outline that screen readers rely on to navigate. Pick one `<h1>`, and step down one level at a time as the report gets more specific.

## Marking Tide Notes

Tide notes are short, but sometimes a single line needs a break. Pressing enter inside HTML is collapsed into a space, so the pier uses `<br>` to force a new line without starting a new paragraph.

```html
<p>Storm surge advisory remains in effect.<br>Check the south jetty at the next low slack.</p>
```

Not every word carries equal weight on the tide board. For emphasis in a rough log, `<b>`, `<i>`, `<u>` and `<s>` do the job. They are learning tools, not a styling system — real presentation belongs to CSS, but in a plain text log they still mark intent clearly.

```html
<p>The <b>south jetty</b> is <i>partly submerged</i>; <u>restricted to staff only</u>. The old marker is <s>still marked open</s>.</p>
```

> [!TIP]
> If you find yourself reaching for bold on every third word, the fix is usually a better heading or a list, not more formatting tags. Structure carries more emphasis than decoration ever will.

## Buoy Inventory

When the observatory lists its equipment, order rarely matters — a buoy is a buoy. An unordered list with `<ul>` and `<li>` keeps them visible as a set.

```html
<h2>Active Buoys</h2>
<ul>
  <li>NB-01 — North Channel</li>
  <li>SB-02 — South Approach</li>
  <li>GB-03 — Greyharbor Entrance</li>
</ul>
```

When the tidewatchers need to follow a sequence, like a pre-storm checklist, an ordered list with `<ol>` makes the steps unambiguous.

```html
<h2>Pre-Storm Checklist</h2>
<ol>
  <li>Secure loose mooring lines at the glass pier.</li>
  <li>Log the current gauge height and barometric trend.</li>
  <li>Raise the restricted zone flag on the south jetty.</li>
  <li>Confirm the radio watch shift is active.</li>
</ol>
```

## Linking the Tide Board

No observatory stands alone. The public page needs links to the hourly forecast and images of the instruments. The `<a>` tag points elsewhere with `href`, and the text inside should say where it goes, not beg to be clicked.

```html
<a href="https://example.org/greyharbor/forecast">Greyharbor hourly tide forecast</a>
```

For instruments, `<img>` shows them. Every image must carry `alt` text — if the glass pier connection drops and the image fails to load, or if a reader uses a screen reader, that text is what remains.

```html
<img src="https://placehold.co/320x200" alt="The Tideglass Observatory glass pier at low tide, showing the gauge housing">
```

## Output

A minimal pier page renders as a readable station log: one title, a readings heading, a short note, a buoy list, and a link to the forecast. In the browser it looks plain by design — the value is the structure, not the decoration.

> [!CAUTION]
> Whitespace in HTML is collapsed. A dozen newlines in the editor become a single space between words. Use `<br>` for intentional line breaks and `<p>` for new blocks of text. If a line "disappears" onto the previous line, whitespace collapse is almost certainly the cause.

## Task 1: Publish the Morning Log

Build `pier-log.html` for the Tideglass Observatory. Include a single `<h1>` naming Greyharbor, a `<h2>` for morning readings, a paragraph with at least one `<br>` and at least two forms of text formatting, an unordered list of three buoys, an ordered list of three checklist steps, an image with meaningful `alt` text, and a link to a forecast page with descriptive link text.

**Why this order:** marking structure first means the observatory can publish a readable log on a bare terminal-like browser, and later add CSS without rewriting the meaning of the page.

**Next:** [[02 - Tideframe Blueprint]]
