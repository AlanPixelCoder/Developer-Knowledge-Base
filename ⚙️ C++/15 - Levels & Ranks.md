# 15. Levels & Ranks

**Spanish version:** [15 - Niveles y Rangos.md](./15%20-%20Niveles%20y%20Rangos.md)

**Course:** C++
**Topic:** Relational Operators and `else if`
**Tags:** `#cpp` `#operators` `#else-if`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

## Relational Operators

To compare two values inside conditions we use relational operators:

| Operator | Meaning |
| :--- | :--- |
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

> [!WARNING]
> `=` assigns; `==` compares. `if (x = 5)` compiles, assigns 5 to `x`, and is always `true`.
> This is the classic C++ footgun — turn on compiler warnings and it gets flagged for you.

## The `else if` Statement

One or more `else if` statements can be added between the `if` and the `else` to check additional
conditions. Only **one** branch will ever execute — the first one whose condition is `true`.
Order matters: the checks run top to bottom.

```cpp
#include <iostream>

int main() {
  int level = 14;

  if (level >= 21) {
    std::cout << "Diamond\n";
  } else if (level >= 16) {
    std::cout << "Platinum\n";
  } else if (level >= 11) {
    std::cout << "Gold\n";
  } else if (level >= 6) {
    std::cout << "Silver\n";
  } else {
    std::cout << "Bronze\n";
  }
}
// Output: Gold
```

> [!TIP]
> **Order from strictest to loosest**
> Because only the first match runs, `level >= 21` must come before `level >= 16`. Reversed, a
> level-25 player would be told they are Bronze.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
