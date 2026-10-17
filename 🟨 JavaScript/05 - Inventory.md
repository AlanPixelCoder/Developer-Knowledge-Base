# 05. Inventory

**Spanish version:** [05 - Inventario.md](05%20-%20Inventario.md)

**Course:** JavaScript
**Topic:** Arrays, index and bracket notation, `.length`, iteration, `push` / `pop` / `shift` / `unshift`, `.indexOf()` / `.includes()` and the Dungeon Seed project
**Tags:** `#javascript` `#arrays` `#data-structures` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-E67E22?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Lessons-23_--_28_%2B_Project-7C5CFF?style=for-the-badge" alt="Lessons 23 to 28 plus project">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Yellow wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

A character with twenty potions needs twenty variables — and a nightmare to manage. **Arrays**
are the engine's single container for many values: the hotbar, the party roster, the seed
string of an entire dungeon. By the end you will generate a **procedural dungeon floor**
from four tile types, all packed into one array. Reference:
[[00b - JavaScript Cheatsheet]].

> [!NOTE]
> **The whole chapter in one sentence**
> An array is one variable holding an ordered list in square brackets `[]`; elements are
> addressed by a **zero-based index**, counted by `.length`, and reshaped with the built-in
> methods `push`, `pop`, `shift` and `unshift`.

---

## 01. The Bag

### What Is an Array?

An **array** is a single variable used to store multiple values grouped together. Create
one with square brackets `[]`, elements separated by commas. An array can mix types or hold
one uniform type — the engine does not care:

```js
let lotteryNumbers = [13, 36, 45, 57, 67, 14];
const lettersAndNumbers = ["a", "b", "c", 1, 2, 3];
```

### Quest: Zone List

The campaign's travel log — five destinations, one variable:

```js
let myDestinations = [
  "Manhattan - Washington Square Park",
  "The Bronx - Yankee Stadium",
  "Brooklyn - Coney Island",
  "Queens - Flushing",
  "Staten Island - Historic Richmond Town"
];

console.log(myDestinations);
```

Printing the variable prints the whole list at once — brackets, quotes and all. Compare
that with five separate `console.log()` statements: same information, one name.

---

## 02. Addresses

### Index and Bracket Notation

An element's **index** is its numeric position inside the array — and JavaScript counts
from **zero**. The first element is `[0]`, not `[1]`:

```js
let fruits = ["strawberries 🍓", "blueberries 🫐", "bananas 🍌"];
console.log(fruits[0]); // strawberries 🍓
```

### Modifying Elements

Bracket notation on the left side of `=` writes:

```js
let pokemon = ["Bulbasaur", "Charmander", "Squirtle"];
pokemon[2] = "Pikachu"; // replaces "Squirtle"
```

### Growing the Array

Assigning to an index **past the end** appends, filling any gap with `undefined` — legal,
but the hole is a bug waiting to be found:

```js
let groceryList = ["🥛 Milk", "🥑 Avocado", "🥚 Eggs", "🍞 Bread"];

groceryList[2] = "🧈 Butter";       // replaces Eggs
groceryList[4] = "🧼 Soap";         // adds at the end

console.log(groceryList);
// ["🥛 Milk", "🥑 Avocado", "🧈 Butter", "🍞 Bread", "🧼 Soap"]
```

> [!WARNING]
> **Off-by-one, the eternal bug.** The last index of an array is `length - 1`. Asking for
> `[length]` returns `undefined` — not an error, just silence. When an array lookup prints
> nothing you expected, count from **zero** and subtract one.

---

## 03. Counting Slots

### The `.length` Property

Every array carries a built-in `.length` property: an integer with the number of elements
it currently holds:

```js
const testScores = [78, 96, 100, 88, 85, 81, 79];
const numberOfScores = testScores.length;
console.log(numberOfScores); // 7
```

### Loops Over Arrays

`.length` pairs naturally with the loops of [[04 - The Farm]] — walk every element
dynamically, without knowing the count in advance:

```js
const musicNotes = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"];

for (let i = 0; i < musicNotes.length; i++) {
  console.log(musicNotes[i]);
}
```

The loop condition uses `.length` directly, so adding a note to the array tomorrow needs
no other edit. Hardcoding `i < 7` would silently skip it.

---

## 04. Hotbar Management

### The Four Cardinals

JavaScript ships built-in methods that modify arrays in place. Four cover most early
programs:

| Method | Effect | Returns |
| :--- | :--- | :--- |
| `push(item)` | Adds to the **end** | New length |
| `pop()` | Removes the **last** element | The removed element |
| `unshift(item)` | Adds to the **beginning** | New length |
| `shift()` | Removes the **first** element | The removed element |

### Quest: Playlist Reorder

A loadout shuffle — remove from both ends, add to both ends:

```js
const musicPlaylist = ["Tom Sawyer", "Sabotage", "Thriller"];

musicPlaylist.shift(); // removes "Tom Sawyer"
musicPlaylist.pop();   // removes "Thriller"
musicPlaylist.push("Scary Monsters and Nice Sprites"); // adds to the end
musicPlaylist.unshift("Fractals", "Bangarang");        // adds to the front

console.log(musicPlaylist);
// ["Fractals", "Bangarang", "Sabotage", "Scary Monsters and Nice Sprites"]
```

`shift` and `unshift` reindex every element that moves — fine for a playlist, costly inside
a per-frame loop. Reach for `push` and `pop` when you can: they touch only one end.

---

## 05. Find the Spy

### `.indexOf(value)`

Returns the numeric index of the **first** occurrence of a value — or `-1` if the value is
not in the array at all:

```js
const characters = ["The Wally Watchers", "Wilma", "Waldo", "Woof"];
console.log(characters.indexOf("Waldo")); // 2
console.log(characters.indexOf("Wanda")); // -1
```

### `.includes(value)`

Checks membership and answers with a Boolean — no index arithmetic, no `-1` sentinel:

```js
if (characters.includes("Waldo")) {
  let waldoIndex = characters.indexOf("Waldo");
  console.log(`Found Waldo at index ${waldoIndex}!`);
} else {
  console.log("Not found");
}
```

The pair reads like a sentence: *if the roster includes Waldo, find where.* `.includes()`
arrived with ES2016 — it is the right tool for the question "is it in there?"; `.indexOf()`
is the right tool for "where is it?".

---

## 06. The Dungeon Seed

### Checkpoint: Chapter Recap

- An array is **one variable**, many ordered values, in `[...]`.
- Indices start at **zero**; the last one is `length - 1`.
- `.length` counts elements; combine it with a `for` to visit them all.
- `push`/`pop` work one end, `shift`/`unshift` the other.
- `.indexOf()` returns a position or `-1`; `.includes()` returns `true` or `false`.

### Project: Procedural Dungeon Floor

The chapter's capstone generates a dungeon from tiles — the same four letters a genetic
sequence uses, the same four-shape trick any procedural generator plays. Twenty-four rooms,
three tiles per room, rolled from one array:

```js
const dungeonTiles = ["#", ".", "^", "C"]; // wall, floor, trap, chest
let myDungeon = [];

for (let i = 0; i < 24; i++) {
  let piece1 = Math.floor(Math.random() * dungeonTiles.length);
  let piece2 = Math.floor(Math.random() * dungeonTiles.length);
  let piece3 = Math.floor(Math.random() * dungeonTiles.length);

  myDungeon.push(
    dungeonTiles[piece1] + dungeonTiles[piece2] + dungeonTiles[piece3]
  );
}

console.log(myDungeon);
```

Every piece from this chapter is on the table: the seed array, `.length` feeding
`Math.random()` from [[03 - Loot Rolls]], a `for` loop from [[04 - The Farm]], and `push`
to grow the result. Twenty-four rooms from ten lines — the array did the storing, the loop
did the work, and the methods kept the bag tidy.

> [!TIP]
> **Game dev version**
> This is procedural generation in its infancy. Swap the four tiles for biome ids, add a
> second loop for rows, and you have a map. The full technique — rooms, corridors, seeds —
> is the same array-of-values problem with better words on it.

---

## ⚡ XP Earned: Key Takeaways

- 🎒 One array = one variable = many ordered values: `[13, 36, 45]`.
- 0️⃣ Indices start at **zero**; last index is `.length - 1`; out-of-range reads return `undefined`.
- ✍️ `arr[2] = x` writes; assigning past the end appends.
- 📏 `.length` counts — feed it to a `for` loop to visit every element.
- 🃏 `push`/`pop` touch the end; `shift`/`unshift` touch the front (and reindex everything).
- 🔍 `.indexOf()` → position or `-1`; `.includes()` → Boolean membership test.

---

## 🎁 Loot Table: Real-World Use Cases

- 🎒 Inventarios, hotbars, party rosters, skill loadouts
- 🗺️ Map rows, dungeon seeds, procedural generation inputs
- 🏆 High-score tables and leaderboards
- 📜 Dialogue queues, turn orders, action timelines
- 🧬 Any "many values, one name" problem — the definition of the array

---

## 🎮 Side Quests: Practice Exercises

1. Create an array of five loot items and print the first and last with bracket notation.
2. Replace the middle element of a party array, then `push` a sixth member.
3. `pop()` the last element and print what was removed.
4. Loop an array of zone names and print each with its index: `0: Ember Depths`.
5. **Boss fight:** a *duplicate detector* — loop an array of drops and print the first
   index where `.indexOf()` disagrees with a manual scan, using `.includes()` to confirm.

---

## 🔗 See Also

- [[00b - JavaScript Cheatsheet]] — array syntax and methods on one page
- [[04 - The Farm]] — previous chapter: the loops that walk arrays
- [[06 - Skill Functions]] — next chapter: wrapping array work in functions
- [[07 - Character Sheet]] — objects, the other half of JavaScript's data toolkit

---
