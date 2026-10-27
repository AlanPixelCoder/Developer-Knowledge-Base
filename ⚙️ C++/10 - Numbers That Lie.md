# 10. Numbers That Lie

**Spanish version:** [10 - Números que Mienten](./10%20-%20N%C3%BAmeros%20que%20Mienten.md)

**Course:** C++
**Chapter:** 2 — Raw Values
**Topic:** Arithmetic, precedence, and integer division
**Tags:** `#cpp` `#operators` `#arithmetic`

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

The combat log says a hit deals **7 damage** and the player has **2 armour points per hit**. Anyone
would write `7 / 2` and expect 3.5. C++ returns 3, and the rounding is not a bug — it is the rule
for two integers.

```cpp
#include <iostream>

int main() {
  int damage = 7;
  int armour_per_hit = 2;

  std::cout << "int division:    " << damage / armour_per_hit << "\n";
  std::cout << "double division: " << damage / 2.0 << "\n";
  std::cout << "remainder:       " << damage % armour_per_hit << "\n";
}
```

## Output

```text
int division:    3
double division: 3.5
remainder:       1
```

Nothing was rounded: the fractional part was **discarded**, because an `int` has nowhere to put it.

## Precedence, in the order that matters

| Priority | Operators | Note |
| :--- | :--- | :--- |
| 1 | `()` | Parentheses beat everything — use them when in doubt |
| 2 | `*` `/` `%` | Left to right |
| 3 | `+` `-` | Left to right |
| 4 | `=` `+=` `-=` | Right to left |

`2 + 3 * 4` is 14, not 20. `(2 + 3) * 4` is 20. `%` is the remainder, and it only accepts integers.

> [!CAUTION]
> A single integer operand is enough to poison the whole expression: `damage / 2 * 1.5` computes
> `damage / 2` first, as an integer, then multiplies. Cast early: `damage / 2.0 * 1.5`.

> [!TIP]
> Read `%` as "what is left over". `damage % armour` tells you whether the hit was fully absorbed —
> and `% 2 == 0` is how you ask whether a number is even.

---

**Next:** [[11 - Echo Chamber]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
