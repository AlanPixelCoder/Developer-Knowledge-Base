# 45. El Fin

**Versión original en inglés:** [45 - The End.md](./45%20-%20The%20End.md)

**Curso:** C++
**Tema:** Repaso del capítulo 8
**Etiquetas:** `#cpp` `#recap` `#pointers` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-AVANZADO-E74C3C?style=for-the-badge" alt="Avanzado">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

## Repaso del capítulo 8

Aprendimos que:

- Una **dirección de memoria** es una secuencia única que localiza bytes en la memoria.
- Los **punteros** son variables especiales que guardan la dirección de otra variable.
- Las **referencias** son alias de otra variable, no una variable nueva.
- **`nullptr`** representa un puntero que no apunta a ninguna dirección.

## Todo el curso en una tabla

| Capítulo | Concepto | Firma |
| :--- | :--- | :--- |
| 1 | Salida y estructura | `std::cout`, `main()`, `//`, `\n` |
| 2 | Datos y matemáticas | `int`, `double`, `std::cin`, `%` |
| 3 | Decisiones | `if`, `else if`, `&&`, `||` |
| 4 | Repetición | `while`, `for` |
| 5 | Colecciones | `std::vector`, `.size()`, índices |
| 6 | Reutilización | funciones, parámetros, `return` |
| 7 | Objetos | `class`, constructores, métodos |
| 8 | Memoria | `&`, `*`, referencia `&`, `nullptr` |

## Hacia dónde seguir

| Dirección | Por qué |
| :--- | :--- |
| **STL** (`<algorithm>`, `<map>`, `<set>`) | La biblioteca estándar es la mayor parte del C++ real |
| **Punteros inteligentes** (`unique_ptr`, `shared_ptr`) | Gestión automática de memoria: RAII |
| **Plantillas y genéricos** | Escribe una vez, funciona con cualquier tipo |
| **Sistemas de construcción** (`CMake`) | Los proyectos multiarchivo necesitan uno |
| **Una librería gráfica** (SFML, SDL, raylib) | Convierte programas de terminal en juegos |

> [!NOTE]
> **Ya tienes el modelo mental que la mayoría de tutoriales omite**
> Los valores viven en direcciones. Los nombres se refieren a valores. Los punteros guardan
> direcciones. Las referencias ponen alias a nombres. Todo lo demás en C++ —vectores, clases,
> punteros inteligentes— se construye sobre esas cuatro frases.

> [!TIP]
> El siguiente paso con mejor retorno: rehacer uno de estos ejercicios como proyecto multiarchivo con
> una cabecera (`.h`) y una implementación (`.cpp`). Esa es la forma de cualquier base de código real.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
