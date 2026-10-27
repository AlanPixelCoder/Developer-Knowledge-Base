# 39. Rescate de Mascotas (Continuación)

**Versión original en inglés:** [39 - Pet Rescue (Continuation).md](./39%20-%20Pet%20Rescue%20%28Continuation%29.md)

**Curso:** C++
**Tema:** Implementación de métodos de clase
**Etiquetas:** `#cpp` `#classes` `#oop` `#methods` `#project`

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

Así se implementan los métodos de `Cat` para poder interactuar de verdad con los objetos.

```cpp
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

    void feed() {
      if (hunger < 10) {
        hunger++;
      }
      std::cout << "\n🍲 Alimentaste a " << name << ". Hambre ahora " << hunger << "/10.\n";
    }

    void play() {
      if (mood < 10) {
        mood++;
      }
      std::cout << "\n🧶 Jugaste con " << name << ". Ánimo ahora " << mood << "/10.\n";
    }

    void status() {
      std::cout << "\n=== Estado de " << name << " ===\n";
      std::cout << "Raza: " << breed << " | Edad: " << age << "\n";
      std::cout << "Ánimo: " << mood << "/10  | Hambre: " << hunger << "/10\n";
      std::cout << "Rescatado: " << (rescued ? "Sí" : "No") << "\n";
    }
};
```

## El menú interactivo

Con un bucle `while` construimos un menú de terminal que sigue preguntando hasta que el usuario
decide salir. Junta `#include <iostream>`, la clase `Cat` del bloque anterior y este `main` en un
solo archivo y corre tal cual.

```cpp
int main() {
  Cat garfield("Garfield", "Persa", 5, true, 4, 9);
  int opcion = 0;

  while (opcion != 4) {
    garfield.status();
    std::cout << "\n1) Alimentar  2) Jugar  3) Estado  4) Salir\n> ";
    std::cin >> opcion;

    if (opcion == 1) garfield.feed();
    else if (opcion == 2) garfield.play();
  }

  std::cout << "\n¡Hasta luego! 🐾\n";
}
```

> [!NOTE]
> **`rescued ? "Sí" : "No"` — el operador ternario**
> Un `if/else` de una línea que produce un valor en lugar de ejecutar sentencias:
> `condicion ? valor_si_true : valor_si_false`. Perfecto para imprimir, inútil para control de flujo.

> [!WARNING]
> El bucle solo sale con `4`. Escribe `9` y reimprime el menú en silencio — lo cual aquí está *bien*,
> pero un menú real debería decir "opción desconocida" para que el usuario sepa que su entrada se
> registró.

> [!TIP]
> Fíjate en que `status()` no recibe parámetros y aun así imprime todo lo que necesita. Esa es la
> recompensa de la encapsulación: el objeto ya tiene su propio estado.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
