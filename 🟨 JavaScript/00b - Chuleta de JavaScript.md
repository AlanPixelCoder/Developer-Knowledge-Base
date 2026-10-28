# 00b. Chuleta de JavaScript

**Versión original en inglés:** [00b - JavaScript Cheatsheet.md](00b%20-%20JavaScript%20Cheatsheet.md)

**Curso:** JavaScript
**Tema:** Referencia rápida del lenguaje base: consola, variables, tipos, operadores, condicionales, bucles, arreglos, funciones y objetos
**Tags:** `#javascript` `#cheatsheet` `#reference` `#core-language` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE_A_INTERMEDIO-6CC24A?style=for-the-badge" alt="De principiante a intermedio">
  <img src="https://img.shields.io/badge/Cubre-Cap%C3%ADtulos_01_--_07-7C5CFF?style=for-the-badge" alt="Capítulos 01 a 07">
  <img src="https://img.shields.io/badge/Tipo-Chuleta-00C2A8?style=for-the-badge" alt="Chuleta">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Una página para todo el lenguaje base. Cada sentencia de aquí se introdujo en
[[01 - Inserta la Moneda]] hasta [[07 - Ficha de Personaje]] — nada de esta chuleta es nuevo.
El DOM, los estilos, los eventos y `addEventListener` viven en
[[00c - Chuleta de JavaScript II]].

> [!TIP]
> Imprímela o tenla en un panel dividido junto a tu editor. Una página escrita sin consultar
> esta chuleta es como se produce la sopa de `let`: variables redeclaradas porque nada en la
> chuleta parecía mal.

**El hilo conductor de este módulo: Emberfall**, un roguelike de mazmorra. Cada ejercicio
construye parte de su lógica de juego: el recibo de la tienda, el calculador de daño por
caída, el dado de mazmorra, el pase de temporada, la semilla del inventario, el analizador
de registro de combate, la ficha de personaje. El código es el mismo código que publica un
estudio real — solo cambian las palabras.

---

## 🖥️ Consola y Comentarios

```js
console.log("The dungeon opens at dawn.");
console.log(5 + 3); // evaluates first: 8

// Single-line comment
/*
  Multi-line
  comment
*/
```

| Sentencia | Qué hace |
| :--- | :--- |
| `console.log(valor)` | Imprime en la Consola de Depuración — tus ojos al depurar |
| `// comentario` | El motor lo ignora; documentación para humanos |
| `/* ... */` | Comentario multilínea; el motor se salta todo lo de dentro |

---

## 📦 Variables y Tipos

### Declarar

| Palabra clave | ¿Reasignar? | Ámbito | Úsala para |
| :--- | :--- | :--- | :--- |
| `const` | ❌ | Bloque | Por defecto — todo lo que conserva su valor |
| `let` | ✅ | Bloque | Contadores, totales, todo lo que cambia |
| `var` | ✅ | Función | Solo legado — nunca lo uses en código nuevo |

```js
const MAX_HP = 100;  // nunca cambia — SERPIENTE_EN_MAYÚSCULAS
let hp = 80;         // cambia con cada golpe
```

### Los Siete Tipos

| Tipo | Ejemplo | Notas |
| :--- | :--- | :--- |
| `string` | `"Emberfall"` / `'Emberfall'` / `` `Emberfall` `` | Texto; los backticks permiten `${var}` |
| `number` | `42` / `3.14` | Enteros y flotantes son un solo tipo |
| `bigint` | `9007n` | Poco usado; enteros enormes |
| `boolean` | `true` / `false` | Banderas: `isCaught`, `soldOut` |
| `undefined` | `x = undeclared;` | Declarado pero nunca asignado |
| `null` | `x = null;` | Intencionalmente vacío — una elección |
| `object` | `{ a: 1 }` / `[1, 2]` | Los tipos compuestos — ver abajo |

```js
typeof "Emberfall"   // "string"
typeof 42            // "number"
typeof true          // "boolean"
typeof undefined     // "undefined"
typeof null          // "object" ← la famosa mentira de JS
```

### Literales de Plantilla

```js
const nombre = "Ashwalker";
const nivel = 12;
console.log(`${nombre} is level ${nivel}`); // Ashwalker is level 12
```

---

## 🧮 Operadores

### Aritméticos

| Operador | Significado | Ejemplo |
| :--- | :--- | :--- |
| `+` | Suma / concatenación | `2 + 2` → `4` |
| `-` | Resta | `10 - 4` → `6` |
| `*` | Multiplicación | `3 * 3` → `9` |
| `/` | División | `9 / 3` → `3` |
| `%` | Módulo — el residuo | `7 % 3` → `1` |
| `**` | Exponente | `2 ** 10` → `1024` |
| `++` | Más uno | `hp++` |
| `--` | Menos uno | `hp--` |

> [!NOTE]
> `+` está sobrecargado: los números suman, las cadenas se unen. `"HP: " + hp` concatena;
> `hp + 1` suma. Mezclar ambos en una expresión es la fuente clásica de los errores
> `"1001"`.

### Comparación

| Operador | Se lee como | Funciona con |
| :--- | :--- | :--- |
| `===` | Igualdad estricta | Valores **y** tipos — usa siempre este |
| `!==` | Desigualdad estricta | Valores **y** tipos — usa siempre este |
| `==` | Igualdad laxa | Convierte tipos antes — evítalo |
| `!=` | Desigualdad laxa | Convierte tipos antes — evítalo |
| `>` `>=` `<` `<=` | Mayor / menor | Números |

```js
5 == "5"   // true  — la cadena se convierte y luego se compara
5 === "5"  // false — tipos distintos, punto final
```

### Lógicos

| Operador | Se lee como | Atajo |
| :--- | :--- | :--- |
| `&&` | Y | Ambos lados deben ser verdaderos |
| `\|\|` | O | Al menos un lado verdadero |
| `!` | No | Invierte el valor |

### Asignación

`=` · `+=` · `-=` · `*=` · `/=` · `%=` — lee, modifica y reescribe en una sola sentencia:
`puntos += 10` es `puntos = puntos + 10`.

---

## 🔀 Condicionales

```js
if (hp === 0) {
  console.log("Game over");
} else if (hp < 25) {
  console.log("Low HP — heal!");
} else {
  console.log("Keep going");
}
```

```js
const estado = hp === 0 ? "down" : "up"; // ternario: condición ? a : b
```

| Forma | Recúrrela cuando |
| :--- | :--- |
| `if / else if / else` | La decisión tiene resultados distintos |
| Ternario `? :` | La decisión es un valor corto |
| `switch` | Una variable se compara con muchos casos exactos |

---

## 🔁 Bucles

| Bucle | Corre mientras | Úsalo para |
| :--- | :--- | :--- |
| `while (cond)` | La condición sea verdadera | Recuento desconocido — sigue pescando |
| `for (init; cond; step)` | La condición sea verdadera | Recuento conocido — el por defecto |
| `for...of` | Queden elementos | Cada elemento de un arreglo o cadena |

```js
for (let i = 0; i < 5; i++) { console.log(i); }   // 0 1 2 3 4
while (pez.length < 10) { pez.push("🐟"); }
for (const obj of inventario) { console.log(obj); }
```

| Control | Efecto |
| :--- | :--- |
| `break` | Sale del bucle **ya** |
| `continue` | Salta a la siguiente iteración |
| Bucle anidado | Un bucle dentro de otro — el interior corre entero en cada vuelta exterior |

---

## 📚 Arreglos

```js
const inventario = ["Sword", "Shield", "Potion"];
```

| Accesor / Método | Qué hace |
| :--- | :--- |
| `arr[i]` | El elemento en el índice `i` — se cuenta desde **0** |
| `arr.length` | Cuántos elementos — siempre uno pasado el último índice |
| `arr.push(x)` | Agrega `x` al **final** |
| `arr.pop()` | Elimina y devuelve el **último** elemento |
| `arr.unshift(x)` | Agrega `x` al **frente** |
| `arr.shift()` | Elimina y devuelve el elemento del **frente** |
| `arr.indexOf(x)` | Índice de `x`, o `-1` si no está |
| `arr.includes(x)` | `true` / `false` — pregunta en vez de buscar |
| `arr.slice(a, b)` | Una copia de los elementos de `a` hasta (sin incluir) `b` |

> [!WARNING]
> Los índices van de `0` a `length - 1`. Leer `inventario[inventario.length]` devuelve
> `undefined` — el mismo silencio que una propiedad inexistente. Comprueba `length` antes
> de indexar.

---

## ⚙️ Funciones

```js
function curar(objetivo, cantidad) {
  return objetivo + cantidad; // de vuelta al llamador, y la función se detiene
}

const atacar = (potencia) => potencia * 2; // arrow — atajo de una línea

console.log(curar(50, 25)); // 75
```

| Concepto | Regla |
| :--- | :--- |
| Parámetro | El nombre en la definición — `objetivo, cantidad` |
| Argumento | El valor que se pasa — `50, 25` |
| `return` | Devuelve un valor; termina la función de inmediato |
| Sin `return` | Devuelve `undefined` |
| Ámbito | Los parámetros y los `let`/`const` de dentro son privados de la función |
| Arrow `=>` | Atajo; ideal para una línea y para callbacks |

---

## 🗂️ Objetos

```js
const heroe = {
  name: "Ashwalker",
  level: 12,
  greet() {
    console.log(`I am ${this.name}`);
  }
};
```

| Operación | Sintaxis | Nota |
| :--- | :--- | :--- |
| Leer | `heroe.name` | Notación con punto |
| Actualizar | `heroe.level = 13` | Clave existente |
| Crear | `heroe.guild = "Ember"` | Clave nueva — sin declaración |
| Método | `heroe.greet()` | Función guardada dentro del objeto |
| Autorreferencia | `this.name` | El objeto hablando de sí mismo |

> [!NOTE]
> Los arreglos y los objetos son ambos compuestos, con contratos distintos: un **arreglo**
> es ordenado y se indexa por posición; un **objeto** es etiquetado y se accede por clave.
> Los personajes son objetos; los inventarios son arreglos — y el inventario de un personaje
> es un arreglo de objetos.

---

## 🎮 La Versión de Una Página

Todo lo de esta chuleta en un solo archivo — una tienda de Emberfall:

```js
const shop = {
  name: "Emberfall Armory",
  gold: 120,
  stock: ["Sword", "Shield", "Potion"],
  sell(item) {
    const index = this.stock.indexOf(item);
    if (index === -1) {
      console.log("Out of stock!");
      return;
    }
    this.stock.pop();
    this.gold += 15;
    console.log(`Sold ${item} — gold: ${this.gold}`);
  }
};

for (let i = 0; i < shop.stock.length; i++) {
  console.log(shop.stock[i]);
}

shop.sell("Potion"); // Sold Potion — gold: 135
shop.sell("Dragon"); // Out of stock!
```

---

## ⚠️ Trampas que Conviene Memorizar

| Trampa | Qué pasa de verdad |
| :--- | :--- |
| Confundir `let` con `const` | Reasignar un `const` lanza un `TypeError` — el motor se detiene |
| `=` dentro de un `if` | Asigna en vez de comparar; usa `===` |
| `==` en vez de `===` | La conversión de tipos esconde errores: `0 == ""` es `true` |
| Índice fuera de uno | `arr[arr.length]` es `undefined`, no un error — silencio, no choque |
| Objeto `const` con campos mutados | Permitido — `const` congela el enlace, no el contenido |
| Declarar dentro de un bucle con `var` | Una sola variable compartida por todas las iteraciones; `let` da una por vuelta |
| Olvidar `()` en un método | Pasas la función en vez de llamarla |
| `this` fuera de un método | `this` no es el objeto que crees — mantenlo dentro de métodos |

---

## 🔗 Ver También

- [[00c - Chuleta de JavaScript II]] — el DOM, `.style`, eventos y `addEventListener`
- [[01 - Inserta la Moneda]] — consola y comentarios, donde empieza esta chuleta
- [[07 - Ficha de Personaje]] — objetos, la última parada antes del DOM
- [[12 - La Carrera de la Marea]] — maquetando la página que este lenguaje va a manejar

---
