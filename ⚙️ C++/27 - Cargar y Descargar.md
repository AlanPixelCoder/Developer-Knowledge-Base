# 27. Cargar y Descargar

**Versión original en inglés:** [27 - Pack and Unpack](./27%20-%20Pack%20and%20Unpack.md)

**Curso:** C++
**Capítulo:** 5 — Colecciones
**Tema:** push_back, pop_back y el tamaño que los acompaña
**Etiquetas:** `#cpp` `#vector` `#push-back`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-5-7C5CFF?style=for-the-badge" alt="Chapter 5">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

El botín llega de uno en uno y se va de uno en uno. La alforja no tiene longitud fija, así que los dos
extremos se mueven.

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> alforja;

  alforja.push_back("antorcha");
  alforja.push_back("cuerda");
  alforja.push_back("pan");

  std::cout << "tras cargar:   " << alforja.size() << "\n";
  std::cout << "objeto arriba: " << alforja.back() << "\n";

  alforja.pop_back();

  std::cout << "tras descargar: " << alforja.size() << "\n";
  std::cout << "objeto arriba:  " << alforja.back() << "\n";
}
```

## Salida

```text
tras cargar:   3
objeto arriba: pan
tras descargar: 2
objeto arriba:  cuerda
```

## Crecer y encoger

| Llamada | Efecto | Coste |
| :--- | :--- | :--- |
| `push_back(x)` | añade `x` al final, tamaño + 1 | constante amortizado |
| `pop_back()` | quita el último elemento, tamaño − 1 | constante |
| `back()` | lee el último elemento | constante |
| `clear()` | quita todo, tamaño 0 | lineal |

El vector guarda una capacidad mayor que su tamaño para que la mayoría de los `push_back` no
reubiquen. Por eso el coste es "amortizado" y no "gratis".

## La trampa del vacío

`pop_back()` sobre un vector vacío y `back()` sobre un vector vacío son comportamiento indefinido.
La guarda cuesta una comparación:

```cpp
if (!alforja.empty()) {
  alforja.pop_back();
}
```

> [!CAUTION]
> `pop_back()` no devuelve nada. Quita el elemento y lo tira. Para conservar el valor, lee
> `alforja.back()` primero y luego haz el pop.

> [!TIP]
> `push_back` es la forma natural de construir una colección de longitud desconocida. Reserva un
> tamaño solo cuando ya lo conozcas y la reubicación aparezca en un perfil.

---

**Siguiente:** [[28 - Recorrer la Alforja]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
