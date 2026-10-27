# 18. Guards and Gates

**Spanish version:** [18 - Guardias y Portones](./18%20-%20Guardias%20y%20Portones.md)

**Course:** C++
**Chapter:** 3 — Decisions
**Topic:** Logical operators and short-circuit evaluation
**Tags:** `#cpp` `#logic` `#booleans`

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

A gate that opens only when the player carries light **and** is not exhausted needs a compound
condition: two facts, one decision.

```cpp
#include <iostream>

int main() {
  bool has_lantern = true;
  bool is_exhausted = false;
  int depth = 12;

  std::cout << std::boolalpha;

  std::cout << "lantern and not exhausted: "
            << (has_lantern && !is_exhausted) << "\n";
  std::cout << "lantern or rope:          "
            << (has_lantern || false) << "\n";
  std::cout << "can descend:              "
            << (has_lantern && !is_exhausted && depth < 20) << "\n";
}
```

## Output

```text
lantern and not exhausted: true
lantern or rope:          true
can descend:              true
```

`std::boolalpha` makes `bool` print as `true` / `false` instead of `1` / `0`; it stays in effect for
the rest of the stream.

## The three operators

| Operator | Name | True when |
| :--- | :--- | :--- |
| `&&` | and | **both** sides are true |
| `\|\|` | or | **at least one** side is true |
| `!` | not | the single operand is false |

## Short-circuit: the part that surprises people

`a && b` evaluates `b` only if `a` is true. `a || b` evaluates `b` only if `a` is false. That is both
a speed trick and a safety mechanism — and a source of bugs when `b` has effects.

> [!WARNING]
> `std::cout << has_lantern && is_exhausted` does **not** print a boolean. `<<` binds tighter than
> `&&`, so it reads as `(std::cout << has_lantern) && ...`. Wrap the condition in parentheses.

> [!TIP]
> Use short-circuit deliberately: `if (index < size && items[index] > 0)` is safe because the second
> test never runs when the first fails. Swap the order and the same line reads out of bounds.

---

**Next:** [[19 - Trial by Question]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
