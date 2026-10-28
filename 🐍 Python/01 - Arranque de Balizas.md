<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 01 - Arranque de Balizas

**Versión original en inglés:** [01 - Beacon Boot Sequence](./01%20-%20Beacon%20Boot%20Sequence.md)

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)![Status Badge](https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge)

**Curso:** Python
**Capítulo:** 1 — Fundamentos de Telemetría
**Tema:** Entorno, Salida, Variables, Tipos de Datos y Aritmética
**Etiquetas:** `#python` `#telemetria` `#balizas` `#basicos` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Encendiendo la Red Costera

Verdant Relay mantiene varias balizas alimentadas por energía solar a lo largo de una costa azotada por tormentas. Cuando un técnico llega al amanecer para revisarlas, lo primero que debe hacer es arrancar la consola de la estación y obtener una lectura limpia. Antes de que funcione cualquier automatización, un script tiene que anunciarse, registrar los valores clave y comprobar que el enlace está activo.

En Python, eso empieza con una línea a la terminal. La función `print()` escribe en stdout sin formato oculto, exactamente lo que se necesita para una línea de telemetría concisa que otro script pueda analizar más tarde.

```python
# Mensaje de arranque de la consola de baliza
print("VERDANT-RELAY :: SECUENCIA DE ARRANQUE INICIADA")
```

## Salida

```text
VERDANT-RELAY :: SECUENCIA DE ARRANQUE INICIADA
```

La ejecución es estrictamente de arriba abajo, por lo que el orden importa. Un script de arranque que registre el voltaje antes de informar el tiempo de actividad es correcto; invertir esas líneas cuenta una historia ligeramente distinta. Esa disciplina con el orden es el primer hábito que conviene mantener cuando se rastrea un enlace inestable en medio de un temporal.

> [!NOTE]
> `print()` añade un salto de línea por defecto. Para los registros de baliza que se envían a un analizador estricto, una línea en blanco extra o que falte cambia el registro. Siempre hay que comprobar el espaciado al unir registros.

## Guardar Lecturas en Variables

Cada baliza informa de varios campos fijos al arrancar: su ID de estación, estado de carga, temperatura y si está enlazada a la malla de relé. En lugar de volver a escribir los valores, se guardan en **variables** — contenedores con nombre en memoria. La asignación se hace con `=` y el nombre a la izquierda apunta al valor a la derecha.

```python
# Instantánea al arrancar de la baliza VR-07
id_estacion = "VR-07"
bateria_porcentaje = 87
temp_nucleo_c = 16.4
enlace_malla = True

print(id_estacion)
print(bateria_porcentaje)
print(temp_nucleo_c)
print(enlace_malla)
```

## Salida

```text
VR-07
87
16.4
True
```

Python infiere los tipos en tiempo de ejecución: `"VR-07"` es `str`, `87` es `int`, `16.4` es `float`, `True` es `bool`. Esos tipos no son meramente decorativos: las operaciones se comportarán de forma distinta según ellos. Intentar sumar una cadena y un entero es un desajuste de tipos, no un atajo válido.

> [!TIP]
> Elige nombres de variable que describan el campo que representan. `bateria_porcentaje` dice mucho más que `b`, sobre todo cuando se leen registros a las 03:00 bajo la llovizna.

## Aritmética para Comprobaciones Rápidas

Un técnico a menudo necesita hacer cálculos rápidos sobre la marcha: capacidad restante, tiempo estimado de funcionamiento o una comprobación derivada del voltaje. Los operadores aritméticos de Python cubren lo básico sin necesidad de módulos extra.

| Operador | Nombre | Ejemplo | Resultado | Uso |
| :--- | :--- | :--- | :--- | :--- |
| `+` | Suma | `87 + 3` | `90` | Totales |
| `-` | Resta | `87 - 12` | `75` | Descarga |
| `*` | Multiplicación | `4 * 12` | `48` | Escalado |
| `/` | División | `48 / 6` | `8.0` | Proporciones (siempre float) |
| `%` | Módulo | `48 % 5` | `3` | Restos |
| `**` | Potenciación | `2 ** 10` | `1024` | Potencias |

```python
# Estimación rápida de horas restantes para VR-07
consumo_mw = 145
reserva_mwh = 12.65
# Horas restantes aproximadas (horas enteras para un registro conciso)
horas_restantes = reserva_mwh * 1000 / consumo_mw
print(horas_restantes)
```

## Salida

```text
87.24137931034483
```

La división produce un float incluso cuando ambos valores parecen enteros. Si un registro espera un recuento entero, eso es una señal para convertir intencionalmente, en lugar de truncar por accidente. Las matemáticas son útiles, pero en telemetría también es fácil malinterpretar la precisión si no se conocen los tipos con los que se trabaja.

> [!WARNING]
> `input()` siempre devuelve una cadena. Si un script pide un umbral numérico desde la consola, es necesario convertirlo con `int()` o `float()` antes de hacer comparaciones o cálculos aritméticos. Olvidarlo es uno de los errores más comunes al arrancar.

### Tarea 1: Instantánea de Baliza

Escribe un script corto que imprima una instantánea limpia al arrancar para la baliza `VR-12`: batería 64%, temperatura del núcleo 19.7 °C, enlace a la malla falso, y una línea que estime las horas restantes si la reserva es 7.8 mWh con un consumo de 145 mW. Haz los cálculos en línea e imprime cuatro líneas en total.
