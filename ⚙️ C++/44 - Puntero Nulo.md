# 44. Puntero Nulo

**Versión original en inglés:** [44 - Nullptr.md](./44%20-%20Nullptr.md)

**Curso:** C++
**Tema:** La palabra clave `nullptr`
**Etiquetas:** `#cpp` `#pointers` `#nullptr`

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

Un puntero guarda la dirección de memoria de otra variable. Pero ¿y si queremos un puntero que
todavía no apunte a nada, un puntero intencionadamente vacío?

Si declaramos `int* p;` sin inicializar, `p` contiene una dirección **aleatoria**. Usarlo ahora podría
tumbar el programa.

`nullptr` es una palabra clave que representa un puntero que no apunta a **ninguna** dirección de
memoria: una dirección que no existe o no se encuentra. Es la forma que tiene C++ de decir: *"este
puntero no apunta a nada"*.

```cpp
int* p = nullptr;
```

## Por qué es mejor que `NULL` o `0`

| Valor | Problema |
| :--- | :--- |
| `NULL` | Es una macro para `0`, un entero: la resolución de sobrecargas puede elegir mal |
| `0` | Ambiguo entre "cero entero" y "puntero nulo" |
| `nullptr` | Tiene su propio tipo, `std::nullptr_t`: nunca ambiguo |

## Proteger con una comprobación

`nullptr` también da una comprobación de flujo limpia: ¿ya se le asignó algo a este puntero?

```cpp
#include <iostream>
#include <string>

void saludar(const std::string* nombre) {
  if (nombre != nullptr) {
    std::cout << "¡Hola, " << *nombre << "!\n";
  } else {
    std::cout << "¡Hola, invitado!\n";
  }
}

int main() {
  std::string usuario = "marcos";

  saludar(&usuario);   // ¡Hola, marcos!
  saludar(nullptr);    // ¡Hola, invitado!
}
```

## Salida

```text
¡Hola, marcos!
¡Hola, invitado!
```

> [!CAUTION]
> **La desreferencia nula es el fallo clásico**
> `*nombre` cuando `nombre == nullptr` es comportamiento indefinido — en la mayoría de sistemas, un
> segfault. La comprobación no es paranoia defensiva: es la razón de que el programa siga vivo.

> [!TIP]
> Inicializa todo puntero que declares, ya sea con una dirección real o con `nullptr`. Un puntero sin
> inicializar es una mina sin etiqueta de advertencia.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
