# 30. Estantes de Piedra y Alforjas

**Versión original en inglés:** [30 - Stone Racks and Satchels](./30%20-%20Stone%20Racks%20and%20Satchels.md)

**Curso:** C++
**Capítulo:** 5 — Colecciones
**Tema:** Arrays al estilo C junto a vectores: cuándo encaja cada uno
**Etiquetas:** `#cpp` `#array` `#vector`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

La forja tiene un estante fijo de seis ranuras de piedra talladas en el muro, y una alforja que se
estira. Uno no cambia de tamaño, la otra sí, y esa única diferencia decide casi todas tus elecciones.

```cpp
#include <iostream>
#include <vector>

int main() {
  int estante[6] = {40, 12, 0, 7, 33, 8};  // fijo: seis piedras, para siempre

  int total = 0;
  for (int i = 0; i < 6; i++) {
    total += estante[i];
  }

  std::vector<int> alforja{total};      // crece cuando la forja da más
  alforja.push_back(95);

  std::cout << "piedras del estante: " << sizeof(estante) / sizeof(estante[0]) << "\n";
  std::cout << "total del estante:   " << total << "\n";
  std::cout << "piedras en alforja:  " << alforja.size() << "\n";
  std::cout << "última de alforja:   " << alforja.back() << "\n";
}
```

## Salida

```text
piedras del estante: 6
total del estante:   100
piedras en alforja:  2
última de alforja:   95
```

## Dos contenedores, dos promesas

| Pregunta | `int estante[6]` | `std::vector<int>` |
| :--- | :--- | :--- |
| Tamaño conocido en compilación | sí | opcional |
| Puede crecer | no | sí |
| Conoce su tamaño | no (truco de `sizeof`) | `size()` |
| Se copia con `=` | no (decae a puntero) | sí |
| Se pasa a una función con seguridad | solo como puntero, tamaño perdido | por valor o referencia |

## El truco de `sizeof`

`sizeof(estante)` es el array completo en bytes; `sizeof(estante[0])` es un elemento. Divide y tienes
la cuenta, pero solo donde el tipo array sigue visible. Dentro de una función que recibió `estante`,
ya decayó a puntero y la división devuelve basura.

> [!CAUTION]
> Pasar un array a una función pierde su tamaño. `void f(int estante[6])` declara
> `void f(int* estante)`. El `6` es documentación, no una promesa. Prefiere
> `std::array<int, 6>` o un vector.

> [!TIP]
> Usa un array fijo cuando la cuenta es de verdad una constante de compilación y nunca cruza una
> frontera de función. En otro caso un vector cuesta un puntero y ahorra una clase de errores.

---

**Siguiente:** [[31 - Un Hechizo, Muchos Usos]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
