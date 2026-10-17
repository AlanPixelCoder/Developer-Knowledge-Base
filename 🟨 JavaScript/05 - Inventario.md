# 05. Inventario

**Versión original en inglés:** [05 - Inventory.md](05%20-%20Inventory.md)

**Curso:** JavaScript
**Tema:** Arreglos, índice y notación con corchetes, `.length`, iteración, `push` / `pop` / `shift` / `unshift`, `.indexOf()` / `.includes()` y el proyecto Semilla de Mazmorra
**Tags:** `#javascript` `#arrays` `#data-structures` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-E67E22?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-23_--_28_%2B_Proyecto-7C5CFF?style=for-the-badge" alt="Lecciones 23 a 28 más proyecto">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Un personaje con veinte pociones necesita veinte variables — y una pesadilla para gestionar.
Los **arreglos** son el contenedor del motor para muchos valores: la barra rápida, la lista
del pelotón, la cadena semilla de una mazmorra entera. Al final generarás una **planta de
mazmorra procedural** con cuatro tipos de tesela, todos metidos en un solo arreglo. Referencia:
[[00b - Chuleta de JavaScript]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Un arreglo es una sola variable que contiene una lista ordenada entre corchetes `[]`; los
> elementos se direccionan por un **índice basado en cero**, se cuentan con `.length` y se
> remodelan con los métodos incorporados `push`, `pop`, `shift` y `unshift`.

---

## 01. La Bolsa

### ¿Qué es un Arreglo?

Un **arreglo** es una sola variable usada para guardar múltiples valores agrupados. Se crea
con corchetes `[]`, con los elementos separados por comas. Un arreglo puede mezclar tipos o
contener un solo tipo uniforme — al motor no le importa:

```js
let lotteryNumbers = [13, 36, 45, 57, 67, 14];
const lettersAndNumbers = ["a", "b", "c", 1, 2, 3];
```

### Misión: Lista de Zonas

El diario de viaje de la campaña — cinco destinos, una variable:

```js
let myDestinations = [
  "Manhattan - Washington Square Park",
  "The Bronx - Yankee Stadium",
  "Brooklyn - Coney Island",
  "Queens - Flushing",
  "Staten Island - Historic Richmond Town"
];

console.log(myDestinations);
```

Imprimir la variable imprime la lista entera de una vez — corchetes, comillas y todo.
Compara con cinco `console.log()` separados: misma información, un solo nombre.

---

## 02. Direcciones

### Índice y Notación con Corchetes

El **índice** de un elemento es su posición numérica dentro del arreglo — y JavaScript
cuenta desde **cero**. El primer elemento es `[0]`, no `[1]`:

```js
let fruits = ["strawberries 🍓", "blueberries 🫐", "bananas 🍌"];
console.log(fruits[0]); // strawberries 🍓
```

### Modificar Elementos

La notación con corchete al lado izquierdo del `=` escribe:

```js
let pokemon = ["Bulbasaur", "Charmander", "Squirtle"];
pokemon[2] = "Pikachu"; // reemplaza a "Squirtle"
```

### Hacer Crecer el Arreglo

Asignar a un índice **más allá del final** agrega, rellenando cualquier hueco con
`undefined` — legal, pero el agujero es un error esperando a que lo encuentren:

```js
let groceryList = ["🥛 Milk", "🥑 Avocado", "🥚 Eggs", "🍞 Bread"];

groceryList[2] = "🧈 Butter";       // reemplaza a Eggs
groceryList[4] = "🧼 Soap";         // agrega al final

console.log(groceryList);
// ["🥛 Milk", "🥑 Avocado", "🧈 Butter", "🍞 Bread", "🧼 Soap"]
```

> [!WARNING]
> **El eterno error de más uno.** El último índice de un arreglo es `length - 1`. Pedir
> `[length]` devuelve `undefined` — no un error, solo silencio. Cuando una búsqueda en un
> arreglo imprime algo que no esperabas, cuenta desde **cero** y resta uno.

---

## 03. Contando Espacios

### La propiedad `.length`

Todo arreglo lleva una propiedad incorporada `.length`: un entero con el número de elementos
que contiene actualmente:

```js
const testScores = [78, 96, 100, 88, 85, 81, 79];
const numberOfScores = testScores.length;
console.log(numberOfScores); // 7
```

### Bucles sobre Arreglos

`.length` combina naturalmente con los bucles de [[04 - El Farmeo]] — recorre cada elemento
dinámicamente, sin conocer el conteo por adelantado:

```js
const musicNotes = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"];

for (let i = 0; i < musicNotes.length; i++) {
  console.log(musicNotes[i]);
}
```

La condición del bucle usa `.length` directamente, así que agregar una nota mañana no
requiere ningún otro edit. Escribir a mano `i < 7` la saltaría en silencio.

---

## 04. Gestión de la Barra Rápida

### Los cuatro Cardinales

JavaScript trae métodos incorporados que modifican arreglos en el sitio. Cuatro cubren la
mayoría de los programas iniciales:

| Método | Efecto | Devuelve |
| :--- | :--- | :--- |
| `push(item)` | Agrega al **final** | Nueva longitud |
| `pop()` | Elimina el **último** elemento | El elemento eliminado |
| `unshift(item)` | Agrega al **principio** | Nueva longitud |
| `shift()` | Elimina el **primer** elemento | El elemento eliminado |

### Misión: Reordenar la Lista

Una reorganización de la barra de carga — quita de un extremo, agrega al otro:

```js
const musicPlaylist = ["Tom Sawyer", "Sabotage", "Thriller"];

musicPlaylist.shift(); // elimina "Tom Sawyer"
musicPlaylist.pop();   // elimina "Thriller"
musicPlaylist.push("Scary Monsters and Nice Sprites"); // agrega al final
musicPlaylist.unshift("Fractals", "Bangarang");        // agrega al frente

console.log(musicPlaylist);
// ["Fractals", "Bangarang", "Sabotage", "Scary Monsters and Nice Sprites"]
```

`shift` y `unshift` reindexan cada elemento que se mueve — bien para una lista de reproducción,
costoso dentro de un bucle por fotograma. Apégate a `push` y `pop` cuando puedas: tocan solo
un extremo.

---

## 05. Encuentra al Espía

### `.indexOf(value)`

Devuelve el índice numérico de la **primera** aparición de un valor — o `-1` si el valor no
está en el arreglo en absoluto:

```js
const characters = ["The Wally Watchers", "Wilma", "Waldo", "Woof"];
console.log(characters.indexOf("Waldo")); // 2
console.log(characters.indexOf("Wanda")); // -1
```

### `.includes(value)`

Comprueba la pertenencia y responde con un booleano — sin aritmética de índices, sin centinela
`-1`:

```js
if (characters.includes("Waldo")) {
  let waldoIndex = characters.indexOf("Waldo");
  console.log(`Found Waldo at index ${waldoIndex}!`);
} else {
  console.log("Not found");
}
```

El par se lee como una frase: *si el elenco incluye a Waldo, encuentra dónde.*
`.includes()` llegó con ES2016 — es la herramienta correcta para la pregunta "¿está ahí?";
`.indexOf()` es la herramienta para "¿dónde está?".

---

## 06. La Semilla de Mazmorra

### Checkpoint: Resumen del capítulo

- Un arreglo es **una sola variable**, muchos valores ordenados, en `[...]`.
- Los índices empiezan en **cero**; el último es `length - 1`.
- `.length` cuenta elementos; combínalo con un `for` para visitarlos todos.
- `push`/`pop` trabajan un extremo, `shift`/`unshift` el otro.
- `.indexOf()` devuelve una posición o `-1`; `.includes()` devuelve `true` o `false`.

### Proyecto: Planta de Mazmorra Procedural

La cápstone del capítulo genera una mazmorra a partir de teselas — las mismas cuatro letras
de una secuencia genética, el mismo truco de cuatro formas de cualquier generador procedural.
Veinticuatro habitaciones, tres teselas por habitación, lanzadas desde un solo arreglo:

```js
const dungeonTiles = ["#", ".", "^", "C"]; // muro, suelo, trampa, cofre
let myDungeon = [];

for (let i = 0; i < 24; i++) {
  let piece1 = Math.floor(Math.random() * dungeonTiles.length);
  let piece2 = Math.floor(Math.random() * dungeonTiles.length);
  let piece3 = Math.floor(Math.random() * dungeonTiles.length);

  myDungeon.push(
    dungeonTiles[piece1] + dungeonTiles[piece2] + dungeonTiles[piece3]
  );
}

console.log(myDungeon);
```

Cada pieza de este capítulo está en la mesa: el arreglo semilla, `.length` alimentando
`Math.random()` de [[03 - Tiradas de Botín]], un bucle `for` de [[04 - El Farmeo]] y `push`
para hacer crecer el resultado. Veinticuatro habitaciones desde diez líneas — el arreglo
hizo el almacenamiento, el bucle hizo el trabajo, y los métodos mantuvieron la bolsa ordenada.

> [!TIP]
> **Versión para game dev**
> Esta es la generación procedural en su infancia. Cambia las cuatro teselas por ids de
> bioma, agrega un segundo bucle para las filas, y tienes un mapa. La técnica completa —
> habitaciones, pasillos, semillas — es el mismo problema de arreglo-de-valores con mejores
> palabras.

---

## ⚡ XP Ganados: Ideas Clave

- 🎒 Un arreglo = una variable = muchos valores ordenados: `[13, 36, 45]`.
- 0️⃣ Los índices empiezan en **cero**; el último es `.length - 1`; leer fuera de rango devuelve `undefined`.
- ✍️ `arr[2] = x` escribe; asignar más allá del final agrega.
- 📏 `.length` cuenta — insértalo en un bucle `for` para visitar cada elemento.
- 🃏 `push`/`pop` tocan el final; `shift`/`unshift` tocan el principio (y reindexan todo).
- 🔍 `.indexOf()` → posición o `-1`; `.includes()` → prueba de pertenencia booleana.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🎒 Inventarios, barras rápidas, listas de pelotón, cargas de habilidades
- 🗺️ Filas de mapas, semillas de mazmorra, entradas de generación procedural
- 🏆 Tablas de récords y tablas de clasificación
- 📜 Colas de diálogo, órdenes de turno, líneas de tiempo de acción
- 🧬 Cualquier problema de "muchos valores, un nombre" — la definición del arreglo

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Crea un arreglo de cinco objetos de botín e imprime el primero y el último con notación de corchete.
2. Reemplaza el elemento central de un arreglo de pelotón y haz `push` de un sexto miembro.
3. Haz `pop()` del último elemento e imprime lo que se eliminó.
4. Itera un arreglo de nombres de zona e imprime cada uno con su índice: `0: Ember Depths`.
5. **Pelea de jefe:** un *detector de duplicados* — itera un arreglo de botín e imprime el
   primer índice donde `.indexOf()` discrepa de un escaneo manual, usando `.includes()` para confirmar.

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — sintaxis y métodos de arreglos en una página
- [[04 - El Farmeo]] — capítulo anterior: los bucles que recorren los arreglos
- [[06 - Funciones de Habilidad]] — siguiente capítulo: envolver el trabajo con arreglos en funciones
- [[07 - Ficha de Personaje]] — objetos, la otra mitad del kit de datos de JavaScript

---
