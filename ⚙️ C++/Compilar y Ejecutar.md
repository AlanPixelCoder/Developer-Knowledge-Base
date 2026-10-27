# Compile & Execute

**Versión original en inglés:** [Compile & Execute.md](./Compile%20%26%20Execute.md)

**Curso:** C++
**Tema:** Compiladores, código fuente y ejecución en terminal
**Etiquetas:** `#cpp` `#compiler` `#terminal` `#execution`

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

## ¿Qué es compilar?

C++ es un lenguaje **compilado**. Para que un programa se ejecute, primero hay que traducirlo de una
forma legible por humanos (**código fuente**) a algo que la máquina entienda (**código máquina** o
**ejecutable**). Esa traducción la hace un **compilador**.

El proceso completo se ve así:

1. Escribir código.
2. Guardar el programa.
3. Compilar y ejecutar.
4. Repetir.

- Los archivos de código fuente tienen extensión `.cpp` (por ejemplo `calculadora.cpp`).
- Los archivos de código máquina tienen extensión `.out` (por ejemplo `calculadora.out`).

## Ejecutar en la terminal

### Compilar

Un compilador traduce el programa a lenguaje máquina. En la terminal escribe `g++` seguido del nombre
del archivo y pulsa enter.

```bash
g++ hola.cpp
```

Esto crea un archivo de código máquina normalmente llamado `a.out`.

### Ejecutar

Para ejecutar el archivo de código máquina, escribe `./` seguido del nombre del archivo y pulsa
enter.

```bash
./a.out
```

### Nombrar el ejecutable

También puedes dar un nombre propio al ejecutable con la bandera `-o`:

```bash
g++ hola.cpp -o hola
./hola
```

> [!TIP]
> En términos de Emberfall: escribir `.cpp` es forjar tu libro de hechizos. Compilar es encantarlo.
> Ejecutar es lanzarlo en la arena de la terminal.

> [!NOTE]
> **Ver errores con contexto**
> Compila con `g++ -Wall -Wextra -std=c++17 archivo.cpp -o archivo`. Las advertencias señalan
> comparaciones sospechosas, variables sin usar y errores silenciosos como `=` en lugar de `==`.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
