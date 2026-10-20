# 08. La Barra de Vida

**Versión original en inglés:** [08 - The Health Bar.md](08%20-%20The%20Health%20Bar.md)

**Curso:** React
**Tema:** qué es el estado, `useState`, anatomía del hook, la función setter, inmutabilidad, actualizar el estado, actualizaciones asíncronas y con temporizadores, actualizaciones funcionales
**Tags:** `#react` `#web-development` `#frontend` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-FFA500?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-01_--_06-7C5CFF?style=for-the-badge" alt="Lecciones">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=61DAFB&height=70&section=header" width="100%" alt="Ola cian" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #61DAFB, #2DD4BF, #61DAFB, transparent); margin: 24px 0;" />

Un HUD con números fijos es una captura de pantalla. La **barra de vida** es el momento en
que un componente de React deja de ser una pintura y se convierte en un instrumento vivo:
posee datos, esos datos cambian, y cada cambio repinta la pantalla. Este capítulo presenta
el **estado** y el hook `useState` — el motor central detrás de cada contador, cuenta de
pociones, campo de formulario y medidor de XP del sitio companion de Emberfall.
Referencia: [[00b - Chuleta de React]].

> [!NOTE]
> **Todo el capítulo en una frase**
> El **estado** son los datos internos de un componente que se espera que cambien con el
> tiempo; guárdalos con `const [valor, setValor] = useState(valorInicial)` y cada llamada
> al setter vuelve a renderizar el componente con el valor fresco — pero solo a través del
> setter.

---

## 01. El Medidor Vital

> [!NOTE]
> **Información clave**
> El estado son **datos internos de un componente que se espera que cambien con el tiempo**
> — contadores, artículos del carrito, entradas de formulario, XP del gremio, cuentas de
> poción. A diferencia de las props, que llegan del padre, el estado pertenece al propio
> componente; y cuando cambia, React **vuelve a renderizar** el componente para que la
> interfaz lo refleje.

Hazte una pregunta para distinguir el estado de todo lo demás: *¿este valor cambia
mientras el componente está en pantalla?*

| Dato | Tipo | Por qué |
| :--- | :--- | :--- |
| `username` pasado desde `App` | **prop** | Llega del padre; el hijo solo la muestra |
| Ruta del avatar `/avatar.png` | constante | Nunca cambia; basta con un string en el marcado |
| `hp` del jefe de la incursión del gremio | **estado** | Baja cada ronda mientras el componente está visible |
| Pociones en la alforja | **estado** | Sube y baja según bebe el jugador |

React le da a los componentes exactamente dos formas de recordar: **props** (heredadas
cuesta abajo desde [[07 - Rutas Comerciales]]) y **estado** (propio, privado, mutable solo
a través de su setter). Este capítulo trata del segundo.

---

## 02. Primer Latido

### Tu primer trozo de estado

`useState` es un **hook** — una función que React permite usar a los componentes normales.
Impórtalo, llámalo arriba de la componente y desempaqueta lo que devuelve:

```js
import React, { useState } from "react";

function TextMessage() {
  const [text, setText] = useState("¡Hola Mundo!");
  return (
    <div>
      <h1>Texto: {text}</h1>
    </div>
  );
}
```

Línea a línea:

- `import React, { useState } from "react";` — `useState` es un import **con nombre**, así
  que lleva llaves; `React` sigue siendo el import por defecto.
- `useState("¡Hola Mundo!")` — crea un estado cuyo **valor inicial** es la cadena
  `"¡Hola Mundo!"`.
- `const [text, setText] = useState(...)` — la **destructuración de array** desempaqueta la
  respuesta del hook en dos cosas: la variable de estado y su setter.
- `{text}` dentro del JSX imprime el valor actual en pantalla.

### Misión: Alforja de Pociones

Escribe un componente `PotionSatchel` cuyo estado empiece en `3` y renderice
`<h1>Pociones: {potions}</h1>`:

```js
const [potions, setPotions] = useState(3);
```

Renderízalo desde `App` (expórtalo con `export default`, como en
[[05 - Bloques de Construcción]]). Todavía nada cambia por su cuenta — has construido el
medidor, no el latido. El latido es el setter, en la siguiente sección.

---

## 03. Anatomía de un Latido

### Qué devuelve `useState`

> [!NOTE]
> **Información clave**
> `useState(valorInicial)` devuelve un **array de dos elementos**:
> `[variableDeEstado, setter]`. Por convención, el nombre del setter es `set` + el nombre
> del estado — `text` recibe `setText`, `potions` recibe `setPotions`. El valor inicial
> puede ser **de cualquier tipo de JavaScript**: cadena, número, booleano, array, objeto.

| Pieza | Convención de nombre | Rol |
| :--- | :--- | :--- |
| Variable de estado | el sustantivo: `text`, `potions`, `scores` | Guarda el valor actual; se lee en JSX |
| Setter | `set` + sustantivo: `setText`, `setPotions` | La **única** forma de cambiar el valor; provoca un re-render |

Tres reglas de la anatomía:

1. **Desempaqueta con `const`.** El par en sí nunca cambia —
   `const [text, setText] = ...`. Lo único que cambia es el *valor de dentro* de `text`.
2. **Llama al hook en el primer nivel** de la componente — nunca dentro de una condición
   ni de un bucle, o React pierde la cuenta de cuántos estados existen.
3. **Un nombre, una ranura.** ¿Quieres un segundo valor? Llama a `useState` otra vez:
   `const [hp, setHp] = useState(100);`.

---

## 04. La Regla de Oro

### Nunca toques el estado directamente

Aquí está la línea que separa una aplicación React de una rota:

```js
text = "¡Hasta la próxima!";                  // ❌ reasigna la variable — nada más
setText("¡Hasta la próxima! 👋");              // ✅ le dice a React que el valor cambió
```

> [!WARNING]
> **El error que todos cometen una vez — y la regla que nunca se rompe**
> **Nunca mutues ni reasignes el estado directamente; usa siempre el setter.** La
> asignación normal `text = "..."` se salta el motor de render de React: la variable en
> memoria cambia, la pantalla no, y te quedas mirando una **interfaz obsoleta**. Solo
> `setText(...)` notifica a React.

¿Por qué tanta ceremonia? React no tiene forma de saber que `text` cambió a menos que se lo
digas. El setter es la notificación:

- **Toda llamada al setter vuelve a renderizar la componente** — la función se ejecuta de
  nuevo con el nuevo valor, y el JSX se redibuja.
- Lo mismo vale para la mutación: `potions.push(...)` en un array o `text = text + "!"`
  no le avisarán a nadie. Construye el valor **nuevo** y entrégaselo al setter.

### Misión: Hasta la Próxima

Toma el componente `TextMessage` y añade un segundo estado, `sent`, que empiece en
`false`. Renderiza `{sent ? "Entregado ✅" : "Esperando…"}` junto al texto. Luego escribe
las dos líneas de `text = ...` y `setText(...)` de esta sección, guarda y mira cuál mueve
la pantalla. Una línea no hace nada; la otra repinta.

---

## 05. El Reloj en Marcha

### Actualizaciones asíncronas y con temporizadores

El estado es como los componentes sobreviven al **tiempo**. Un cronómetro es un solo
`useState`, un temporizador y un setter — la actualización ocurre de forma asíncrona, un
segundo entero después del último render:

```js
import React, { useState } from "react";

function Stopwatch() {
  const [seconds, setSeconds] = useState(0);

  function tick() {
    setTimeout(function () {
      setSeconds(seconds + 1);
    }, 1000);
  }

  return (
    <div>
      <h1>Segundos: {seconds}</h1>
      <button onClick={tick}>Iniciar</button>
    </div>
  );
}
```

Lee la secuencia:

1. Ocurre el render; `seconds` queda capturado dentro del cierre de `tick`.
2. `setTimeout` programa el callback **1000 ms después** — la componente ya siguió adelante.
3. El callback se ejecuta, llama a `setSeconds(seconds + 1)` y React vuelve a renderizar
   con `+1`.

Dos notas para el camino:

- `onClick={tick}` — handler pasado **sin** paréntesis — se cubre por completo en
  [[09 - El Mando]]; aquí es solo el detonador del temporizador.
- El valor `seconds + 1` se calculó a partir del valor **del momento del render**. Para
  una única actualización programada eso basta; para actualizaciones que se apilan, hace
  falta la fórmula de la siguiente sección.

> [!TIP]
> **Versión para game dev**
> Esto es un bucle de juego en miniatura: programa trabajo, deja pasar el tiempo, muta el
> estado, deja que el motor redibuje. Cambia `setTimeout` por `requestAnimationFrame` y
> tienes el contador de frames que ejecuta todo HUD.

---

## 06. La Fórmula del Rebobino

### Actualizaciones funcionales

Cuando el **nuevo estado se deriva del estado anterior**, entrégale al setter una función
en lugar de un valor. Esa función recibe el estado más reciente como argumento:

```js
const [volume, setVolume] = useState(50);

function raiseVolume() {
  setVolume((prevVolume) => Math.min(prevVolume + 5, 100));
}
```

Léelo: *pon el volumen en lo que fuera `prevVolume`, más cinco, tope cien.* La función de
flecha `(prevVolume) => ...` es la **forma de actualización funcional**:

| Forma | Qué recibe el setter | Úsala cuando |
| :--- | :--- | :--- |
| `setValue(5)` | un valor fijo | el nuevo estado no depende del anterior |
| `setValue((prev) => ...)` | una función del estado **más reciente** | el nuevo estado se deriva del anterior |

Por qué importa: entre el momento en que *programas* una actualización y el momento en
que React la *renderiza*, pueden haber llegado otras. La forma con valor sigue usando tu
instantánea vieja; la forma funcional siempre recibe el estado **más reciente** — y eso es
exactamente como evita los bugs de render asíncrono: ticks perdidos, contadores malos, un
cronómetro que se salta segundos.

### Misión: Botón de Silencio

Añade el espejo de `raiseVolume` — un `lowerVolume` que reste cinco y tenga cero como
suelo:

```js
setVolume((prevVolume) => Math.max(prevVolume - 5, 0));
```

Luego usa ambos en una sola componente con dos botones y comprueba que martillarlos en
cualquier orden siempre aterriza en un múltiplo de cinco entre 0 y 100. Ninguna instantánea
nunca quedó obsoleta — la fórmula leyó el estado más reciente cada vez.

---

## ⚡ XP Ganados: Ideas Clave

- 🧠 El **estado** son datos internos de un componente que se espera que cambien con el
  tiempo — poseídos por la componente, no heredados como props.
- 💉 `useState(valorInicial)` devuelve `[valor, setValor]`; el valor inicial puede ser
  **de cualquier tipo** de JavaScript.
- 🏷️ El setter se llama `set` + nombre del estado — `text` → `setText` — y **toda** llamada
  al setter vuelve a renderizar la componente.
- 🚫 **Nunca** reasignes ni mutues el estado directamente — `text = "..."` deja una
  interfaz obsoleta; solo `setText(...)` notifica a React.
- ⏱️ Los temporizadores actualizan el estado de forma asíncrona: programa, espera, set,
  repinta.
- 🔁 Cuando el nuevo estado se deriva del anterior, usa la forma funcional
  `setValor((prev) => ...)` para tener siempre el valor más reciente.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- ❤️ Medidores de vida, maná, XP y aguante que laten durante una pelea
- 🛒 Carritos de compra, contadores de me gusta y de vistas en cualquier página de producto
- ⏱️ Cronómetros, cuentas atrás, temporizadores de enfriamiento y relojes de partido
- 🔢 Indicadores de progreso: subidas, pasos de asistente, posición de la lista de reproducción
- 🎛️ Deslizadores y interruptores — volumen, brillo, ajustes que se mueven al arrastrar

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Construye `PotionSatchel` de la sección 02 con dos estados: `potions` (número) y
   `label` (cadena).
2. Toma la asignación directa `text = "..."` de la sección 04, ejecútala en una componente
   y describe en una sola frase por qué la pantalla no se movió.
3. Escribe un `MatchClock` que sume un segundo por tick con `setSeconds(seconds + 1)` y
   arráncalo desde un botón.
4. Escribe `raiseVolume` y `lowerVolume` para una `ManaBar` con tope 100 y suelo 0, ambos
   en la forma funcional.
5. **Pelea de jefe:** construye una **`ManaBar`** completa —
   `const [mana, setMana] = useState(50);` — con una acción `regen` (+10, tope 100), una
   acción `cast` (-25, suelo 0) y un porcentaje mostrado, con cada actualización escrita
   en la forma funcional para que martillear ambos botones nunca desincronice la barra.

---

## 🔗 Ver También

- [[00b - Chuleta de React]] — `useState`, el setter y las reglas de inmutabilidad en una página
- [[05 - Bloques de Construcción]] — capítulo anterior: los componentes que poseen el estado
- [[06 - El Árbol de Habilidades]] — capítulo anterior: dónde vive el estado en el árbol padre-hijo
- [[07 - Rutas Comerciales]] — capítulo anterior: las props, la otra mitad de la historia de datos de React
- [[09 - El Mando]] — siguiente capítulo: los eventos que cambian el estado
- [[11 - El Sistema de Reliquias]] — más adelante: `useEffect` y `useRef`, los hooks que manejan el tiempo

---
