# 36. Cuentas Bancarias

**Versión original en inglés:** [36 - Bank Accounts.md](./36%20-%20Bank%20Accounts.md)

**Curso:** C++
**Tema:** Métodos de clase
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

Los atributos describen lo que un objeto **tiene**. Los **métodos** describen lo que un objeto
**hace**.

Un método es una función definida **dentro** de una clase. Puede leer y modificar los atributos del
propio objeto sin que se los pasen como parámetros: ya vive dentro del objeto.

## Ejemplo

```cpp
#include <iostream>
#include <string>

class BankAccount {
  public:
    std::string name;
    double balance = 0;

    void depositar(double cantidad) {
      balance += cantidad;
    }

    void mostrar() {
      std::cout << name << ": $" << balance << "\n";
    }
};

int main() {
  BankAccount cuenta;
  cuenta.name = "Cámara del Gremio";
  cuenta.depositar(250);
  cuenta.mostrar(); // Cámara del Gremio: $250
}
```

## Atributos vs métodos

| | Declara | Se llama como | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Atributo** | Datos | `obj.atributo` | `cuenta.balance` |
| **Método** | Comportamiento | `obj.metodo()` | `cuenta.depositar(50)` |

> [!NOTE]
> **`this` — el nombre propio del objeto**
> Dentro de un método, `balance` y `this->balance` significan lo mismo. `this` es un puntero al
> objeto sobre el que se opera: la razón por la que un solo cuerpo de método sirve a mil objetos
> distintos.

> [!TIP]
> Regla práctica: si el primer pensamiento de una función es "¿qué objeto?", pertenece dentro de esa
> clase como método.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
