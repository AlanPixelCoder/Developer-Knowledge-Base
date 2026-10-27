# 43. References vs. Pointers

**Spanish version:** [43 - Referencias vs Punteros.md](./43%20-%20Referencias%20vs%20Punteros.md)

**Course:** C++
**Topic:** References and Pass-By-Reference
**Tags:** `#cpp` `#pointers` `#references` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-ADVANCED-E74C3C?style=for-the-badge" alt="Advanced">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

While pointers have existed since C (and early C++), **references** were introduced in C++ later
— mainly to make function parameter passing and aliasing easier. A reference is a safer, more
convenient alternative to a pointer when you don't need pointer arithmetic or to reassign the
address.

Unlike pointers, references:

- must be **initialized** when declared,
- cannot be **null** (you can't nickname yourself if you don't exist),
- cannot be **reassigned** to alias another variable.

```cpp
// Reference
int value = 42;
int& reference = value;

// Pointer
int x = 10;
int* p = &x;
```

> [!NOTE]
> Here `&` means **reference type**, not "address-of". Context decides: `int& r = value;` declares
> a reference; `&value` takes an address.

## Comparison

| Feature | Pointer | Reference |
| :--- | :--- | :--- |
| Syntax | `int* p = &x;` | `int& r = x;` |
| Can be null | Yes (`nullptr`) | No |
| Reassignable | Yes | No |
| Needs dereference | Yes (`*p`) | No — it *is* the variable |
| Arithmetic | Yes | No |
| Initialization | Optional | Required |

## Pass-by-value vs pass-by-reference

- **Pass-by-value** — the function gets a **copy**. Changes inside don't touch the original.
- **Pass-by-reference** — the function gets an **alias**. Changes inside *do* affect the original.

```cpp
#include <iostream>

// int& passes health by reference
void healPlayer(int& health) {
  health += 20;
}

int main() {
  int playerHealth = 50;

  healPlayer(playerHealth); // permanently alters playerHealth

  std::cout << playerHealth << "\n"; // 70
}
```

> [!IMPORTANT]
> **The classic exam question**
> Remove the `&` and `playerHealth` stays `50` — the function healed a copy. The `&` is the entire
> difference between "heal the hero" and "heal a hologram".

> [!TIP]
> Prefer references for parameters; reach for pointers only when "no object" is a legitimate state
> (`nullptr`) or when you need to re-point.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
