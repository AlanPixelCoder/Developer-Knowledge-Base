# 31. Fuera de Oficina

**Versión original en inglés:** [31 - OOO.md](./31%20-%20OOO.md)

**Curso:** C++
**Tema:** Parámetros vs argumentos
**Etiquetas:** `#cpp` `#functions` `#parameters` `#arguments`

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

A veces una función realiza una tarea que varía según la entrada o entradas.

## Parámetros

Los **parámetros** son las variables que una función recibe como entrada. Van dentro de los
paréntesis en la **definición** de la función y se usan dentro del cuerpo. Cada parámetro necesita un
tipo de dato.

```cpp
void mensaje_fuera_oficina(std::string fecha) { // 'fecha' es el parámetro
  // ...
}
```

## Argumentos

Un **argumento** es el valor que se **envía** a la función cuando se **llama**.

```cpp
mensaje_fuera_oficina("Lunes"); // "Lunes" es el argumento
```

## La diferencia

| | Cuándo | Qué es |
| :--- | :--- | :--- |
| **Parámetro** | Al definir | La variable listada dentro de los paréntesis |
| **Argumento** | Al llamar | El valor real que se pasa |

> [!TIP]
> **Mnemotecnia**
> **P**arámetro = **P**laceholder (marcador). **A**rgumento = **A**ctual (valor real).

## Ejemplo

```cpp
#include <iostream>
#include <string>

void mensaje_fuera_oficina(std::string fecha) {
  std::cout << "Gracias por tu correo.\n";
  std::cout << "Estoy fuera de la oficina y volveré el " << fecha << ".\n";
  std::cout << "Responderé en cuanto regrese.\n\n";
}

int main() {
  mensaje_fuera_oficina("Lunes");
  mensaje_fuera_oficina("2 de noviembre");
}
```

> [!NOTE]
> Cada llamada recibe una **copia nueva** del parámetro. Llamar dos veces con argumentos distintos
> produce dos cartas distintas, y ninguna sobrescribe a la otra.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
