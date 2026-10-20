# 02. Spawn Point

**Spanish version:** [02 - Punto de Aparición.md](02%20-%20Punto%20de%20Aparici%C3%B3n.md)

**Course:** React
**Topic:** Node.js & npm, Vite scaffolding, the dev server, hot reloading, project structure, and the root mounting container with `createRoot`
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-01_--_07-7C5CFF?style=for-the-badge" alt="Lessons 01 to 07">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Chapter 01 sold you on the library. This chapter **installs it**. By the end you will have
Node.js and npm verified, a React project scaffolded with **Vite**, the dev server running
at `http://localhost:5173/`, and a clear map of every file in the project — including the
one sacred line that anchors the whole app to the page. Quick reference for everything in
this chapter: [[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A React app is a pile of JavaScript files until `npm run dev` gives them a server — so
> this chapter sets up the toolchain, walks the project files, and lands on the single
> `<div id="root">` where everything you build will live.

---

## 01. Before You Spawn

> [!NOTE]
> **Key information**
> **Node.js** is a JavaScript runtime that executes the language **outside the browser**.
> **npm** (Node Package Manager) is the tool that downloads and manages the libraries your
> project depends on. Both ship together when you install Node.

React development happens on your machine, not inside a browser tab: your editor writes the
code, Node.js runs the tools that process it, and npm fetches the libraries those tools need.
Install Node.js from nodejs.org (the LTS build is the safe pick), then verify the spawn
requirements:

```bash
# Check that Node.js is installed — v18 or newer recommended
node -v
```

The terminal answers with a version like `v20.11.0`. If it answers with *command not found*,
the install did not land — go back to nodejs.org before continuing.

> [!TIP]
> npm is not a separate download: it is bundled with Node. `node -v` green means `npm` is
> already on your system, ready to summon packages from the registry.

### Quest: Loadout Check

Run `node -v` and write down the version. Anything from **v18** upward is ready for this
module. If you are on an ancient version (v12, v14), upgrade to the LTS build now — modern
Vite refuses to spawn on runtimes that old.

---

## 02. The Vite Glyph

### What Is Vite?

**Vite** (pronounced /veet/, from the French for "quick") is a lightweight frontend build
tool. It bundles your code, starts a dev server in milliseconds, and refreshes the page as
you type. It is the standard way new React projects are born.

### Scaffolding the Project

One command conjures the project. Vite asks three interactive questions — project name,
framework and variant:

```bash
# Scaffold a fresh React app. The prompts ask for:
#   project name -> my-first-app
#   framework    -> React
#   variant      -> JavaScript (or JavaScript + SWC, the Rust-based Speedy Web Compiler)
npm create vite@latest
```

Answer the prompts like this:

| Prompt | Your answer | Notes |
| :--- | :--- | :--- |
| **Project name** | `my-first-app` | Becomes the folder name |
| **Framework** | `React` | The library this course covers |
| **Variant** | `JavaScript` | `JavaScript + SWC` is the same thing, compiled by the Rust-based **S**peedy **W**eb **C**ompiler — faster, same result |

Then enter the folder, download the dependencies, and boot:

```bash
# Enter the project folder and download its dependencies into node_modules
cd my-first-app
npm install

# Boot the dev server — the site appears at http://localhost:5173/
npm run dev
```

- `npm install` reads `package.json` and downloads every dependency into a folder called
  `node_modules`. It runs once per project (and again whenever dependencies change).
- `npm run dev` starts the dev server. Open `http://localhost:5173/` and the default app
  greets you — your first React app, running.

> [!WARNING]
> **The mistake everyone makes once**
> Running `npm run dev` in the wrong folder — or before `npm install` — and getting
> `Cannot find module` or an empty directory listing. The server runs **inside** the project
> folder: `cd my-first-app` first, and run `npm install` once before the first boot.

### Quest: First Boot

Scaffold `my-first-app`, run the install, start the dev server, and open
`http://localhost:5173/`. Edit the text inside `src/App.jsx`, save, and watch the browser
update **before you finish reaching for the mouse**. You are now running React.

---

## 03. Anatomy of a Spawn Point

Every Vite React project has the same skeleton:

```text
my-first-app/
├── index.html          ← root entry: hosts the <div id="root"> mount point
├── package.json        ← scripts and dependency list
├── vite.config.js      ← Vite configuration
└── src/
    ├── App.jsx         ← the root component (JSX markup lives here)
    └── index.css       ← global styles
```

| File | Role |
| :--- | :--- |
| `index.html` | The only real page the browser ever loads; it hosts `<div id="root">` |
| `package.json` | Declares dependencies and the `dev` / `build` scripts |
| `vite.config.js` | Configuration for the bundler and dev server |
| `src/App.jsx` | The root component — the top of everything you will render |
| `src/index.css` | Global styles applied across the app |

> [!NOTE]
> Note the `.jsx` extension on `App.jsx`. Vite accepts both `.js` and `.jsx`, but the extra
> `x` announces "this file contains JSX markup" to the compiler and to your editor — both
> of which read it and switch into the right mode.

### Quest: Read the Runes

Without searching the internet, write one sentence for each file above explaining what would
break if it were deleted. `index.html` and `App.jsx` are the two you will touch most; the
other three you mostly configure and ignore.

---

## 04. The Two Engines

Look inside `package.json` and two dependencies matter more than the rest:

```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }
}
```

| Package | Role |
| :--- | :--- |
| `react` | The **core engine**: components, hooks, and the virtual DOM — the ideas from chapter [[01 - The Rebirth]] |
| `react-dom` | The **DOM-specific renderer**: everything that puts React's output onto an actual web page, including `createRoot` |

They split responsibilities on purpose. `react` knows what a component *is*; `react-dom`
knows how to show one on a browser page. A future renderer (React Native, for phones) swaps
`react-dom` out and keeps `react` — same engine, different display.

---

## 05. The Living Reload

Start the server with `npm run dev` and leave it running. Vite watches your files: the
rendered output updates **in real time as you type**, with no manual refresh and no rebuild
step. Save a file and the browser reflects the edit almost instantly — that is **hot
reloading**.

The dev server is also your first debugger:

- A **compile error** (unbalanced tag, stray brace) appears as an overlay in the browser,
  with the file name and the message.
- A **runtime error** appears the same way, with the file and the **stack trace** — the
  chain of function calls that led to the crash.

> [!TIP]
> Read the overlay instead of refreshing it away. The top line names the file; the stack
> trace names the line. Nine times out of ten the bug is the first file in that list.

### Quest: Break It Deliberately

Open `src/App.jsx` and delete one closing `</div>` tag. Save. Read the error overlay out
loud — file name, message. Undo the change, save, and watch the app heal. Repeat with a
runtime error (type `{undefinedThing.map(...)}` inside the markup). Fear of the red overlay
is the fastest way to stop learning; reading it is the fastest way to start.

---

## 06. The Classic Layout

Vite is the modern spawn point, but you will meet older React projects — and plenty of
tutorials — laid out the classic way (the Create React App convention):

```text
classic-project/
├── public/
│   └── index.html      ← static entry page, copied as-is into the build
├── src/
│   ├── index.js        ← entry script: renders <App /> into the root
│   ├── App.js          ← root component
│   └── styles.css      ← global styles
└── package.json
```

| File | Role |
| :--- | :--- |
| `public/index.html` | The static HTML shell served to the browser |
| `src/index.js` | The JavaScript entry point: it imports React and mounts the app |
| `src/App.js` | The root component — same job as Vite's `App.jsx` |
| `package.json` | Dependencies and scripts, as always |
| `styles.css` | Global stylesheet — same job as Vite's `index.css` |

Same castle, different floor plan: a public HTML shell, an entry script that mounts the app,
a root component, and a stylesheet. Whether you see `App.js` or `App.jsx` and `index.js` or
`main.jsx`, the wiring is identical — an entry script finds the root element and renders the
root component into it.

---

## 07. The Root Anchor

### The Mounting Container

Every React app needs **one place** on the real page to take over. The classic HTML shell
keeps it in the `<body>`:

```html
<body>
  <div id="root"></div>
</body>
```

An empty `<div>` with an `id` of `"root"`. React does not care what else is on the page —
it will treat that div as its territory.

### `createRoot` and `render`

The entry script claims the container with `createRoot` (imported from `react-dom/client`)
and paints the app into it:

```javascript
import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

const root = createRoot(document.getElementById("root"));
root.render(<App />);
```

Line by line: import React, import `createRoot`, import the root component `App`; grab the
`<div id="root">` from the document with `document.getElementById("root")`; hand it to
`createRoot`; call `root.render(<App />)` to draw the component tree into the page. From
that call on, everything inside `<App />` is React's to maintain.

> [!WARNING]
> **The classic crash**
> Delete the `id="root"` attribute (or point `getElementById` at a different id) and the app
> dies on boot with the runtime error `Target container is not a DOM element`. React cannot
> find its anchor, so it refuses to render anything. One attribute, holding up the entire
> companion site.

### Quest: Re-Wire the Anchor

In `index.html`, rename the container to `id="app"`, then fix the entry script so the app
boots again. Break it first on purpose, read the `Target container is not a DOM element`
overlay, and only then apply the fix. You have now traced the full spawn path: HTML
container → `createRoot` → `render`.

---

## ⚡ XP Earned: Key Takeaways

- 🛠️ **Node.js** runs JavaScript outside the browser; **npm** fetches libraries. Verify with
  `node -v` (v18+ recommended).
- ⚡ **Vite** (/veet/, French for "quick") scaffolds the project: `npm create vite@latest`,
  then `cd`, `npm install`, `npm run dev` → `http://localhost:5173/`.
- 🗂️ Vite anatomy: `index.html` (hosts the root div), `package.json`, `vite.config.js`,
  `src/App.jsx`, `src/index.css`. The classic layout adds `public/`, `index.js` and `App.js`.
- 📦 `react` is the core engine; `react-dom` is the DOM renderer that provides `createRoot`.
- 🔥 **Hot reloading** repaints as you type; compile and runtime errors show an overlay with
  the file and the stack trace.
- 🎯 Everything mounts through one anchor: `<div id="root">` → `createRoot(...)` →
  `root.render(<App />)`. Lose the id and you lose the app: `Target container is not a DOM
  element`.

---

## 🎁 Loot Table: Real-World Use Cases

- 🏗️ `npm create vite@latest` is how nearly every modern React project, prototype and
  hackathon app starts
- 🧪 A local dev server with hot reload is the standard feedback loop for front-end work
- 📦 Understanding `package.json` transfers to every JS tool on the planet
- 🔍 The error overlay teaches you to read stack traces — a skill that outlives React
- 🧩 Knowing both Vite and classic layouts lets you contribute to old and new codebases

---

## 🎮 Side Quests: Practice Exercises

1. Scaffold a second project named `guild-dashboard` and delete it afterwards — muscle memory
   for the three prompts.
2. List the contents of `node_modules` and find the `react` folder inside it.
3. Add a `<p>` to `index.html` **outside** the root div and observe that React never touches it.
4. Change `src/index.css`, save, and time how long the browser takes to show it.
5. **Boss fight:** reproduce the `Target container is not a DOM element` error from scratch —
   rename the id, run the app, read the overlay — then fix it with a one-line change and
   write down the exact path from `index.html` to `root.render`.

---

## 🔗 See Also

- [[01 - The Rebirth]] — the previous chapter: what React is, and why this toolchain exists
- [[03 - Glyph Workshop]] — next chapter: JSX, the syntax `App.jsx` is written in
- [[04 - Living Markup]] — what you can actually put inside that JSX
- [🟨 JavaScript MOC](../%F0%9F%9F%A8%20JavaScript/README.md) — the JavaScript foundations this module assumes

---
