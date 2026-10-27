# 13. Coin Flip

**Spanish version:** [13 - Lanzamiento de Moneda.md](./13%20-%20Lanzamiento%20de%20Moneda.md)

**Course:** C++
**Topic:** Introduction to Control Flow and Logic
**Tags:** `#cpp` `#logic` `#control-flow` `#random`

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

Up to this point, C++ programs execute one line at a time, top to bottom, giving the same result
every time. Sometimes we want a program to do **different** things based on different conditions.
This is how programs "make decisions" — by evaluating conditions to introduce logic.

**Control flow** is the order in which the program's code executes. Branches (`if`), loops, and
function calls are all control flow.

## Coin Toss Simulation

- 50% of the time it outputs "Heads".
- 50% of the time it outputs "Tails".

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int num = std::rand() % 2; // 0 or 1

  if (num > 0.5) {
    std::cout << "Heads\n";
  } else {
    std::cout << "Tails\n";
  }
}
```

> [!WARNING]
> **The trap worth noticing**
> `num` is an `int` and `0.5` is a `double`, so the compiler converts `num` before comparing:
> `1 > 0.5` is true, `0 > 0.5` is false. The output is right, but the expression lies about what it
> means — it reads as "more than half" when it is really "equals one". Write `if (num == 1)` and the
> intent is visible. Keep comparisons between integers.

> [!NOTE]
> `srand(time(NULL))` seeds the generator with the current clock so each run differs. Without it,
> every launch produces the same sequence. See [[16 - Fortune Cookie]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
