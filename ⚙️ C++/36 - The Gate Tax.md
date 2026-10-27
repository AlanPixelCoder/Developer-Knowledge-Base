# 36. The Gate Tax

**Spanish version:** [36 - El Impuesto del Portal](./36%20-%20El%20Impuesto%20del%20Portal.md)

**Course:** C++
**Chapter:** 6 — Functions
**Topic:** Pass by value versus pass by reference
**Tags:** `#cpp` `#functions` `#references`

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

Every traveller pays a tax at the gate. The gate clerk writes the amount in the ledger. Two ways to
hand the ledger over: a copy they can scribble on, or the real book.

```cpp
#include <iostream>

int tax_by_copy(int gold) {
  gold -= 10;          // changes the copy only
  return gold;
}

void tax_by_reference(int& gold) {
  gold -= 10;          // changes the caller's variable
}

int main() {
  int purse = 50;

  std::cout << "returned: " << tax_by_copy(purse) << "\n";
  std::cout << "purse:    " << purse << "\n";

  tax_by_reference(purse);
  std::cout << "purse:    " << purse << "\n";
}
```

## Output

```text
returned: 40
purse:    50
purse:    40
```

## The four ways to pass

| Signature | Copies? | Caller sees change? | Use when |
| :--- | :--- | :--- | :--- |
| `int x` | yes | no | small values, plain inputs |
| `const int&` | no | no | large read-only objects |
| `int&` | no | yes | the function must modify |
| `int*` | no (pointer copied) | yes, if dereferenced | optional "no value" case |

An `int` is small enough that copying is faster than indirection. A `std::string` or a `std::vector`
is not, which is why `const std::string&` is the default for read-only parameters.

## `&` on the parameter, `&` in the call

The ampersand belongs to the **type** in the signature. At the call site you write `tax_by_reference(purse)`
with no `&` — the function already demands a reference.

> [!CAUTION]
> `tax_by_reference(50)` does not compile: a literal is not an lvalue, so no non-const reference can
> bind to it. If the caller's value must not change, take `int` or `const int&`.

> [!TIP]
> A function that both takes and returns a value through a reference is a sign you wanted
> `int tax(int gold) { return gold - 10; }`. Modify through a reference only when the point of the
> function is the modification.

---

**Next:** [[37 - Where Names Live]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
