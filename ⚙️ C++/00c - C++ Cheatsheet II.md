# C++ Cheatsheet II

**Spanish version:** [00c - Chuleta de C++ II.md](./00c%20-%20Chuleta%20de%20C%2B%2B%20II.md)

**Course:** C++
**Topic:** Advanced Quick Reference
**Tags:** `#cpp` `#cheatsheet` `#reference` `#memory`

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

## Scope

| Scope | Where | Accessible |
| :--- | :--- | :--- |
| **Local** | Inside a function or block `{}` | Only within it |
| **Global** | Outside all functions | Anywhere in the file |

## Access modifiers

| Modifier | Access |
| :--- | :--- |
| `public` | Anyone |
| `private` | Only the class itself (default for `class`) |
| `protected` | The class and its derived classes |

## Constructors

```cpp
class Car {
  public:
    std::string brand;
    Car(std::string b) { brand = b; } // constructor
};

Car c("Ford"); // initialized in one line
```

## Pass-by-value vs pass-by-reference

```cpp
// Pass-by-value (copy)
void damage(int hp) { hp -= 10; }     // original unchanged

// Pass-by-reference (alias)
void damageRef(int& hp) { hp -= 10; } // original changed
```

## Pointers vs references

| Feature | Pointer | Reference |
| :--- | :--- | :--- |
| Syntax | `int* p = &x;` | `int& ref = x;` |
| Can be null | Yes (`nullptr`) | No |
| Reassignable | Yes | No |
| Dereference | `*p` required | Use the name directly |
| Initialization | Optional | Required |

## `nullptr` safety

```cpp
void greet(const std::string* name) {
  if (name != nullptr) {
    std::cout << *name;
  } else {
    std::cout << "Guest";
  }
}
```

## Common headers

| Header | Purpose |
| :--- | :--- |
| `<iostream>` | I/O (`std::cout`, `std::cin`) |
| `<string>` | `std::string` |
| `<vector>` | `std::vector` |
| `<cstdlib>` | `std::rand()` |
| `<ctime>` | `time(NULL)`, `srand()` |

## Habits worth keeping

- Always initialize a pointer — to a real address or to `nullptr`.
- Prefer references for parameters when the function should modify the original.
- Mark pointers and references `const` when you only read through them.
- Compile with `g++ -Wall -Wextra -std=c++17 main.cpp -o main`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
