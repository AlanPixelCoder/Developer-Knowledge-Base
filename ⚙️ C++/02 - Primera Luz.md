# 02. Primera Luz

**Versión original en inglés:** [02 - First Light](./02%20-%20First%20Light.md)

**Curso:** C++
**Capítulo:** 1 — Primer Arranque
**Tema:** Imprimir en la consola con std::cout
**Etiquetas:** `#cpp` `#output` `#iostream`

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

La consola del motor no sirve de nada hasta que puede hablar. Lo primero que hace en cada arranque
es imprimir un cartel de bienvenida, y ese cartel son tres instrucciones que se leen igual:

```cpp
#include <iostream>

int main() {
  std::cout << "Consola del motor Emberfall\n";
  std::cout << "build 0.1.0\n";
  std::cout << "estado: listo\n";
}
```

## Leer la línea de derecha a izquierda

| Pieza | Nombre | Qué hace |
| :--- | :--- | :--- |
| `std::cout` | flujo de salida de caracteres | La tubería de salida de la consola |
| `<<` | operador de inserción | Empuja el valor de la derecha hacia el flujo de la izquierda |
| `"..."` | literal de cadena | Exactamente los caracteres entre comillas |
| `;` | terminador | Cierra la sentencia: el compilador no va a adivinar |

`std::` significa *biblioteca estándar*: `cout` vive en un espacio de nombres y el prefijo dice
dónde encontrarlo.

## Salida

```text
Consola del motor Emberfall
build 0.1.0
estado: listo
```

Tres sentencias distintas, tres líneas, porque cada cadena termina en `\n`.

> [!TIP]
> `\n` dentro de la cadena y `std::endl` después de ella rompen la línea igual. Prefiere `\n`:
> `endl` además vacía el búfer, un costo que casi nunca necesitas en una línea de registro.

> [!WARNING]
> Si falta un `;`, el error se reporta en la línea **siguiente**, porque ahí es donde el compilador
> se rinde. Cuando el mensaje apunte a una línea que se ve perfecta, revisa la de arriba.

---

**Siguiente:** [[03 - El Archivo Esqueleto]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
