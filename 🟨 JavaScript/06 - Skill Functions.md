# 06. Skill Functions

**Spanish version:** [06 - Funciones de Habilidad.md](06%20-%20Funciones%20de%20Habilidad.md)

**Course:** JavaScript
**Topic:** Function declarations, `return`, parameters & arguments, scope, arrow functions and the Combat Log Analyzer project
**Tags:** `#javascript` `#functions` `#scope` `#arrow-functions` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-E67E22?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-29_--_33_%2B_Project-7C5CFF?style=for-the-badge" alt="Lessons 29 to 33 plus project">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

An ability you can only cast once is a cutscene. A **function** is a skill: written once,
invoked by name, any number of times — with inputs that change the outcome. This chapter
teaches the engine to package logic, feed it values and hand back results. By the end you
will build a **combat log analyzer** that computes mean and median damage over a whole
fight. Reference: [[00b - JavaScript Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> A function is a reusable block of code defined with `function`, called by name with
> parentheses `()`, fed **parameters** (the inputs it expects) and giving back a `return`
> value — and **scope** decides which variables each function can see.

---

## 01. First Spell

### What Is a Function?

A **function** is a reusable block of code, written once and executed multiple times by
calling its name. Functions break complex tasks into small, manageable pieces — and give
those pieces names you can read out loud.

```js
function helloWorld() {
  console.log("Hello, World!");
}

helloWorld();
```

Two moments, one name:

- **Declaration** — `function helloWorld() { ... }` writes the spell into the spellbook.
  Nothing runs yet.
- **Call** — `helloWorld()` casts it. The parentheses `()` are not optional decoration:
  every function in JavaScript needs them, at the definition **and** at every call.

### Quest: Broadcast

Print the server announcement three times — write the message once:

```js
function announceRaid() {
  console.log("⚔️ Raid starts in 10 minutes!");
}

announceRaid();
announceRaid();
announceRaid();
```

Three calls, three prints, one body. Change the message in one place and all three change.

---

## 02. The Return Portal

### The `return` Keyword

A function that only prints is a announcement. A function that **returns** gives a value
back to the caller — where it can be stored, compared, or printed:

```js
function countdown() {
  for (let i = 10; i >= 1; i--) {
    console.log(i);
  }
  return "Blast Off! 🚀";
}

console.log(countdown());
```

The loop runs during the call, then the string `"Blast Off! 🚀"` travels back to the call
site, where `console.log` receives it. One call, two effects: the prints inside, the value
outside.

### Naming

Function names are written in **camelCase**, and should name the action: `calculateDamage`,
not `damage2`. A function is a verb — it does something when you call it.

---

## 03. Casting with Inputs

### Parameters vs. Arguments

Functions become skills by accepting **inputs**:

| Term | What it is | Example |
| :--- | :--- | :--- |
| **Parameter** | The placeholder variable in the declaration | `function hit(damage)` |
| **Argument** | The actual value passed at the call | `hit(25)` |

### Quest: Kinetic Strike

The engine's physics lesson, packaged as an ability. Energy equals mass times the square
of velocity — the formula from [[02 - Player Stats]], now a spell that takes any mass:

$$E = m \cdot v^2$$

```js
function kineticStrike(mass) {
  const speed = 3e8;              // 3 × 10⁸, the classic constant
  const energy = mass * (speed ** 2);
  return energy;
}

console.log(kineticStrike(70));
```

The parameter `mass` is a slot; the argument `70` is what fills it. Call the function with
`1` and you have a different spell — same body, new input. That is the entire economics of
functions: **pay once, cast many**.

---

## 04. What a Function Can See

### Scope

**Scope** decides where a variable can be accessed. Two rules cover most programs:

- **Local scope:** a variable declared **inside** a function lives only inside that
  function. Reading it from outside throws a **ReferenceError**.
- **Global scope:** anything **outside** every function's braces is global — visible
  everywhere, changed by anyone, the classic source of "who mutated my config?" bugs.

```js
const guildName = "Ember Wardens"; // global

function reportStatus() {
  let potions = 3;                 // local to reportStatus
  console.log(guildName + " has " + potions + " potions");
}

reportStatus();
// console.log(potions); // ReferenceError: potions is not defined
```

> [!TIP]
> Keep the default **local**. A function that needs a value should receive it as a
> parameter — that is what the last chapter's inputs are for. Global state is a shortcut
> that compounds; local state is a contract you can read from the signature alone.

---

## 05. The One-Liner Variant

### Arrow Functions

Introduced in **ES6 (2015)**, **arrow functions** are a concise syntax for anonymous
functions — ideal for short, single-expression work:

```js
// Traditional function
function greet(name) {
  return "Hello, " + name + "!";
}

// Arrow function
const greetArrow = (name) => "Hello, " + name + "!";
```

The anatomy of an arrow:

```js
const add = (a, b) => {
  return a + b;
};
```

When the body is a **single expression**, both the braces and the `return` can vanish —
the value is returned **implicitly**:

```js
const multiply = (a, b) => a * b;
```

### The Map Trick

Arrow functions pair perfectly with array methods. Squaring a whole stat array in one line:

```js
const numbers = [1, 2, 3, 4, 5];
const squaredNumbers = numbers.map((num) => num ** 2);
console.log(squaredNumbers); // [1, 4, 9, 16, 25]
```

Read it right to left: *for each `num` in `numbers`, return `num ** 2`* — and `map` collects
the results into a new array. Ten lines of `for` loop, replaced by one line of intent.

---

## 06. The Combat Log Analyzer

### Checkpoint: Chapter Recap

- Functions isolate **reusable** blocks; `function` defines, `()` calls.
- `return` hands a value back; without it, a function returns `undefined`.
- Parameters are placeholders; arguments are the values filled in at the call.
- Scope: locals live inside the function, globals leak everywhere — prefer parameters.
- Arrow functions: `(params) => expression`, with implicit return for one-liners.

### Project: Combat Log Analyzer

The capstone: three fight logs — one per build — and the numbers a designer actually needs.
`mean` totals an array and divides by `.length` (from [[05 - Inventory]]); `median` sorts
and grabs the middle. Both take the array as a **parameter**:

```js
const slashDamage = [1932, 2300, 453, 5222, 6733, 7402, 8334];
const critDamage = [936, 2576, 453, 7013, 5489, 7402, 3921];
const spellDamage = [2300, 453, 5222, 989, 6733, 7402, 2789];

function mean(damageArray) {
  let totalDamage = 0;
  for (let i = 0; i < damageArray.length; i++) {
    totalDamage += damageArray[i];
  }
  return totalDamage / damageArray.length;
}

function median(damageArray) {
  let sortedStats = damageArray.sort(function (a, b) {
    return a - b;
  });
  let middleIndex = Math.floor(damageArray.length / 2);
  return sortedStats[middleIndex];
}

console.log("Slash build");
console.log("Mean:", mean(slashDamage));
console.log("Median:", median(slashDamage));
```

One pair of functions, three datasets — swap the argument, keep the logic. That is the
chapter in one program.

### Rune Words: The Palindrome Checker

A final gift from the Deep Halls: an enchanted door opens only for words that read the
same backwards. The checker lowercases the input, reverses it with a loop, and compares:

```js
function isPalindrome(word) {
  let lowerCaseWord = word.toLowerCase();
  let reversedWord = "";

  for (let i = lowerCaseWord.length - 1; i >= 0; i--) {
    reversedWord += lowerCaseWord[i];
  }

  return reversedWord === lowerCaseWord;
}

console.log(isPalindrome("racecar"));  // true
console.log(isPalindrome("moonlight")); // false
```

Note `toLowerCase()`: the door is case-insensitive, and the function takes **one** input —
the word. Everything else is internal machinery the caller never sees. Scope working as
designed.

---

## ⚡ XP Earned: Key Takeaways

- 🧩 Functions package logic under a name; declare with `function`, cast with `()`.
- ↩️ `return` sends a value home; no `return` means `undefined` comes home.
- 🧮 Parameters are the slots; arguments fill them — one call, many inputs.
- 🔒 Locals are invisible outside; globals are visible everywhere — prefer parameters.
- ➡️ Arrow functions: `(name) => expression`, implicit return for one-liners.
- 🗺️ `.map((num) => num ** 2)` — the loop that reads as a rule.

---

## 🎁 Loot Table: Real-World Use Cases

- ⚔️ Abilities and status effects: one function, many sources and targets
- 📊 Stats engines: mean, median, percentiles over combat or telemetry logs
- 🧪 Pure helpers: converters, validators, formatters — the function's best friend
- 🎲 Roll tables and generators packaged for reuse
- 🧹 Keeping the global namespace clean — the real reason scope matters

---

## 🎮 Side Quests: Practice Exercises

1. Write `function greetHero(name)` that returns a greeting; print its result.
2. Turn the fall damage formula from [[02 - Player Stats]] into a function of `fallDistance`.
3. Add a third parameter to `kineticStrike` and print three different masses.
4. Rewrite `multiply` from the arrow section as a traditional function, then back.
5. **Boss fight:** a `rarity(roll)` function using `else if`, called five times with five
   random rolls — prove the function is one spell and five castings.

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — function and arrow syntax on one page
- [[05 - Inventory]] — previous chapter: the arrays these analyzers consume
- [[07 - Character Sheet]] — next chapter: functions promoted to object methods
- [[08 - Living HUD]] — functions wired to real user events

---
