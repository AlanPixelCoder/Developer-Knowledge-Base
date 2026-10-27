# 37. Dónde Viven los Nombres

**Versión original en inglés:** [37 - Where Names Live](./37%20-%20Where%20Names%20Live.md)

**Curso:** C++
**Capítulo:** 6 — Funciones
**Tema:** Ámbito, tiempo de vida y ocultamiento
**Etiquetas:** `#cpp` `#scope` `#lifetime`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El motor tiene un contador global `tick`, una función con un `tick` local y un bloque dentro de esa
función con otro `tick`. Tres variables, un nombre, y la más interna gana en todo lugar donde es
visible.

```cpp
#include <iostream>

int tick = 100;                 // ámbito de archivo

void avanzar() {
  int tick = 1;                 // oculta el global
  {
    int tick = 7;               // oculta el local
    std::cout << "interno: " << tick << "\n";
  }
  std::cout << "local:   " << tick << "\n";
}

int main() {
  avanzar();
  std::cout << "global:  " << tick << "\n";
  std::cout << "::tick:  " << ::tick << "\n";
}
```

## Salida

```text
interno: 7
local:   1
global:  100
::tick:  100
```

## El ámbito es donde un nombre es visible

| Nombre | Ámbito | Tiempo de vida |
| :--- | :--- | :--- |
| `tick` (archivo) | todo el archivo tras la declaración | todo el programa |
| `tick` (local) | el cuerpo de `avanzar` | cada llamada |
| `tick` (interno) | solo ese bloque | hasta la `}` del bloque |

Un local se crea al entrar y se destruye en la llave de cierre. El global existe antes de `main` y
después de que retorne.

## Ocultar es legal y casi siempre un error

El compilador lo permite; `-Wshadow` te dirá que ha pasado. `::tick` atraviesa todos los locales hasta
el global, y necesitarlo es una pista fuerte de que dos variables no deberían compartir nombre.

> [!WARNING]
> Una variable oculta no es "la misma variable con un valor nuevo". La de fuera conserva su valor y
> retoma el mando cuando el bloque interno termina, que es justo la confusión que invita el
> ocultamiento.

> [!TIP]
> Prefiere pasar valores como parámetros antes que recurrir a globales. Una función que lee un global
> no se puede probar sin el global, ni llamar dos veces con entradas distintas.

> [!NOTE]
> Declara las variables lo más tarde posible y en el ámbito más pequeño que funcione. Un nombre que
> existe durante cuarenta líneas es un nombre que puedes usar mal durante cuarenta líneas.

---

**Siguiente:** [[38 - Planos del Gremio]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
