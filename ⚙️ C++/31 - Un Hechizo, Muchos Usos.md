# 31. Un Hechizo, Muchos Usos

**Versión original en inglés:** [31 - One Spell, Many Casts](./31%20-%20One%20Spell%2C%20Many%20Casts.md)

**Curso:** C++
**Capítulo:** 6 — Funciones
**Tema:** Por qué existen las funciones: una definición, muchas llamadas
**Etiquetas:** `#cpp` `#functions` `#basics`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El mismo cálculo de daño de tres líneas aparece en seis sitios: la rama cuerpo a cuerpo, la de
hechizos, la de trampas, la del jefe. Cambia la fórmula y tienes que encontrar los seis. Una función
lo deja en un solo sitio.

```cpp
#include <iostream>

int dano(int poder, int armadura) {
  int bruto = poder * 3;
  int reducido = bruto - armadura;
  return reducido < 1 ? 1 : reducido;
}

int main() {
  std::cout << "goblin:   " << dano(4, 2) << "\n";
  std::cout << "esqueleto: " << dano(4, 11) << "\n";
  std::cout << "ogro:     " << dano(9, 6) << "\n";
}
```

## Salida

```text
goblin:   10
esqueleto: 1
ogro:     21
```

## Anatomía

| Parte | Aquí | Significado |
| :--- | :--- | :--- |
| Tipo de retorno | `int` | el tipo del valor devuelto |
| Nombre | `dano` | cómo la llamas |
| Parámetros | `int poder, int armadura` | las entradas, con tipo |
| Cuerpo | las tres líneas | el trabajo |
| `return` | `return ...;` | el valor y la salida |

## Tres razones, no una

1. **Un solo sitio que cambiar.** Un parche de balance toca la fórmula, no seis llamadas.
2. **Un nombre para la idea.** `dano(4, 2)` se lee mejor que `4 * 3 - 2`.
3. **Un sitio donde probar.** Puedes llamar a `dano` con casos límite antes de que exista el juego.

> [!NOTE]
> La función debe estar declarada o definida *antes* de la primera llamada. Definirla encima de
> `main` es lo más simple; un prototipo encima de `main` y el cuerpo debajo es la otra vía.

> [!TIP]
> Si copias tres líneas dos veces, escribe una función. Si las copias seis veces, ya tienes un error:
> las copias han empezado a divergir.

---

**Siguiente:** [[32 - El Tablón de la Taberna]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
