# 08. Naming the Parts

**Spanish version:** [08 - Nombrar las Piezas](./08%20-%20Nombrar%20las%20Piezas.md)

**Course:** C++
**Chapter:** 2 — Raw Values
**Topic:** Declaring variables, valid names and naming conventions
**Tags:** `#cpp` `#variables` `#style`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

A declaration tells the compiler three things at once: the type, the name, and — if you initialise
it — the starting value. Skip the third and C++ gives you whatever was already in that memory.

```cpp
#include <iostream>

int main() {
  int ticks_per_second = 60;          // one value, one purpose
  double gravity = 9.81;              // no suffix needed for double
  char difficulty = 'H';              // single quotes: one character
  bool vsync_enabled = true;          // lowercase true / false
  std::string engine_name = "Emberfall";  // double quotes: text

  std::cout << engine_name << " | ticks " << ticks_per_second << "\n";
  std::cout << "gravity " << gravity << " | difficulty " << difficulty << "\n";
  std::cout << "vsync " << vsync_enabled << "\n";
}
```

## What a name may and may not be

| Rule | Valid | Invalid |
| :--- | :--- | :--- |
| Letters, digits, underscore | `spawn_rate_2` | `spawn-rate` |
| Cannot start with a digit | `level2` | `2level` |
| Case matters | `Level` ≠ `level` | — |
| No keywords | `value` | `int`, `class`, `return` |

## Two conventions that keep the engine readable

| Convention | Looks like | Used for |
| :--- | :--- | :--- |
| `snake_case` | `spawn_rate` | variables and functions |
| `PascalCase` | `SpawnTable` | types and classes |

## Output

```text
Emberfall | ticks 60
gravity 9.81 | difficulty H
vsync 1
```

> [!NOTE]
> `bool` prints as `1` and `0` unless you ask for `std::boolalpha` first. The value is still a real
> boolean; only the formatting changes.

> [!WARNING]
> `Level` and `level` are two different variables. That is legal, compiles cleanly, and is the
> fastest way to spend an afternoon debugging a value that never changes.

---

**Next:** [[09 - In, Through, Out]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
