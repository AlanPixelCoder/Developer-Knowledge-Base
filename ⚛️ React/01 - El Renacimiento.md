# 01. El Renacimiento

**Versión original en inglés:** [01 - The Rebirth.md](01%20-%20The%20Rebirth.md)

**Curso:** React
**Tema:** Qué es React, su historia, el diseño declarativo y basado en componentes, características clave y la comparación antes vs. con React
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-01_--_05-7C5CFF?style=for-the-badge" alt="Lecciones 01 a 05">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

La tecnología detrás del **sitio companion de Emberfall Online** — el panel del gremio, la
tienda y el feed social donde cada jugador se detiene entre partida y partida. Este capítulo
inicial es el pergamino de lore: qué es React, quién lo forjó en **2013**, las dos leyes de
diseño que obedece y la vieja forma de parchear páginas a mano que reemplazó. La referencia
rápida de todo el capítulo está en [[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> React es una librería JavaScript declarativa y basada en componentes: tú describes **qué**
> debe mostrar la interfaz para un conjunto de datos, y React mantiene la página en
> sincronía — en vez de que tú persigas nodos del DOM y los parchees a mano.

---

## 01. La Leyenda de React

> [!NOTE]
> **Información clave**
> **React** es una **librería JavaScript** de código abierto, presentada en **2013**,
> creada por un pequeño equipo de ingeniería de **Facebook** (**Jordan Walke**) para
> optimizar la función Newsfeed. Hoy también alimenta Instagram, Netflix y Airbnb.

React es una **librería**, no un framework completo: se centra en un trabajo y lo hace
extremadamente bien — construir la **interfaz de usuario**. Es una librería declarativa y
basada en componentes para interfaces dinámicas. En lugar de rastrear y actualizar manualmente
elementos del DOM repartidos en archivos separados, compones **componentes** reutilizables
que se actualizan en tiempo real cuando cambian los datos.

| Aliado | Qué ejecuta React para ellos |
| :--- | :--- |
| **Facebook / Meta** | El Newsfeed para el que nació |
| **Instagram** | La aplicación web de instagram.com |
| **Netflix** | Partes de la interfaz de navegación |
| **Airbnb** | Resultados de búsqueda y flujos de reserva |
| **Emberfall Online** | El sitio companion que construirás en este curso |

### Misión: La Auditoría del Escriba

Cada pantalla del sitio companion es candidata a React. En una hoja de papel, lista cinco
pantallas del sitio de Emberfall — el HUD del gremio, la tienda, el feed social, el tablero
de misiones, el test de clase — y anota junto a cada una qué pieza **cambia con la página
abierta**. Esas piezas que cambian son exactamente los datos de los que React se encargará.

---

## 02. Las Dos Leyes

### Ley primera: declarativa

Una librería **declarativa** te deja describir el resultado deseado y la librería calcula los
pasos. Tú dices *«la barra de vida muestra 72 de 100»* — React descubre qué nodo de texto
tocar y lo toca. La alternativa imperativa es el hechizo antiguo: ve, busca `#guild-hp`,
lee sus hijos, reemplaza el texto y recuerda hacerlo también en los otros tres archivos que
muestran el mismo número.

### Ley segunda: basada en componentes

La interfaz se descompone en **componentes** — funciones pequeñas y reutilizables que cada
una renderiza una pieza de la pantalla. Un componente recibe datos, devuelve marcado y se
vuelve a renderizar cuando sus datos cambian. La barra de vida y la lista de misiones del
HUD del gremio son dos componentes; cambia los datos de fondo y ambos se actualizan **en
tiempo real**, sin recargar la página y sin que tú escribas la lógica de actualización dos
veces.

> [!TIP]
> Piensa en un componente como una escena reutilizable de un motor de juego: la creas una
> vez, la insertas en veinte pantallas y un cambio en la escena original se propaga a todas
> las instancias.

### Misión: Dibuja el Árbol del Grupo

Toma el HUD del gremio de la misión anterior y divídelo en componentes. Dibújalo como un
árbol: una caja por componente y líneas hacia sus hijos. Una primera división razonable es
`GuildHud` que contiene `HealthBar`, `QuestList` y `PlayerBadge`. Acabas de diseñar tu
primera jerarquía de componentes React; los capítulos [[03 - Taller de Glifos]] y
[[04 - Marcado Vivo]] enseñan a escribirla de verdad.

---

## 03. Los Cuatro Runes

Toda la publicidad de React se reduce a cuatro características. Aprende a nombrarlas y podrás
explicar la librería en treinta segundos:

| Característica | Qué significa | En el sitio companion |
| :--- | :--- | :--- |
| **Arquitectura guiada por componentes** | La interfaz se construye con componentes pequeños, reutilizables e independientes | El HUD, el feed y la tienda se ensamblan con tarjetas compartidas |
| **Sintaxis JSX** | Marcado tipo HTML escrito directamente dentro de JavaScript | Las páginas se escriben en un lenguaje, no en tres |
| **Actualizaciones DOM eficientes** | React toca **solo lo que cambió** en la página real | Un nuevo contador de likes repinta un número, no el feed entero |
| **Alta escalabilidad y rendimiento** | El modelo aguanta desde una landing hasta una app enorme | El sitio companion puede crecer hasta ser una red social completa |

> [!NOTE]
> El tercer rune — *solo lo que cambió* — es el que sentirás en el capítulo
> [[02 - Punto de Aparición]] en cuanto guardes un archivo y el servidor de desarrollo
> repinte la pantalla más rápido de lo que puedes cambiar de ventana.

### Misión: Recita los Runes

Cubre la tabla y escribe las cuatro características de memoria. Después, para cada una,
nombra una pantalla del sitio companion donde importe. Si no logras situar la *Sintaxis JSX*
en ninguna, has encontrado el hueco que este curso rellena.

---

## 04. El Pacto Antiguo vs. el Pacto de React

### Antes de React

La manipulación tradicional del DOM consiste en buscar elementos en cada documento HTML y
modificarlos manualmente con JavaScript puro. El mismo valor mostrado en tres lugares
significa tres llamadas a `querySelector`, tres asignaciones y tres oportunidades de olvidar
una cuando el marcado cambia. Es **repetitivo y propenso a errores**:

```javascript
// La forma antigua: persigue el elemento y parchéalo a mano —
// y repite en cada archivo que muestre el mismo valor
const hpBar = document.querySelector("#guild-hp");
hpBar.textContent = "HP: 72 / 100";

const questLine = document.querySelector("#quest-line");
questLine.textContent = "Deep Halls — barre el tercer piso";
```

Si te saltas una de esas actualizaciones, la interfaz miente al jugador: el HUD dice 72
mientras el servidor ya aplicó el golpe.

### Con React

El modelo de React centraliza la lógica de interfaz en componentes. Actualizas los datos
**una vez** y el cambio se aplica **en todas partes donde se renderice el componente**:

```javascript
// La forma React: un componente es dueño de la lógica de presentación
function HealthBar(props) {
  return <div className="hp-bar">HP: {props.hp} / 100</div>;
}

// Actualiza los datos una vez — todo lugar donde se muestre la barra sigue
<HealthBar hp={72} />
```

Hay una sola definición de la barra de vida, así que hay un solo lugar que actualizar y un
solo lugar que romper. El tratamiento completo de cómo llega los datos a un componente llega
en un capítulo posterior sobre props; de momento, retén la forma: **centraliza, actualiza una
vez, aplica en todas partes**.

> [!WARNING]
> **El error clásico**
> Parchear el DOM a mano (`querySelector`, `innerHTML`) dentro de una app React. React
> guarda su propia idea de lo que contiene la página — los edits manuales desalinean esa
> copia y el siguiente cambio de datos los sobreescribe en silencio. En React, los datos y
> el marcado cambian **a través de los componentes**, nunca a su alrededor.

### Misión: Porta un Parche

Toma cualquier parche con `querySelector` que escribiste en el curso de JavaScript — una
lectura de HUD, una línea de recibo, un contador — y reescríbelo como un componente que
reciba el valor y lo imprima. Cuenta las líneas que borraste. Esa razón es la existencia
misma de React.

---

## 05. El HUD Vivo

### Checkpoint: Resumen del capítulo

- React es una **librería JavaScript** de código abierto de **2013**, creada en **Facebook**
  por el equipo de **Jordan Walke** para el Newsfeed.
- Es **declarativa**: tú describes el resultado, React ejecuta el trabajo del DOM.
- Es **basada en componentes**: la interfaz son piezas reutilizables que se vuelven a
  renderizar cuando cambian los datos.
- Las cuatro características: arquitectura guiada por componentes, sintaxis JSX,
  actualizaciones DOM eficientes, alta escalabilidad y rendimiento.
- Antes de React: buscar y parchear elementos a mano, en todas partes. Con React: la lógica
  centralizada, se actualiza una vez y se aplica en todas partes.

### El HUD del Gremio

Este es el ejemplo marco hacia el que apunta todo el curso: un HUD del gremio donde la barra
de vida y la lista de misiones son componentes que se actualizan en vivo cuando cambian los
datos de fondo.

```javascript
function GuildHud() {
  const hp = 84;
  const nextQuest = "Deep Halls — barre el tercer piso";

  return (
    <div className="guild-hud">
      <h2>WardenOfTheNinth</h2>
      <div className="hp-bar">HP: {hp} / 100</div>
      <p className="quest-line">Siguiente misión: {nextQuest}</p>
    </div>
  );
}
```

Cambia `hp` y cambia el texto de la barra. Cambia `nextQuest` y cambia la línea de misión.
Nada más en la página se mueve, porque nada más cambió — ese es el cuarto rune en acción.

> [!TIP]
> **Versión para game dev**
> HTML etiqueta el contenido, CSS lo estiliza, JavaScript se ejecuta — React es el ejército
> que los mantiene en sincronía. En un motor de juego tampoco hurgas en buffers de píxeles:
> cambias los *datos* de una entidad y el renderizador la redibuja. React trae esa disciplina
> al navegador, y el siguiente capítulo, [[02 - Punto de Aparición]], instala el toolchain
> que lo ejecuta.

---

## ⚡ XP Ganados: Ideas Clave

- 🧬 **React es una librería** — de código abierto, presentada en **2013**, nacida en
  **Facebook** (**Jordan Walke**) para el Newsfeed; también ejecuta Instagram, Netflix y Airbnb.
- 📜 **Declarativa** significa que describes la interfaz deseada y React ejecuta las
  actualizaciones del DOM.
- 🧩 **Basada en componentes** significa que la interfaz son piezas reutilizables que se
  actualizan en tiempo real cuando cambian los datos — se acabó parchear el mismo valor en
  cinco archivos.
- 🔮 Los cuatro runess: arquitectura guiada por componentes, sintaxis JSX, actualizaciones
  DOM eficientes (solo lo que cambió), alta escalabilidad y rendimiento.
- ⚔️ Antes de React: parches manuales, repetitivos y propensos a errores con `querySelector`.
  Con React: lógica de componente centralizada — se actualiza una vez y se aplica en todas
  partes.
- 🎯 El HUD del gremio es el objetivo: una barra de vida y una lista de misiones que se
  actualizan en vivo.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 📰 Dashboards cargados de datos cuyos valores se refrescan sin recargar (feeds, tickers)
- 🛒 Tiendas cuyo carrito, stock y precios cambian mientras navegas
- 🎮 Sitios companion y herramientas de segunda pantalla para juegos en vivo
- 🧱 Sistemas de diseño: un componente de tarjeta reutilizado en docenas de pantallas
- 🔄 Todo lo que antes eran veinte parches con `querySelector` y una plegaria

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Escribe el bloque de datos de React (librería, 2013, Facebook, Jordan Walke, Newsfeed)
   de memoria y compruébalo contra esta página.
2. Nombra tres aplicaciones que uses a diario y busca pruebas de React en su frontend web.
3. Divide en componentes una página que ya hayas construido (curso de HTML) y dibuja el
   árbol de jerarquía.
4. Reescribe un parche imperativo con `querySelector` de un proyecto antiguo como componente.
5. **Pelea de jefe:** toma el Recibo del Mercader del curso de JavaScript y describe, línea
   por línea, qué partes son **datos** (artículos, precios, total) y cuáles son
   **presentación** — y luego dibuja los componentes que construirías para que el total se
   recalcule solo.

---

## 🔗 Ver También

- [[02 - Punto de Aparición]] — siguiente capítulo: Node.js, Vite y el arranque de tu primera app React
- [[03 - Taller de Glifos]] — JSX: la sintaxis de marcado en la que se escriben los cuatro runess
- [[04 - Marcado Vivo]] — expresiones, condicionales y atributos dentro de ese marcado

---
