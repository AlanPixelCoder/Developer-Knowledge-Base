# Arrays en C++

**Versión original en inglés:** [Arrays.md](./Arrays.md)

**Curso:** C++
**Tema:** Arrays estilo C vs vectores
**Etiquetas:** `#cpp` `#arrays` `#data-structures` `#memory`

<p align="left">
  <img src="https://img.shields.io/badge/Lenguaje-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Estado-Completo-00C2A8?style=for-the-badge" alt="Completo">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Bóveda-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

Los arrays clásicos de C++ se conocen como **arrays estilo C**.

La mayor diferencia entre arrays y vectores es que un array tiene **tamaño fijo**: no puede crecer ni
encogerse.

## Sintaxis

```cpp
int loteria[6];                          // array de 6 enteros
int loteria[6] = {6, 7, 25, 46, 57, 12}; // inicializado
```

## Arrays vs vectores

| Característica | Arrays | Vectores |
| :--- | :--- | :--- |
| **Tamaño** | Fijo en tiempo de compilación | Dinámico: crece y se encoge |
| **Sintaxis** | Estilo C básico | Moderna (`std::vector`) |
| **Memoria** | Pila | Montículo (heap) |
| **Velocidad** | Muy rápida | Muy rápida, algo más lenta que un array |
| **Cuándo usarlos** | Conoces el tamaño de antemano y no cambiará. Quieres algo más de velocidad. Trabajas en bajo nivel, hardware o robótica donde controlas la memoria. | Necesitas flexibilidad para añadir y quitar elementos |

> [!TIP]
> ¿Trabajas con C++ moderno? `std::array` te da un array de tamaño fijo con `.size()` y semántica más
> segura: el punto medio sensato entre `int arr[6]` y `std::vector`.

> [!NOTE]
> Los arrays no conocen su propio tamaño. No existe `arr.size()`. Pasas la longitud aparte o usas
> `std::size(arr)`. Esa contabilidad es justo lo que los vectores hacen por ti, y justo por eso
> reemplazaron a los arrays en el código diario.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
