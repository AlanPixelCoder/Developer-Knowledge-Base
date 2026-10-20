# 03. Glyph Workshop

**Spanish version:** [03 - Taller de Glifos.md](03%20-%20Taller%20de%20Glifos.md)

**Course:** React
**Topic:** What JSX is, transpilation, `React.createElement`, basic component syntax, file extensions, and the parentheses rule
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Beginner to Intermediate">
  <img src="https://img.shields.io/badge/Lessons-01_--_06-7C5CFF?style=for-the-badge" alt="Lessons 01 to 06">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

At the spawn point you met the toolchain. Now you meet the **language it compiles**:
**JSX**. This chapter is the workshop where HTML-shaped glyphs are scribed directly inside
JavaScript, ground into the native `React.createElement` calls the browser can actually
execute, and wrapped in the parentheses that keep the compiler from eating your markup.
Quick reference for everything in this chapter: [[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> **JSX** is a syntax extension that lets you write HTML-shaped markup inside JavaScript; a
> **transpiler** rewrites it into `React.createElement(...)` calls that browsers can run.

---

## 01. The Glyph Language

**JSX** stands for **JavaScript Syntax Extension** — you may also see it called
**JavaScript XML**. It is **syntactic sugar** for the native React API: a friendlier
spelling that means exactly the same thing to the machine, the way `+= 1` means the same as
`= x + 1`.

The problem it solves: browsers **cannot execute JSX directly**. The `<h1>` you see is not
HTML the browser knows — it is a glyph from React's workshop, and it must be **transpiled**
(translated) into plain JavaScript before it can run.

```javascript
// What you write (JSX):
let heading = <h1 id="welcome-heading">Welcome!</h1>;

// What the transpiler produces (plain JavaScript):
let heading = React.createElement("h1", { id: "welcome-heading" }, "Welcome!");
```

Read the two lines carefully — they are the same instruction. The first argument to
`React.createElement` is the **tag name** (`"h1"`), the second is the **attributes object**
(`{ id: "welcome-heading" }`), and every argument after that is a **child** (`"Welcome!"`).

### Quest: Translate by Hand

Take this Emberfall sign and rewrite it as the `React.createElement` call a transpiler would
produce:

```javascript
<header id="main-header">Emberfall Launcher ☕</header>
```

Answer: tag `"header"`, attributes `{ id: "main-header" }`, one child string. You should
arrive at:

```javascript
React.createElement("header", { id: "main-header" }, "Emberfall Launcher ☕");
```

Do ten of these and JSX stops being magic. It becomes a spelling.

---

## 02. The Transpilers

A **transpiler** is a tool that reads source code in one language and writes it out as
another (or as a newer/older version of the same). In React's world, the transpilers that
turn JSX into browser-readable JavaScript are:

| Tool | Where you meet it |
| :--- | :--- |
| **Babel** | The classic long-time default; still everywhere in tutorials and configs |
| **SWC** | The Rust-based **S**peedy **W**eb **C**ompiler — the fast option Vite offers |
| **esbuild** | An extremely fast Go-based bundler/transpiler used under the hood by Vite |

> [!NOTE]
> You rarely invoke a transpiler by hand. Vite wires one into the pipeline: you save a
> `.jsx` file, the transpiler rewrites it, and the browser receives plain JavaScript. The
> hot reloading from [[02 - Spawn Point]] is this step running on every keystroke.

### Quest: Pick Your Forge

Re-scaffold a project with `npm create vite@latest` and choose `JavaScript + SWC` this time
instead of plain `JavaScript`. The app behaves identically — you have only swapped the
transpiler in the pipeline. That is the point: JSX in, JavaScript out, and the forge in the
middle is replaceable.

---

## 03. The Component Spell

JSX lives inside **components**. The basic component syntax is a function that **returns
markup**:

```javascript
export default function App() {
  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
}
```

Three things to notice, all of which you will use in every single component:

1. The function name is **capitalized** (`App`). React uses the capital letter to tell your
   components apart from HTML tags. Detail treatment is in [[05 - Building Blocks]].
2. It uses the `export default` keywords so other files can import it.
3. It **returns** JSX — the markup is the component's output, its return value.

`<h1>Hello, World!</h1>` is already a JSX expression; `<div>...</div>` wraps it so the
component has a single root (the rule chapter [[04 - Living Markup]] will hammer on).

> [!WARNING]
> **The classic mistake**
> Writing `return` on one line and the markup on the next:
>
> ```javascript
> return
>   <div>...</div>; // ❌ returns undefined!
> ```
>
> JavaScript's **automatic semicolon insertion (ASI)** quietly inserts a semicolon after
> `return`, and the function returns `undefined` — the markup is never reached, and nothing
> renders. This is exactly why the parentheses exist, and why the next section exists.

---

## 04. The Parenthesis Runes

Wrap multi-line JSX in **parentheses** `( )`:

```javascript
export default function App() {
  return (
    <div>
      <h1>Hello, World!</h1>
      <p>Welcome to the Emberfall codex.</p>
    </div>
  );
}
```

The parentheses do **not** change what the markup means. They tell JavaScript "the `return`
expression continues on the next line" — defeating **ASI**. With them, the markup reaches
the return; without them, on multiple lines, ASI turns your component into one that returns
nothing at all.

> [!TIP]
> Adopt the habit early: the moment a component spans more than one line of markup, put the
> opening `(` right after `return` and the closing `)` on its own line. Most editors and
> linters will format it that way for you anyway.

### Quest: Save the Scribes

Take the last multi-line JSX expression you typed (or the Merchant Receipt rendered as
markup) and deliberately remove the parentheses. Save it and watch the component render
nothing. Then put them back and watch it heal. You have now seen ASI bite; you will not
forget it.

---

## 05. The File Extension

JSX can live in files with either extension:

| Extension | Meaning |
| :--- | :--- |
| `.js` | Plain JavaScript — the classic layout put components here |
| `.jsx` | JavaScript that contains JSX markup — the Vite convention, an explicit hint to the compiler and the editor |

Both compile when a transpiler is wired in. Vite's scaffold uses `.jsx` to make the presence
of JSX unmistakable: `src/App.jsx` announces at a glance that its contents are markup-bearing
JavaScript, not a utility file.

> [!NOTE]
> The `.jsx` choice is a convention, not a requirement. The compiler does not care — it
> parses every file the same way. Teams pick `.jsx` so that a human scanning the file tree
> can tell markup from logic without opening anything.

### Quest: Rename the Forge

Rename `src/App.jsx` to `src/App.js` and fix the import in whatever file imports it. Run the
dev server: it works. Now rename it back. The lesson: the extension is a signal, and any
linter or teammate relying on that signal will thank you for keeping it accurate.

---

## 06. Glyphs at a Glance

### Checkpoint: Chapter Recap

- **JSX** is a JavaScript syntax extension (JavaScript XML) — syntactic sugar over
  `React.createElement`.
- Browsers cannot run JSX; **transpilers** (Babel, SWC, esbuild) rewrite it.
- `React.createElement(tag, attributes, ...children)` is what every JSX element becomes.
- A component is a **capitalized function** returning JSX, exported with `export default`.
- JSX lives in `.js` or `.jsx` files.
- Multi-line JSX needs **parentheses** to dodge automatic semicolon insertion.

### The Kit of Parts

Here is the same component, shown in both languages side by side, so the mapping stays in
front of you:

```javascript
// JSX glyph spell
export default function App() {
  return (
    <div className="hud">
      <h1>Emberfall Launcher ☕</h1>
    </div>
  );
}
```

```javascript
// What the transpiler grinds it into
export default function App() {
  return React.createElement(
    "div",
    { className: "hud" },
    React.createElement("h1", null, "Emberfall Launcher ☕")
  );
}
```

Notice `className` in both — `class` is a JavaScript keyword, a distinction chapter
[[04 - Living Markup]] covers in full. Notice too that the nested element becomes the third
argument of the outer call: children are arguments, all the way down.

> [!TIP]
> **Game dev version**
> Think of JSX as a scripting DSL for building scene trees. You write the tree in a shape a
> human reads instantly; the engine receives a flat list of "create node" calls. Every UI
> framework, every game editor, every CSS-in-JS engine has this same compile step under the
> hood — this chapter just lets you see it happening.

---

## ⚡ XP Earned: Key Takeaways

- 🏷️ **JSX** = JavaScript Syntax Extension (a.k.a. JavaScript XML): sugar over the native
  React API. Browsers cannot execute it.
- 🔧 **Transpilers** — **Babel**, **SWC**, **esbuild** — rewrite JSX into browser-readable
  JavaScript. Vite runs one in its pipeline on every save.
- 🧱 `React.createElement(tag, attributes, ...children)` is what every JSX element desugars
  to: tag string, attributes object, children as arguments.
- ✍️ A component is a **capitalized** function returning JSX, exported with `export default`.
- 📄 JSX lives in `.js` or `.jsx` files; `.jsx` is the Vite convention that signals markup.
- 🧷 Wrap multi-line JSX in `( )` — otherwise **automatic semicolon insertion** makes your
  function return `undefined`.

---

## 🎁 Loot Table: Real-World Use Cases

- 🖥️ Every React UI you have ever used is compiled from JSX down to `createElement` (or the
  runtime equivalent) before it reaches a browser
- 🧰 Understanding the output is what you need when a build error points at internals rather
  than your source
- 🎛️ Babel's and SWC's transpile step is the same one that powers TypeScript, modern syntax
  support and code minification
- 🧩 JSX-shaped DSLs echo across the ecosystem: styled-components, MDX, and game-editor
  scene builders all reuse the pattern
- 📐 The ASI parenthesis rule saves the single most common "why is nothing rendering?" bug

---

## 🎮 Side Quests: Practice Exercises

1. Translate three JSX signs (header, list, button) into `React.createElement` by hand.
2. Write a component with a capital name and one with a lowercase name and observe what
   React does differently.
3. Break ASI on purpose: `return` and markup on separate lines. Read the empty result.
4. Add a nested `<span>` inside your component and identify its position in the
   `createElement` argument list.
5. **Boss fight:** take the guild HUD from [[01 - The Rebirth]] (HP bar + quest list) and
   write it first in JSX with parentheses, then hand-translate the whole thing to nested
   `React.createElement` calls — including the `className` and the child elements. If your
   two versions render identically, you have mastered the workshop.

---

## 🔗 See Also

- [[01 - The Rebirth]] — the chapter that introduced components and JSX by name
- [[02 - Spawn Point]] — the toolchain that transpiles this syntax on every save
- [[04 - Living Markup]] — everything you can put inside JSX: expressions, conditions, attributes
- [[05 - Building Blocks]] — components and their naming and export rules in full

---
