# 41. A Few Pointers

**Spanish version:** [41 - Unos Punteros.md](./41%20-%20Unos%20Punteros.md)

**Course:** C++
**Topic:** Pointers Introduction
**Tags:** `#cpp` `#pointers` `#memory`

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

Now that we know about memory addresses, let's tackle pointers.

**Pointers** are special variables that store the memory address of another variable. Think of it
as sharing your pizza's location instead of carrying the pizza everywhere — you hand out the
address and friends come to you for a slice.

Create a pointer with the `*` operator:

```cpp
int x = 420;
int* p = &x; // p holds the address of x
```

> [!NOTE]
> **The pointer's type matters**
> A pointer must match the type of the variable it points to: an `int*` points at an `int`. The
> type tells the compiler how many bytes to read when you dereference, and how far to step when
> you do arithmetic.

## Declaring one

The spacing around `*` does not matter:

```cpp
double* pPrice;
double *pPrice;
double * pPrice;
```

All three are identical to the compiler. Pick one style and hold it — consistency is what makes
pointer-heavy code readable.

## Why do we need pointers?

| Use case | Why it helps |
| :--- | :--- |
| **Modify data** | A function that knows the address can change the original value |
| **Dynamic structures** | Linked lists and trees link nodes to nodes *by address* |
| **Performance** | Pass a pointer to a huge object instead of copying it |
| **Low-level interfacing** | Talk to APIs, system calls, C libraries, and hardware |

## Example

```cpp
#include <iostream>
#include <string>

int main() {
  std::string tip1 = "Stay consistent: even 10 minutes a day adds up.";
  std::string tip2 = "Take notes: writing things down helps concepts stick.";
  std::string tip3 = "Build small projects: apply what you learn.";
  std::string tip4 = "Join a community: it's easier when you're not alone.";

  std::string* pTip1 = &tip1;
  std::string* pTip2 = &tip2;
  std::string* pTip3 = &tip3;
  std::string* pTip4 = &tip4;

  std::cout << "Waypoint 1: " << pTip1 << "\n";
  std::cout << "Waypoint 2: " << pTip2 << "\n";
  std::cout << "Waypoint 3: " << pTip3 << "\n";
  std::cout << "Waypoint 4: " << pTip4 << "\n";
}
```

> [!WARNING]
> **A pointer is just a number until you dereference it**
> Printing `pTip1` gives an address. Printing `*pTip1` gives the string. Getting these confused is
> the first day of every C++ debugging session.

> [!TIP]
> This is also the reason C++ can feel "dangerous": the address is real, and nothing stops you from
> reading whatever lives there. See [[44 - Nullptr]] for the safety net.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
