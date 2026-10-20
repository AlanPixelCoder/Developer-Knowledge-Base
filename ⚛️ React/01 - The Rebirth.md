# 01. The Rebirth

**Spanish version:** [01 - El Renacimiento.md](01%20-%20El%20Renacimiento.md)

**Course:** React
**Topic:** What React is, its history, declarative & component-based design, key features, and the before vs. with React comparison
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-01_--_05-7C5CFF?style=for-the-badge" alt="Lessons 01 to 05">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

The engine behind the **Emberfall Online companion site** — the guild dashboard, storefront
and social feed where every player parks between runs. This opening chapter is the lore
scroll: what React is, who forged it in **2013**, the two design laws it obeys, and the
old way of hand-patching pages it replaced. Quick reference for everything in this chapter:
[[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> React is a declarative, component-based JavaScript library: you describe **what** the
> interface should show for a given set of data, and React keeps the page in sync —
> instead of you hunting DOM nodes and patching them by hand.

---

## 01. The Legend of React

> [!NOTE]
> **Key information**
> **React** is an open-source **JavaScript library**, introduced in **2013**, created by a
> small engineering team at **Facebook** (**Jordan Walke**) to optimize the Newsfeed
> feature. Today it also powers Instagram, Netflix and Airbnb.

React is a **library**, not a full framework: it focuses on one job and does it extremely
well — building the **user interface**. It is a declarative, component-based library for
dynamic user interfaces. Instead of manually tracking and updating DOM elements across
separate files, you compose reusable **components** that update in real time when data
changes.

| Ally | What React runs for them |
| :--- | :--- |
| **Facebook / Meta** | The Newsfeed it was born to optimize |
| **Instagram** | The web app at instagram.com |
| **Netflix** | Parts of the browsing interface |
| **Airbnb** | Search results and booking flows |
| **Emberfall Online** | The companion site you are building in this course |

### Quest: The Scribe's Audit

Every screen of the companion site is a candidate for React. On a sheet of paper, list five
screens of the Emberfall companion site — the guild HUD, the storefront, the social feed,
the quest board, the class quiz — and mark next to each one which piece of it **changes
while the page is open**. Those changing pieces are exactly the data React will be
responsible for.

---

## 02. The Two Laws

### Law One: Declarative

A **declarative** library lets you describe the desired outcome, and the library figures out
the steps. You say *"the HP bar shows 72 of 100"* — React works out which text node to touch
and touches it. The imperative alternative is the old spell: go find `#guild-hp`, read its
children, replace the text, remember to do it again in the three other files that display
the same number.

### Law Two: Component-Based

The interface is broken into **components** — small, reusable functions that each render one
piece of the screen. A component receives data, returns markup, and re-renders itself when
its data changes. The HP bar and the quest list of the guild HUD are two components; change
the underlying data and both update **in real time**, without a page reload and without you
writing the update logic twice.

> [!TIP]
> Think of a component as a reusable scene in a game engine: you author it once, drop it
> into twenty screens, and a change to the source scene propagates to every instance.

### Quest: Draw the Party Tree

Take the guild HUD from the previous quest and split it into components. Draw it as a tree:
one box per component, lines to its children. A reasonable first split is `GuildHud`
containing `HealthBar`, `QuestList` and `PlayerBadge`. You have just designed your first
React component hierarchy — chapters [[03 - Glyph Workshop]] and [[04 - Living Markup]]
teach you how to actually write them.

---

## 03. The Four Runes

Every React advertisement reduces to four features. Learn to name them and you can explain
the library in thirty seconds:

| Feature | What it means | On the companion site |
| :--- | :--- | :--- |
| **Component-Driven Architecture** | The UI is built from small, reusable, independent components | The HUD, feed and storefront are assembled from shared cards |
| **JSX Syntax** | HTML-like markup written directly inside JavaScript | Pages are written in one language, not three |
| **Efficient DOM Updates** | React touches **only what changed** in the real page | A new like count repaints one number, not the whole feed |
| **High Scalability & Performance** | The model holds up from a landing page to a huge app | The companion site can grow into a full social network |

> [!NOTE]
> The third rune — *only what changed* — is the one you will feel in chapter
> [[02 - Spawn Point]] the moment you save a file and the dev server repaints the screen
> faster than you can alt-tab.

### Quest: Recite the Runes

Cover the table and write the four features from memory. Then, for each one, name a screen
of the companion site where it matters. If you cannot place *JSX Syntax* anywhere, you have
found the gap this course fills.

---

## 04. The Old Pact vs. the React Pact

### Before React

Traditional DOM manipulation means finding elements in every HTML document, then modifying
them manually with vanilla JavaScript. The same value displayed in three places means three
`querySelector` calls, three assignments, and three chances to forget one when the markup
changes. It is **repetitive and error-prone**:

```javascript
// The old way: hunt the element down, then patch it by hand —
// and repeat in every file that displays the same value
const hpBar = document.querySelector("#guild-hp");
hpBar.textContent = "HP: 72 / 100";

const questLine = document.querySelector("#quest-line");
questLine.textContent = "Deep Halls — sweep the third floor";
```

Miss one of those updates and the interface lies to the player: the HUD says 72 while the
server already applied the hit.

### With React

React's model centralizes interface logic into components. You update the data **once**,
and the change applies **everywhere the component is rendered**:

```javascript
// The React way: one component owns the display logic
function HealthBar(props) {
  return <div className="hp-bar">HP: {props.hp} / 100</div>;
}

// Update the data once — every place the bar is rendered follows
<HealthBar hp={72} />
```

There is one definition of the HP bar, so there is one place to update and one place to
break. Full treatment of how data reaches a component arrives in a later chapter on props;
for now, hold the shape: **centralize, update once, apply everywhere**.

> [!WARNING]
> **The classic mistake**
> Patching the DOM by hand (`querySelector`, `innerHTML`) inside a React app. React keeps
> its own idea of what the page contains — hand edits make that copy drift, and the next
> data change silently overwrites them. In React, data and markup change **through
> components**, never around them.

### Quest: Port One Patch

Take any `querySelector` patch you wrote in the JavaScript course — a HUD readout, a
receipt line, a counter — and rewrite it as a component that receives the value and prints
it. Count the lines you deleted. That ratio is the reason React exists.

---

## 05. The Living HUD

### Checkpoint: Chapter Recap

- React is an open-source **JavaScript library** from **2013**, built at **Facebook** by
  **Jordan Walke**'s team for the Newsfeed.
- It is **declarative**: you describe the result, React performs the DOM work.
- It is **component-based**: the UI is reusable pieces that re-render when data changes.
- The four features: Component-Driven Architecture, JSX Syntax, Efficient DOM Updates,
  High Scalability & Performance.
- Before React: find and patch elements manually, everywhere. With React: centralize the
  logic, update once, apply everywhere.

### The Guild HUD

Here is the framing example this whole course builds toward: a guild HUD where the HP bar
and the quest list are components that refresh live when the data behind them changes.

```javascript
function GuildHud() {
  const hp = 84;
  const nextQuest = "Deep Halls — sweep the third floor";

  return (
    <div className="guild-hud">
      <h2>WardenOfTheNinth</h2>
      <div className="hp-bar">HP: {hp} / 100</div>
      <p className="quest-line">Next quest: {nextQuest}</p>
    </div>
  );
}
```

Change `hp` and the bar text changes. Change `nextQuest` and the quest line changes. Nothing
else on the page moves, because nothing else changed — that is the fourth rune in action.

> [!TIP]
> **Game dev version**
> HTML labels content, CSS styles it, JavaScript runs — React is the army that keeps them
> in sync. In a game engine you never poke pixel buffers either: you change the *data* of an
> entity and the renderer redraws it. React brings that discipline to the browser, and the
> next chapter, [[02 - Spawn Point]], installs the toolchain that runs it.

---

## ⚡ XP Earned: Key Takeaways

- 🧬 **React is a library** — open source, introduced **2013**, born at **Facebook**
  (**Jordan Walke**) for the Newsfeed; it also runs Instagram, Netflix and Airbnb.
- 📜 **Declarative** means you describe the desired UI and React performs the DOM updates.
- 🧩 **Component-based** means the UI is reusable pieces that update in real time when
  data changes — no more patching the same value in five files.
- 🔮 The four runes: Component-Driven Architecture, JSX Syntax, Efficient DOM Updates
  (only what changed), High Scalability & Performance.
- ⚔️ Before React: manual, repetitive, error-prone `querySelector` patching. With React:
  centralized component logic — update once, apply everywhere.
- 🎯 The guild HUD is the target: an HP bar and a quest list that refresh live.

---

## 🎁 Loot Table: Real-World Use Cases

- 📰 Data-heavy dashboards where values refresh without page reloads (feeds, stock tickers)
- 🛒 Storefronts whose carts, stock and prices change while you browse
- 🎮 Companion sites and second-screen tools for live games
- 🧱 Design systems: one card component reused across dozens of screens
- 🔄 Anything that was previously twenty `querySelector` patches and a prayer

---

## 🎮 Side Quests: Practice Exercises

1. Write the React fact block (library, 2013, Facebook, Jordan Walke, Newsfeed) from
   memory, then check it against this page.
2. Name three apps you use daily and find evidence of React in their web front end.
3. Split a page you already built (HTML course) into components and draw the hierarchy tree.
4. Rewrite one imperative `querySelector` patch from an old project as a component.
5. **Boss fight:** take the Merchant Receipt from the JavaScript course and describe, line by
   line, which parts of it are **data** (items, prices, total) and which are **presentation**
   — then sketch the components you would build so the total recalculates itself.

---

## 🔗 See Also

- [[02 - Spawn Point]] — next chapter: Node.js, Vite, and booting your first React app
- [[03 - Glyph Workshop]] — JSX: the markup syntax the four runes are written in
- [[04 - Living Markup]] — expressions, conditionals and attributes inside that markup

---
