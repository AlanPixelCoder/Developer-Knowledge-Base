# 33. Filling the Slots

**Spanish version:** [33 - Llenar las Ranuras](./33%20-%20Llenar%20las%20Ranuras.md)

**Course:** C++
**Chapter:** 6 — Functions
**Topic:** Default arguments and overloads with different arities
**Tags:** `#cpp` `#functions` `#default-arguments`

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

Most potions are brewed with water and one herb. Some add a catalyst. Some add two. Rather than three
functions with near-identical names, the slots get defaults.

```cpp
#include <iostream>
#include <string>

std::string brew(const std::string& herb,
                 const std::string& base = "water",
                 int potency = 1) {
  return herb + " in " + base + " x" + std::to_string(potency);
}

int main() {
  std::cout << brew("emberroot") << "\n";
  std::cout << brew("emberroot", "oil") << "\n";
  std::cout << brew("emberroot", "oil", 3) << "\n";
}
```

## Output

```text
emberroot in water x1
emberroot in oil x1
emberroot in oil x3
```

## How defaults are chosen

The caller supplies arguments **left to right**. Any parameter without an argument must have a
default, and defaults must be the trailing ones:

| Call | herb | base | potency |
| :--- | :--- | :--- | :--- |
| `brew("emberroot")` | emberroot | water | 1 |
| `brew("emberroot", "oil")` | emberroot | oil | 1 |
| `brew("emberroot", "oil", 3)` | emberroot | oil | 3 |

You cannot skip `base` and pass only `potency`. That is why the most-likely-to-change parameter goes
last.

## Defaults live in the declaration

If the function is declared and defined separately, the default belongs in the declaration — the
header, where callers can see it. Repeating it in the definition is a redefinition error.

> [!WARNING]
> Default arguments are evaluated at the call site, not at definition. A default of `time(nullptr)`
> or `rand()` is computed on every call; a default that names a global may surprise you when that
> global changes.

> [!TIP]
> Overloading and defaults solve the same problem two ways. Defaults keep one implementation; a
> second overload keeps two. Prefer defaults when the extra parameters only tune the same algorithm.

---

**Next:** [[34 - Handing Back the Loot]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
