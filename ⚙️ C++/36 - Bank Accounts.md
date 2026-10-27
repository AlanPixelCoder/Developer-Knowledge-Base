# 36. Bank Accounts

**Spanish version:** [36 - Cuentas Bancarias.md](./36%20-%20Cuentas%20Bancarias.md)

**Course:** C++
**Topic:** Class Methods
**Tags:** `#cpp` `#classes` `#methods` `#oop`

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

Attributes describe what an object **has**. **Methods** describe what an object **does**.

A method is a function defined **inside** a class. It can read and change the object's own
attributes without being handed them as parameters — it already lives inside the object.

## Example

```cpp
#include <iostream>
#include <string>

class BankAccount {
  public:
    std::string name;
    double balance = 0;

    void deposit(double amount) {
      balance += amount;
    }

    void display() {
      std::cout << name << ": $" << balance << "\n";
    }
};

int main() {
  BankAccount acc;
  acc.name = "Guild Vault";
  acc.deposit(250);
  acc.display(); // Guild Vault: $250
}
```

## Attributes vs Methods

| | Declares | Called as | Example |
| :--- | :--- | :--- | :--- |
| **Attribute** | Data | `obj.attribute` | `acc.balance` |
| **Method** | Behavior | `obj.method()` | `acc.deposit(50)` |

> [!NOTE]
> **`this` — the object's own name**
> Inside a method, `balance` and `this->balance` mean the same thing. `this` is a pointer to the
> object being operated on — the reason one method body can serve a thousand different objects.

> [!TIP]
> Rule of thumb: if a function's first thought is "which object?" — it belongs inside that class
> as a method.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
