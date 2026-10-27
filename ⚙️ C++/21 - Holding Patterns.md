# 21. Holding Patterns

**Spanish version:** [21 - Patrones de Espera](./21%20-%20Patrones%20de%20Espera.md)

**Course:** C++
**Chapter:** 4 — Iteration
**Topic:** The while loop and a condition that changes
**Tags:** `#cpp` `#while` `#loops`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The lantern burns while it has oil. No fixed count, no known end: just a condition that is true
until it is not.

```cpp
#include <iostream>

int main() {
  double oil = 3.0;
  int minutes = 0;

  while (oil > 0.0) {
    oil -= 0.75;
    minutes++;
    if (oil < 0.0) {
      oil = 0.0;  // never show negative fuel in the HUD
    }
    std::cout << "minute " << minutes << ": oil " << oil << "\n";
  }

  std::cout << "darkness after " << minutes << " minutes\n";
}
```

## Output

```text
minute 1: oil 2.25
minute 2: oil 1.5
minute 3: oil 0.75
minute 4: oil 0
darkness after 4 minutes
```

## `while` in one sentence

Repeat the body **as long as** the condition is true; check before every pass, including the first.
If the condition starts false, the body never runs.

| Situation | Loop that fits |
| :--- | :--- |
| Unknown number of passes | `while` |
| At least one pass, then maybe more | `do ... while` |
| Known count, or counting a range | `for` (next lesson) |

## The clamp matters

`oil -= 0.75` overshoots: after four passes the true value is `0.0`, but with other numbers it can go
negative. Floating point cares; a HUD that shows `-0.25` looks broken even when the loop is right.

> [!WARNING]
> `while (oil > 0.0)` with `oil` never modified is an infinite loop, and the program prints forever.
> Before writing the condition, write the line that will make it false.

> [!TIP]
> `minutes` exists only to explain the run. Real code would print the fuel, not the counter — but a
> counter is the cheapest way to see how many passes a `while` actually made.

---

**Next:** [[22 - Tick by Tick]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
