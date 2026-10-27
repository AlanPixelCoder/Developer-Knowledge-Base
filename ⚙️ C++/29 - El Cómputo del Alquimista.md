# 29. El Cómputo del Alquimista

**Versión original en inglés:** [29 - The Alchemist's Tally](./29%20-%20The%20Alchemist%27s%20Tally.md)

**Curso:** C++
**Capítulo:** 5 — Colecciones
**Tema:** Acumuladores: suma, cuenta, máximo y media sobre una colección
**Etiquetas:** `#cpp` `#vector` `#accumulator`

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

El alquimista quiere un número por pregunta: cuántos, cuánto, cuál es el mayor, cuál es la media. Los
cuatro son el mismo bucle con otro valor inicial y otra actualización.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> lotes{12, 7, 25, 4, 18};

  int cuenta = 0;
  int suma = 0;
  int mejor = lotes[0];

  for (int n : lotes) {
    cuenta++;
    suma += n;
    if (n > mejor) {
      mejor = n;
    }
  }

  std::cout << "lotes:   " << cuenta << "\n";
  std::cout << "total:   " << suma << "\n";
  std::cout << "mejor:   " << mejor << "\n";
  std::cout << "promedio: " << static_cast<double>(suma) / cuenta << "\n";
}
```

## Salida

```text
lotes:   5
total:   66
mejor:   25
promedio: 13.2
```

## Cuatro formas, un bucle

| Objetivo | Inicio | Actualización |
| :--- | :--- | :--- |
| Contar | `0` | `cuenta++` |
| Sumar | `0` | `suma += n` |
| Máximo | primer elemento | `if (n > mejor) mejor = n` |
| Media | suma y cuenta | dividir al final |

Empezar `mejor` en `0` es un error clásico: con una colección toda negativa la respuesta es falsa.
Empezar en `lotes[0]` es correcto para cualquier colección no vacía.

## La trampa de la división entera

`suma / cuenta` con dos `int` trunca. `66 / 5` es `13`, no `13.2`. Convertir un lado a `double`
cambia toda la expresión a coma flotante.

> [!WARNING]
> `static_cast<double>(suma / cuenta)` convierte el *cociente*, que ya es `13`. La conversión debe
> envolver solo `suma`, o mejor, escribirse como
> `static_cast<double>(suma) / static_cast<double>(cuenta)`.

> [!TIP]
> `std::accumulate` de `<numeric>` hace la suma en una llamada, y `std::max_element` de `<algorithm>`
> encuentra el máximo. Aprende primero los bucles: son lo que esos algoritmos compilan.

---

**Siguiente:** [[30 - Estantes de Piedra y Alforjas]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
