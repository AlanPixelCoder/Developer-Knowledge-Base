# 14. Caminos Bifurcados

**Versión original en inglés:** [14 - Forked Roads](./14%20-%20Forked%20Roads.md)

**Curso:** C++
**Capítulo:** 3 — Decisiones
**Tema:** Flujo de control, y por qué hay que sembrar una tirada aleatoria
**Etiquetas:** `#cpp` `#control-flow` `#random`

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

Hasta ahora todos los programas corrían las mismas líneas en el mismo orden. El flujo de control
cambia eso: el guion tiene bifurcaciones y el programa recorre una de ellas.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int tirada = std::rand() % 6 + 1;   // de 1 a 6

  if (tirada >= 5) {
    std::cout << "golpe crítico: " << tirada << "\n";
  } else if (tirada >= 3) {
    std::cout << "golpe firme: " << tirada << "\n";
  } else {
    std::cout << "golpe débil: " << tirada << "\n";
  }
}
```

Tres posibles líneas de salida, una por rama, decididas en tiempo de ejecución.

## `srand` no es opcional

`std::rand()` es un **generador de secuencias**, no una fuente de caos. Sin semilla repite la misma
secuencia en cada ejecución: los mismos dados, en cada arranque, para siempre. `srand(time(NULL))` le
entrega el reloj para que cada sesión empiece en otro punto.

| Llamada | Efecto |
| :--- | :--- |
| `std::rand()` | Siguiente número de la secuencia actual |
| `srand(semilla)` | Reinicia la secuencia desde esa semilla |
| `srand(time(NULL))` | Reinicia desde el segundo actual |

> [!CAUTION]
> Sembrar con `time(NULL)` significa que dos ejecuciones **dentro del mismo segundo** obtienen
> secuencias idénticas. Eso es comportamiento correcto, no un fallo, pero explica por qué una prueba
> que corre dos veces seguidas parece trucada.

> [!NOTE]
> `rand()` y `srand()` vienen de C. El C++ moderno tiene `<random>` con `std::mt19937` y
> distribuciones de verdad; en [[17 - Dados Cargados]] está la diferencia de calidad. Usa `<random>`
> el día que los dados muevan algo que importe.

---

**Siguiente:** [[15 - Puertas y Llaves]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
