# 13. Lanzamiento de Moneda

**Versión original en inglés:** [13 - Coin Flip.md](./13%20-%20Coin%20Flip.md)

**Curso:** C++
**Tema:** Introducción al flujo de control y la lógica
**Etiquetas:** `#cpp` `#logic` `#control-flow` `#random`

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

Hasta ahora los programas C++ se ejecutan línea a línea, de arriba hacia abajo, dando siempre el
mismo resultado. A veces queremos que el programa haga cosas **distintas** según la situación. Así
es como los programas "toman decisiones": evaluando condiciones para introducir lógica.

El **flujo de control** es el orden en que se ejecuta el código. Las ramas (`if`), los bucles y las
llamadas a funciones son flujo de control.

## Simulación de lanzamiento de moneda

- El 50% de las veces muestra "Cara".
- El 50% de las veces muestra "Cruz".

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
  srand(time(NULL));

  int num = std::rand() % 2; // 0 o 1

  if (num > 0.5) {
    std::cout << "Cara\n";
  } else {
    std::cout << "Cruz\n";
  }
}
```

> [!WARNING]
> **La trampa que vale la pena notar**
> `num` es un `int` y `0.5` es un `double`, así que el compilador convierte `num` antes de comparar:
> `1 > 0.5` es verdadero y `0 > 0.5` es falso. La salida es correcta, pero la expresión miente sobre
> lo que significa: se lee como "más de la mitad" cuando en realidad dice "igual a uno". Escribe
> `if (num == 1)` y la intención queda a la vista. Mantén las comparaciones entre enteros.

> [!NOTE]
> `srand(time(NULL))` siembra el generador con el reloj actual para que cada ejecución difiera. Sin
> eso, cada arranque produce la misma secuencia. Ver [[16 - Galleta de la Fortuna]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
