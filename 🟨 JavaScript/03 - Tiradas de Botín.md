# 03. Tiradas de Botín

**Versión original en inglés:** [03 - Loot Rolls.md](03%20-%20Loot%20Rolls.md)

**Curso:** JavaScript
**Capítulo:** 3 — La Puerta de Corte
**Tema:** if/else, comparaciones, operadores lógicos, Math.random()
**Etiquetas:** `#javascript` `#condicionales` `#logica` `#aleatorio` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-3-7C5CFF?style=for-the-badge" alt="Capítulo 3">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

Tras el arranque, el gabinete ya no ejecuta todas las líneas sin pensar. La Puerta de Corte bloquea el paso hasta que se cumpla una comprobación: suficientes créditos, boleto válido o anulación diaria. Los condicionales permiten bifurcar el script, y `Math.random()` permite tirar dados.

## Una bifurcación

Un `if` evalúa una expresión booleana. Si es `true`, se ejecuta su bloque. Si es `false`, no pasa nada a menos que haya un `else`.

```js
let creditos = 2;
if (creditos >= 1) {
  console.log("PUERTA: ACEPTADA - CRÉDITOS OK");
} else {
  console.log("PUERTA: BLOQUEADA - INSERTE MONEDA");
}
```

## Salida

```text
PUERTA: ACEPTADA - CRÉDITOS OK
```

> [!IMPORTANT]
> La condición debe evaluarse a `true` o `false`. Comparaciones como `>=`, `===`, `!==` devuelven booleanos; usar `=` es asignación, no comparación — es un error muy común.

## Más de dos opciones

Cuando hay más de dos resultados, `else if` crea una cadena. Solo se ejecuta el primer bloque cuya condición sea verdadera; el resto se ignoran.

```js
let claseBoleto = "tripulacion";
if (claseBoleto === "gremio") {
  console.log("PUERTA: ACCESO PRIORITARIO");
} else if (claseBoleto === "tripulacion") {
  console.log("PUERTA: ACCESO A TRIPULACIÓN");
} else if (claseBoleto === "invitado") {
  console.log("PUERTA: ACCESO A INVITADOS");
} else {
  console.log("PUERTA: BOLETO DESCONOCIDO");
}
```

## Salida

```text
PUERTA: ACCESO A TRIPULACIÓN
```

> [!TIP]
> Si las condiciones pudieran solaparse, conviene poner primero la regla más restrictiva o prioritaria. Si son mutuamente excluyentes, con condiciones precisas el orden es menos frágil.

## Lógica sin adivinanzas

A veces una sola comprobación no basta. `&&` exige que ambas sean verdaderas, `||` exige que al menos una lo sea, `!` invierte un booleano.

```js
let tieneBoleto = true;
let llaveBypass = false;
if (tieneBoleto && !llaveBypass) {
  console.log("COMPROBACIÓN: ENTRADA ESTÁNDAR");
}
if (llaveBypass || tieneBoleto) {
  console.log("COMPROBACIÓN: ENTRADA PERMITIDA");
}
```

## Salida

```text
COMPROBACIÓN: ENTRADA ESTÁNDAR
COMPROBACIÓN: ENTRADA PERMITIDA
```

> [!WARNING]
> `&&` tiene mayor precedencia que `||`. Al mezclar ambos, los paréntesis evitan errores de lectura: `(a && b) || c` no es lo mismo que `a && (b || c)`.

## Tirar el interruptor

Para probar la puerta de forma impredecible se usa `Math.random()`. Devuelve un número en `[0, 1)` (0 incluido, 1 excluido). Se escala y se redondea hacia abajo para obtener un rango.

```js
let tirada = Math.floor(Math.random() * 6) + 1; // 1..6
if (tirada >= 5) {
  console.log("INTERRUPTOR: SOBRECARGA - SUBIDA RARA");
} else if (tirada >= 3) {
  console.log("INTERRUPTOR: ZUMBIDO - ESTABLE");
} else {
  console.log("INTERRUPTOR: PARPADEO - LEVE");
}
```

## Salida

```text
INTERRUPTOR: PARPADEO - LEVE
```
(El resultado exacto depende de la tirada; lo que importa es la bifurcación.)

La idea es simple: `Math.random()` no tiene límite superior. Multiplica por el número de resultados, usa `Math.floor()` para obtener índices enteros y suma un offset si quieres empezar en 1. Es el mismo truco que se usa para dados en cualquier gabinete.

**Siguiente:** [[04 - El Farmeo]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
