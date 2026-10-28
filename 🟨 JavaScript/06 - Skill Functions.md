# 06. Skill Functions

**Spanish version:** [06 - Funciones de Habilidad.md](06%20-%20Funciones%20de%20Habilidad.md)

**Course:** JavaScript
**Chapter:** 6 — Repair Routines
**Topic:** functions, parameters, return, scope, arrow functions
**Tags:** `#javascript` `#functions` `#scope` `#arrow` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

The repair bench has standard routines: reseat a relay, clean contacts, test a fuse. Writing the same log lines over and over invites typos. A function names a routine, takes inputs, and returns a result so you can call it anywhere.

## Naming a Routine

Declare with `function`, give it a clear name, add parentheses and a block. Call it by name followed by `()`.

```js
function logBoot() {
  console.log("REPAIR: CABINET BOOT TEST RUN");
}
logBoot();
logBoot();
```

## Output

```text
REPAIR: CABINET BOOT TEST RUN
REPAIR: CABINET BOOT TEST RUN
```

## Inputs and Outputs

Parameters let you pass values in. `return` sends a value back out. Without `return`, a function gives `undefined`.

```js
function fuseCheck(voltage) {
  if (voltage >= 5) {
    return "FUSE: OK";
  } else {
    return "FUSE: REPLACE";
  }
}
console.log(fuseCheck(6));
console.log(fuseCheck(3));
```

## Output

```text
FUSE: OK
FUSE: REPLACE
```

> [!IMPORTANT]
> Parameters are local names for the values you pass. `return` ends the function and produces a value you can store in a variable, pass to `console.log()`, or use in an expression.

## Scope: What Stays Inside

Variables declared inside a function are local to that function. Variables declared outside are in the broader scope and visible inside, but changing globals carelessly couples routines together.

```js
let benchId = "BENCH-2"; // global to this script
function relayReport(count) {
  let status = "RUNNING"; // local
  console.log(benchId + ": " + count + " relays - " + status);
}
relayReport(3);
// console.log(status); // error if uncommented
```

## Output

```text
BENCH-2: 3 relays - RUNNING
```

> [!WARNING]
> Avoid leaning on globals for everything. Pass what a routine needs as parameters. That makes the function easier to reason about and much harder to break when other code changes.

## Arrow Functions

Arrow functions give a shorter syntax. For simple returns, you can omit `{}` and `return`.

```js
const wattsToLoad = (amps, volts) => amps * volts;
console.log("LOAD: " + wattsToLoad(2, 12) + "W");
```

## Output

```text
LOAD: 24W
```

Arrow functions are not a replacement for everything (especially with `this` later), but they are convenient for small pure calculations like conversions on the repair bench. The key is readability: use the form that makes intent obvious.

**Next:** [[07 - Character Sheet]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
