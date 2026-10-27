# 32. Conversiones

**Versión original en inglés:** [32 - Conversions.md](./32%20-%20Conversions.md)

**Curso:** C++
**Tema:** Valor de retorno
**Etiquetas:** `#cpp` `#functions` `#return` `#void`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Las funciones pueden recibir entradas, pero también pueden **enviar** valores.

Cuando declaramos una función con `void`, la función solo hace una tarea y no nos deja nada.

Para devolver un valor, cambia `void` por el tipo de dato que quieres retornar (por ejemplo `int`,
`double`, `std::string`) y usa la palabra clave `return`.

`return` **termina la función** y deja un valor detrás.

## Sintaxis

```cpp
int sumar(int x, int y) {
  int resultado = 0;
  resultado = x + y;
  return resultado; // deja el valor detrás
}
```

Ahora, llamar a la función produce un valor que podemos imprimir, asignar o pasar a otra expresión.

```cpp
int total = sumar(4, 3);     // total es 7
std::cout << sumar(10, 5);   // 15
```

## `void` vs tipo de retorno

| Tipo | Devuelve | Úsalo para |
| :--- | :--- | :--- |
| `void` | Nada | Imprimir, actualizar estado, efectos secundarios |
| `int` / `double` / … | Un valor de ese tipo | Cálculos, búsquedas, conversiones |

> [!IMPORTANT]
> **El valor retornado tiene que usarse o guardarse**
> `sumar(1, 2);` solo en su línea calcula 3 y lo tira. La llamada es legal, pero inútil. Asígnalo,
> imprímelo o págalo hacia otra expresión.

> [!TIP]
> Un `return` dentro de una función actúa como salida anticipada: todo lo que venga después en esa
> función se salta. Ver [[32 - Conversiones (Continuación)]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
