# 18. Trivia Quiz

**Spanish version:** [18 - Trivial Quiz.md](./18%20-%20Trivial%20Quiz.md)

**Course:** C++
**Topic:** Chapter 3 Recap & Quiz Project
**Tags:** `#cpp` `#recap` `#project` `#control-flow`

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

## Chapter 3 Recap

- **Control flow** is the order in which the program's code executes.
- **`if`** tests a condition for truth and runs its block when `true`.
- **`else if`** can be added between `if` and `else` to check further conditions.
- **`else`** runs when none of the above matched.
- **Relational operators** compare two values: `==`, `!=`, `>`, `>=`, `<`, `<=`.
- **Logical operators** combine conditions: `&&`, `||`, `!`.

## Project: Trivia Quiz

```cpp
#include <iostream>
#include <string>

int main() {
  int score = 0;
  int ans1, ans2;
  std::string ans3;

  // Q1
  std::cout << "Q1) What is the name of the world's longest river? 💧\n";
  std::cout << "1) Missouri River\n";
  std::cout << "2) Nile\n";
  std::cout << "3) Amazon River\n";
  std::cout << "4) Yangtze River\n\n";
  std::cin >> ans1;

  if (ans1 == 2) {
    score++;
  }

  // Q2
  std::cout << "\nQ2) How many bones are in the human body? 🦴\n";
  std::cout << "1) 92\n";
  std::cout << "2) 150\n";
  std::cout << "3) 206\n";
  std::cout << "4) 10\n\n";
  std::cin >> ans2;

  if (ans2 == 3) {
    score++;
  }

  // Q3 (free text)
  std::cout << "\nQ3) What food never spoils? 🍯\n";
  std::cout << "Type your answer: ";
  std::cin >> ans3;

  if (ans3 == "Honey" || ans3 == "honey") {
    score++;
  }

  std::cout << "\nYour final score is: " << score << "/3\n";
}
```

> [!NOTE]
> **`score++` is `score = score + 1`**
> The increment operator adds one and stores the result back. Its mirror, `score--`, subtracts
> one. Both return to center stage in [[21 - Counting Sheep]].

> [!TIP]
> Free-text answers are fragile — `std::cin >> ans3` stops at the first space, so "honey bee"
> only ever compares "honey". Normalize input (lowercase it) before comparing.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
