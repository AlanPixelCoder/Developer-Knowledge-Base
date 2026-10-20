# 09. The Controller

**Spanish version:** [09 - El Mando.md](09%20-%20El%20Mando.md)

**Course:** React
**Topic:** synthetic events, onClick, the event object, inline camelCase styles, mouse hover events, focus/blur, tabIndex, keyboard events, e.key, and composing events for accessibility
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

The Emberfall Arena gates have just opened. Spectators flood the stands, challengers step onto the sand, and the guild HUD must respond the instant anyone presses a button, hovers over a banner, or hits a key to ready their stance. Up to this point, your components have been statues — they rendered static markup or changed only when state shifted on their own schedule. Now it's time to take up **The Controller**: React's event system. Every click, tap, hover, focus or keystroke becomes a command you can intercept, validate and route through the Emberfall companion site.

> [!NOTE]
> **The whole chapter in one sentence**
> React wraps native browser events in a synthetic event layer and lets you attach camelCase handlers (like `onClick`, `onMouseOver`, `onFocus`, `onKeyDown`) to elements so your Emberfall HUD reacts to user input immediately while staying accessible to keyboard and assistive tech.

---

## 01. Synthetic Events

> [!NOTE]
> **Key information**
> React wraps native browser events in a **synthetic event wrapper** to guarantee consistency across browsers. Handlers are written in **camelCase** (for example, `onClick`), not lowercase like in HTML.

Events are the user's interactions: clicks, form submissions, page loads and so on. In React you pass **functions** to event handlers, never strings.

### Quest: A Button That Answers

```javascript
function handleClick() {
  alert("hi! you clicked me!");
}

function App() {
  return <h1 onClick={handleClick}>Click Me!</h1>;
}

export default App;
```

**Key rules:**

- Define the handler separately, outside the return statement
- Pass it **without parentheses** (`handleClick`, not `handleClick()`). Adding parentheses would execute the function on render, not on click

---

## 02. The Event Object

Every handler receives an event object `e` (or `event`). React passes it automatically. Use it to reach the element that triggered the event with `e.target`.

### Quest: Paint It Yellow

```javascript
function handleClick(e) {
  e.target.style.backgroundColor = "yellow";
}

function App() {
  return <button onClick={handleClick}>Click me</button>;
}

export default App;
```

> [!WARNING]
> **The mistake everyone makes once**
> Inline styles in JSX use **camelCase**. Instead of `background-color`, write `backgroundColor`. Instead of `font-size`, write `fontSize`.

---

## 03. Mouse Events: Hover

The `onMouseOver` and `onMouseLeave` events let you reveal information when the user hovers over an element.

### Quest: Arena Tooltip

```javascript
import React, { useState } from "react";

function ArenaBanner() {
  const [showTooltip, setShowTooltip] = useState(false);

  return (
    <div>
      <h1
        onMouseOver={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
      >
        Emberfall Arena Banner
      </h1>
      {showTooltip && <div className="tooltip">Sign-ups close at dusk!</div>}
    </div>
  );
}

export default ArenaBanner;
```

---

## 04. Focus and Blur

`onFocus` fires when an element receives focus (it is selected or clicked into). `onBlur` fires when the element loses focus (the user clicks away or tabs out).

### Quest: Highlight the Guild Field

```javascript
function handleFocus(e) {
  e.target.style.backgroundColor = "lightblue";
}

function handleBlur(e) {
  e.target.style.backgroundColor = "white";
}

function GuildForm() {
  return (
    <div>
      <label htmlFor="guildName">Guild Name:</label>
      <input
        type="text"
        id="guildName"
        onFocus={handleFocus}
        onBlur={handleBlur}
      />
    </div>
  );
}

export default GuildForm;
```

Non-form elements (`<div>`, `<img>`) cannot receive focus by default. To enable it, add `tabIndex={0}`.

### Quest: Focus to Zoom an Emblem

```javascript
function handleZoomIn(e) {
  e.target.style.transform = "scale(1.2)";
}

function handleZoomOut(e) {
  e.target.style.transform = "scale(1)";
}

function Emblem() {
  return (
    <img
      src="/emblem.png"
      alt="Emberfall emblem"
      tabIndex={0}
      onFocus={handleZoomIn}
      onBlur={handleZoomOut}
      style={{ transition: "transform 0.2s" }}
    />
  );
}

export default Emblem;
```

---

## 05. Keyboard Events

`onKeyDown` fires the moment a key is pressed. `onKeyUp` fires when it is released. Use `e.key` to identify which key was pressed.

### Quest: HUD Shortcuts

```javascript
function handleKeyDown(e) {
  if (e.key === "h" || e.key === "H") {
    e.target.style.backgroundColor = "gold";
  }
}

function HUD() {
  return <div onKeyDown={handleKeyDown} tabIndex={0}>Press H to highlight the HUD</div>;
}

export default HUD;
```

Common accessibility patterns:

- `e.key === "ArrowUp"` / `e.key === "ArrowDown"` for volume controls
- `e.key === " "` or `e.key === "Enter"` to activate buttons from the keyboard

---

## 06. Composing Events for Accessibility

The best HUD components respond to both mouse and keyboard. An Arena "Going" button must work with a click, a hover, a Tab focus, and an Enter or Space activation.

### Quest: An Accessible "Going" Button

```javascript
import React, { useState } from "react";

function GoingButton() {
  const [goingCount, setGoingCount] = useState(0);
  const [isHovering, setIsHovering] = useState(false);

  function handleGoing() {
    setGoingCount(goingCount + 1);
    alert("You're registered for Arena Night!");
  }

  function handleKeyDown(e) {
    if (e.key === " " || e.key === "Enter") {
      e.preventDefault();
      handleGoing();
    }
  }

  return (
    <button
      tabIndex="0"
      onClick={handleGoing}
      onMouseEnter={() => setIsHovering(true)}
      onMouseLeave={() => setIsHovering(false)}
      onFocus={() => setIsHovering(true)}
      onBlur={() => setIsHovering(false)}
      onKeyDown={handleKeyDown}
      onKeyUp={() => {}}
      style={{
        backgroundColor: isHovering ? "#61DAFB" : "#e0e0e0",
        padding: "10px 20px",
        cursor: "pointer"
      }}
    >
      Going ({goingCount})
    </button>
  );
}

export default GoingButton;
```

> [!TIP]
> **Game dev version**
> Every game HUD combines these events. Menus must be keyboard-navigable (tabIndex + onKeyDown), icons must show tooltips on hover (onMouseOver/onMouseLeave), and buttons must give visual feedback on focus (onFocus). Accessibility is not optional: it is what makes your HUD playable for every adventurer.

---

## ⚡ XP Earned: Key Takeaways

- 🎮 **Synthetic events:** React wraps native events for cross-browser consistency
- 🖱️ **onClick:** define handlers separately and pass them without parentheses
- 🎯 **e.target:** reach the element that triggered the event
- 🎨 **Inline styles:** use camelCase (`backgroundColor`, not `background-color`)
- 🖱️ **Mouse:** `onMouseOver`/`onMouseLeave` for tooltips and hover effects
- 👁️ **Focus:** `onFocus`/`onBlur` for validation and highlighting; `tabIndex={0}` on unfocusable elements
- ⌨️ **Keyboard:** `onKeyDown`/`onKeyUp` with `e.key` for shortcuts; handle Space/Enter for accessibility
- ♿ **Composition:** combine events to serve mouse and keyboard users alike

---

## 🎁 Loot Table: Real-World Use Cases

- 🎯 Interactive buttons in the guild HUD
- 💬 Informational tooltips on hover
- 📝 Form field highlighting on focus
- ⌨️ Keyboard shortcuts in admin panels
- ♿ Interfaces that work for every user

---

## 🎮 Side Quests: Practice Exercises

1. **Basic quest:** create a button that alerts "You forged an Emberfall Sword!" on click.
2. **Intermediate quest:** implement a tooltip that only appears while the mouse hovers an item name.
3. **Advanced quest:** create an input that changes color on focus and reverts on blur.
4. **Keyboard quest:** add a `tabIndex={0}` div that changes color when you press "R", "G" or "B".
5. **Boss fight:** build a fully accessible "Join the Guild" button that works with click, hover, focus and the Space/Enter keys, showing a member counter.

---

## 🔗 See Also

- [[10 - The Forge]] — forms that combine events with state
- [[11 - The Relic System]] — lifecycle and side effects
- [[12 - The Guild Ledger]] — global state for shared interactions

---
