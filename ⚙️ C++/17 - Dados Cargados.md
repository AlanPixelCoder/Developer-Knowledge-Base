# 17. Dados Cargados

**Versión original en inglés:** [17 - Loaded Dice](./17%20-%20Loaded%20Dice.md)

**Curso:** C++
**Capítulo:** 3 — Decisiones
**Tema:** Rangos aleatorios, el truco del módulo y su sesgo
**Etiquetas:** `#cpp` `#random` `#modulo`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-3-7C5CFF?style=for-the-badge" alt="Chapter 3">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

`std::rand()` devuelve un número entre `0` y `RAND_MAX`. Cada juego necesita un rango distinto, y una
sola expresión los cubre todos.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int d6 = std::rand() % 6 + 1;      // 1..6
  int d20 = std::rand() % 20 + 1;    // 1..20
  int desde_cero = std::rand() % 5;  // 0..4
  double probabilidad = (std::rand() % 101) / 100.0;  // 0.00..1.00

  std::cout << "d6: " << d6 << "\n";
  std::cout << "d20: " << d20 << "\n";
  std::cout << "0..4: " << desde_cero << "\n";
  std::cout << "probabilidad: " << probabilidad << "\n";
}
```

## La fórmula, en dos partes

| Forma | Da | Ejemplo |
| :--- | :--- | :--- |
| `rand() % n` | `0` a `n - 1` | `% 5` → `0 1 2 3 4` |
| `rand() % n + 1` | `1` a `n` | `% 5 + 1` → `1 2 3 4 5` |

El `%` pliega el rango enorme del generador en el pequeño; el `+ 1` desplaza el resultado.

> [!CAUTION]
> `%` no es perfectamente uniforme. Si `RAND_MAX + 1` no es múltiplo de `n`, los valores bajos salen
> algo más a menudo. Es invisible en una tirada de dados y no lo es en una tabla de botín que corre un
> millón de veces. Para eso existe `std::uniform_int_distribution`.

> [!NOTE]
> `(rand() % 101) / 100.0` da un porcentaje entre `0.0` y `1.0`, pero la división es por `100.0` y no
> por `100`, justamente para que la fracción sobreviva. Ver [[10 - Números que Mienten]].

> [!TIP]
> Nombra el rango en la variable: `d20`, `d6`, `probabilidad`. `tirada` en tres sitios es cómo un dado
> de 20 caras se convierte en uno de 6 durante un refactor.

---

**Siguiente:** [[18 - Guardias y Portones]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
