# 12. The Guild Ledger

**Spanish version:** [12 - El Libro del Gremio.md](12%20-%20El%20Libro%20del%20Gremio.md)

**Course:** React
**Topic:** prop drilling, createContext, Provider, useContext, custom provider components, global state patterns
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE_TO_ADVANCED-FF6B35?style=for-the-badge" alt="Intermediate to Advanced">
  <img src="https://img.shields.io/badge/Lessons-01_--_06-7C5CFF?style=for-the-badge" alt="Lessons">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Cyan wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Every Guild Master knows the pain: important records must be accessible to every hall, council chamber, and outpost in the realm. The Guild Ledger is Emberfall's central record of members, contracts, and gold. But passing scrolls from the Grand Hall all the way down to the furthest outpost through a chain of messengers is inefficient and error-prone. This is exactly the problem React faces with **prop drilling**. The solution is the **Context API** — a magical conduit that allows data to flow directly to any component in the tree, no matter how deeply nested.

> [!NOTE]
> **The whole chapter in one sentence**
> The Context API (`createContext`, `Provider`, `useContext`) eliminates prop drilling by providing global-like state accessible to any component in the tree, and custom provider components make this pattern reusable and clean.

---

## 01. The Burden of Prop Drilling

**Prop drilling** occurs when you pass props through multiple layers of components just to reach a deeply nested child. This creates tight coupling, makes refactoring difficult, and clutters intermediate components.

### Example of Prop Drilling

Imagine passing the current guild theme from `App` down to a deeply nested `ThemeButton`:

```javascript
function App() {
  const theme = "ember";
  return <Hall theme={theme} />;
}

function Hall({ theme }) {
  return <Council theme={theme} />;
}

function Council({ theme }) {
  return <ThemeButton theme={theme} />;
}

function ThemeButton({ theme }) {
  return <button>Switch Theme: {theme}</button>;
}
```

`Hall` and `Council` don't need `theme`, but they must pass it down. This is prop drilling.

---

## 02. Creating a Context

The Context API starts with `createContext()`. This creates a Context object that can be used to provide and consume data.

```javascript
import { createContext } from "react";

export const ThemeContext = createContext();
```

By default, `createContext()` can take an optional default value, but it's more common to provide values through a Provider.

---

## 03. Providing Context with Provider

Wrap the component tree that needs access to the data with the Context's `Provider`. Use the `value` prop to pass down anything — strings, objects, functions, or state.

### Mission: Guild Theme Provider

```javascript
import React, { useState, createContext } from "react";
import ThemeSwitcher from "./ThemeSwitcher";
import Home from "./Home";

export const ThemeContext = createContext();

function App() {
  const [theme, setTheme] = useState("dark");

  function toggleTheme() {
    setTheme(theme === "dark" ? "light" : "dark");
  }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <Home />
      <ThemeSwitcher />
    </ThemeContext.Provider>
  );
}

export default App;
```

---

## 04. Consuming Context with useContext

Instead of drilling props, use the `useContext` hook to access the context value directly.

### Mission: Using the Theme

```javascript
import React, { useContext } from "react";
import { ThemeContext } from "./App";

function ThemeSwitcher() {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <button onClick={toggleTheme}>
      Current Theme: {theme} | Switch
    </button>
  );
}

export default ThemeSwitcher;
```

---

## 05. Custom Provider Components - Clean Architecture

For better organization and reusability, extract the context logic into a custom provider component. This keeps `App.js` clean and makes the provider easy to test.

### Mission: UserContext with Custom Provider

```javascript
import React, { createContext, useState } from "react";

export const UserContext = createContext();

export function UserProvider({ children }) {
  const [name, setName] = useState("");

  return (
    <UserContext.Provider value={{ name, setName }}>
      {children}
    </UserContext.Provider>
  );
}
```

### Wrapping the App

```javascript
import React from "react";
import { UserProvider } from "./UserContext";
import UserForm from "./UserForm";
import Results from "./Results";

function App() {
  return (
    <UserProvider>
      <UserForm />
      <Results />
    </UserProvider>
  );
}

export default App;
```

### Consuming in Child Components

```javascript
import React, { useContext } from "react";
import { UserContext } from "./UserContext";

function UserForm() {
  const { name, setName } = useContext(UserContext);

  return (
    <input
      type="text"
      value={name}
      onChange={(e) => setName(e.target.value)}
      placeholder="Enter your adventurer name"
    />
  );
}

export default UserForm;
```

```javascript
import React, { useContext } from "react";
import { UserContext } from "./UserContext";

function Results() {
  const { name } = useContext(UserContext);

  return <h1>Welcome to the Guild, {name}!</h1>;
}

export default Results;
```

---

## 06. When to Use Context

Context is powerful, but not a replacement for all state management. Use it wisely.

| Use Case | Context? | Notes |
| :-- | :-- | :-- |
| Theme (dark/light mode) | Yes | Global UI preference |
| Authentication/User data | Yes | Current user across the app |
| Language/Localization | Yes | App-wide settings |
| Form data in a single form | No | Local state is better |
| Frequent updates (animations) | No | Can cause performance issues due to re-renders |
| Complex state logic with many actions | Maybe | Consider reducers (useReducer) or external libraries |

> [!TIP]
> **Game dev version**
> The Guild Ledger is the single source of truth for Emberfall. Context is like the Guild Archives' magical scrying network — once you inscribe data in the Ledger, any adventurer (component) in the realm can access it directly, no matter how far they are from the Grand Hall.

---

## ⚡ XP Earned: Key Takeaways

- 🚧 **Prop drilling:** Passing props through unnecessary layers is hard to maintain
- 📦 **createContext:** Creates a context object to share data
- 🎁 **Provider:** Wraps components and provides data via the `value` prop
- 🔍 **useContext:** Consumes context data without prop drilling
- 🛠️ **Custom providers:** Encapsulate context logic for cleaner, reusable code
- 🌍 **Global patterns:** Perfect for themes, auth, language, and app-wide data
- ⚖️ **Use wisely:** Not every state should go in context

---

## 🎁 Loot Table: Real-World Use Cases

- 🌓 Dark mode / theme switching across the entire app
- 👤 User authentication and profile data
- 🌐 Multi-language localization
- 🛒 Shopping cart state across pages
- 🔔 Notification systems
- ⚙️ App-wide configuration settings

---

## 🎮 Side Quests: Practice Exercises

1. **Misión básica:** Create a context for a guild motto and consume it in two different components without prop drilling.
2. **Misión intermedia:** Build a theme context with dark/light mode toggle, applying styles dynamically to components.
3. **Misión avanzada:** Create a custom `UserProvider` that manages user login state (logged in/out), sharing it across multiple components.
4. **Misión compleja:** Build a shopping cart context with `addToCart`, `removeFromCart`, and `cartItems` accessible throughout the Emberfall marketplace.
5. **Pelea de jefe:** Forge a complete "Guild Hall" system using Context: manage guild name, member count, and funds in a custom provider, with multiple components reading and updating these values.

---

## 🔗 See Also

- [[11 - The Relic System]] — Hooks like useEffect and useRef
- [[10 - The Forge]] — Forms that can use context for submission data
- [[09 - The Controller]] — Events that update context state
- [[08 - The Health Bar]] — Foundation for state management
- [[13 - The Courier]] — Data fetching that can populate context

---
