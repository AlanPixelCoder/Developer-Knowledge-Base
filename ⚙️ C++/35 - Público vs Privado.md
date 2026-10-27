# 35. Público vs Privado

**Versión original en inglés:** [35 - Public vs. Private.md](./35%20-%20Public%20vs.%20Private.md)

**Curso:** C++
**Tema:** Modificadores de acceso y encapsulación
**Etiquetas:** `#cpp` `#classes` `#oop` `#encapsulation`

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

Una clase es un plano, pero un plano que nadie puede leer es inútil. Los **modificadores de acceso**
deciden quién puede tocar cada miembro.

| Modificador | Quién accede |
| :--- | :--- |
| `public` | Cualquiera, dentro y fuera de la clase |
| `private` | Solo el código de la propia clase |
| `protected` | La clase y las clases que heredan de ella |

```cpp
class Player {
  public:
    std::string name;  // cualquiera lee y escribe
    int level;
  private:
    double wallet;     // solo los métodos de Player
};
```

El código externo puede asignar `player.name`, pero `player.wallet = 999;` es un error de
compilación.

## Encapsulación

La **encapsulación** consiste en esconder los datos internos detrás de una interfaz controlada. La
clase decide qué puede ver el mundo exterior y cómo puede cambiarlo.

> [!NOTE]
> **¿Para qué molestarse?** Porque un invariante solo vale algo si nada puede romperlo. Si `wallet`
> pudiera asignarse directamente, cualquier línea de código podría inventar dinero. Miembros privados
> más un método público que valida significa que solo un lugar puede romper la regla — y solo un
> lugar debe hacerla cumplir.

## Ejemplo

```cpp
#include <iostream>

class Player {
  public:
    std::string name;

    void mostrar_saldo() {
      std::cout << name << " tiene $" << wallet << "\n";
    }

    void gastar(double cantidad) {
      if (cantidad > 0 && cantidad <= wallet) {
        wallet -= cantidad;
      }
    }

  private:
    double wallet = 100.0;
};

int main() {
  Player hero;
  hero.name = "Aldric";
  hero.gastar(30);
  hero.mostrar_saldo(); // Aldric tiene $70
}
```

> [!TIP]
> Empieza todo en `private`. Abre un miembro a `public` solo cuando tengas una razón: en una clase
> bien diseñada, el valor por defecto es cerrado.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
