# 25. La Alforja

**Versión original en inglés:** [25 - The Satchel](./25%20-%20The%20Satchel.md)

**Curso:** C++
**Capítulo:** 5 — Colecciones
**Tema:** Qué es un std::vector y por qué gana a un puñado de variables
**Etiquetas:** `#cpp` `#vector` `#collections`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Cuatro montones de ingredientes, cuatro variables, cuatro líneas de impresión. Luego la receta crece
a seis y el código crece con ella. Un `std::vector` guarda todos bajo un nombre y conoce su tamaño.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> alforja{7, 3, 12, 1};  // cuatro montones, un contenedor

  std::cout << "montones: " << alforja.size() << "\n";
  std::cout << "primero:  " << alforja[0] << "\n";
  std::cout << "último:   " << alforja[alforja.size() - 1] << "\n";
}
```

## Salida

```text
montones: 4
primero:  7
último:   1
```

## Un nombre, muchas ranuras

| Necesidad | Con variables | Con un vector |
| :--- | :--- | :--- |
| Añadir un quinto montón | variable nueva + impresión nueva | `alforja.push_back(9)` |
| Informar la cuenta | llevar un contador aparte | `alforja.size()` |
| Recorrer todo | una línea por variable | un `for` de tres líneas |

El contenedor no hace menos accesibles los valores. `alforja[2]` es el mismo doce que habrías
guardado en `monton3`.

## Incluir, declarar, llenar

1. `#include <vector>`
2. `std::vector<int> alforja;` — vacío, crece después
3. `std::vector<int> alforja{7, 3, 12, 1};` — cuatro valores desde el inicio
4. `std::vector<int> alforja(4);` — cuidado: cuatro **ceros**, no cuatro ranuras vacías

> [!CAUTION]
> `std::vector<int> alforja(4)` y `std::vector<int> alforja{4}` son distintos: el primero son
> cuatro ceros, el segundo es un elemento que vale 4. Llaves frente a paréntesis es toda la
> diferencia.

> [!TIP]
> `size()` devuelve un tipo sin signo. Cuando le restes, como en `size() - 1`, asegúrate primero de
> que el vector no está vacío, o la resta dará la vuelta a un número enorme.

---

**Siguiente:** [[26 - Ranura e Índice]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
