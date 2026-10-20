# 06. The Skill Tree

**Spanish version:** [06 - El Árbol de Habilidades.md](06%20-%20El%20%C3%81rbol%20de%20Habilidades.md)

**Course:** React
**Topic:** component composition, component hierarchy, parent-child relationships, one-way data flow, building the guild post, final assembly
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

A single component is a brick. The Emberfall guild feed — avatar, username, caption,
follow button, like button — is a **wall**, and walls are built by stacking bricks in a
chosen order. This chapter is about **composition**: combining small specialized
components into hierarchical structures, and understanding the parent-child tree that
every React app secretly is. By the end you will have assembled the full `Post` card,
file by file. Reference: [[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> React interfaces are **trees**: a single root component (`App`) parents every other
> component, small specialized components nest inside larger ones, and data always travels
> **downhill** — from parent to child, never the other way around.

---

## 01. The Composition Ritual

> [!NOTE]
> **Key information**
> **Composition** is the act of combining small, specialized components into hierarchical
> structures. Instead of one file containing the whole page, each component owns one job
> and larger components are built by nesting smaller ones inside their markup.

The benefits are the ones you already met in [[05 - Building Blocks]], now multiplied:

- **One job per component.** A `LikeButton` that only likes is easier to write, test and
  reuse than a page-sized function that likes, follows and fetches.
- **Swappable pieces.** Replace the follow button with a "message" button and the `Post`
  does not care.
- **Shared vocabulary.** Every developer on the guild site says `Post`, `Header`,
  `Button` — and means the same file.

The structure that results is never flat. It is always a tree with exactly one root.

---

## 02. Reading the Skill Tree

### The Guild Post Hierarchy

Here is the hierarchy of the post you are about to build:

```text
App (Top-Level Container)
 └── Post (Card Container)
      ├── FollowButton (Action Widget)
      └── LikeButton (Interactive Toggle)
```

Read it like a skill tree in reverse — everything unlocks **from the root outward**:

| Node | Role | Children |
| :--- | :--- | :--- |
| **App** | Top-level container; the root of the whole application | `Post` |
| **Post** | Card container: avatar, username, caption | `FollowButton`, `LikeButton` |
| **FollowButton** | Action widget: follow / unfollow | none |
| **LikeButton** | Interactive toggle: like count and heart | none |

Two vocabulary terms you will hear in every React codebase:

- **Parent** — a component that renders another one. `Post` is the parent of both buttons.
- **Child** — a component rendered **inside** another. `LikeButton` is a child of `Post`.

A component can be a parent and a child at the same time: `Post` is the child of `App`.

### Quest: Map Your Own Tree

Draw the tree for the Emberfall quest feed before writing any code: a root `QuestFeed`
container, one `QuestRow` card per quest, and inside each row a `RewardBadge` and a
`ClaimButton`. Write the four names in PascalCase and connect them with `└──` and `├──`
exactly as above. If you cannot point at the root with one finger, the tree is wrong.

---

## 03. Forging the Post

### `Post.js`

The card container. It imports both widgets, renders the post metadata in the header, and
lets the buttons do their own work in the footer:

```js
import React from "react";
import FollowButton from "./FollowButton.js";
import LikeButton from "./LikeButton.js";

export default function Post() {
  return (
    <div className="post-container">
      <header>
        <img src="/avatar.png" alt="Avatar" />
        <h2>WardenOfTheNinth</h2>
        <FollowButton />
      </header>
      <p>Cleared the Deep Halls without a single torch.</p>
      <footer>
        <LikeButton />
      </footer>
    </div>
  );
}
```

What each line is doing:

- The two imports are the **edges** of the tree — this is composition happening at the top
  of the file.
- `className="post-container"` is the styling hook (JSX uses `className`, not `class`).
- `<img src="/avatar.png" alt="Avatar" />` is a static attribute exactly as in HTML.
- `Post` never explains **how** to follow or like — it only decides **where** those widgets
  appear. That indifference is what makes the buttons reusable.

> [!WARNING]
> **The mistake everyone makes once**
> Writing the buttons' markup inline inside `Post` "just for now". Two files later the
> same button is needed on the profile page, and you are copying JSX between files. Build
> the widget as its own component **first**, then place it.

---

## 04. The Root Warden

### `App.js`

The top-level container hosts the post. Nothing more — the root's job is to sit at the top
and render what belongs on screen:

```js
import React from "react";
import Post from "./Post.js";

export default function App() {
  return (
    <div>
      <Post />
    </div>
  );
}
```

`App` imports `Post` and instantiates it with the self-closing tag from
[[05 - Building Blocks]]. React renders `App`, React renders `Post`, and React renders the
two buttons inside — one traversal of the tree, top to bottom.

### Quest: Second Seat

Add a second `<Post />` under the first one and save. Two identical cards appear, side by
side — two instances of the same component, one definition. Then delete the second one:
composition is cheap, and so is undoing it.

---

## 05. Final Assembly

### Checkpoint: Chapter Recap

- **Composition** = combining small specialized components into hierarchical structures.
- Every React app is a tree with **one root**; parents render children.
- `Post` aggregates the metadata and the buttons; it never implements the widgets itself.
- Data flows **parent → child** only — the subject of the next section.

### The Finished File Tree

```text
App.js
 └── Post.js
      ├── FollowButton.js
      └── LikeButton.js
```

Each file, its role:

| File | Role in the tree |
| :--- | :--- |
| `App.js` | Root that hosts `<Post />`; the entry point of the whole component tree |
| `Post.js` | Aggregates the post metadata — avatar, username, caption — and both buttons |
| `FollowButton.js` | Owns the follow / unfollow toggle state for this post |
| `LikeButton.js` | Owns the like count and the heart animation for this post |

The arrows in that tree are not decoration: they are the direction React allows data to
travel. That constraint is the whole subject of section 06 — and of the next chapter.

---

## 06. Downhill Only

### The Parent-Child Architecture

React components form an **inverted tree**: one root at the top, branches spreading
downward. `<App>` is the parent of everything; each generation below is a child of the one
above:

```text
        <App>            ← parent of Post
          │
        <Post>            ← child of App, parent of the buttons
        /    \
<FollowButton> <LikeButton>   ← children of Post
```

### The One-Way Rule

> [!NOTE]
> **Key information**
> Data flows **only from parent to child** — one-way data flow. A parent can hand
> information down to a child; a child can never reach up and rewire its parent. When a
> parent's data changes, React re-renders the parent, and the new render trickles down the
> whole branch.

In practice that means:

- The **parent owns the truth**; children display what they are given.
- Siblings never talk to each other directly — they share a parent.
- To change something high in the tree, you change it **high in the tree**.

The formal mechanism for handing data downhill is called **props**, and it is the entire
subject of [[07 - Trade Routes]]. The mechanism for a component remembering its own
changes — the follow toggle, the like count — is **state**, covered in
[[08 - The Health Bar]].

> [!TIP]
> **Game dev version**
> Every game HUD is the same tree. The root screen is `App`; the health panel, the minimap
> and the quest tracker are containers; the individual bars, pips and rows are widgets. If
> you have ever parented a widget to a screen in an engine's UI editor, you already know
> React's architecture — the direction of the arrows is the only new part.

---

## ⚡ XP Earned: Key Takeaways

- 🌳 **Composition** combines small specialized components into hierarchical structures.
- 📁 One component per job, one file per component — swap widgets without touching the card.
- 🌲 Every React app is an **inverted tree** with exactly one root: `<App>`.
- 👨‍👦 **Parent** renders **child**; a component can be both at once.
- ⬇️ Data flows **parent → child only**; siblings communicate through their parent.
- 🧱 `Post` aggregates metadata and widgets — it never reimplements them.

---

## 🎁 Loot Table: Real-World Use Cases

- 📰 Social feeds — every card on every timeline is a `Post`-style container with widgets
- 🎮 HUD layouts: root screen → panels → bars, pips and rows, exactly this tree
- 🛍️ Product cards: image, title and price composed from smaller reusable pieces
- 🧰 Design systems built as component trees instead of copy-pasted markup
- 👥 Team scale — many developers owning leaf components while one owns the root

---

## 🎮 Side Quests: Practice Exercises

1. Redraw the guild post hierarchy from memory, then compare it with the tree in section 02.
2. Write `FollowButton.js` and `LikeButton.js` as standalone components that return a
   single `<button>`, and compose them into `Post`.
3. Build the `QuestFeed` tree from your Quest — `QuestFeed`, `QuestRow`, `RewardBadge`,
   `ClaimButton` — with one file per component.
4. Add a `<Post />` to `App` a total of three times and confirm three cards render from a
   single definition.
5. **Boss fight:** assemble a profile page tree — `App` → `ProfileHeader` → (`Avatar`,
   `FollowButton`) and `App` → `Post` ×2 — with every file importing its own children, and
   draw the final tree in a `text` block at the bottom of your notes.

---

## 🔗 See Also

- [[00b - React Cheatsheet]] — component rules and composition on one page
- [[04 - Living Markup]] — previous chapter: expressions and conditional rendering inside a component
- [[05 - Building Blocks]] — previous chapter: defining, exporting and instantiating components
- [[07 - Trade Routes]] — next chapter: sending data down the tree with props
- [[08 - The Health Bar]] — later: letting child widgets remember their own changes
- [[09 - The Controller]] — later: wiring the widgets in this tree to real user events

---
