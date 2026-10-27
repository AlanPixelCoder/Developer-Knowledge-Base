# 39. Rescate de Mascotas

**Versión original en inglés:** [39 - Pet Rescue.md](./39%20-%20Pet%20Rescue.md)

**Curso:** C++
**Tema:** Repaso del capítulo 7 y proyecto de POO
**Etiquetas:** `#cpp` `#recap` `#classes` `#oop` `#project`

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

## Repaso del capítulo 7

Aprendimos a:

- Crear una clase e inicializarla con atributos.
- Crear objetos a partir de esas clases y asignarles valores.
- Crear clases con un **constructor** que hace la inicialización.
- Crear **métodos de clase** que usan o actualizan esos atributos.

## Proyecto: Rescate de Mascotas

Supón que construimos una app de rescate donde los usuarios crean e interactúan con mascotas.
Creamos una clase `Cat` con atributos (`name`, `breed`, `age`, `rescued`, `mood`, `hunger`) y métodos
`feed()`, `play()` y `status()`.

```cpp
#include <iostream>
#include <string>

class Cat {
  public:
    std::string name;
    std::string breed;
    int age;
    bool rescued;
    int mood;   // 0 = triste, 10 = muy feliz
    int hunger; // 0 = hambriento, 10 = lleno

    Cat(std::string n, std::string b, int a, bool r, int m, int h) {
      name = n;
      breed = b;
      age = a;
      rescued = r;
      mood = m;
      hunger = h;
    }

    // feed(), play(), status() van aquí
};

int main() {
  Cat garfield("Garfield", "Persa", 5, true, 4, 9);
  Cat luna("Luna", "Esfinge", 2, false, 7, 3);

  // Interactuar mediante un menú de texto
}
```

## Flujo de datos

| Acción | Efecto en `hunger` | Efecto en `mood` |
| :--- | :--- | :--- |
| `feed()` | +1, tope en 10 | — |
| `play()` | — | +1, tope en 10 |
| `status()` | solo lee | solo lee |

> [!NOTE]
> **Los topes son el diseño**
> `if (hunger < 10) hunger++;` mantiene la estadística dentro de su banda 0–10. Sin la guarda, unas
> docenas de comidas llevarían el hambre a 40 y romperían todas las suposiciones de la interfaz.

> [!TIP]
> Dos objetos, una clase. `garfield.hunger` y `luna.hunger` son cajas totalmente independientes: ese
> es el sentido completo de instanciar un plano.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
