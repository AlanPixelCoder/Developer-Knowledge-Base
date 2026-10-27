# 09. Temperature

**Spanish version:** [09 - Temperatura.md](./09%20-%20Temperatura.md)

**Course:** C++
**Topic:** Arithmetic Operators
**Tags:** `#cpp` `#math` `#operators`

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

Computers are incredible at doing math calculations. C++ has the following arithmetic operators:

| Operator | Operation | Note |
| :--- | :--- | :--- |
| `+` | Addition | |
| `-` | Subtraction | |
| `*` | Multiplication | |
| `/` | Division | Integer division truncates when both operands are `int` |
| `%` | Modulo | Returns the **remainder** — only works with integers |

In C++, parentheses have the highest order of operations. We can use parentheses to calculate
the total in just a single line of code.

## Operator Precedence

1. `( )` — parentheses
2. `*`, `/`, `%` — left to right
3. `+`, `-` — left to right

## Example

```cpp
#include <iostream>

int main() {
  double fahrenheit = 65.0;
  double celsius = (fahrenheit - 32) / 1.8;

  std::cout << celsius; // Output: 18.3333
}
```

> [!WARNING]
> **The integer division trap**
> `5 / 2` is `2`, not `2.5`, because both operands are `int`. Write `5.0 / 2` (or cast) when you
> want the fraction. This single bug has sunk more than one temperature converter.

> [!TIP]
> The formula itself: $C = (F - 32) \div 1.8$ — and the inverse $F = C 	imes 1.8 + 32$.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
