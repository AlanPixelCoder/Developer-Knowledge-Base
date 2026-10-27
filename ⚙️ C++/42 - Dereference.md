# 42. Dereference

**Spanish version:** [42 - Desreferenciación.md](./42%20-%20Desreferenciaci%C3%B3n.md)

**Course:** C++
**Topic:** Dereferencing Pointers
**Tags:** `#cpp` `#pointers` `#dereference`

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

We know how to create a pointer and get the address of the variable it points to. But how do we
access the **value** it points to?

**Dereference** means accessing the value a pointer is pointing to. We do it with `*` — the
dereferencing operator.

```cpp
int x = 420;
int* p = &x;

std::cout << p << "\n";  // the memory address (e.g. 0x16f...)
std::cout << *p << "\n"; // the value: 420
```

## The two faces of `*`

| Context | Meaning | Example |
| :--- | :--- | :--- |
| In a **declaration** | Creates a pointer | `int* p = &x;` |
| **Not** in a declaration | Dereferences — reads the value | `std::cout << *p;` |

Same character, two jobs. The difference is position: `*` next to a type is a declaration; `*` in
an expression is a dereference.

## Writing through a pointer

Dereferencing is also how you **change** the original value:

```cpp
*p = 99;          // x is now 99
std::cout << x;   // 99
```

```cpp
// Continuing the previous note
std::cout << *pTip1 << "\n";
std::cout << *pTip2 << "\n";
std::cout << *pTip3 << "\n";
std::cout << *pTip4 << "\n";
```

> [!TIP]
> **Read `*` as "the value at"**
> `*p` → "the value at `p`". `&x` → "the address of `x`". Those two phrases cover almost every
> line of pointer code you will read.

> [!WARNING]
> Dereferencing an uninitialized or dangling pointer is undefined behavior. The address may be
> valid, it may point into another variable, or it may crash. Always initialize — see
> [[44 - Nullptr]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
