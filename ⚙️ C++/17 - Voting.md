# 17. Voting

**Spanish version:** [17 - Votación.md](./17%20-%20Votaci%C3%B3n.md)

**Course:** C++
**Topic:** Logical Operators
**Tags:** `#cpp` `#logic` `#operators` `#boolean`

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

Logical operators, also known as Boolean operators, combine and evaluate two conditions:

| Operator | Name | Result |
| :--- | :--- | :--- |
| `&&` | and | `true` only if **both** sides are `true` |
| `\|\|` | or | `true` if **at least one** side is `true` |
| `!` | not | flips `true` ↔ `false` |

## Truth Table

| A | B | `A && B` | `A \|\| B` |
| :--- | :--- | :--- | :--- |
| true | true | true | true |
| true | false | false | true |
| false | true | false | true |
| false | false | false | false |

## Example

```cpp
#include <iostream>

int main() {
  int age = 31;
  bool citizen = true;
  bool registered = true;

  if (age >= 18 && citizen && registered) {
    std::cout << "You can vote!\n";
  } else if (age < 18) {
    std::cout << "You are not old enough to vote.\n";
  } else if (!citizen) {
    std::cout << "You are not eligible to vote.\n";
  } else if (!registered) {
    std::cout << "You need to register first.\n";
  } else {
    std::cout << "You have not met the requirements.\n";
  }
}
```

> [!TIP]
> **Short-circuit evaluation**
> C++ stops evaluating an `&&` chain at the first `false`, and an `||` chain at the first `true`.
> That lets you write `if (ptr != nullptr && *ptr == 42)` safely — the dereference never runs when
> the check fails. See [[44 - Nullptr]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
