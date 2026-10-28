# 05. Inventory

**Spanish version:** [05 - Inventario.md](05%20-%20Inventario.md)

**Course:** JavaScript
**Chapter:** 5 — Spare Parts Bin
**Topic:** arrays, indexing, methods, mutation
**Tags:** `#javascript` `#arrays` `#methods` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Cabinet%20Guild-FF6B35?style=for-the-badge" alt="Cabinet Guild">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

The Guild's spare parts bin holds a list in order: fuses, relays, grommets, and the odd capacitor. When the list grows or shrinks between repairs, variables won't do. An array keeps items in sequence and lets you index, add, remove, or search.

## Ordered Storage

Arrays use square brackets `[]` and commas to separate values. Indices start at `0`.

```js
let partsBin = ["fuse", "relay", "grommet", "capacitor"];
console.log(partsBin[0]);
console.log(partsBin[2]);
console.log("Count: " + partsBin.length);
```

## Output

```text
fuse
grommet
Count: 4
```

> [!IMPORTANT]
> The first element is index 0, not 1. The last index is `length - 1`. Off-by-one is the most common way to pull the wrong part from the bin.

## Changing the Bin

Arrays are mutable. Methods like `push()`, `pop()`, `unshift()`, `shift()`, and `splice()` change the array in place. Know which end you touch and whether you need the removed value.

```js
let partsBin = ["fuse", "relay"];
partsBin.push("diode");      // add to end
console.log(partsBin);
partsBin.unshift("washer");   // add to front
console.log(partsBin);
let last = partsBin.pop();    // remove from end
console.log("Removed: " + last);
console.log(partsBin);
```

## Output

```text
["fuse", "relay", "diode"]
["washer", "fuse", "relay", "diode"]
Removed: diode
["washer", "fuse", "relay"]
```

> [!WARNING]
> `push/pop` affect the end (cheap and common). `unshift/shift` affect the front (reindex the whole array in larger lists). For a small bin it doesn't matter; for big lists it's worth remembering.

## Finding Parts

To check for a part without scanning by hand, use `includes()` or `indexOf()`.

```js
let partsBin = ["fuse", "relay", "grommet"];
console.log(partsBin.includes("relay")); // true
console.log(partsBin.indexOf("grommet")); // 2
console.log(partsBin.indexOf("coil"));   // -1 (not found)
```

## Output

```text
true
2
-1
```

> [!TIP]
> `indexOf()` returns `-1` when not found, not `false`. Always check for `-1` explicitly if the logic depends on "exists".

## Why Arrays

Arrays group related items under one name, keep order, and give you methods to reshape the list without creating a dozen variables. The tradeoff: mutation is easy to forget. If two parts of the script both change the same array, read order matters — the bin state can change between checks.

**Next:** [[06 - Skill Functions]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Yellow footer" />
</p>
