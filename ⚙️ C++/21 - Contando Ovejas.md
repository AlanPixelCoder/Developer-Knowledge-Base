# 21. Contando Ovejas

**Versión original en inglés:** [21 - Counting Sheep.md](./21%20-%20Counting%20Sheep.md)

**Curso:** C++
**Tema:** Bucles `for`
**Etiquetas:** `#cpp` `#loops` `#for` `#iteration`

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

Para recorrer un bloque de código un número concreto de veces, usa un bucle `for`.

Un bucle `for` tiene **tres partes** entre paréntesis, separadas por puntos y coma:

1. **Inicialización** — `int i = 0;` crea el contador.
2. **Condición** — `i < 6;` se comprueba antes de cada iteración.
3. **Cambio** — `i++` se ejecuta después de cada iteración.

```cpp
for (int i = 0; i < 6; i++) {
  // cuerpo
}
```

El contador arranca en su valor inicial. Si la condición es verdadera, el cuerpo se ejecuta. Luego
el contador cambia y el bucle repite hasta que la condición deja de ser verdadera.

## Orden de ejecución

| Paso | Qué ocurre |
| :--- | :--- |
| 1 | Inicialización — **una sola vez**, antes de todo |
| 2 | Condición — se comprueba; `false` sale del bucle |
| 3 | Cuerpo — se ejecuta |
| 4 | Cambio — `i++` |
| 5 | Vuelve al paso 2 |

## Ejemplo

```cpp
#include <iostream>

int main() {
  for (int i = 1; i <= 50; i++) {
    std::cout << i << " ovejas\n";
  }
}
```

> [!WARNING]
> **`<` vs `<=` es un off-by-one esperando**
> `i < 50` imprime 1–49. `i <= 50` imprime 1–50. Cuenta los elementos que realmente quieres antes de
> elegir la comparación: es el error de bucle más común que existe.

> [!TIP]
> `i++` es el operador de incremento. `i--` decrementa: el tema de [[22 - 99 Botellas]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
