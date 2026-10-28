# 02. Player Stats

**Spanish version:** [02 - Atributos del Jugador.md](02%20-%20Atributos%20del%20Jugador.md)

**Course:** JavaScript
**Chapter:** 2 — Cabinet Loadout
**Topic:** let, const, types, arithmetic, coercion notes
**Tags:** `#javascript` `#variables` `#types` `#arithmetic` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

A fresh cabinet needs a loadout card. The Guild writes down coin count, cabinet serial, whether a credit is still owed, and the pilot's callsign. Those values change across a session, so they must be stored, not retyped. That is the job of variables.

## Slots for Values

`const` pins a slot to its first value. `let` opens a slot you intend to rewrite. Pick `const` by default; only reach for `let` when the value must change during the run.

```js
const cabinetSerial = "CAB-9";
const guildId = "GUILD-PRIME";
let credits = 3;
let pilotCallsign = "RIVET";

console.log(cabinetSerial + " | " + guildId);
console.log("Pilot: " + pilotCallsign + " | Credits: " + credits);
```

## Output

```text
CAB-9 | GUILD-PRIME
Pilot: RIVET | Credits: 3
```

> [!CAUTION]
> You cannot reassign `const`. Trying to do so throws a type error in strict reasoning; the key is intent: constants are for values that must not move for the whole run (identities), not for values the cabinet mutates.

## What the Cabinet Can Hold

JavaScript tags values by type at runtime. For the loadout you will hit these most often:

| Type | Example | Notes |
| :--- | :--- | :--- |
| `number` | `credits = 2`, `heat = 37.5` | Integers and decimals share the same type. |
| `string` | `"RIVET"`, `"CAB-9"` | Text wrapped in matching quotes. |
| `boolean` | `hasTicket = true` | `true` or `false` for yes/no gates. |
| `undefined` | declared but not assigned | A slot exists with no value yet — easy to miss. |

```js
let hasTicket = false;
let repairNotes; // undefined until assigned
console.log(typeof hasTicket);
console.log(typeof repairNotes);
```

## Output

```text
boolean
undefined
```

`typeof` tells you what the engine sees. Relying on types is useful, but `undefined` is not the same as `null` in meaning; here it just signals "no assignment yet".

## Arithmetic and the Cost of a Retry

Running a retry costs credits. The cabinet also tracks wear. Arithmetic behaves predictably on numbers, but string concatenation has higher precedence in how your eyes read it.

```js
let credits = 5;
credits = credits - 1; // retry spent
console.log("Credits left: " + credits);

let baseHeat = 12;
let overclock = 1.5;
console.log("Thermal load: " + (baseHeat * overclock));
```

## Output

```text
Credits left: 4
Thermal load: 18
```

> [!TIP]
> Wrap arithmetic in parentheses when concatenating to a string. Without them `baseHeat + overclock` would still add numbers, but as expressions grow it's easy to misread; parentheses make the intent unambiguous.

## Why Types Matter

The engine does not silently guess your intent for everything. Coercion can sneak in when mixing types, which is why you should be explicit about strings vs numbers. Keeping `const` for fixed identities and `let` for counters prevents accidental rebinds later when more logic piles onto the same loadout card.

**Next:** [[03 - Loot Rolls]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
