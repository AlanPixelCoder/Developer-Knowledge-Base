# C++ Cheatsheet

**Spanish version:** [00b - Chuleta de C++.md](./00b%20-%20Chuleta%20de%20C%2B%2B.md)

**Course:** C++
**Topic:** Quick Reference
**Tags:** `#cpp` `#cheatsheet` `#reference`

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

> [!TIP]
> Keep this open while grinding through the terminal. Faster lookup, less tab-hopping, more
> dungeon-clearing.

## I/O

```cpp
#include <iostream>

std::cout << "Hello!";       // output
std::cin >> variable;        // input
std::cout << "Value: " << x; // chaining
```

## Data types

| Type | Use | Example |
| :--- | :--- | :--- |
| `int` | Whole numbers | `int hp = 100;` |
| `double` | Decimals | `double gold = 24.99;` |
| `char` | One character | `char rank = 'S';` |
| `std::string` | Text | `std::string name = "Knight";` |
| `bool` | True / False | `bool alive = true;` |

## Operators

| Operator | Purpose |
| :--- | :--- |
| `+ - * / %` | Arithmetic (`%` = remainder) |
| `== != > < >= <=` | Relational |
| `&&` `\|\|` `!` | Logical (and, or, not) |
| `=` | Assignment |

## Control flow

```cpp
if (condition) { /* ... */ }
else if (condition) { /* ... */ }
else { /* ... */ }
```

## Loops

```cpp
while (condition) { /* ... */ }

for (int i = 0; i < n; i++) { /* ... */ }
```

## Vectors

```cpp
#include <vector>

std::vector<std::string> inv = {"Potion", "Map"};
inv.push_back("Sword");
inv.pop_back();
inv.size();
inv[0]; // access
```

## Functions

```cpp
void greet() { std::cout << "Hello\n"; }

int add(int x, int y) { return x + y; }

greet();
int total = add(2, 3);
```

## Classes

```cpp
class Hero {
  public:
    std::string name;
    int hp;

    Hero(std::string n, int h) {
      name = n;
      hp = h;
    }

    void heal() { hp += 10; }
};

Hero knight("Aldric", 100);
knight.heal();
```

## Pointers & references

```cpp
int x = 10;
int* p = &x;      // pointer to address
std::cout << *p;  // dereference

int& ref = x;     // reference (alias)
ref = 20;         // changes x

int* nullp = nullptr;
```

## Compile & run

```bash
g++ main.cpp -o main
./main
```

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
