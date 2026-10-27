# 29. The Alchemist's Tally

**Spanish version:** [29 - El Cómputo del Alquimista](./29%20-%20El%20C%C3%B3mputo%20del%20Alquimista.md)

**Course:** C++
**Chapter:** 5 — Collections
**Topic:** Accumulators: sum, count, max, and average over a collection
**Tags:** `#cpp` `#vector` `#accumulator`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

The alchemist wants one number per question: how many, how much, which one is biggest, what is the
average. All four are the same loop with a different starting value and a different update.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> batches{12, 7, 25, 4, 18};

  int count = 0;
  int sum = 0;
  int best = batches[0];

  for (int n : batches) {
    count++;
    sum += n;
    if (n > best) {
      best = n;
    }
  }

  std::cout << "batches: " << count << "\n";
  std::cout << "total:   " << sum << "\n";
  std::cout << "best:    " << best << "\n";
  std::cout << "average: " << static_cast<double>(sum) / count << "\n";
}
```

## Output

```text
batches: 5
total:   66
best:    25
average: 13.2
```

## Four shapes, one loop

| Goal | Start | Update |
| :--- | :--- | :--- |
| Count | `0` | `count++` |
| Sum | `0` | `sum += n` |
| Maximum | first element | `if (n > best) best = n` |
| Average | sum and count | divide at the end |

Starting `best` at `0` is a classic bug: with an all-negative collection the answer is wrong. Starting
at `batches[0]` is correct for any non-empty collection.

## The integer division trap

`sum / count` with two `int`s truncates. `66 / 5` is `13`, not `13.2`. Casting one side to `double`
switch the whole expression to floating point.

> [!WARNING]
> `static_cast<double>(sum / count)` casts the *quotient*, which is already `13`. The cast must wrap
> `sum` alone, or better, the whole thing must be written as
> `static_cast<double>(sum) / static_cast<double>(count)`.

> [!TIP]
> `std::accumulate` from `<numeric>` does the sum in one call, and `std::max_element` from
> `<algorithm>` finds the maximum. Learn the loops first; they are what the algorithms compile to.

---

**Next:** [[30 - Stone Racks and Satchels]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
