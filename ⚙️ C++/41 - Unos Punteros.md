# 41. Unos Punteros

**Versión original en inglés:** [41 - A Few Pointers.md](./41%20-%20A%20Few%20Pointers.md)

**Curso:** C++
**Tema:** Introducción a los punteros
**Etiquetas:** `#cpp` `#pointers` `#memory`

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

Ya conocemos las direcciones de memoria. Ahora, los punteros.

Los **punteros** son variables especiales que guardan la dirección de memoria de otra variable. Es
como compartir la ubicación de tu pizza en vez de cargarla a todas partes: repartes la dirección y
tus amigos vienen a por una porción.

Crea un puntero con el operador `*`:

```cpp
int x = 420;
int* p = &x; // p guarda la dirección de x
```

> [!NOTE]
> **El tipo del puntero importa**
> Un puntero debe coincidir con el tipo de la variable a la que apunta: un `int*` apunta a un `int`.
> El tipo le dice al compilador cuántos bytes leer al desreferenciar y cuánto avanzar al hacer
> aritmética.

## Declarar uno

El espaciado alrededor de `*` da igual:

```cpp
double* pPrecio;
double *pPrecio;
double * pPrecio;
```

Las tres son idénticas para el compilador. Elige un estilo y mantenlo: la consistencia es lo que hace
legible el código lleno de punteros.

## ¿Para qué necesitamos punteros?

| Caso de uso | Por qué ayuda |
| :--- | :--- |
| **Modificar datos** | Una función que conoce la dirección puede cambiar el valor original |
| **Estructuras dinámicas** | Listas enlazadas y árboles conectan nodos *por dirección* |
| **Rendimiento** | Pasar un puntero a un objeto enorme en lugar de copiarlo |
| **Interfaz de bajo nivel** | Hablar con APIs, llamadas al sistema, librerías C y hardware |

## Ejemplo

```cpp
#include <iostream>
#include <string>

int main() {
  std::string consejo1 = "Sé constante: incluso 10 minutos al día suman.";
  std::string consejo2 = "Toma notas: escribir ayuda a fijar conceptos.";
  std::string consejo3 = "Haz proyectos pequeños: aplica lo que aprendes.";
  std::string consejo4 = "Únete a una comunidad: es más fácil acompañado.";

  std::string* pConsejo1 = &consejo1;
  std::string* pConsejo2 = &consejo2;
  std::string* pConsejo3 = &consejo3;
  std::string* pConsejo4 = &consejo4;

  std::cout << "Punto 1: " << pConsejo1 << "\n";
  std::cout << "Punto 2: " << pConsejo2 << "\n";
  std::cout << "Punto 3: " << pConsejo3 << "\n";
  std::cout << "Punto 4: " << pConsejo4 << "\n";
}
```

> [!WARNING]
> **Un puntero es solo un número hasta que lo desreferencias**
> Imprimir `pConsejo1` da una dirección. Imprimir `*pConsejo1` da la cadena. Confundirlos es el primer
> día de toda sesión de depuración en C++.

> [!TIP]
> Esta es también la razón de que C++ pueda sentirse "peligroso": la dirección es real y nada te
> impide leer lo que haya allí. Ver [[44 - Nullptr]] para la red de seguridad.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
