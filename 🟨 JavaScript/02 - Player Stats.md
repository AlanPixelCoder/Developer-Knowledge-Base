# 02. Player Stats

**Spanish version:** [02 - Atributos del Jugador.md](02%20-%20Atributos%20del%20Jugador.md)

**Course:** JavaScript
**Topic:** `let` & `const`, naming conventions, data types, arithmetic operators, exponents and the Fall Damage project
**Tags:** `#javascript` `#variables` `#data-types` `#operators` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Lessons-06_--_10_%2B_Project-7C5CFF?style=for-the-badge" alt="Lessons 06 to 10 plus project">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Every RPG character is a pile of numbers waiting for a name. This chapter teaches the
engine to **remember** — names, hit points, prices, flags — with variables and data types,
and to **compute** damage, tips and gravity with arithmetic and exponents. By the end you
will build a **fall damage calculator** from a real physics formula. Syntax reference:
[[00b - JavaScript Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A variable is a labeled box inside the engine's memory; the four data types (Number,
> String, Boolean, Undefined) are what you are allowed to put in the box, and the
> arithmetic operators are what you are allowed to do with it.

---

## 01. Save Slots

### What Is a Variable?

A **variable** is a container that stores a data value so the program can reference and
manipulate it later. Every variable has a **name** and holds a **value**.

### `let` and `const`

JavaScript declares variables with two keywords:

| Keyword | Use it when | Reassignable? |
| :--- | :--- | :--- |
| `let` | The value is expected to **change** | Yes |
| `const` | The value **stays constant** for the whole program | No — throws an error |

```js
const playerName = "Ashwalker";
let hitPoints = 100;
```

- `playerName` is a `const`: a character's name does not change mid-run.
- `hitPoints` is a `let`: the whole point of a health variable is that things hit it.

The general rule: **default to `const`**, and demote to `let` only when you know the value
must change. A `const` you never reassign cannot be reassigned by accident later.

### Assignment

The equal sign `=` is the **assignment operator**: it places a value into a variable.

```js
hitPoints = 85; // legal: hitPoints was declared with let
```

Reassigning a `const` is a **TypeError** at runtime — the engine refuses:

```js
const maxLevel = 50;
maxLevel = 51; // TypeError: Assignment to constant variable
```

### Naming: camelCase

Multi-word variable names are written in **camelCase**: first word all lowercase, first
letter of every following word capitalized.

```js
let playerClass;      // ✅ camelCase
let criticalHitRate;  // ✅ camelCase
let Player_Class;     // ❌ not camelCase
```

Names should say what the value *is*. `let x = 42` compiles; `let orbCount = 42` survives
a code review.

### Quest: Character Roster

Declare one `const` and one `let` for your own character — name, class, level, HP — and
print them with `console.log()` from [[01 - Insert Coin]]:

```js
const heroName = "Ashwalker";
const heroClass = "Lantern Knight";
let heroLevel = 12;
let heroHP = 140;

console.log(heroName + " the " + heroClass + ", level " + heroLevel);
```

---

## 02. What's in the Box

### The Four Core Data Types

JavaScript is **dynamically typed**: the keyword does not declare a type — the *value*
carries its own. Four primary types cover most early programs:

### Number

Integers and decimals — whole values, fractions, prices, damage, coordinates:

```js
let patchVersion = 1.4;
let swordDamage = 27;
```

### String

Text, wrapped in double `"..."` or single `'...'` quotes:

```js
let battleCry = "For the Ninth Floor!";
const guildName = "Ember Wardens";
```

Strings concatenate with `+` — note the spaces, which do not appear on their own:

```js
console.log(battleCry + " " + guildName);
// For the Ninth Floor! Ember Wardens
```

### Boolean

Exactly two values, always lowercase: `true` or `false`. Booleans answer the questions the
engine will keep asking: is the boss alive? Is the door locked? Is the player online?

```js
let hasKey = true;
let bossDefeated = false;
```

### Undefined

A variable that has been **declared but never given a value** holds `undefined` — not
`null`, not zero, not an empty string. `undefined` means "nobody has put anything in this
box yet":

```js
let endDate;
console.log(endDate); // undefined
```

> [!WARNING]
> **`undefined` travels.** Forgetting to initialize a variable is one of the most common
> first bugs: `let score; console.log(score + 10)` prints `NaN` — Not a Number — because
> the engine tried to add 10 to nothing. Initialize your variables.

---

## 03. The Forge: Arithmetic Operators

### The Operator Set

JavaScript supports the standard arithmetic operators:

| Operator | Name | Example | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Modulo: The Parity Operator

`%` returns the **remainder** of a division — the single most useful operator in game
logic. `x % 2` is `0` when x is even and `1` when it is odd; that one test drives
turn-based alternation, item stacking, grid checkers and loot rarity rolls everywhere.

```js
let turn = 5;
if (turn % 2 === 0) {
  console.log("Player's turn");
} else {
  console.log("Enemy's turn");
}
```

(The `if` is formalized in [[03 - Loot Rolls]] — the comparison is the point here.)

### Order of Operations

Standard precedence applies; **parentheses `()` override it** and are evaluated first.
Compare the tavern bill with and without them:

```js
const stew = 2.99;
const ale = 0.99;
let tip = (stew + ale) * 0.2;   // 0.796 — tip on the meal

let wrongTip = stew + ale * 0.2; // 3.188 — tip on the ale alone
```

Always parenthesize what you mean. The engine follows precedence rules; your reader
should not have to.

### Exponents

JavaScript writes powers with the double asterisk `**` — there is no superscript notation
in code:

```js
console.log(2 ** 3); // 8, i.e. 2³
```

Exponents bind tighter than multiplication and division, which bind tighter than addition
and subtraction — the same pyramid you know from math class.

### Quest: Frostforge Temperature

The Emberfall forge runs in Fahrenheit; the design doc quotes Celsius. Convert with the
standard formula, and print both:

```js
const fahrenheit = 68;
const celsius = (fahrenheit - 32) / 1.8;
console.log(celsius); // 20
```

The parentheses matter: subtract first, then divide. Remove them and the engine divides
32 by 1.8 before subtracting — a number no forge would survive.

---

## 04. The Physics Engine

### BMI-Style Formulas in Games

Many game formulas follow the same shape as the Body Mass Index — a quantity divided by
the **square** of another:

$$bmi = \frac{mass}{height^2}$$

```js
const mass = 70;
const height = 1.75;
const bmi = mass / (height ** 2);
console.log(bmi); // 22.857...
```

Note the parentheses around `height ** 2`: without them, the engine computes
`mass / height ** 2` correctly by precedence, but surrounding the power makes the intent
readable — and protects the formula when you later fold it into a bigger expression.

Games reuse this shape constantly: movement speed scales with mass, area-of-effect
damage falls off with the square of the distance, armor mitigation divides by squared
resist values. Learn to read `a / (b ** 2)` as a unit.

### Fall Damage: The Project

Every platformer's silent killer — fall damage — is arithmetic. The classic design: damage
grows with the **square** of the fall distance, so a slip hurts and a leap from the
battlements ends the run.

```js
const safeDrop = 3;           // blocks — no damage below this
let fallDistance = 12;        // blocks
const fallDamage = (fallDistance - safeDrop) ** 2;

console.log("Fall distance: " + fallDistance + " blocks");
console.log("Fall damage: " + fallDamage + " HP");
```

Tune the two knobs — `safeDrop` and the exponent — and you have shipped a mechanic.

### Gravity Across the System: Planet Weight

On the Emberfall star-chart campaign, the same character lands on different worlds. Weight
on another planet is Earth weight times that planet's gravity factor (Mars: `0.38`):

```js
const earthWeight = 210;
const marsWeight = earthWeight * 0.38;

console.log("Your weight on Earth is " + earthWeight + " pounds.");
console.log("Your weight on Mars is " + marsWeight + " pounds.");
```

Same character, same code, different world — one constant changes the entire campaign.

---

## 💎 Bonus Loot: Three Errors Every Debugger Meets

> [!NOTE]
> **Where "bug" comes from**
> On September 9, 1947, the team operating the Harvard Mark II — including pioneer
> **Grace Hopper** — found a moth trapped in a relay, taped it into the log book and
> labeled it the "First actual case of bug being found." The technical sense of *bug*
> predates even that, going back to Edison in 1878 — but the moth got the credit.

JavaScript reports failures in three flavors you will meet in your first hour:

| Error | When | Classic trigger |
| :--- | :--- | :--- |
| **SyntaxError** | The code itself is invalid | Missing `)`, `}` or quote |
| **ReferenceError** | Using a variable that was never declared | Typo in the variable name |
| **TypeError** | Misusing a data type | Reassigning a `const`, calling `x()` when `x` is not a function |

```js
// SyntaxError:  missing closing quote
console.log("Emberfall");

// ReferenceError: lanternOil was never declared
console.log(lanternOil);

// TypeError: cannot reassign a constant
const oilLevel = 10;
oilLevel = 0;
```

Read the error **name** first, the message second. SyntaxError means fix the punctuation;
ReferenceError means find the declaration; TypeError means the value is not what the
operation needs.

---

## ⚡ XP Earned: Key Takeaways

- 📦 **`const` by default, `let` when it must change.** Reassigning a `const` is a TypeError.
- 🐫 **camelCase** names: `criticalHitRate`, never `Critical_Hit_Rate`.
- 🧳 Four core types: **Number**, **String**, **Boolean**, **Undefined** — the value carries the type.
- ➕ Operators: `+ - * / % **` — modulo finds remainders, `**` raises to a power.
- 🧮 Parentheses override precedence; `(fahrenheit - 32) / 1.8` only works with them.
- 🪂 Fall damage, BMI and gravity all follow the same shape: **divide or square** a second quantity.
- 🐛 Three error names to triage: **SyntaxError** (punctuation), **ReferenceError** (undeclared name), **TypeError** (wrong type).

---

## 🎁 Loot Table: Real-World Use Cases

- 💰 Price and tax calculation — checkout carts are arithmetic
- ❤️ HP, mana, stamina: every stat is a `let`
- 🧪 Unit conversion: temperature, currency, metric/imperial
- 🎲 Damage formulas: base × modifier, squared falloff, percentage mitigation
- 🪐 Scaling across levels, zones or planets — change one constant, rebalance the world

---

## 🎮 Side Quests: Practice Exercises

1. Declare a `const` item price and a `let` quantity; print the line total.
2. Convert 98.6°F to Celsius and print both values in one sentence.
3. Compute `7 ** 3` and verify the result with repeated multiplication.
4. Write a `let` named `lanternOil` that starts full and burns down to `0` — three assignments.
5. **Boss fight:** build a *critical hit calculator*: base damage, a strength modifier, and
   a `** 2` scaling on distance — print a full combat log line for a hit at 4 blocks.

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — types, operators and declarations on one page
- [[01 - Insert Coin]] — previous chapter: the console and `console.log()`
- [[03 - Loot Rolls]] — next chapter: conditionals and decision-making
- [[06 - Skill Functions]] — where these formulas become reusable abilities

---
