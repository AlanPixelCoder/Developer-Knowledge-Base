# 01. The Rebirth

**Spanish version:** [01 - El Renacimiento.md](01%20-%20El%20Renacimiento.md)

**Course:** React
**Topic:** A first step into rebuilding the Armory Console
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

After the last raid, the Emberfall Armory Console lay in pieces. Wards had been layered by hand for years, and a single change to the tally board meant hunting through brittle scripts in three different places. To keep the Armory standing through the next wave of repairs, the Wardens decided to rebuild its readouts from the ground up — not by stapling more DOM calls together, but by letting the interface describe itself from its data. This is the first step of that rebuild: understanding why React earns its place on the bench.

> [!NOTE]
> The goal here is not to memorize history for its own sake. It is to understand the shift in mindset: describe *what* should appear for a given set of values, and let the library figure out *how* to update the page.

## Why patching fails under pressure

When an Armory clerk updates a wounded Warden's health mid-inspection, that value shows up in at least three places at once — the status strip, the triage list, and the duty roster. With plain DOM manipulation, each of those spots requires its own query and its own assignment. One missed spot leaves the console lying to a tired clerk.

```javascript
// Brittle: three places, three chances to drift
const statusHp = document.querySelector("#status-hp");
statusHp.textContent = "HP: 72 / 100";

const triageHp = document.querySelector("#triage-hp");
triageHp.textContent = "HP: 72 / 100";

const rosterHp = document.querySelector("#roster-hp");
rosterHp.textContent = "HP: 72 / 100";
```

The more pieces of the console that repeat a value, the harder it becomes to keep them honest. The fix is not "be more careful" — the fix is to give each repeating piece a single source of truth.

## A different contract

React asks for a different bargain. Instead of reaching into the page to change nodes, you write small functions called **components** that return markup for the data they are given. You update the data in one place, and every component that uses it re-renders with the new values. React then updates only the parts of the real DOM that actually changed — a process tied to its reconciliation model.

```javascript
function HealthStrip(props) {
  return <div className="health-strip">HP: {props.hp} / 100</div>;
}

// One definition, used in every panel that needs the readout
<HealthStrip hp={72} />
```

> [!TIP]
> Think of components as engraved plates in the Armory: engrave the pattern once, cast it wherever it's needed, and change the engraving only when the rule changes.

## The mindset that carries forward

There are two ideas to lock in before setting up the workshop. First, **declarative**: say what the interface should look like for a given state, rather than issuing a list of DOM mutations. Second, **component-based**: split the console into independent pieces that can be tested, reused, and composed into larger views without leaking update logic between them.

> [!IMPORTANT]
> React is a library, not a framework. It focuses on rendering UI. The rest of the tools you'll reach for over the next chapters are there to solve other problems — and that's by design.

## Output

```text
The Armory Console will describe itself from its data.
Each component will answer for its own slice of that data.
```

## Why this matters

The console rebuild isn't a cosmetic change. By centralizing how a value is rendered, you prevent an entire class of desync bugs. More importantly, you start thinking in terms of *data flow* rather than *DOM surgery*. That shift is what makes the rest of the module — props, state, effects, and routing — feel like natural extensions instead of disconnected tricks. From here, the forge needs to be lit: it's time to scaffold the workspace and mount the first component.

**Next:** [[02 - Spawn Point]]
