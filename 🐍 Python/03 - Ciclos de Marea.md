<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 03 - Ciclos de Marea

**Versión original en inglés:** [03 - Tide Cycles](./03%20-%20Tide%20Cycles.md)

![Status Badge](https://img.shields.io/badge/Topic-Loops-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 1 — Fundamentos de Telemetría
**Tema:** Bucles while, bucles for, range(), Control de iteración
**Etiquetas:** `#python` `#telemetria` `#bucles` `#iteracion` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Por Qué Fallan las Repeticiones

Algunas tareas de telemetría son finitas y conocidas de antemano: sondear cuatro canales de sensores, imprimir una fila de cabecera para doce lecturas o recorrer una lista fija de balizas. Otras no lo son: un reintento de enlace debe seguir intentándolo hasta que tenga éxito o hasta agotar los intentos. Un bloque escrito dos veces es un riesgo de copiar y pegar; un bucle es una regla que puede ejecutarse cero, algunas o muchas veces sin duplicar código. Cada pasada por el bloque es una **iteración**.

## `while`: Comprobar Antes de Ejecutar

Un bucle `while` comprueba su condición al inicio de cada iteración. Si es falsa inicialmente, el cuerpo nunca se ejecuta. Eso encaja bien con la lógica de reintentos: comprobar la conectividad y solo reintentar mientras esté caída.

```python
reintentos = 0
max_reintentos = 3
enlazado = False
while not enlazado and reintentos < max_reintentos:
    reintentos += 1
    print(f"VR-07 :: REINTENTO_ENLACE {reintentos}")
    if reintentos == 3:
        enlazado = True  # éxito simulado en el tercer intento
print(f"VR-07 :: ESTADO_ENLACE {enlazado}")
```

## Salida

```text
VR-07 :: REINTENTO_ENLACE 1
VR-07 :: REINTENTO_ENLACE 2
VR-07 :: REINTENTO_ENLACE 3
VR-07 :: ESTADO_ENLACE True
```

Un centinela es un valor que significa «parar», no un dato. Al leer hasta un centinela, debe existir alguna ruta que lo produzca dentro del bucle, ya sea desde una entrada simulada o con un `break`. Si nada puede cambiar la condición, el bucle nunca termina.

> [!CAUTION]
> Todo bucle `while` necesita una salida. Actualiza la variable que alimenta la condición dentro del cuerpo, o usa `break` con una justificación clara. Un bucle infinito es barato de escribir y caro de depurar en una baliza remota.

## `for`: Contar sobre un Conjunto Conocido

Cuando el recuento o la secuencia se conocen, `for` con `range()` es más limpio. `range(n)` produce `0` a `n-1`; `range(inicio, fin)` va hasta pero sin incluir `fin`; `range(inicio, fin, paso)` cambia el incremento.

```python
# Registrar un breve lote de lecturas por canal
for ch in range(1, 5):
    print(f"VR-07 :: LECTURA_CH{ch}")
```

## Salida

```text
VR-07 :: LECTURA_CH1
VR-07 :: LECTURA_CH2
VR-07 :: LECTURA_CH3
VR-07 :: LECTURA_CH4
```

La interpolación de cadenas con f-strings mantiene los registros compactos y legibles. El marcador `{ch}` se evalúa en tiempo de ejecución, ideal para IDs de estación, números de canal o marcas de tiempo en líneas concisas.

## Decisiones Anidadas en un Bucle

La telemetría real suele combinar bucles con condiciones. Un lote de descargas puede pasar cada archivo por una validación rápida: omitir un archivo corrupto conocido, avisar si es grande o, en caso contrario, registrarlo como en cola. Poner `if/elif/else` dentro de un bucle es normal, pero anidar demasiado complica el seguimiento — es mejor usar comprobaciones tempranas cuando sea posible.

```python
lote = ["baliza_07_001.log", "baliza_07_002.tmp", "baliza_07_003.log"]
for nombre in lote:
    if nombre.endswith(".tmp"):
        print(f"VR-07 :: OMITE {nombre} (temp)")
        continue
    if nombre.endswith(".log"):
        print(f"VR-07 :: ENCOLA {nombre}")
    else:
        print(f"VR-07 :: AVISO {nombre} (desconocido)")
```

## Salida

```text
VR-07 :: OMITE baliza_07_002.tmp (temp)
VR-07 :: ENCOLA baliza_07_001.log
VR-07 :: ENCOLA baliza_07_003.log
```

`continue` salta a la siguiente iteración; `break` sale completamente del bucle. Ambos son útiles, pero hacen que el flujo de control sea menos obvio. Una condición bien formada suele ser más fácil de razonar que un `break` oculto en lo más profundo de la lógica.

> [!TIP]
> Si un bucle necesita su contador después de terminar, decláralo antes de la cabecera `while`. Si solo se necesita dentro de un bucle `for`, mantén su ámbito dentro del bucle.

### Tarea 3: Sondeo de Mareas

Escribe un script que sondee los canales del 1 al 6 con `range()`. Para los canales pares imprime `VR-12 :: CHx ESTABLE`, para los impares imprime `VR-12 :: CHx RUIDOSO`. Usa f-strings e imprime una línea por canal en orden.
