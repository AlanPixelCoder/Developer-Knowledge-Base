# 37. Cuentas Bancarias (Continuación)

**Versión original en inglés:** [37 - Bank Accounts (Continuation).md](./37%20-%20Bank%20Accounts%20%28Continuation%29.md)

**Curso:** C++
**Tema:** Métodos de clase aplicados
**Etiquetas:** `#cpp` `#classes` `#methods` `#oop`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Vamos a aplicar los métodos de clase construyendo un pequeño sistema bancario. Definimos una clase
`BankAccount` con métodos `deposit()`, `withdraw()` y `display_balance()`.

```cpp
#include <iostream>
#include <string>

class BankAccount {
  public:
    std::string name;
    int account_id;
    std::string account_type;
    double balance;

    // Añadir dinero y devolver el nuevo saldo
    double deposit(double amount) {
      balance += amount;
      return balance;
    }

    // Restar dinero del saldo
    void withdraw(double amount) {
      balance -= amount;
    }

    // Imprimir el saldo actual
    void display_balance() {
      std::cout << "Saldo actual: $" << balance << "\n";
    }
};

int main() {
  BankAccount fondo_cabana;
  fondo_cabana.name = "Alan Pixel Coder";
  fondo_cabana.account_id = 777;
  fondo_cabana.account_type = "Ahorros";
  fondo_cabana.balance = 1000.00;

  fondo_cabana.deposit(96);   // 1096
  fondo_cabana.withdraw(25);  // 1071
  fondo_cabana.display_balance();
}
```

## Salida

```text
Saldo actual: $1071
```

> [!WARNING]
> **`withdraw()` confía en quien la llama**
> Nada impide que el saldo quede negativo. Cuando `balance` sea `private` (ver
> [[35 - Público vs Privado]]), `withdraw()` se convierte en el único lugar donde añadir la
> comprobación: `if (amount <= balance)`.

> [!NOTE]
> `deposit()` devuelve `double` mientras que `withdraw()` devuelve `void`: una asimetría deliberada.
> Un depósito responde "¿cuál es el nuevo total?"; un retiro solo necesita informar éxito o fracaso.

> [!TIP]
> Un valor por defecto en el campo (`balance = 1000.00;`) más un constructor (siguiente nota)
> colapsarían esas cuatro líneas de asignación en una.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
