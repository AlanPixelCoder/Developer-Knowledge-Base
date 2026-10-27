# 20. Guess the Number

**Spanish version:** [20 - Adivina el Número.md](./20%20-%20Adivina%20el%20N%C3%BAmero.md)

**Course:** C++
**Topic:** `while` Loops
**Tags:** `#cpp` `#loops` `#while` `#iteration`

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

A `while` loop looks very similar to an `if` statement. Like an `if`, it executes its code when
the condition is `true`. The difference: the `while` loop runs the code *over and over again* for
as long as the condition stays `true`.

Instead of executing once if a condition is true, it executes again and again while that
condition is true.

At the beginning of each pass, the condition is re-checked. The moment it becomes `false`, the
program exits the loop and continues from the line after it.

> [!NOTE]
> If the condition was `false` from the start, the code block never runs at all — the loop is
> skipped entirely. A `while` can execute **zero** times; that is by design.

## Example

```cpp
#include <iostream>

int main() {
  int guess = 0;
  int answer = 64;

  std::cout << "Guess the number: ";
  std::cin >> guess;

  while (guess != answer) {
    std::cout << "Guess the number: ";
    std::cin >> guess;
  }

  std::cout << "You guessed it correct!\n";
}
```

The first guess is read before the loop so the condition has something to test. Every failed
attempt re-reads inside the loop — that re-read is what eventually makes `guess != answer` false.

> [!TIP]
> **The loop always ends. Eventually.**
> The only way out is a correct guess. In a real game you would add an attempt counter and a
> `break`, which arrives in the next chapters.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
