# 04. Living Markup

**Spanish version:** [04 - Marcado Vivo.md](04%20-%20Marcado%20Vivo.md)

**Course:** React
**Topic:** The single-root rule, fragments, embedding JavaScript expressions, conditional rendering, static and dynamic attributes, and `className`
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Beginner to Intermediate">
  <img src="https://img.shields.io/badge/Lessons-01_--_08-7C5CFF?style=for-the-badge" alt="Lessons 01 to 08">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Chapter 03 taught you the glyphs. This chapter makes them **breathe**: how the single-root
rule and fragments hold markup together, how to embed live JavaScript expressions with curly
braces, how to show different markup per condition, and how attributes — static and dynamic —
plus the `className` quirk carry data into the page. Quick reference for everything in this
chapter: [[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A React component returns exactly **one** root element, and inside that markup curly braces
> `{ }` let you drop in any JavaScript expression — values, conditionals, dynamic attributes —
> while `className` stands in for the reserved word `class`.

---

## 01. The Single Root Rule

A `return` can contain **only ONE root element**. Two siblings at the top level:

```javascript
// ❌ Two roots — this does not compile
return (
  <h1>Deep Halls</h1>
  <p>Warden of the Ninth Floor</p>
);
```

Two elements standing side by side with no shared parent is a syntax error. Wrap them in a
single container:

```javascript
// ✅ One root wrapping the siblings
return (
  <div>
    <h1>Deep Halls</h1>
    <p>Warden of the Ninth Floor</p>
    <ul>
      <li>Ember Gate</li>
      <li>Frozen Cistern</li>
      <li>The Ninth Floor</li>
    </ul>
  </div>
);
```

The `<div>` is the root; the `<h1>`, `<p>` and `<ul>` are its children, and the `<li>`s are
the tour dates of the raid — quest locations. Same element tree you drew for the party in the
HTML course, now as a return value.

> [!IMPORTANT]
> The parentheses around the whole thing are not optional decoration: without them,
> automatic semicolon insertion (from chapter [[03 - Glyph Workshop]]) truncates the return
> after the first line. Parentheses plus a single root is the whole contract.

### Quest: The Raid Card

Build an Emberfall item card: one root `<div>` containing an `<h1>Deep Halls</h1>`, a
`<p>Warden of the Ninth Floor</p>` and a `<ul>` of at least three quest locations. Then
delete the `<div>` and watch the compiler reject the two bare roots. Put it back.

---

## 02. The Fragment Rune

Sometimes you want siblings **without** an extra `<div>` polluting the DOM. A **React
Fragment** wraps them and emits **no DOM node** at all:

```javascript
return (
  <>
    <h1>Deep Halls</h1>
    <p>Warden of the Ninth Floor</p>
  </>
);
```

`<>...</>` is shorthand for `React.Fragment`. The browser's document does **not** get a
wrapper element between the `<h1>` and the `<p>` — the fragment is a ghost parent that
satisfies the single-root rule while leaving the actual HTML clean.

> [!TIP]
> Reach for a fragment whenever the only reason for your `<div>` was the single-root rule.
> If the `<div>` carries a class or is a real layout container, keep it; if it exists purely
> to please the compiler, replace it with `<>`.

### Quest: De-Div the HUD

Take the guild HUD and wrap its HP bar and quest list in `<>...</>` instead of a `<div>`. In
the browser's element inspector, confirm that neither bar nor list has a wrapper element.
You have removed a `<div>` that was doing nothing but appeasing the rule — a `<div>` soup
diet.

---

## 03. Live Expressions

Wrap a JavaScript expression in **curly braces** `{ }` and React renders its value. This is
how data gets into markup:

```javascript
const articleTitle = "As We May Think";
const articleAuthor = "Vannevar Bush";
const readNumber = 750;

return (
  <article>
    <h2>{articleTitle}</h2>
    <p>By {articleAuthor}</p>
    <p>Read {readNumber} times</p>
  </article>
);
```

Any valid JavaScript expression that resolves to **a single value** works inside `{ }`:
a variable, `2 + 2`, `name.toUpperCase()`, a ternary, a function call. Full member access
(`props.title`), arithmetic, string methods — all welcome. What does **not** work is a
statement (`if`, `for`) or anything that returns nothing meaningful.

> [!WARNING]
> **The classic mistake**
> Putting a statement or an object literal where an expression belongs. `{ if (signedIn) ... }`
> is invalid inside JSX, and `{ { a: 1 } }` renders nothing useful. Use an **expression** — a
> ternary or `&&` for conditions (section 04), and `Object.entries` / `.map` to reshape
> objects before rendering.

### Quest: Lore Entry

Retheme the article above to an Emberfall lore entry: `entryTitle`, `author` and a
`readNumber` of chapter reads. Render all three with curly braces. Then change one value,
save, and watch only that text update — hot reload from [[02 - Spawn Point]] running a live
expression.

---

## 04. Conditional Rendering

Three shapes, from most verbose to tightest:

### 1. Assign in a variable

```javascript
let page = null;

if (signedIn) {
  page = <div>Guild member dashboard</div>;
} else {
  page = <div>Log in to enter the guild hall</div>;
}

return <main>{page}</main>;
```

A variable holds whichever JSX applies, and `{page}` renders it. Clear and debuggable, at the
cost of boilerplate.

### 2. Ternary

```javascript
return (
  <main>
    {signedIn ? <GuildDashboard /> : <LoginGate />}
  </main>
);
```

`condition ? a : b` picks one of two markup branches inline. This is the most common
either/or form in real code.

### 3. Logical AND

```javascript
return (
  <main>
    {signedIn && <GuildDashboard />}
  </main>
);
```

`condition && markup` renders the markup only when the condition is truthy, and renders
nothing otherwise — no else branch. Use it when there is only a "show it" case.

> [!TIP]
> Pick by the number of branches: `&&` for zero-or-one, ternary for exactly-two, an
> `if`/`else` with a variable when the branches grow or need names. Mixing all three in one
> return is a smell — split the component instead.

### Quest: The Login Gate

In a component, set `const signedIn = false;`. Render a `LoginGate` with `&&`, then switch
to a ternary that also shows a `GuildDashboard` when true. Flip `signedIn` and save — the
floor of the hall changes with one boolean.

---

## 05. Static Attributes

Attributes look like HTML. `src`, `alt`, `href`, `id` take quoted strings exactly as in the
HTML course:

```javascript
// A guild avatar path — plain static strings
<img src="username/camera/recents/today.png" alt="a guild selfie" />
```

Nothing surprising here: quoted values, same syntax, same meaning. This is the easy half of
attributes.

---

## 06. Dynamic Attributes

To make an attribute depend on a JavaScript variable, **drop the quotes** and wrap the value
in curly braces:

```javascript
const tokyoUrl = "https://i.imgur.com/0Ax1wzO.png";
const tokyoImage = <img src={tokyoUrl} alt="Tokyo" />;
```

`src={tokyoUrl}` evaluates the variable and uses whatever it holds — no quotes inside the
braces. Change `tokyoUrl` and the image source follows on the next render. Any expression
works: `src={avatarUrl}`, `id={"slot-" + index}`, `alt={item.name}`.

> [!WARNING]
> **The classic mistake**
> Wrapping braces in quotes: `src="{tokyoUrl}"` renders the literal text `{tokyoUrl}` as the
> URL. Quotes make a static string; braces make a live expression. You choose one, never
> both.

### Quest: Avatar Forge

Declare `const avatarUrl = "username/camera/recents/today.png";` and render an `<img>` whose
`src` is dynamic. Point `avatarUrl` at a different path, save, and watch the portrait swap
without touching the markup.

---

## 07. `className`

`class` is a **reserved JavaScript keyword** (think `class Planet`), so JSX cannot use it for
the HTML attribute. React's spelling is **`className`**:

```javascript
<button className="forge-button">Enter the Deep Halls</button>
```

`className` takes the same value the `class` attribute would, and it accepts **dynamic**
values too, because it is just an attribute:

```javascript
const isLocked = true;
<button className={isLocked ? "forge-button is-locked" : "forge-button"}>
  {isLocked ? "Locked" : "Enter the Deep Halls"}
</button>
```

The CSS in your stylesheet still targets `.forge-button` — only the JSX-side name changes.

> [!NOTE]
> The same reserved-word problem produces a cluster of JSX renames you will meet again:
> `class` → `className`, `for` → `htmlFor` (chapter [[10 - The Forge]]), and inline style
> properties that are camelCase (`background-color` → `backgroundColor`, chapter
> [[09 - The Controller]]). Learn the pattern once — JSX renames the collisions.

### Quest: Restyle the Button

Take a button from an old HTML project with `class="login-button"` and bring it into JSX.
Rename the attribute to `className="forge-button"`, keep the CSS targeting `.forge-button`,
and add a dynamic variant using a ternary. The stylesheet has no idea anything moved.

---

## 08. The Breathing Interface

### Checkpoint: Chapter Recap

- **Single root:** one element per return; wrap siblings in a container or a fragment.
- **Fragment** `<>...</>` groups siblings and emits **no DOM node**.
- **Curly braces** `{ }` embed any single-value JavaScript **expression** into markup.
- **Conditional rendering** has three shapes: a variable with `if`/`else`, a **ternary**
  (`? :`), and **logical AND** (`&&`) with no else branch.
- **Attributes**: static strings stay as in HTML; dynamic values drop the quotes and use
  `{expression}`.
- **`className`** replaces `class` because `class` is reserved in JavaScript.

### The Living Card

Everything in one component — the single root, a fragment, live expressions, a ternary, a
static attribute and a dynamic one:

```javascript
function RelicCard(props) {
  const { name, imageUrl, rarity } = props;
  const isLegendary = rarity === "legendary";

  return (
    <>
      <h2>{name}</h2>
      <img src={imageUrl} alt={name} width="200" />
      {isLegendary ? (
        <p className="badge legendary">Legendary! 🔥</p>
      ) : (
        <p className="badge">Common</p>
      )}
    </>
  );
}

export default function App() {
  return (
    <div className="catalog">
      <RelicCard
        name="Ember Blade"
        imageUrl="https://i.imgur.com/0Ax1wzO.png"
        rarity="legendary"
      />
    </div>
  );
}
```

Read it back against the rules: the App root is one `<div>`; `RelicCard` returns a fragment
with no wrapper; `{name}`, `{imageUrl}` and the ternary are live expressions; `width` and
`alt` are static; `src={imageUrl}` is dynamic; `className` stands in for `class`.

> [!TIP]
> **Game dev version**
> This is exactly how a HUD widget is drawn: one root panel, child slots grouped without
> extra scaffolding, and attributes bound to live values. Swap the relic for a health bar,
> the rarity for a damage tier, and the ternary for `hp < 20 ? <Critical/> : <Stable/>` —
> the same component shape builds the whole companion site.

---

## ⚡ XP Earned: Key Takeaways

- 🌳 **One root per return.** Two bare siblings is a compile error; wrap them.
- 👻 **Fragment** `<>...</>` satisfies the single-root rule without adding a DOM node — the
  cure for `<div>` soup.
- 🧮 **Curly braces** `{ }` interpolate any single-value JavaScript **expression** — variables,
  arithmetic, methods, ternaries.
- 🔀 **Conditionals** come in three shapes: `if`/`else` into a variable, the **ternary** `? :`,
  and **logical AND** `&&` for the no-else case.
- 🏷️ **Attributes** are static strings by default; to bind them to a variable, drop the quotes
  and use `{expression}`.
- 🔤 **`className`** replaces `class` — `class` is reserved in JavaScript. The same collision
  later yields `htmlFor` and camelCase inline styles.

---

## 🎁 Loot Table: Real-World Use Cases

- 🃏 Card grids (items, profiles, products) where each card is one root with live fields
- 🔐 Authenticated vs. guest views driven by a single boolean and a ternary or `&&`
- 🖼️ Avatars, product images and icons whose URLs arrive from data as dynamic attributes
- 🎨 Conditional CSS classes for locked, legendary or highlighted states
- 🧩 Fragments keeping list and grid markup free of pointless wrapper divs

---

## 🎮 Side Quests: Practice Exercises

1. Rewrite a two-root return so it compiles, once with a `<div>` and once with a fragment.
2. Render your guild XP as `{xp}` and then as `{xp * 2}` — prove expressions, not just
   variables, work in braces.
3. Build all three conditional shapes (variable, ternary, `&&`) for the same signed-in state.
4. Make a card image whose `src` comes from a variable and whose `alt` is a static string.
5. **Boss fight:** build a full `RelicCard` component — fragment root, dynamic image, dynamic
   `className` via ternary, and a `<ul>` of stats rendered from an array with `.map`. Render
   three cards in an `App` and verify the markup has no wrapper divs anywhere it should not.

---

## 🔗 See Also

- [[03 - Glyph Workshop]] — the previous chapter: JSX, transpilation and the parentheses rule
- [[05 - Building Blocks]] — next chapter: functional components, naming, export and import
- [[09 - The Controller]] — events and the camelCase inline-style rules `className` foreshadows
- [[10 - The Forge]] — forms, where `htmlFor` joins `className` as a reserved-word rename

---
