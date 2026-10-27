# 15. Doors and Keys

**Spanish version:** [15 - Puertas y Llaves](./15%20-%20Puertas%20y%20Llaves.md)

**Course:** C++
**Chapter:** 3 — Decisions
**Topic:** if / else, braces, and the two-way branch
**Tags:** `#cpp` `#if` `#control-flow`

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

A locked gate has exactly two outcomes, and a two-way branch is the smallest decision C++ can make.

```cpp
#include <iostream>

int main() {
  int required_key = 7;
  int held_key = 7;

  if (held_key == required_key) {
    std::cout << "the gate swings open\n";
  } else {
    std::cout << "the lock refuses the key\n";
  }
}
```

Change `held_key` to `3` and the other line prints. Nothing else about the program changes.

## The shape

| Piece | Meaning |
| :--- | :--- |
| `if (condition)` | Run the next block only when the condition is true |
| `else` | Run the other block when it is not |
| `{ }` | The block; required as soon as there is more than one statement |

`else` is optional. Without it, a false condition simply means *do nothing and continue*.

> [!WARNING]
> Without braces, **only the next statement** belongs to the `if`. Add a second line and it always
> runs, no matter the condition — and the indentation will insist it is part of the branch.

> [!TIP]
> Prefer a positive condition. `if (has_key)` reads better than `if (!no_key)` and costs the reader
> one less mental negation.

---

**Next:** [[16 - Tiers and Thresholds]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
