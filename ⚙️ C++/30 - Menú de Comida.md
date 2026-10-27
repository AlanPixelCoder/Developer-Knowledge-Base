# 30. Menú de Comida

**Versión original en inglés:** [30 - Food Menu.md](./30%20-%20Food%20Menu.md)

**Curso:** C++
**Tema:** Definir y llamar funciones
**Etiquetas:** `#cpp` `#functions` `#void`

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

Las **funciones definidas por el usuario** son funciones que creamos nosotros para una tarea
concreta. Es un proceso de dos pasos:

1. **Definir** la función.
2. **Llamar** la función.

## Definir una función

Una definición empieza con la palabra clave `void`, seguida del nombre de la función y un par de
paréntesis `()`. El código de dentro es el **cuerpo**, entre llaves y con sangría.

```cpp
void buzon_voz() {
  std::cout << "¡Hola! Has llamado a Bob's Burgers.\n";
}
```

`void` significa "esta función no devuelve nada": hace el trabajo y no entrega ningún valor.

> [!NOTE]
> La convención clásica para funciones es `snake_case`, aunque `camelCase` moderno también vale.
> Elige una por proyecto.

## Llamar una función

Definir una función la crea, pero C++ no la ejecuta automáticamente. Para ejecutar el cuerpo la
**llamamos**: el nombre seguido de `()`, normalmente dentro de `main()`.

```cpp
#include <iostream>

void bienvenida() {
  std::cout << "¡Bienvenido a la Taberna del Escudero Pixel!\n\n";
  std::cout << "Este es el menú:\n";
  std::cout << "1. 🍗 Pierna asada\n";
  std::cout << "2. 🍚 Arroz jazmín\n";
  std::cout << "3. 🧪 Poción de vida\n";
  std::cout << "4. ☕ Espresso triple\n";
  std::cout << "5. 🍪 Galleta de viaje\n\n";
}

int main() {
  bienvenida(); // primera llamada
  bienvenida(); // segunda llamada — mismo cuerpo, cero código duplicado
}
```

> [!IMPORTANT]
> **El orden importa**
> Una función debe estar *declarada o definida* antes de la línea que la llama. Pon las definiciones
> encima de `main()` o añade un **prototipo** (`void bienvenida();`) arriba y define el cuerpo
> después.

> [!TIP]
> Esto es DRY en su forma más simple: dos llamadas, un cuerpo. Cambia el menú una vez y ambas
> impresiones se actualizan.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
