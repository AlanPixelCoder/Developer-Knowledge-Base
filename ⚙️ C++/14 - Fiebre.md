# 14. Fiebre

**Versión original en inglés:** [14 - Fever.md](./14%20-%20Fever.md)

**Curso:** C++
**Tema:** Sentencias `if` y `else`
**Etiquetas:** `#cpp` `#conditionals` `#if-else`

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

## La sentencia `if`

Una sentencia `if` comprueba si una condición es verdadera:

- Si la condición es `true`, el código del bloque `if` se ejecuta.
- Si es `false`, el bloque se salta.

El código "dentro" del `if` debe ir indentado (normalmente dos espacios).

```cpp
if (temp >= 100) {
  std::cout << "Tienes fiebre.\n";
}
```

## La cláusula `else`

Una cláusula `else` puede ir opcionalmente después de un `if`:

- Condición `true` → se ejecuta el bloque del `if`.
- Condición `false` → se ejecuta el bloque del `else`.

Siempre se ejecuta exactamente una de las dos. No hay camino donde corran ambas, ni camino donde no
corra ninguna.

```cpp
#include <iostream>

int main() {
  double temp = 98.6;

  if (temp >= 100) {
    std::cout << "Tienes fiebre. 🤒\n";
  } else {
    std::cout << "No tienes fiebre. 🌡️\n";
  }
}
```

> [!TIP]
> **Las llaves no son opcionales en la práctica**
> C++ permite escribir un `if` sin llaves para una sola sentencia. No lo hagas. El día que añadas
> una segunda línea a ese bloque, solo la primera seguirá siendo condicional — y el error es
> invisible.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
