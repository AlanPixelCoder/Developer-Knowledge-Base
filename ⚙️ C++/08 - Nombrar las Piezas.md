# 08. Nombrar las Piezas

**Versión original en inglés:** [08 - Naming the Parts](./08%20-%20Naming%20the%20Parts.md)

**Curso:** C++
**Capítulo:** 2 — Valores en Bruto
**Tema:** Declarar variables, nombres válidos y convenciones de nombres
**Etiquetas:** `#cpp` `#variables` `#style`

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

Una declaración le dice tres cosas al compilador a la vez: el tipo, el nombre y — si lo inicializas —
el valor de partida. Si omites lo tercero, C++ te entrega lo que ya hubiera en esa memoria.

```cpp
#include <iostream>

int main() {
  int ticks_por_segundo = 60;             // un valor, un propósito
  double gravedad = 9.81;                 // sin sufijo para double
  char dificultad = 'H';                  // comillas simples: un carácter
  bool vsync_activo = true;               // true / false en minúsculas
  std::string nombre_motor = "Emberfall"; // comillas dobles: texto

  std::cout << nombre_motor << " | ticks " << ticks_por_segundo << "\n";
  std::cout << "gravedad " << gravedad << " | dificultad " << dificultad << "\n";
  std::cout << "vsync " << vsync_activo << "\n";
}
```

## Qué puede y qué no puede ser un nombre

| Regla | Válido | Inválido |
| :--- | :--- | :--- |
| Letras, dígitos, guion bajo | `tasa_aparicion_2` | `tasa-aparicion` |
| No puede empezar por dígito | `nivel2` | `2nivel` |
| Distingue mayúsculas | `Nivel` ≠ `nivel` | — |
| Sin palabras reservadas | `valor` | `int`, `class`, `return` |

## Dos convenciones que mantienen legible el motor

| Convención | Se ve así | Se usa para |
| :--- | :--- | :--- |
| `snake_case` | `tasa_aparicion` | variables y funciones |
| `PascalCase` | `TablaAparicion` | tipos y clases |

## Salida

```text
Emberfall | ticks 60
gravedad 9.81 | dificultad H
vsync 1
```

> [!NOTE]
> `bool` se imprime como `1` y `0` salvo que pidas `std::boolalpha` antes. El valor sigue siendo un
> booleano real; solo cambia el formato.

> [!WARNING]
> `Nivel` y `nivel` son dos variables distintas. Es legal, compila limpio, y es la forma más rápida
> de pasar una tarde depurando un valor que nunca cambia.

---

**Siguiente:** [[09 - Entra, Procesa, Sale]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
