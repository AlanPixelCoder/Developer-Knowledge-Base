# 08. Living HUD

**Spanish version:** [08 - HUD Vivo.md](08%20-%20HUD%20Vivo.md)

**Course:** JavaScript
**Chapter:** 8 — Backpanel Display
**Topic:** DOM selection, innerText, style, addEventListener
**Tags:** `#javascript` `#dom` `#events` `#hud` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FF6B35?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

The backpanel of a cabinet has status lamps and readouts. Until now, the script has only written to the console. To light those readouts, JavaScript must touch the page: find elements, change their text, tweak styles, and react to button presses. That is the DOM.

## Finding Elements

Use `document.querySelector()` to grab the first element matching a CSS selector. Give elements `id` attributes so they are easy to target.

```js
// Assuming HTML has <span id="creditReadout">0</span>
let readout = document.querySelector("#creditReadout");
console.log(readout);
```

> [!NOTE]
> The selector `#id` targets an ID. `.class` targets classes. `button` targets a tag. If nothing matches, `querySelector` returns `null` — trying to read properties from `null` will throw an error, so check or be sure the element exists.

## Changing Text and Styles

Update visible text with `innerText`. Change CSS inline with `.style`.

```js
let readout = document.querySelector("#creditReadout");
readout.innerText = "CREDITS: 3";
readout.style.color = "#F7DF1E";
readout.style.fontWeight = "bold";
```

## Output

```text
(readout updates on the page)
```

The exact visual change is in the browser, but the action is deterministic: find element, assign new text, assign style properties. Keep in mind that `innerText` is about visible text; `innerHTML` exists but can be risky if you inject untrusted content.

> [!WARNING]
> Writing user input directly to `innerHTML` opens the door to injection. For plain status text, prefer `innerText`.

## Reacting with Events

A button does nothing until you listen for a click. `addEventListener("click", handler)` wires a function to run when the event fires.

```js
let insertBtn = document.querySelector("#insertCoin");
let readout = document.querySelector("#creditReadout");
let credits = 0;

insertBtn.addEventListener("click", function() {
  credits = credits + 1;
  readout.innerText = "CREDITS: " + credits;
  readout.style.color = credits >= 3 ? "#2DD4BF" : "#F7DF1E";
});
```

## Output

```text
(clicking updates the readout on the page)
```

> [!TIP]
> The handler is just a function. You can use a named function or an arrow function. The logic inside is the same as the console — variables, conditionals, arithmetic — now connected to the page.

## Why the DOM

The console is a testing bench. The HUD is the cabinet speaking back to the pilot. By combining selection, mutation of text/styles, and event listeners, the static markup becomes a live display that responds to actions. Every concept from chapters 1–7 (variables, conditionals, loops, arrays, functions, objects) remains the same; only the output target changes to the page.

**End of Module — Cabinet Guild: Complete**

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
