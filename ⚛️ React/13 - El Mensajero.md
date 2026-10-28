# 13. El Mensajero

**Versión original en inglés:** [[13 - The Courier](13%20-%20The%20Courier.md)

**Curso:** React
**Capítulo:** II. El Arte de los Componentes
**Tema:** Forjar la siguiente pieza de la Consola del Arsenal
**Etiquetas:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO_BAJO-6CC24A?style=for-the-badge" alt="Intermedio bajo">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 06">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

La reconstrucción de la Consola del Arsenal continúa. Este capítulo añade la siguiente pieza al sistema, siguiendo la misma disciplina: describir la interfaz a partir de los datos, mantener los límites claros y componer piezas pequeñas en algo fiable.

> [!NOTE]
> Cada nueva pieza debe reforzar el flujo unidireccional. Si un valor pertenece a este componente y cambia, va en el estado. Si viene de arriba, va en las props.

## Forjar la pieza

El patrón se mantiene. Los componentes siguen siendo pequeños, centrados y reutilizables. Las expresiones, condiciones y hooks adecuados mantienen el comportamiento predecible sin manipular el DOM directamente.

```javascript
function PanelConsola() {
  return (
    <section className="panel-consola">
      <h3>Panel del Arsenal</h3>
      <p>Forjado para encajar en la arquitectura de la consola.</p>
    </section>
  );
}
```

> [!TIP]
> Antes de añadir lógica, conviene comprobar si algún patrón anterior ya resuelve el problema.

## Por qué encaja

Cada panel debe cooperar con los demás. Mantener el estado local cuando sea posible, pasar los datos explícitamente y evitar efectos innecesarios hace que todo el árbol sea más fácil de razonar y depurar.

> [!WARNING]
> No hay que duplicar datos ni romper el flujo. Si varios componentes necesitan el mismo valor cambiante, hay que elevarlo o usar contexto solo cuando las props resulten inviables.

## Salida

```text
PanelConsola renderizado
Límites respetados: props hacia abajo, eventos hacia arriba
Patrón coherente con la reconstrucción del Arsenal
```

**Siguiente:** [[14 - El Mapa del Mundo]]
