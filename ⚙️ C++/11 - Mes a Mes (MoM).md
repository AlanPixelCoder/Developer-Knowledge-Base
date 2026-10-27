# 11. Mes a Mes (MoM)

**Versión original en inglés:** [11 - Month-over-Month (MoM).md](./11%20-%20Month-over-Month%20%28MoM%29.md)

**Curso:** C++
**Tema:** Entrada de usuario (`std::cin`)
**Etiquetas:** `#cpp` `#input` `#cin`

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

Para obtener entrada del usuario, C++ usa la sentencia `std::cin`.

- `cin` viene de **c**haracter **in**put y se refiere al flujo de entrada estándar.
- Va seguido del operador `>>` y de la variable donde guardar.

En la terminal el usuario escribe su respuesta y pulsa `enter`. Lo que haya escrito se guarda en la
variable.

> [!IMPORTANT]
> Debes **declarar** la variable antes de usarla para guardar entrada. `std::cin >> x;` con una `x`
> sin declarar no compila.

## `cin` vs `cout`

| | Operador | Dirección | Destino |
| :--- | :--- | :--- | :--- |
| `std::cout` | `<<` | Programa → pantalla | Un valor |
| `std::cin` | `>>` | Teclado → programa | Una variable |

Las flechas siempre apuntan **hacia el destino**.

## Ejemplo

```cpp
#include <iostream>

int main() {
  double mes1;
  double mes2;

  std::cout << "Ingresa el mes 1: ";
  std::cin >> mes1;

  std::cout << "Ingresa el mes 2: ";
  std::cin >> mes2;

  double mom = ((mes2 - mes1) / mes1) * 100;

  std::cout << "Cambio mes a mes: " << mom << "%";
}
```

> [!NOTE]
> La fórmula: $\text{MoM} = \dfrac{\text{mes}_2 - \text{mes}_1}{\text{mes}_1} \times 100$.
> Un resultado positivo es crecimiento; uno negativo, caída.

> [!WARNING]
> `std::cin` corta en el primer espacio. Escribir `1.000` lee `1` y deja `,000` en el búfer para la
> siguiente lectura. Números completos, uno por pregunta.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
