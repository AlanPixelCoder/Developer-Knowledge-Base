# 00b. JavaScript Cheatsheet

**Spanish version:** [00b - Chuleta de JavaScript.md](00b%20-%20Chuleta%20de%20JavaScript.md)

**Course:** JavaScript
**Topic:** Quick reference for the core language: console, variables, types, operators, conditionals, loops, arrays, functions and objects
**Tags:** `#javascript` `#cheatsheet` `#reference` `#core-language` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Beginner to intermediate">
  <img src="https://img.shields.io/badge/Covers-Chapters_01_--_07-7C5CFF?style=for-the-badge" alt="Chapters 01 to 07">
  <img src="https://img.shields.io/badge/Type-Cheatsheet-00C2A8?style=for-the-badge" alt="Cheatsheet">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

One page for the whole core language. Every statement here was introduced in
[[01 - Insert Coin]] through [[07 - Character Sheet]] — nothing on this sheet is new. The
DOM, styles, events and `addEventListener` live in [[00c - JavaScript Cheatsheet II]].

> [!TIP]
> Print it, or keep it in a split pane next to your editor. A page written without checking
> this sheet is how `let` soup happens: redeclaring variables because nothing on the sheet
> looked wrong.

**The running theme of this module: Emberfall**, a roguelike dungeon crawler. Every exercise
builds part of its game logic: the shop receipt, the fall-damage calculator, the dungeon die,
the season pass, the inventory seed, the combat log analyzer, the character sheet. The code
is the same code a real studio ships — only the words change.

---

## 🖥️ Console & Comments

```js
console.log("The dungeon opens at dawn.");
console.log(5 + 3); // evaluates first: 8

// Single-line comment
/*
  Multi-line
  comment
*/
```

| Statement | What it does |
| :--- | :--- |
| `console.log(value)` | Prints to the Debug Console — your eyes while debugging |
| `// comment` | Ignored by the engine; documentation for humans |
| `/* ... */` | Multi-line comment; the engine skips everything inside |

---

## 📦 Variables & Types

### Declaring

| Keyword | Reassign? | Scope | Use it for |
| :--- | :--- | :--- | :--- |
| `const` | ❌ | Block | The default — anything that keeps its value |
| `let` | ✅ | Block | Counters, totals, anything that changes |
| `var` | ✅ | Function | Legacy only — never use it in new code |

```js
const MAX_HP = 100;  // never changes — SCREAMING_SNAKE_CASE
let hp = 80;         // changes every hit
```

### The Seven Types

| Type | Example | Notes |
| :--- | :--- | :--- |
| `string` | `"Emberfall"` / `'Emberfall'` / `` `Emberfall` `` | Text; backticks allow `${var}` |
| `number` | `42` / `3.14` | Integers and floats are one type |
| `bigint` | `9007n` | Rarely needed; huge integers |
| `boolean` | `true` / `false` | Flags: `isCaught`, `soldOut` |
| `undefined` | `x = undeclared;` | Declared but never assigned |
| `null` | `x = null;` | Intentionally empty — a choice |
| `object` | `{ a: 1 }` / `[1, 2]` | The compound types — see below |

```js
typeof "Emberfall"   // "string"
typeof 42            // "number"
typeof true          // "boolean"
typeof undefined     // "undefined"
typeof null          // "object" ← the famous JS lie
```

### Template Literals

```js
const name = "Ashwalker";
const level = 12;
console.log(`${name} is level ${level}`); // Ashwalker is level 12
```

---

## 🧮 Operators

### Arithmetic

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `+` | Addition / concatenation | `2 + 2` → `4` |
| `-` | Subtraction | `10 - 4` → `6` |
| `*` | Multiplication | `3 * 3` → `9` |
| `/` | Division | `9 / 3` → `3` |
| `%` | Modulo — the remainder | `7 % 3` → `1` |
| `**` | Exponent | `2 ** 10` → `1024` |
| `++` | Plus one | `hp++` |
| `--` | Minus one | `hp--` |

> [!NOTE]
> `+` is overloaded: numbers add, strings join. `"HP: " + hp` concatenates; `hp + 1` adds.
> Mixing both in one expression is the classic source of `"1001"` bugs.

### Comparison

| Operator | Reads as | Works on |
| :--- | :--- | :--- |
| `===` | Strictly equal | Values **and** types — always use this |
| `!==` | Not strictly equal | Values **and** types — always use this |
| `==` | Loosely equal | Coerces types first — avoid it |
| `!=` | Not loosely equal | Coerces types first — avoid it |
| `>` `>=` `<` `<=` | Greater / less | Numbers |

```js
5 == "5"   // true  — string converted, then compared
5 === "5"  // false — different types, full stop
```

### Logic

| Operator | Reads as | Shortcut |
| :--- | :--- | :--- |
| `&&` | AND | Both sides must be true |
| `\|\|` | OR | At least one side true |
| `!` | NOT | Flips the value |

### Assignment

`=` · `+=` · `-=` · `*=` · `/=` · `%=` — read, modify, write back in one statement:
`score += 10` is `score = score + 10`.

---

## 🔀 Conditionals

```js
if (hp === 0) {
  console.log("Game over");
} else if (hp < 25) {
  console.log("Low HP — heal!");
} else {
  console.log("Keep going");
}
```

```js
const status = hp === 0 ? "down" : "up"; // ternary: condition ? a : b
```

| Form | Reaches for it when |
| :--- | :--- |
| `if / else if / else` | The decision has outcomes |
| Ternary `? :` | The decision is one short value |
| `switch` | One variable is compared against many exact cases |

---

## 🔁 Loops

| Loop | Runs while | Use it for |
| :--- | :--- | :--- |
| `while (cond)` | Condition is true | Unknown count — keep fishing |
| `for (init; cond; step)` | Condition is true | Known count — the default |
| `for...of` | Items remain | Every item in an array or string |

```js
for (let i = 0; i < 5; i++) { console.log(i); }   // 0 1 2 3 4
while (fish.length < 10) { fish.push("🐟"); }
for (const item of inventory) { console.log(item); }
```

| Control | Effect |
| :--- | :--- |
| `break` | Exits the loop **now** |
| `continue` | Skips to the next iteration |
| Nested loop | A loop inside a loop — the inner one runs fully each outer pass |

---

## 📚 Arrays

```js
const inventory = ["Sword", "Shield", "Potion"];
```

| Accessor / Method | What it does |
| :--- | :--- |
| `arr[i]` | The item at index `i` — counting starts at **0** |
| `arr.length` | How many items — always one past the last index |
| `arr.push(x)` | Adds `x` to the **end** |
| `arr.pop()` | Removes and returns the **last** item |
| `arr.unshift(x)` | Adds `x` to the **front** |
| `arr.shift()` | Removes and returns the **front** item |
| `arr.indexOf(x)` | Index of `x`, or `-1` if absent |
| `arr.includes(x)` | `true` / `false` — ask instead of searching |
| `arr.slice(a, b)` | A copy of items `a` up to (not including) `b` |

> [!WARNING]
> Indexes run `0` to `length - 1`. Reading `inventory[inventory.length]` returns
> `undefined` — the same silence as a missing property. Check `length` before indexing.

---

## ⚙️ Functions

```js
function heal(target, amount) {
  return target + amount; // back to the caller, and the function stops
}

const attack = (power) => power * 2; // arrow — one-liner shorthand

console.log(heal(50, 25)); // 75
```

| Concept | Rule |
| :--- | :--- |
| Parameter | The name in the definition — `target, amount` |
| Argument | The value passed in — `50, 25` |
| `return` | Sends a value back; ends the function immediately |
| No `return` | Returns `undefined` |
| Scope | Parameters and `let`/`const` inside are private to the function |
| Arrow `=>` | Shorthand; ideal for one-liners and callbacks |

---

## 🗂️ Objects

```js
const hero = {
  name: "Ashwalker",
  level: 12,
  greet() {
    console.log(`I am ${this.name}`);
  }
};
```

| Operation | Syntax | Note |
| :--- | :--- | :--- |
| Read | `hero.name` | Dot notation |
| Update | `hero.level = 13` | Existing key |
| Create | `hero.guild = "Ember"` | New key — no declaration needed |
| Method | `hero.greet()` | Function stored inside the object |
| Self-reference | `this.name` | The object talking about itself |

> [!NOTE]
> Arrays and objects are both compounds, with different contracts: an **array** is ordered
> and indexed by position; an **object** is labeled and accessed by key. Characters are
> objects; inventories are arrays — and a character's inventory is an array of objects.

---

## 🎮 The One-Page Version

Everything from this sheet in a single file — one Emberfall shop:

```js
const shop = {
  name: "Emberfall Armory",
  gold: 120,
  stock: ["Sword", "Shield", "Potion"],
  sell(item) {
    const index = this.stock.indexOf(item);
    if (index === -1) {
      console.log("Out of stock!");
      return;
    }
    this.stock.pop();
    this.gold += 15;
    console.log(`Sold ${item} — gold: ${this.gold}`);
  }
};

for (let i = 0; i < shop.stock.length; i++) {
  console.log(shop.stock[i]);
}

shop.sell("Potion"); // Sold Potion — gold: 135
shop.sell("Dragon"); // Out of stock!
```

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| `let` vs `const` mix-up | Reassigning a `const` throws a `TypeError` — the engine stops |
| `=` inside `if` | Assigns instead of comparing; use `===` |
| `==` instead of `===` | Type coercion hides bugs: `0 == ""` is `true` |
| Off-by-one index | `arr[arr.length]` is `undefined`, not an error — silence, not a crash |
| `const` object, mutated fields | Allowed — `const` freezes the binding, not the contents |
| Declaring inside a loop with `var` | One shared variable for every iteration; `let` gives each pass its own |
| Forgetting `()` on a method | Passing the function itself instead of calling it |
| `this` outside a method | `this` is not the object you think — keep it inside methods |

---

## 🔗 See Also

- [[00c - JavaScript Cheatsheet II]] — the DOM, `.style`, events and `addEventListener`
- [[01 - Insert Coin]] — console and comments, where this sheet begins
- [[07 - Character Sheet]] — objects, the last stop before the DOM
- [[12 - Flexbox]] — laying out the page this language will drive

---
