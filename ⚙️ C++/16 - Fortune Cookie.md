# 16. Fortune Cookie

**Spanish version:** [16 - Galleta de la Fortuna.md](./16%20-%20Galleta%20de%20la%20Fortuna.md)

**Course:** C++
**Topic:** Random Numbers
**Tags:** `#cpp` `#random` `#cstdlib`

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

Sometimes we need a random value to make results more interesting.

C++ has a `std::rand()` function (short for **rand**om) from `<cstdlib>` that generates a
pseudo-random number. You must `#include <cstdlib>` to use it.

To limit the number to a specific range, use the `%` modulo operator (which returns the
remainder). For example, `std::rand() % 10` limits the result to **0–9**.

## Seeding

To make sure every run gives a different sequence, **seed** the generator before declaring the
variable:

```cpp
srand(time(NULL));
```

This requires `#include <ctime>`. `time(NULL)` returns the current time in seconds, so each run
gets a new starting point.

## Example

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int fortune = std::rand() % 6;

  std::cout << "🥠 ";

  if (fortune == 0) {
    std::cout << "Don't pursue happiness - create it.\n";
  } else if (fortune == 1) {
    std::cout << "All things are difficult before they are easy.\n";
  } else if (fortune == 2) {
    std::cout << "The early bird gets the worm, but the second mouse gets the cheese.\n";
  } else if (fortune == 3) {
    std::cout << "Someone in your life needs a letter from you.\n";
  } else if (fortune == 4) {
    std::cout << "The fortune you search for is in another cookie.\n";
  } else {
    std::cout << "Help! I'm being held prisoner in a Chinese bakery!\n";
  }

  // Bonus: six lucky numbers between 0 and 50
  std::cout << "\nLucky numbers: "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << "\n";
}
```

> [!NOTE]
> **`rand()` is a teaching tool, not a game-grade RNG**
> Call `srand()` **once**, at the top of `main()`. Calling it before every `rand()` reseeds with
> the same second and hands you the same number twice. Modern C++ offers `<random>`
> (`std::mt19937`) when distribution quality actually matters — more on that later.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
