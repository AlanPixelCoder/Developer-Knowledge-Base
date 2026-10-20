# 08. The Health Bar

**Spanish version:** [08 - La Barra de Vida.md](08%20-%20La%20Barra%20de%20Vida.md)

**Course:** React
**Topic:** what state is, `useState`, hook anatomy, the setter function, immutability, updating state, async and timer updates, functional updates
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

A HUD with fixed numbers is a screenshot. The **health bar** is the moment a React
component stops being a painting and becomes a living instrument: it owns data, that data
changes, and every change repaints the screen. This chapter introduces **state** and the
`useState` hook — the core engine behind every counter, potion tally, form field and XP
meter on the Emberfall companion site. Reference: [[00b - React Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> **State** is a component's internal data that is expected to change over time; store it
> with `const [value, setValue] = useState(initialValue)` and every call to the setter
> re-renders the component with the fresh value — but only through the setter.

---

## 01. The Vital Meter

> [!NOTE]
> **Key information**
> State is **internal component data expected to change over time** — counts, cart items,
> form entries, guild XP, potion counts. Unlike props, which arrive from a parent, state
> belongs to the component itself; and when it changes, React **re-renders** the component
> so the UI reflects it.

Ask one question to tell state from everything else: *does this value change while the
component is on screen?*

| Data | Kind | Why |
| :--- | :--- | :--- |
| `username` passed from `App` | **prop** | Comes from the parent; the child only displays it |
| Avatar path `/avatar.png` | constant | Never changes; a string in the markup is enough |
| `hp` of the guild's raid boss | **state** | Drops every round while the component is visible |
| Number of potions in the satchel | **state** | Goes up and down as the player drinks |

React gives components exactly two ways to remember: **props** (inherited downhill from
[[07 - Trade Routes]]) and **state** (owned, private, mutable only through its setter).
This chapter is about the second one.

---

## 02. First Heartbeat

### Your First Piece of State

`useState` is a **hook** — a function React lets regular components use. Import it, call
it at the top of the component, and unpack what it gives back:

```js
import React, { useState } from "react";

function TextMessage() {
  const [text, setText] = useState("Hello World!");
  return (
    <div>
      <h1>Text: {text}</h1>
    </div>
  );
}
```

Line by line:

- `import React, { useState } from "react";` — `useState` is a **named** import, so it
  takes curly braces; `React` stays the default import.
- `useState("Hello World!")` — creates a piece of state whose **initial value** is the
  string `"Hello World!"`.
- `const [text, setText] = useState(...)` — **array destructuring** unpacks the hook's
  answer into two things: the state variable and its setter.
- `{text}` inside the JSX prints the current value on screen.

### Quest: Potion Satchel

Write a `PotionSatchel` component whose state starts at `3` and renders
`<h1>Potions: {potions}</h1>`:

```js
const [potions, setPotions] = useState(3);
```

Render it from `App` (export it with `export default`, as in
[[05 - Building Blocks]]). Nothing changes on its own yet — you have built the meter, not
the heartbeat. The heartbeat is the setter, next section.

---

## 03. Anatomy of a Heartbeat

### What `useState` Returns

> [!NOTE]
> **Key information**
> `useState(initialValue)` returns a **two-element array**: `[stateVariable, setter]`.
> The setter's name is by convention `set` + the state name — `text` gets `setText`,
> `potions` gets `setPotions`. The initial value can be **any JavaScript type**: string,
> number, boolean, array, object.

| Piece | Name convention | Role |
| :--- | :--- | :--- |
| State variable | the noun: `text`, `potions`, `scores` | Holds the current value; read it in JSX |
| Setter | `set` + noun: `setText`, `setPotions` | The **only** way to change the value; triggers a re-render |

Three rules of the anatomy:

1. **Destructure with `const`.** The pair itself never changes — `const [text, setText] = ...`.
   Only the *value inside* `text` changes.
2. **Call the hook at the top level** of the component — never inside a condition or a
   loop, or React loses track of how many pieces of state exist.
3. **One name, one slot.** Want a second value? Call `useState` again:
   `const [hp, setHp] = useState(100);`.

---

## 04. The Golden Rule

### Never Touch State Directly

Here is the line that separates a React app from a broken one:

```js
text = "Catch ya next time!";                 // ❌ reassigns the variable — nothing more
setText("Catch ya next time! 👋");             // ✅ tells React the value changed
```

> [!WARNING]
> **The mistake everyone makes once — and the rule that is never broken**
> **Never mutate or reassign state directly; always use the setter.** The plain assignment
> `text = "..."` bypasses React's render engine: the variable in memory changes, the screen
> does not, and you are staring at a **stale UI**. Only `setText(...)` notifies React.

Why the ceremony? React has no way to know `text` changed unless you say so. The setter is
the notification:

- **Any setter call re-renders the component** — the function runs again with the new
  value, and the JSX is redrawn.
- The same applies to mutation: `potions.push(...)` on an array or
  `text = text + "!"` will not notify anyone. Build the **new** value and hand it to the
  setter.

### Quest: Catch You Next Time

Take the `TextMessage` component and add a second state, `sent`, starting at `false`.
Render `{sent ? "Delivered ✅" : "Waiting…"}` beside the text. Then write the two lines of
`text = ...` and `setText(...)` from this section, save, and watch which one moves the
screen. One line does nothing; the other repaints.

---

## 05. The Ticking Clock

### Async and Timer Updates

State is how components survive **time**. A stopwatch is one `useState`, one timeout and
one setter — the update happens asynchronously, a full second after the last render:

```js
import React, { useState } from "react";

function Stopwatch() {
  const [seconds, setSeconds] = useState(0);

  function tick() {
    setTimeout(function () {
      setSeconds(seconds + 1);
    }, 1000);
  }

  return (
    <div>
      <h1>Seconds: {seconds}</h1>
      <button onClick={tick}>Start</button>
    </div>
  );
}
```

Read the sequence:

1. Render happens; `seconds` is captured inside the closure of `tick`.
2. `setTimeout` schedules the callback **1000 ms later** — the component has moved on.
3. The callback runs, calls `setSeconds(seconds + 1)`, and React re-renders with `+1`.

Two notes for the road:

- `onClick={tick}` — handler passed **without** parentheses — is fully covered in
  [[09 - The Controller]]; here it is only the trigger for the timer.
- The value `seconds + 1` was computed from the value **at render time**. For a single
  scheduled update that is fine; for updates that pile up, you need the next section's
  formula.

> [!TIP]
> **Game dev version**
> This is a game loop in miniature: schedule work, let time pass, mutate state, let the
> engine redraw. Swap `setTimeout` for `requestAnimationFrame` and you have the frame
> ticker every HUD runs on.

---

## 06. The Rewind Formula

### Functional Updates

When the **new state derives from the previous state**, hand the setter a function instead
of a value. That function receives the latest state as its argument:

```js
const [volume, setVolume] = useState(50);

function raiseVolume() {
  setVolume((prevVolume) => Math.min(prevVolume + 5, 100));
}
```

Read it: *set the volume to whatever `prevVolume` was, plus five, capped at 100.* The
arrow function `(prevVolume) => ...` is the **functional update form**:

| Form | What the setter receives | Use it when |
| :--- | :--- | :--- |
| `setValue(5)` | a fixed value | the new state does not depend on the old one |
| `setValue((prev) => ...)` | a function of the **latest** state | the new state is derived from the previous one |

Why it matters: between the moment you *schedule* an update and the moment React
*renders* it, other updates may have landed. The value form still uses your old snapshot;
the functional form always receives the **most recent** state — which is exactly how it
avoids async-render bugs: missed ticks, wrong counts, a stopwatch that skips seconds.

### Quest: Mute Button

Add the mirror of `raiseVolume` — a `lowerVolume` that subtracts five and floors at zero:

```js
setVolume((prevVolume) => Math.max(prevVolume - 5, 0));
```

Then use both in one component with two buttons and prove that hammering them in any
order always lands on a multiple of five between 0 and 100. No snapshot ever went stale —
the formula read the latest state every time.

---

## ⚡ XP Earned: Key Takeaways

- 🧠 **State** is internal component data expected to change over time — owned by the
  component, not handed down as props.
- 💉 `useState(initialValue)` returns `[value, setValue]`; the initial value can be **any**
  JavaScript type.
- 🏷️ The setter is named `set` + state name — `text` → `setText` — and **every** setter
  call re-renders the component.
- 🚫 **Never** reassign or mutate state directly — `text = "..."` leaves a stale UI; only
  `setText(...)` notifies React.
- ⏱️ Timers update state asynchronously: schedule, wait, set, repaint.
- 🔁 When new state derives from old state, use the functional form
  `setValue((prev) => ...)` for the latest value, always.

---

## 🎁 Loot Table: Real-World Use Cases

- ❤️ Health, mana, XP and stamina meters that tick during a fight
- 🛒 Shopping carts, like counts and view counters on any product page
- ⏱️ Stopwatches, countdowns, cooldown timers and match clocks
- 🔢 Progress indicators: uploads, wizard steps, playlist position
- 🎛️ Sliders and toggles — volume, brightness, settings that move as you drag

---

## 🎮 Side Quests: Practice Exercises

1. Build `PotionSatchel` from section 02 with two states: `potions` (number) and
   `label` (string).
2. Take the direct assignment `text = "..."` from section 04, run it in a component, and
   describe in one sentence why the screen did not move.
3. Write a `MatchClock` that adds one second per tick with `setSeconds(seconds + 1)` and
   start it from a button.
4. Write `raiseVolume` and `lowerVolume` for a `ManaBar` capped at 100 and floored at 0,
   both using the functional form.
5. **Boss fight:** build a full **`ManaBar`** — `const [mana, setMana] = useState(50);` —
   with a `regen` action (`+10`, capped at 100), a `cast` action (`-25`, floored at 0) and
   a displayed percentage, every update written in the functional form so spam-clicking
   both buttons never desyncs the bar.

---

## 🔗 See Also

- [[00b - React Cheatsheet]] — `useState`, the setter and immutability rules on one page
- [[05 - Building Blocks]] — previous chapter: the components that own the state
- [[06 - The Skill Tree]] — previous chapter: where state lives in the parent-child tree
- [[07 - Trade Routes]] — previous chapter: props, the other half of React's data story
- [[09 - The Controller]] — next chapter: the events that change state
- [[11 - The Relic System]] — later: `useEffect` and `useRef`, the hooks that handle time

---
