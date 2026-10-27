# Field Manual II

**Spanish version:** [00c - Manual de Campo II](./00c%20-%20Manual%20de%20Campo%20II.md)

**Course:** C++
**Topic:** Quick reference
**Tags:** `#cpp` `#cheatsheet` `#reference`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Reference-Field%20Manual-7C5CFF?style=for-the-badge" alt="Field Manual">
  <img src="https://img.shields.io/badge/Status-Complete-00C2A8?style=for-the-badge" alt="Complete">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

<p align="center">
  <sub>5–8 · Collections to Memory</sub>
</p>

> [!TIP]
> Everything in chapters 5 to 8: containers, functions, types you define, and where values actually
> live. The page you want open while writing the spawner.

## Containers

```cpp
#include <vector>

std::vector<int> stacks{2, 5, 1};   // from a list
std::vector<int> empty;             // grows later
std::vector<int> zeros(4);          // four zeroes
```

| Call | Effect |
| :--- | :--- |
| `v.push_back(x)` | append, size + 1 |
| `v.pop_back()` | remove last, size − 1 |
| `v[i]` | element i, **unchecked** |
| `v.at(i)` | element i, throws if out of range |
| `v.size()` | number of elements |
| `v.empty()` | `size() == 0` |
| `v.front()` / `v.back()` | first / last element |
| `v.clear()` | remove all |

| Loop | Gives you |
| :--- | :--- |
| `for (auto& x : v)` | each element, modifiable |
| `for (const auto& x : v)` | each element, read-only, no copy |
| `for (std::size_t i = 0; i < v.size(); i++)` | the index too |

## Functions

```cpp
int damage(int power, int armor = 0);          // declaration with a default
int damage(int power, int armor) { return power * 2 - armor; }  // definition
```

| Parameter form | Copies | Caller sees change |
| :--- | :--- | :--- |
| `int x` | yes | no |
| `const std::string& s` | no | no |
| `std::vector<int>& v` | no | yes |
| `Entity* e` | pointer only | yes, if dereferenced |

## Types you define

```cpp
class Entity {
 public:
  Entity(std::string name, int hp) : name_(std::move(name)), hp_(hp) {}

  void hit(int amount) { hp_ -= amount; }
  bool alive() const { return hp_ > 0; }

 private:
  std::string name_;
  int hp_;
};
```

| Keyword | Meaning |
| :--- | :--- |
| `public:` | usable by any code with the object |
| `private:` | usable only inside the class |
| `const` after a method | promises not to modify the object |
| `static` member | one copy shared by the class |
| `this` | pointer to the object being used |

## Files

| File | Holds | Included by |
| :--- | :--- | :--- |
| `entity.hpp` | class shape, function declarations | anything that uses it |
| `entity.cpp` | method bodies | nothing |
| `main.cpp` | `#include "entity.hpp"` and `main` | — |

```bash
g++ -std=c++17 -Wall -Wextra main.cpp entity.cpp -o console
```

## Memory

| Where | Created by | Freed by | Lifetime |
| :--- | :--- | :--- | :--- |
| Stack | the compiler | the compiler | the enclosing block |
| Heap | `new`, containers, smart pointers | `delete`, the owner | until released |
| Static | the loader | the program exit | whole run |

| Symbol | Means |
| :--- | :--- |
| `&x` | address of `x` |
| `*p` | object `p` points at |
| `p->field` | `(*p).field` |
| `nullptr` | points at nothing |
| `new T{...}` | allocate on the heap |
| `delete p` | release one object |
| `std::make_unique<T>(...)` | owned heap value, freed automatically |

> [!CAUTION]
> A pointer to a local (`&local` returned from a function), a double `delete`, and a dereferenced
> `nullptr` are the three ways this chapter is usually lost. Check before `->`, and never return the
> address of a local.

## The three habits

1. Let the compiler catch it: `-Wall -Wextra -Wshadow -fsanitize=address,undefined`.
2. Let containers and smart pointers own heap memory; use raw pointers only to observe.
3. Make the type uphold its own rules — validation in the constructor, clamping in the method.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
