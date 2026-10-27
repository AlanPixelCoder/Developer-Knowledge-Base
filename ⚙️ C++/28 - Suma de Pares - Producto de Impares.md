# 28. Suma de Pares - Producto de Impares

**Versión original en inglés:** [28 - Sum of Even - Product of Odd.md](./28%20-%20Sum%20of%20Even%20-%20Product%20of%20Odd.md)

**Curso:** C++
**Tema:** Repaso del capítulo 5 y problema de lógica
**Etiquetas:** `#cpp` `#recap` `#vectors` `#logic` `#loops`

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

## Repaso del capítulo 5

- Los vectores almacenan varios elementos del mismo tipo en una sola variable.
- Un índice es la posición de un elemento dentro de un vector.
- Los vectores de C++ son base 0.
- Los vectores tienen métodos: `.push_back()`, `.pop_back()`, `.size()`.
- Iteramos un vector con un bucle `for` y `.size()` como límite.

## Problema de lógica

Escribe un programa que use un bucle `for` para recorrer un vector de números y calcular la **suma de
los pares** y el **producto de los impares**.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> num = {2, 4, 3, 6, 1, 9, 8, 0, 8, 5, 7, 3, 3};

  int suma_par = 0;
  int producto_impar = 1;

  for (int i = 0; i < num.size(); i++) {
    if (num[i] % 2 == 0) {
      suma_par += num[i];
    } else {
      producto_impar *= num[i];
    }
  }

  std::cout << "La suma de los pares: " << suma_par << "\n";
  std::cout << "El producto de los impares: " << producto_impar << "\n";
}
```

> [!IMPORTANT]
> **Los valores identidad importan**
> Una suma empieza en `0` (sumar nada no cambia nada). Un producto empieza en `1` (multiplicar por
> uno no cambia nada). Empezar `producto_impar` en `0` aniquilaría cualquier resultado a `0`.

> [!TIP]
> `suma_par += num[i]` es la forma corta de `suma_par = suma_par + num[i]`. Los operadores `*=`,
> `-=` y `/=` funcionan exactamente igual.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
