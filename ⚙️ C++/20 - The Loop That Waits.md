# 20. The Loop That Waits

**Spanish version:** [20 - El Bucle que Espera](./20%20-%20El%20Bucle%20que%20Espera.md)

**Course:** C++
**Chapter:** 4 — Iteration
**Topic:** What iteration is, and the four parts of a loop that ends
**Tags:** `#cpp` `#loops` `#do-while`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The engine asks for a four-digit unlock code. The player gets three attempts, and each wrong code
has to bring the program back to the prompt — that "back to the prompt" is iteration.

```cpp
#include <iostream>

int main() {
  const int UNLOCK_CODE = 4821;
  int attempts = 0;
  int guess = 0;

  do {
    attempts++;
    guess = UNLOCK_CODE + (attempts == 2 ? -111 : 0);  // simulated input
    std::cout << "attempt " << attempts << ": " << guess << "\n";
  } while (guess != UNLOCK_CODE && attempts < 3);

  if (guess == UNLOCK_CODE) {
    std::cout << "console unlocked after " << attempts << " attempts\n";
  } else {
    std::cout << "console locked out\n";
  }
}
```

## Output

```text
attempt 1: 4821
console unlocked after 1 attempts
```

## The four parts

| Part | In this program | Missing it means |
| :--- | :--- | :--- |
| Starting state | `attempts = 0` | The counter starts as garbage |
| Condition | `guess != UNLOCK_CODE && attempts < 3` | The loop never stops |
| Body | ask, compare, print | Nothing useful happens |
| Change | `attempts++` | The condition never becomes false |

## `do` runs at least once

A `while` checks first and may run zero times. A `do ... while` runs the body, then checks. Prompts
want the second: you always show the prompt before you can be told the answer is wrong.

> [!CAUTION]
> Every loop needs a path to a false condition. If the change step is inside an `if` that never
> fires, the loop runs forever and the only symptom is a program that never prints again.

> [!TIP]
> Trace the first two iterations on paper before running the program. Loops are easy to write and
> hard to read back; two lines of trace catch most off-by-one mistakes.

---

**Next:** [[21 - Holding Patterns]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
