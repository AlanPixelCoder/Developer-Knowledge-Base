# 12. Años Gato

**Versión original en inglés:** [12 - Cat Years.md](./12%20-%20Cat%20Years.md)

**Curso:** C++
**Tema:** Repaso del capítulo 2 y aplicación
**Etiquetas:** `#cpp` `#recap` `#input` `#math`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

## Repaso del capítulo 2

- **Tipos de datos:** `int`, `double`, `char`, `std::string`, `bool`.
- **Operadores aritméticos:** `+`, `-`, `*`, `/`.
- **El `%` módulo** devuelve el resto.
- **Encadenar** escribe varias salidas en una sola sentencia con `<<`.
- **`std::cin`** lee entrada del usuario en una variable declarada.

## Ejemplo

Los dos primeros años de un gato equivalen a 24 años humanos; cada año siguiente cuenta como unos
4.

```cpp
#include <iostream>

int main() {
  int gato;
  int humano;

  std::cout << "¡Bienvenido al programa Años Gato! Solo funciona con gatos mayores de 2 años.\n";
  std::cout << "Ingresa la edad de tu gato: ";
  std::cin >> gato;

  humano = (gato - 2) * 4 + 24;

  std::cout << "Tu gato tiene " << humano << " años en años humanos.\n";
}
```

> [!TIP]
> **Cuida el caso límite**
> Con menos de 2 años la fórmula se vuelve negativa: un gatito de un mes saldría como "−16 años
> humanos". Añade un `if (gato < 2)` cuando llegues a [[14 - Fiebre]] y el programa dejará de
> mentirle a su usuario.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
