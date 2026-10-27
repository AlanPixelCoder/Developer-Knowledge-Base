# ⚙️ C++: Systems Programming & Game Engine Foundations (MOC)

**Español:** [README-ES.md](./README-ES.md)

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B20-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++20">
  <img src="https://img.shields.io/badge/Toolchain-g%2B%2B%20%7C%20Clang-7C5CFF?style=for-the-badge&logo=llvm&logoColor=white" alt="Toolchain">
  <img src="https://img.shields.io/badge/Paradigm-Procedural%20%26%20OOP-FF6B35?style=for-the-badge" alt="Procedural & OOP">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER_TO_ADVANCED-6CC24A?style=for-the-badge" alt="Beginner to advanced">
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

**Note:**
This module is the Map of Content (MOC) for the C++ notes in this Obsidian vault. C++ is the language
behind game engines, operating systems, browsers, and anything else that cannot afford to be slow.
It gives you the machine's actual memory as a thing you can point at — which is both the reason it is
fast and the reason it is unforgiving. Every example here is minimal and runnable as written.

**Tip:**
Start at [[01 - The Program]]. Compile and run something before you study anything else: the loop of
*write → `g++` → `./a.out`* is the habit the whole module depends on. Then follow the chapter order —
each one assumes the one before it.

**Prerequisite:** none. A terminal, a compiler (`g++` or `clang++`), and a text editor. See
[[Compile & Execute]] if `g++` is not installed yet.

> [!NOTE]
> **The Emberfall narrative**
> Every exercise belongs to the same fictional project: *Emberfall*, a roguelike. Fortunes become
> quest rumours, coin flips become loot rolls, bank accounts become guild vaults, and terminal menus
> become taverns. The syntax never changes — that is the point: you learn one vocabulary and reuse it
> in every program you will ever ship.

---

## 🗺️ Map of Content

### 📚 Reference & Cheatsheets

* **Cheatsheets:**
  * [00b - C++ Cheatsheet](./00b%20-%20C%2B%2B%20Cheatsheet.md) — I/O, types, operators, control flow, loops, vectors, functions, classes, pointers.
  * [00c - C++ Cheatsheet II](./00c%20-%20C%2B%2B%20Cheatsheet%20II.md) — Scope, access modifiers, constructors, pass-by-reference, pointer vs reference table, headers.

### ⚡ 1. Hello, Systems (Chapter 1)

* **[01 - The Program](./01%20-%20The%20Program.md)** — Stroustrup, 1979, "C with Classes", where C++ runs today, and the `.cpp` file.
* **[02 - Howdy!](./02%20-%20Howdy%21.md)** — `std::cout`, the four pieces of an output statement, the semicolon.
* **[03 - See Ya Later Alligator](./03%20-%20See%20Ya%20Later%20Alligator.md)** — `#include`, `int main()`, code blocks, escape sequences (`\n`, `\t`).
* **[04 - Ouija Board](./04%20-%20Ouija%20Board.md)** — `//` and `/* */`, why commented-out code is a smell.
* **[05 - Sign Bunny](./05%20-%20Sign%20Bunny.md)** — Chapter 1 recap and ASCII art that survives escaping.
* **[Compile & Execute](./Compile%20%26%20Execute.md)** — Source vs machine code, `g++`, `-o`, `./a.out`.

### 🔢 2. Variables, Types & Math (Chapter 2)

* **[06 - Data Types](./06%20-%20Data%20Types.md)** — `int`, `double`, `char`, `std::string`, `bool` — and how many bytes each costs.
* **[07 - Declaration of Independence](./07%20-%20Declaration%20of%20Independence.md)** — Declaring, naming rules, `snake_case` vs `PascalCase`.
* **[08 - IPO](./08%20-%20IPO.md)** — Input → Process → Output, assignment vs equality, printing variables.
* **[09 - Temperature](./09%20-%20Temperature.md)** — Arithmetic operators, precedence, the integer division trap.
* **[10 - Knighthood](./10%20-%20Knighthood.md)** — Chaining output with multiple `<<`.
* **[11 - Month-over-Month (MoM)](./11%20-%20Month-over-Month%20%28MoM%29.md)** — `std::cin`, the direction of the arrows, and the percentage formula.
* **[12 - Cat Years](./12%20-%20Cat%20Years.md)** — Chapter 2 recap applied to a formula with an edge case.

### 🧠 3. Logic & Control Flow (Chapter 3)

* **[13 - Coin Flip](./13%20-%20Coin%20Flip.md)** — Control flow, `srand`, and a real bug worth spotting.
* **[14 - Fever](./14%20-%20Fever.md)** — `if` / `else`, and why braces are not optional in practice.
* **[15 - Levels & Ranks](./15%20-%20Levels%20%26%20Ranks.md)** — Six relational operators, `else if`, first-match-wins ordering.
* **[16 - Fortune Cookie](./16%20-%20Fortune%20Cookie.md)** — `std::rand()`, `%` ranges, seeding with `time(NULL)`.
* **[17 - Voting](./17%20-%20Voting.md)** — `&&`, `||`, `!`, truth tables, short-circuit evaluation.
* **[18 - Trivia Quiz](./18%20-%20Trivia%20Quiz.md)** — Chapter 3 recap as a scored quiz project.

### 🔁 4. Loops & Iteration (Chapter 4)

* **[19 - Enter PIN](./19%20-%20Enter%20PIN.md)** — What iteration is, and the four pieces of a loop that terminates.
* **[20 - Guess the Number](./20%20-%20Guess%20the%20Number.md)** — `while`: the loop that can run zero times.
* **[21 - Counting Sheep](./21%20-%20Counting%20Sheep.md)** — `for`: initialization, condition, change — and off-by-one.
* **[22 - 99 Bottles](./22%20-%2099%20Bottles.md)** — Counting down with `i--`.
* **[23 - Fizz Buzz](./23%20-%20Fizz%20Buzz.md)** — Chapter 4 recap and the interview classic, where ordering is everything.

### 📦 5. Vectors & Collections (Chapter 5)

* **[24 - Survival Gear](./24%20-%20Survival%20Gear.md)** — `std::vector`, headers, and why vectors replaced arrays.
* **[25 - Lemonade Stand](./25%20-%20Lemonade%20Stand.md)** — 0-indexing, `v[size() - 1]`, and undefined behaviour past the end.
* **[26 - Order Cart](./26%20-%20Order%20Cart.md)** — `.push_back()`, `.pop_back()`, `.size()`.
* **[27 - Roadtrip Playlist](./27%20-%20Roadtrip%20Playlist.md)** — Iterating with `for` and `.size()` as the bound.
* **[28 - Sum of Even - Product of Odd](./28%20-%20Sum%20of%20Even%20-%20Product%20of%20Odd.md)** — Chapter 5 recap and identity values (`0` for sums, `1` for products).
* **[Arrays](./Arrays.md)** — C-style arrays vs `std::vector`: fixed vs dynamic, stack vs heap.

### 🧩 6. Functions & Scope (Chapter 6)

* **[29 - D.R.Y.](./29%20-%20D.R.Y..md)** — Don't Repeat Yourself, and what a function actually buys you.
* **[30 - Food Menu](./30%20-%20Food%20Menu.md)** — Defining and calling `void` functions; declare before you call.
* **[31 - OOO](./31%20-%20OOO.md)** — Parameters are placeholders, arguments are actual values.
* **[32 - Conversions](./32%20-%20Conversions.md)** — `return`, and the difference between `void` and a return type.
* **[32 - Conversions (Continuation)](./32%20-%20Conversions%20%28Continuation%29.md)** — Using a returned value inside an expression.
* **[33 - Tips Calculator](./33%20-%20Tips%20Calculator.md)** — Chapter 6 recap: gather, compute, report.
* **[Scope in C++](./Scope%20in%20C%2B%2B.md)** — Local vs global, lifetime, and shadowing.

### 🏛️ 7. Classes & OOP (Chapter 7)

* **[34 - Restaurants](./34%20-%20Restaurants.md)** — `class` as a blueprint; the semicolon everyone forgets.
* **[35 - Public vs. Private](./35%20-%20Public%20vs.%20Private.md)** — Access modifiers and encapsulation.
* **[36 - Bank Accounts](./36%20-%20Bank%20Accounts.md)** — Attributes vs methods; `this`.
* **[37 - Bank Accounts (Continuation)](./37%20-%20Bank%20Accounts%20%28Continuation%29.md)** — A working deposit / withdraw / display system.
* **[38 - Classic Cars](./38%20-%20Classic%20Cars.md)** — Constructors, default values, and the implicit constructor that disappears.
* **[39 - Pet Rescue](./39%20-%20Pet%20Rescue.md)** — Chapter 7 recap as an OOP project skeleton.
* **[39 - Pet Rescue (Continuation)](./39%20-%20Pet%20Rescue%20%28Continuation%29.md)** — The methods, the stats caps, and the interactive menu.

### 🧠 8. Pointers & Memory (Chapter 8)

* **[40 - Memories](./40%20-%20Memories.md)** — Memory addresses, hexadecimal, and the stack picture.
* **[40 - Memories (Continuation)](./40%20-%20Memories%20%28Continuation%29.md)** — The `&` address-of operator and the `(void*)` cast.
* **[41 - A Few Pointers](./41%20-%20A%20Few%20Pointers.md)** — `int*`, type matching, and the four reasons pointers exist.
* **[42 - Dereference](./42%20-%20Dereference.md)** — `*` as declaration vs `*` as operator.
* **[43 - References vs. Pointers](./43%20-%20References%20vs.%20Pointers.md)** — Aliases, the comparison table, pass-by-reference.
* **[44 - Nullptr](./44%20-%20Nullptr.md)** — The pointer that points nowhere, and why it beats `NULL`.
* **[45 - The End](./45%20-%20The%20End.md)** — Chapter 8 recap and the whole course in one table.

---

## 🎯 Learning Path

1. **Hello, systems** → compile, run, output, comment, escape.
2. **Variables & math** → types, declarations, `cin`, arithmetic.
3. **Logic** → `if` / `else if` / `else`, relational and logical operators, randomness.
4. **Loops** → `while` and `for`, incrementing and decrementing, iteration bounds.
5. **Vectors** → dynamic collections, indices, methods, iteration.
6. **Functions** → DRY, parameters and arguments, returns, scope.
7. **Classes** → blueprints, encapsulation, constructors, methods.
8. **Pointers** → addresses, dereferencing, references, `nullptr`.

---

## 🎯 What You'll Be Able To Do

- Write, compile, and run C++ programs from the terminal with `g++`.
- Choose the right data type and know what it costs in memory.
- Print formatted output and read user input with `std::cin`.
- Control flow with conditionals and both loop types, without off-by-one errors.
- Store and traverse collections with `std::vector` instead of parallel variables.
- Break a program into functions with clear inputs, outputs, and scope.
- Model entities with classes, constructors, and methods — the shape of game code.
- Explain what a pointer is, when to use a reference instead, and why `nullptr` matters.

---

## 🧰 Tools

| Tool | Why |
| :--- | :--- |
| `g++` or `clang++` | Compiles `.cpp` into a runnable executable |
| A terminal | Where you compile and where the program's output appears |
| Any code editor (VS Code recommended) | Write, save, and run `.cpp` files |
| Obsidian (this vault) | Keep the notes, cheatsheets, and exercises together |

```bash
# the loop you will repeat for the rest of the module
g++ -Wall -Wextra -std=c++17 main.cpp -o main
./main
```

---

## 🗺️ Course Map

| # | Notes | What you learn |
| :--- | :--- | :--- |
| 00b / 00c | Cheatsheets I & II | Everything at a glance, for consultation |
| 1 | 01 – 05 + Compile & Execute | Output, structure, comments, escaping, the compile loop |
| 2 | 06 – 12 | Types, declarations, assignment, arithmetic, input |
| 3 | 13 – 18 | `if` / `else`, comparisons, logical operators, `rand()` |
| 4 | 19 – 23 | `while`, `for`, increment/decrement, Fizz Buzz |
| 5 | 24 – 28 + Arrays | Vectors, indices, methods, iteration, arrays vs vectors |
| 6 | 29 – 33 + Scope | Functions, parameters, returns, DRY, local vs global |
| 7 | 34 – 39 | Classes, access, methods, constructors, OOP project |
| 8 | 40 – 45 | Addresses, pointers, dereference, references, `nullptr` |

---

## 🎮 Practice Philosophy

C++ gives you no safety net: an out-of-bounds index does not throw, an uninitialized pointer is not
detected, and an infinite loop just keeps running. That is why every note here pairs a concept with
the **specific trap** it hides — undefined behaviour, integer division, first-match ordering,
uninitialized memory.

Compile after every small change. A C++ program that produces an error is a program that told you
something; a program that compiles and misbehaves silently is the one that costs you an evening.

---

## 🔗 See Also

- [🐍 Python MOC](../%F0%9F%90%8D%20Python/README.md) — the gentler on-ramp to programming logic before manual memory.
- [🟣 C# MOC](../%F0%9F%9F%A3%20CSharp/README.md) — the same OOP ideas, with garbage collection and Unity.
- [🖥️ Command Line MOC](../%F0%9F%96%A5%EF%B8%8F%20Command%20Line/README.md) — navigating the folder, running `g++`, executing binaries.
- [🧮 Data Structures & Algorithms MOC](../%F0%9F%A7%AE%20Data%20Structures%20%26%20Algorithms/README.md) — what to do once vectors and pointers are familiar.
- [🌐 HTML MOC](../%F0%9F%8C%90%20HTML/README.md) · [🎨 CSS MOC](../%F0%9F%8E%A8%20CSS/README.md) · [🟨 JavaScript MOC](../%F0%9F%9F%A8%20JavaScript/README.md) · [⚛️ React MOC](../%E2%9A%9B%EF%B8%8F%20React/README.md) — the web track, for contrast with systems programming.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer wave" />
</p>
