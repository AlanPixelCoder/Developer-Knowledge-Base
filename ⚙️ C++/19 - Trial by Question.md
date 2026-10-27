# 19. Trial by Question

**Spanish version:** [19 - Prueba de Preguntas](./19%20-%20Prueba%20de%20Preguntas.md)

**Course:** C++
**Chapter:** 3 — Decisions
**Topic:** Chapter 3 recap: a scored quiz built from branches
**Tags:** `#cpp` `#recap` `#control-flow`

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

The engine's tutorial ends with three questions. Correct answers add a point, and the pass mark is
two out of three — a whole program made of the branches from this chapter.

```cpp
#include <iostream>

int main() {
  const int ANSWER_1 = 3;
  const int ANSWER_2 = 1;
  const int ANSWER_3 = 4;

  int given_1 = 3;
  int given_2 = 2;
  int given_3 = 4;

  int score = 0;

  if (given_1 == ANSWER_1) score++;
  if (given_2 == ANSWER_2) score++;
  if (given_3 == ANSWER_3) score++;

  std::cout << "score: " << score << "/3\n";

  if (score == 3) {
    std::cout << "rank: archivist\n";
  } else if (score == 2) {
    std::cout << "rank: apprentice\n";
  } else {
    std::cout << "rank: visitor\n";
  }

  std::cout << "percentage: " << 100.0 * score / 3 << "%\n";
}
```

## Output

```text
score: 2/3
rank: apprentice
percentage: 66.6667%
```

## Three separate `if`s, on purpose

| Written | Behaviour |
| :--- | :--- |
| Three `if` statements | Each question is checked independently |
| One `else if` chain | Only the first correct answer would score |

The chain from [[16 - Tiers and Thresholds]] is right for exclusive tiers and wrong for a tally.

> [!NOTE]
> In the real tutorial the three `given_` values come from `std::cin`. Hard-coding them keeps this
> example runnable without typing at the keyboard, and nothing else about the logic changes.

> [!TIP]
> `100.0 * score / 3` keeps the fraction; `100 * score / 3` would print `66` for the same score.
> The `3` matches the number of questions — a named constant there saves you from a wrong mark when
> a fourth question is added.

---

**Next:** [[20 - The Loop That Waits]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
