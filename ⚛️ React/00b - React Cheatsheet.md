# 00b. React Cheatsheet

**Spanish version:** [00b - Chuleta de React.md](00b%20-%20Chuleta%20de%20React.md)

**Course:** React
**Topic:** Quick reference for the core toolkit: JSX, components, composition, props, state and events
**Tags:** `#react` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Beginner to intermediate">
  <img src="https://img.shields.io/badge/Covers-Chapters_01_--_09-7C5CFF?style=for-the-badge" alt="Chapters 01 to 09">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

One page for the whole core toolkit — JSX, components, composition, props, state and
events. Every statement here was introduced in [[01 - The Rebirth]] through
[[09 - The Controller]] — nothing on this sheet is new. Forms, hooks, context, data
fetching and routing live in [[00c - React Cheatsheet II]].

> [!TIP]
> Print it, or keep it in a split pane next to your editor. A page written without checking
> this sheet is how prop soup happens: passing data nobody receives, because nothing on the
> sheet looked wrong.

**The running theme of this module: Emberfall**, the companion site for a roguelike of the
same name. Every exercise builds part of it: the guild HUD, the social post, the relic
catalog, the bestiary search, the class quiz. The code is the same code a real studio
ships — only the words change.

---

## ⚛️ React in 30 Seconds

**React** is an open-source JavaScript **library**, introduced in **2013** by a small team
at **Facebook** (Jordan Walke) to power the Newsfeed. It is **declarative** (you describe
what the UI should look like for a given state) and **component-based** (the UI is a tree
of reusable functions).

```js
// The root mount — one per app, from react-dom/client
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

```text
my-app/
├── index.html      ← hosts <div id="root"></div>
├── package.json    ← "react" + "react-dom" live here
├── vite.config.js
└── src/
    ├── App.jsx
    └── index.css
```

| Concept | Rule |
| :--- | :--- |
| Declarative | Describe the output for a state; React handles the DOM diff |
| Component-based | UI = a hierarchy of small functions returning markup |
| `react` | The engine: components, hooks, the virtual DOM |
| `react-dom` | The DOM adapter: `createRoot`, the bridge to the browser |

---

## 🧬 JSX at a Glance

**JSX** (JavaScript Syntax Extension) is sugar over `React.createElement` calls. Browsers
cannot run it directly — a transpiler (**Babel**, **SWC**, **esbuild**) converts it first.

| JSX | Transpiles to |
| :--- | :--- |
| `<h1 id="welcome">Welcome!</h1>` | `React.createElement("h1", { id: "welcome" }, "Welcome!")` |
| `<EmberBanner title="Season 4" />` | `React.createElement(EmberBanner, { title: "Season 4" })` |

```js
export default function App() {
  return (
    <div>
      <h1>Hello, Emberfall!</h1>
    </div>
  );
}
```

- Lives in `.js` or `.jsx` files (`.jsx` signals JSX to compiler and reader).
- Wrap multi-line JSX in parentheses `( )` so Automatic Semicolon Insertion cannot sever the `return`.

---

## 🏷️ Living Markup

### Expressions

Anything in curly braces `{ }` — any JS expression resolving to a single value:

```js
const relicName = "Ember Shard";
const dropRate = 0.05;
<h2>{relicName}</h2>
<p>Drop rate: {dropRate * 100}%</p>
```

### Conditional Rendering

| Shape | Use it when |
| :--- | :--- |
| `if / else` into a variable, render `{page}` | The branches are big |
| `{signedIn ? <Dashboard /> : <SignIn />}` | Two exclusive alternatives |
| `{signedIn && <Dashboard />}` | Show something, or show nothing |

### Attributes

Static strings like HTML (`src`, `alt`, `href`, `id`); dynamic values in braces. And
because `class` is a reserved JS keyword, JSX uses **`className`**:

```js
const avatarUrl = "/avatar.png";
<img src={avatarUrl} alt="Guild avatar" />
<button className="forge-button">Heat the metal</button>
```

---

## 🧩 Components & Composition

```js
import React from "react";

export default function Greetings() {
  return (
    <div>
      <h1>Welcome back, Warden!</h1>
    </div>
  );
}
```

| Rule | Why |
| :--- | :--- |
| **PascalCase** names | React tells your components apart from HTML tags |
| **Single root element** | Wrap siblings in a `<div>` or a Fragment `<>...</>` |
| **`export default`** | Makes the component importable from other files |
| Use as `<Greetings />` | Self-closing; instantiation happens where it is rendered |
| JSX comments `{/* ... */}` | The only comment syntax that lives inside markup |

**Composition** = nesting small components into a hierarchy — data flows **parent → child**,
one way, from a single root:

```text
App (root)
 └── Post (card)
      ├── FollowButton
      └── LikeButton
```

---

## 📦 Props

**Props** are data fragments delivered to components — the mechanism for one-way
parent → child flow. Any JS type: strings, booleans, objects, functions.

```js
// Passing — quotes for strings, braces for everything else
<Notification message="GuildMasterVex's feast is today!" isRead={true} />

// Receiving — one parameter, conventionally props
function Notification(props) {
  return <p>{props.message}</p>;
}
```

### Lists with `.map()`

```js
{relicList.map(function(relic) {
  return (
    <div key={relic.name}>
      <h2>{relic.name}</h2>
      <h3>Rarity: {relic.rarity}</h3>
    </div>
  );
})}
```

| Pattern | Shape |
| :--- | :--- |
| State as props | Parent holds `scores`; children receive `<Player score={scores[0]} />` |
| Component lists | Parent maps data → `<Relic name rarity imageUrl />`; child renders `props.name` etc. |
| `key` | A stable id per item — lets React match old and new rows |

---

## 🧮 State

**State** is internal data expected to change (HP, potion counts, form entries). `useState`
returns `[value, setter]`; **any setter call re-renders** the component.

```js
import React, { useState } from "react";

function HealthBar() {
  const [hp, setHp] = useState(80);
  return <h1>HP: {hp}</h1>;
}
```

| Rule | Wrong | Right |
| :--- | :--- | :--- |
| Never mutate state | `hp = 50;` | `setHp(50);` |
| New value from old | `setHp(hp - 10);` | `setHp((prevHp) => prevHp - 10);` |
| Arrays/objects | `items.push(x)` | `setItems([...items, x])` |

The functional form `(prev) => ...` always reads the freshest state — mandatory inside
timers and batched updates. Initial value can be any JS type; it is set **once**, on mount.

---

## 🖱️ Events

React wraps native events in a **synthetic event system** for cross-browser consistency.
Handlers are **camelCase** and take the function itself — **no parentheses**, or they run
on render.

```js
function handleClick(e) {
  console.log(e.target); // the DOM element that triggered it
}
return <h1 onClick={handleClick}>Click me!</h1>;
```

| Event | Fires when | Typical use |
| :--- | :--- | :--- |
| `onClick` | Click | Buttons, toggles |
| `onMouseOver` / `onMouseLeave` | Pointer enters / leaves | Tooltips |
| `onFocus` / `onBlur` | Element gains / loses focus | Validation, highlights |
| `onKeyDown` / `onKeyUp` | Key pressed / released | Shortcuts, volume keys |

- Non-focusable elements (`<div>`, `<img>`) need **`tabIndex={0}`** before they can fire focus events.
- Inline styles are objects with **camelCase** properties: `e.target.style.backgroundColor = "yellow"`.
- Keyboard identity lives in **`e.key`**: `e.key === "ArrowUp"`, `e.key === "Enter"`, `e.key === " "`.

```js
// Keyboard + accessibility in one widget
<button
  tabIndex="0"
  onClick={handleGoing}
  onKeyDown={function(e) { if (e.key === "Enter") handleGoing(); }}
>
  Attend arena night ({goingCount})
</button>
```

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| `class=` in JSX | Silently ignored — use `className=` |
| `onClick={handle()}` | Calls on render; pass `onClick={handle}` |
| Mutating state directly | UI goes stale — the setter is what re-renders |
| Missing `key` in `.map()` | React warns; list updates misbehave |
| Lowercase component `<relic />` | Treated as an HTML tag, not your function |
| Returning adjacent siblings | Syntax error — wrap in one root or `<>...</>` |
| Prop name typos | No error — the prop is simply `undefined` |

---

## 🔗 See Also

- [[00c - React Cheatsheet II]] — forms, hooks, context, fetch and routing
- [[01 - The Rebirth]] — what React is, where this sheet begins
- [[06 - The Skill Tree]] — composition and the component hierarchy
- [[09 - The Controller]] — events, the last stop on this sheet

---
