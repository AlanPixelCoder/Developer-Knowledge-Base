# 09. In, Through, Out

**Spanish version:** [09 - Entra, Procesa, Sale](./09%20-%20Entra%2C%20Procesa%2C%20Sale.md)

**Course:** C++
**Chapter:** 2 — Raw Values
**Topic:** Assignment versus equality, and the three beats of a computation
**Tags:** `#cpp` `#variables` `#assignment`

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

Every useful program in this course follows the same rhythm: a value goes **in**, something happens
to it, a result comes **out**. Get the rhythm right and the syntax stops being the problem.

```cpp
#include <iostream>

int main() {
  double lantern_oil = 6.0;       // in: what the player starts with
  double burn_per_minute = 0.75;  // in: consumption

  double minutes_left = lantern_oil / burn_per_minute;  // through

  std::cout << "minutes of light: " << minutes_left << "\n";  // out
}
```

## `=` is not `==`

| Operator | Meaning | Example | Result |
| :--- | :--- | :--- | :--- |
| `=` | store the right side into the left | `fuel = 10;` | `fuel` becomes 10 |
| `==` | ask whether the two sides are equal | `fuel == 10` | `true` or `false` |

Using `=` where you meant `==` inside a condition is legal C++ and silently wrong: the assignment
happens, and the *stored value* becomes the condition. Compilers warn about it — that is one of the
reasons `-Wall` exists.

## Two ways to change a variable

```cpp
#include <iostream>

int main() {
  int embers = 4;

  embers = embers + 3;  // long form
  embers += 2;          // compound assignment
  embers++;             // increment by one

  std::cout << "embers: " << embers << "\n";
}
```

## Output

```text
embers: 10
```

> [!NOTE]
> The first snippet prints `8` minutes of light: 6 / 0.75. Division only turns into integer division
> when **both** operands are integers — that trap is one lesson away, in [[10 - Numbers That Lie]].

> [!TIP]
> Write the three beats as three separate statements before you compress anything. A reader should be
> able to point at one line and say "that is where the input enters".

---

**Next:** [[10 - Numbers That Lie]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
