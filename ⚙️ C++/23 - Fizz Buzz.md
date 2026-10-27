# 23. Fizz Buzz

**Spanish version:** [23 - Fizz Buzz (Reto).md](./23%20-%20Fizz%20Buzz%20%28Reto%29.md)

**Course:** C++
**Topic:** Chapter 4 Recap & Fizz Buzz Challenge
**Tags:** `#cpp` `#recap` `#loops` `#challenge`

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

## Chapter 4 Recap

- The `while` loop iterates over and over while the condition is `true`.
- The `for` loop iterates a certain number of times.
- `i++` increments, `i--` decrements.
- Both loops can run zero times if the condition starts out `false`.

## Fizz Buzz

Fizz Buzz is a children's word game that teaches division — and a classic technical interview
question.

The rules:

- Output numbers from 1 to 100.
- For multiples of 3, print `Fizz` instead of the number.
- For multiples of 5, print `Buzz` instead of the number.
- For multiples of **both** 3 and 5, print `FizzBuzz`.

## Example

```cpp
#include <iostream>

int main() {
  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      std::cout << "FizzBuzz\n";
    } else if (i % 3 == 0) {
      std::cout << "Fizz\n";
    } else if (i % 5 == 0) {
      std::cout << "Buzz\n";
    } else {
      std::cout << i << "\n";
    }
  }
}
```

> [!IMPORTANT]
> **Order is the whole trick**
> The combined `i % 15 == 0` case must be checked **first**. If `i % 3` came first, 15 would print
> `Fizz` and never reach `FizzBuzz`. Because `else if` stops at the first match, specificity must
> come before generality — the same lesson as [[15 - Levels & Ranks]].

> [!TIP]
> `%` is the whole engine here: a number is divisible by `n` exactly when `x % n == 0`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
