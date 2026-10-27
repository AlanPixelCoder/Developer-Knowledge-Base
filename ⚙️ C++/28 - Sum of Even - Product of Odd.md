# 28. Sum of Even / Product of Odd

**Spanish version:** [28 - Suma de Pares - Producto de Impares.md](./28%20-%20Suma%20de%20Pares%20-%20Producto%20de%20Impares.md)

**Course:** C++
**Topic:** Chapter 5 Recap & Logic Problem
**Tags:** `#cpp` `#recap` `#vectors` `#logic` `#loops`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

## Chapter 5 Recap

- Vectors store multiple items of the same data type in a single variable.
- An index is an element's position in a vector.
- C++ vectors are 0-indexed.
- Vectors have methods: `.push_back()`, `.pop_back()`, `.size()`.
- We iterate over a vector with a `for` loop and `.size()` as the bound.

## Logic Problem

Write a program that uses a `for` loop to walk a vector of numbers and compute the **sum of the
even** numbers and the **product of the odd** numbers.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> num = {2, 4, 3, 6, 1, 9, 8, 0, 8, 5, 7, 3, 3};

  int sum_even = 0;
  int product_odd = 1;

  for (int i = 0; i < num.size(); i++) {
    if (num[i] % 2 == 0) {
      sum_even += num[i];
    } else {
      product_odd *= num[i];
    }
  }

  std::cout << "The sum of even numbers: " << sum_even << "\n";
  std::cout << "The product of odd numbers: " << product_odd << "\n";
}
```

> [!IMPORTANT]
> **The identity values matter**
> A sum starts at `0` (adding nothing changes nothing). A product starts at `1` (multiplying by
> one changes nothing). Starting `product_odd` at `0` would annihilate every result into `0`.

> [!TIP]
> `sum_even += num[i]` is shorthand for `sum_even = sum_even + num[i]`. The `*=`, `-=` and `/=`
> operators work exactly the same way.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
