# 45. Where Things Live

**Spanish version:** [45 - Dónde Viven las Cosas](./45%20-%20D%C3%B3nde%20Viven%20las%20Cosas.md)

**Course:** C++
**Chapter:** 8 — Memory
**Topic:** The stack and the heap, and which one your variables use
**Tags:** `#cpp` `#memory` `#stack`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermediate">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Every value in a running program lives somewhere. Two regions cover almost everything you write: the
stack, which grows and shrinks with function calls, and the heap, which you ask for and give back.

```cpp
#include <iostream>

int global_counter = 7;          // static storage: whole program

void show_stack() {
  int local = 41;                // automatic storage: this call only
  std::cout << "local address:  " << &local << "\n";
}

int main() {
  int a = 1;
  int b = 2;

  show_stack();

  std::cout << "a address:      " << &a << "\n";
  std::cout << "b address:      " << &b << "\n";
  std::cout << "global address: " << &global_counter << "\n";
}
```

## Output

A sample run — addresses change on every run and every build:

```text
local address:  0x7ff7b6f0a5ac
a address:      0x7ff7b6f0a5b8
b address:      0x7ff7b6f0a5bc
global address: 0x10b3d0000
```

## Three regions, three lifetimes

| Region | Who creates | Lifetime | Example |
| :--- | :--- | :--- | :--- |
| Stack (automatic) | the compiler, on entry | until the block ends | `int a = 1;` |
| Heap (dynamic) | `new` or a container | until `delete` or the owner dies | `new int(5)` |
| Static | the loader | the whole program | globals, `static` locals |

The exact addresses differ every run and every build. What does not change: stack addresses are close
together and grow downward, heap addresses come from another region entirely.

## Why the distinction matters

- Stack allocation is a pointer move — effectively free.
- Heap allocation asks the allocator for a block, which costs time and can fail.
- Stack memory disappears automatically. Heap memory does not, which is either convenient or a leak.

> [!NOTE]
> `std::vector` keeps its elements on the heap even when the vector object itself is on the stack.
> That is how it can grow: the small object holds a pointer, a size and a capacity.

> [!TIP]
> Printing `&variable` shows where it lives, not what it holds. Addresses are a debugging tool, never
> a value to compare or store — the same variable can move between runs.

---

**Next:** [[46 - The Address-Of Lens]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
