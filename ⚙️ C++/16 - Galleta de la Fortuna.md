# 16. Galleta de la Fortuna

**Versión original en inglés:** [16 - Fortune Cookie.md](./16%20-%20Fortune%20Cookie.md)

**Curso:** C++
**Tema:** Números aleatorios
**Etiquetas:** `#cpp` `#random` `#cstdlib`

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

A veces necesitamos un valor aleatorio para que los resultados sean más interesantes.

C++ tiene la función `std::rand()` (de **rand**om) en `<cstdlib>`, que genera un número
pseudoaleatorio. Debes `#include <cstdlib>` para usarla.

Para limitar el número a un rango, usa el operador `%` (que devuelve el resto). Por ejemplo,
`std::rand() % 10` limita el resultado a **0–9**.

## Sembrar el generador

Para que cada ejecución dé una secuencia distinta, **siembra** el generador antes de declarar la
variable:

```cpp
srand(time(NULL));
```

Esto requiere `#include <ctime>`. `time(NULL)` devuelve la hora actual en segundos, así que cada
ejecución parte de un punto distinto.

## Ejemplo

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int fortuna = std::rand() % 6;

  std::cout << "🥠 ";

  if (fortuna == 0) {
    std::cout << "No persigas la felicidad: créala.\n";
  } else if (fortuna == 1) {
    std::cout << "Todo es difícil antes de ser fácil.\n";
  } else if (fortuna == 2) {
    std::cout << "El madrugador atrapa el gusano, pero el segundo ratón se queda con el queso.\n";
  } else if (fortuna == 3) {
    std::cout << "Alguien en tu vida necesita una carta tuya.\n";
  } else if (fortuna == 4) {
    std::cout << "La fortuna que buscas está en otra galleta.\n";
  } else {
    std::cout << "¡Socorro! ¡Me tienen prisionero en una panadería!\n";
  }

  // Bonus: seis números de la suerte entre 0 y 50
  std::cout << "\nNúmeros de la suerte: "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << " "
            << std::rand() % 51 << "\n";
}
```

> [!NOTE]
> **`rand()` es una herramienta didáctica, no un RNG de calidad**
> Llama a `srand()` **una vez**, al inicio de `main()`. Llamarla antes de cada `rand()` resiembra con
> el mismo segundo y te devuelve el mismo número dos veces. El C++ moderno ofrece `<random>`
> (`std::mt19937`) cuando la calidad de la distribución importa de verdad.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
