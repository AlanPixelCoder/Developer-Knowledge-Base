# 37. Where Names Live

**Spanish version:** [37 - Dónde Viven los Nombres](./37%20-%20D%C3%B3nde%20Viven%20los%20Nombres.md)

**Course:** C++
**Chapter:** 6 — Functions
**Topic:** Scope, lifetime, and shadowing
**Tags:** `#cpp` `#scope` `#lifetime`

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

The engine has a global `tick` counter, a function with a local `tick`, and a block inside that
function with another `tick`. Three variables, one name, and the innermost one wins everywhere it is
visible.

```cpp
#include <iostream>

int tick = 100;                 // file scope

void advance() {
  int tick = 1;                 // shadows the global
  {
    int tick = 7;               // shadows the local
    std::cout << "inner:  " << tick << "\n";
  }
  std::cout << "local:  " << tick << "\n";
}

int main() {
  advance();
  std::cout << "global: " << tick << "\n";
  std::cout << "::tick: " << ::tick << "\n";
}
```

## Output

```text
inner:  7
local:  1
global: 100
::tick: 100
```

## Scope is where a name is visible

| Name | Scope | Lifetime |
| :--- | :--- | :--- |
| `tick` (file) | whole file after the declaration | whole program |
| `tick` (local) | `advance`'s body | each call |
| `tick` (inner) | that block only | until the block's `}` |

A local is created on entry and destroyed at the closing brace. The global exists before `main` and
after it returns.

## Shadowing is legal and usually a mistake

The compiler allows it; `-Wshadow` will tell you it happened. `::tick` reaches past every local to the
global, and needing it is a strong hint that two variables should not share a name.

> [!WARNING]
> A shadowed variable is not "the same variable with a new value". The outer one keeps its value and
> resumes when the inner block ends, which is exactly the confusion shadowing invites.

> [!TIP]
> Prefer passing values as parameters over reaching for globals. A function that reads a global
> cannot be tested without the global, and cannot be called twice with different inputs.

> [!NOTE]
> Declare variables as late as possible and in the smallest scope that works. A name that exists for
> forty lines is a name you can misuse for forty lines.

---

**Next:** [[38 - Guild Blueprints]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
