# 41. La Caja Fuerte, Conectada

**Versión original en inglés:** [41 - The Relic Safe, Wired](./41%20-%20The%20Relic%20Safe%2C%20Wired.md)

**Curso:** C++
**Capítulo:** 7 — Entidades
**Tema:** Constructores delegados y construcción por defecto
**Etiquetas:** `#cpp` `#class` `#delegating-constructor`

<p align="left">
  <img src="https://img.shields.io/badge/Language-C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Difficulty-INTERMEDIATE-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Chapter-7-7C5CFF?style=for-the-badge" alt="Chapter 7">
  <img src="https://img.shields.io/badge/Lore-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=70&section=header" width="100%" alt="C++ wave" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #00599C, #4FC3F7, #00599C, transparent); margin: 24px 0;" />

La cámara ahora envía dos variantes: una caja de archivo con cuatro discos y una de expedición con
dos. Ambas comparten las mismas reglas, así que el segundo constructor pasa su trabajo al primero en
lugar de repetir la validación.

```cpp
#include <iostream>
#include <string>

class CajaReliquias {
 public:
  CajaReliquias(std::string duenio, int discos)
      : duenio_(duenio), discos_(discos < 3 ? 3 : discos), cerrada_(true) {}

  CajaReliquias() : CajaReliquias("sin asignar", 3) {}          // por defecto: delega
  CajaReliquias(std::string duenio) : CajaReliquias(duenio, 3) {}  // un argumento

  std::string describir() const {
    return duenio_ + " / " + std::to_string(discos_) + " discos / " +
           (cerrada_ ? "cerrada" : "abierta");
  }

 private:
  std::string duenio_;
  int discos_;
  bool cerrada_;
};

int main() {
  CajaReliquias a;
  CajaReliquias b("mensajera");
  CajaReliquias c("expedicion", 2);   // recortada a 3

  std::cout << a.describir() << "\n";
  std::cout << b.describir() << "\n";
  std::cout << c.describir() << "\n";
}
```

## Salida

```text
sin asignar / 3 discos / cerrada
mensajera / 3 discos / cerrada
expedicion / 3 discos / cerrada
```

## Un constructor que conoce las reglas

| Constructor | Delega en | Por qué |
| :--- | :--- | :--- |
| `CajaReliquias(duenio, discos)` | — | el que valida |
| `CajaReliquias()` | `CajaReliquias("sin asignar", 3)` | estado vacío con sentido |
| `CajaReliquias(duenio)` | `CajaReliquias(duenio, 3)` | comodidad de un argumento |

La delegación ejecuta primero el constructor destino y después su cuerpo. Las reglas viven en un solo
sitio, así que cambiar el mínimo de discos cambia todos los caminos a la vez.

## La regla de la que depende `CajaReliquias a;`

Sin `CajaReliquias()`, `CajaReliquias a;` no compila, y normalmente ese es el resultado correcto. Una
caja que existe sin dueño solo es útil si "sin dueño" es un estado con sentido; aquí se escribe
explícitamente en lugar de llegar como memoria sin inicializar.

> [!WARNING]
> `CajaReliquias a();` no es un objeto, es la declaración de una función. El "parse más irritante"
> pica a todo el mundo una vez. Usa `CajaReliquias a;` o `CajaReliquias a{};` cuando quieras un
> objeto.

> [!TIP]
> Si dos constructores tendrían cuerpos idénticos, borra uno y da argumentos por defecto al otro. La
> delegación es para cuando los cuerpos difieren pero deben compartir las mismas garantías.

---

**Siguiente:** [[42 - Nacer con Atributos]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00599C&height=60&section=footer" width="100%" alt="C++ footer" />
</p>
