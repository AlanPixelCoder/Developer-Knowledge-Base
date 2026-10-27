# 01. Cold Start

**Spanish version:** [01 - Arranque en Frío](./01%20-%20Arranque%20en%20Fr%C3%ADo.md)

**Course:** C++
**Chapter:** 1 — First Boot
**Topic:** What C++ is, where it came from, and the file everything starts from
**Tags:** `#cpp` `#foundations` `#toolchain`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Every project in this module belongs to one imaginary studio and one imaginary product: the
**Emberfall engine**, the console a small team uses to boot, configure and debug its game. Lesson
one is not about the game. It is about the file the engine is built from.

## Where the language comes from

Bjarne Stroustrup started it at Bell Labs in **1979** as *C with Classes*: C's speed and direct
access to memory, plus the ability to define your own types. It was renamed **C++** in 1983, and
the standards that matter today arrived decades later — C++11, C++17, C++20, C++23.

## What people build with it

| Domain | Why C++ and not something friendlier |
| :--- | :--- |
| Game engines | Frame budgets are measured in milliseconds; there is no room for a garbage collector pause |
| Operating systems | The code has to run before any runtime exists |
| Browsers | Parsing, rendering and scripting at interactive speed |
| Trading, simulation, embedded | Deterministic timing and predictable memory |

The trade is explicit: you manage memory and types yourself, and in exchange you get control that
no scripting language offers.

## The file you will live in

C++ source lives in `.cpp` files. Each one is a **translation unit**: the compiler reads it on its
own, without knowing about the others, and produces an object file. One of those units contains
`main` — the entry point where the operating system starts your program.

```cpp
int main() {
  return 0;
}
```

`return 0;` is the exit code the shell receives: zero means *finished without error*. This program
does nothing else, and it already compiles, links and runs.

> [!NOTE]
> A `.cpp` file is compiled in isolation. That is why the same header gets included in many files:
> each unit needs to know the declarations on its own.

> [!TIP]
> Name the file after what it holds — `engine_console.cpp`, `spawn_table.cpp` — not after the
> lesson number. The compiler does not care; the next person reading the folder does.

---

**Next:** [[02 - First Light]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
