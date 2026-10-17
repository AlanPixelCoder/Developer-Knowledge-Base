# 06. Funciones de Habilidad

**Versión original en inglés:** [06 - Skill Functions.md](06%20-%20Skill%20Functions.md)

**Curso:** JavaScript
**Tema:** Declaraciones de función, `return`, parámetros y argumentos, scope, funciones flecha y el proyecto Analizador de Registro de Combate
**Tags:** `#javascript` `#functions` `#scope` `#arrow-functions` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-E67E22?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-29_--_33_%2B_Proyecto-7C5CFF?style=for-the-badge" alt="Lecciones 29 a 33 más proyecto">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Una habilidad que solo puedes lanzar una vez es una cinemática. Una **función** es una
habilidad: escrita una vez, invocada por nombre, tantas veces como haga falta — con entradas
que cambian el resultado. Este capítulo enseña al motor a empaquetar lógica, alimentarla con
valores y devolver resultados. Al final construirás un **analizador de registro de combate**
que calcula la media y la mediana del daño de una pelea entera. Referencia:
[[00b - Chuleta de JavaScript]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Una función es un bloque reutilizable de código definido con `function`, llamado por nombre
> con paréntesis `()`, alimentado con **parámetros** (las entradas que espera) y que devuelve
> un valor con `return` — y el **scope** decide qué variables ve cada función.

---

## 01. Primer Hechizo

### ¿Qué es una Función?

Una **función** es un bloque reutilizable de código, escrito una vez y ejecutado múltiples
veces llamando a su nombre. Las funciones parten tareas complejas en piezas pequeñas y
manejables — y les dan nombres que puedes leer en voz alta.

```js
function helloWorld() {
  console.log("Hello, World!");
}

helloWorld();
```

Dos momentos, un nombre:

- **Declaración** — `function helloWorld() { ... }` escribe el hechizo en el grimorio.
  Nada se ejecuta todavía.
- **Llamada** — `helloWorld()` lo lanza. Los paréntesis `()` no son decoración opcional:
  toda función en JavaScript los necesita, en la definición **y** en cada llamada.

### Misión: Difusión

Imprime el anuncio del servidor tres veces — escribe el mensaje una sola vez:

```js
function announceRaid() {
  console.log("⚔️ Raid starts in 10 minutes!");
}

announceRaid();
announceRaid();
announceRaid();
```

Tres llamadas, tres impresiones, un cuerpo. Cambia el mensaje en un lugar y los tres cambian.

---

## 02. El Portal de Retorno

### La palabra clave `return`

Una función que solo imprime es un anuncio. Una función que **retorna** devuelve un valor
al llamador — donde puede guardarse, compararse o imprimirse:

```js
function countdown() {
  for (let i = 10; i >= 1; i--) {
    console.log(i);
  }
  return "Blast Off! 🚀";
}

console.log(countdown());
```

El bucle corre durante la llamada y luego el string `"Blast Off! 🚀"` viaja de vuelta al
sitio de la llamada, donde `console.log` lo recibe. Una llamada, dos efectos: las impresiones
adentro, el valor afuera.

### Nombres

Los nombres de función se escriben en **camelCase** y deben nombrar la acción:
`calculateDamage`, no `damage2`. Una función es un verbo — hace algo cuando la llamas.

---

## 03. Lanzar con Entradas

### Parámetros vs. Argumentos

Las funciones se vuelven habilidades al aceptar **entradas**:

| Término | Qué es | Ejemplo |
| :--- | :--- | :--- |
| **Parámetro** | La variable de marcador en la declaración | `function hit(damage)` |
| **Argumento** | El valor real pasado en la llamada | `hit(25)` |

### Misión: Golpe Cinético

La lección de física del motor, empaquetada como una habilidad. La energía es masa por el
cuadrado de la velocidad — la fórmula de [[02 - Atributos del Jugador]], ahora un hechizo
que acepta cualquier masa:

$$E = m \cdot v^2$$

```js
function kineticStrike(mass) {
  const speed = 3e8;              // 3 × 10⁸, la constante clásica
  const energy = mass * (speed ** 2);
  return energy;
}

console.log(kineticStrike(70));
```

El parámetro `mass` es una ranura; el argumento `70` es lo que la llena. Llama la función
con `1` y tienes un hechizo distinto — mismo cuerpo, nueva entrada. Esa es toda la economía
de las funciones: **paga una vez, lanza muchas**.

---

## 04. Lo que una Función Puede Ver

### Scope

El **scope** decide dónde se puede acceder a una variable. Dos reglas cubren la mayoría de
los programas:

- **Scope local:** una variable declarada **dentro** de una función vive solo dentro de esa
  función. Leerla desde fuera lanza un **ReferenceError**.
- **Scope global:** cualquier cosa **fuera** de las llaves de toda función es global — visible
  en todas partes, cambiada por cualquiera, la fuente clásica de los errores "¿quién mutó mi
  config?".

```js
const guildName = "Ember Wardens"; // global

function reportStatus() {
  let potions = 3;                 // local a reportStatus
  console.log(guildName + " has " + potions + " potions");
}

reportStatus();
// console.log(potions); // ReferenceError: potions is not defined
```

> [!TIP]
> Mantén por defecto el **local**. Una función que necesita un valor debe recibirlo como
> parámetro — para eso son las entradas del capítulo anterior. El estado global es un
> atajo que se compone; el estado local es un contrato que puedes leer desde la firma sola.

---

## 05. La Variante de Una Línea

### Funciones Flecha

Introducidas en **ES6 (2015)**, las **funciones flecha** son una sintaxis concisa para
funciones anónimas — ideales para trabajo corto de una sola expresión:

```js
// Función tradicional
function greet(name) {
  return "Hello, " + name + "!";
}

// Función flecha
const greetArrow = (name) => "Hello, " + name + "!";
```

La anatomía de una flecha:

```js
const add = (a, b) => {
  return a + b;
};
```

Cuando el cuerpo es una **sola expresión**, tanto las llaves como el `return` pueden
desaparecer — el valor se retorna **implícitamente**:

```js
const multiply = (a, b) => a * b;
```

### El Truco de Map

Las funciones flecha emparejan perfectamente con los métodos de arreglo. Elevar al cuadrado
un arreglo entero de stats en una línea:

```js
const numbers = [1, 2, 3, 4, 5];
const squaredNumbers = numbers.map((num) => num ** 2);
console.log(squaredNumbers); // [1, 4, 9, 16, 25]
```

Léela de derecha a izquierda: *para cada `num` en `numbers`, retorna `num ** 2`* — y `map`
recolecta los resultados en un arreglo nuevo. Diez líneas de bucle `for`, reemplazadas por
una línea de intención.

---

## 06. El Analizador de Registro de Combate

### Checkpoint: Resumen del capítulo

- Las funciones aíslan bloques **reutilizables**; `function` define, `()` llama.
- `return` entrega un valor de vuelta; sin él, la función retorna `undefined`.
- Los parámetros son marcadores; los argumentos son los valores rellenados en la llamada.
- Scope: los locales viven dentro de la función, los globales se filtran a todas partes — prefiere parámetros.
- Funciones flecha: `(params) => expression`, con retorno implícito en una línea.

### Proyecto: Analizador de Registro de Combate

La cápstone: tres registros de pelea — uno por build — y los números que un diseñador realmente
necesita. `mean` suma un arreglo y divide por `.length` (de [[05 - Inventario]]); `median`
ordena y toma el central. Ambas reciben el arreglo como **parámetro**:

```js
const slashDamage = [1932, 2300, 453, 5222, 6733, 7402, 8334];
const critDamage = [936, 2576, 453, 7013, 5489, 7402, 3921];
const spellDamage = [2300, 453, 5222, 989, 6733, 7402, 2789];

function mean(damageArray) {
  let totalDamage = 0;
  for (let i = 0; i < damageArray.length; i++) {
    totalDamage += damageArray[i];
  }
  return totalDamage / damageArray.length;
}

function median(damageArray) {
  let sortedStats = damageArray.sort(function (a, b) {
    return a - b;
  });
  let middleIndex = Math.floor(damageArray.length / 2);
  return sortedStats[middleIndex];
}

console.log("Slash build");
console.log("Mean:", mean(slashDamage));
console.log("Median:", median(slashDamage));
```

Un par de funciones, tres conjuntos de datos — cambia el argumento, conserva la lógica.
Eso es el capítulo entero en un programa.

### Palabras Rúnicas: el Detector de Palíndromos

Un último regalo del Deep Halls: una puerta encantada que solo se abre para palabras que
leen igual al revés. El detector pasa la entrada a minúsculas, la invierte con un bucle y
compara:

```js
function isPalindrome(word) {
  let lowerCaseWord = word.toLowerCase();
  let reversedWord = "";

  for (let i = lowerCaseWord.length - 1; i >= 0; i--) {
    reversedWord += lowerCaseWord[i];
  }

  return reversedWord === lowerCaseWord;
}

console.log(isPalindrome("racecar"));  // true
console.log(isPalindrome("moonlight")); // false
```

Notar `toLowerCase()`: la puerta no distingue mayúsculas, y la función recibe **una** sola
entrada — la palabra. Todo lo demás es maquinaria interna que el llamador nunca ve. El scope
funcionando como fue diseñado.

---

## ⚡ XP Ganados: Ideas Clave

- 🧩 Las funciones empaquetan lógica bajo un nombre; declara con `function`, lanza con `()`.
- ↩️ `return` envía un valor a casa; sin `return` regresa `undefined`.
- 🧮 Los parámetros son las ranuras; los argumentos las llenan — una llamada, muchas entradas.
- 🔒 Los locales son invisibles fuera; los globales visibles en todas partes — prefiere parámetros.
- ➡️ Funciones flecha: `(name) => expression`, retorno implícito en una línea.
- 🗺️ `.map((num) => num ** 2)` — el bucle que se lee como una regla.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- ⚔️ Habilidades y efectos de estado: una función, muchas fuentes y objetivos
- 📊 Motores de stats: media, mediana y percentiles sobre registros de combate o telemetría
- 🧪 Utilidades puras: convertidores, validadores, formateadores — el mejor amigo de la función
- 🎲 Tablas de botín y generadores empaquetados para reutilizar
- 🧹 Mantener limpio el espacio de nombres global — la verdadera razón del scope

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Escribe `function greetHero(name)` que retorne un saludo; imprime su resultado.
2. Convierte la fórmula de daño por caída de [[02 - Atributos del Jugador]] en una función de `fallDistance`.
3. Agrega un tercer parámetro a `kineticStrike` e imprime tres masas distintas.
4. Reescribe `multiply` de la sección de flechas como función tradicional, y luego de vuelta.
5. **Pelea de jefe:** una función `rarity(roll)` con `else if`, llamada cinco veces con cinco
   tiradas aleatorias — demuestra que la función es un hechizo y cinco lanzamientos.

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — sintaxis de función y flecha en una página
- [[05 - Inventario]] — capítulo anterior: los arreglos que estos analizadores consumen
- [[07 - Ficha de Personaje]] — siguiente capítulo: funciones promovidas a métodos de objeto
- [[08 - HUD Vivo]] — funciones conectadas a eventos reales de usuario

---
