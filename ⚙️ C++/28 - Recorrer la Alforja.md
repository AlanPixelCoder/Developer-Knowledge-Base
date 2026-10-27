# 28. Recorrer la Alforja

**Versión original en inglés:** [28 - Walking the Satchel](./28%20-%20Walking%20the%20Satchel.md)

**Curso:** C++
**Capítulo:** 5 — Colecciones
**Tema:** Range-for y bucles con índice sobre un vector
**Etiquetas:** `#cpp` `#vector` `#range-for`

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

Imprimir cada montón significa visitar cada índice. Dos bucles lo hacen; difieren en lo que te dan
dentro del cuerpo.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> alforja{"antorcha", "cuerda", "pan"};
  std::vector<int> montones{2, 5, 1};

  std::cout << "bucle con índice:\n";
  for (std::size_t i = 0; i < alforja.size(); i++) {
    std::cout << "  " << i << ": " << alforja[i] << "\n";
  }

  std::cout << "bucle por rango:\n";
  for (const std::string& objeto : alforja) {
    std::cout << "  " << objeto << "\n";
  }

  int total = 0;
  for (int n : montones) {
    total += n;
  }
  std::cout << "montones totales: " << total << "\n";
}
```

## Salida

```text
bucle con índice:
  0: antorcha
  1: cuerda
  2: pan
bucle por rango:
  antorcha
  cuerda
  pan
montones totales: 8
```

## Qué bucle elegir

| Necesitas | Bucle |
| :--- | :--- |
| Cada elemento, sin índice | `for (const auto& x : v)` |
| También el índice | `for (std::size_t i = 0; i < v.size(); i++)` |
| Modificar cada elemento | `for (auto& x : v)` |
| Cortar antes según una condición | bucle con índice y `break` |

`std::size_t` es el tipo que devuelve `size()`. Usar `int` provoca un aviso de comparación
con signo y sin signo bajo `-Wextra`.

## El `&` no es decoración

`for (const std::string& objeto : alforja)` enlaza una referencia: sin copia por pasada. Sin el `&`,
se copia una cadena nueva por elemento, invisible en un ejemplo de tres y caro en uno de mil.

> [!IMPORTANT]
> Quita `const` y añade `&` para modificar en sitio: `for (auto& x : v) { x *= 2; }`. Sin el `&`
> modificas una copia y el vector nunca cambia.

> [!TIP]
> El range-for no puede darte el índice. Si la salida necesita numeración, usa el bucle con índice;
> no inventes un contador manual junto a un range-for.

---

**Siguiente:** [[29 - El Cómputo del Alquimista]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
