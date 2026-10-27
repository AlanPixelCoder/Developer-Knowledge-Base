# 16. Rangos y Umbrales

**Versión original en inglés:** [16 - Tiers and Thresholds](./16%20-%20Tiers%20and%20Thresholds.md)

**Curso:** C++
**Capítulo:** 3 — Decisiones
**Tema:** Operadores relacionales y la cadena de else if
**Etiquetas:** `#cpp` `#comparisons` `#else-if`

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

El gremio clasifica a los jugadores por reputación: ceniza, chispa, forja, brasa. Cuatro rangos, tres
umbrales y una cadena de `else if` que debe ir del listón más alto al más bajo.

```cpp
#include <iostream>

int main() {
  int reputacion = 640;

  if (reputacion >= 900) {
    std::cout << "rango: brasa\n";
  } else if (reputacion >= 600) {
    std::cout << "rango: forja\n";
  } else if (reputacion >= 300) {
    std::cout << "rango: chispa\n";
  } else {
    std::cout << "rango: ceniza\n";
  }
}
```

## Salida

```text
rango: forja
```

## Los seis operadores de comparación

| Operador | Pregunta | `640` frente a `600` |
| :--- | :--- | :--- |
| `>` | estrictamente mayor | verdadero |
| `>=` | mayor o igual | verdadero |
| `<` | estrictamente menor | falso |
| `<=` | menor o igual | falso |
| `==` | igual | falso |
| `!=` | distinto | verdadero |

## Por qué el orden decide la respuesta

`else if` se detiene en la primera condición verdadera. Escrito al revés —`>= 300` primero— una
reputación de 640 coincide con *chispa* y la cadena termina ahí, así que `brasa` se vuelve
inalcanzable para todos los que pasan de 300.

> [!WARNING]
> Pon primero la condición más restrictiva. Una cadena de `else if` no es un conjunto de
> comprobaciones independientes: es una lista de preguntas hechas en orden hasta que una dice sí.

> [!TIP]
> Si los rangos viven en datos —una tabla de `{umbral, nombre}`— un bucle sobre ella sustituye la
> cadena entera. Tendrás las herramientas en [[25 - La Alforja]].

---

**Siguiente:** [[17 - Dados Cargados]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
