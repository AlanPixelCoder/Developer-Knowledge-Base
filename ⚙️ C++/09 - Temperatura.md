# 09. Temperatura

**Versión original en inglés:** [09 - Temperature.md](./09%20-%20Temperature.md)

**Curso:** C++
**Tema:** Operadores aritméticos
**Etiquetas:** `#cpp` `#math` `#operators`

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

Las computadoras son increíbles haciendo cálculos. C++ tiene estos operadores aritméticos:

| Operador | Operación | Nota |
| :--- | :--- | :--- |
| `+` | Suma | |
| `-` | Resta | |
| `*` | Multiplicación | |
| `/` | División | Con dos `int` trunca los decimales |
| `%` | Módulo | Devuelve el **resto**; solo con enteros |

En C++ los paréntesis tienen la mayor prioridad. Podemos usarlos para calcular el total en una sola
línea de código.

## Precedencia de operadores

1. `( )` — paréntesis
2. `*`, `/`, `%` — de izquierda a derecha
3. `+`, `-` — de izquierda a derecha

## Ejemplo

```cpp
#include <iostream>

int main() {
  double fahrenheit = 65.0;
  double celsius = (fahrenheit - 32) / 1.8;

  std::cout << celsius; // Salida: 18.3333
}
```

> [!WARNING]
> **La trampa de la división entera**
> `5 / 2` es `2`, no `2.5`, porque ambos operandos son `int`. Escribe `5.0 / 2` (o convierte) cuando
> quieras la fracción. Este único error ha hundido más de un conversor de temperatura.

> [!TIP]
> La fórmula: $C = (F - 32) \div 1.8$ — y la inversa $F = C \times 1.8 + 32$.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
