# 19. Introducir PIN

**Versión original en inglés:** [19 - Enter PIN.md](./19%20-%20Enter%20PIN.md)

**Curso:** C++
**Tema:** Introducción a los bucles
**Etiquetas:** `#cpp` `#loops` `#while` `#iteration`

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

En programación, un **bucle** repite un bloque de código hasta que se cumple una condición. Es una
herramienta increíblemente potente y se usa todo el tiempo.

A menudo se dice **iterar** al hablar de bucles: iterar simplemente significa "repetir".

Hay dos tipos de bucles que veremos:

- bucles `while`
- bucles `for`

## El bucle `while`

Piensa en el `while` como una rotonda: cada vuelta es una **iteración**. Un coche dará vueltas y
vueltas hasta que ya no pueda más.

```cpp
while (condicion) {
  // se ejecuta una y otra vez mientras la condición sea true
}
```

> [!WARNING]
> **El bucle infinito**
> Si la condición nunca se vuelve `false`, el programa nunca sale del bucle. Dentro de un `while`
> que depende de la entrada del usuario, asegúrate de que la lectura esté *dentro* del bucle; si no,
> se comprueba la misma respuesta para siempre.

## Anatomía de un bucle que termina

| Pieza | Propósito |
| :--- | :--- |
| Un estado inicial | Algo es `true` antes de empezar |
| Una condición | Se comprueba antes de cada iteración |
| Un cuerpo | El trabajo, que debe acercar el estado hacia `false` |
| Un cambio | Normalmente dentro del cuerpo, a menudo releer la entrada |

> [!TIP]
> Di el bucle en voz alta antes de escribirlo: *"mientras el PIN sea incorrecto, pregunta otra vez"*.
> Si no puedes terminar la frase, todavía no tienes la condición de salida.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
