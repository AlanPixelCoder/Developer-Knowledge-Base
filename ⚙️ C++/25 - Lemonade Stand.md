# 25. Lemonade Stand

**Spanish version:** [25 - Puesto de Limonada.md](./25%20-%20Puesto%20de%20Limonada.md)

**Course:** C++
**Topic:** Vector Index
**Tags:** `#cpp` `#vectors` `#index`

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

Vector elements are changeable, meaning we can update individual elements. But first we need to
know how to **access** an individual element.

This is where the **index** comes in: an index is an element's position in a vector.

C++ is **0-indexed**, meaning indices start at `0`:

- Index `0` is the first item.
- Index `1` is the second item, and so on.
- The last index is always `size() - 1`.

Access an element with the `name[index]` syntax.

```cpp
std::vector<int> lemonade = {25, 28, 40, 85, 76};
std::cout << lemonade[0]; // 25
std::cout << lemonade[4]; // 76 — the last element
```

## Example

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> lemonade = {25, 28, 40, 85, 76};
  std::vector<double> sales = {75.50, 89.25, 60.00, 102.45, 95.10};

  std::cout << "Lemons used on the last day: " << lemonade[4] << "\n";
  std::cout << "Sales on the last day: $" << sales[4] << "\n";

  double profit_per_lemonade = sales[4] / lemonade[4];
  std::cout << "Profit per lemonade: $" << profit_per_lemonade << "\n";

  // Out of bounds — reads memory that isn't ours. Undefined behavior:
  // std::cout << lemonade[9] << "\n";
}
```

> [!CAUTION]
> **Out-of-bounds is not an error you get told about**
> `lemonade[9]` on a 5-element vector does not throw. It reads whatever happens to live at that
> offset — garbage, or someone else's data. In C++, this is *undefined behavior*: the compiler
> owes you nothing. Guard the index, or use `.at()` if you want a real exception.

> [!TIP]
> The last element is always `v[v.size() - 1]`. Memorize that spelling; it appears constantly.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
