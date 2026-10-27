# 32. The Tavern Board

**Spanish version:** [32 - El Tablón de la Taberna](./32%20-%20El%20Tabl%C3%B3n%20de%20la%20Taberna.md)

**Course:** C++
**Chapter:** 6 — Functions
**Topic:** Parameters versus arguments, and returning a computed value
**Tags:** `#cpp` `#functions` `#return`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

A board outside the tavern lists bounty prices: so much per wolf pelt, a bonus for a clean kill, a
penalty for damaged goods. The price depends on the inputs, and the board never changes.

```cpp
#include <iostream>

double bounty(int pelts, bool clean, int damaged) {
  double total = pelts * 12.5;
  if (clean) {
    total += 20.0;
  }
  total -= damaged * 4.0;
  return total;
}

int main() {
  std::cout << bounty(3, true, 0) << "\n";
  std::cout << bounty(3, false, 1) << "\n";
  std::cout << bounty(0, true, 0) << "\n";
}
```

## Output

```text
57.5
33.5
20
```

## Parameter and argument

| Word | Where it lives | Example |
| :--- | :--- | :--- |
| Parameter | in the definition | `int pelts` |
| Argument | in the call | `3` |

The parameter is a local variable created fresh for each call. Assigning to it inside the function
never touches the caller's variable.

## Return ends the call

`return` sends the value back and stops. Nothing after it in that call runs.

```cpp
if (pelts < 0) {
  return 0.0;   // early exit: the rest of the body is skipped
}
```

An early return for an impossible case keeps the main path flat, which is easier to read than a nest
of `if`s.

> [!IMPORTANT]
> A function with a non-`void` return type must return on every path. Falling off the end is
> undefined behaviour, and g++ only warns when the missing path is obvious.

> [!TIP]
> Note that `bounty(0, true, 0)` returns `20`, not `0`: the clean-kill bonus applies before any pelts
> are counted. If a zero hunt should pay nothing, guard first and keep the rule visible.

---

**Next:** [[33 - Filling the Slots]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
