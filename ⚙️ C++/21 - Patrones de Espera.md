# 21. Patrones de Espera

**Versión original en inglés:** [21 - Holding Patterns](./21%20-%20Holding%20Patterns.md)

**Curso:** C++
**Capítulo:** 4 — Iteración
**Tema:** El bucle while y una condición que cambia
**Etiquetas:** `#cpp` `#while` `#loops`

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

La linterna arde mientras tenga aceite. Sin número fijo, sin final conocido: solo una condición que
es verdadera hasta que deja de serlo.

```cpp
#include <iostream>

int main() {
  double aceite = 3.0;
  int minutos = 0;

  while (aceite > 0.0) {
    aceite -= 0.75;
    minutos++;
    if (aceite < 0.0) {
      aceite = 0.0;  // nunca mostrar combustible negativo en el HUD
    }
    std::cout << "minuto " << minutos << ": aceite " << aceite << "\n";
  }

  std::cout << "oscuridad tras " << minutos << " minutos\n";
}
```

## Salida

```text
minuto 1: aceite 2.25
minuto 2: aceite 1.5
minuto 3: aceite 0.75
minuto 4: aceite 0
oscuridad tras 4 minutos
```

## `while` en una frase

Repite el cuerpo **mientras** la condición sea verdadera; comprueba antes de cada pasada, incluida la
primera. Si la condición empieza falsa, el cuerpo nunca corre.

| Situación | Bucle que encaja |
| :--- | :--- |
| Número de pasadas desconocido | `while` |
| Al menos una pasada, y quizá más | `do ... while` |
| Conteo conocido, o recorrer un rango | `for` (siguiente lección) |

## El recorte importa

`aceite -= 0.75` se pasa: tras cuatro pasadas el valor real es `0.0`, pero con otros números puede
quedar negativo. A la coma flotante le importa; un HUD que muestra `-0.25` parece roto aunque el
bucle sea correcto.

> [!WARNING]
> `while (aceite > 0.0)` con `aceite` sin modificar es un bucle infinito, y el programa imprime sin
> parar. Antes de escribir la condición, escribe la línea que la hará falsa.

> [!TIP]
> `minutos` existe solo para explicar la corrida. El código real imprimiría el combustible, no el
> contador, pero un contador es la forma más barata de ver cuántas pasadas hizo un `while`.

---

**Siguiente:** [[22 - Tic a Tic]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
