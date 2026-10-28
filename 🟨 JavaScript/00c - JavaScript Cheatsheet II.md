# 00c. JavaScript Cheatsheet II

**Spanish version:** [00c - Chuleta de JavaScript II.md](00c%20-%20Chuleta%20de%20JavaScript%20II.md)

**Course:** JavaScript
**Topic:** Quick reference for the browser half: `<script>`, the DOM, selection, content & style writes, events and `addEventListener`
**Tags:** `#javascript` `#dom` `#events` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-E67E22?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Covers-Chapter_08-7C5CFF?style=for-the-badge" alt="Chapter 08">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

The browser half of the module on one page. Everything here was introduced in
[[08 - Living HUD]] — nothing on this sheet is new. The core language — variables, types,
operators, loops, arrays, functions and objects — lives in [[00b - JavaScript Cheatsheet]].

> [!TIP]
> The DOM never gets more complicated than this sheet suggests: **select, read, write,
> listen**. Real projects only multiply the number of elements, not the number of ideas.

**The running theme of this module: Emberfall**, a roguelike dungeon crawler. This sheet is
the wiring behind its web companion: the health bar, the mood stone, the potion button, the
loot card generator.

---

## 🔌 Loading JavaScript

```html
<!-- At the end of <body> — after the markup it touches -->
<script src="script.js"></script>
```

| Placement | Note |
| :--- | :--- |
| End of `<body>` | The default — elements exist before the script runs |
| In `<head>` | Only with `defer`, or the elements are not there yet |
| Inline `<script>...</script>` | Fine for tiny demos; keep real code in `.js` files |

---

## 🌳 The DOM in One Table

The **DOM** (Document Object Model) is the rendered page as a tree of objects. The global
`document` is its root; every tag is an object under it.

| Method | Returns | Reaches for it when |
| :--- | :--- | :--- |
| `document.querySelector("css")` | First matching element | You know a CSS selector |
| `document.getElementById("id")` | One element by id | The element has a unique `id` |
| `document.getElementsByClassName("cls")` | Collection of matches | You need **every** element with a class |
| `document.body` | The `<body>` element | Styling or appending to the whole page |

`querySelector` accepts any CSS selector from the CSS course: `"p"`, `".card"`,
`"#health-bar"`.

---

## ✍️ Writing to the Page

| Property | Writes | Note |
| :--- | :--- | :--- |
| `.innerText` | Rendered text | The safe default — no markup interpreted |
| `.innerHTML` | Raw HTML | Powerful, and a hole if the input is user text |
| `.src` | Image source | The sprite-swap trick: `img.src = "lit.png"` |
| `.disabled` | Button state | `true` mutes the button — game over screens |
| `.className` | Replaces all classes | Overwrites every class on the element |
| `.classList.add("x")` | Adds one class | Keeps the rest — the modern habit |

```js
const hpBar = document.querySelector("#health-bar");
hpBar.innerText = "HP: 85 / 100";
document.querySelector("img").src = "smiley2.png";
```

---

## 🎨 Writing Styles

Every selected element carries `.style` for its inline CSS. Two rules:

- Multi-word properties become **camelCase**: `background-color` → `backgroundColor`,
  `font-size` → `fontSize`, `text-align` → `textAlign`.
- Values are **strings** — quotes required.

```js
element.style.backgroundColor = "red";
element.style.fontSize = "24px";
element.style.textAlign = "center";
```

---

## 🖱️ Events

An **event** is anything the player does: click, hover, keypress, submit. `addEventListener`
attaches a function and **waits** — it runs once per trigger.

```js
button.addEventListener("click", function () {
  // runs on every click
});
```

| Event | Fires when |
| :--- | :--- |
| `"click"` | The element is clicked — buttons, cards, the page itself |
| `"mouseover"` | The pointer enters the element |
| `"keydown"` | A key is pressed — the classic input handler |
| `"submit"` | A form is submitted |

```js
let hp = 100;
const useButton = document.getElementById("use-button");

useButton.addEventListener("click", function () {
  hp = hp + 25;
  if (hp > 100) {
    hp = 100;
  }
  document.querySelector("#hp-display").innerText = "HP: " + hp + " / 100";
});
```

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| Script in `<head>` without `defer` | The script runs before the elements exist; `querySelector` returns `null` |
| `.style.background` with a hyphen | Syntax error — DOM properties are camelCase |
| Forgetting quotes on style values | `style.fontSize = 24px` throws; it must be `"24px"` |
| `.innerHTML` with user input | Injects markup — including anything hostile; prefer `.innerText` |
| Listener inside a loop with `var` | Every iteration shares one variable; `let` gives each its own |
| Expecting `.style` to read CSS rules | It only reflects **inline** styles — computed styles need `getComputedStyle` |
| Selecting before the DOM exists | `null` — the element is not in the tree yet; check your script placement |

---

## 🎮 The One-Page Version

Everything from this sheet in a single file — one Emberfall campfire widget:

```html
<!DOCTYPE html>
<html>
  <body>
    <h1 id="status">HP: 100 / 100</h1>
    <button id="use-button">Use Potion 🧪</button>

    <script>
      let hp = 100;
      const useButton = document.getElementById("use-button");
      const status = document.getElementById("status");

      useButton.addEventListener("click", function () {
        hp = hp + 25;
        if (hp > 100) {
          hp = 100;
          status.style.backgroundColor = "green";
        }
        status.innerText = "HP: " + hp + " / 100";
      });
    </script>
  </body>
</html>
```

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — the core language half: variables, loops, arrays, functions, objects
- [[08 - Living HUD]] — where every statement on this sheet is introduced, with quests
- [[01 - Glass Pier Primer]] — the markup the DOM renders
- [[12 - The Tide Run]] — laying out the page this script manipulates

---
