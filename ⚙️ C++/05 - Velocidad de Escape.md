# 05. Velocidad de Escape

**Versión original en inglés:** [05 - Escape Velocity](./05%20-%20Escape%20Velocity.md)

**Curso:** C++
**Capítulo:** 1 — Primer Arranque
**Tema:** Escapar barras y comillas, y dibujar con texto
**Etiquetas:** `#cpp` `#strings` `#ascii-art`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El cartel de la consola necesita un marco. Los marcos se construyen con caracteres que significan
otra cosa dentro de un literal de cadena, así que antes de enmarcar un cartel hay que aprender a
neutralizarlos. Solo dos lo necesitan: la barra invertida y la comilla doble.

```cpp
#include <iostream>

int main() {
  std::cout << "************************\n";
  std::cout << "*  MOTOR EMBERFALL     *\n";
  std::cout << "*  \"¡compila!\"          *\n";
  std::cout << "*  ruta: C:\\ember      *\n";
  std::cout << "************************\n";
}
```

## La tabla de escapes

| Quieres imprimir | Debes escribir | Porque |
| :--- | :--- | :--- |
| `\` | `\\` | Una barra sola inicia una secuencia de escape |
| `"` | `\"` | Una comilla suelta termina la cadena antes de tiempo |
| salto de línea | `\n` | El escape del salto de línea |
| tabulación | `\t` | El escape de la tabulación |

## Salida

```text
************************
*  MOTOR EMBERFALL     *
*  "¡compila!"          *
*  ruta: C:\ember      *
************************
```

> [!WARNING]
> Un escape que C++ no reconoce — `\d`, por ejemplo — suele compilar igual: el compilador avisa y
> luego imprime el carácter pelado. Compila con `-Wall` y lee el aviso en lugar de culpar a la
> terminal.

> [!TIP]
> Para arte pesado usa una cadena cruda: `R"(...)"` deja cada barra literal, así que puedes pegar un
> cartel entero sin tocarlo. Los paréntesis son parte de la sintaxis.

> [!NOTE]
> Cada `\n` de esta lección va **dentro** de las comillas. Fuera de ellas no es un escape: es un
> error de sintaxis esperando su mensaje del compilador.

---

**Siguiente:** [[06 - De Fuente a Interruptor]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
