# 17. Votación

**Versión original en inglés:** [17 - Voting.md](./17%20-%20Voting.md)

**Curso:** C++
**Tema:** Operadores lógicos
**Etiquetas:** `#cpp` `#logic` `#operators` `#boolean`

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

Los operadores lógicos, también llamados booleanos, combinan y evalúan dos condiciones:

| Operador | Nombre | Resultado |
| :--- | :--- | :--- |
| `&&` | and (y) | `true` solo si **ambos** lados son `true` |
| `||` | or (o) | `true` si **al menos uno** es `true` |
| `!` | not (no) | invierte `true` ↔ `false` |

## Tabla de verdad

| A | B | `A && B` | `A || B` |
| :--- | :--- | :--- | :--- |
| true | true | true | true |
| true | false | false | true |
| false | true | false | true |
| false | false | false | false |

## Ejemplo

```cpp
#include <iostream>

int main() {
  int edad = 31;
  bool ciudadano = true;
  bool registrado = true;

  if (edad >= 18 && ciudadano && registrado) {
    std::cout << "¡Puedes votar!\n";
  } else if (edad < 18) {
    std::cout << "No tienes edad para votar.\n";
  } else if (!ciudadano) {
    std::cout << "No eres elegible para votar.\n";
  } else if (!registrado) {
    std::cout << "Necesitas registrarte primero.\n";
  } else {
    std::cout << "No cumples los requisitos.\n";
  }
}
```

> [!TIP]
> **Evaluación de cortocircuito**
> C++ deja de evaluar una cadena `&&` en el primer `false`, y una cadena `||` en el primer `true`.
> Eso permite escribir `if (ptr != nullptr && *ptr == 42)` con seguridad: la desreferencia nunca
> ocurre si la comprobación falla. Ver [[44 - Nullptr]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
