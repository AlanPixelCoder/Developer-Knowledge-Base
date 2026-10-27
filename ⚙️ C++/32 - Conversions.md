# 32. Conversions

**Spanish version:** [32 - Conversiones.md](./32%20-%20Conversiones.md)

**Course:** C++
**Topic:** Return Value
**Tags:** `#cpp` `#functions` `#return` `#void`

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

Functions can take inputs, but they can also **send out** values.

When we declare a function with `void`, the function just does a task and leaves us nothing.

To output a value, change `void` to the data type you want to return (e.g., `int`, `double`,
`std::string`) and use the `return` keyword.

The `return` keyword **terminates the function** and leaves a value behind.

## Syntax

```cpp
int add(int x, int y) {
  int answer = 0;
  answer = x + y;
  return answer; // leaves the value behind
}
```

Now, calling the function produces a value we can print, assign, or feed into another expression.

```cpp
int total = add(4, 3);     // total is 7
std::cout << add(10, 5);   // 15
```

## void vs Return Type

| Type | Hands back | Use it for |
| :--- | :--- | :--- |
| `void` | Nothing | Printing, updating state, side effects |
| `int` / `double` / … | A value of that type | Calculations, lookups, conversions |

> [!IMPORTANT]
> **The returned value has to be *used* or *stored***
> `add(1, 2);` on its own line computes 7 and throws it away. The call is legal, but pointless.
> Assign it, print it, or pass it onward.

> [!TIP]
> A `return` inside a function acts like an early exit. Everything after it in that function is
> skipped. See [[32 - Conversions (Continuation)]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
