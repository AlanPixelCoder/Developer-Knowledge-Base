<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 00b - Tarjeta de Campo de Verdant Relay

**Versión original en inglés:** [00b - Verdant Relay Field Card](./00b%20-%20Verdant%20Relay%20Field%20Card.md)

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status Badge](https://img.shields.io/badge/Reference-Cheatsheet-brightgreen?style=for-the-badge)

**Curso:** Python
**Capítulo:** Referencia
**Tema:** Referencia rápida de sintaxis — Verdant Relay
**Etiquetas:** `#python` `#chuleta` `#telemetria` `#referencia` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Arranque y E/S

```python
print("VERDANT-RELAY :: ARRANQUE")
id_estacion = input("ESTACION: ")
bateria_porcentaje = int(input("BATERIA%: "))
```

## Tipos

```python
sid = "VR-07"           # str
bateria = 87            # int
temperatura = 16.4      # float
enlace = True           # bool
```

## Operadores

```python
# Aritméticos
horas = (reserva_mwh * 1000) / consumo_mw
resto = 48 % 5
potencia = 2 ** 10

# Relacionales
bateria >= 40
enlace == True
temperatura != 25.0

# Lógicos
enlace and bateria >= 40
baja or sin_enlace
not enlace_malla
```

## Control de Flujo

```python
if bateria < 30:
    print("BATERIA_BAJA")
elif bateria < 40:
    print("AVISO_BATERIA")
else:
    print("BATERIA_OK")
```

## Bucles

```python
# while
reintentos = 0
while reintentos < 3:
    reintentos += 1

# for / range
for ch in range(1, 5):
    print(ch)
```

## Listas

```python
rssi = [-62, -65, -71]
rssi.append(-64)
rssi[0]      # -62
rssi[1:3]    # [-65, -71]
len(rssi)
```

## Diccionarios y Conjuntos

```python
baliza = {"id": "VR-07", "bateria": 64}
baliza["enlace"] = True
fallos = {"BATERIA_BAJA", "DESVIO"}
fallos.add("AVISO_TEMPERATURA")
```

## Funciones y Clases

```python
def estado_bateria(pct):
    return "BAJO" if pct < 30 else "OK"

class Baliza:
    def __init__(self, sid, bateria):
        self.sid = sid
        self.bateria = bateria
    def bateria_baja(self):
        return self.bateria < 30
```

## Importaciones

```python
import math
from random import randint
from relay_utils import estado_bateria
```
