# 01. Insert Coin

**Spanish version:** [01 - Inserta la Moneda.md](01%20-%20Inserta%20la%20Moneda.md)

**Course:** JavaScript
**Topic:** What JavaScript is, the Web Console, `console.log()`, line-by-line execution, comments and the Merchant Receipt project
**Tags:** `#javascript` `#web-development` `#basics` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-01_--_05_%2B_Project-7C5CFF?style=for-the-badge" alt="Lessons 01 to 05 plus project">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

The first chapter of the language that powers roughly **97.5% of the websites on the
internet** — including every page of the Emberfall companion site. By the end of it you
will know how to run JavaScript in the browser console, print messages, and leave comments,
and you will have built your first program: a **merchant's receipt** printed line by line
to the terminal. Quick reference for everything in this chapter:
[[00b - JavaScript Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> HTML labels content and CSS styles it; JavaScript is the first language in this vault
> that actually **runs** — you write instructions, the engine executes them in order, and
> what they do is up to you.

---

## 01. The Engine Room

> [!NOTE]
> **Key information**
> **JavaScript** was created by **Brendan Eich** at Netscape in **1995** — legendaryy, in
> about ten days, at the dawn of the dot-com era. Today it is the only language that runs
> natively in every browser, and it powers about 97.5% of all websites.

JavaScript is a **programming language**: unlike HTML, it does not label content — it
**instructs** the machine. Those instructions can print messages, react to clicks, roll
damage dice, or drive an entire game loop.

### The Three Core Web Technologies

| Technology | Role | In the Emberfall site |
| :--- | :--- | :--- |
| **HTML** | Creates the **structure** of a web page | The skeleton: which HUD panels exist |
| **CSS** | Styles the **appearance** of a page | The skin: colors, fonts, layout |
| **JavaScript** | Makes it **interactive** | The engine: health bars that update |

This course focuses on JavaScript. Files we create use the **`.js`** file extension — but
for the first chapters we will not even need a file: everything runs in the browser console.

### Quest: First Input

Every game console boots with a test. Open the Web Console (see below) and run:

```js
console.log("Emberfall engine v1.0 online");
```

The console prints `Emberfall engine v1.0 online`. You just executed your first line of
JavaScript — the engine is alive.

---

## 02. The Console

### What Is the Web Console?

The **Web Console** is a built-in browser feature used to run JavaScript code and view
output messages. It is the terminal of the web world, and it comes attached to every page
you visit.

### Opening the Console

| Browser | Path | Keyboard Shortcut |
| :--- | :--- | :--- |
| **Google Chrome** | View > Developer > JavaScript Console | `cmd` + `option` + `c` (macOS) |
| **Apple Safari** | Develop > Show JavaScript Console | `option` + `cmd` + `c` |
| **Mozilla Firefox** | Tools > Browser Tools > Web Developer Tools | `ctrl` + `shift` + `i` (Windows/Linux) |

> [!TIP]
> In Chrome the Console tab sits between **Elements** and **Sources**; in Firefox, between
> **Inspector** and **Debugger**. The shortcut `cmd` + `option` + `c` works in all three
> and is worth memorizing — you will open the console dozens of times a day.

### `console.log()`

`console.log()` tells the web console to output a message. The message goes between the
parentheses `()` and inside quotes — either double `"..."` or single `'...'`, as long as
the opening and closing quotes **match**:

```js
console.log("Lantern oil: low");
console.log('Ember Shard in inventory');
```

Both lines print their text exactly as written.

> [!NOTE]
> A semicolon `;` at the end of a JavaScript statement is **optional**. This vault writes
> them, because most style guides do — but the engine will not complain if you skip them.

> [!WARNING]
> **The mistake everyone makes once**
> Quotes must match. `"Emberfall'` is a **SyntaxError**: the engine reads the string from
> the first `"` and keeps looking for the closing `"` until it gives up. Same rule for
> parentheses and braces — an unclosed one swallows everything after it.

---

## 03. Line by Line

### Sequential Execution

JavaScript runs code **sequentially**: one line at a time, from top to bottom. There is no
mystery and no jumping around — line 2 waits for line 1, line 3 waits for line 2.

Multiple `console.log()` calls print in the order they appear:

```js
console.log("Entering the Deep Halls...");
console.log("Torch equipped");
console.log("Something moves in the dark...");
// Output:
// Entering the Deep Halls...
// Torch equipped
// Something moves in the dark...
```

### Quest: Signal Flag

ASCII art only works if every line prints exactly where it should. Recreate this banner
with one `console.log()` per line:

```js
console.log("    a");
console.log("  b c");
console.log(" d e f");
console.log("g h i j");
console.log("   k");
```

Swap the letters for the first letter of your own game's title and check that the shape
survives. If one line is off, the engine printed something different from what you
expected — which is exactly how debugging starts.

---

## 04. Secret Recipe

### Comments

**Comments** are notes written for humans. The engine **ignores them completely** — they
never execute, never print, never break anything. They document what the code does, or
park code you are not ready to delete.

### Single-Line Comments

Two forward slashes `//` comment out the rest of the line:

```js
// console.log("This never runs");
console.log("Only this prints"); // this trailing note is ignored too
```

### Multi-Line Comments

`/*` opens a comment and `*/` closes it. Everything between them is dead to the engine,
no matter how many lines long:

```js
/*
  Emberfall crafting notes:
  1 Ember Shard + 2 Ash Mushrooms = one Lantern Charge.
  Drop rates documented in the design doc, section 4.
*/
console.log("Recipe loaded");
```

> [!TIP]
> Comments are the easiest place to leave a lie behind. `// fix before launch` survives for
> years. Write comments that stay true, or delete them.

---

## 05. Merchant Receipt

### Checkpoint: Chapter Recap

- `console.log()` outputs messages to the console.
- JavaScript executes **line by line**, top to bottom.
- Single-line comments use `//`; multi-line comments use `/* ... */`.
- Strings need **matching** quotes; semicolons are optional but recommended.

### Project: Merchant Receipt

Time for the first program. Using nothing but `console.log()`, print the receipt of a
supply purchase from the Emberfall outpost merchant — name of the shop, an **Order
Details** block with **Item**, **Quantity** and **Price** columns, at least two items, and
a total:

```js
console.log("================================");
console.log("    EMBERFALL OUTPOST SUPPLY    ");
console.log("================================");
console.log("          Order Details         ");
console.log("--------------------------------");
console.log("Item        Quantity    Price");
console.log("--------------------------------");
console.log("Torch         2        4.50");
console.log("Rope          1        3.25");
console.log("Lantern Oil   1        6.00");
console.log("--------------------------------");
console.log("Total                  18.25");
console.log("================================");
```

Count the lines: the receipt is just a sequence of prints, but the alignment comes from
**you** spacing the strings by hand. That is the whole skill of this chapter: precision in
what the engine receives.

> [!TIP]
> **Game dev version**
> This is the shape of every debug overlay ever written. The HP bar readout in an
> engine's developer HUD, the loot table dump, the server log — all of them are
> `console.log()` in a trench coat. Chapter [[03 - Loot Rolls]] teaches the engine to
> compute the numbers you are currently typing by hand.

---

## 💎 Bonus Loot: The Console Is a Full Interpreter

The console is not just an output window — it is a complete JavaScript interpreter. A few
powers worth knowing now:

### Evaluate Anything

Arithmetic and string concatenation work directly in the console:

```js
console.log(42 * 3);              // 126
console.log("Ember " + "Fall");   // Ember Fall
```

### Store Values in Variables

Results can be kept in variables with `let` or `const` — the full treatment is in
[[02 - Player Stats]]:

```js
let followers = 1000000;
```

### Autocomplete

Typing `document` followed by a period `.` pops a list of every available method and
property. The console tells you the API as you type — use it.

### Multi-Line Mode

All modern consoles support writing full multi-line programs: paste a whole block, or use
the console's multi-line input, and run it as one program.

---

## ⚡ XP Earned: Key Takeaways

- 🟨 **JavaScript runs.** It is the first language in the vault the machine actually executes.
- 🖥️ The **Web Console** is the browser's terminal; `cmd` + `option` + `c` opens it.
- 📢 `console.log("message")` prints — quotes must **match**, semicolons are optional.
- 📜 Execution is **line by line**, top to bottom. No exceptions at this level.
- 💬 `//` comments out one line; `/* ... */` comments out a block.
- 🧾 A receipt is just many `console.log()` calls, aligned by hand.

---

## 🎁 Loot Table: Real-World Use Cases

- 🐛 Debugging: print the value of anything, at any point, while it runs
- 🧪 Testing snippets before committing them to a file
- 📊 Server-side logs — `console.log()` also runs in Node.js
- 🎮 Debug overlays, loot dumps and stat readouts in game tools
- 📝 Quick calculations without leaving the browser

---

## 🎮 Side Quests: Practice Exercises

1. Print your game's title as an ASCII banner, one `console.log()` per line.
2. Print a receipt for an in-game blacksmith order with at least three items.
3. Print a five-line "patch notes" list using only `console.log()`.
4. Write a comment that disables one `console.log()`, run the file, and confirm it is silent.
5. **Boss fight:** print a full screen-width receipt — name, address line, three items, tax
   line, total — with every column aligned using only spaces inside the strings.

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — every statement from this chapter on one page
- [[02 - Player Stats]] — next chapter: variables, data types and damage math
- [[03 - Loot Rolls]] — conditionals: teaching the engine to make decisions
- [[08 - Living HUD]] — where `console.log` grows up into a real interface

---
