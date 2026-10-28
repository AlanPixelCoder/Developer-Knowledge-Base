# 07. Ficha de Personaje

**Versión original en inglés:** [07 - Character Sheet.md](07%20-%20Character%20Sheet.md)

**Curso:** JavaScript
**Capítulo:** 7 — Ficha de la Lista de Pilotos
**Tema:** objetos, propiedades, métodos, this
**Etiquetas:** `#javascript` `#objetos` `#metodos` `#this` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-7-7C5CFF?style=for-the-badge" alt="Capítulo 7">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Un piloto de la lista del Gremio es mucho más que un nombre. Tiene un nombre clave, un gabinete asignado, un saldo de créditos y un rango. Agrupar valores relacionados en un objeto evita una pila de variables sueltas y mantiene la ficha coherente.

## Agrupar propiedades

Los objetos usan `{}` con pares clave:valor. Se accede con notación de punto o con corchetes.

```js
let piloto = {
  alias: "RIVET",
  gabinete: "GAB-9",
  creditos: 4,
  rango: "TRIPULACIÓN"
};
console.log(piloto.alias);
console.log(piloto["gabinete"]);
```

## Salida

```text
RIVET
GAB-9
```

> [!TIP]
> La notación de punto es más limpia para claves conocidas. La notación con corchetes es útil cuando la clave viene de una variable o tiene espacios (raro, pero posible).

## Métodos y `this`

Cuando una función vive dentro de un objeto, se llama método. Dentro de ese método, `this` hace referencia al objeto sobre el que se llamó, así puede leer sus propias propiedades.

```js
let piloto = {
  alias: "RIVET",
  creditos: 2,
  gastarCredito: function() {
    this.creditos = this.creditos - 1;
    console.log(this.alias + ": CRÉDITOS RESTANTES " + this.creditos);
  }
};
piloto.gastarCredito();
piloto.gastarCredito();
```

## Salida

```text
RIVET: CRÉDITOS RESTANTES 1
RIVET: CRÉDITOS RESTANTES 0
```

> [!IMPORTANT]
> `this` depende del contexto. Si copias `piloto.gastarCredito` a otra variable y lo llamas sin el objeto, el enlace puede perderse. Por ahora, llama siempre a los métodos como `objeto.metodo()` para mantener el enlace correcto.

## Actualizar y añadir

Los objetos son mutables: se puede actualizar una propiedad existente o añadir una nueva en cualquier momento.

```js
let piloto = { alias: "RIVET", rango: "TRIPULACIÓN" };
piloto.rango = "SENIOR";
piloto.ultimaPartida = "GAB-9";
console.log(piloto.rango + " | " + piloto.ultimaPartida);
```

## Salida

```text
SENIOR | GAB-9
```

## ¿Por qué usar objetos?

Los objetos modelan una sola entidad con muchos atributos y comportamientos. Los arrays modelan listas de entidades. La ficha del piloto es una entidad con estado (`creditos`) y acciones (`gastarCredito()`). Mantener el estado y la lógica que lo modifica juntos hace que la lista sea más fácil de razonar y menos propensa a errores cuando crece.

**Siguiente:** [[08 - HUD Vivo]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
