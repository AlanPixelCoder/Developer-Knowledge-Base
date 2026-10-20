# 07. Trade Routes

**Spanish version:** [07 - Rutas Comerciales.md](07%20-%20Rutas%20Comerciales.md)

**Course:** React
**Topic:** props, passing props, receiving props, props as any JavaScript type, rendering lists with `.map()`, state as props, component lists and state mapping
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-01_--_06-7C5CFF?style=for-the-badge" alt="Lessons">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Caravans move goods between Emberfall's outposts; **props** move data between your
components. The tree from [[06 - The Skill Tree]] gave every component a place — this
chapter gives them a voice. By the end you will pass props into notifications and menus,
render whole catalogs with `.map()`, hand state down as props, and build a relic gallery
that maps data into components. Reference: [[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> **Props** (short for *properties*) are data fragments delivered to JSX elements and
> components — the mechanism for React's **one-way** parent → child information flow — and
> they can be any JavaScript type: strings, booleans, objects, functions.

---

## 01. Caravans of Data

> [!NOTE]
> **Key information**
> Props are the data fragments you hand to JSX elements and components, and the only
> sanctioned road for **one-way** parent → child information flow. A parent packages data;
> the child receives it and renders it.

Two facts keep the caravans honest:

- **Props are read-only.** A child never edits the props it receives — it displays them.
  Changing data means changing it at the parent, which then re-renders the child (the
  one-way rule from [[06 - The Skill Tree]]).
- **Everything is a prop.** The attributes you have used all along — `src`, `alt`, `href`,
  `id` — are props of plain HTML elements. Your own components simply add new ones.

```js
// Props on a plain HTML element
<img src="/avatar.png" alt="Avatar" />

// Props on your own component
<Notification message="Raid tonight" isRead={true} />
```

---

## 02. Sending a Parcel

### Passing Props

Props are written **exactly like HTML attributes**, on the opening tag, separated by
spaces:

```js
<Notification message="GuildMasterVex's feast is today!" isRead={true} />
```

- `message="..."` — a **string**, written in quotes, just like `alt` or `src`.
- `isRead={true}` — a **boolean**, written in curly braces because `{true}` is a JavaScript
  expression.

### Any JavaScript Type Travels the Route

Curly braces `{ }` open the route to every type JavaScript has:

| Type | How it is passed | Example |
| :--- | :--- | :--- |
| **String** | quotes or braces | `message="GuildMasterVex's feast is today!"` |
| **Boolean** | literal inside braces | `isRead={true}` |
| **Number** | literal inside braces | `attendees={120}` |
| **Object / array** | expression inside braces | `event={{ title: "Arena Night" }}` |
| **Function** | reference **without** parentheses | `onRead={markAsRead}` |

> [!WARNING]
> **The mistake everyone makes once**
> Writing `isRead="false"` — a non-empty string is **truthy**, so the component sees
> `true`. Strings lie about booleans; use `{false}`. And never write `onRead={markAsRead()}`
> with parentheses: that **calls** the function during render instead of passing it.

### Quest: Two Labels

Send a `Notification` with three props: a `message` string about tonight's arena
tournament, `isRead={false}`, and a number prop `attendees={64}`. Then guess what the
child logs when you `console.log(props)` — and check in the next section.

---

## 03. Opening the Parcel

### Receiving Props

A component receives props as its **single parameter**, conventionally named `props` —
and `props` is an object:

```js
function GuildCanteen(props) {
  console.log(props);
  return (
    <div className="menu-card">
      <h2>{props.dish}</h2>
      <p>{props.description}</p>
    </div>
  );
}
```

Used from a parent:

```js
<GuildCanteen dish="Ember Stew" description="Restores 40 HP. Served hot." />
```

What `console.log(props)` prints is one object:

```json
{ "dish": "Ember Stew", "description": "Restores 40 HP. Served hot." }
```

Three rules of the parcel:

1. **One parameter.** Whatever the number of props, they arrive together in that single
   object.
2. **Dot access.** `props.dish`, `props.description` — the same property access you know
   from plain JavaScript.
3. **Curly braces to read.** Inside JSX, `{props.dish}` evaluates the expression and
   prints the value.

> [!TIP]
> Destructuring is the shortcut: `function GuildCanteen({ dish, description }) { ... }`
> unpacks the object in the parameter list. The data arriving is identical — it is just
> unpacked before you use it.

---

## 04. The Catalog Caravan

### Rendering Lists with `.map()`

A storefront is the same card fifty times. Instead of fifty copies of JSX, you keep one
template and let **`.map()`** stamp it once per item — the array method from the
JavaScript vault, now driving markup:

```js
const catalogItems = [
  { name: "Ember Shard", category: "Crafting" },
  { name: "Warden's Lantern", category: "Gear" },
  { name: "Ashen Blade", category: "Weapon" },
];

export default function Catalog() {
  return (
    <div>
      {catalogItems.map(function (item) {
        return (
          <div>
            <h2>{item.name}</h2>
            <h3>Specialty: {item.category}</h3>
          </div>
        );
      })}
    </div>
  );
}
```

Read it as a transaction: **for each `item` in `catalogItems`, return this block of
markup** — and `.map()` collects all the returned blocks into an array of elements React
renders in order.

> [!TIP]
> Add a `key` to the outermost element of each returned block — `key={item.name}` — and
> React can tell the siblings apart when the list changes. The console reminds you if you
> forget; the rest of the pattern stays exactly the same.

### Quest: Restock the Shelves

Grow `catalogItems` to five items and add a third line per card: `<p>{item.category}</p>`.
Confirm that five cards appear from one template — then delete two items from the array
and watch two cards disappear. The template never changed; the data did.

---

## 05. The Shared Scoreboard

### State as Props

Props get interesting when the data at the top is **state**. The `Game` component owns
the scores; the `Player` children only receive them:

```js
import React, { useState } from "react";
import Player from "./Player.js";

export default function Game() {
  const [scores, setScores] = useState([0, 0, 0]);

  return (
    <div>
      <Player score={scores[0]} />
      <Player score={scores[1]} />
      <Player score={scores[2]} />
    </div>
  );
}
```

```js
export default function Player(props) {
  return (
    <div className="player-row">
      <span>Score: {props.score}</span>
    </div>
  );
}
```

One `useState([0, 0, 0])` at the top, three `<Player score={...} />` caravans below. The
benefits are the two pillars of prop-driven design:

- **Reusability** — `Player` stays **abstract**. It renders whatever number arrives in
  `props.score`; it does not know, or care, whether it is player one or player three.
- **Single source of truth** — the scores live in **one** place. The day `Game` calls
  `setScores`, the parent re-renders, and every child re-renders with the fresh numbers.
  No child keeps a private copy that can drift out of sync.

---

## 06. The Relic Gallery

### Component Lists and State Mapping

The final pattern combines everything in this chapter: a **list component** receives an
array through props, `.map()`s it into **child components**, and each child renders its
own slice of the data. The old movie-gallery shape, rethemed to an item catalog:

| Movie gallery | Emberfall relic gallery |
| :--- | :--- |
| `<TrendingList>` | `<RelicList>` |
| `props.movies` | `props.relics` |
| `<Movie title releaseYear imageUrl />` | `<Relic name rarity imageUrl />` |

The list component does the mapping:

```js
import React from "react";
import Relic from "./Relic.js";

export default function RelicList(props) {
  return (
    <div className="relic-list">
      {props.relics.map(function (relic) {
        return (
          <Relic
            name={relic.name}
            rarity={relic.rarity}
            imageUrl={relic.imageUrl}
          />
        );
      })}
    </div>
  );
}
```

The child receives through `props` and renders each field:

```js
export default function Relic(props) {
  return (
    <div className="relic-card">
      <img src={props.imageUrl} alt={props.name} />
      <h3>{props.name}</h3>
      <p>Rarity: {props.rarity}</p>
    </div>
  );
}
```

The caravan arrives in three hops: `App` → `RelicList` (the array) → each `Relic` (one
relic's worth of data). One `.map()`, one template per card, zero duplicated markup.

### Quest: Fifth Relic

Add a fourth relic to the array and render the list with
`<RelicList relics={relicItems} />`. Then give `Relic` a new prop — `origin` — and print
it under the rarity. Only two files change: the parent that packages the parcel, and the
child that opens it.

---

## ⚡ XP Earned: Key Takeaways

- 📦 **Props** are data fragments delivered to JSX elements and components — React's
  **one-way** parent → child road.
- ✍️ Pass props like HTML attributes; read them in the child as `props.name` inside `{}`
  braces.
- 🧳 Any JavaScript type travels: strings, booleans, numbers, objects, functions — curly
  braces for everything that is not a plain string.
- 🚫 Props are **read-only**; children display, parents decide.
- 🔁 `{items.map(function (item) { return <Card />; })}` stamps one element per item.
- 🏆 State passed down as props gives you reusability and a **single source of truth**.

---

## 🎁 Loot Table: Real-World Use Cases

- 🔔 Notifications, toasts and badges fed by props from a central store
- 🛒 Product and catalog grids rendered with `.map()` from one card template
- 🏆 Scoreboards, leaderboards and player lists — state at the top, numbers below
- 🎨 Theme and size variants: one `<Button color="ember" size="lg" />` component, many looks
- 🧾 Form fields rendered from a config array (`label`, `type`, `placeholder` as props)

---

## 🎮 Side Quests: Practice Exercises

1. Give `Notification` a fourth prop `type="raid"` and render it as a badge in the child.
2. Write a `HealthBar` component that receives `current` and `max` props and renders both
   numbers.
3. Convert your catalog into a `.map()` over an array of four items — no duplicated cards.
4. Extend `Game` to four players by adding `<Player score={scores[3]} />` and a fourth
   initial score.
5. **Boss fight:** build a `<GuildRoster members={memberList} />` where `members` is an
   array of objects (`{ name, className, level }`), mapped into a `<MemberCard>` child that
   renders all three fields through props — array in, component list out.

---

## 🔗 See Also

- [[00b - React Cheatsheet]] — props syntax, passing and `.map()` on one page
- [[05 - Building Blocks]] — previous chapter: the components these parcels travel between
- [[06 - The Skill Tree]] — previous chapter: the parent-child tree props run down
- [[08 - The Health Bar]] — next chapter: state, the data that changes on its own
- [[09 - The Controller]] — later: passing functions as props to handle real events
- [[04 - Living Markup]] — expressions inside `{}` and conditional rendering beside your lists

---
