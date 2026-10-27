# 22. Tic a Tic

**Versión original en inglés:** [22 - Tick by Tick](./22%20-%20Tick%20by%20Tick.md)

**Curso:** C++
**Capítulo:** 4 — Iteración
**Tema:** El bucle for: inicio, fin, paso
**Etiquetas:** `#cpp` `#for` `#loops`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

La simulación del motor avanza en ticks fijos. Sesenta por segundo, y cada tick tiene un número: eso
es un bucle `for` con tres datos en una línea.

```cpp
#include <iostream>

int main() {
  const int TICKS = 5;

  for (int tick = 1; tick <= TICKS; tick++) {
    std::cout << "tick " << tick << " de " << TICKS << "\n";
  }

  std::cout << "simulación detenida\n";
}
```

## Salida

```text
tick 1 de 5
tick 2 de 5
tick 3 de 5
tick 4 de 5
tick 5 de 5
simulación detenida
```

## Las tres cláusulas

| Cláusula | Aquí | Cuándo se ejecuta |
| :--- | :--- | :--- |
| Inicialización | `int tick = 1` | Una vez, antes del bucle |
| Condición | `tick <= TICKS` | Antes de cada pasada |
| Incremento | `tick++` | Después de cada pasada |

Se lee así: *empieza en 1, sigue mientras no pase de 5, suma uno cada vez.*

## `<=` frente a `<`

Ambos son correctos, con contadores distintos:

| Escrito | Pasadas | Último valor |
| :--- | :--- | :--- |
| `tick = 1; tick <= 5` | 5 | 5 |
| `tick = 0; tick < 5` | 5 | 4 |

Elige uno y mantenlo. La segunda forma es la que usarás para indexar un vector, porque los índices de
un contenedor empiezan en cero.

> [!CAUTION]
> `tick <= TICKS` con `tick` empezando en `0` corre **seis** veces. El bucle no está mal: el par
> (inicio, comparación) sí. Imprime el contador en la primera y en la última pasada siempre que la
> cuenta importe.

> [!TIP]
> Un `for` es un `while` con el trabajo repetitivo movido a la cabecera. Si necesitas el contador
> después de terminar, declara `tick` fuera de la cabecera: dentro, desaparece en la llave de cierre.

---

**Siguiente:** [[23 - Protocolo de Cuenta Atrás]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
