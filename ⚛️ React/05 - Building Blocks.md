# 05. Building Blocks

**Spanish version:** [05 - Bloques de Construcción.md](05%20-%20Bloques%20de%20Construcci%C3%B3n.md)

**Course:** React
**Topic:** functional components, component naming rules, PascalCase, export & import, composing components, defining vs instantiating, JSX comments
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-01_--_05-7C5CFF?style=for-the-badge" alt="Lessons">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

The Emberfall companion site is not one screen — it is dozens of small pieces: a health
widget, a quest row, a follow button, a greeting banner. Until now you have been gluing
raw JSX into a single file. This chapter introduces the **building blocks** React is
actually made of: **functional components** — reusable units you name, export, import and
render like stamps in a workshop. By the end you will have forged a `Greetings` component
and summoned it from `App`. Quick reference for everything here:
[[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A React component is a plain JavaScript function named in **PascalCase** that returns
> JSX, is shipped with `export default`, and is summoned into another component with an
> import plus a self-closing tag like `<Greetings />`.

---

## 01. The Building Yard

> [!NOTE]
> **Key information**
> Components are React's **primary building blocks** of the user interface. JSX is the
> visual language; components are the **functional units**. A functional component is a
> JavaScript function that returns JSX — React renders any function whose name starts with
> a capital letter as if it were an HTML tag.

Every screen of the guild dashboard is a stack of these units. The separation of concerns
is simple:

| Layer | Job | Example |
| :--- | :--- | :--- |
| **JSX** | Describes what the interface **looks like** | `<h1>Welcome!</h1>` |
| **Component** | Wraps a piece of interface you can **reuse and name** | `function Greetings() { ... }` |

The rules of JSX from [[03 - Glyph Workshop]] and the expressions from
[[04 - Living Markup]] all live **inside** a component's `return`. Components are the crates
those rules ship in: one component, one job, one file.

> [!TIP]
> Think of components as prefabs. The health bar, the quest card and the avatar header are
> built once and stamped anywhere they are needed — change the prefab and every instance
> on the site updates.

---

## 02. The Naming Rites

### The Three Key Rules

> [!NOTE]
> **Key information**
> Three rules decide whether React accepts your component: **PascalCase** naming (React
> distinguishes components from HTML tags by the capital first letter), a **single root
> element** per return, and **`export default`** for module access.

| Rule | Requirement | Why it exists |
| :--- | :--- | :--- |
| **PascalCase** | `Greetings`, never `greetings` | React tells components apart from HTML tags by that capital letter |
| **Single root element** | One root per `return`; wrap siblings in a `<div>` or a Fragment | A return can only expose one tree — the rule from [[04 - Living Markup]] |
| **`export default`** | `export default function Greetings() { ... }` | Gives other files module access to the component |

### Quest: Name Check

Audit three names before React does: `guildHeader` (lowercase — React would read it as an
HTML tag), `guild_header` (snake_case — a naming style React components never use) and
`GuildHeader` (PascalCase — the only one that ships). Rename your last component to
PascalCase and confirm the tag you write in JSX matches it **character for character**.

> [!WARNING]
> **The mistake everyone makes once**
> Write `<greetings />` in lowercase and React does not complain — it treats `greetings`
> as an unknown HTML element and renders nothing useful. Same trap on the other side:
> define a component and forget `export default`, import it, and the import is
> `undefined`. The two failures are silent until you stare at a blank screen.

---

## 03. The First Forge

### Building `Greetings`

Time to forge. One component, one file, all three rules applied:

```js
import React from "react";

export default function Greetings() {
  return (
    <div>
      <h1>Welcome back, Warden of the Ninth!</h1>
      <p>The Deep Halls raid queue is open.</p>
    </div>
  );
}
```

Anatomy of the file:

- `import React from "react";` — the standard opening line of a component file.
- `export default function Greetings() { ... }` — the function **is** the component, and
  the export hands it to every other file in the project.
- `return ( ... );` — the parentheses keep the multi-line JSX from being cut off by
  automatic semicolon insertion, exactly as in [[03 - Glyph Workshop]].
- The `<div>` root satisfies the single-root rule; the `<h1>` and `<p>` ride inside it.

### Quest: Herald

Write a second component called `QuestStatus` that reports today's progress. Keep it
PascalCase, single-rooted and exported:

```js
export default function QuestStatus() {
  return (
    <div>
      <h2>Daily Quests</h2>
      <p>3 of 5 completed</p>
    </div>
  );
}
```

Two files, two components, zero shared code — and neither one can run on its own. That is
the point: components are built to be **used**, which is the next section.

---

## 04. Summoning Circle

### Importing and Composing

A component becomes useful only when another component renders it. `App.js` imports
`Greetings` and drops it into its markup with a **self-closing tag**:

```js
import Greetings from "./Greetings.js";

export default function App() {
  return (
    <div>
      <Greetings />
    </div>
  );
}
```

The mechanics:

- The import path `"./Greetings.js"` points at the file where the component lives.
- The imported name must match the exported name, **including the capital**.
- `<Greetings />` is self-closing — components take no closing tag when they have no
  children, just like `<img />` or `<br />`.
- Rendering a component inside another is called **composition**: `App` now *contains*
  `Greetings`.

### Quest: Full Roster

Compose both of your components in `App` — the greeting first, the quest tracker under it:

```js
import Greetings from "./Greetings.js";
import QuestStatus from "./QuestStatus.js";

export default function App() {
  return (
    <div>
      <Greetings />
      <QuestStatus />
    </div>
  );
}
```

Save the file and the dev server prints both blocks. You never edited `Greetings` to put
it on the page — you **placed** it, and React did the rest.

---

## 05. Define and Summon

### Two Halves of the Same Rune

Every component in React passes through the same three-step flow. **Defining** creates the
component; **instantiating** is the act of putting it on screen — and they happen in
different files:

1. **Export the component** — `export default function FunctionComponent() { ... }` in its
   own file. Nothing renders yet.
2. **Import it** — `import FunctionComponent from "file/path/to/FunctionComponent.js";`
   in the file that needs it. Still nothing renders.
3. **Render it** — write `<FunctionComponent />` inside another component's markup. Now it
   is on screen.

```js
// 1. Define and export — FunctionComponent.js
export default function FunctionComponent() {
  return <div>I exist once someone renders me.</div>;
}

// 2. Import — from "file/path/to/FunctionComponent.js"
import FunctionComponent from "file/path/to/FunctionComponent.js";

// 3. Instantiate — inside another component's return
export default function App() {
  return (
    <div>
      <FunctionComponent />
    </div>
  );
}
```

An unused exported component costs nothing; a component that is never exported cannot be
imported at all. Definition without instantiation is a prefab still sitting in the yard.

### Commenting Inside Markup

Inside JSX, plain `//` comments are **syntax errors** — the parser is reading markup, not
JavaScript. JSX comments live inside curly braces, wrapped in a block comment:

```js
export default function Greetings() {
  return (
    <div>
      {/* This line never reaches the DOM */}
      <h1>Welcome back, Warden of the Ninth!</h1>
    </div>
  );
}
```

Outside the markup — above the function, between imports — normal `//` and `/* ... */`
comments work as they always have. Rule of thumb: **inside the tags, use `{/* ... */}`.**

---

## ⚡ XP Earned: Key Takeaways

- 🧱 Components are React's **primary building blocks**: JSX is the visual language,
  components are the functional units.
- 🏷️ **PascalCase** is how React tells your components from HTML tags — lowercase names
  render as unknown elements.
- 📦 One **root element** per return; `export default` is what makes a component
  importable.
- 🗡️ `<Greetings />` is a self-closing **instantiation** — placing a defined component on
  screen.
- 🔁 The flow is always **define → import → render**, in three different steps.
- 💬 `{/* ... */}` is the only comment syntax that survives inside JSX markup.

---

## 🎁 Loot Table: Real-World Use Cases

- 🧩 Reusable UI kits: buttons, cards, badges and avatars defined once, used across pages
- 🏗️ Design systems — a component library is a yard full of exported prefabs
- 🧱 Feature slicing: each team ships its own component file and composes it at the root
- ♻️ Copy-free layouts — the same `Post` stamped into a feed, a profile and a preview
- 📝 Readable JSX — `<GuildHeader />` says more than fifty lines of nested markup

---

## 🎮 Side Quests: Practice Exercises

1. Rename every component in this chapter to camelCase, render it, and observe what React
   does with a lowercase tag.
2. Write a `HealthBar` component with a single root `<div>` and render it from `App`.
3. Split your `App` into three components (`Header`, `Feed`, `Footer`) and compose all
   three with imports and self-closing tags.
4. Add a `{/* ... */}` comment inside each component's markup and confirm nothing reaches
   the rendered page.
5. **Boss fight:** build a `GuildRoster` component that renders a `Greetings` **and** a
   `QuestStatus`, then import `GuildRoster` into `App` — a component that summons other
   components, three levels deep, with every name in PascalCase.

---

## 🔗 See Also

- [[00b - React Cheatsheet]] — component anatomy and rules on one page
- [[03 - Glyph Workshop]] — previous chapter: JSX, the language components speak
- [[04 - Living Markup]] — previous chapter: what goes inside a component's `return`
- [[06 - The Skill Tree]] — next chapter: composing components into hierarchies
- [[07 - Trade Routes]] — later: sending data into components with props
- [[08 - The Health Bar]] — later: components that remember things with state

---
