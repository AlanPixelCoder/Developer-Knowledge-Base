# 24. Survival Gear

**Spanish version:** [24 - Equipo de Supervivencia.md](./24%20-%20Equipo%20de%20Supervivencia.md)

**Course:** C++
**Topic:** Vectors
**Tags:** `#cpp` `#vectors` `#data-structures`

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

**Vectors** store multiple items in a single variable. This is a neat way to store a bunch of data
values instead of creating a pile of separate variables, which is tedious and error-prone.

`std::vector` lives in the `<vector>` header, so add `#include <vector>` at the top of the program.

## Creating a Vector

- The `std::vector` keyword, then the element type in angle brackets `< >`.
- Then the vector's name.
- Elements go inside curly braces, separated by commas.

```cpp
std::vector<type> name = {1, 2, 3, 4};
```

## Facts about vectors

| Property | Detail |
| :--- | :--- |
| Duplicates | Allowed — the same value can appear many times |
| Element types | All elements share **one** data type |
| Size | Can grow and shrink at runtime |

> [!NOTE]
> **Why vectors replaced arrays**
> People used to use "arrays" from the C language. Arrays are **fixed** in size — decided once,
> forever. Vectors grow and shrink on demand, which matches how inventories actually behave.
> The full comparison lives in [[Arrays]].

## Example

```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
  std::vector<std::string> survival_gear = {
    "Heavy winter coat",
    "Wood-splitting axe",
    "Flint and steel",
    "Water purifier",
    "Solar generator",
    "Laptop",
    "Blender",
    "Jasmine rice",
    "Health potions",
    "Broadsword"
  };
}
```

> [!TIP]
> Angle brackets can nest. A vector of vectors — an inventory with bag slots — is written
> `std::vector<std::vector<std::string>>`. In C++11 and later the closing `>>` is fine; older
> compilers demanded a space between them.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
