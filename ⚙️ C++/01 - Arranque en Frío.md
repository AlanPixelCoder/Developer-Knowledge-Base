# 01. Arranque en Frío

**Versión original en inglés:** [01 - Cold Start](./01%20-%20Cold%20Start.md)

**Curso:** C++
**Capítulo:** 1 — Primer Arranque
**Tema:** Qué es C++, de dónde viene y el archivo del que parte todo
**Etiquetas:** `#cpp` `#foundations` `#toolchain`

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

Todo lo que viene en este módulo pertenece a un estudio imaginario y a un producto imaginario: el
**motor Emberfall**, la consola con la que un equipo pequeño arranca, configura y depura su juego.
La primera lección no trata del juego: trata del archivo con el que se construye el motor.

## De dónde viene el lenguaje

Bjarne Stroustrup lo empezó en los laboratorios Bell en **1979** como *C with Classes*: la
velocidad de C y su acceso directo a la memoria, más la posibilidad de definir tus propios tipos.
En 1983 pasó a llamarse **C++**, y los estándares que hoy importan llegaron décadas después:
C++11, C++17, C++20, C++23.

## Para qué se usa

| Terreno | Por qué C++ y no algo más cómodo |
| :--- | :--- |
| Motores de juego | El presupuesto de un fotograma se mide en milisegundos; no cabe una pausa del recolector |
| Sistemas operativos | El código tiene que correr antes de que exista cualquier runtime |
| Navegadores | Analizar, maquetar y ejecutar a velocidad interactiva |
| Trading, simulación, embebido | Tiempos deterministas y memoria predecible |

El intercambio es explícito: tú gestionas la memoria y los tipos, y a cambio obtienes un control
que ningún lenguaje de script ofrece.

## El archivo en el que vas a vivir

El código C++ vive en archivos `.cpp`. Cada uno es una **unidad de traducción**: el compilador lo
lee por su cuenta, sin saber de los demás, y produce un archivo objeto. Una de esas unidades
contiene `main`, el punto de entrada donde el sistema operativo arranca tu programa.

```cpp
int main() {
  return 0;
}
```

`return 0;` es el código de salida que recibe la terminal: cero significa *terminó sin errores*.
Este programa no hace nada más, y ya compila, enlaza y se ejecuta.

> [!NOTE]
> Un archivo `.cpp` se compila aislado. Por eso la misma cabecera se incluye en muchos archivos:
> cada unidad necesita conocer las declaraciones por sí misma.

> [!TIP]
> Nombra el archivo por lo que contiene — `consola_motor.cpp`, `tabla_aparicion.cpp` — y no por el
> número de lección. Al compilador le da igual; a quien abra la carpeta después, no.

---

**Siguiente:** [[02 - Primera Luz]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
