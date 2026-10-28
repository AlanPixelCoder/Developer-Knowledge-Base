# 07. Character Sheet

**Spanish version:** [07 - Ficha de Personaje.md](07%20-%20Ficha%20de%20Personaje.md)

**Course:** JavaScript
**Chapter:** 7 — Pilot Roster Card
**Topic:** objects, properties, methods, this
**Tags:** `#javascript` `#objects` `#methods` `#this` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-7-7C5CFF?style=for-the-badge" alt="Chapter 7">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

A pilot on the Guild roster is more than a name. They have a callsign, a cabinet assignment, a credit balance, and a rank. Bundling related values under one object avoids a pile of loose variables and keeps the card coherent.

## Bundling Properties

Objects use `{}` with key:value pairs. Access with dot notation or bracket notation.

```js
let pilot = {
  callsign: "RIVET",
  cabinet: "CAB-9",
  credits: 4,
  rank: "CREW"
};
console.log(pilot.callsign);
console.log(pilot["cabinet"]);
```

## Output

```text
RIVET
CAB-9
```

> [!TIP]
> Dot notation is cleaner for known keys. Bracket notation is useful when the key comes from a variable or has spaces (spaces are rare, but possible).

## Methods and `this`

When a function lives inside an object, it is a method. Inside that method, `this` refers to the object the method was called on, so it can read its own properties.

```js
let pilot = {
  callsign: "RIVET",
  credits: 2,
  spendCredit: function() {
    this.credits = this.credits - 1;
    console.log(this.callsign + ": CREDITS LEFT " + this.credits);
  }
};
pilot.spendCredit();
pilot.spendCredit();
```

## Output

```text
RIVET: CREDITS LEFT 1
RIVET: CREDITS LEFT 0
```

> [!IMPORTANT]
> `this` is context-based. If you copy `pilot.spendCredit` to another variable and call it without the object, `this` can lose its binding. For now, always call methods as `object.method()` to keep the binding correct.

## Updating and Adding

Objects are mutable: you can update existing properties or add new ones at any time.

```js
let pilot = { callsign: "RIVET", rank: "CREW" };
pilot.rank = "SENIOR";
pilot.lastRun = "CAB-9";
console.log(pilot.rank + " | " + pilot.lastRun);
```

## Output

```text
SENIOR | CAB-9
```

## Why Objects

Objects model a single thing with many attributes and behaviors. Arrays model lists of things. The pilot card is one entity with state (`credits`) and actions (`spendCredit()`). Keeping state and the logic that changes it together makes the roster easier to reason about and less error-prone when the card grows.

**Next:** [[08 - Living HUD]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
