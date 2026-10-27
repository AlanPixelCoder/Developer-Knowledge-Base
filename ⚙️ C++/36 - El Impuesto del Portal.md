# 36. El Impuesto del Portal

**Versión original en inglés:** [36 - The Gate Tax](./36%20-%20The%20Gate%20Tax.md)

**Curso:** C++
**Capítulo:** 6 — Funciones
**Tema:** Paso por valor frente a paso por referencia
**Etiquetas:** `#cpp` `#functions` `#references`

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

Cada viajero paga un impuesto en el portal. El escriba anota la cantidad en el libro mayor. Dos formas
de entregar el libro: una copia donde puede garabatear, o el libro de verdad.

```cpp
#include <iostream>

int impuesto_por_copia(int oro) {
  oro -= 10;          // cambia solo la copia
  return oro;
}

void impuesto_por_referencia(int& oro) {
  oro -= 10;          // cambia la variable de quien llama
}

int main() {
  int bolsa = 50;

  std::cout << "devuelto: " << impuesto_por_copia(bolsa) << "\n";
  std::cout << "bolsa:    " << bolsa << "\n";

  impuesto_por_referencia(bolsa);
  std::cout << "bolsa:    " << bolsa << "\n";
}
```

## Salida

```text
devuelto: 40
bolsa:    50
bolsa:    40
```

## Las cuatro formas de pasar

| Firma | ¿Copia? | ¿Quien llama ve el cambio? | Úsalo cuando |
| :--- | :--- | :--- | :--- |
| `int x` | sí | no | valores pequeños, entradas simples |
| `const int&` | no | no | objetos grandes de solo lectura |
| `int&` | no | sí | la función debe modificar |
| `int*` | no (se copia el puntero) | sí, si se desreferencia | caso opcional "sin valor" |

Un `int` es lo bastante pequeño como para que copiar sea más rápido que la indirección. Un
`std::string` o un `std::vector` no lo son, y por eso `const std::string&` es el defecto para
parámetros de solo lectura.

## `&` en el parámetro, `&` en la llamada

El ampersand pertenece al **tipo** en la firma. En la llamada escribes
`impuesto_por_referencia(bolsa)` sin `&`: la función ya exige una referencia.

> [!CAUTION]
> `impuesto_por_referencia(50)` no compila: un literal no es un lvalue, así que ninguna referencia no
> constante puede enlazarlo. Si el valor de quien llama no debe cambiar, toma `int` o `const int&`.

> [!TIP]
> Una función que toma y devuelve un valor por referencia es señal de que querías
> `int impuesto(int oro) { return oro - 10; }`. Modifica por referencia solo cuando el objetivo de la
> función sea la modificación.

---

**Siguiente:** [[37 - Dónde Viven los Nombres]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
