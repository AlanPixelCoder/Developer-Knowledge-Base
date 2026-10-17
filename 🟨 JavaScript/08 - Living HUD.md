# 08. Living HUD

**Spanish version:** [08 - HUD Vivo.md](08%20-%20HUD%20Vivo.md)

**Course:** JavaScript
**Topic:** The `<script>` element, the DOM, selection methods, `innerText` / `src` / `.style`, events, `addEventListener()` and the Loot Card Generator capstone
**Tags:** `#javascript` `#dom` `#events` `#browser` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-E67E22?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-39_--_44_%2B_Capstone-7C5CFF?style=for-the-badge" alt="Lessons 39 to 44 plus capstone">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Everything so far ran in the console — invisible to players. This chapter wires the engine
to the page. The **DOM** turns the HTML of [[01 - HTML Basics]] into a live object tree
JavaScript can read and rewrite, and **events** let the player pull the levers. By the end
you will build the module's capstone: a **Loot Card Generator** that mints a random card
on every click. Reference: [[00c - JavaScript Cheatsheet II]].

> [!NOTE]
> **The whole chapter in one sentence**
> The DOM is the page rendered as a tree of objects under the global `document`; select
> elements with `querySelector` / `getElementById`, change them with `innerText`, `src`
> and `.style`, and react to the player with `addEventListener`.

---

## 01. Green Light

### The `<script>` Element

HTML builds the page, CSS styles it — **`<script>`** is how JavaScript gets on the page at
all. It can live in `<head>` or near the end of `<body>`:

```html
<script src="script.js"></script>
```

For anything larger than a snippet, keep scripts in a separate `.js` file and link it with
the `src` attribute — exactly the clean split HTML preaches. The browser loads the HTML,
then fetches and runs the script.

---

## 02. The Scene Tree

### What Is the DOM?

The **Document Object Model (DOM)** represents the page as a family tree of nodes and
objects. The root is `<html>`, which branches into `<head>` and `<body>`, each holding
attributes, child elements and text nodes.

Every tag you wrote in the HTML course is now an **object** in memory — with properties
JavaScript can read and write. The bridge between the two languages is the global
`document` object.

### Selecting Elements

| Method | Returns | Use it for |
| :--- | :--- | :--- |
| `document.querySelector("css")` | First match | One element, any selector |
| `document.getElementById("id")` | One element | A known, unique id |
| `document.getElementsByClassName("cls")` | Collection | Every element with a class |

`querySelector` accepts any CSS selector from the CSS course — tag, `.class` or `#id`:

```js
document.querySelector("p");
document.querySelector(".card");
document.querySelector("#health-bar");
```

### Reading and Writing Text

The `.innerText` property reads or replaces the **rendered text** inside an element:

```js
document.querySelector("#health-bar").innerText = "HP: 85 / 100";
```

`.innerHTML` does the same for the raw HTML inside — useful when the replacement is markup,
dangerous when the input is user text. `.src` swaps an `<img>`'s source, the classic
sprite-change trick:

```js
document.querySelector("img").src = "smiley2.png";
```

---

## 03. Mood Ring

### Changing Styles with `.style`

Every selected element carries a `.style` property for its inline CSS. Two rules:

- Multi-word CSS properties become **camelCase** in the DOM: `background-color` →
  `backgroundColor`, `font-size` → `fontSize`, `text-align` → `textAlign`.
- Values are **strings** — quotes required.

### Quest: Campfire Mood

A stone that changes color with the engine's mood — the mood ring of a dungeon camp:

```js
let stone = document.getElementById("stone");
let randomNumber = Math.floor(Math.random() * 9) + 1;

if (randomNumber === 1) {
  stone.style.backgroundColor = "red";
} else if (randomNumber === 2) {
  stone.style.backgroundColor = "orange";
} else {
  stone.style.backgroundColor = "black";
}
```

Every piece of the chapter so far, together: a DOM selection, `Math.random()` from
[[03 - Loot Rolls]], and an `else if` chain writing a camelCase style property.

---

## 04. The Player Pulls the Lever

### Events and Event Listeners

An **event** is anything the player does on the page: a click, a hover, a form submit, a
keypress. `addEventListener()` attaches a function to an element and **waits** — nothing
runs until the action actually happens:

```js
element.addEventListener("click", function () {
  // runs on every click
});
```

### Quest: Health Potion Button

The HUD's most honest interaction — a potion that heals, one press at a time:

```js
let useButton = document.getElementById("use-button");
let hpDisplay = document.getElementById("hp-display");

let currentHP = 100;

useButton.addEventListener("click", function () {
  currentHP = currentHP + 25;
  if (currentHP > 100) {
    currentHP = 100;
  }
  hpDisplay.innerText = "HP: " + currentHP + " / 100";
});
```

Read the flow: the function is **defined** at load time and **called** later, once per
click — a function from [[06 - Skill Functions]] living inside an event from this chapter.

---

## 05. The Capstone

### Checkpoint: Chapter Recap

- `<script src="script.js">` links JavaScript to HTML — usually at the end of `<body>`.
- The DOM is the page as an object tree; `document` is its global root.
- `querySelector` (any CSS selector), `getElementById`, `getElementsByClassName` select.
- `.innerText`, `.innerHTML` and `.src` rewrite content; `.style.camelCase` rewrites look.
- `addEventListener("click", fn)` waits for the player and runs `fn` on every trigger.

### Project: Loot Card Generator

The module's final boss. Two arrays from [[05 - Inventory]] — art and flavor text — a random
index into each, and a click handler that mints a fresh card every press. This is the
internet's oldest party trick, wearing game gear:

```js
const cardArt = [
  "https://placehold.co/300x200/ff6b35/white?text=Ember+Shard",
  "https://placehold.co/300x200/7c5cff/white?text=Lantern+Oil",
  "https://placehold.co/300x200/00c2a8/white?text=Ash+Blade",
  "https://placehold.co/300x200/f7df1e/black?text=Ember+Key"
];

const cardFlavor = [
  "When your damage formula compiles on the first try with zero null references",
  "Me explaining 2D pixel RPG tactical damage formulas at 2 AM",
  "When the boss has 1 HP left and your 95% hit-rate attack misses",
  "Fixing one bug in the engine only to spawn three new boss fights in the console",
  "When the melodic boss theme drops right as you enter flow state"
];

let cardImage = document.getElementById("card-image");
let cardText = document.getElementById("card-text");
let forgeButton = document.getElementById("forge-button");

forgeButton.addEventListener("click", function () {
  let artIndex = Math.floor(Math.random() * cardArt.length);
  let textIndex = Math.floor(Math.random() * cardFlavor.length);

  cardImage.src = cardArt[artIndex];
  cardText.innerText = cardFlavor[textIndex];
});
```

The HTML side is one `<img>`, one `<p>` and one `<button>` — structure from the HTML course,
style from the CSS course, and everything that makes it *alive* from this module. Three
languages, one page, one button.

> [!TIP]
> **Where this goes next**
> Every real game UI is this file scaled up: a health bar that listens, an inventory grid
> that rerenders on change, a settings menu of sliders. The vocabulary never grows past
> select, read, write, listen — only the number of elements does.

---

## ⚡ XP Earned: Key Takeaways

- 🔌 `<script src="...">` is the bridge from HTML to JavaScript.
- 🌳 The DOM is the page as a tree of objects; `document` is the root.
- 🎯 Select: `querySelector` (any CSS selector), `getElementById`, `getElementsByClassName`.
- ✍️ Write: `.innerText` for text, `.src` for images, `.style.backgroundColor` for CSS (camelCase!).
- 🖱️ `addEventListener("click", fn)` waits for the player; `fn` runs on every trigger.
- 🃏 The capstone: arrays + randomness + selection + events = a working generator.

---

## 🎁 Loot Table: Real-World Use Cases

- ❤️ Live HUDs: health, mana, cooldowns, score counters
- 🎰 Gacha pulls, card generators, randomizers of every flavor
- 🧪 Click-through demos and interactive tutorials
- 🌗 Theme switchers — one class flip, the whole page changes
- 📱 The entire mobile web: taps in, DOM out

---

## 🎮 Side Quests: Practice Exercises

1. Wire a button that swaps an `<h1>`'s text to your game's title on click.
2. Make a second button that changes `document.body.style.backgroundColor`.
3. Build a two-state torch: one button toggles `src` between lit and unlit images.
4. Print a random NPC name from an array into a paragraph on every click.
5. **Boss fight:** a *damage simulator* — a "Hit" button, a `currentHP` variable, a random
   damage roll per click, and a `game over` state that disables the button at `0` HP
   (`button.disabled = true`).

---

## 🔗 See Also

- [[00c - JavaScript Cheatsheet II]] — DOM, styles and events on one page
- [[07 - Character Sheet]] — previous chapter: objects — the DOM is one big one
- [[01 - HTML Basics]] — the markup this chapter brings to life
- [[12 - Flexbox]] — laying out the page this script manipulates

---
