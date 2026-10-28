# 01. Inserta la Moneda

**Versión original en inglés:** [01 - Insert Coin.md](01%20-%20Insert%20Coin.md)

**Curso:** JavaScript
**Capítulo:** 1 — Arranque del Gabinete
**Tema:** Salida por consola, orden de líneas, comentarios
**Etiquetas:** `#javascript` `#consola` `#comentarios` `#arcade`

<p align="left">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dificultad-PRINCIPIANTE-6CC24A?style=for-the-badge" alt="Principiante">
  <img src="https://img.shields.io/badge/Cap%C3%ADtulo-1-7C5CFF?style=for-the-badge" alt="Capítulo 1">
  <img src="https://img.shields.io/badge/Trama-Gremio%20de%20Gabinetes-FF6B35?style=for-the-badge" alt="Gremio de Gabinetes">
  <img src="https://img.shields.io/badge/Vault-Obsidian-7B3FE4?style=for-the-badge&logo=obsidian" alt="Obsidian">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=70&section=header" width="100%" alt="Ola amarilla" />
</p>

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #F7DF1E, #2DD4BF, #F7DF1E, transparent); margin: 24px 0;" />

El Gremio de Gabinetes guarda una fila de máquinas arcade medio oxidadas en su trastienda. Cada gabinete arranca desde cero: sin menú, solo una ranura para monedas y un pequeño registro de servicio. Para despertarlo hay que hablarle a ese registro con la consola del navegador, una instrucción a la vez.

## Hablarle al registro de servicio

Un gabinete no adivina. Cuando le das una instrucción, el motor la ejecuta en orden estricto de arriba a abajo. `console.log()` sirve para escribir en ese registro sin cambiar el arte del gabinete.

```js
console.log("GABINETE-7: SECUENCIA DE ARRANQUE INICIADA");
console.log("GABINETE-7: RANURA DE MONEDAS EN REPOSO");
console.log("GABINETE-7: ESPERANDO INSERCIÓN");
```

## Salida

```text
GABINETE-7: SECUENCIA DE ARRANQUE INICIADA
GABINETE-7: RANURA DE MONEDAS EN REPOSO
GABINETE-7: ESPERANDO INSERCIÓN
```

El orden es lo importante. Si cambias dos líneas, el registro cuenta una historia distinta. El motor nunca las reordena; las lee tal como están escritas.

> [!IMPORTANT]
> La ejecución es secuencial. Si la línea 1 define un estado que se lee en la línea 2, la 2 debe ir después. Cambiar el orden es un fallo lógico aunque cada línea sea sintácticamente correcta.

## Dejar notas en el script

Los técnicos del gremio anotan el motivo de cada línea para no olvidarlo. JavaScript tiene comentarios para eso: el motor los ignora por completo.

```js
// Calentar el bucle de atracción antes de que lleguen los jugadores
console.log("GABINETE-7: BUCLE DE ATRACCIÓN ACTIVADO");

/*
   NO volver a activar el contador de pagos heredado.
   El gremio lo desactivó tras atascarse el gabinete 3.
*/
console.log("GABINETE-7: CONTADOR DE PAGOS: FUERA DE LÍNEA");
```

## Salida

```text
GABINETE-7: BUCLE DE ATRACCIÓN ACTIVADO
GABINETE-7: CONTADOR DE PAGOS: FUERA DE LÍNEA
```

> [!TIP]
> Un comentario que dice *qué* hace la línea siguiente suele sobrar. Uno que dice *por qué* existe una línea rara te ahorrará horas la próxima vez.

## ¿Por qué empezar por la consola?

La consola del navegador es un intérprete en vivo: puedes probar una sola instrucción sin escribir una página HTML completa. Para un registro de gabinete es ideal: una línea resuelve una duda. Además, los errores aparecen ahí mismo: comillas sin cerrar o paréntesis sin cerrar suelen fallar al analizar, y el mensaje señala la línea exacta.

> [!WARNING]
> Las comillas deben coincidir. `"ESPERANDO` sin comilla de cierre es un error de sintaxis: el parser sigue buscando hasta encontrarla o hasta rendirse. Los paréntesis siguen la misma regla.

**Siguiente:** [[02 - Atributos del Jugador]]

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=F7DF1E&height=60&section=footer" width="100%" alt="Pie amarillo" />
</p>
