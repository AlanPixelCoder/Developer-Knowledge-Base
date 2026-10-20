# 14. The World Map

**Spanish version:** [14 - El Mapa del Mundo.md](14%20-%20El%20Mapa%20del%20Mundo.md)

**Course:** React
**Topic:** Single-page applications, client-side routing, react-router-dom, BrowserRouter, Routes, Route, Link, useNavigate and the history stack
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-6CC24A?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-01_--_06-7C5CFF?style=for-the-badge" alt="Lessons 01 to 06">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

The Emberfall companion site has outgrown a single screen: it needs a Home page, a Codex,
a Support desk — and players expect real URLs, a working back button and links they can
share in guild chat. This chapter is the world map that ties those screens together:
**client-side routing** with `react-router-dom`, the package that decides which component
shows at which URL **without ever reloading the page**. Quick reference for this chapter:
[[00c - React Cheatsheet II]].

> [!NOTE]
> **The whole chapter in one sentence**
> Wrap the app in `<BrowserRouter>`, declare pages with `<Route path element>`, swap
> between them with `<Link to>` or `useNavigate()` — and the browser's URL becomes a
> viewport onto your component tree instead of a request to a server.

---

## 01. One Page, Many Doors

> [!NOTE]
> **Key information**
> A **single-page application (SPA)** serves one HTML document and swaps its contents in
> the browser. Users still expect URLs, the back button and shareable links — so the
> routing is decided **inside the browser**: that is **client-side routing**, and no
> full-page reload ever happens.

Classic websites are multi-page: every click requests a fresh HTML document, the old page
dies, the new one boots from zero — including the game state, the theme and every open
dropdown. An SPA keeps one document alive and swaps **components** in and out of it.

React's core has no routing built in. The standard answer is the external package
**`react-router-dom`**, and it ships exactly four pieces you need at this level:

| Component | Role |
| :--- | :--- |
| `<BrowserRouter>` | The portal frame — one instance, wraps the whole app, watches the URL |
| `<Routes>` | The map legend — scans the current URL and picks the matching `<Route>` |
| `<Route>` | One door: a `path` paired with the `element` (component) it injects |
| `<Link>` | A signpost — the router-aware replacement for `<a href>` inside the app |

> [!WARNING]
> **The mistake everyone makes once**
> Reaching for `<a href="/codex">` out of habit. The browser treats it as a navigation to
> another document: full reload, SPA state gone. Inside the app, every internal link is a
> `<Link to="...">`.

---

## 02. The Travel Pack

Routing is a dependency like any other — install it in the Vite project from
[[02 - Spawn Point]]:

```bash
# Add client-side routing to the project
npm install react-router-dom
```

Then import the pieces where you use them:

```js
import { BrowserRouter, Routes, Route, Link, useNavigate } from "react-router-dom";
```

Everything above is **one package** — `react-router-dom` — but each import is a separate
tool: the frame, the map, the doors, the signposts and the fast-travel button, in the
order you will meet them in this chapter.

---

## 03. The Portal Frame

The `<BrowserRouter>` wraps the app at the entry point, exactly like the
`<StrictMode>` wrapper from the Vite setup:

```js
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>
);
```

One `<BrowserRouter>` for the entire app. It has no visible output — its job is to watch
the URL bar and give every `<Route>` and `<Link>` below it access to the current
location. Two frames (one per page component) means two maps of the same territory: they
will disagree about where you are.

### Quest: Frame Check

Take the `index.js` from chapter [[02 - Spawn Point]], add the import and the wrapper,
and confirm the app still renders. Remove `<BrowserRouter>` on purpose, click a
`<Link>`, and read the error — knowing the failure message is half of debugging routing.

---

## 04. Marking the Trails

Inside `<App>`, `<Routes>` holds every `<Route>` of the site. Retheme the companion
site's three pages to Home, Codex and Support:

```js
function App() {
  return (
    <div>
      <NavBar />
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/codex" exact element={<Codex />} />
        <Route path="/support" exact element={<Support />} />
      </Routes>
    </div>
  );
}
```

Each door has three parts:

| Prop | What it is | Example |
| :--- | :--- | :--- |
| `path` | The URL string the door watches | `"/codex"` |
| `exact` | Match the path **perfectly** — no extras | `exact` |
| `element` | The component injected when the path wins | `<Codex />` |

The browser is now at `/` → `<Home />` renders. Navigate to `/codex` → `<Routes>` notices
the URL changed, `<Codex />` takes the stage, and the document never reloaded.

> [!TIP]
> `exact` matters because React Router matches paths **prefix-first** by default: without
> it, `path="/"` would also claim `/codex` and `/support`, and the landing page would
> swallow the whole map. Match precisely, and the router never has to guess.

### Quest: New Territory

Add a `path="/guild"` door for a `Guild` component, then visit `/guild` in the address
bar. Confirm the URL, the rendered component and the absence of any page reload all
agree.

---

## 05. The Signposts

`<Link>` replaces `<a href>` for **internal** navigation. The `to` prop replaces `href`;
the router intercepts the click, updates the URL and swaps the component — no reload:

```js
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/codex">Codex</Link>
      <Link to="/support">Support</Link>
    </nav>
  );
}
```

| Anchor `<a>` | Signpost `<Link>` |
| :--- | :--- |
| `href="/codex"` | `to="/codex"` |
| Full page reload | URL and UI update in place |
| Leaves the SPA | Never leaves the SPA |
| Use for external sites | Use for every page inside the app |

### Quest: Nav Audit

Browse any production site and count the internal links that would kill an SPA if they
were `<a>` tags — then write the same nav for the companion site with `<Link>` and watch
the Network tab stay empty as you click through it.

---

## 06. Fast Travel

`<Link>` covers clicks on visible signposts. Some navigation has **no element** to click:
a redirect after login, a "return to store" button after checkout, the browser's back
arrow inside your own UI. That is `useNavigate()`:

```js
import { useNavigate } from "react-router-dom";

function SignIn() {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();
    // credentials checked elsewhere — send the player home
    navigate("/home");
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Enter the guild hall</button>
    </form>
  );
}
```

`navigate(path)` jumps to any URL your `<Routes>` know. The history stack — the same
stack behind the browser's back and forward buttons — is steerable too:

| Call | Effect |
| :--- | :--- |
| `navigate("/codex")` | Push `/codex` onto the stack and go there |
| `navigate(-1)` | **Back** — one step down the stack |
| `navigate(1)` | **Forward** — one step up, if there is one |

> [!TIP]
> **Game dev version**
> This is a world map fast-travel system: signposts (`<Link>`) for the marked destinations,
> a warp spell (`navigate()`) for everything programmatic, and the history stack as the
> breadcrumb trail back to the last waypoint. The capstone in [[15 - The Final Boss]] uses
> exactly this pack to move between the landing page and the class quiz.

---

## ⚡ XP Earned: Key Takeaways

- 🗺️ An **SPA** keeps one HTML document alive and swaps components; client-side routing picks the component **in the browser**.
- 📦 Routing is not core React — it is `react-router-dom`, installed like any other dependency.
- 🖼️ `<BrowserRouter>` wraps the app **once**, at the entry point, beside `<StrictMode>`.
- 🚪 A `<Route>` is `path` + `exact` + `element` — URL string, perfect match, component to inject.
- 🪧 `<Link to>` replaces `<a href>` internally: no reload, URL and UI update together.
- ⚡ `useNavigate()` navigates without a click; `navigate(-1)` / `navigate(1)` walk the history stack.

---

## 🎁 Loot Table: Real-World Use Cases

- 🏠 Multi-screen sites: dashboards, storefronts, help desks — one document, many URLs
- 🔐 Post-login redirects with `navigate("/home")` after form submission
- 🧭 Tabs and panels that must stay bookmarkable and shareable in chat
- ↩️ In-app back buttons that behave exactly like the browser's own
- 🛒 Checkout flows: cart → payment → confirmation, without ever losing SPA state

---

## 🎮 Side Quests: Practice Exercises

1. Add a `NotFound` route with `path="*"` and confirm every unknown URL lands there.
2. Build a footer `<Link to="/support">Report a bug</Link>` and verify the Network tab stays empty on click.
3. Wire a "Back to the codex" button that calls `navigate(-1)` instead of hardcoding a path.
4. Log `window.location.pathname` on every render inside `<App>` and watch it change as you navigate.
5. **Boss fight:** combine chapters [[13 - The Courier]] and this one — fetch a random patch note from the GitHub releases API into a `PatchNote` page, route it at `/news`, and add a `<Link to="/news">` to the nav bar.

---

## 🔗 See Also

- [[00c - React Cheatsheet II]] — the routing table and `useNavigate` on one page
- [[02 - Spawn Point]] — where the Vite project (and the `index.js` you just wrapped) was created
- [[15 - The Final Boss]] — the capstone quiz that routes between landing page and questions
- [[13 - The Courier]] — previous chapter: fetching the data these pages display

---
