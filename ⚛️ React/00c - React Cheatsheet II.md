# 00c. React Cheatsheet II

**Spanish version:** [00c - Chuleta de React II.md](00c%20-%20Chuleta%20de%20React%20II.md)

**Course:** React
**Topic:** Quick reference for the advanced toolkit: forms, hooks, context, data fetching, routing and styling
**Tags:** `#react` `#cheatsheet` `#reference` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE_TO_ADVANCED-F0AD4E?style=for-the-badge" alt="Intermediate to advanced">
  <img src="https://img.shields.io/badge/Covers-Chapters_10_--_15-7C5CFF?style=for-the-badge" alt="Chapters 10 to 15">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

The second half of the toolkit — everything a real Emberfall companion page needs once the
basics are locked: forms that own their data, hooks for effects and refs, context for
global state, `fetch` for remote data, a router for multiple screens and three layers of
CSS. Every statement here was introduced in [[10 - The Forge]] through
[[15 - The Final Boss]]. The core toolkit (JSX, components, props, state, events) is in
[[00b - React Cheatsheet]].

> [!TIP]
> This is the sheet you open when something *almost* works: the form that loses its value,
> the effect that never stops fetching, the link that reloads the page. Find the symptom
> in the tables, jump to the pattern, ship the fix.

**The running theme of this module: Emberfall**, the companion site for a roguelike of the
same name. Every pattern below ships in it: the login form, the gilded-cat feed, the
theme switcher, the class quiz. The code is the same code a real studio ships — only the
words change.

---

## 📝 Forms

The five-step checklist, in order — skip a step and the form misbehaves:

| Step | Rule |
| :--- | :--- |
| 1. Initialize | `useState` holds every field, usually one object |
| 2. Control | `value={...}` on every `<input>`, `<select>` and `<textarea>` |
| 3. Change handler | `onChange` writes `e.target.value` back into state |
| 4. Submit handler | `onSubmit` on the `<form>` validates and acts |
| 5. Prevent default | `e.preventDefault()` — or the browser reloads and eats the state |

```js
// Labels use htmlFor (for is a reserved keyword); inputs carry name + value + onChange
function SignInForm() {
  const [formData, setFormData] = useState({ email: "", password: "" });

  function handleFormData(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Welcome back, " + formData.email);
    setFormData({ email: "", password: "" });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="email">Email</label>
      <input
        type="email"
        id="email"
        name="email"
        value={formData.email}
        onChange={handleFormData}
      />
      <label htmlFor="password">Password</label>
      <input
        type="password"
        id="password"
        name="password"
        value={formData.password}
        onChange={handleFormData}
      />
      <button type="submit">Enter</button>
    </form>
  );
}
```

| Element | Controlled shape |
| :--- | :--- |
| `<input>` | `value` + `onChange` — React state owns the text |
| `<select>` | `value` on the **parent** `<select>`; no `selected` on `<option>` |
| `<textarea>` | `value` + `onChange`; `rows` / `cols` optional |
| Computed key | `[e.target.name]: e.target.value` lets one handler serve many fields |

---

## 🪝 Hooks

React **16.8** (Feb 2019) gave functional components state and lifecycle. The workhorse is
`useEffect(fn, deps)` — a **side effect** is anything reaching outside the component (data,
DOM, timers, pop-ups):

| Dependency array | Runs |
| :--- | :--- |
| `[]` | Once, after the first render |
| omitted | After **every** render |
| `[count]` | When `count` changes |

```js
// Cleanup: intervals and listeners outlive the component unless you return a teardown
useEffect(function() {
  const intervalId = setInterval(function() {
    setSeconds(function(prevSeconds) { return prevSeconds + 1; });
  }, 1000);
  return function() { clearInterval(intervalId); };
}, []);
```

### `useRef`

A mutable box that survives renders, stored in `.current`, that **never re-renders**:

```js
const dataRef = useRef([]);        // data for your own bookkeeping
dataRef.current.push(Math.random());

const viewRef = useRef(null);      // direct DOM access
<input ref={viewRef} />;
viewRef.current.focus();
```

| | `useState` | `useRef` |
| :--- | :--- | :--- |
| Update triggers re-render | ✅ fresh UI | ❌ silent |
| Read on mount | via initial value | `ref.current` |
| Use for | anything the screen must show | DOM nodes, timer ids, dimensions, animation handles |

---

## 🗄️ Context

**Prop drilling** (handing props through many layers) dies here. Context = one value,
many consumers, zero middlemen:

```js
import { createContext, useContext, useState } from "react";

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("dark");
  function toggleTheme() {
    setTheme(theme === "dark" ? "light" : "dark");
  }
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// Anywhere below the provider:
const { theme, toggleTheme } = useContext(ThemeContext);
return <button onClick={toggleTheme}>Switch theme</button>;
```

| Piece | Job |
| :--- | :--- |
| `createContext()` | Creates the channel — export it from its own file |
| `<Ctx.Provider value={...}>` | Publishes the value; wraps the subtree that needs it |
| `useContext(Ctx)` | Subscribes a component to the channel |
| Provider component | Owns the state (`useState`) so consumers only read and call |

---

## 📡 Data Fetching

`fetch()` is native JS. It is a side effect, so it lives in `useEffect` — and it needs a
loading flag and an error slot, because every request has three futures:

```js
const [data, setData] = useState([]);
const [isLoading, setIsLoading] = useState(false);
const [error, setError] = useState(null);

useEffect(function() {
  async function loadData() {
    setIsLoading(true);
    try {
      const response = await fetch("https://api.thecatapi.com/v1/images/search?limit=10");
      if (response.ok === false) {
        // fetch() resolves on 404/500 — check the flag yourself
        throw new Error("Failed to fetch data");
      }
      const json = await response.json();
      setData(json);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  }
  loadData();
}, []); // [] = once; missing it = infinite request loop

// Rendering all three states:
{isLoading && <p>Loading...</p>}
{error && <div>{error}</div>}
{!error && !isLoading && data.length > 0 && <GildedList items={data} />}
```

### Filtering the result

```js
const filteredRelics = relicList.filter(function(relic) {
  return relic.name.toLowerCase().startsWith(searchTerm.toLowerCase());
});
```

Master list stays pristine; the display list is **derived** on every render.

---

## 🗺️ Routing

Client-side routing swaps components **in the browser** — no page reloads. The package is
`react-router-dom`:

```bash
npm install react-router-dom
```

| Piece | Role |
| :--- | :--- |
| `<BrowserRouter>` | One per app; wraps everything at the entry point |
| `<Routes>` | Picks the `<Route>` matching the current URL |
| `<Route>` | `path` + `exact` + `element` — the component to inject |
| `<Link to>` | Internal navigation without a reload (replaces `<a href>`) |
| `useNavigate()` | Programmatic navigation |

```js
<Routes>
  <Route path="/" exact element={<Home />} />
  <Route path="/codex" exact element={<Codex />} />
</Routes>

const navigate = useNavigate();
navigate("/codex");  // go
navigate(-1);        // back — walk the history stack
navigate(1);         // forward
```

---

## 🎨 Styling

Three layers, one home per rule — from the capstone in [[15 - The Final Boss]]:

| Layer | Lives in | Examples |
| :--- | :--- | :--- |
| Global | `index.css` | `html { font-family: Arial; min-height: 100vh; }` |
| Component rules | the same stylesheet, scoped by selector | `form input { width: 400px; }`, `nav a:hover` |
| Dynamic API content | dedicated classes | `.artwork img { max-width: 30%; border-radius: 10px; }` |

```css
html {
  display: flex;
  flex-direction: column; /* stack children top to bottom */
  align-items: center;
  min-height: 100vh;      /* fill the viewport even with little content */
}

.artwork img {
  max-width: 30%;         /* seatbelt for untrusted API image sizes */
}
```

Inline `style={{ }}` works but breaks the layering — camelCase properties only
(`backgroundColor`, not `background-color`).

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| Submitting without `preventDefault` | Full page reload; all state gone |
| Uncontrolled `<select>` | Put `value` on the parent, not `selected` on options |
| `useEffect` with a changing object in deps | Re-runs every render — deps compare by identity |
| Interval without cleanup | Keeps firing after unmount — return a teardown |
| Mutating `ref.current` for the UI | Nothing on screen changes — refs do not re-render |
| `<a href>` inside the app | SPA kills the document; use `<Link to>` |
| Two `<BrowserRouter>`s | Two competing maps of the URL — one frame only |
| Forgetting `createContext` export | Every consumer creates a new, silent context |

---

## 🔗 See Also

- [[00b - React Cheatsheet]] — JSX, components, props, state and events (chapters 01–09)
- [[10 - The Forge]] — the controlled-form pattern behind the checklist
- [[13 - The Courier]] — the full fetch/loading/error story
- [[15 - The Final Boss]] — every pattern on this sheet, assembled into one SPA

---
