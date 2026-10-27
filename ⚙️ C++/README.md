# ⚙️ C++: Engine Foundations (MOC)

**Español:** [README-ES.md](./README-ES.md)

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++17">
  <img src="https://img.shields.io/badge/Toolchain-g%2B%2B%20%7C%20Clang-7C5CFF?style=for-the-badge&logo=llvm&logoColor=white" alt="Toolchain">
  <img src="https://img.shields.io/badge/Paradigm-Procedural%20%26%20Objects-FF6B35?style=for-the-badge" alt="Procedural & objects">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_INTERMEDIATE-6CC24A?style=for-the-badge" alt="Beginner to intermediate">
  <img src="https://img.shields.io/badge/Chapters-8-7C5CFF?style=for-the-badge" alt="8 chapters">
  <img src="https://img.shields.io/badge/Notes-53-00C2A8?style=for-the-badge" alt="53 notes">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
  <img src="https://img.shields.io/badge/Environment-macOS-lightgrey?style=for-the-badge&logo=apple&logoColor=white" alt="macOS">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

> [!NOTE]
> This module is the map of content for the C++ notes in this vault: 51 lessons in eight chapters,
> plus two field manuals. Every program is complete, compiles with `-Wall -Wextra`, and its documented
> output is the output it really prints.

> [!TIP]
> Start at [[01 - Cold Start]] and follow the numbers. Compile and run every example before moving on:
> the habit of *write → `g++` → run → read the output* is what the whole module trains.

**Prerequisite:** a terminal, `g++` (or `clang++`) and any text editor. Nothing else — chapter 1
builds the compile loop from scratch.

> [!NOTE]
> **The Emberfall thread**
> Every example belongs to one in-house project: the console and tooling of *Emberfall*, a small game
> engine. Boot logs, config values, spawn tables, satchels, entity blueprints and memory handles give
> the examples a shared vocabulary. The language is exactly the standard one — the setting is just
> what keeps the programs from being `foo` and `bar`.

---

## 🗺️ Map of Content

### 📚 Reference

* **[00b - Field Manual I](./00b%20-%20Field%20Manual%20I.md)** — I/O, types, operators, control flow, loops, compiler flags.
* **[00c - Field Manual II](./00c%20-%20Field%20Manual%20II.md)** — Containers, functions, classes, files, and memory.

### ⚡ 1. First Boot

Compiling, printing, and the shape of a program.

* **[01 - Cold Start](./01%20-%20Cold%20Start.md)** — What C++ is, where it runs, and the shape of a `.cpp` file.
* **[02 - First Light](./02%20-%20First%20Light.md)** — `std::cout`, `#include <iostream>`, the four parts of an output statement.
* **[03 - The Skeleton File](./03%20-%20The%20Skeleton%20File.md)** — `int main()`, braces, `return 0`, and escape sequences.
* **[04 - Notes in the Margin](./04%20-%20Notes%20in%20the%20Margin.md)** — `//` and `/* */`, and when a comment is hiding a bug.
* **[05 - Escape Velocity](./05%20-%20Escape%20Velocity.md)** — Chapter 1 recap: ASCII art that survives escaping.
* **[06 - From Source to Switch](./06%20-%20From%20Source%20to%20Switch.md)** — Source, object, executable: what `g++` actually does to your file.

### 🔢 2. Raw Values

Types, declarations, arithmetic, and input.

* **[07 - Raw Materials](./07%20-%20Raw%20Materials.md)** — `int`, `double`, `char`, `bool`, `std::string`, and what each costs.
* **[08 - Naming the Parts](./08%20-%20Naming%20the%20Parts.md)** — Declaring, initialising, naming rules, and the constants that should not move.
* **[09 - In, Through, Out](./09%20-%20In%2C%20Through%2C%20Out.md)** — Input, process, output — and assignment versus comparison.
* **[10 - Numbers That Lie](./10%20-%20Numbers%20That%20Lie.md)** — Arithmetic, precedence, integer division, and `%`.
* **[11 - Echo Chamber](./11%20-%20Echo%20Chamber.md)** — Chaining `<<`, `std::cin`, and the direction of the arrows.
* **[12 - Speak to the Machine](./12%20-%20Speak%20to%20the%20Machine.md)** — `std::getline`, formatted output, and text that contains spaces.
* **[13 - Level Scaling](./13%20-%20Level%20Scaling.md)** — Chapter 2 recap: one formula, several numeric types, one rounding decision.

### 🧠 3. Decisions

Branching, comparisons, randomness, and logic.

* **[14 - Forked Roads](./14%20-%20Forked%20Roads.md)** — `srand` / `rand`, and the seeding bug that makes every run identical.
* **[15 - Doors and Keys](./15%20-%20Doors%20and%20Keys.md)** — `if` / `else`, braces that are not optional, and boolean conditions.
* **[16 - Tiers and Thresholds](./16%20-%20Tiers%20and%20Thresholds.md)** — Six relational operators, `else if`, and first-match-wins ordering.
* **[17 - Loaded Dice](./17%20-%20Loaded%20Dice.md)** — `rand()` ranges, modulo bias, and `%` as a range tool.
* **[18 - Guards and Gates](./18%20-%20Guards%20and%20Gates.md)** — `&&`, `||`, `!`, truth tables, and short-circuit evaluation.
* **[19 - Trial by Question](./19%20-%20Trial%20by%20Question.md)** — Chapter 3 recap as a scored quiz that branches on totals.

### 🔁 4. Iteration

`while`, `for`, counting down, and repeating without repeating yourself.

* **[20 - The Loop That Waits](./20%20-%20The%20Loop%20That%20Waits.md)** — What iteration is, `do ... while`, and the four parts of a loop that ends.
* **[21 - Holding Patterns](./21%20-%20Holding%20Patterns.md)** — `while`, conditions that change, and clamping a value on the way down.
* **[22 - Tick by Tick](./22%20-%20Tick%20by%20Tick.md)** — `for`: initialisation, condition, increment, and the off-by-one that follows.
* **[23 - Countdown Protocol](./23%20-%20Countdown%20Protocol.md)** — Counting down, decrementing loops, and signed versus unsigned counters.
* **[24 - The Pattern Trial](./24%20-%20The%20Pattern%20Trial.md)** — Chapter 4 recap: overlapping rules evaluated in order.

### 📦 5. Collections

Vectors, indices, growth, traversal, and arrays.

* **[25 - The Satchel](./25%20-%20The%20Satchel.md)** — `std::vector`, `#include <vector>`, and why the container beats parallel variables.
* **[26 - Slot and Index](./26%20-%20Slot%20and%20Index.md)** — Zero-based indices, `v[i]`, `at()`, and undefined behaviour past the end.
* **[27 - Pack and Unpack](./27%20-%20Pack%20and%20Unpack.md)** — `push_back`, `pop_back`, `back`, and the empty-container trap.
* **[28 - Walking the Satchel](./28%20-%20Walking%20the%20Satchel.md)** — Range-`for` versus index loops, and what `&` saves you.
* **[29 - The Alchemist's Tally](./29%20-%20The%20Alchemist%27s%20Tally.md)** — Chapter 5 recap: sum, count, maximum, average — and integer division.
* **[30 - Stone Racks and Satchels](./30%20-%20Stone%20Racks%20and%20Satchels.md)** — C-style arrays next to vectors: fixed size, decay, and the `sizeof` trick.

### 🧩 6. Functions

Parameters, returns, composition, and scope.

* **[31 - One Spell, Many Casts](./31%20-%20One%20Spell%2C%20Many%20Casts.md)** — Why functions exist: one definition, many call sites, one place to change.
* **[32 - The Tavern Board](./32%20-%20The%20Tavern%20Board.md)** — Parameters versus arguments, `return`, and early exits.
* **[33 - Filling the Slots](./33%20-%20Filling%20the%20Slots.md)** — Default arguments, trailing defaults, and where the default belongs.
* **[34 - Handing Back the Loot](./34%20-%20Handing%20Back%20the%20Loot.md)** — `void`, value returns, references, and returning a struct.
* **[35 - Chained Returns](./35%20-%20Chained%20Returns.md)** — Composing functions, and reading a call chain inside out.
* **[36 - The Gate Tax](./36%20-%20The%20Gate%20Tax.md)** — Pass by value versus pass by reference, and the cost of a copy.
* **[37 - Where Names Live](./37%20-%20Where%20Names%20Live.md)** — Local, global, block scope, lifetime, and shadowing.

### 🏛️ 7. Entities

Structs, classes, constructors, methods, and headers.

* **[38 - Guild Blueprints](./38%20-%20Guild%20Blueprints.md)** — Defining a `struct`: a type you invent, and what `sizeof` says about it.
* **[39 - Sealed and Open Doors](./39%20-%20Sealed%20and%20Open%20Doors.md)** — `public`, `private`, and an invariant kept inside the type.
* **[40 - The Relic Safe](./40%20-%20The%20Relic%20Safe.md)** — Constructors guarantee a valid object from the first line.
* **[41 - The Relic Safe, Wired](./41%20-%20The%20Relic%20Safe%2C%20Wired.md)** — Delegating constructors and the default constructor that must exist.
* **[42 - Spawn With Stats](./42%20-%20Spawn%20With%20Stats.md)** — Member functions, the implicit `this`, and chaining with `*this`.
* **[43 - The Familiar Codex](./43%20-%20The%20Familiar%20Codex.md)** — A class that owns a collection, with `const` methods and a `static` counter.
* **[44 - The Familiar Codex, Animated](./44%20-%20The%20Familiar%20Codex%2C%20Animated.md)** — Header, implementation, and the build command that links them.

### 🧠 8. Memory

Stack, heap, pointers, references, and ownership.

* **[45 - Where Things Live](./45%20-%20Where%20Things%20Live.md)** — Stack, heap, static storage — and which one your variable uses.
* **[46 - The Address-Of Lens](./46%20-%20The%20Address-Of%20Lens.md)** — Pointers: `&`, `*`, `nullptr`, and the two meanings of `*`.
* **[47 - Handles to Memory](./47%20-%20Handles%20to%20Memory.md)** — `new`, `delete`, `->`, and the three rules that come with them.
* **[48 - Reaching Through the Handle](./48%20-%20Reaching%20Through%20the%20Handle.md)** — Pointers as parameters: the object, not a copy — and the null check.
* **[49 - Aliases vs Handles](./49%20-%20Aliases%20vs%20Handles.md)** — When a reference is better than a pointer, and the reassignment trap.
* **[50 - The Empty Handle](./50%20-%20The%20Empty%20Handle.md)** — Null checks, dangling pointers, and who owns the object.
* **[51 - The Last Ember](./51%20-%20The%20Last%20Ember.md)** — Chapter 8 and course recap: memory chosen deliberately.

---

## 🎯 Learning Path

1. **First boot** → compile, run, print, comment, read the error message.
2. **Raw values** → types, declarations, arithmetic, `std::cin`, `getline`.
3. **Decisions** → `if` / `else if` / `else`, comparisons, `rand()`, logical operators.
4. **Iteration** → `do ... while`, `while`, `for`, counting down, pattern rules.
5. **Collections** → vectors, indices, growth, traversal, arrays for fixed sizes.
6. **Functions** → parameters, returns, defaults, composition, scope.
7. **Entities** → structs, classes, constructors, methods, headers.
8. **Memory** → stack and heap, pointers, references, ownership.

---

## 🎯 What You'll Be Able To Do

- Write, compile, and run C++ programs from the terminal, and read `g++`'s diagnostics.
- Pick a type on purpose and explain what it costs.
- Branch and loop without off-by-one errors, and know why a loop terminates.
- Keep a collection of unknown length in a `std::vector` and walk it correctly.
- Split a program into functions with explicit inputs, outputs, and lifetimes.
- Model an entity with a class that upholds its own invariants.
- Explain where a value lives, and choose a pointer, a reference, or a value accordingly.

---

## 🧰 Tools

| Tool | Why |
| :--- | :--- |
| `g++` (or `clang++`) | Compiles `.cpp` into a runnable binary |
| A terminal | Where you compile, and where the output appears |
| Any editor (VS Code recommended) | Write, save, compile |
| Obsidian (this vault) | Notes, field manuals and exercises in one place |

```bash
# the loop every lesson repeats
g++ -std=c++17 -Wall -Wextra main.cpp -o console
./console
```

---

## 🗺️ Course Map

| # | Lessons | What you learn |
| :--- | :--- | :--- |
| 00b / 00c | Field Manuals I & II | Everything at a glance, for consultation |
| 1 | 01 – 06 | Output, program shape, comments, escaping, the compile loop |
| 2 | 07 – 13 | Types, declarations, arithmetic, input, text |
| 3 | 14 – 19 | Branching, comparisons, `rand()`, logic, a scored quiz |
| 4 | 20 – 24 | `do ... while`, `while`, `for`, countdown, ordered rules |
| 5 | 25 – 30 | Vectors, indexing, growth, traversal, arrays |
| 6 | 31 – 37 | Functions, parameters, returns, composition, scope |
| 7 | 38 – 44 | Structs, classes, constructors, methods, header files |
| 8 | 45 – 51 | Stack and heap, pointers, references, ownership |

---

## 🎮 Practice Philosophy

C++ gives you no safety net: an out-of-range index does not throw, an uninitialised pointer is not
detected, and an infinite loop simply keeps running. Every lesson therefore pairs a concept with the
specific trap it hides — undefined behaviour, integer division, first-match ordering, dangling
references.

Compile after every small change, and turn the warnings on. A program that refuses to compile told you
something; a program that compiles and misbehaves quietly is the one that costs an evening.

---

## 🔗 See Also

- [🐍 Python MOC](../%F0%9F%90%8D%20Python/README.md) — the gentler on-ramp to the same logic.
- [🟣 C# MOC](../%F0%9F%9F%A3%20CSharp/README.md) — the same object ideas with garbage collection.
- [🖥️ Command Line MOC](../%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README.md) — moving around and running `g++`.
- [🧮 Data Structures & Algorithms MOC](../%F0%9F%A7%AE%20Data%20Structures%20%26%20Algorithms/README.md) — what to study once vectors and pointers are familiar.
- [🌐 HTML MOC](../%F0%9F%8C%90%20HTML/README.md) · [🎨 CSS MOC](../%F0%9F%8E%A8%20CSS/README.md) · [🟨 JavaScript MOC](../%F0%9F%9F%A8%20JavaScript/README.md) · [⚛️ React MOC](../%E2%9A%9B%EF%B8%8F%20React/README.md) — the web track, for contrast.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="Ola de cierre C++" />
</p>
