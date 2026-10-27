# 03. El Archivo Esqueleto

**Versión original en inglés:** [03 - The Skeleton File](./03%20-%20The%20Skeleton%20File.md)

**Curso:** C++
**Capítulo:** 1 — Primer Arranque
**Tema:** Includes, main, llaves y secuencias de escape
**Etiquetas:** `#cpp` `#structure` `#escape-sequences`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-1-7C5CFF?style=for-the-badge" alt="Chapter 1">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Casi todo programa C++ arranca del mismo esqueleto. Apréndelo una vez y dejarás de leerlo para
empezar a leer lo que cambió.

```cpp
#include <iostream>

int main() {
  std::cout << "ranura\tnombre\testado\n";
  std::cout << "01\tlinterna\tencendida\n";
  std::cout << "02\tpuerta\tsellada\n";
}
```

## Las cinco piezas

| Línea | Pieza | Qué aporta |
| :--- | :--- | :--- |
| `#include <iostream>` | directiva de preprocesador | Copia las declaraciones de entrada/salida en esta unidad |
| `int main()` | punto de entrada | Donde empieza la ejecución; devuelve un `int` a la terminal |
| `{` `}` | bloque | Todo lo que hay entre ellas es el cuerpo de `main` |
| `std::cout <<` | sentencia | Una acción: enviar texto a la consola |
| `\t`, `\n` | secuencias de escape | Una tabulación y un salto de línea dentro de una cadena normal |

El include no es una importación de biblioteca en tiempo de ejecución. Es un **copiar y pegar que
ocurre antes de compilar**: las declaraciones de la cabecera aterrizan arriba de tu archivo.

## Salida

```text
ranura	nombre	estado
01	linterna	encendida
02	puerta	sellada
```

Las tabulaciones alinean las columnas, que es justo lo que una tabla de consola necesita antes de
aprender a dar formato de verdad.

> [!NOTE]
> A C++ le da igual la indentación y los saltos de línea. Las llaves deciden la estructura. El
> formato es para las personas, y cada guía de estilo del mundo tiene una opinión al respecto.

> [!WARNING]
> Las barras invertidas, las comillas y los caracteres de control son donde se pierde una hora:
> `\n` es un salto de línea, pero `\\n` es una barra literal seguida de una `n`. Ver
> [[05 - Velocidad de Escape]].

---

**Siguiente:** [[04 - Notas al Margen]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
