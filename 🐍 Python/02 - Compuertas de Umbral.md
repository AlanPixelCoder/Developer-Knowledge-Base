<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 02 - Compuertas de Umbral

**Versión original en inglés:** [02 - Threshold Gates](./02%20-%20Threshold%20Gates.md)

![Status Badge](https://img.shields.io/badge/Topic-Control%20Flow-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 1 — Fundamentos de Telemetría
**Tema:** Errores, Lógica Condicional, Operadores Relacionales y Lógicos
**Etiquetas:** `#python` `#telemetria` `#condicionales` `#logica` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Lectura de un Informe Defectuoso

No todas las lecturas de una baliza empapada por la tormenta son válidas. Un conector suelto puede producir una cadena donde se espera un entero, o un script puede hacer referencia a un campo que nunca se asignó durante un arranque parcial. Antes de ramificarse por umbrales, conviene conocer los modos de fallo comunes para no confundirlos con «mal tiempo» cuando solo son errores de tipo o variables ausentes.

- **`SyntaxError`** — La línea no sigue la gramática de Python (falta dos puntos, comillas sin cerrar). El analizador falla antes de ejecutar nada.
- **`NameError`** — Se usa un nombre como `rssi_malla` antes de asignarlo. Suele deberse a una errata o a un retorno parcial en un script incompleto.
- **`TypeError`** — Operaciones entre tipos incompatibles (por ejemplo, concatenar `str` e `int`). Convertir el tipo lo soluciona cuando los valores realmente deben combinarse.

```python
# Un error común al construir una línea de registro
id_estacion = "VR-07"
bateria_porcentaje = 87
# La siguiente línea daría TypeError: can only concatenate str (not "int") to str
# print("Batería: " + bateria_porcentaje + "%")
# Solución: convertir a str
print("Batería: " + str(bateria_porcentaje) + "%")
```

## Salida

```text
Batería: 87%
```

## Cuándo Activar la Alarma

Con valores válidos, el trabajo pasa a tomar decisiones. Verdant Relay trata ciertas lecturas como compuertas: si el voltaje está por debajo del mínimo, la baliza debe informar `BATERIA_BAJA` y aplazar una tarea de alto consumo; si la temperatura supera un límite estricto, debe señalar `SOBRECALENTAMIENTO` sin importar la carga. `if`, `elif` y `else` permiten tomar distintos caminos según resultados booleanos.

```python
bateria_porcentaje = 23
if bateria_porcentaje < 30:
    print("VR-07 :: BATERIA_BAJA — aplazar sincronización de alto consumo")
else:
    print("VR-07 :: BATERIA_OK — sincronización completa permitida")
```

## Salida

```text
VR-07 :: BATERIA_BAJA — aplazar sincronización de alto consumo
```

Los operadores relacionales (`==`, `!=`, `>`, `<`, `>=`, `<=`) producen `True`/`False`. Cuando hay más de dos casos, se encadenan con `elif`. El orden importa: gana la primera condición que evalúe `True` y las demás se omiten para esa pasada.

```python
temp_nucleo_c = 41.7
if temp_nucleo_c >= 45.0:
    print("VR-07 :: SOBRECALENTAMIENTO_CRITICO")
elif temp_nucleo_c >= 38.0:
    print("VR-07 :: AVISO_SOBRECALENTAMIENTO")
elif temp_nucleo_c >= 35.0:
    print("VR-07 :: TEMPERATURA_ELEVADA")
else:
    print("VR-07 :: TEMP_OK")
```

## Salida

```text
VR-07 :: AVISO_SOBRECALENTAMIENTO
```

> [!IMPORTANT]
> El orden de los umbrales es un algoritmo, no una cuestión de estilo. Hay que comprobar primero la condición más severa. Si `>= 38.0` estuviera antes que `>= 45.0`, una lectura realmente crítica se notificaría solo como aviso, un intercambio sutil pero peligroso en telemetría.

## Combinar Condiciones

A veces una compuerta depende de dos cosas a la vez. Una baliza solo puede intentar un relé por malla si está enlazada *y* tiene suficiente carga. O puede recurrir a una caché local si tiene poca carga *o* está desconectada. Los operadores lógicos combinan expresiones booleanas: `and` requiere ambas, `or` requiere al menos una, `not` las invierte.

| A | B | A and B | A or B |
| :--- | :--- | :--- | :--- |
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

```python
enlace_malla = True
bateria_porcentaje = 52
if enlace_malla and bateria_porcentaje >= 40:
    print("VR-07 :: INTENTO_RELE")
else:
    print("VR-07 :: CACHE_LOCAL")
```

## Salida

```text
VR-07 :: INTENTO_RELE
```

Cuando las condiciones se complican, suele quedar más claro calcular un booleano en una variable con un nombre significativo (por ejemplo, `puede_relevar = enlace_malla and bateria_porcentaje >= 40`) que anidarlo en exceso. La legibilidad vence a la astucia cuando hay que depurar con mal tiempo.

> [!CAUTION]
> No se debe confundir la asignación `=` con la igualdad `==`. `if bateria_porcentaje = 30:` da un error de sintaxis en una condición; `if bateria_porcentaje == 30:` compara valores. Ese error tipográfico pasa fácilmente desapercibido.

### Tarea 2: Auditoría de Umbrales

Escribe la lógica para la baliza `VR-09` con batería 26%, `enlace_malla` True, `temp_nucleo_c` 39.2. Imprime exactamente una línea de estado: `CRITICO` si batería < 20, si no `BAJO` si batería < 30, si no `OK`. Por separado, imprime `RELE` si `enlace_malla` es True y batería >= 25, si no `CACHE`. Respeta ese orden y no añadas texto extra.
