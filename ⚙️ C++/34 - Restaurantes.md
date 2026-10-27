# 34. Restaurantes

**Versión original en inglés:** [34 - Restaurants.md](./34%20-%20Restaurants.md)

**Curso:** C++
**Tema:** Introducción a las clases
**Etiquetas:** `#cpp` `#classes` `#oop` `#data-types`

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

Con las **clases** podemos crear nuestros propios tipos de datos y usarlos para modelar objetos
cotidianos con características y comportamientos propios.

Las clases sirven como plantilla para los objetos creados con ellas. Dicho simple: una clase es un
**plano**. Un fabricante de coches usa un plano para construir cientos de coches, cada uno con su
propia pintura y kilometraje.

## Definir una clase

La palabra clave `class` seguida de un nombre crea la clase. Por convención el nombre va en
**mayúscula inicial**.

```cpp
class Student {
  std::string name;
  int year;
  double gpa;
};
```

> [!IMPORTANT]
> **No olvides el punto y coma**
> Hay un `;` después de la `}` de cierre de una clase. Si lo omites, el compilador señala un error en
> la línea *siguiente*, lo que hace parecer que el problema está en otro lado.

## Clase vs objeto

| Término | Significado |
| :--- | :--- |
| **Clase** | El plano: la definición, sin datos |
| **Objeto** | Una instancia concreta construida a partir de ese plano |

> [!NOTE]
> **El acceso por defecto es `private`**
> Los miembros de una `class` son privados salvo que se marquen `public`. Por eso existe la siguiente
> nota, [[35 - Público vs Privado]]: ahora mismo nada fuera de la clase puede siquiera leer `name`,
> `year` o `gpa`.

> [!TIP]
> Todo este capítulo es la pista de despegue del código de juego estilo Unity: `class Enemy`,
> `class Inventory`, `class Weapon` son la misma construcción que aprendes aquí.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
