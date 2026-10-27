# 35. Chained Returns

**Spanish version:** [35 - Retornos Encadenados](./35%20-%20Retornos%20Encadenados.md)

**Course:** C++
**Chapter:** 6 — Functions
**Topic:** Composing functions: small pieces that call each other
**Tags:** `#cpp` `#functions` `#composition`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

A rune's final damage is built in stages: base, then the affinity multiplier, then the armour
subtraction, then the floor of one. Each stage is a function, and each one is testable alone.

```cpp
#include <iostream>

double base_damage(int power) {
  return power * 2.5;
}

double affinity(double value, double multiplier) {
  return value * multiplier;
}

int after_armor(double value, int armor) {
  double reduced = value - armor;
  return reduced < 1.0 ? 1 : static_cast<int>(reduced);
}

int rune_damage(int power, double multiplier, int armor) {
  return after_armor(affinity(base_damage(power), multiplier), armor);
}

int main() {
  std::cout << rune_damage(10, 1.5, 4) << "\n";
  std::cout << rune_damage(2, 1.0, 30) << "\n";
}
```

## Output

```text
33
1
```

## Read the pipeline inside out

`rune_damage` reads as: base from power, then affinity, then armour, then clamp.

| Stage | In | Out |
| :--- | :--- | :--- |
| `base_damage(10)` | 10 | 25 |
| `affinity(25, 1.5)` | 25 | 37.5 |
| `after_armor(37.5, 4)` | 37.5 | 33 |

Chaining calls in one expression is fine **when the order matches the sentence**. When it stops
matching, name an intermediate variable.

## Why split at all

- Each stage can be replaced by a balance change without touching the others.
- Each stage can be checked with one call and one expected number.
- The printed trace of a broken run points at one stage, not at "the whole formula".

> [!IMPORTANT]
> `static_cast<int>` truncates toward zero, so `after_armor(4.9, 0)` returns 4, not 5. If the game
> rounds damage, decide explicitly: cast after adding `0.5`, or use `std::lround`.

> [!TIP]
> Keep each function to one idea. If a name needs "and" in it — `damage_and_armor` — it is two
> functions wearing one coat.

---

**Next:** [[36 - The Gate Tax]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
