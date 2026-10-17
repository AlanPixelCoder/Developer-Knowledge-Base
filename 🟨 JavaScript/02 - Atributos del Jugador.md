# 02. Atributos del Jugador

**Versión original en inglés:** [02 - Player Stats.md](02%20-%20Player%20Stats.md)

**Curso:** JavaScript
**Tema:** `let` y `const`, convenciones de nombres, tipos de datos, operadores aritméticos, exponentes y el proyecto Caída Mortal
**Tags:** `#javascript` `#variables` `#data-types` `#operators` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-06_--_10_%2B_Proyecto-7C5CFF?style=for-the-badge" alt="Lecciones 06 a 10 más proyecto">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Cada personaje de RPG es un montón de números esperando un nombre. Este capítulo enseña al
motor a **recordar** — nombres, puntos de vida, precios, banderas — con variables y tipos de
datos, y a **calcular** daño, propinas y gravedad con aritmética y exponentes. Al final
construirás una **calculadora de daño por caída** a partir de una fórmula física real. La
referencia de sintaxis está en [[00b - Chuleta de JavaScript]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Una variable es una caja con etiqueta en la memoria del motor; los cuatro tipos de datos
> (Number, String, Boolean, Undefined) es lo que se puede meter en la caja, y los operadores
> aritméticos es lo que se puede hacer con ello.

---

## 01. Ranuras de Guardado

### ¿Qué es una Variable?

Una **variable** es un contenedor que guarda un valor de datos para que el programa pueda
referenciarlo y manipularlo después. Cada variable tiene un **nombre** y contiene un
**valor**.

### `let` y `const`

JavaScript declara variables con dos palabras clave:

| Palabra clave | Úsala cuando | ¿Se puede reasignar? |
| :--- | :--- | :--- |
| `let` | Se espera que el valor **cambie** | Sí |
| `const` | El valor **permanece constante** en todo el programa | No — lanza un error |

```js
const playerName = "Ashwalker";
let hitPoints = 100;
```

- `playerName` es un `const`: el nombre de un personaje no cambia en medio de una partida.
- `hitPoints` es un `let`: todo el sentido de una variable de vida es que le den golpes.

La regla general: **empieza con `const`**, y degrada a `let` solo cuando sepas que el valor
debe cambiar. Un `const` que nunca se reasigna no puede reasignarse por accidente después.

### Asignación

El signo igual `=` es el **operador de asignación**: coloca un valor dentro de una variable.

```js
hitPoints = 85; // legal: hitPoints se declaró con let
```

Reasignar un `const` es un **TypeError** en tiempo de ejecución — el motor se niega:

```js
const maxLevel = 50;
maxLevel = 51; // TypeError: Assignment to constant variable
```

### Nombres: camelCase

Los nombres de variables de varias palabras se escriben en **camelCase**: la primera palabra
todo en minúsculas y la primera letra de cada palabra siguiente en mayúscula.

```js
let playerClass;      // ✅ camelCase
let criticalHitRate;  // ✅ camelCase
let Player_Class;     // ❌ no es camelCase
```

Los nombres deben decir qué *es* el valor. `let x = 42` compila; `let orbCount = 42` sobrevive
a una revisión de código.

### Misión: Lista de Personajes

Declara un `const` y un `let` para tu propio personaje — nombre, clase, nivel, vida — e
imprímelos con `console.log()` de [[01 - Inserta la Moneda]]:

```js
const heroName = "Ashwalker";
const heroClass = "Lantern Knight";
let heroLevel = 12;
let heroHP = 140;

console.log(heroName + " the " + heroClass + ", level " + heroLevel);
```

---

## 02. Qué Hay en la Caja

### Los cuatro tipos de datos principales

JavaScript es **dinámicamente tipado**: la palabra clave no declara un tipo — el *valor*
trae su propio tipo. Cuatro tipos principales cubren la mayoría de los programas iniciales:

### Number

Enteros y decimales — valores completos, fracciones, precios, daño, coordenadas:

```js
let patchVersion = 1.4;
let swordDamage = 27;
```

### String

Texto, entre comillas dobles `"..."` o simples `'...'`:

```js
let battleCry = "For the Ninth Floor!";
const guildName = "Ember Wardens";
```

Las cadenas se concatenan con `+` — notar los espacios, que no aparecen solos:

```js
console.log(battleCry + " " + guildName);
// For the Ninth Floor! Ember Wardens
```

### Boolean

Exactamente dos valores, siempre en minúscula: `true` o `false`. Los booleanos responden
las preguntas que el motor seguirá haciendo: ¿está vivo el jefe? ¿está cerrada la puerta?
¿está en línea el jugador?

```js
let hasKey = true;
let bossDefeated = false;
```

### Undefined

Una variable **declarada pero a la que nadie le dio un valor** contiene `undefined` — no
`null`, no cero, no una cadena vacía. `undefined` significa "nadie ha puesto nada en esta
caja todavía":

```js
let endDate;
console.log(endDate); // undefined
```

> [!WARNING]
> **`undefined` viaja.** Olvidar inicializar una variable es uno de los primeros errores más
> comunes: `let score; console.log(score + 10)` imprime `NaN` — Not a Number — porque el
> motor intentó sumar 10 a la nada. Inicializa tus variables.

---

## 03. La Fragua: Operadores Aritméticos

### El conjunto de operadores

JavaScript admite los operadores aritméticos estándar:

| Operador | Nombre | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| `+` | Suma | `10 + 5` | `15` |
| `-` | Resta | `10 - 5` | `5` |
| `*` | Multiplicación | `10 * 5` | `50` |
| `/` | División | `10 / 5` | `2` |
| `%` | Módulo (residuo) | `10 % 3` | `1` |
| `**` | Exponenciación | `2 ** 3` | `8` |

### El Módulo: el Operador de Paridad

`%` devuelve el **residuo** de una división — el operador más útil en la lógica de juego.
`x % 2` es `0` cuando x es par y `1` cuando es impar; ese solo test mueve la alternancia por
turnos, el apilado de objetos, los tableros y las tiradas de rareza de botín en todas partes.

```js
let turn = 5;
if (turn % 2 === 0) {
  console.log("Player's turn");
} else {
  console.log("Enemy's turn");
}
```

(El `if` se formaliza en [[03 - Tiradas de Botín]] — lo importante aquí es la comparación.)

### Orden de Operaciones

Se aplica la precedencia estándar; los **paréntesis `()` la anulan** y se evalúan primero.
Compara la cuenta de la taberna con y sin ellos:

```js
const stew = 2.99;
const ale = 0.99;
let tip = (stew + ale) * 0.2;   // 0.796 — propina sobre la comida

let wrongTip = stew + ale * 0.2; // 3.188 — propina solo sobre la sidra
```

Pon siempre paréntesis sobre lo que quieras decir. El motor sigue las reglas de precedencia;
tu lector no debería tener que adivinarlas.

### Exponentes

JavaScript escribe potencias con el doble asterisco `**` — no hay notación de superíndice
en el código:

```js
console.log(2 ** 3); // 8, es decir 2³
```

Los exponentes se enlazan más fuerte que la multiplicación y la división, y estas más fuerte
que la suma y la resta — la misma pirámide de la clase de matemáticas.

### Misión: Temperatura de la Fragua Helada

La fragua de Emberfall opera en Fahrenheit; el documento de diseño cita Celsius. Convierte
con la fórmula estándar e imprime ambos:

```js
const fahrenheit = 68;
const celsius = (fahrenheit - 32) / 1.8;
console.log(celsius); // 20
```

Los paréntesis importan: resta primero, luego divide. Quítalos y el motor divide 32 entre
1.8 antes de restar — una temperatura que ninguna fragua sobreviviría.

---

## 04. El Motor Físico

### Fórmulas con forma de BMI en los juegos

Muchas fórmulas de juego siguen la misma forma que el Índice de Masa Corporal — una cantidad
dividida por el **cuadrado** de otra:

$$bmi = \frac{mass}{height^2}$$

```js
const mass = 70;
const height = 1.75;
const bmi = mass / (height ** 2);
console.log(bmi); // 22.857...
```

Notar los paréntesis alrededor de `height ** 2`: sin ellos, el motor calcula
`mass / height ** 2` correctamente por precedencia, pero rodear la potencia hace legible la
intención — y protege la fórmula cuando luego la combines en una expresión mayor.

Los juegos reutilizan esta forma constantemente: la velocidad de movimiento escala con la
masa, el daño de área se desvanece con el cuadrado de la distancia, la mitigación de armadura
divide por valores de resistencia al cuadrado. Aprende a leer `a / (b ** 2)` como una unidad.

### Daño por Caída: El Proyecto

El asesino silencioso de toda saga de plataformas — el daño por caída — es aritmética. El
diseño clásico: el daño crece con el **cuadrado** de la distancia de caída, así que un
resbalón duele y un salto desde las murallas termina la partida.

```js
const safeDrop = 3;           // bloques — sin daño por debajo de esto
let fallDistance = 12;        // bloques
const fallDamage = (fallDistance - safeDrop) ** 2;

console.log("Fall distance: " + fallDistance + " blocks");
console.log("Fall damage: " + fallDamage + " HP");
```

Ajusta las dos perillas — `safeDrop` y el exponente — y habrás publicado una mecánica.

### Gravedad en todo el Sistema: Peso en Otro Planeta

En la campaña de carta estelar de Emberfall, el mismo personaje aterriza en mundos
distintos. El peso en otro planeta es el peso en Tierra multiplicado por el factor de gravedad
de ese planeta (Marte: `0.38`):

```js
const earthWeight = 210;
const marsWeight = earthWeight * 0.38;

console.log("Your weight on Earth is " + earthWeight + " pounds.");
console.log("Your weight on Mars is " + marsWeight + " pounds.");
```

Mismo personaje, mismo código, mundo distinto — una constante cambia toda la campaña.

---

## 💎 Bonus Loot: Tres Errores que Todo Depurador Encuentra

> [!NOTE]
> **De dónde viene "bug"**
> El 9 de septiembre de 1947, el equipo que operaba el Harvard Mark II — incluida la pionera
> **Grace Hopper** — encontró una polilla atrapada en un relé, la pegaron al cuaderno de
> registro y la etiquetaron como el "Primer caso real de bug encontrado". El sentido técnico
> de *bug* es incluso anterior, vuelve a Edison en 1878 — pero la polilla se llevó el crédito.

JavaScript informa los fallos en tres sabores que encontrarás en tu primera hora:

| Error | Cuándo | Disparador clásico |
| :--- | :--- | :--- |
| **SyntaxError** | El código en sí es inválido | Falta un `)`, `}` o comilla |
| **ReferenceError** | Se usa una variable que nunca se declaró | Un error de dedo en el nombre |
| **TypeError** | Se mal usa un tipo de dato | Reasignar un `const`, llamar `x()` cuando `x` no es función |

```js
// SyntaxError: falta la comilla de cierre
console.log("Emberfall");

// ReferenceError: lanternOil nunca se declaró
console.log(lanternOil);

// TypeError: no se puede reasignar una constante
const oilLevel = 10;
oilLevel = 0;
```

Lee el **nombre** del error primero, el mensaje después. SyntaxError significa arregla la
puntuación; ReferenceError significa busca la declaración; TypeError significa que el valor
no es lo que la operación necesita.

---

## ⚡ XP Ganados: Ideas Clave

- 📦 **`const` por defecto, `let` cuando debe cambiar.** Reasignar un `const` es un TypeError.
- 🐫 Nombres en **camelCase**: `criticalHitRate`, nunca `Critical_Hit_Rate`.
- 🧳 Cuatro tipos principales: **Number**, **String**, **Boolean**, **Undefined** — el valor trae el tipo.
- ➕ Operadores: `+ - * / % **` — el módulo halla residuos, `**` eleva a una potencia.
- 🧮 Los paréntesis anulan la precedencia; `(fahrenheit - 32) / 1.8` solo funciona con ellos.
- 🪂 El daño por caída, el BMI y la gravedad siguen la misma forma: **dividir o elevar al cuadrado** una segunda cantidad.
- 🐛 Tres nombres de error para triaje: **SyntaxError** (puntuación), **ReferenceError** (nombre no declarado), **TypeError** (tipo equivocado).

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 💰 Cálculo de precios e impuestos — los carritos de compra son aritmética
- ❤️ Vida, maná, estamina: cada stat es un `let`
- 🧪 Conversión de unidades: temperatura, moneda, métrico/imperial
- 🎲 Fórmulas de daño: base × modificador, caída al cuadrado, mitigación por porcentaje
- 🪐 Escalado entre niveles, zonas o planetas — cambia una constante y reequilibra el mundo

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Declara un `const` de precio de objeto y un `let` de cantidad; imprime el total de la línea.
2. Convierte 98.6°F a Celsius e imprime ambos valores en una sola frase.
3. Calcula `7 ** 3` y verifica el resultado con multiplicación repetida.
4. Escribe un `let` llamado `lanternOil` que empiece lleno y baje hasta `0` — tres asignaciones.
5. **Pelea de jefe:** construye una *calculadora de golpe crítico*: daño base, un modificador
   de fuerza y un escalado `** 2` por distancia — imprime una línea de combate completa para
   un golpe a 4 bloques.

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — tipos, operadores y declaraciones en una página
- [[01 - Inserta la Moneda]] — capítulo anterior: la consola y `console.log()`
- [[03 - Tiradas de Botín]] — siguiente capítulo: condicionales y toma de decisiones
- [[06 - Funciones de Habilidad]] — donde esas fórmulas se vuelven habilidades reutilizables

---
