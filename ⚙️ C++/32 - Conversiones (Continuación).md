# 32. Conversiones (Continuación)

**Versión original en inglés:** [32 - Conversions (Continuation).md](./32%20-%20Conversions%20%28Continuation%29.md)

**Curso:** C++
**Tema:** Retornar valores y llamar funciones
**Etiquetas:** `#cpp` `#functions` `#return` `#conversion`

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

Cuando una función devuelve un valor, podemos usarlo directamente en una sentencia de salida o
asignarlo a una variable.

> [!NOTE]
> Cuando se alcanza un `return`, C++ detiene la ejecución de la función actual y envía un valor al
> lugar donde se llamó.

## Ejemplo

```cpp
#include <iostream>

// Recibe BPM, devuelve segundos por pulso
double bpm_a_segundos(double bpm) {
  return 60.0 / bpm;
}

int main() {
  double bpm_pista = 140.0;

  std::cout << "Analizando pista...\n";
  std::cout << "Tempo: " << bpm_pista << " BPM\n";

  // Usar el valor retornado directamente en la salida
  std::cout << "Tiempo por pulso: " << bpm_a_segundos(bpm_pista) << " segundos\n";

  // Llamarla otra vez con otro argumento
  std::cout << "\nAnalizando pista ambiental...\n";
  std::cout << "Tempo: 90 BPM\n";
  std::cout << "Tiempo por pulso: " << bpm_a_segundos(90.0) << " segundos\n";
}
```

## Salida

```text
Analizando pista...
Tempo: 140 BPM
Tiempo por pulso: 0.428571 segundos

Analizando pista ambiental...
Tempo: 90 BPM
Tiempo por pulso: 0.666667 segundos
```

> [!NOTE]
> La fórmula: $\text{segundos por pulso} = \dfrac{60}{\text{BPM}}$. A 120 BPM un pulso dura medio
> segundo; duplica el tempo y el pulso se reduce a la mitad.

> [!TIP]
> `60.0` —no `60`— es lo que mantiene la división en punto flotante. Escribe `60 / bpm` con dos
> enteros y obtendrías `0`. La misma trampa que en [[09 - Temperatura]].

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
