# 34. Devolver el Botín

**Versión original en inglés:** [34 - Handing Back the Loot](./34%20-%20Handing%20Back%20the%20Loot.md)

**Curso:** C++
**Capítulo:** 6 — Funciones
**Tema:** Tipos de retorno: void, valor, referencia, y devolver varias cosas
**Etiquetas:** `#cpp` `#functions` `#struct`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-6-7C5CFF?style=for-the-badge" alt="Chapter 6">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Algunas funciones responden a una pregunta, otras cambian el mundo y no responden nada, y otras deben
devolver dos números a la vez. C++ tiene una palabra clave para las tres, y el tipo decide el resto.

```cpp
#include <iostream>
#include <string>

struct Botin {
  std::string nombre;
  int valor;
};

Botin mejor_de(const Botin& a, const Botin& b) {
  return a.valor >= b.valor ? a : b;
}

void anunciar(const Botin& objeto) {
  std::cout << "encontrado " << objeto.nombre << " que vale " << objeto.valor << "\n";
}

int main() {
  Botin moneda{"moneda oxidada", 3};
  Botin anillo{"anillo de plata", 40};

  anunciar(mejor_de(moneda, anillo));
}
```

## Salida

```text
encontrado anillo de plata que vale 40
```

## Dos formas de devolver

| Forma | Firma | Significado |
| :--- | :--- | :--- |
| Responder una pregunta | `int dano(...)` | quien llama necesita el valor |
| Cambiar el mundo | `void anunciar(...)` | quien llama necesita el efecto |
| Responder con estructura | `Botin mejor_de(...)` | varios valores viajan juntos |

Un `struct` es la forma más barata de devolver más de un valor. Dos campos relacionados con nombre
ganan a un `std::pair` cuyos miembros se llaman `first` y `second`.

## Devolver una referencia

Una función puede devolver una referencia cuando quien llama debe ver el objeto original y no una
copia:

```cpp
const Botin& mas_pesado(const std::vector<Botin>& objetos);
```

Eso es seguro solo si el objeto vive más que la llamada. Nunca devuelvas una referencia a un local:
el local se destruye en la llave de cierre y quien llama queda con una referencia colgada.

> [!CAUTION]
> `Botin& mejor_de(...)` devolviendo un parámetro por valor es el caso clásico de referencia colgada.
> Devuelve por valor para objetos nuevos, por referencia solo para objetos que quien llama ya posee.

> [!TIP]
> El compilador elide la copia al devolver un local por valor, así que `return a;` no es más lento
> que devolver un puntero. No retuerzas el diseño para "evitar una copia" antes de medir.

---

**Siguiente:** [[35 - Retornos Encadenados]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
