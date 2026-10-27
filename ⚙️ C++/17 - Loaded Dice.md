# 17. Loaded Dice

**Spanish version:** [17 - Dados Cargados](./17%20-%20Dados%20Cargados.md)

**Course:** C++
**Chapter:** 3 — Decisions
**Topic:** Random ranges, the modulo trick, and its bias
**Tags:** `#cpp` `#random` `#modulo`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-3-7C5CFF?style=for-the-badge" alt="Chapter 3">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

`std::rand()` returns a number between `0` and `RAND_MAX`. Every game needs a different range, and
one expression covers all of them.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int d6 = std::rand() % 6 + 1;      // 1..6
  int d20 = std::rand() % 20 + 1;    // 1..20
  int zero_based = std::rand() % 5;  // 0..4
  double chance = (std::rand() % 101) / 100.0;  // 0.00..1.00

  std::cout << "d6: " << d6 << "\n";
  std::cout << "d20: " << d20 << "\n";
  std::cout << "0..4: " << zero_based << "\n";
  std::cout << "chance: " << chance << "\n";
}
```

## The formula, in two parts

| Shape | Gives | Example |
| :--- | :--- | :--- |
| `rand() % n` | `0` to `n - 1` | `% 5` → `0 1 2 3 4` |
| `rand() % n + 1` | `1` to `n` | `% 5 + 1` → `1 2 3 4 5` |

The `%` folds the generator's huge range into the small one; the `+ 1` shifts the result.

> [!CAUTION]
> `%` is not perfectly uniform. If `RAND_MAX + 1` is not a multiple of `n`, the low values come up
> slightly more often. It is invisible in a dice roll and not invisible in a loot table that runs a
> million times. That is the case `std::uniform_int_distribution` was written for.

> [!NOTE]
> `(rand() % 101) / 100.0` gives a percentage between `0.0` and `1.0` — but the division is by
> `100.0`, not `100`, precisely so the fraction survives. See [[10 - Numbers That Lie]].

> [!TIP]
> Name the range in the variable: `d20`, `d6`, `chance`. `roll` in three places is how a 20-sided die
> quietly becomes a 6-sided one during a refactor.

---

**Next:** [[18 - Guards and Gates]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
