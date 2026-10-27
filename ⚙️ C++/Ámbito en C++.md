# Ámbito en C++

**Versión original en inglés:** [Scope in C++.md](./Scope%20in%20C%2B%2B.md)

**Curso:** C++
**Tema:** Ámbito local y global
**Etiquetas:** `#cpp` `#scope` `#variables`

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

En C++, el **ámbito** (scope) es la región del programa donde un nombre (de variable, función o
clase) es visible y accesible.

## Ámbito local

Una **variable local** se declara dentro de una función o bloque `{}`. Pertenece a ese ámbito y solo
puede usarse dentro. Si intentas acceder fuera, el programa no compila.

- *Caso de uso:* un valor que solo se necesita temporalmente dentro de una función.
- *Buena práctica:* local siempre que sea posible.

## Ámbito global

Una **variable global** se crea fuera de cualquier función y pertenece al ámbito global: es accesible
desde cualquier parte del archivo.

- *Caso de uso:* un valor realmente compartido entre varias funciones o archivos.

## Ejemplo

```cpp
#include <iostream>

int dia = 3; // global

void bienvenida() {
  std::cout << "Bienvenido al día " << dia << " de Beast Games\n";
}

int main() {
  std::cout << "¿Qué día es hoy?\n";
  std::cout << dia << "\n";
  bienvenida();
}
```

## Local vs global

| | Local | Global |
| :--- | :--- | :--- |
| Se declara | Dentro de `{}` | Fuera de toda función |
| Visible | Solo en ese bloque | Todo el archivo |
| Vida | Hasta que termina el bloque | Hasta que termina el programa |
| Riesgo | Bajo | Acoplamientos ocultos, mutaciones accidentales |

> [!WARNING]
> **Sombreado (shadowing)**
> Si una variable local tiene el mismo nombre que una global, la local *gana* dentro de su bloque.
> `int dia = 9;` dentro de `main()` oculta la global `dia`, y la global mantiene su valor en silencio.
> Código legal, programa confuso.

> [!TIP]
> Ante la duda, mantenlo local. Una global es una variable que toda función puede alcanzar: eso
> significa que toda función es sospechosa cuando cambia sin explicación.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
