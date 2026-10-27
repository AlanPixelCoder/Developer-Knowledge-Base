# 02. ¡Howdy!

**Versión original en inglés:** [02 - Howdy!.md](./02%20-%20Howdy%21.md)

**Curso:** C++
**Tema:** Salida de texto, `std::cout` y sintaxis básica
**Etiquetas:** `#cpp` `#output` `#syntax`

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

En C++, la sentencia `std::cout` (abreviatura de **c**haracter **out**put, se pronuncia
"see-out") le dice a la terminal que muestre un mensaje.

## Anatomía de una sentencia de salida

| Pieza | Significado |
| :--- | :--- |
| **`std::cout`** | Indica al programa que muestre un mensaje |
| **`<<`** | Dos flechas a la izquierda: el operador de inserción |
| **`""`** | El mensaje va entre comillas dobles |
| **`;`** | Toda sentencia de C++ termina con punto y coma |

El texto que aparece en la terminal se llama **salida** (output).

```cpp
// Howdy 🤠
// Registro de arranque de Emberfall

#include <iostream>

int main() {
  std::cout << "Emberfall v1.0 — servidores en línea";
}
```

> [!TIP]
> Olvida el punto y coma y el compilador se niega a ejecutar. Es el error más común del primer
> día — y el más rápido de arreglar.

> [!NOTE]
> **Qué significa `std::`**
> `cout` vive en la **biblioteca estándar**, expuesta bajo el espacio de nombres `std`. Escribir
> `std::cout` es decir "el `cout` que pertenece a `std`". Un `using namespace std;` permitiría
> quitar el prefijo, pero este módulo lo mantiene explícito: es el hábito que escala.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
