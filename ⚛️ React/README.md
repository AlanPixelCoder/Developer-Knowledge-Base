# ⚛️ React: The Rebirth of the Interface (MOC)

**Español:** [README-ES.md](./README-ES.md)

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE_TO_ADVANCED-F0AD4E?style=for-the-badge" alt="Intermediate to advanced">
  <img src="https://img.shields.io/badge/Chapters-15-7C5CFF?style=for-the-badge" alt="15 chapters">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
  <img src="https://img.shields.io/badge/Environment-macOS-lightgrey?style=for-the-badge&logo=apple&logoColor=white" alt="macOS">
</p>

**Note:**
This module is the Map of Content (MOC) for the React notes in this Obsidian vault. React is the library that turns static pages into living interfaces — components that update themselves when data changes, forms that hold their own state, effects that reach out to APIs, and a router that makes a single HTML document feel like a whole website. Every example is kept minimal and builds the same fictional product: the *Emberfall Online* companion site, a guild dashboard, storefront and social feed for the vault's shared roguelike.

**Tip:**
Start at [[01 - The Rebirth]]. Learn what React is and why components exist before you touch JSX or hooks — once the component mental model is muscle memory, everything else in this module is composition.

**Prerequisite:** [🟨 JavaScript MOC](../%F0%9F%9F%A8%20JavaScript/README.md). This module assumes variables, types, functions, objects, arrays and DOM events are already familiar — [[08 - Living HUD]] in particular is the direct predecessor of everything here. [🌐 HTML MOC](../%F0%9F%8C%90%20HTML/README.md) and [🎨 CSS MOC](../%F0%9F%8E%A8%20CSS/README.md) complete the trio: React consumes the structure HTML provides and coexists with the styles CSS writes.

> [!NOTE]
> **The Emberfall narrative**
> Every exercise in this module belongs to the same fictional product: the *Emberfall Online*
> companion site. The guild HUD becomes a component tree, the social post becomes a
> composition exercise, the relic catalog becomes a `.map()` over state, the arena RSVP
> button becomes an accessibility drill, the class quiz becomes the capstone SPA. Nothing
> about the syntax changes between exercises — which is the point: you learn one
> vocabulary and reuse it everywhere.

---

## 🗺️ Map of Content

### 📚 Reference & Cheatsheets

* **Cheatsheets:**
  * [00b - React Cheatsheet](./00b%20-%20React%20Cheatsheet.md) — JSX, components, composition, props, state and events.
  * [00c - React Cheatsheet II](./00c%20-%20React%20Cheatsheet%20II.md) — forms, hooks, context, data fetching, routing and styling.

### 🏛️ I. The Interface Reborn (Chapters 1–4)

* **The Rebirth:** [01 - The Rebirth](./01%20-%20The%20Rebirth.md) — What React is, its 2013 origin at Facebook, declarative & component-based design, before vs. with React.
* **Spawn Point:** [02 - Spawn Point](./02%20-%20Spawn%20Point.md) — Node.js & npm, Vite scaffolding, the dev server, hot reloading, project structure and the `createRoot` mounting container.
* **Glyph Workshop:** [03 - Glyph Workshop](./03%20-%20Glyph%20Workshop.md) — What JSX is, transpilation into `React.createElement`, basic component syntax and the parentheses rule.
* **Living Markup:** [04 - Living Markup](./04%20-%20Living%20Markup.md) — The single-root rule, fragments, embedded expressions, conditional rendering, attributes and `className`.

### ⚙️ II. The Component Craft (Chapters 5–8)

* **Building Blocks:** [05 - Building Blocks](./05%20-%20Building%20Blocks.md) — Functional components, PascalCase, export/import, composing and instantiating components.
* **The Skill Tree:** [06 - The Skill Tree](./06%20-%20The%20Skill%20Tree.md) — Composition, hierarchy, parent-child relationships, one-way data flow and the guild post build.
* **Trade Routes:** [07 - Trade Routes](./07%20-%20Trade%20Routes.md) — Props, receiving props, `.map()` lists, state as props and component lists over state arrays.
* **The Health Bar:** [08 - The Health Bar](./08%20-%20The%20Health%20Bar.md) — `useState`, the setter, the immutability rule, timers and functional updates.

### 🎮 III. Interaction & Input (Chapters 9–10)

* **The Controller:** [09 - The Controller](./09%20-%20The%20Controller.md) — Synthetic events, `onClick`, the event object, hover, focus/blur, keyboard events and accessible composition.
* **The Forge:** [10 - The Forge](./10%20-%20The%20Forge.md) — Forms, `htmlFor`, `onChange`, `onSubmit`, controlled components, `select`/`textarea` and the form checklist.

### ✨ IV. Hooks, State & Data (Chapters 11–13)

* **The Relic System:** [11 - The Relic System](./11%20-%20The%20Relic%20System.md) — Hooks, `useEffect`, the dependency array, cleanup functions, `useRef` and state vs. refs.
* **The Guild Ledger:** [12 - The Guild Ledger](./12%20-%20The%20Guild%20Ledger.md) — Prop drilling, the Context API, `createContext`, providers, `useContext` and custom provider components.
* **The Courier:** [13 - The Courier](./13%20-%20The%20Courier.md) — `fetch()`, promises, loading states, `try/catch`, `response.ok`, error rendering and list filtering.

### 🗺️ V. The Whole Product (Chapters 14–15)

* **The World Map:** [14 - The World Map](./14%20-%20The%20World%20Map.md) — SPAs, client-side routing, `react-router-dom`, `BrowserRouter`, `Routes`, `Link` and `useNavigate`.
* **The Final Boss:** [15 - The Final Boss](./15%20-%20The%20Final%20Boss.md) — The capstone: the "Which Emberfall class are you?" quiz SPA, architecture, quiz logic, conditional routes and styling.

---

## 🎯 Learning Path

1. **The Rebirth** → understand the model: declarative UI, components, one-way updates.
2. **Spawn Point** → set up the forge: Node, Vite, the dev server and the root container.
3. **Glyph Workshop** → learn the alphabet: JSX and what it transpiles into.
4. **Living Markup** → make markup think: expressions, conditionals, attributes.
5. **Building Blocks** → write components: the unit of everything that follows.
6. **The Skill Tree** → compose them: hierarchies, parents and children.
7. **Trade Routes** → pass data: props, lists and state flowing downward.
8. **The Health Bar** → hold data: state that changes and re-renders.
9. **The Controller** → react to the player: events, mouse, keyboard, accessibility.
10. **The Forge** → collect input: controlled forms from `onChange` to submit.
11. **The Relic System** → reach outside: effects, cleanup, refs.
12. **The Guild Ledger** → go global: context instead of prop drilling.
13. **The Courier** → talk to APIs: fetch, promises, loading and errors.
14. **The World Map** → add pages: client-side routing without reloads.
15. **The Final Boss** → ship the product: everything in one quiz SPA.

---

## 🎯 What You'll Be Able To Do

- Scaffold a React app with Vite and explain every file in the project tree.
- Write JSX, know what it transpiles into, and respect its formatting rules.
- Build and compose functional components with correct PascalCase and exports.
- Pass props, render lists with `.map()`, and flow state downward to children.
- Manage state with `useState`, update it immutably, and use functional updates.
- Handle mouse, focus and keyboard events accessibly with synthetic events.
- Build controlled forms: `htmlFor`, `onChange`, `onSubmit`, `select` and `textarea`.
- Run side effects with `useEffect`, clean them up, and hold mutable data with `useRef`.
- Share state globally with the Context API and custom providers.
- Fetch data from APIs with loading states, error handling and list filtering.
- Route between views with `react-router-dom` without full-page reloads.
- Assemble all of it into a complete single-page application.

---

## 🧰 Tools

| Tool | Why |
| :--- | :--- |
| Node.js & npm | Runtime and package manager for the React toolchain |
| Vite | Build tool and dev server with hot reloading |
| Any code editor (VS Code recommended) | Write `.jsx` component files |
| A modern browser with DevTools | Run the app, inspect components, watch renders |
| Obsidian (this vault) | Keep your notes, cheatsheets and exercises in one place |

---

## 🗺️ Course Map

| # | Note | Lessons | What you learn |
| --- | --- | --- | :--- |
| 00b | [00b - React Cheatsheet](./00b%20-%20React%20Cheatsheet.md) | — | JSX, components, props, state, events |
| 00c | [00c - React Cheatsheet II](./00c%20-%20React%20Cheatsheet%20II.md) | — | Forms, hooks, context, fetching, routing, styling |
| 01 | [01 - The Rebirth](./01%20-%20The%20Rebirth.md) | 01–05 | What React is, its history, declarative design, before vs. with |
| 02 | [02 - Spawn Point](./02%20-%20Spawn%20Point.md) | 01–07 | Node, npm, Vite, hot reloading, project structure, `createRoot` |
| 03 | [03 - Glyph Workshop](./03%20-%20Glyph%20Workshop.md) | 01–06 | JSX, transpilation, `React.createElement`, component syntax |
| 04 | [04 - Living Markup](./04%20-%20Living%20Markup.md) | 01–08 | Single root, fragments, expressions, conditionals, attributes |
| 05 | [05 - Building Blocks](./05%20-%20Building%20Blocks.md) | 01–05 | Functional components, PascalCase, export/import, composition |
| 06 | [06 - The Skill Tree](./06%20-%20The%20Skill%20Tree.md) | 01–06 | Composition, hierarchy, parent-child, one-way data flow |
| 07 | [07 - Trade Routes](./07%20-%20Trade%20Routes.md) | 01–06 | Props, `.map()` lists, state as props, component lists |
| 08 | [08 - The Health Bar](./08%20-%20The%20Health%20Bar.md) | 01–06 | `useState`, setter, immutability, timers, functional updates |
| 09 | [09 - The Controller](./09%20-%20The%20Controller.md) | 01–06 | Synthetic events, onClick, event object, hover, focus, keyboard |
| 10 | [10 - The Forge](./10%20-%20The%20Forge.md) | 01–07 | Forms, htmlFor, onChange, onSubmit, controlled components |
| 11 | [11 - The Relic System](./11%20-%20The%20Relic%20System.md) | 01–06 | Hooks, useEffect, cleanup, useRef, state vs. refs |
| 12 | [12 - The Guild Ledger](./12%20-%20The%20Guild%20Ledger.md) | 01–06 | Prop drilling, Context API, providers, useContext |
| 13 | [13 - The Courier](./13%20-%20The%20Courier.md) | 01–06 | fetch, promises, loading, errors, list filtering |
| 14 | [14 - The World Map](./14%20-%20The%20World%20Map.md) | 01–06 | SPAs, react-router-dom, BrowserRouter, Routes, Link, useNavigate |
| 15 | [15 - The Final Boss](./15%20-%20The%20Final%20Boss.md) | 01–07 | Capstone quiz SPA: architecture, logic, routes, styling |

---

## 🎮 Practice Philosophy

Code is a machine you build by typing. The exercises keep that principle: every snippet runs
as written — the comments state the output you should actually get. When something looks
wrong, open DevTools, find the component in the Components tab, and compare the real
props and state with the ones you expected.

Every chapter ends with side quests that combine the chapter's concepts into one feature —
the guild HUD, the social post, the arena RSVP button, the bestiary search, the class
quiz — so nothing stays as isolated trivia.

---

## 🔗 See Also

- [🟨 JavaScript MOC](../%F0%9F%9F%A8%20JavaScript/README.md) — the language React is written in; prerequisite
- [🌐 HTML MOC](../%F0%9F%8C%90%20HTML/README.md) — the structure React replaces the DOM of
- [🎨 CSS MOC](../%F0%9F%8E%A8%20CSS/README.md) — the styling half of the same pages
- [🟣 CSharp MOC](../%F0%9F%9F%A3%20CSharp/README.md) — the strongly typed counterpart, same game-first framing

---
