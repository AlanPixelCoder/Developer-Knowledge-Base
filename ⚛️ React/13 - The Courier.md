# 13. The Courier

**Spanish version:** [13 - El Mensajero.md](13%20-%20El%20Mensajero.md)

**Course:** React
**Topic:** fetch(), data fetching as a side effect, promises, loading state, try/catch, response.ok, error rendering and list filtering
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE_TO_ADVANCED-F0AD4E?style=for-the-badge" alt="Intermediate to advanced">
  <img src="https://img.shields.io/badge/Lessons-01_--_06-7C5CFF?style=for-the-badge" alt="Lessons 01 to 06">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Everything built so far runs on data that was already inside the app. The Emberfall
companion site does not work that way: the gilded-cat asset feed, the guild roster and the
relic vault all live behind **APIs**. This chapter hands you the courier that runs to fetch
them — the native `fetch()` API, called from inside `useEffect` — plus the three futures
every request can have (waiting, delivered, failed) and the search bench that filters
whatever comes back. Quick reference for this chapter and the rest of the module's second
half: [[00c - React Cheatsheet II]].

> [!NOTE]
> **The whole chapter in one sentence**
> Fetch remote data inside `useEffect`, then handle the three possible outcomes — still
> loading, delivered, or failed — before rendering the filtered list players actually
> want to see.

---

## 01. The Courier Guild

> [!NOTE]
> **Key information**
> `fetch()` is part of **native JavaScript** — no library required. React's only job is
> deciding **when** it runs: fetching is an asynchronous **side effect**, so it belongs
> inside `useEffect()` with an empty dependency array `[]`, which runs it exactly once
> after the first render.

Modern apps pull data from external sources — APIs, feeds, remote databases. React does
not ship a data client of its own; it uses the browser's `fetch()`, exactly as plain
JavaScript does.

### The Gilded-Cat Asset Feed

The storefront's gilded-cat portraits come from a real public API:
`https://api.thecatapi.com/v1/images/search?limit=10`. The rule for anything like this:
the request reaches **outside** the component, so it is a side effect, so it runs inside
`useEffect` — never in the render body:

```js
import React, { useState, useEffect } from "react";

function CatImages() {
  const [catImages, setCatImages] = useState([]);

  useEffect(function() {
    // Async side effect: ask the gilded-cat feed for ten portraits
    async function fetchCatImages() {
      const response = await fetch(
        "https://api.thecatapi.com/v1/images/search?limit=10"
      );
      const data = await response.json();
      setCatImages(data);
    }
    fetchCatImages();
  }, []); // [] = run once after mount; without it every render refires the request

  return (
    <div className="cat-grid">
      {catImages.map(function(image) {
        return <img key={image.id} src={image.url} alt="Gilded cat" />;
      })}
    </div>
  );
}
```

Read the effect line by line:

| Line | What it does |
| :--- | :--- |
| `async function fetchCatImages()` | Declares the request **inside** the effect, so it closes over the component's state |
| `await fetch(...)` | Sends the request; execution pauses until the answer arrives |
| `await response.json()` | Parses the body as JSON — also a promise, also awaited |
| `setCatImages(data)` | The setter triggers the re-render that paints the grid |
| `[]` | Dependency array: after the first render, and never again |

> [!WARNING]
> **The mistake everyone makes once**
> Fetch from the effect body **without** the dependency array and React re-runs the
> effect after every render: the setter causes a render, the render refires the request,
> the request sets state again — an infinite request loop that burns the API's rate limit
> in seconds. The `[]` is not optional decoration.

### Quest: Feed Runner

Clone the skeleton into a `PatchNotes()` component that fetches
`https://api.github.com/repos/facebook/react/releases?per_page=3` and renders
`release.name` for each item. Open the Network tab and confirm exactly **one** request
fires on mount — then remove the `[]` and watch the tab flood.

---

## 02. Three States of a Promise

A **promise** is an object representing a value that does not exist yet. `fetch()`
always returns one, and every promise lives in exactly one of three states:

| State | Meaning | What the UI should show |
| :--- | :--- | :--- |
| **Pending** | The request went out; no answer yet | The loading gate |
| **Fulfilled** | The answer arrived and `response.json()` parsed it | The data |
| **Rejected** | Network died, CORS refused, machine is offline | The error message |

`async`/`await` is syntax sugar over those states: `await` suspends the function while
the promise is pending and resumes it with the resolved value — or **throws** if it
rejects, which is exactly what the next section's `catch` block picks up. The same three
states written the classic way:

```js
fetch("https://api.thecatapi.com/v1/images/search?limit=10")
  .then(function(response) { return response.json(); })  // fulfilled path
  .then(function(data) { setCatImages(data); })
  .catch(function(err) { setError(err.message); });      // rejected path
```

> [!TIP]
> `await` pauses **one coroutine**, not the page. The component keeps rendering while you
> wait — which is why the next section exists: without a loading flag, the UI sits on an
> empty box and players assume the game is broken.

---

## 03. The Loading Gate

`async`/`await` pauses execution, but the screen does not pause with it — so tell the
player what is happening with a loading state:

```js
const [isLoading, setIsLoading] = useState(false);
const [loadingMessage, setLoadingMessage] = useState("Summoning gilded cats...");
```

Set both at the **start** of the effect, clear both when the **data arrives**:

```js
useEffect(function() {
  async function fetchCatImages() {
    setIsLoading(true);              // gate opens
    const response = await fetch(
      "https://api.thecatapi.com/v1/images/search?limit=10"
    );
    const data = await response.json();
    setCatImages(data);
    setIsLoading(false);             // data arrived — close the gate
    setLoadingMessage("");
  }
  fetchCatImages();
}, []);
```

And render the indicator only while the request is in flight:

```js
{isLoading && <p className="loading">{loadingMessage}</p>}
{!isLoading && <h2>Gilded Cat Gallery</h2>}
```

The pattern generalizes to every fetch in the module: **open the gate before you ask,
close it when the answer lands** — in a `finally` block once errors enter the picture.

### Quest: Slow Mirror

Wrap your `PatchNotes()` fetch in the same flag pair, with the message
`"Consulting the guild ledger..."`. Use the Network tab's throttling (Slow 3G) to watch
the loading line appear and disappear.

---

## 04. When the Courier Gets Lost

> [!NOTE]
> **Key information**
> `fetch()` does **not** reject on HTTP errors. A `404` or `500` is a perfectly *resolved*
> promise — the only thing that rejects it is a real network failure. You must check
> `response.ok` yourself and throw.

Surround the request with `try`/`catch`, save `error.message` to state, and render it:

```js
async function fetchCatImages() {
  setIsLoading(true);
  try {
    const response = await fetch(
      "https://api.thecatapi.com/v1/images/search?limit=10"
    );
    if (response.ok === false) {
      // 404, 500... fetch() is fine with them, so make the failure explicit
      throw new Error("Failed to fetch data");
    }
    const data = await response.json();
    setCatImages(data);
  } catch (err) {
    setError(err.message);     // store only the message — it is what you render
  } finally {
    setIsLoading(false);       // runs on success AND failure
  }
}
```

`response.ok` is `true` for `200`–`299` and `false` for everything else. Turning the flag
into a thrown `Error` means one `catch` handles every failure — bad status, dead network,
malformed JSON — with the same code path.

### Rendering the Error

Errors are just state, so they render with the same `&&` guard used everywhere else:

```js
{error && <div>{error}</div>}
{!error && <h1>No errors!</h1>}
```

Because `error` is `null` at rest, the two lines collapse into the `||` shorthand —
left side renders if truthy, right side otherwise:

```js
{error || <h1>No errors!</h1>}
```

### Quest: Broken Supply Line

Point the fetch at a wrong path (`https://api.thecatapi.com/v1/images/serch?limit=10`),
reload, and watch `Failed to fetch data` take the screen. Then fix the path and confirm
the error clears on the next render.

---

## 05. The Bestiary Filter

Lists arrive from APIs **whole**; players search them **partially**. `.filter()` is the
bridge — it walks an array and returns a **new** array containing only the items whose
callback returns `true`. The original is never touched:

```js
const filteredCreatures = creatures.filter(function(creature) {
  return creature.name.toLowerCase().startsWith(searchTerm.toLowerCase());
});
```

| Piece | Why it is there |
| :--- | :--- |
| `.filter(...)` | Returns a new array; the master list stays pristine |
| `.toLowerCase()` on **both** sides | `searchTerm` and `name` are normalized, so the search ignores capitals |
| `.startsWith(...)` | The match is a prefix search — `"ash"` finds `"Ashen Wolf"` |

Any valid expression returning a boolean works: compare `rarity`, check `level <= 5`,
test membership with `.includes()`.

### Quest: Beast Scribe

Given `const searchTerm = "cinder";` and a creature named `"Cinder Hound"`, predict the
length of `filteredCreatures` **before** running it. Then add a creature named
`"Ember Hound"` and re-check — did the filter change, or did your assumption?

---

## 06. The Search Bench: Master vs Display

The storefront's relic search runs on two lists, and knowing which is which is the whole
trick:

- **Master list** (`relicList`) — the source of truth. Never mutated, never filtered in place.
- **Display list** (`filteredRelicList`) — **derived** from the master on every render,
  from whatever `searchTerm` currently is.

```js
import React, { useState } from "react";

function RelicSearch() {
  const [searchTerm, setSearchTerm] = useState("");
  const relicList = [
    { name: "Ember Shard", rarity: "Legendary" },
    { name: "Ashen Compass", rarity: "Rare" },
    { name: "Cinder Bell", rarity: "Uncommon" },
  ];

  // Derived on every render: master, filtered by the current search
  const filteredRelicList = relicList.filter(function(relic) {
    return relic.name.toLowerCase().startsWith(searchTerm.toLowerCase());
  });

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={function(e) { setSearchTerm(e.target.value); }}
        placeholder="Search the relic vault"
      />
      {filteredRelicList.map(function(relic) {
        return (
          <div key={relic.name}>
            <h2>{relic.name}</h2>
            <h3>Rarity: {relic.rarity}</h3>
          </div>
        );
      })}
    </div>
  );
}
```

The data flow is a one-way pipeline: **keystroke → `setSearchTerm` → re-render → re-filter
the master → paint the display list**. Delete a search term and the full catalog reappears,
because the master was never reduced in the first place.

> [!TIP]
> **Game dev version**
> This is the inventory screen of every RPG ever shipped: a master data table, a query
> string, and a view that is nothing but `master.filter(...)` drawn to the screen. The
> same pipeline drives the quest log, the auction house and the bestiary — see
> [[07 - Trade Routes]] for the props side of the same idea.

---

## ⚡ XP Earned: Key Takeaways

- 📡 `fetch()` is native JavaScript; React decides **when** it runs — inside `useEffect(..., [])`.
- 🔁 Missing `[]` means an infinite request loop: render → fetch → setState → render.
- ⏳ Every promise is **pending**, **fulfilled** or **rejected** — your UI owes each state an answer.
- 🚦 `isLoading` + `loadingMessage` keep the screen honest while `await` does its work.
- 🚫 `fetch()` never rejects on `404`/`500` — check `response.ok` and `throw` yourself.
- 🧹 `.filter()` returns a **new** array; the master list stays untouched, the display list is derived.

---

## 🎁 Loot Table: Real-World Use Cases

- 🛒 Storefronts and inventories: product lists pulled from an API on mount
- 📰 Feeds: patch notes, guild posts, social timelines — all `fetch` + `.filter()`
- 🔍 Search-as-you-type over remote catalogs (relics, bestiary, players)
- ⚠️ Error boundaries of one kind: surfacing failed requests instead of blank screens
- ⏳ Skeleton screens and spinners — the loading gate wearing different clothes

---

## 🎮 Side Quests: Practice Exercises

1. Add a second effect to `CatImages` that fetches `?limit=5` into its own state, with its own loading flag.
2. Render the raw `error` object with `{error && <div>{error}</div>}`, then switch to `error.message` and compare.
3. Extend `RelicSearch` with a rarity dropdown that composes with the text search (`&&` of two filters).
4. Build a `Bestiary()` component whose master list lives in state and whose display list is filtered by `searchTerm`.
5. **Boss fight:** build a `useCatFeed()` custom hook that owns `catImages`, `isLoading` and `error`, and returns all three — then use it in two different components and confirm the Network tab shows two independent request lifecycles.

---

## 🔗 See Also

- [[00c - React Cheatsheet II]] — this chapter's `fetch`, loading and filter patterns on one page
- [[12 - The Guild Ledger]] — context, the other way to move data through the tree
- [[11 - The Relic System]] — `useEffect` fundamentals: dependencies and cleanup
- [[14 - The World Map]] — next chapter: routing the pages these feeds render into

---
