# 04. Notas al Margen

**Versión original en inglés:** [04 - Notes in the Margin](./04%20-%20Notes%20in%20the%20Margin.md)

**Curso:** C++
**Capítulo:** 1 — Primer Arranque
**Tema:** Comentarios: de línea, de bloque y para qué sirven
**Etiquetas:** `#cpp` `#comments` `#readability`

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

Un comentario es texto que el compilador tira. Bien usado, guarda el *porqué* que el código no puede
decir solo; mal usado, repite lo que el código ya dice, en una versión que deja de ser cierta.

```cpp
#include <iostream>

int main() {
  // La tasa de ticks está limitada a 60: el paso de física se calibró con ese valor.
  const int TICKS_POR_SEGUNDO = 60;

  std::cout << "tasa de ticks: " << TICKS_POR_SEGUNDO << "\n";

  /* El presupuesto de render es generoso a propósito.
     El motor dibuja el brillo de la linterna en dos pasadas, y la
     segunda todavía no tiene límite de fuentes de luz. */
  const double PRESUPUESTO_RENDER_MS = 12.5;

  std::cout << "presupuesto de render: " << PRESUPUESTO_RENDER_MS << " ms\n";
}
```

## Las dos formas

| Forma | Sintaxis | Cuándo es la herramienta correcta |
| :--- | :--- | :--- |
| Comentario de línea | `// hasta el final de la línea` | Casi siempre: una razón, una línea |
| Comentario de bloque | `/* ... */` | Un párrafo de contexto sobre una declaración |

## Salida

```text
tasa de ticks: 60
presupuesto de render: 12.5 ms
```

> [!CAUTION]
> Los comentarios de bloque **no** se anidan. `/* externo /* interno */ sigue siendo comentario */`
> cierra en el primer `*/`, y todo lo que viene después pasa a ser código que el compilador
> intentará leer.

> [!WARNING]
> El código comentado no es documentación, es sedimento. El control de versiones ya recuerda la
> versión anterior: bórralo y deja que el historial haga su trabajo.

> [!TIP]
> Si un comentario explica *qué* hace la línea siguiente, renombra la variable. Si explica *por qué*
> la línea existe, consérvalo para siempre.

---

**Siguiente:** [[05 - Velocidad de Escape]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
