# 04. El Farmeo

**Versión original en inglés:** [04 - The Farm.md](04%20-%20The%20Farm.md)

**Curso:** JavaScript
**Tema:** Introducción a bucles, `while`, `for`, iteradores, `break` y `continue`, bucles anidados y el proyecto Pase de Temporada
**Tags:** `#javascript` `#loops` `#while` `#for` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-E67E22?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-18_--_22_%2B_Proyecto-7C5CFF?style=for-the-badge" alt="Lecciones 18 a 22 más proyecto">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Cien llamadas idénticas a `console.log()` no son un programa — son un castigo. Los **bucles**
son la promesa del motor de repetir un bloque tantas veces como digas: cien turnos de farmeo,
mil tiradas de botín, un calendario entero de eventos. Al final construirás un **rastreador de
pase de temporada** que recorre un año completo del juego y marca cada día de XP doble.
Referencia: [[00b - Chuleta de JavaScript]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Un bucle ejecuta un bloque de código repetidamente mientras se sostenga una condición: los
> `while` corren mientras la condición sea `true`, los `for` corren un número contado de veces
> — y `break` y `continue` son las salidas de emergencia.

---

## 01. Pato, Pato, Ganso

### ¿Qué es un Bucle?

En programación, los **bucles** repiten un bloque de código basándose en una condición. En
vez de escribir la misma línea cincuenta veces, la escribes una vez y le dices al motor que
la ejecute cincuenta veces.

### Un primer `while`

El clásico juego del recreo, simulado: el motor sigue lanzando "Pato" hasta que la tirada
sale "Ganso":

```js
let randomNumber = Math.floor(Math.random() * 10);

while (randomNumber !== 7) {
  console.log("Duck 🦆");
  randomNumber = Math.floor(Math.random() * 10);
}

console.log("Goose! 🦢");
```

Síguelo: lanza una vez, luego comprueba. Mientras la tirada no sea `7`, imprime un pato y
lanza otra vez. En el momento en que aparece un `7`, la condición falla y el bucle cae
hasta el ganso.

> [!WARNING]
> **El bucle infinito.** Si nada dentro del bucle cambia jamás la condición probada, el
> motor repite el bloque para siempre — pestaña congelada, ventilador a tope. Todo `while`
> necesita un camino hacia `false`: en el juego de arriba, la nueva tirada dentro del bloque
> es ese camino. Comprueba que el camino exista **antes** de ejecutar el código.

---

## 02. El Número de la Suerte

### Sintaxis de `while`

```js
while (condition) {
  // Code here
}
```

La condición se prueba **antes de cada iteración**. Mientras sea `true`, el bloque corre; la
primera vez que devuelve `false`, el bucle termina. No se requiere nada más — ni contador,
ni estructura. Solo una condición y la promesa de romperla alguna vez.

### Misión: Cracking la Cofre

El taladro de un cerrajero: sigue adivinando hasta que la combinación abra. El número de la
suerte vive en un `const`; las conjeturas se lanzan frescas en cada pasada:

```js
const luckyNumber = 7;
let guess = Math.floor(Math.random() * 10) + 1;

while (guess !== luckyNumber) {
  console.log("Nope, it isn't " + guess);
  guess = Math.floor(Math.random() * 10) + 1;
}

console.log("My lucky number is " + luckyNumber + "!");
```

Dos lanzamientos de `guess` — uno antes del bucle para alimentar la primera prueba, y otro
dentro para avanzar hacia la salida. Ese baile es toda la forma del `while`.

---

## 03. La Cinta de XP

### Iteradores

Una variable actualizada dentro de un bucle para controlar la ejecución es un **iterador** —
por convención, se llama `i`. **Iterar** es ejecutar el cuerpo del bucle una vez; cuando el
iterador lleva la condición a `false`, el bucle sale limpiamente.

### El bucle `for`

`for` empaqueta el bucle entero en una línea: inicialización, condición y actualización —
tres cláusulas separadas por punto y coma:

```js
for (let i = initialValue; condition; updateIterator) {
  // Code here
}
```

| Cláusula | Ejemplo | Rol |
| :--- | :--- | :--- |
| Inicializar | `let i = 1` | Crea el iterador, una vez |
| Condición | `i <= 10` | Se prueba antes de cada iteración |
| Actualizar | `i++` | Se ejecuta tras cada iteración (`i++` = `i = i + 1`) |

### El Mensaje del Farmeo

El hechizo de detención, reescrito como rutina de entrenamiento: cien repeticiones, contadas
por el bucle:

```js
for (let i = 1; i <= 100; i++) {
  console.log("Rep " + i + ": I must not tell lies.");
}
```

Las tres cláusulas se sientan en una línea y el cuerpo queda limpio. Compara la versión con
`while`: escribirías a mano la inicialización, la prueba y el incremento en tres lugares
distintos. `for` los mantiene juntos porque siempre viajan juntos.

> [!TIP]
> Los límites del bucle son donde viven los errores de más uno. `i <= 10` corre diez veces
> (`1` a `10`); `i < 10` corre nueve. Decide si tu conteo es inclusivo y escribe el operador
> en consecuencia — luego comprueba la salida impresa, no el código.

---

## 04. Salidas de Emergencia

### `continue`

Cuando una condición se dispara, `continue` **termina la iteración actual de inmediato** y
salta a la siguiente — el resto de esa pasada se omite:

```js
for (let i = 0; i < 5; i++) {
  if (i === 1) {
    continue;
  }
  console.log(i);
}
// Output: 0, 2, 3, 4
```

### `break`

`break` **termina el bucle por completo**, reanudando el programa justo después de la llave
de cierre — sin más iteraciones, importe lo que importe la condición:

```js
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}
// Output: 0, 1, 2
```

Uno se salta un turno; el otro voltea la mesa. En la lógica de juego: `continue` se salta los
mobs de relleno de una oleada; `break` detiene la oleada en cuanto muere el jefe.

---

## 05. La Rejilla de Daño

### Bucles Anidados

Un **bucle anidado** es un bucle dentro de otro — la luna orbitando la Tierra mientras la
Tierra orbita el sol. El bucle interior completa su **ciclo entero** en cada iteración única
del bucle exterior.

### Misión: Matriz de Daño

La hoja de balanceo que guarda todo juego de táctica — una tabla de multiplicar de
multiplicadores de ataque, filas por columnas:

```js
for (let i = 1; i <= 3; i++) {
  for (let j = 1; j <= 3; j++) {
    console.log(`${i} * ${j} = ${i * j}`);
  }
}
```

- El bucle **exterior** (`i`) recorre las filas.
- El bucle **interior** (`j`) recorre las columnas de cada fila — por completo, antes de que `i` avance.

Nueve líneas desde dos líneas de código. El coste: las iteraciones se multiplican — una
rejilla de 10×10 dentro de un bucle de 100 fotogramas son 10,000 pasadas internas por
fotograma. Anida con intención.

> [!NOTE]
> La sintaxis `` `${i} * ${j}` `` es un **literal de plantilla**: comillas invertidas alrededor
> de la cadena y `${expression}` para insertar un valor. Se lee mejor que la concatenación con
> `+` cuando las cadenas se alargan — se usa en el resto de esta vault.

---

## 06. El Pase de Temporada

### Checkpoint: Resumen del capítulo

- Los **bucles** ejecutan un bloque repetidamente.
- Los `while` corren mientras una condición sea `true` — y necesitan un camino hacia `false`.
- Los `for` corren un número contado de veces vía un iterador: inicio, condición, actualización.
- `continue` salta una iteración; `break` termina el bucle para siempre.
- Los bucles anidados multiplican — ciclos interiores completos, por cada paso exterior.

### Proyecto: Rastreador de Pase de Temporada

La cápstone del capítulo recorre el calendario completo de un año live-service e imprime
cada día de XP doble. Una comprobación de año bisiesto decide la duración del calendario —
mantén la regla exactamente como la escribieron los diseñadores:

$$leap = (year \% 4 = 0 \land year \% 100 \neq 0) \lor year \% 400 = 0$$

```js
let eventCount = 0;

for (let year = 2000; year <= 3000; year++) {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log(`✨ [Year ${year}] -> Leap Year Unlocked! (+1 Extra Day Buff)`);
    eventCount++;
  }
}

console.log(`🏆 SEASON COMPLETE: ${eventCount} bonus days in the archives!`);
```

Cada pieza de los últimos tres capítulos está en este programa: un contador `let` de
[[02 - Atributos del Jugador]], la cadena `&&`/`||` de [[03 - Tiradas de Botín]], aritmética
de módulo y un bucle `for` que corre **1,001 veces** para comprobarlas todas. Esa es la
forma del código real — nada nuevo, solo combinado.

---

## ⚡ XP Ganados: Ideas Clave

- 🔁 Los **bucles** reemplazan la repetición con una condición.
- ⚠️ Un `while` cuya condición nunca cambia es un **bucle infinito** — traza siempre un camino hacia `false`.
- 🎲 `while (guess !== luckyNumber)` — prueba primero, lanza otra vez dentro del bloque.
- 🔢 `for (let i = 1; i <= 100; i++)` — inicializa, prueba, actualiza, en una línea.
- 🚪 `continue` salta la iteración actual; `break` termina el bucle para siempre.
- 🪆 Bucles anidados: el interior corre **completo**, una vez por iteración exterior — los costes se multiplican.
- 📅 El rastreador de pase de temporada: 1,001 iteraciones, una regla de año bisiesto, cero código repetido.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🔄 Bucles de juego: update, tick de física, render — cada fotograma
- 🎰 Tiradas por lotes: tablas de botín, ruletas gacha, semillas de generación procedural
- 📊 Iterar stats: daño total de una pelea, media de una lista de puntuaciones
- 🗓️ Calendarios, pases de temporada, rachas de inicio de sesión diario
- 🧱 Rejillas: inventarios, mapas, matrices de crafteo — bucles anidados hasta el fondo

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Imprime "Level up!" diez veces con un bucle `for` y un contador visible.
2. Reescribe el Pato-Ganso del `while` para que pare en un `5` en vez de un `7`.
3. Itera de `0` a `10`, pero salta con `continue` cada número impar — imprime solo pares.
4. Imprime una rejilla de 5×5 de caracteres `*` con bucles anidados.
5. **Pelea de jefe:** un *contador de piedad* — itera hasta 90 tiradas, haz `break` en cuanto
   salga un Legendary e imprime cuántas tiradas hizo falta.

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — sintaxis de bucles y salidas en una página
- [[03 - Tiradas de Botín]] — capítulo anterior: los condicionales que los bucles arrastran
- [[05 - Inventario]] — siguiente capítulo: arreglos, los datos sobre los que suelen girar los bucles
- [[06 - Funciones de Habilidad]] — bucles envueltos en funciones reutilizables

---
