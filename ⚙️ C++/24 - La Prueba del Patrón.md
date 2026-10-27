# 24. La Prueba del Patrón

**Versión original en inglés:** [24 - The Pattern Trial](./24%20-%20The%20Pattern%20Trial.md)

**Curso:** C++
**Capítulo:** 4 — Iteración
**Tema:** Repaso del capítulo 4: reglas que se solapan, evaluadas en orden
**Etiquetas:** `#cpp` `#recap` `#loops`

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

La última puerta del tutorial enciende una baliza en cada décimo de la carrera. La regla tiene tres
casos, y el tercero es la trampa: algunos pasos cumplen dos a la vez.

```cpp
#include <iostream>

int main() {
  for (int paso = 1; paso <= 15; paso++) {
    if (paso % 6 == 0) {
      std::cout << "FUEGO BRAVO\n";
    } else if (paso % 2 == 0) {
      std::cout << "Brasa\n";
    } else if (paso % 3 == 0) {
      std::cout << "Ceniza\n";
    } else {
      std::cout << paso << "\n";
    }
  }
}
```

## Salida

```text
1
Brasa
Ceniza
Brasa
5
FUEGO BRAVO
7
Brasa
Ceniza
Brasa
11
FUEGO BRAVO
13
Brasa
Ceniza
```

## Por qué `% 6` se comprueba primero

`6` es el mínimo común múltiplo de `2` y `3`. Cualquier paso divisible por ambos llega a
`FUEGO BRAVO` solo porque esa prueba va antes que las otras dos; baja una línea y el paso 6 imprime
`Brasa`, y `FUEGO BRAVO` no aparece nunca.

| Paso | `% 6` | `% 2` | `% 3` | Rama tomada |
| :--- | :--- | :--- | :--- | :--- |
| 6 | 0 | 0 | 0 | FUEGO BRAVO |
| 4 | 4 | 0 | 1 | Brasa |
| 9 | 3 | 1 | 0 | Ceniza |
| 7 | 1 | 1 | 1 | número |

> [!IMPORTANT]
> Aquí el orden no es una preferencia de estilo, es el algoritmo. Cuando las condiciones se solapan,
> gana la primera coincidencia y toda prueba posterior es código muerto para ese valor.

> [!TIP]
> Un bucle más una cadena de condiciones es la forma de la mitad de las reglas de un juego: estados
> alterados, tipos de daño, niveles de botín. Escribe primero la regla más específica y lee la salida
> en voz alta: un orden equivocado se oye de inmediato.

---

**Siguiente:** [[25 - La Alforja]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
