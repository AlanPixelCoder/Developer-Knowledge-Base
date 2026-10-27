# 22. 99 Botellas

**Versión original en inglés:** [22 - 99 Bottles.md](./22%20-%2099%20Bottles.md)

**Curso:** C++
**Tema:** Bucles `for` decrementales
**Etiquetas:** `#cpp` `#loops` `#for` `#decrement`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Puedes escribir bucles `for` donde el contador **sube** (incremento) y también donde **baja**
(decremento).

Para contar hacia abajo: inicializa en un número mayor, comprueba que sea *mayor* que un valor y usa
`i--` como cambio.

```cpp
for (int i = 99; i > 0; i--) {
  // cuerpo
}
```

## Hacia arriba vs hacia abajo

| Dirección | Inicio | Condición | Cambio |
| :--- | :--- | :--- | :--- |
| Arriba | `int i = 0` | `i < n` | `i++` |
| Abajo | `int i = n` | `i > 0` | `i--` |

## Ejemplo

```cpp
#include <iostream>

int main() {
  for (int i = 99; i > 0; i--) {
    std::cout << i << " botellas de cerveza en la pared\n";
    std::cout << i << " botellas de cerveza\n";
    std::cout << "Toma una, pásala\n";
    std::cout << i - 1 << " botellas de cerveza en la pared\n\n";
  }
}
```

> [!NOTE]
> Fíjate en el `i - 1` de la última línea: el contador sigue en la botella actual, así que el número
> "después de tomar una" hay que calcularlo. La última iteración imprime `0 botellas en la pared`:
> gramaticalmente discutible, canónicamente parte de la canción.

> [!TIP]
> Contar hacia abajo es exactamente lo que necesitas para recorrer un vector al revés:
> `for (int i = v.size() - 1; i >= 0; i--)`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
