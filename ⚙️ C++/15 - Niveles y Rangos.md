# 15. Niveles y Rangos

**Versión original en inglés:** [15 - Levels & Ranks.md](./15%20-%20Levels%20%26%20Ranks.md)

**Curso:** C++
**Tema:** Operadores relacionales y `else if`
**Etiquetas:** `#cpp` `#operators` `#else-if`

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

## Operadores relacionales

Para comparar dos valores dentro de condiciones usamos operadores relacionales:

| Operador | Significado |
| :--- | :--- |
| `==` | igual a |
| `!=` | distinto de |
| `>` | mayor que |
| `<` | menor que |
| `>=` | mayor o igual que |
| `<=` | menor o igual que |

> [!WARNING]
> `=` asigna; `==` compara. `if (x = 5)` compila, asigna 5 a `x` y siempre es `true`. Es el clásico
> error de C++ — activa las advertencias del compilador y te lo marcará.

## La sentencia `else if`

Se pueden añadir uno o más `else if` entre el `if` y el `else` para comprobar condiciones
adicionales. Solo **una** rama se ejecutará: la primera cuya condición sea `true`. El orden importa;
las comprobaciones van de arriba hacia abajo.

```cpp
#include <iostream>

int main() {
  int nivel = 14;

  if (nivel >= 21) {
    std::cout << "Diamante\n";
  } else if (nivel >= 16) {
    std::cout << "Platino\n";
  } else if (nivel >= 11) {
    std::cout << "Oro\n";
  } else if (nivel >= 6) {
    std::cout << "Plata\n";
  } else {
    std::cout << "Bronce\n";
  }
}
// Salida: Oro
```

> [!TIP]
> **Ordena de lo más estricto a lo más laxo**
> Como solo se ejecuta la primera coincidencia, `nivel >= 21` debe ir antes que `nivel >= 16`. Al
> revés, a un jugador de nivel 25 le dirían que es Bronce.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
