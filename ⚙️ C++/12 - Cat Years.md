# 12. Cat Years

**Spanish version:** [12 - Años Gato.md](./12%20-%20A%C3%B1os%20Gato.md)

**Course:** C++
**Topic:** Chapter 2 Recap & Application
**Tags:** `#cpp` `#recap` `#input` `#math`

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

## Chapter 2 Recap

- **Data types:** `int`, `double`, `char`, `std::string`, `bool`.
- **Arithmetic operators:** `+`, `-`, `*`, `/`.
- **The `%` modulo** finds the remainder.
- **Chaining** writes multiple outputs in a single statement with `<<`.
- **`std::cin`** reads user input into a declared variable.

## Example

The first two cat years count as 24 human years; every year after that counts as roughly 4.

```cpp
#include <iostream>

int main() {
  int cat;
  int human;

  std::cout << "Welcome to the Cat Years program! This only works for cats older than 2 years old.\n";
  std::cout << "Enter your cat's age: ";
  std::cin >> cat;

  human = (cat - 2) * 4 + 24;

  std::cout << "Your cat is " << human << " years old in human years.\n";
}
```

> [!TIP]
> **Guard the edge case**
> Below age 2 the formula goes negative — a one-month-old kitten would be reported as
> "−16 human years". Add an `if (cat < 2)` branch once you reach [[14 - Fever]] and the program
> stops lying to its user.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
