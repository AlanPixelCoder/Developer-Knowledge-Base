# 14. Forked Roads

**Spanish version:** [14 - Caminos Bifurcados](./14%20-%20Caminos%20Bifurcados.md)

**Course:** C++
**Chapter:** 3 — Decisions
**Topic:** Control flow, and why a random roll must be seeded
**Tags:** `#cpp` `#control-flow` `#random`

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

Until now every program ran the same lines in the same order. Control flow changes that: the script
has forks, and the program walks one of them.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int roll = std::rand() % 6 + 1;   // 1 through 6

  if (roll >= 5) {
    std::cout << "critical hit: " << roll << "\n";
  } else if (roll >= 3) {
    std::cout << "solid hit: " << roll << "\n";
  } else {
    std::cout << "glancing blow: " << roll << "\n";
  }
}
```

Three possible lines of output, one per branch, decided at runtime.

## `srand` is not optional

`std::rand()` is a **sequence generator**, not a source of chaos. Without a seed it replays the same
sequence every run — the same dice, every launch, forever. `srand(time(NULL))` feeds it the clock so
each session starts somewhere else.

| Call | Effect |
| :--- | :--- |
| `std::rand()` | Next number in the current sequence |
| `srand(seed)` | Restart the sequence from that seed |
| `srand(time(NULL))` | Restart from the current second |

> [!CAUTION]
> Seeding with `time(NULL)` means two runs **inside the same second** get identical sequences. That
> is correct behaviour, not a bug — but it is why a test that runs twice in a loop looks rigged.

> [!NOTE]
> `rand()` and `srand()` come from C. Modern C++ has `<random>` with `std::mt19937` and proper
> distributions; see [[17 - Loaded Dice]] for the difference in quality, and use `<random>` the day
> the dice start driving something that matters.

---

**Next:** [[15 - Doors and Keys]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
