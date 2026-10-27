# 40. Recuerdos (Continuación)

**Versión original en inglés:** [40 - Memories (Continuation).md](./40%20-%20Memories%20%28Continuation%29.md)

**Curso:** C++
**Tema:** Direcciones de memoria y el operador `&`
**Etiquetas:** `#cpp` `#memory` `#address`

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

Cuando creamos variables, cada una se guarda en una dirección distinta (por ejemplo `0x1000`,
`0x1004`).

Podemos acceder a esa memoria con `&`, el operador **dirección-de**. En palabras simples, `&x`
significa "dame la dirección de memoria de `x`". Esa dirección es donde vive la variable en la RAM.

## Ejemplo

```cpp
#include <iostream>
#include <string>

int main() {
  std::string juego_favorito = "Destroy All Humans!";
  int anio_primera_partida = 2005;
  double peor_nota = 5.8;
  char seccion_tutor = 'B';

  std::cout << "--- Direcciones de memoria ---\n";
  std::cout << "Juego: " << &juego_favorito << "\n";
  std::cout << "Año: " << &anio_primera_partida << "\n";
  std::cout << "Nota: " << &peor_nota << "\n";

  // Convertir a (void*) para que la dirección se imprima limpia en lugar de como carácter
  std::cout << "Sección: " << (void*)&seccion_tutor << "\n";
}
```

## Salida de ejemplo

```text
--- Direcciones de memoria ---
Juego: 0x16da47718
Año: 0x16da47714
Nota: 0x16da47708
Sección: 0x16da47707
```

> [!IMPORTANT]
> **Por qué el cast a `(void*)`**
> Un `char*` se trata como cadena C al enviarse a un flujo, así que `&seccion_tutor` imprimiría los
> *caracteres* de esa dirección hasta encontrar un byte nulo — normalmente nada, a veces basura.
> Convertirlo a `void*` le dice a `std::cout` "esto es un puntero, imprime el número".

> [!NOTE]
> Las direcciones exactas cambian en cada ejecución. Es normal: el sistema operativo decide dónde va
> la pila de tu programa. El orden **relativo** sí es estable. Recorriendo la salida de ejemplo:
> `&seccion_tutor` está un byte por debajo de `&peor_nota` porque un `char` mide un byte; el `double`
> ocupa sus 8 bytes completos; y el `int` cae 4 bytes después, porque la alineación a 8 deja un
> hueco. Lee los huecos y estarás leyendo tamaños de tipo y relleno.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
