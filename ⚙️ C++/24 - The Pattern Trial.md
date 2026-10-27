# 24. The Pattern Trial

**Spanish version:** [24 - La Prueba del Patrón](./24%20-%20La%20Prueba%20del%20Patr%C3%B3n.md)

**Course:** C++
**Chapter:** 4 — Iteration
**Topic:** Chapter 4 recap: rules that overlap, evaluated in order
**Tags:** `#cpp` `#recap` `#loops`

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

The tutorial's final gate lights a beacon for every tenth of the run. The rule has three cases, and
the third one is the trap: some ticks satisfy two of them at once.

```cpp
#include <iostream>

int main() {
  for (int step = 1; step <= 15; step++) {
    if (step % 6 == 0) {
      std::cout << "WILDFIRE\n";
    } else if (step % 2 == 0) {
      std::cout << "Ember\n";
    } else if (step % 3 == 0) {
      std::cout << "Ash\n";
    } else {
      std::cout << step << "\n";
    }
  }
}
```

## Output

```text
1
Ember
Ash
Ember
5
WILDFIRE
7
Ember
Ash
Ember
11
WILDFIRE
13
Ember
Ash
```

## Why `% 6` is checked first

`6` is the least common multiple of `2` and `3`. Any step divisible by both reaches `WILDFIRE` only
because that test comes before the other two; move it down one line and step 6 prints `Ember`
instead, and `WILDFIRE` never fires.

| Step | `% 6` | `% 2` | `% 3` | Branch taken |
| :--- | :--- | :--- | :--- | :--- |
| 6 | 0 | 0 | 0 | WILDFIRE |
| 4 | 4 | 0 | 1 | Ember |
| 9 | 3 | 1 | 0 | Ash |
| 7 | 1 | 1 | 1 | number |

> [!IMPORTANT]
> Order is not a style preference here, it is the algorithm. When conditions overlap, the first
> match wins and every later test is dead code for that value.

> [!TIP]
> A loop plus a chain of conditions is the shape of half the rules in a game: status effects, damage
> types, loot tiers. Write the most specific rule first and read the output aloud — a wrong order is
> audible immediately.

---

**Next:** [[25 - The Satchel]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
