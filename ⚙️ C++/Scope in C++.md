# Scope in C++

**Spanish version:** [Ámbito en C++.md](./%C3%81mbito%20en%20C%2B%2B.md)

**Course:** C++
**Topic:** Local and Global Scope
**Tags:** `#cpp` `#scope` `#variables`

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

In C++, **scope** refers to the region of the program where a name (a variable, function, or class
name) is visible and can be accessed.

## Local Scope

A **local variable** is declared inside a function or block `{}`. It belongs to that scope and can
only be used inside it. Access it outside and the program refuses to compile.

- *Use case:* a value only needed temporarily inside a function.
- *Best practice:* local whenever possible.

## Global Scope

A **global variable** is created outside of any function and belongs to the global scope — it is
accessible from anywhere in the program file.

- *Use case:* a value genuinely shared across multiple functions or files.

## Example

```cpp
#include <iostream>

int day = 3; // global

void welcome() {
  std::cout << "Welcome to day " << day << " of Beast Games\n";
}

int main() {
  std::cout << "Which day is it again?\n";
  std::cout << day << "\n";
  welcome();
}
```

## Local vs Global

| | Local | Global |
| :--- | :--- | :--- |
| Declared | Inside `{}` | Outside all functions |
| Visible | That block only | Whole file |
| Lifetime | Until the block ends | Until the program ends |
| Risk | Low | Hidden couplings, accidental mutation |

> [!WARNING]
> **Shadowing**
> If a local variable has the same name as a global one, the local one *wins* inside its block.
> `int day = 9;` inside `main()` hides the global `day`, and the global silently keeps its old
> value. Legal code, confusing program.

> [!TIP]
> When in doubt, keep it local. A global is a variable every function can reach — which means
> every function is a suspect when it changes unexpectedly.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
