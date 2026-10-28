# 02. Atributos del Jugador

**Versión original en inglés:** [02 - Player Stats.md](02%20-%20Player%20Stats.md)

**Curso:** JavaScript
**Capítulo:** 2 — Carga del Gabinete
**Tema:** let, const, tipos, aritmética, coerción
**Etiquetas:** `#javascript` `#variables` `#tipos` `#aritmetica` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-2-7C5CFF?style=for-the-badge" alt="Capítulo 2">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Todo gabinete necesita una ficha de carga. El Gremio anota el número de créditos, el número de serie, si queda un crédito pendiente y el nombre clave del piloto. Esos valores cambian durante una partida, así que hay que guardarlos, no reescribirlos a mano. Ahí entran las variables.

## Ranuras para valores

`const` fija una ranura a su primer valor. `let` abre una ranura que se pretende modificar. Usa `const` por defecto; recurre a `let` solo cuando el valor vaya a cambiar durante la partida.

```js
const numeroSerie = "GAB-9";
const idGremio = "GREMIO-PRIME";
let creditos = 3;
let aliasPiloto = "RIVET";

console.log(numeroSerie + " | " + idGremio);
console.log("Piloto: " + aliasPiloto + " | Créditos: " + creditos);
```

## Salida

```text
GAB-9 | GREMIO-PRIME
Piloto: RIVET | Créditos: 3
```

> [!CAUTION]
> No se puede reasignar `const`. Intentarlo provoca un error. La clave es la intención: las constantes son para identidades que no deben cambiar durante toda la partida, no para valores que el gabinete modifica.

## Lo que puede guardar el gabinete

JavaScript etiqueta los valores por tipo en tiempo de ejecución. Para la ficha de carga lo más común es lo siguiente:

| Tipo | Ejemplo | Notas |
| :--- | :--- | :--- |
| `number` | `creditos = 2`, `calor = 37.5` | Enteros y decimales comparten el mismo tipo. |
| `string` | `"RIVET"`, `"GAB-9"` | Texto entre comillas que coincidan. |
| `boolean` | `tieneBoleto = true` | `true` o `false` para puertas lógicas. |
| `undefined` | declarada sin asignar | Existe la ranura pero no hay valor — fácil de pasar por alto. |

```js
let tieneBoleto = false;
let notasReparacion; // undefined hasta que se asigne
console.log(typeof tieneBoleto);
console.log(typeof notasReparacion);
```

## Salida

```text
boolean
undefined
```

`typeof` indica lo que ve el motor. Conviene fiarse de los tipos, pero `undefined` no es lo mismo que `null`. Aquí simplemente significa "sin asignación".

## Aritmética y el coste de un reintento

Un reintento cuesta créditos. El gabinete también controla el desgaste. La aritmética con números es predecible, pero la concatenación con cadenas cambia la forma en que leemos la expresión.

```js
let creditos = 5;
creditos = creditos - 1; // se gasta un reintento
console.log("Créditos restantes: " + creditos);

let calorBase = 12;
let overclock = 1.5;
console.log("Carga térmica: " + (calorBase * overclock));
```

## Salida

```text
Créditos restantes: 4
Carga térmica: 18
```

> [!TIP]
> Usa paréntesis al mezclar aritmética con concatenación. Sin ellos el cálculo sigue siendo correcto, pero con expresiones más largas es fácil confundirse; los paréntesis dejan la intención clara.

## ¿Por qué importan los tipos?

El motor no adivina siempre nuestra intención. Cuando se mezclan tipos puede haber coerción, por eso conviene distinguir explícitamente entre cadenas y números. Usar `const` para identidades fijas y `let` para contadores evita reasignaciones accidentales cuando la lógica crece sobre la misma ficha.

**Siguiente:** [[03 - Tiradas de Botín]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
