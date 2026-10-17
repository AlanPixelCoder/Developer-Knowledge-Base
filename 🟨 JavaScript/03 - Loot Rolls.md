# 03. Loot Rolls

**Spanish version:** [03 - Tiradas de Botín.md](03%20-%20Tiradas%20de%20Bot%C3%ADn.md)

**Course:** JavaScript
**Topic:** Control flow, `if` / `else` / `else if`, comparison and logical operators, `Math.random()`, nested conditionals and the Rarity Roll project
**Tags:** `#javascript` `#control-flow` `#conditionals` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-11_--_17_%2B_Project-7C5CFF?style=for-the-badge" alt="Lessons 11 to 17 plus project">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

So far the engine has executed everything, in order, every time. This chapter hands it a
choice. **Conditionals** let a program fork the road: crit or normal hit, rare drop or
common, gate opens or stays shut — and `Math.random()` supplies the dice. By the end you
will build a **dungeon die** that rolls a random verdict on your question. Reference:
[[00b - JavaScript Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> An `if` statement tests a condition and runs its block **only** when the test comes back
> `true`; everything else in the chapter — `else`, `else if`, comparisons, logical operators,
> nesting — is a variation on that one fork.

---

## 01. Flip the Coin

### Control Flow

By default, programs run line by line, top to bottom — no surprises. **Control flow**
statements break that conveyor belt: they let the engine evaluate a condition and execute
one block of code instead of another.

### `Math.random()`

The ingredient every loot table needs: `Math.random()` generates a decimal from `0`
(inclusive) to `1` (exclusive) — `0.0`, never quite `1.0`.

To get a **random integer** in a range, multiply by the range size and round down with
`Math.floor()`:

```js
Math.floor(Math.random() * 10);   // a whole number from 0 to 9
Math.floor(Math.random() * 6) + 1; // a die roll: 1 to 6
```

### Quest: Initiative Flip

The classic first coin flip. The engine rolls a number above or below `0.5` and picks a side:

```js
let num = Math.random();

if (num > 0.5) {
  console.log("Heads");
} else {
  console.log("Tails");
}
```

Run it a few times. Half the runs print `Heads`, half `Tails` — a working coin, ten lines
into the course.

---

## 02. The Gate

### The `if` Statement

`if` tests a condition for truth and executes the code inside its curly braces `{}` **only
if** the condition evaluates to `true`. If it is `false`, the block is skipped entirely:

```js
if (condition) {
  // Do something
}
```

A live example — the gatekeeper at the Deep Halls checks your level before letting you in:

```js
let level = 14;

if (level >= 15) {
  console.log("Access granted: Deep Halls");
}
```

The condition lives inside parentheses `()`. The tested value is a **Boolean expression**:
something that comes back `true` or `false` — which is where comparison operators come in.

### Comparison Operators

Used to compare two values inside a condition:

| Operator | Meaning | Example | Result |
| :--- | :--- | :--- | :--- |
| `===` | Strict equal | `5 === 5` | `true` |
| `!==` | Strict not equal | `5 !== 3` | `true` |
| `>` | Greater than | `5 > 3` | `true` |
| `>=` | Greater than or equal | `5 >= 5` | `true` |
| `<` | Less than | `5 < 3` | `false` |
| `<=` | Less than or equal | `3 <= 5` | `true` |

> [!WARNING]
> **Three equals, always.** `=` assigns; `===` compares. Writing `if (level = 15)` assigns
> 15 to `level` and the condition is truthy by accident — the classic bug that looks like
> logic but is really a typo. In conditionals, reach for `===` and `!==` every time.

---

## 03. The Two Doors

### The `else` Clause

`else` is an optional clause at the end of an `if` that handles the case where the condition
came back `false`:

```js
if (condition) {
  // Do something
} else {
  // Do something else
}
```

Every road splits both ways. The outpost guard waves you through or turns you around:

```js
let torchLit = true;

if (torchLit) {
  console.log("The corridor lights up ahead.");
} else {
  console.log("You bump into the wall in the dark.");
}
```

Exactly one branch runs — never both, never neither. That is the entire contract.

---

## 04. The Loot Table

### The `else if` Chain

`else if` evaluates multiple conditions in sequence, between the opening `if` and the
closing `else`:

```js
if (conditionA) {
  // Do this
} else if (conditionB) {
  // Do this, instead
} else {
  // Do this if none of the above are true
}
```

Conditions are tested **top to bottom** and the first `true` wins — the rest of the chain is
never examined. That order is not decoration: it is the logic.

### Quest: Rarity Roll

A loot rarity table is an `else if` chain with the thresholds ordered carefully. Read it
from the top; a `96` falls into the first branch that claims it:

```js
let roll = 96;

if (roll >= 95) {
  console.log("Legendary drop!");
} else if (roll >= 80) {
  console.log("Epic drop.");
} else if (roll >= 50) {
  console.log("Rare drop.");
} else {
  console.log("Common drop. Better luck next run.");
}
```

> [!NOTE]
> Flip the order — test `roll >= 50` first — and a `96` prints "Rare". The chain stops at
> the first `true`, so **order from most restrictive to least**. The same trap guards every
> damage table, every affinity chart and every weather system you will ever write.

### Air Quality, Affinity-Style

Ranges work the same way. An elemental affinity check is the pH-scale pattern with game
words — test the band the value falls into:

```js
let fireResist = 65;

if (fireResist >= 0 && fireResist <= 50) {
  console.log("Vulnerable");
} else if (fireResist >= 51 && fireResist <= 100) {
  console.log("Resistant");
} else {
  console.log("Immune");
}
```

The `&&` in those ranges is a logical operator — the next section.

---

## 05. Combining Conditions

### Logical Operators

Logical (Boolean) operators combine and evaluate multiple conditions at once:

| Operator | Name | Returns `true` when |
| :--- | :--- | :--- |
| `&&` | AND | **Both** conditions are true |
| `\|\|` | OR | **At least one** condition is true |
| `!` | NOT | The condition is **false** — reverses it |

```js
let hasTicket = true;
let isVip = false;

console.log(hasTicket && isVip);  // false — both must be true
console.log(hasTicket || isVip);  // true  — one is enough
console.log(!isVip);             // true  — flips false to true
```

The affinity range from the last section is `&&` in its natural habitat:

```js
let aqi = 65;

if (aqi >= 0 && aqi <= 50) {
  console.log("Good");
} else if (aqi >= 51 && aqi <= 100) {
  console.log("Moderate");
} else {
  console.log("Hazardous");
}
```

### Quest: The Dungeon Die — Project

The chapter's capstone rolls a random verdict on any question, an `else if` chain fed by
`Math.random()`:

```js
const question = "Will the Ember Key drop this run?";
const randomNumber = Math.floor(Math.random() * 9) + 1;
let answer = "";

if (randomNumber === 1) {
  answer = "Yes — definitely.";
} else if (randomNumber === 2) {
  answer = "It is decidedly so.";
} else if (randomNumber === 3) {
  answer = "Reply hazy, try again.";
} else {
  answer = "Very doubtful.";
}

console.log("Question: " + question);
console.log("Oracle: " + answer);
```

Run it five times; the answer changes every run because the roll happens **before** the
chain. Randomness in, branching out — that is a loot table in miniature.

---

## 💎 Bonus Loot: Nested Ifs

A **nested if** is an `if` inside another `if`. The inner condition is only examined when
the **outer** one is `true` — gates in front of gates. Emberfall's weather system works
exactly like this: first decide if the sky event is sunny, then decide what that means for
the temperature:

```js
let weather = "Sunny";
let temperature = 85;

if (weather === "Sunny") {
  if (temperature > 80) {
    console.log("Desert zone is open. Pack water.");
  } else {
    console.log("Mild day — good climbing weather.");
  }
} else {
  console.log("Indoor dungeon day. Raid the Deep Halls instead.");
}
```

Three outcomes, two tests, one readable tree. Nest only as deep as the decision really is —
three levels of nesting is usually a sign the conditions want names.

---

## ⚡ XP Earned: Key Takeaways

- 🔀 **Control flow** lets the engine choose paths instead of running every line.
- 🎲 `Math.random()` returns 0–1; `Math.floor(Math.random() * n)` returns 0 to n−1.
- 🚪 `if (condition)` runs its block only when the condition is `true`.
- 🚪 The `else` clause catches everything the `if` rejected.
- 🧮 `else if` chains test top to bottom; **first `true` wins** — order thresholds most-restrictive-first.
- ⚖️ Comparisons: `===`, `!==`, `>`, `>=`, `<`, `<=` — three equals, always.
- 🔗 Logic: `&&` (both), `||` (either), `!` (not) — combine tests into ranges and gates.
- 🪆 Nested `if`s evaluate the inner gate only when the outer one opens.

---

## 🎁 Loot Table: Real-World Use Cases

- 🎰 Loot tables, gacha rolls and crit chances
- 🚦 Gate checks: level requirements, feature flags, permission tests
- 🌦️ Weather, affinity and status-effect systems
- 🎯 Input validation: "only accept a number between 1 and 99"
- 🔐 Unlock logic: key + door + boss-defeated, combined with `&&`

---

## 🎮 Side Quests: Practice Exercises

1. Roll `Math.floor(Math.random() * 20) + 1` — a d20 — and print the number.
2. Write an `if`/`else` that prints "Level too low" or "Welcome" based on a level variable.
3. Build a three-tier loot table: Common, Rare, Legendary.
4. Combine two Booleans with `&&`, `||` and `!` and print all six results.
5. **Boss fight:** a nested-conditional mount check — if the player has the saddle **and**
   the creature is tamed, print "Mount ready"; if only one is true, print which piece is
   missing; if neither, print "What creature?".

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — operators and conditional syntax on one page
- [[02 - Player Stats]] — previous chapter: the values these conditions test
- [[04 - The Farm]] — next chapter: loops, when one decision is not enough
- [[07 - Character Sheet]] — conditionals living inside object methods

---
