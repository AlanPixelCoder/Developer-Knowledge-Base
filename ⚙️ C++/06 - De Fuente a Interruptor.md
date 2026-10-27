# 06. De Fuente a Interruptor

**Versión original en inglés:** [06 - From Source to Switch](./06%20-%20From%20Source%20to%20Switch.md)

**Curso:** C++
**Capítulo:** 1 — Primer Arranque
**Tema:** Compilar y ejecutar: fuente, objeto, ejecutable
**Etiquetas:** `#cpp` `#toolchain` `#gcc`

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

El motor no puede arrancar desde un archivo `.cpp`. La máquina solo entiende instrucciones, así que
alguien tiene que traducir. Ese alguien es la cadena de herramientas, y tiene tres etapas.

| Etapa | Qué ocurre | Resultado |
| :--- | :--- | :--- |
| Preproceso | Se copian las cabeceras, se expanden las macros | Una unidad de traducción grande |
| Compilación | Esa unidad pasa a ensamblador y luego a código máquina | `main.o` |
| Enlazado | Se unen objetos y bibliotecas, `main` pasa a ser el punto de entrada | `ember` |

El driver hace las tres cuando le pides un ejecutable:

```bash
g++ -std=c++17 -Wall -Wextra -O2 main.cpp -o ember
./ember
```

## Leer el comando

| Bandera | Significado |
| :--- | :--- |
| `-std=c++17` | Usa el estándar C++17, para que el compilador deje de adivinar |
| `-Wall -Wextra` | Activa los avisos que atrapan errores reales |
| `-O2` | Optimiza; el motor no va a ser rápido por casualidad |
| `-o ember` | Nombra la salida `ember` en lugar de `a.out` |
| `./ember` | Ejecuta el archivo de la carpeta actual: el `./` no es decoración |

> [!WARNING]
> `-o` toma la palabra siguiente como nombre de salida. `g++ -o main.cpp ember` construye un
> programa llamado `main.cpp` a partir de un archivo llamado `ember`, y el mensaje de error será
> desconcertante.

> [!CAUTION]
> Después de una compilación fallida, el ejecutable anterior sigue ahí. Ejecutar `./ember` y ver el
> comportamiento de antes es la señal clásica de que la compilación nunca terminó y nadie leyó la
> salida.

> [!TIP]
> Encadena los dos pasos para que una compilación fallida nunca se ejecute:
> `g++ main.cpp -o ember && ./ember`. El `&&` corre el segundo comando solo si el primero terminó
> bien.

---

**Siguiente:** [[07 - Materia Prima]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
