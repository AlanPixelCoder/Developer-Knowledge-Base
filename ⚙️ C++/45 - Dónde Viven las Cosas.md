# 45. Dónde Viven las Cosas

**Versión original en inglés:** [45 - Where Things Live](./45%20-%20Where%20Things%20Live.md)

**Curso:** C++
**Capítulo:** 8 — Memoria
**Tema:** La pila y el montón, y cuál usa cada variable
**Etiquetas:** `#cpp` `#memory` `#stack`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-8-7C5CFF?style=for-the-badge" alt="Chapter 8">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Todo valor en un programa en ejecución vive en algún sitio. Dos regiones cubren casi todo lo que
escribes: la pila, que crece y decrece con las llamadas, y el montón, que pides y devuelves.

```cpp
#include <iostream>

int contador_global = 7;          // almacenamiento estático: todo el programa

void mostrar_pila() {
  int local = 41;                 // almacenamiento automático: solo esta llamada
  std::cout << "dirección local:   " << &local << "\n";
}

int main() {
  int a = 1;
  int b = 2;

  mostrar_pila();

  std::cout << "dirección de a:    " << &a << "\n";
  std::cout << "dirección de b:    " << &b << "\n";
  std::cout << "dirección global:  " << &contador_global << "\n";
}
```

## Salida

Una ejecución de ejemplo: las direcciones cambian en cada corrida y en cada compilación:

```text
dirección local:   0x7ff7b6f0a5ac
dirección de a:    0x7ff7b6f0a5b8
dirección de b:    0x7ff7b6f0a5bc
dirección global:  0x10b3d0000
```

## Tres regiones, tres tiempos de vida

| Región | Quién la crea | Tiempo de vida | Ejemplo |
| :--- | :--- | :--- | :--- |
| Pila (automática) | el compilador, al entrar | hasta que acaba el bloque | `int a = 1;` |
| Montón (dinámica) | `new` o un contenedor | hasta `delete` o hasta que muera el dueño | `new int(5)` |
| Estática | el cargador | todo el programa | globales, locales `static` |

Las direcciones exactas cambian en cada ejecución y en cada compilación. Lo que no cambia: las
direcciones de pila están cerca entre sí y crecen hacia abajo, y las del montón vienen de otra región
distinta.

## Por qué importa la distinción

- Reservar en la pila es mover un puntero: prácticamente gratis.
- Reservar en el montón pide un bloque al asignador, cuesta tiempo y puede fallar.
- La memoria de la pila desaparece sola. La del montón no, lo que es cómodo o una fuga.

> [!NOTE]
> `std::vector` guarda sus elementos en el montón aunque el objeto vector esté en la pila. Así puede
> crecer: el objeto pequeño guarda un puntero, un tamaño y una capacidad.

> [!TIP]
> Imprimir `&variable` muestra dónde vive, no qué contiene. Las direcciones son una herramienta de
> depuración, nunca un valor para comparar o guardar: la misma variable puede moverse entre
> ejecuciones.

---

**Siguiente:** [[46 - La Lente Dirección-De]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
