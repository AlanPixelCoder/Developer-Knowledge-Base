# 40. Recuerdos

**Versión original en inglés:** [40 - Memories.md](./40%20-%20Memories.md)

**Curso:** C++
**Tema:** Direcciones de memoria
**Etiquetas:** `#cpp` `#memory` `#pointers`

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

Bienvenido al último capítulo del curso de C++. Aquí entramos en uno de los conceptos más clásicos de
C++: los **punteros**.

Antes de los punteros, hablemos de las **direcciones de memoria**.

Una **dirección de memoria** es una secuencia única que sirve para localizar un byte concreto (o un
grupo de bytes) en la memoria del ordenador.

La memoria está organizada como una larga secuencia de celdas numeradas (bytes). Cada celda se
accede por su dirección, igual que las casas de una calle.

```text
0x00  0x01  0x02  0x03  0x04  ...
```

## ¿Por qué hexadecimal?

Las direcciones se imprimen en **hexadecimal** (base 16) porque acorta los números binarios largos y
los hace legibles: `0x7ffefb2a` en lugar de treinta y dos bits de unos y ceros.

| Base | Dígitos | Ejemplo |
| :--- | :--- | :--- |
| Binario | `0`–`1` | `1111111111111110` |
| Decimal | `0`–`9` | `65534` |
| Hexadecimal | `0`–`9`, `a`–`f` | `0xfffe` |

## El mapa de la pila

| Variable | Dirección | Valor |
| :--- | :--- | :--- |
| `anio` | `0x1000` | `2005` |
| `nota` | `0x1004` | `5.8` |

> [!NOTE]
> **Una variable es dos cosas a la vez**
> Su **dirección** (dónde vive) y su **valor** (qué contiene). El código normal solo ve el valor. Los
> punteros son la herramienta que te deja trabajar con la dirección.

> [!TIP]
> En un sistema de 64 bits moderno las direcciones suelen ocupar 8 bytes (64 bits) — por eso se ven
> absurdamente largas en `std::cout`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
