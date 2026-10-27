# 10. Números que Mienten

**Versión original en inglés:** [10 - Numbers That Lie](./10%20-%20Numbers%20That%20Lie.md)

**Curso:** C++
**Capítulo:** 2 — Valores en Bruto
**Tema:** Aritmética, precedencia y división entera
**Etiquetas:** `#cpp` `#operators` `#arithmetic`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-2-7C5CFF?style=for-the-badge" alt="Chapter 2">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El registro de combate dice que un golpe hace **7 de daño** y que el jugador tiene **2 puntos de
armadura por golpe**. Cualquiera escribiría `7 / 2` esperando 3.5. C++ devuelve 3, y ese redondeo no
es un fallo: es la regla cuando ambos operandos son enteros.

```cpp
#include <iostream>

int main() {
  int danio = 7;
  int armadura_por_golpe = 2;

  std::cout << "división entera:  " << danio / armadura_por_golpe << "\n";
  std::cout << "división double:  " << danio / 2.0 << "\n";
  std::cout << "resto:            " << danio % armadura_por_golpe << "\n";
}
```

## Salida

```text
división entera:  3
división double:  3.5
resto:            1
```

No se redondeó nada: la parte fraccionaria se **descartó**, porque un `int` no tiene dónde guardarla.

## Precedencia, en el orden que importa

| Prioridad | Operadores | Nota |
| :--- | :--- | :--- |
| 1 | `()` | Los paréntesis ganan a todo: úsalos cuando dudes |
| 2 | `*` `/` `%` | De izquierda a derecha |
| 3 | `+` `-` | De izquierda a derecha |
| 4 | `=` `+=` `-=` | De derecha a izquierda |

`2 + 3 * 4` es 14, no 20. `(2 + 3) * 4` es 20. `%` es el resto, y solo acepta enteros.

> [!CAUTION]
> Un solo operando entero basta para contaminar toda la expresión: `danio / 2 * 1.5` calcula primero
> `danio / 2` como entero y luego multiplica. Convierte pronto: `danio / 2.0 * 1.5`.

> [!TIP]
> Lee `%` como "lo que sobra". `danio % armadura` te dice si el golpe fue absorbido del todo, y
> `% 2 == 0` es cómo preguntas si un número es par.

---

**Siguiente:** [[11 - Cámara de Eco]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
