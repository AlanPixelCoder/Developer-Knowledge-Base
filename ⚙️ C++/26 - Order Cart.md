# 26. Order Cart

**Spanish version:** [26 - Carrito de Compras.md](./26%20-%20Carrito%20de%20Compras.md)

**Course:** C++
**Topic:** Vector Methods (`push_back`, `pop_back`, `size`)
**Tags:** `#cpp` `#vectors` `#methods`

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

Vectors come with built-in functions that act as ready-to-use tools.

## Adding and Removing Elements

| Method | Effect |
| :--- | :--- |
| `.push_back(x)` | Adds `x` at the **end** of the vector |
| `.pop_back()` | Removes the element at the **end** |
| `.size()` | Returns the number of elements |

```cpp
std::vector<std::string> dna = {"AUG", "AUC", "UCG"};

dna.push_back("UAA"); // {"AUG", "AUC", "UCG", "UAA"}
dna.pop_back();       // {"AUG", "AUC", "UCG"}
```

## Size

`.size()` returns the number of elements in the vector. With dozens of elements it becomes
invaluable — and it is the canonical loop bound.

```cpp
std::cout << dna.size() << "\n"; // Output: 3
```

## Full Example

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> cart = {
    "🍕 Pepperoni pizza",
    "🥗 Garden salad",
    "🥤 Diet Coke"
  };

  cart.push_back("🥫 Marinara sauce");
  cart.pop_back();

  std::cout << cart[0] << " ";
  std::cout << cart[1] << " ";
  std::cout << cart[2] << "\n";

  std::cout << cart.size() << "\n";
}
```

> [!WARNING]
> **`pop_back()` on an empty vector** is undefined behavior — there is nothing to remove. Check
> `!cart.empty()` first. Like out-of-bounds indexing, it will not warn you.

> [!TIP]
> `.empty()` is the idiomatic emptiness check (`size() == 0` works too, but says less).

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
