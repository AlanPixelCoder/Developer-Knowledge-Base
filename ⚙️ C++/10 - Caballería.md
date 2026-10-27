# 10. Caballería

**Versión original en inglés:** [10 - Knighthood.md](./10%20-%20Knighthood.md)

**Curso:** C++
**Tema:** Encadenamiento de salida
**Etiquetas:** `#cpp` `#output` `#chaining`

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

En C++ podemos usar el **encadenamiento** para mostrar texto y una variable en una sola línea.

Encadenar es útil sobre todo porque produce código más conciso y legible. Lo hacemos con varios
operadores `<<` en una misma sentencia: cada `<<` pasa el flujo a la siguiente pieza.

```cpp
std::cout << "Levántate, " << nombre << ", caballero de los Siete Reinos.\n";
```

Se lee de izquierda a derecha: envía `"Levántate, "` a la pantalla, luego `nombre`, luego el resto.

## Ejemplo

```cpp
#include <iostream>

int main() {
  std::string nombre = "Brienne";

  std::cout << "En el nombre del Guerrero, te ordeno ser valiente.\n";
  std::cout << "En el nombre del Padre, te ordeno ser justo.\n";
  std::cout << "En el nombre de la Madre, te ordeno defender al inocente.\n";
  std::cout << "Levántate, " << nombre << ", caballero de los Siete Reinos.\n";
}
```

> [!TIP]
> Encadena los espacios explícitamente (`"Levántate, "` con espacio final) en lugar de confiar en
> que `std::cout` añada separación. Nunca la añade: por eso la salida encadenada acaba como
> `Levántate,Brienne,caballero`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
