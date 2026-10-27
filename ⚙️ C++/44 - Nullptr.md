# 44. Nullptr

**Spanish version:** [44 - Puntero Nulo.md](./44%20-%20Puntero%20Nulo.md)

**Course:** C++
**Topic:** The `nullptr` Keyword
**Tags:** `#cpp` `#pointers` `#nullptr`

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

A pointer holds the memory address of another variable. But what if we want a pointer that doesn't
point anywhere yet — an intentionally empty pointer?

If we declare `int* p;` without initializing it, `p` contains a **random** address. Using it now
could crash the program.

`nullptr` is a keyword representing a pointer that points to **no** memory address — an address
that doesn't exist or isn't found. It's C++'s way of saying: *"this pointer points to nothing."*

```cpp
int* p = nullptr;
```

## Why it's better than `NULL` or `0`

| Value | Problem |
| :--- | :--- |
| `NULL` | A macro for `0` — an integer, so overload resolution can pick the wrong function |
| `0` | Ambiguous between "integer zero" and "null pointer" |
| `nullptr` | Has its own type, `std::nullptr_t` — never ambiguous |

## Guarding with a check

`nullptr` also gives you a clean control-flow check: has this pointer been assigned something yet?

```cpp
#include <iostream>
#include <string>

void greet(const std::string* name) {
  if (name != nullptr) {
    std::cout << "Hello, " << *name << "!\n";
  } else {
    std::cout << "Hello, guest!\n";
  }
}

int main() {
  std::string user = "marcos";

  greet(&user);   // Hello, marcos!
  greet(nullptr); // Hello, guest!
}
```

## Output

```text
Hello, marcos!
Hello, guest!
```

> [!CAUTION]
> **Null dereference is the classic crash**
> `*name` when `name == nullptr` is undefined behavior — on most systems, a segfault. The check is
> not defensive paranoia; it's the reason the program stays alive.

> [!TIP]
> Initialize every pointer you declare — either to a real address or to `nullptr`. An
> uninitialized pointer is a landmine with no warning label.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
