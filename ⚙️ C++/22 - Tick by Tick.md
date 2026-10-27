# 22. Tick by Tick

**Spanish version:** [22 - Tic a Tic](./22%20-%20Tic%20a%20Tic.md)

**Course:** C++
**Chapter:** 4 — Iteration
**Topic:** The for loop: start, stop, step
**Tags:** `#cpp` `#for` `#loops`

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

The engine simulation runs in fixed ticks. Sixty per second, and each tick has a number — that is a
`for` loop with three facts in one line.

```cpp
#include <iostream>

int main() {
  const int TICKS = 5;

  for (int tick = 1; tick <= TICKS; tick++) {
    std::cout << "tick " << tick << " of " << TICKS << "\n";
  }

  std::cout << "simulation stopped\n";
}
```

## Output

```text
tick 1 of 5
tick 2 of 5
tick 3 of 5
tick 4 of 5
tick 5 of 5
simulation stopped
```

## The three clauses

| Clause | Here | Runs |
| :--- | :--- | :--- |
| Initialisation | `int tick = 1` | Once, before the loop |
| Condition | `tick <= TICKS` | Before every pass |
| Increment | `tick++` | After every pass |

Read it as: *start at 1, keep going while at most 5, add one each time.*

## `<=` versus `<`

Both are correct, with different counters:

| Written | Passes | Last value |
| :--- | :--- | :--- |
| `tick = 1; tick <= 5` | 5 | 5 |
| `tick = 0; tick < 5` | 5 | 4 |

Pick one and stay consistent. The second form is what you will use to index a vector, because
container indices start at zero.

> [!CAUTION]
> `tick <= TICKS` with `tick` starting at `0` runs **six** times. The loop is not wrong; the pair
> (start, comparison) is. Print the counter on the first and last pass whenever the count matters.

> [!TIP]
> A `for` loop is a `while` with the boilerplate moved into the header. If a loop needs the counter
> after it finishes, declare `tick` outside the header — inside, it is gone at the closing brace.

---

**Next:** [[23 - Countdown Protocol]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
