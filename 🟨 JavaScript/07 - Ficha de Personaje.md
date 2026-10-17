# 07. Ficha de Personaje

**Versión original en inglés:** [07 - Character Sheet.md](07%20-%20Character%20Sheet.md)

**Curso:** JavaScript
**Tema:** Objetos, propiedades, notación con punto, actualizar y agregar campos, métodos, `this` y el proyecto Pase de Gremio
**Tags:** `#javascript` `#objects` `#properties` `#methods` `#game-dev`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-INTERMEDIO-E67E22?style=for-the-badge" alt="Intermedio">
  <img src="https://img.shields.io/badge/Lecciones-34_--_38_%2B_Proyecto-7C5CFF?style=for-the-badge" alt="Lecciones 34 a 38 más proyecto">
  <img src="https://img.shields.io/badge/Estado-Completado-00C2A8?style=for-the-badge" alt="Completado">
  <img src="https://img.shields.io/badge/Trama-Emberfall-FF6B35?style=for-the-badge" alt="Emberfall">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Doce variables sueltas no describen a un héroe. Un **objeto** sí: un nombre, una ficha entera
de valores etiquetados — nombre, clase, nivel, oro — e incluso **acciones** que el héroe puede
realizar. Este capítulo completa el kit de datos de JavaScript. Al final construirás un **Pase
de Gremio** con métodos vivos que mejoran un billete y calculan su tiempo de viaje. Referencia:
[[00b - Chuleta de JavaScript]].

> [!NOTE]
> **Todo el capítulo en una frase**
> Un objeto es una colección de **pares clave-valor** entre llaves `{}`; lees y escribes los
> pares con **notación con punto**, y una función guardada dentro de un objeto es un
> **método** — una acción que el objeto sabe realizar.

---

## 01. La Ficha

### ¿Qué es un Objeto?

Un **objeto** es un tipo de dato central para guardar colecciones de datos y comportamientos
relacionados. Mientras un arreglo es una lista ordenada, un objeto es una bolsa **etiquetada**:
cada valor responde a un nombre que tú eliges:

```js
const book = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  year: 1937
};
```

Cada par `key: value` es una **propiedad**. Los pares se separan con comas y van entre llaves
`{}`.

### Misión: El Objeto Pizza

El pedido de la taberna, como lo ve la cocina — toppings, estilo, porciones, precio, todo
bajo un nombre:

```js
const pizza = {
  topping: "Pepperoni 🍕",
  type: "Hand-tossed",
  slices: 12,
  price: 14.99
};

console.log(pizza);
```

Compara el objeto con cuatro variables paralelas: mismos datos, pero el objeto puede pasarse
a una función como **un solo argumento** — y así es como todo sistema real mueve un
personaje, un objeto o un archivo de guardado.

---

## 02. Leyendo la Ficha

### Propiedades y Notación con Punto

Una **propiedad** es un par clave-valor dentro del objeto. La **notación con punto** la lee:
un punto `.` seguido del nombre de la propiedad:

```js
const stadium = {
  name: "Dodger Stadium",
  location: "Los Angeles, CA",
  capacity: 56000,
  soldOut: false
};

console.log(stadium.name);     // Dodger Stadium
console.log(stadium.capacity); // 56000
```

Pedir una propiedad que no existe devuelve `undefined` — el mismo silencio que un índice de
arreglo fuera de rango en [[05 - Inventario]].

### Agregar Propiedades

La notación con punto a la izquierda del `=` también **crea** propiedades que nunca se
declararon:

```js
const car = {};
car.model = "Honda";
car.year = 2024;
car.color = "white";
car.used = false;
```

Un objeto vacío es un punto de partida válido — construye la ficha campo por campo a medida
que el juego los descubre.

---

## 03. Editando la Ficha

### Actualizar una Propiedad Existente

Asignar un valor nuevo a una clave existente la actualiza — sin ceremonia:

```js
const user = {
  username: "@ashwalker",
  verified: false
};

user.verified = true; // actualizado
```

### Agregar una Propiedad Nueva

Asignar a una clave que aún no existe la **agrega**. El motor no se queja, porque los objetos
no tienen esquema fijo:

```js
const fruit = {
  name: "apple",
  quantity: 10
};

fruit.organic = true; // propiedad de nueva creación
```

### Misión: Registro de Captura

Un registro de captura se actualiza a medida que corre la partida — agrega una bandera, luego
voltea y renombra la entrada:

```js
const pokemon = {
  name: "Pikachu",
  type: "Electric ⚡",
  level: 25
};

pokemon.isCaught = false; // agregada
pokemon.isCaught = true;  // actualizada
pokemon.name = "Sparky";  // renombrada
```

> [!WARNING]
> **El ty po que se esconde.** `hero.hp = 100` y `hero.HP = 100` crean **dos propiedades
> distintas**. JavaScript no te avisará — un camino de código escribe `hp`, otro lee `HP`, y
> el héroe misteriosamente sigue con la vida llena. Elige una convención de mayúsculas para
> los nombres de propiedad (camelCase, como todo lo demás en esta vault) y nunca te desvíes.

---

## 04. Acciones

### Métodos de Objeto

Un **método** es una función guardada dentro de un objeto — una acción que el objeto puede
realizar. Dos sintaxis, un comportamiento:

```js
const phone = {
  model: "iPhone 11 Pro Max",
  // Sintaxis tradicional de función:
  ringtone: function () {
    console.log("Ring, ring! 📱");
  },
  // Sintaxis abreviada de método:
  vibrate() {
    console.log("Bzz, bzz!");
  }
};

phone.ringtone(); // llamando al método
phone.vibrate();
```

Llama a un método con la misma notación con punto que a una propiedad, seguida de `()` —
las propiedades se leen, los métodos se **ejecutan**.

### La palabra clave `this`

Dentro de un método, `this` se refiere **al propio objeto** — la ficha leyendo sus propios
campos. Un ejemplo de granja que se presenta solo:

```js
const pig = {
  name: "Napoleon",
  type: "pig",
  age: 63,
  makeSound() {
    console.log(this.name + " is a " + this.age + " year old " + this.type + " that goes oink!");
  }
};

pig.makeSound();
// Napoleon is a 63 year old pig that goes oink!
```

`this.name` se resuelve contra `pig` cuando se llama como `pig.makeSound()` — y contra
cualquier otro objeto si el mismo método se copia allí después. Esa indirección es exactamente
lo que hace que un método sirva a un elenco entero.

---

## 05. El Pase de Gremio

### Checkpoint: Resumen del capítulo

- Los objetos guardan datos y comportamiento relacionados como **pares clave-valor** en `{}`.
- La **notación con punto** lee, actualiza y crea propiedades.
- Una función dentro de un objeto es un **método**; llámala con `obj.method()`.
- `this` apunta al objeto sobre el que se llamó el método — sus propios campos, bajo demanda.

### Proyecto: Pase de Gremio

La cápstone junta el capítulo: un objeto de pase de viaje con campos de datos **y** dos métodos
vivos. `upgrade()` voltea un booleano sobre `this`; `flightTime()` calcula la duración desde
las horas de salida y llegada — envolviendo la resta en un `let` y comprobando el caso de
medianoche:

```js
const departTripTicket = {
  name: "Alan Lozano",
  from: "Mexico City (MEX)",
  to: "Banff, Canada (YYC)",
  businessClass: false,
  leaveTime: 8,
  arriveTime: 14,
  upgrade() {
    if (this.businessClass) {
      console.log("Your ticket is already business class!");
    } else {
      this.businessClass = true;
    }
  },
  flightTime() {
    let travelTime = this.arriveTime - this.leaveTime;
    if (travelTime < 0) {
      travelTime += 24;
    }
    console.log(`Flight duration: ${travelTime} hours`);
  }
};

departTripTicket.upgrade();   // this.businessClass → true
departTripTicket.flightTime(); // "Flight duration: 6 hours"
```

Mira lo que acaba de pasar: el objeto sostiene sus propios datos, se mejora **a sí mismo** y
calcula su propia duración — el llamador nunca toca un campo directamente. Esa es toda la
promesa de los objetos: los datos y las operaciones sobre ellos, viajando juntos. El capítulo
[[06 - Funciones de Habilidad]] aportó la lógica; este capítulo le dio un hogar.

> [!TIP]
> **Versión para game dev**
> Esto es una ficha de personaje, un billete de misión, una tarjeta de objeto — la misma
> forma. Cambia los campos por `hp`, `mp` y `skills`, agrega un método `takeDamage(amount)`
> que mute `this.hp`, y has escrito el núcleo de todo inventario y sistema de entidades de RPG
> jamás publicado.

---

## ⚡ XP Ganados: Ideas Clave

- 🗂️ Un objeto = un nombre = muchos valores **etiquetados**: `{ key: value, ... }`.
- ➕ La notación con punto lee, actualiza **y** crea propiedades — sin paso de declaración.
- ❓ Las propiedades desconocidas se leen como `undefined`; los nombres distinguen mayúsculas, los ty pos incluidos.
- 🛠️ Los métodos son funciones dentro de objetos; `obj.method()` ejecuta, `obj.property` lee.
- 🪞 `this` es el objeto hablando de sí mismo — el ancla del método.

---

## 🎁 Tabla de Botín: Casos de Uso Reales

- 🧑‍🎤 Fichas de personaje, archivos de guardado, perfiles de jugador
- 🗺️ Estado del mundo: hora del día, clima, zona actual, banderas de misión
- 🧾 Carritos de compra, billetes, facturas — cualquier cosa con campos con nombre
- ⚔️ Entidades: campos de datos más `takeDamage()`, `levelUp()`, `usePotion()`
- 📦 Respuestas de API — el JSON que mueve la web moderna es objetos hasta el fondo

---

## 🎮 Misiones Secundarias: Ejercicios de Práctica

1. Modela a tu héroe como un objeto con cuatro propiedades e imprime una frase sobre ellos.
2. Agrega una quinta propiedad que no existiera en la declaración.
3. Escribe un método con `this` que imprima el nombre y el nivel del héroe.
4. Llama a un método del objeto dos veces y confirma que `this` se resuelve igual en ambas.
5. **Pelea de jefe:** un objeto de *objeto de tienda* — `name`, `price`, `stock` — con un
   método `buy()` que reduzca `stock` en uno e imprima la línea del recibo; llámalo hasta que
   imprima "Out of stock".

---

## 🔗 Ver También

- [[00b - Chuleta de JavaScript]] — sintaxis de objeto y métodos en una página
- [[06 - Funciones de Habilidad]] — capítulo anterior: las funciones que los objetos guardan como métodos
- [[08 - HUD Vivo]] — siguiente capítulo: los objetos conocen la página — el DOM es un objeto gigante
- [[05 - Inventario]] — arreglos y objetos, lado a lado, los dos kits de datos

---
