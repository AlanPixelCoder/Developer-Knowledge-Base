# 31. OOO

**Spanish version:** [31 - Fuera de Oficina.md](./31%20-%20Fuera%20de%20Oficina.md)

**Course:** C++
**Topic:** Parameters vs. Arguments
**Tags:** `#cpp` `#functions` `#parameters` `#arguments`

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

Sometimes a function performs a task that varies depending on different input(s).

## Parameters

**Parameters** are the variables a function takes as input. They go inside the parentheses in the
function **definition** and are used inside the body. Every parameter needs a data type.

```cpp
void ooo_message(std::string date) { // 'date' is the parameter
  // ...
}
```

## Arguments

An **argument** is the value **sent** to the function when the function is **called**.

```cpp
ooo_message("Monday"); // "Monday" is the argument
```

## The Difference

| | When | What |
| :--- | :--- | :--- |
| **Parameter** | At definition | The variable listed inside the parentheses |
| **Argument** | At the call | The actual value passed in |

> [!TIP]
> **Mnemonic**
> **P**arameter = **P**laceholder. **A**rgument = **A**ctual value.

## Example

```cpp
#include <iostream>
#include <string>

void ooo_message(std::string date) {
  std::cout << "Thank you for your email.\n";
  std::cout << "I am currently out of the office and will be back " << date << ".\n";
  std::cout << "I will respond as soon as I can upon my return.\n\n";
}

int main() {
  ooo_message("Monday");
  ooo_message("November 2nd");
}
```

> [!NOTE]
> Each call gets a **fresh copy** of the parameter. Calling `ooo_message` twice with different
> arguments produces two different letters, and neither call overwrites the other.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
