# 11. The Relic System

**Spanish version:** [11 - El Sistema de Reliquias.md](11%20-%20El%20Sistema%20de%20Reliquias.md)

**Course:** React
**Topic:** hooks, class→functional shift, useEffect, side effects, dependency array, cleanup, useRef, state vs refs
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

Deep in the Emberfall vaults lie ancient relics, sealed away for centuries. These artifacts pulse with hidden power that awakens only when certain conditions are met. Much like these relics, React components have powers beyond rendering UI: they can fetch data from the Guild Archives, interact with the DOM directly, set up timers for arena events, and clean up after themselves. These are called **side effects**, and the Relic System (Hooks) gives you the tools to control them.

> [!NOTE]
> **The whole chapter in one sentence**
> Hooks allow functional components to use state and lifecycle features — `useEffect` handles side effects with precise control via the dependency array and cleanup functions, while `useRef` persists mutable values across renders without triggering re-renders.

---

## 01. The Awakening of Hooks

Hooks were introduced in **React 16.8** (February 2019), allowing functional components to use state and lifecycle methods without writing class components.

### From Classes to Functions

Before hooks, class components were verbose. Now, the functional approach is preferred.

**Class Component (Legacy):**
```javascript
class Planet extends React.Component {
  constructor(props) {
    super(props);
    this.state = { realm: "Cinderfall" };
  }
  render() {
    return <h1>The realm of {this.state.realm}</h1>;
  }
}
```

**Functional Component with useState (Modern):**
```javascript
import React, { useState } from "react";

function Planet() {
  const [realm, setRealm] = useState("Emberhold");
  return <h1>The realm of {realm}</h1>;
}
```

---

## 02. useEffect - Awakening the Relics

`useEffect` lets you perform **side effects** — operations that reach outside of React's render cycle. Examples: fetching data, setting up subscriptions, timers, or manually manipulating the DOM.

### Basic Syntax

```javascript
useEffect(function() {
  // Side effect logic
}, [dependencyArray]);
```

### Timing of Execution

- **Empty dependency array `[]`**: Runs once, after the initial render. Perfect for fetching initial data.
- **No dependency array**: Runs after every render. Use with caution!
- **With dependencies `[count]`**: Runs only when `count` changes.

### Mission: Log Realm Entry

```javascript
import React, { useEffect, useState } from "react";

function RealmGate() {
  const [visitors, setVisitors] = useState(0);

  useEffect(() => {
    console.log(`A new adventurer has entered! Total: ${visitors}`);
  }, [visitors]);

  return (
    <button onClick={() => setVisitors(visitors + 1)}>
      Enter Emberhold ({visitors})
    </button>
  );
}

export default RealmGate;
```

---

## 03. Cleanup - Sealing the Relics

Some effects (timers, event listeners, subscriptions) persist after the component unmounts or re-renders. This can cause memory leaks. To prevent this, **return a cleanup function** from `useEffect`.

### Mission: Arena Timer

```javascript
import React, { useState, useEffect } from "react";

function ArenaTimer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(function() {
    const intervalId = setInterval(function() {
      setSeconds(function(prevSeconds) {
        return prevSeconds + 1;
      });
    }, 1000);

    return function() {
      clearInterval(intervalId);
      console.log("Arena timer sealed - relic deactivated");
    };
  }, []);

  return <h1>Arena Time: {seconds}s</h1>;
}

export default ArenaTimer;
```

> [!WARNING]
> **Critical Rule**
> Always clean up effects that create persistent resources. React runs cleanup before unmounting and before re-running the effect.

---

## 04. useRef - Preserving Relic Essence

`useRef` creates a mutable reference that persists across renders. The value is stored in `.current`. **Mutating `.current` does NOT trigger a re-render.**

### Storing Mutable Values

```javascript
import React, { useRef } from "react";

function RelicCounter() {
  const relicCountRef = useRef(0);

  function addRelic() {
    relicCountRef.current += 1;
    console.log("Relics collected:", relicCountRef.current);
  }

  return <button onClick={addRelic}>Collect Relic</button>;
}
```

Notice: clicking doesn't update the UI, but the value persists internally.

---

## 05. useRef - DOM Access

One of the most powerful uses of `useRef` is to directly access DOM elements. This is useful for focusing inputs, measuring elements, or triggering animations.

### Mission: Auto-Focus Guild Portal

```javascript
import React, { useRef, useEffect } from "react";

function GuildPortal() {
  const portalRef = useRef(null);

  useEffect(() => {
    portalRef.current.focus();
  }, []);

  return (
    <input
      ref={portalRef}
      type="text"
      placeholder="Enter your adventurer name..."
    />
  );
}

export default GuildPortal;
```

---

## 06. State vs Refs - Know the Difference

Understanding when to use `useState` vs `useRef` is crucial.

| Aspect | `useState` | `useRef` |
| :-- | :-- | :-- |
| Triggers Re-render | Yes, when setter is called | No, mutating `.current` is silent |
| Purpose | UI state that must be displayed | Mutable values, DOM access, timers |
| Persistence | Persists across renders | Persists across renders |
| Usage | Counts, form values, toggles | Timer IDs, previous values, DOM nodes |

> [!TIP]
> **Game dev version**
> The Relic System mirrors Emberfall's magic. `useEffect` is the ritual that awakens relics when conditions change (deps). Cleanup is the sealing ward that prevents corruption (memory leaks). `useRef` is the essence of an artifact — it persists even when the world re-renders around it.

---

## ⚡ XP Earned: Key Takeaways

- 🪝 **Hooks:** Enable functional components to use state and lifecycle (React 16.8+)
- ⚡ **useEffect:** Manages side effects (fetching, timers, subscriptions, DOM manipulation)
- 📋 **Dependency array:** Controls when effects run (`[]` once, none always, `[deps]` conditionally)
- 🧹 **Cleanup:** Return a cleanup function to prevent memory leaks
- 🔗 **useRef:** Persists mutable values in `.current` without triggering re-renders
- 🎯 **DOM access:** `useRef` gives direct access to DOM elements via the `ref` prop
- ⚖️ **State vs Ref:** Use state for UI-visible data, refs for internal/mutable non-UI data

---

## 🎁 Loot Table: Real-World Use Cases

- 🌐 Fetching data from APIs (Guild Archives, relic catalog)
- ⏱️ Timers, countdowns, and arena clocks
- 🎯 Auto-focusing inputs and managing keyboard focus
- 🎨 Animations and DOM measurements
- 🔌 WebSocket connections with proper cleanup
- 💾 Storing previous values without causing re-renders

---

## 🎮 Side Quests: Practice Exercises

1. **Misión básica:** Create a component that logs "Relic awakened!" to the console only once when it mounts.
2. **Misión intermedia:** Build an arena countdown timer that starts at 10 and counts down to 0, cleaning up properly on unmount.
3. **Misión avanzada:** Create a button that increments a count in state and also tracks total clicks in a ref (without re-rendering side effects).
4. **Misión compleja:** Build an input that auto-focuses on mount and tracks how many times the user typed (using ref for the counter).
5. **Pelea de jefe:** Forge a "Relic Scanner" component that fetches mock data after 2 seconds (using setTimeout in useEffect), shows loading state, and cleans up the timeout if unmounted early.

---

## 🔗 See Also

- [[10 - The Forge]] — Forms that benefit from useEffect validation
- [[12 - The Guild Ledger]] — Context API for global state
- [[09 - The Controller]] — Events and user interactions
- [[08 - The Health Bar]] — Foundation of state management

---
