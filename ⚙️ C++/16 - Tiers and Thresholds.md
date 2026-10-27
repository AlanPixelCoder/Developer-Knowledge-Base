# 16. Tiers and Thresholds

**Spanish version:** [16 - Rangos y Umbrales](./16%20-%20Rangos%20y%20Umbrales.md)

**Course:** C++
**Chapter:** 3 — Decisions
**Topic:** Relational operators and the elseless-if chain
**Tags:** `#cpp` `#comparisons` `#else-if`

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

The guild ranks players by reputation: ash, spark, forge, ember. Four tiers, three thresholds, and
one `else if` chain that must be ordered from the highest bar down.

```cpp
#include <iostream>

int main() {
  int reputation = 640;

  if (reputation >= 900) {
    std::cout << "tier: ember\n";
  } else if (reputation >= 600) {
    std::cout << "tier: forge\n";
  } else if (reputation >= 300) {
    std::cout << "tier: spark\n";
  } else {
    std::cout << "tier: ash\n";
  }
}
```

## Output

```text
tier: forge
```

## The six comparison operators

| Operator | Asks | `640` vs `600` |
| :--- | :--- | :--- |
| `>` | strictly greater | true |
| `>=` | greater or equal | true |
| `<` | strictly less | false |
| `<=` | less or equal | false |
| `==` | equal | false |
| `!=` | different | true |

## Why order decides the answer

`else if` stops at the first true condition. Written the other way round — `>= 300` first — a
reputation of 640 matches *spark* and the chain ends there, so `ember` becomes unreachable for
everyone above 300.

> [!WARNING]
> Put the most restrictive condition first. A chain of `else if` is not a set of independent checks;
> it is a list of questions asked in order until one says yes.

> [!TIP]
> If the tiers live in data — a table of `{threshold, name}` — a loop over it replaces the chain
> entirely. You will have the tools for that in [[25 - The Satchel]].

---

**Next:** [[17 - Loaded Dice]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
