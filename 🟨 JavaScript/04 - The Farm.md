# 04. The Farm

**Spanish version:** [04 - El Farmeo.md](04%20-%20El%20Farmeo.md)

**Course:** JavaScript
**Chapter:** 4 — Cooldown Loop
**Topic:** while, for, break, continue
**Tags:** `#javascript` `#loops` `#iteration` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

After a surge, the cabinet's cooling fins need a timed loop. You do not want to copy-paste ten `console.log()` calls — you want the script to repeat work until a condition says stop. That is iteration.

## while: check first

`while` tests its condition before each pass. If it is false at the start, the body runs zero times.

```js
let charge = 0;
while (charge < 3) {
  charge = charge + 1;
  console.log("COOLANT: CYCLE " + charge);
}
console.log("COOLANT: READY");
```

## Output

```text
COOLANT: CYCLE 1
COOLANT: CYCLE 2
COOLANT: CYCLE 3
COOLANT: READY
```

> [!CAUTION]
> Every `while` needs a way for the condition to become false. If nothing inside changes a variable the condition checks, the loop never ends. That is the infinite loop trap.

## for: count known

When you know the exact count, `for` keeps the counter and updates in one place. It is just `while` with bookkeeping moved to the header.

```js
for (let tick = 1; tick <= 4; tick++) {
  console.log("VENT: TICK " + tick);
}
```

## Output

```text
VENT: TICK 1
VENT: TICK 2
VENT: TICK 3
VENT: TICK 4
```

| Clause | When | Purpose |
| :--- | :--- | :--- |
| `let tick = 1` | once | initialize |
| `tick <= 4` | before each pass | test |
| `tick++` | after each pass | update |

## break and continue

`break` leaves the loop entirely. `continue` skips to the next iteration (and runs the update clause in a `for`).

```js
for (let slot = 1; slot <= 6; slot++) {
  if (slot === 3) continue; // skip blocked fin
  if (slot === 5) break;    // emergency shutoff
  console.log("FIN: ONLINE " + slot);
}
```

## Output

```text
FIN: ONLINE 1
FIN: ONLINE 2
FIN: ONLINE 4
```

> [!WARNING]
> `break` and `continue` are powerful, but they make flow harder to follow. Prefer tightening the condition first. Reach for them only for a real exception like a blocked slot or an emergency stop.

## Why the shape matters

The choice between `while` and `for` is about clarity, not capability. Use `while` when the stop is an event ("until stable"), use `for` when the count is fixed ("do exactly N passes"). Either way, the engine repeats mechanically — what prevents bugs is making the stop condition obvious and impossible to miss.

**Next:** [[05 - Inventory]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
