# 20. Adivina el Número

**Versión original en inglés:** [20 - Guess the Number.md](./20%20-%20Guess%20the%20Number.md)

**Curso:** C++
**Tema:** Bucles `while`
**Etiquetas:** `#cpp` `#loops` `#while` `#iteration`

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

Un bucle `while` se parece mucho a una sentencia `if`. Igual que un `if`, ejecuta su código cuando la
condición es `true`. La diferencia: el `while` ejecuta el código *una y otra vez* mientras la
condición siga siendo `true`.

En lugar de ejecutarse una vez si la condición es verdadera, se ejecuta de nuevo y de nuevo mientras
lo sea.

Al inicio de cada pasada se vuelve a comprobar la condición. En el momento en que se vuelve `false`,
el programa sale del bucle y continúa en la línea siguiente.

> [!NOTE]
> Si la condición era `false` desde el principio, el bloque nunca se ejecuta: el bucle se salta por
> completo. Un `while` puede ejecutarse **cero** veces; es parte del diseño.

## Ejemplo

```cpp
#include <iostream>

int main() {
  int intento = 0;
  int respuesta = 64;

  std::cout << "Adivina el número: ";
  std::cin >> intento;

  while (intento != respuesta) {
    std::cout << "Adivina el número: ";
    std::cin >> intento;
  }

  std::cout << "¡Lo adivinaste!\n";
}
```

El primer intento se lee antes del bucle para que la condición tenga algo que comprobar. Cada intento
fallido vuelve a leer dentro del bucle: esa relectura es lo que finalmente hace falsa la condición.

> [!TIP]
> **El bucle siempre termina. Tarde o temprano.**
> La única salida es acertar. En un juego real añadirías un contador de intentos y un `break`, que
> llegan en los próximos capítulos.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
