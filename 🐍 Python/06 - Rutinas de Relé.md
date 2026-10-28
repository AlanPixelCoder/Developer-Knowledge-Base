<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 06 - Rutinas de Relé

**Versión original en inglés:** [06 - Relay Routines](./06%20-%20Relay%20Routines.md)

![Status Badge](https://img.shields.io/badge/Topic-Functions-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 3 — Automatización
**Tema:** Funciones, Parámetros, Argumentos, Retorno, Ámbito, Lambda
**Etiquetas:** `#python` `#telemetria` `#funciones` `#automatizacion` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## No Repitas la Comprobación

Tras escribir la misma comprobación de umbral por tercera vez, el copiar y pegar se convierte en un riesgo. Una **función** es un bloque reutilizable que hace un solo trabajo. Se define con `def` y se llama por nombre con `()`. Mantener la lógica en funciones significa que una corrección se aplica allá donde se llame.

```python
def informe_arranque():
    print("VERDANT-RELAY :: INICIO DE COMPROBACIÓN DE RUTINA")

informe_arranque()
informe_arranque()
```

## Salida

```text
VERDANT-RELAY :: INICIO DE COMPROBACIÓN DE RUTINA
VERDANT-RELAY :: INICIO DE COMPROBACIÓN DE RUTINA
```

## Los Parámetros Dan Flexibilidad

Un **parámetro** es un marcador en la definición; un **argumento** es el valor que se pasa al llamar. Los parámetros convierten una rutina fija en una genérica.

```python
def comprobacion_estacion(id_estacion, bateria_porcentaje):
    print(f"{id_estacion} :: BATERIA {bateria_porcentaje}%")

comprobacion_estacion("VR-07", 64)
comprobacion_estacion("VR-12", 26)
```

## Salida

```text
VR-07 :: BATERIA 64%
VR-12 :: BATERIA 26%
```

## Valores de Retorno, No Solo Impresiones

`print()` muestra salida en consola, pero no devuelve datos. `return` envía un valor al llamador para que pueda almacenarlo, compararlo o pasarlo. Si no hay `return`, Python devuelve `None`.

```python
def horas_restantes(reserva_mwh, consumo_mw):
    if consumo_mw <= 0:
        return None
    return reserva_mwh * 1000 / consumo_mw

h = horas_restantes(7.8, 145)
print(round(h, 1))
```

## Salida

```text
53.8
```

Dividir el trabajo en funciones pequeñas que devuelvan valores es más fácil de probar y razonar que un script grande que solo imprime.

> [!NOTE]
> Devolver `None` para una entrada inválida es una forma limpia de señalar «no se puede calcular» sin que el programa falle. El llamador puede comprobarlo.

## Ámbito: Local frente a Global

Las variables **locales** viven dentro de una función y desaparecen al volver. Las variables **globales** viven a nivel de módulo y son legibles desde cualquier sitio, pero asignar a una global dentro de una función requiere `global` (usar con moderación). Es preferible pasar valores como parámetros y devolver resultados.

```python
min_bateria = 30  # global

def puede_sincronizar(bateria_porcentaje):
    return bateria_porcentaje >= min_bateria  # lee global

print(puede_sincronizar(26))
print(puede_sincronizar(52))
```

## Salida

```text
False
True
```

## Lambda para Transformaciones Rápidas

Una **lambda** es una función anónima de una línea: `lambda args: expression`. Es útil para pasadas cortas como `map()` o `filter()`, pero si la lógica crece más allá de una expresión simple, es más claro usar `def` normal.

```python
rssi = [-62, -65, -71, -68, -64]
# Marcar enlaces débiles (< -68)
debiles = list(filter(lambda x: x < -68, rssi))
print(debiles)
```

## Output

```text
[-71]
```

> [!TIP]
> No uses lambda por defecto. Úsalo cuando necesites una función diminuta para un único uso en una llamada de orden superior.

### Tarea 6: Rutinas de Relé

Escribe `def estado_bateria(pct):` que devuelva `"BAJO"` si pct < 30, `"OK"` si pct >= 30. Llámala con 26 e imprime el resultado. También escribe `def a_dbm(mv):` que devuelva mv / 1000.0 e imprime `a_dbm(65000)`.
