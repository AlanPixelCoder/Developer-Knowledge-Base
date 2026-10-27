# 19. Prueba de Preguntas

**Versión original en inglés:** [19 - Trial by Question](./19%20-%20Trial%20by%20Question.md)

**Curso:** C++
**Capítulo:** 3 — Decisiones
**Tema:** Repaso del capítulo 3: un cuestionario con puntuación hecho de ramas
**Etiquetas:** `#cpp` `#recap` `#control-flow`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-3-7C5CFF?style=for-the-badge" alt="Chapter 3">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El tutorial del motor termina con tres preguntas. Cada respuesta correcta suma un punto y se aprueba
con dos de tres: un programa entero hecho con las ramas de este capítulo.

```cpp
#include <iostream>

int main() {
  const int RESPUESTA_1 = 3;
  const int RESPUESTA_2 = 1;
  const int RESPUESTA_3 = 4;

  int dada_1 = 3;
  int dada_2 = 2;
  int dada_3 = 4;

  int puntaje = 0;

  if (dada_1 == RESPUESTA_1) puntaje++;
  if (dada_2 == RESPUESTA_2) puntaje++;
  if (dada_3 == RESPUESTA_3) puntaje++;

  std::cout << "puntaje: " << puntaje << "/3\n";

  if (puntaje == 3) {
    std::cout << "rango: archivero\n";
  } else if (puntaje == 2) {
    std::cout << "rango: aprendiz\n";
  } else {
    std::cout << "rango: visitante\n";
  }

  std::cout << "porcentaje: " << 100.0 * puntaje / 3 << "%\n";
}
```

## Salida

```text
puntaje: 2/3
rango: aprendiz
porcentaje: 66.6667%
```

## Tres `if` separados, a propósito

| Escrito | Comportamiento |
| :--- | :--- |
| Tres sentencias `if` | Cada pregunta se comprueba de forma independiente |
| Una cadena `else if` | Solo puntuaría la primera respuesta correcta |

La cadena de [[16 - Rangos y Umbrales]] es correcta para rangos excluyentes e incorrecta para una
cuenta acumulada.

> [!NOTE]
> En el tutorial real los tres valores `dada_` vienen de `std::cin`. Fijarlos aquí mantiene el
> ejemplo ejecutable sin teclear, y nada más de la lógica cambia.

> [!TIP]
> `100.0 * puntaje / 3` conserva la fracción; `100 * puntaje / 3` imprimiría `66` con el mismo
> puntaje. El `3` coincide con el número de preguntas: una constante con nombre ahí te salva de una
> nota equivocada cuando se añada una cuarta pregunta.

---

**Siguiente:** [[20 - El Bucle que Espera]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
