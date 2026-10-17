# 04. The Farm

**Spanish version:** [04 - El Farmeo.md](04%20-%20El%20Farmeo.md)

**Course:** JavaScript
**Topic:** Loops overview, `while`, `for`, iterators, `break` & `continue`, nested loops and the Season Pass project
**Tags:** `#javascript` `#loops` `#while` `#for` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-E67E22?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-18_--_22_%2B_Project-7C5CFF?style=for-the-badge" alt="Lessons 18 to 22 plus project">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

A hundred identical `console.log()` calls is not a program — it is a punishment. **Loops**
are the engine's promise to repeat a block as many times as you say: a hundred turns of
grinding, a thousand loot rolls, a full calendar of events. By the end you will build a
**season pass tracker** that walks a whole in-game year and flags every double-XP day.
Reference: [[00b - JavaScript Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A loop runs a block of code repeatedly while a condition holds: `while` loops as long as
> the condition stays `true`, `for` loops a counted number of times — and `break` and
> `continue` are the emergency exits.

---

## 01. Duck, Duck, Goose

### What Is a Loop?

In programming, **loops** repeat a block of code based on a condition. Instead of writing
the same line fifty times, you write it once and tell the engine to run it fifty times.

### A First `while`

The classic playground game, simulated: the engine keeps rolling "Duck" until the roll
comes up "Goose":

```js
let randomNumber = Math.floor(Math.random() * 10);

while (randomNumber !== 7) {
  console.log("Duck 🦆");
  randomNumber = Math.floor(Math.random() * 10);
}

console.log("Goose! 🦢");
```

Trace it: roll once, then check. While the roll is not `7`, print a duck and roll again.
The moment a `7` appears, the condition fails and the loop falls through to the goose.

> [!WARNING]
> **The infinite loop.** If nothing inside the loop ever changes the tested condition, the
> engine repeats the block forever — tab frozen, fan spinning. Every `while` needs a path
> to `false`: in the game above, the re-roll inside the block is that path. Check that path
> exists **before** you run the code.

---

## 02. The Lucky Number

### `while` Syntax

```js
while (condition) {
  // Code here
}
```

The condition is tested **before every iteration**. While it is `true`, the block runs;
the first time it comes back `false`, the loop ends. Nothing else is required — no counter,
no structure. Just a condition and a promise to eventually break it.

### Quest: Crack the Vault

A locksmith's drill: keep guessing until the combination opens. The lucky number lives in
a `const`; the guesses are rolled fresh each pass:

```js
const luckyNumber = 7;
let guess = Math.floor(Math.random() * 10) + 1;

while (guess !== luckyNumber) {
  console.log("Nope, it isn't " + guess);
  guess = Math.floor(Math.random() * 10) + 1;
}

console.log("My lucky number is " + luckyNumber + "!");
```

Two rolls of `guess` — one before the loop to feed the first test, one inside to move toward
the exit. That dance is the whole shape of `while`.

---

## 03. The XP Treadmill

### Iterators

A variable updated inside a loop to control execution is an **iterator** — conventionally
named `i`. To **iterate** is to run the loop's body once; when the iterator drives the
condition to `false`, the loop exits cleanly.

### The `for` Loop

`for` packs the whole loop into one line: initialization, condition, and update — three
clauses separated by semicolons:

```js
for (let i = initialValue; condition; updateIterator) {
  // Code here
}
```

| Clause | Example | Role |
| :--- | :--- | :--- |
| Initialize | `let i = 1` | Creates the iterator, once |
| Condition | `i <= 10` | Tested before every iteration |
| Update | `i++` | Runs after every iteration (`i++` = `i = i + 1`) |

### The Grind Message

The detention spell, rewritten as a training drill: one hundred reps, counted by the loop:

```js
for (let i = 1; i <= 100; i++) {
  console.log("Rep " + i + ": I must not tell lies.");
}
```

The three clauses sit in one line and the body stays clean. Compare the `while` version —
you would hand-write the initialization, the test and the increment in three separate
places. `for` keeps them together because they always travel together.

> [!TIP]
> Loop boundaries are where off-by-one bugs live. `i <= 10` runs ten times (`1` through
> `10`); `i < 10` runs nine. Decide whether your count is inclusive, and write the operator
> to match — then check the printed output, not the code.

---

## 04. Emergency Exits

### `continue`

When a condition fires, `continue` **ends the current iteration immediately** and jumps to
the next one — the rest of that pass is skipped:

```js
for (let i = 0; i < 5; i++) {
  if (i === 1) {
    continue;
  }
  console.log(i);
}
// Output: 0, 2, 3, 4
```

### `break`

`break` **terminates the loop entirely**, resuming the program right after the closing
curly bracket — no more iterations, condition notwithstanding:

```js
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}
// Output: 0, 1, 2
```

One skips a turn; the other flips the table. In game logic: `continue` skips the junk mobs
in a spawn wave; `break` stops the wave the moment the boss dies.

---

## 05. The Multiplication Grid

### Nested Loops

A **nested loop** is a loop inside another loop — the moon orbiting Earth while Earth
orbits the sun. The inner loop completes its **entire cycle** for every single iteration
of the outer loop.

### Quest: Damage Matrix

The balancing spreadsheet every tactics game keeps — a multiplication table of attack
multipliers, rows times columns:

```js
for (let i = 1; i <= 3; i++) {
  for (let j = 1; j <= 3; j++) {
    console.log(`${i} * ${j} = ${i * j}`);
  }
}
```

- The **outer** loop (`i`) walks the rows.
- The **inner** loop (`j`) walks the columns of each row — fully, before `i` advances.

Nine lines from two lines of code. The cost: iterations multiply — a 10×10 grid inside a
100-frame loop is 10,000 inner passes per frame. Nest with intent.

> [!NOTE]
> The `` `${i} * ${j}` `` syntax is a **template literal**: backticks around the string,
> `${expression}` to splice a value in. It reads cleaner than `+` concatenation once strings
> get long — used throughout the rest of this vault.

---

## 06. The Season Pass

### Checkpoint: Chapter Recap

- **Loops** execute a block repeatedly.
- `while` loops run as long as a condition is `true` — and need a path to `false`.
- `for` loops run a counted number of times via an iterator: init, condition, update.
- `continue` skips one iteration; `break` exits the loop entirely.
- Nested loops multiply — inner cycles fully, per outer step.

### Project: Season Pass Tracker

The chapter's capstone walks the full calendar of a live-service year and prints every
double-XP day. A leap year check decides the calendar's length — keep the rule exactly as
the designers wrote it:

$$leap = (year \% 4 = 0 \land year \% 100 \neq 0) \lor year \% 400 = 0$$

```js
let eventCount = 0;

for (let year = 2000; year <= 3000; year++) {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log(`✨ [Year ${year}] -> Leap Year Unlocked! (+1 Extra Day Buff)`);
    eventCount++;
  }
}

console.log(`🏆 SEASON COMPLETE: ${eventCount} bonus days in the archives!`);
```

Every piece from the last three chapters is in this program: a `let` counter from
[[02 - Player Stats]], the `&&`/`||` chain from [[03 - Loot Rolls]], modulo arithmetic, and
a `for` loop that runs **1,001 times** to check them all. That is the shape of real code —
nothing new, only combined.

---

## ⚡ XP Earned: Key Takeaways

- 🔁 **Loops** replace repetition with a condition.
- ⚠️ A `while` whose condition never changes is an **infinite loop** — always chart a path to `false`.
- 🎲 `while (guess !== luckyNumber)` — test first, roll again inside the block.
- 🔢 `for (let i = 1; i <= 100; i++)` — initialize, test, update, in one line.
- 🚪 `continue` skips the current iteration; `break` ends the loop for good.
- 🪆 Nested loops: the inner loop runs **fully**, once per outer iteration — costs multiply.
- 📅 The season pass tracker: 1,001 iterations, one leap-year rule, zero repeated code.

---

## 🎁 Loot Table: Real-World Use Cases

- 🔄 Game loops: update, physics tick, render — every frame
- 🎰 Batch rolls: loot tables, gacha pulls, procedural generation seeds
- 📊 Iterating stats: total damage over a fight, average of a score list
- 🗓️ Calendars, season passes, daily-login streaks
- 🧱 Grids: inventories, maps, crafting matrices — nested loops all the way down

---

## 🎮 Side Quests: Practice Exercises

1. Print "Level up!" ten times with a `for` loop and a visible counter.
2. Rewrite the Duck-Goose `while` to stop on a `5` instead of a `7`.
3. Loop `0` to `10`, but `continue` past every odd number — print only evens.
4. Print a 5×5 grid of `*` characters with nested loops.
5. **Boss fight:** a *pity counter* — loop up to 90 pulls, `break` the moment a Legendary
   drops, and print how many pulls it took.

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — loop syntax and exits on one page
- [[03 - Loot Rolls]] — previous chapter: the conditionals loops carry
- [[05 - Inventory]] — next chapter: arrays, the data loops are usually for
- [[06 - Skill Functions]] — loops wrapped in reusable functions

---
