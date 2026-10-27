# 07. Declaración de Independencia

**Versión original en inglés:** [07 - Declaration of Independence.md](./07%20-%20Declaration%20of%20Independence.md)

**Curso:** C++
**Tema:** Declaración de variables y reglas de nombres
**Etiquetas:** `#cpp` `#variables` `#declaration`

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

Toda variable en C++ debe **declararse** (crearse) antes de usarse.

Para declarar una variable necesitamos dos cosas:

1. Un **tipo de dato**.
2. Un **nombre de variable**.

```cpp
int puntuacion;
```

- `int` es el tipo de dato.
- `puntuacion` es el nombre de la variable.
- `;` termina la sentencia.

## Reglas para nombres de variables

| Regla | Detalle |
| :--- | :--- |
| Caracteres permitidos | Letras, dígitos y guiones bajos `_` |
| Sensible a mayúsculas | `Talla_Camisa` y `talla_camisa` son variables **distintas** |
| Sin espacios | `mi puntuacion` no es válido |
| Sin caracteres especiales | `!`, `#`, `%`, `-` se rechazan |
| Debe empezar con letra | `2fast` no vale; `fast2` sí |
| Palabras reservadas | No puedes llamar a una variable `int`, `return`, `class`… |

> [!NOTE]
> **Estilo de nombres**
> C++ no impone una convención única, pero la comunidad converge en `snake_case` para variables y
> funciones (`vida_jugador`) y `PascalCase` para clases (`BankAccount`). Elige una y mantenla: la
> consistencia vale más que la elección "correcta".

> [!TIP]
> Una variable `int` declarada pero sin inicializar contiene **basura**: lo que hubiera en esa celda
> de memoria. Inicializa siempre. Ver [[08 - IPO]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
