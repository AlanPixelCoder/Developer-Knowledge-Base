# 23. Protocolo de Cuenta Atrás

**Versión original en inglés:** [23 - Countdown Protocol](./23%20-%20Countdown%20Protocol.md)

**Curso:** C++
**Capítulo:** 4 — Iteración
**Tema:** Bucles decrementales y la dirección de una cuenta atrás
**Etiquetas:** `#cpp` `#for` `#decrement`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-BEGINNER-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Chapter-4-7C5CFF?style=for-the-badge" alt="Chapter 4">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

La consola anuncia un apagado y cuenta los ticks que le quedan. Contar hacia atrás es el mismo bucle
con el incremento invertido, y un detalle decide si el último tick se imprime.

```cpp
#include <iostream>

int main() {
  for (int ticks_restantes = 5; ticks_restantes > 0; ticks_restantes--) {
    std::cout << ticks_restantes << " ticks para el apagado\n";
  }

  std::cout << "motor detenido\n";
}
```

## Salida

```text
5 ticks para el apagado
4 ticks para el apagado
3 ticks para el apagado
2 ticks para el apagado
1 ticks para el apagado
motor detenido
```

## Qué cambia al contar hacia atrás

| Dirección | Cabecera | Se detiene cuando |
| :--- | :--- | :--- |
| Hacia arriba | `for (int i = 0; i < n; i++)` | `i` llega a `n` |
| Hacia abajo | `for (int i = n; i > 0; i--)` | `i` llega a `0` |

La comparación se invierte con la dirección. Mantener `i <= n` mientras decrementas da un bucle que
nunca empieza, que al menos es fácil de detectar.

> [!CAUTION]
> Si el contador es `unsigned`, `i--` en cero da la vuelta al valor más grande posible y la condición
> `i >= 0` siempre es verdadera. Un contador con signo evita el problema por completo; los
> contenedores usan índices sin signo, así que ahí cuenta hacia atrás con cuidado.

> [!NOTE]
> `i--` devuelve el valor *antes* de decrementar; `--i` lo devuelve después. Dentro del cuerpo del
> bucle la diferencia es invisible; dentro de una expresión o una condición es toda la historia.

> [!TIP]
> Cuenta hacia atrás con `> 0` en lugar de `>= 0` salvo que quieras de verdad la pasada del cero. El
> mensaje de apagado va después del bucle, donde se imprime exactamente una vez.

---

**Siguiente:** [[24 - La Prueba del Patrón]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
