# 03. Tiradas de Botín

**Versión original en inglés:** [03 - Loot Rolls.md](03%20-%20Loot%20Rolls.md)

**Curso:** JavaScript
**Tema:** Control de flujo, `if` / `else` / `else if`, operadores de comparación y lógicos, `Math.random()`, condicionales anidados y el proyecto Tirada de Rareza
**Tags:** `#javascript` `#control-flow` `#conditionals` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Lecciones-11_--_17_%2B_Proyecto-7C5CFF?style=for-the-badge" alt="Lecciones 11 a 17 más proyecto">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Hasta ahora el motor lo ejecuta todo, en orden, siempre. Este capítulo le entrega una
decisión. Los **condicionales** permiten que un programa bifurque el camino: golpe crítico
o normal, botín raro o común, la puerta se abre o se queda cerrada — y `Math.random()` aporta
los dados. Al final construirás un **dado de mazmorra** que lanza un veredicto aleatorio sobre
tu pregunta. Referencia: [[00b - Chuleta de JavaScript]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Una sentencia `if` prueba una condición y ejecuta su bloque **solo** cuando la prueba
> devuelve `true`; todo lo demás del capítulo — `else`, `else if`, comparaciones, operadores
> lógicos, anidamiento — es una variación de esa misma bifurcación.

---

## 01. La Moneda al Aire

### Control de Flujo

Por defecto, los programas corren línea por línea, de arriba abajo — sin sorpresas. Las
sentencias de **control de flujo** rompen esa cinta transportadora: permiten que el motor
evalúe una condición y ejecute un bloque de código en vez de otro.

### `Math.random()`

El ingrediente que necesita toda tabla de botín: `Math.random()` genera un decimal desde `0`
(inclusive) hasta `1` (exclusive) — `0.0`, nunca quite `1.0`.

Para obtener un **entero aleatorio** en un rango, multiplica por el tamaño del rango y
redondea hacia abajo con `Math.floor()`:

```js
Math.floor(Math.random() * 10);   // un número entero de 0 a 9
Math.floor(Math.random() * 6) + 1; // tirada de dado: 1 a 6
```

### Misión: Iniciativa

La primera moneda al aire. El motor lanza un número por encima o por debajo de `0.5` y elige
bando:

```js
let num = Math.random();

if (num > 0.5) {
  console.log("Heads");
} else {
  console.log("Tails");
}
```

Ejecútala unas veces. La mitad imprime `Heads`, la mitad `Tails` — una moneda que funciona,
a diez líneas del curso.

---

## 02. La Puerta

### La sentencia `if`

`if` prueba una condición en busca de verdad y ejecuta el código dentro de sus llaves `{}`
**solo si** la condición evalúa a `true`. Si es `false`, el bloque se omite por completo:

```js
if (condition) {
  // Do something
}
```

Un ejemplo en vivo — el guardián del Deep Halls revisa tu nivel antes de dejarte entrar:

```js
let level = 14;

if (level >= 15) {
  console.log("Access granted: Deep Halls");
}
```

La condición vive entre paréntesis `()`. El valor probado es una **expresión booleana**:
algo que devuelve `true` o `false` — y ahí entran los operadores de comparación.

### Operadores de Comparación

Se usan para comparar dos valores dentro de una condición:

| Operador | Significado | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| `===` | Igualdad estricta | `5 === 5` | `true` |
| `!==` | Desigualdad estricta | `5 !== 3` | `true` |
| `>` | Mayor que | `5 > 3` | `true` |
| `>=` | Mayor o igual que | `5 >= 5` | `true` |
| `<` | Menor que | `5 < 3` | `false` |
| `<=` | Menor o igual que | `3 <= 5` | `true` |

> [!WARNING]
> **Tres iguales, siempre.** `=` asigna; `===` compara. Escribir `if (level = 15)` asigna 15
> a `level` y la condición sale verdad por accidente — el error clásico que parece lógica pero
> es un ty po. En los condicionales, usa `===` y `!==` cada vez.

---

## 03. Las Dos Puertas

### La cláusula `else`

`else` es una cláusula opcional al final de un `if` que maneja el caso en que la condición
resultó `false`:

```js
if (condition) {
  // Do something
} else {
  // Do something else
}
```

Todo camino se bifurca en ambos sentidos. El guardia del puesto te deja pasar o te da la
vuelta:

```js
let torchLit = true;

if (torchLit) {
  console.log("The corridor lights up ahead.");
} else {
  console.log("You bump into the wall in the dark.");
}
```

Exactamente una rama se ejecuta — nunca ambas, nunca ninguna. Ese es todo el contrato.

---

## 04. La Tabla de Botín

### La cadena `else if`

`else if` evalúa varias condiciones en secuencia, entre el `if` inicial y el `else` final:

```js
if (conditionA) {
  // Do this
} else if (conditionB) {
  // Do this, instead
} else {
  // Do this if none of the above are true
}
```

Las condiciones se prueban **de arriba abajo** y gana la primera `true` — el resto de la
cadena nunca se examina. Ese orden no es decoración: es la lógica.

### Misión: Tirada de Rareza

Una tabla de rareza de botín es una cadena `else if` con los umbrales ordenados con cuidado.
Léela desde arriba; un `96` cae en la primera rama que lo reclama:

```js
let roll = 96;

if (roll >= 95) {
  console.log("Legendary drop!");
} else if (roll >= 80) {
  console.log("Epic drop.");
} else if (roll >= 50) {
  console.log("Rare drop.");
} else {
  console.log("Common drop. Better luck next run.");
}
```

> [!NOTE]
> Invierte el orden — prueba `roll >= 50` primero — y un `96` imprime "Rare". La cadena se
> detiene en la primera `true`, así que **ordena de más restrictivo a menos**. La misma trampa
> custodia cada tabla de daño, cada carta de afinidad y cada clima que escribas jamás.

### Afinidad al Estilo pH

Los rangos funcionan igual. Una comprobación de resistencia elemental es el patrón de la
escala pH con palabras de juego — prueba el tramo en que cae el valor:

```js
let fireResist = 65;

if (fireResist >= 0 && fireResist <= 50) {
  console.log("Vulnerable");
} else if (fireResist >= 51 && fireResist <= 100) {
  console.log("Resistant");
} else {
  console.log("Immune");
}
```

El `&&` de esos rangos es un operador lógico — la siguiente sección.

---

## 05. Combinando Condiciones

### Operadores Lógicos

Los operadores lógicos (booleanos) combinan y evalúan varias condiciones a la vez:

| Operador | Nombre | Devuelve `true` cuando |
| :--- | :--- | :--- |
| `&&` | AND | **Ambas** condiciones son verdaderas |
| `\|\|` | OR | **Al menos una** condición es verdadera |
| `!` | NOT | La condición es **falsa** — la invierte |

```js
let hasTicket = true;
let isVip = false;

console.log(hasTicket && isVip);  // false — ambas deben ser verdaderas
console.log(hasTicket || isVip);  // true  — una basta
console.log(!isVip);             // true  — invierte false a true
```

El rango de afinidad de la sección anterior es un `&&` en su hábitat natural:

```js
let aqi = 65;

if (aqi >= 0 && aqi <= 50) {
  console.log("Good");
} else if (aqi >= 51 && aqi <= 100) {
  console.log("Moderate");
} else {
  console.log("Hazardous");
}
```

### Misión: El Dado de Mazmorra — Proyecto

La cápstone del capítulo lanza un veredicto aleatorio sobre cualquier pregunta, una cadena
`else if` alimentada por `Math.random()`:

```js
const question = "Will the Ember Key drop this run?";
const randomNumber = Math.floor(Math.random() * 9) + 1;
let answer = "";

if (randomNumber === 1) {
  answer = "Yes — definitely.";
} else if (randomNumber === 2) {
  answer = "It is decidedly so.";
} else if (randomNumber === 3) {
  answer = "Reply hazy, try again.";
} else {
  answer = "Very doubtful.";
}

console.log("Question: " + question);
console.log("Oracle: " + answer);
```

Ejecútalo cinco veces; la respuesta cambia en cada una porque la tirada ocurre **antes** de
la cadena. Aleatoriedad adentro, bifurcación afuera — eso es una tabla de botín en miniatura.

---

## 💎 Bonus Loot: Ifs Anidados

Un **if anidado** es un `if` dentro de otro `if`. La condición interior solo se examina
cuando la **exterior** es `true` — puertas frente a puertas. El clima de Emberfall funciona
exactamente así: primero decide si el evento celeste es soleado, y luego qué significa eso
para la temperatura:

```js
let weather = "Sunny";
let temperature = 85;

if (weather === "Sunny") {
  if (temperature > 80) {
    console.log("Desert zone is open. Pack water.");
  } else {
    console.log("Mild day — good climbing weather.");
  }
} else {
  console.log("Indoor dungeon day. Raid the Deep Halls instead.");
}
```

Tres resultados, dos pruebas, un árbol legible. Anida solo tan profundo como la decisión lo
sea de verdad — tres niveles de anidamiento suelen ser una señal de que las condiciones
merecen nombres.

---

## ⚡ XP Ganados: Ideas Clave

- 🔀 El **control de flujo** permite al motor elegir caminos en vez de ejecutar cada línea.
- 🎲 `Math.random()` devuelve 0–1; `Math.floor(Math.random() * n)` devuelve 0 a n−1.
- 🚪 `if (condition)` ejecuta su bloque solo cuando la condición es `true`.
- 🚪 La cláusula `else` captura todo lo que el `if` rechazó.
- 🧮 Las cadenas `else if` prueban de arriba abajo; **gana la primera `true`** — ordena los umbrales de más restrictivo a menos.
- ⚖️ Comparaciones: `===`, `!==`, `>`, `>=`, `<`, `<=` — tres iguales, siempre.
- 🔗 Lógica: `&&` (ambas), `||` (cualquiera), `!` (no) — combina pruebas en rangos y puertas.
- 🪆 Los `if` anidados evalúan la compuerta interior solo cuando la exterior se abre.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🎰 Tablas de botín, ruletas gacha y probabilidades de crítico
- 🚦 Comprobaciones de acceso: requisitos de nivel, feature flags, permisos
- 🌦️ Sistemas de clima, afinidad y efectos de estado
- 🎯 Validación de entrada: "solo aceptar un número entre 1 y 99"
- 🔐 Lógica de desbloqueo: llave + puerta + jefe derrotado, combinados con `&&`

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Lanza `Math.floor(Math.random() * 20) + 1` — un d20 — e imprime el número.
2. Escribe un `if`/`else` que imprima "Level too low" o "Welcome" según una variable de nivel.
3. Construye una tabla de botín de tres niveles: Common, Rare, Legendary.
4. Combina dos booleanos con `&&`, `||` y `!` e imprime los seis resultados.
5. **Pelea de jefe:** una comprobación de montura con condicional anidado — si el jugador tiene
   la montura **y** la criatura está domesticada, imprime "Mount ready"; si solo uno es cierto,
   imprime cuál pieza falta; si ninguno, imprime "What creature?".

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — operadores y sintaxis condicional en una página
- [[02 - Atributos del Jugador]] — capítulo anterior: los valores que estas condiciones prueban
- [[04 - El Farmeo]] — siguiente capítulo: bucles, cuando una decisión no basta
- [[07 - Ficha de Personaje]] — condicionales viviendo dentro de métodos de objeto

---
