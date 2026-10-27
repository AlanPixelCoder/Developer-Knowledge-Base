# 21. Counting Sheep

**Spanish version:** [21 - Contando Ovejas.md](./21%20-%20Contando%20Ovejas.md)

**Course:** C++
**Topic:** `for` Loops
**Tags:** `#cpp` `#loops` `#for` `#iteration`

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

To loop through a block of code a specified number of times, use a `for` loop.

A `for` loop has **three parts** inside the parentheses, separated by semicolons:

1. **Initialization** — `int i = 0;` creates the counter.
2. **Condition** — `i < 6;` is checked before every iteration.
3. **Change** — `i++` runs after every iteration.

```cpp
for (int i = 0; i < 6; i++) {
  // body
}
```

The counter starts at its initial value. If the condition is true, the body runs. Then the
counter changes, and the loop repeats until the condition is no longer true.

## Execution Order

| Step | What happens |
| :--- | :--- |
| 1 | Initialization — **once**, before anything else |
| 2 | Condition — checked; `false` exits the loop |
| 3 | Body — runs |
| 4 | Change — `i++` |
| 5 | Back to step 2 |

## Example

```cpp
#include <iostream>

int main() {
  for (int i = 1; i <= 50; i++) {
    std::cout << i << " sheep\n";
  }
}
```

> [!WARNING]
> **`<` vs `<=` is an off-by-one waiting to happen**
> `i < 50` prints 1–49. `i <= 50` prints 1–50. Count the elements you actually want before you
> pick the comparison — this is the single most common loop bug in existence.

> [!TIP]
> `i++` is the increment operator. `i--` decrements — the whole subject of [[22 - 99 Bottles]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
