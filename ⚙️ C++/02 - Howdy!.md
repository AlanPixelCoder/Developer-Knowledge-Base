# 02. Howdy!

**Spanish version:** [02 - ¡Howdy!.md](./02%20-%20%C2%A1Howdy%21.md)

**Course:** C++
**Topic:** Outputting text, `std::cout`, and basic syntax
**Tags:** `#cpp` `#output` `#syntax`

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

In C++, the `std::cout` statement (short for **c**haracter **out**put, pronounced "see-out") tells the terminal to output a message.

## Anatomy of an Output Statement

| Piece | Meaning |
| :--- | :--- |
| **`std::cout`** | Instructs the program to output a message |
| **`<<`** | Two left arrows follow the statement — the "insertion" operator |
| **`""`** | The message we want to display is surrounded by double quotes |
| **`;`** | Every C++ statement ends with a semicolon |

The text that is displayed in the terminal is referred to as the **output**.

```cpp
// Howdy 🤠
// Emberfall boot log

#include <iostream>

int main() {
  std::cout << "Emberfall v1.0 — servers online";
}
```

> [!TIP]
> Forget the semicolon and the compiler refuses to run. It is the single most common
> first-day error — and the fastest one to fix.

> [!NOTE]
> **`std::` explained**
> `cout` lives inside the **standard library**, exposed through the `std` namespace. Writing
> `std::cout` is how you say "the `cout` that belongs to `std`". A `using namespace std;`
> line would let you drop the prefix, but this module keeps it explicit — it's the habit that
> scales into larger codebases.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
