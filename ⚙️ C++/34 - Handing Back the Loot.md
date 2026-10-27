# 34. Handing Back the Loot

**Spanish version:** [34 - Devolver el Botín](./34%20-%20Devolver%20el%20Bot%C3%ADn.md)

**Course:** C++
**Chapter:** 6 — Functions
**Topic:** Return types: void, value, reference, and returning several things
**Tags:** `#cpp` `#functions` `#struct`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Some functions answer a question, some change the world and answer nothing, and some must hand back
two numbers at once. C++ has one keyword for all three, and the type decides the rest.

```cpp
#include <iostream>
#include <string>

struct Loot {
  std::string name;
  int value;
};

Loot best_of(const Loot& a, const Loot& b) {
  return a.value >= b.value ? a : b;
}

void announce(const Loot& item) {
  std::cout << "found " << item.name << " worth " << item.value << "\n";
}

int main() {
  Loot coin{"rusted coin", 3};
  Loot ring{"silver ring", 40};

  announce(best_of(coin, ring));
}
```

## Output

```text
found silver ring worth 40
```

## Two shapes of return

| Shape | Signature | Meaning |
| :--- | :--- | :--- |
| Answer a question | `int damage(...)` | caller needs the value |
| Change the world | `void announce(...)` | caller needs the effect |
| Answer with structure | `Loot best_of(...)` | several values travel together |

A `struct` is the cheapest way to return more than one value. Two related fields with names beat an
`std::pair` whose members are called `first` and `second`.

## Returning a reference

A function may return a reference when the caller should see the original object, not a copy:

```cpp
const Loot& heaviest(const std::vector<Loot>& items);
```

That is safe only if the object outlives the call. Never return a reference to a local: the local is
destroyed at the closing brace and the caller holds a dangling reference.

> [!CAUTION]
> `Loot& best_of(...)` returning a parameter by value is the classic dangling case. Return by value
> for new objects, by reference only for objects the caller already owns.

> [!TIP]
> Compilers elide the copy when you return a local by value, so `return a;` is not slower than
> returning a pointer. Do not contort the design to "avoid a copy" before measuring.

---

**Next:** [[35 - Chained Returns]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
