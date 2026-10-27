# 46. La Lente Dirección-De

**Versión original en inglés:** [46 - The Address-Of Lens](./46%20-%20The%20Address-Of%20Lens.md)

**Curso:** C++
**Capítulo:** 8 — Memoria
**Tema:** Punteros: tomar una dirección, desreferenciar y nulo
**Etiquetas:** `#cpp` `#pointers` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Un puntero es un número que nombra un lugar. `&` pide el lugar, `*` lee a través de él. Dos operadores,
una idea: el puntero no es el valor, es la etiqueta del estante.

```cpp
#include <iostream>

int main() {
  int vida = 30;
  int* asa = &vida;

  std::cout << "valor:      " << vida << "\n";
  std::cout << "dirección:  " << asa << "\n";
  std::cout << "a través:   " << *asa << "\n";

  *asa = 12;                // escribe vida, no una copia
  std::cout << "vida ahora: " << vida << "\n";

  int* nada = nullptr;
  std::cout << "¿nulo?      " << (nada == nullptr) << "\n";
  std::cout << "imprime nulo: " << nada << "\n";
}
```

## Salida

Una ejecución de ejemplo: tus direcciones serán distintas:

```text
valor:      30
dirección:  0x7ff7b6f0a5ac
a través:   30
vida ahora: 12
¿nulo?      1
imprime nulo: 0
```

## Los dos operadores

| Símbolo | Nombre | Significado |
| :--- | :--- | :--- |
| `&x` | dirección-de | un puntero a `x` |
| `*p` | desreferencia | el objeto al que apunta `p` |
| `int*` | tipo puntero | "puntero a int" |

`*` en una declaración significa "esto es un puntero". `*` en una expresión significa "ve allí". El
mismo glifo, dirección opuesta, y una de las pocas herencias genuinamente confusas de C++.

## `nullptr` es un valor, no una dirección

`nullptr` significa "no apunta a nada". Desreferenciarlo es comportamiento indefinido: normalmente
una caída, a veces algo peor. `std::cout << nullptr` está definido: imprime `0` por la sobrecarga de
`void*`.

> [!CAUTION]
> Un puntero al que nunca asignaste nada guarda basura, no `nullptr`. `int* p;` y luego `*p = 5;`
> escriben en una dirección aleatoria. Inicializa siempre: `int* p = nullptr;` o directo a un objeto
> real.

> [!TIP]
> `const int* p` no puede cambiar el valor; `int* const p` no puede cambiar el puntero. Lee la
> declaración de derecha a izquierda: "p es un puntero constante a int" frente a "p es un puntero a
> int constante".

---

**Siguiente:** [[47 - Asas a la Memoria]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
