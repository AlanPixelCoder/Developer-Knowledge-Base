# 13. Level Scaling

**Spanish version:** [13 - Escalado de Niveles](./13%20-%20Escalado%20de%20Niveles.md)

**Course:** C++
**Chapter:** 2 — Raw Values
**Topic:** Chapter 2 recap: a formula with an edge case
**Tags:** `#cpp` `#recap` `#arithmetic`

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

The engine turns total experience into a level and a progress bar. Three values, one formula, and one
edge case that decides whether the UI shows a bar or a blank space.

```cpp
#include <iostream>

int main() {
  int xp = 2450;
  int xp_per_level = 300;

  int level = xp / xp_per_level;
  int xp_into_level = xp % xp_per_level;
  double progress = 100.0 * xp_into_level / xp_per_level;

  std::cout << "xp: " << xp << "\n";
  std::cout << "level: " << level << "\n";
  std::cout << "into level: " << xp_into_level << "\n";
  std::cout << "progress: " << progress << "%\n";
}
```

## Output

```text
xp: 2450
level: 8
into level: 50
progress: 16.6667%
```

## Why the three lines work

| Expression | Type | Why that type |
| :--- | :--- | :--- |
| `xp / xp_per_level` | `int` | Levels are counted in whole steps |
| `xp % xp_per_level` | `int` | What is left inside the current level |
| `100.0 * ...` | `double` | `100.0` forces the division to keep the fraction |

## The edge case

```cpp
#include <iostream>

int main() {
  int xp = 120;
  int xp_per_level = 300;

  std::cout << "level: " << xp / xp_per_level << "\n";
  std::cout << "progress: " << 100.0 * (xp % xp_per_level) / xp_per_level << "%\n";
}
```

```text
level: 0
progress: 40%
```

A fresh character is level **0**, which is correct arithmetic and wrong for the UI. Guard it:

```cpp
int level = 1 + xp / xp_per_level;
```

> [!CAUTION]
> `xp_per_level` must never be zero: integer division by zero is undefined behaviour, and the program
> may crash, print garbage or appear to work. Validate config values before you divide by them.

> [!NOTE]
> `100.0 * xp_into_level / xp_per_level` keeps the fraction because the multiplication happens first,
> left to right. Were it written `100 * (xp_into_level / xp_per_level)`, the inner division would be
> integer and the result would be `0`.

---

**Next:** [[14 - Forked Roads]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
