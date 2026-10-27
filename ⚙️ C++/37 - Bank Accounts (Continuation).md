# 37. Bank Accounts (Continuation)

**Spanish version:** [37 - Cuentas Bancarias (Continuación).md](./37%20-%20Cuentas%20Bancarias%20%28Continuaci%C3%B3n%29.md)

**Course:** C++
**Topic:** Class Methods Applied
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

Let's apply class methods by building a small bank account system. We define a `BankAccount` class
with methods to `deposit()`, `withdraw()`, and `display_balance()`.

```cpp
#include <iostream>
#include <string>

class BankAccount {
  public:
    std::string name;
    int account_id;
    std::string account_type;
    double balance;

    // Add money, return the new balance
    double deposit(double amount) {
      balance += amount;
      return balance;
    }

    // Subtract money from the balance
    void withdraw(double amount) {
      balance -= amount;
    }

    // Print the current balance
    void display_balance() {
      std::cout << "Current Balance: $" << balance << "\n";
    }
};

int main() {
  BankAccount cabin_fund;
  cabin_fund.name = "Alan Pixel Coder";
  cabin_fund.account_id = 777;
  cabin_fund.account_type = "Savings";
  cabin_fund.balance = 1000.00;

  cabin_fund.deposit(96);   // 1096
  cabin_fund.withdraw(25);  // 1071
  cabin_fund.display_balance();
}
```

## Output

```text
Current Balance: $1071
```

> [!WARNING]
> **`withdraw()` trusts its caller**
> Nothing stops the balance from going negative. Once `balance` is `private` (see
> [[35 - Public vs. Private]]), `withdraw()` becomes the single place to add a check:
> `if (amount <= balance)`.

> [!NOTE]
> `deposit()` returns `double` while `withdraw()` returns `void` — a deliberate asymmetry. A
> deposit answers "what is the new total?"; a withdrawal only needs to report success or failure.

> [!TIP]
> An object literal with a `balance = 1000.00;` field default plus a constructor (next note) would
> collapse those four assignment lines into one.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
