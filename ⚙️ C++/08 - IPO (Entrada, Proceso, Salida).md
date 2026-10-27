# 08. IPO (Entrada, Proceso, Salida)

**Versión original en inglés:** [08 - IPO.md](./08%20-%20IPO.md)

**Curso:** C++
**Tema:** Inicialización y actualización de variables
**Etiquetas:** `#cpp` `#variables` `#initialization`

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

**E**ntrada → **P**roceso → **S**alida. Todo programa de este módulo sigue esa forma, y las
variables son donde ocurre el paso del medio.

Después de declarar una variable podemos darle un valor. Eso se llama **inicialización**.

```cpp
int puntuacion;
puntuacion = 0;
```

- `puntuacion` es el nombre de la variable.
- `=` significa **asignación**, no "igual a". En C++ el signo igual dice *guarda este valor en esta
  caja*, no *estas dos cosas son lo mismo*.
- `;` termina la sentencia.

Puedes actualizar el valor tantas veces como quieras después:

```cpp
puntuacion = 10;
puntuacion = 8;
```

## Imprimir variables

Imprime el valor de una variable poniendo su nombre después de `<<` **sin** comillas dobles.

```cpp
std::cout << puntuacion; // Salida: 8
```

> [!WARNING]
> `std::cout << "puntuacion";` imprime la palabra `puntuacion`. `std::cout << puntuacion;` imprime
> `8`. Las comillas son toda la diferencia, y es uno de los errores más comunes al empezar.

> [!TIP]
> **Declarar e inicializar en una línea**
> `int puntuacion = 0;` es equivalente a las dos líneas anteriores y elimina la ventana en la que la
> variable existe pero contiene basura.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
