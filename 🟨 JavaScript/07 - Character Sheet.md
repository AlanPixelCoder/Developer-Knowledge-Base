# 07. Character Sheet

**Spanish version:** [07 - Ficha de Personaje.md](07%20-%20Ficha%20de%20Personaje.md)

**Course:** JavaScript
**Topic:** Objects, properties, dot notation, updating & adding fields, methods, `this` and the Guild Pass project
**Tags:** `#javascript` `#objects` `#properties` `#methods` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-E67E22?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-34_--_38_%2B_Project-7C5CFF?style=for-the-badge" alt="Lessons 34 to 38 plus project">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Twelve loose variables cannot describe a hero. An **object** can: one name, a whole sheet
of labeled values — name, class, level, gold — and even **actions** the hero can take.
This chapter completes JavaScript's data toolkit. By the end you will build a **Guild Pass**
with live methods that upgrade a ticket and compute its travel time. Reference:
[[00b - JavaScript Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> An object is a collection of related **key-value pairs** inside curly braces `{}`; you
> read and write pairs with **dot notation**, and a function stored inside an object is a
> **method** — an action the object knows how to perform.

---

## 01. The Sheet

### What Is an Object?

An **object** is a core data type used to store collections of related data and behaviors.
Where an array is an ordered list, an object is a **labeled** bag — every value answers to
a name you chose:

```js
const book = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  year: 1937
};
```

Each `key: value` pair is a **property**. Pairs are separated by commas, wrapped in curly
braces `{}`.

### Quest: The Pizza Object

The tavern order, as the kitchen sees it — toppings, style, slices, price, all under one
name:

```js
const pizza = {
  topping: "Pepperoni 🍕",
  type: "Hand-tossed",
  slices: 12,
  price: 14.99
};

console.log(pizza);
```

Compare the object with four parallel variables: same data, but the object can be passed to
a function as **one argument** — which is how every real system moves a character, an item
or a save file around.

---

## 02. Reading the Sheet

### Properties and Dot Notation

A **property** is one key-value pair inside the object. **Dot notation** reads it: a period
`.` followed by the property name:

```js
const stadium = {
  name: "Dodger Stadium",
  location: "Los Angeles, CA",
  capacity: 56000,
  soldOut: false
};

console.log(stadium.name);     // Dodger Stadium
console.log(stadium.capacity); // 56000
```

Asking for a property that does not exist returns `undefined` — the same silence as an
out-of-range array index from [[05 - Inventory]].

### Adding Properties

Dot notation on the left of `=` also **creates** properties that were never declared:

```js
const car = {};
car.model = "Honda";
car.year = 2024;
car.color = "white";
car.used = false;
```

An empty object is a valid starting point — build the sheet field by field as the game
discovers them.

---

## 03. Editing the Sheet

### Updating an Existing Property

Assigning a new value to an existing key updates it — no ceremony:

```js
const user = {
  username: "@ashwalker",
  verified: false
};

user.verified = true; // updated
```

### Adding a New Property

Assigning to a key that does not exist yet **adds** it. The engine does not complain,
because objects have no fixed schema:

```js
const fruit = {
  name: "apple",
  quantity: 10
};

fruit.organic = true; // brand-new property
```

### Quest: Catch Progress

A capture log updates as the run goes — add a flag, then flip it, then rename the entry:

```js
const pokemon = {
  name: "Pikachu",
  type: "Electric ⚡",
  level: 25
};

pokemon.isCaught = false; // added
pokemon.isCaught = true;  // updated
pokemon.name = "Sparky";  // renamed
```

> [!WARNING]
> **The typo that vanishes.** `hero.hp = 100` and `hero.HP = 100` create **two different
> properties**. JavaScript will not warn you — one code path writes `hp`, the other reads
> `HP`, and the hero mysteriously stays at full health. Pick a case convention for property
> names (camelCase, like everything else in this vault) and never deviate.

---

## 04. Actions

### Object Methods

A **method** is a function stored inside an object — an action the object can perform.
Two syntaxes, one behavior:

```js
const phone = {
  model: "iPhone 11 Pro Max",
  // Traditional function syntax:
  ringtone: function () {
    console.log("Ring, ring! 📱");
  },
  // Shorthand method syntax:
  vibrate() {
    console.log("Bzz, bzz!");
  }
};

phone.ringtone(); // calling the method
phone.vibrate();
```

Call a method with the same dot notation as a property, followed by `()` — properties
read, methods **run**.

### The `this` Keyword

Inside a method, `this` refers to **the object itself** — the sheet reading its own fields.
A barnyard example that introduces itself:

```js
const pig = {
  name: "Napoleon",
  type: "pig",
  age: 63,
  makeSound() {
    console.log(this.name + " is a " + this.age + " year old " + this.type + " that goes oink!");
  }
};

pig.makeSound();
// Napoleon is a 63 year old pig that goes oink!
```

`this.name` resolves against `pig` when called as `pig.makeSound()` — and against any
other object if the same method is copied there later. That indirection is exactly what
makes one method serve a whole roster.

---

## 05. The Guild Pass

### Checkpoint: Chapter Recap

- Objects store related data and behavior as **key-value pairs** in `{}`.
- **Dot notation** reads, updates and creates properties.
- A function inside an object is a **method**; call it with `obj.method()`.
- `this` points at the object the method was called on — its own fields, on demand.

### Project: Guild Pass

The capstone ties the chapter together: one travel pass object with data fields **and**
two live methods. `upgrade()` flips a Boolean on `this`; `flightTime()` computes duration
from the departure and arrival hours — wrapping subtraction in a `let` and checking for the
midnight case:

```js
const departTripTicket = {
  name: "Alan Lozano",
  from: "Mexico City (MEX)",
  to: "Banff, Canada (YYC)",
  businessClass: false,
  leaveTime: 8,
  arriveTime: 14,
  upgrade() {
    if (this.businessClass) {
      console.log("Your ticket is already business class!");
    } else {
      this.businessClass = true;
    }
  },
  flightTime() {
    let travelTime = this.arriveTime - this.leaveTime;
    if (travelTime < 0) {
      travelTime += 24;
    }
    console.log(`Flight duration: ${travelTime} hours`);
  }
};

departTripTicket.upgrade();   // this.businessClass → true
departTripTicket.flightTime(); // "Flight duration: 6 hours"
```

Read what just happened: the object holds its own data, upgrades **itself**, and computes
its own duration — the caller never touches a field directly. That is the whole promise of
objects: data and the operations on it, traveling together. Chapter [[06 - Skill Functions]]
supplied the logic; this chapter gave it a home.

> [!TIP]
> **Game dev version**
> This is a character sheet, a quest ticket, an item card — the same shape. Swap the fields
> for `hp`, `mp` and `skills`, add a `takeDamage(amount)` method that mutates `this.hp`, and
> you have written the core of every RPG inventory and entity system ever shipped.

---

## ⚡ XP Earned: Key Takeaways

- 🗂️ One object = one name = many **labeled** values: `{ key: value, ... }`.
- ➕ Dot notation reads, updates **and** creates properties — no declaration step.
- ❓ Unknown properties read as `undefined`; property names are case-sensitive, typos included.
- 🛠️ Methods are functions inside objects; `obj.method()` runs, `obj.property` reads.
- 🪞 `this` is the object talking about itself — the method's anchor.

---

## 🎁 Loot Table: Real-World Use Cases

- 🧑‍🎤 Character sheets, save files, player profiles
- 🗺️ World state: time of day, weather, current zone, quest flags
- 🧾 Shopping carts, tickets, invoices — anything with named fields
- ⚔️ Entities: data fields plus `takeDamage()`, `levelUp()`, `usePotion()`
- 📦 API responses — the JSON that moves the modern web is objects all the way down

---

## 🎮 Side Quests: Practice Exercises

1. Model your hero as an object with four properties and print one sentence about them.
2. Add a fifth property that did not exist in the declaration.
3. Write a method using `this` that prints the hero's name and level.
4. Call a method on the object twice and confirm `this` resolves the same way both times.
5. **Boss fight:** a *shop item* object — `name`, `price`, `stock` — with a `buy()`
   method that reduces `stock` by one and prints the receipt line; call it until it prints
   "Out of stock".

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — object syntax and methods on one page
- [[06 - Skill Functions]] — previous chapter: the functions objects store as methods
- [[08 - Living HUD]] — next chapter: objects meet the page — the DOM is one big object
- [[05 - Inventory]] — arrays and objects, side by side, the two data toolkits

---
