# 13. Escalado de Niveles

**Versión original en inglés:** [13 - Level Scaling](./13%20-%20Level%20Scaling.md)

**Curso:** C++
**Capítulo:** 2 — Valores en Bruto
**Tema:** Repaso del capítulo 2: una fórmula con caso límite
**Etiquetas:** `#cpp` `#recap` `#arithmetic`

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

El motor convierte la experiencia total en un nivel y una barra de progreso. Tres valores, una
fórmula y un caso límite que decide si la interfaz muestra una barra o un hueco vacío.

```cpp
#include <iostream>

int main() {
  int xp = 2450;
  int xp_por_nivel = 300;

  int nivel = xp / xp_por_nivel;
  int xp_en_nivel = xp % xp_por_nivel;
  double progreso = 100.0 * xp_en_nivel / xp_por_nivel;

  std::cout << "xp: " << xp << "\n";
  std::cout << "nivel: " << nivel << "\n";
  std::cout << "dentro del nivel: " << xp_en_nivel << "\n";
  std::cout << "progreso: " << progreso << "%\n";
}
```

## Salida

```text
xp: 2450
nivel: 8
dentro del nivel: 50
progreso: 16.6667%
```

## Por qué funcionan las tres líneas

| Expresión | Tipo | Por qué ese tipo |
| :--- | :--- | :--- |
| `xp / xp_por_nivel` | `int` | Los niveles se cuentan en pasos completos |
| `xp % xp_por_nivel` | `int` | Lo que queda dentro del nivel actual |
| `100.0 * ...` | `double` | `100.0` obliga a la división a conservar la fracción |

## El caso límite

```cpp
#include <iostream>

int main() {
  int xp = 120;
  int xp_por_nivel = 300;

  std::cout << "nivel: " << xp / xp_por_nivel << "\n";
  std::cout << "progreso: " << 100.0 * (xp % xp_por_nivel) / xp_por_nivel << "%\n";
}
```

```text
nivel: 0
progreso: 40%
```

Un personaje recién creado es nivel **0**, que es aritmética correcta e interfaz incorrecta.
Protégelo:

```cpp
int nivel = 1 + xp / xp_por_nivel;
```

> [!CAUTION]
> `xp_por_nivel` no puede ser cero: dividir enteros entre cero es comportamiento indefinido, y el
> programa puede caerse, imprimir basura o parecer que funciona. Valida los valores de configuración
> antes de dividir por ellos.

> [!NOTE]
> `100.0 * xp_en_nivel / xp_por_nivel` conserva la fracción porque la multiplicación ocurre primero,
> de izquierda a derecha. Escrito `100 * (xp_en_nivel / xp_por_nivel)`, la división interna sería
> entera y el resultado `0`.

---

**Siguiente:** [[14 - Caminos Bifurcados]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
