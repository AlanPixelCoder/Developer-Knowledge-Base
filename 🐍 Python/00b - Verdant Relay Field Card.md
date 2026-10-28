<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 00b - Verdant Relay Field Card

**Spanish version:** [00b - Tarjeta de Campo de Verdant Relay](./00b%20-%20Tarjeta%20de%20Campo%20de%20Verdant%20Relay.md)

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status Badge](https://img.shields.io/badge/Reference-Cheatsheet-brightgreen?style=for-the-badge)

**Course:** Python
**Chapter:** Reference
**Topic:** Syntax Quick Reference — Verdant Relay
**Tags:** `#python` `#cheatsheet` `#telemetry` `#reference` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Boot & I/O

```python
print("VERDANT-RELAY :: BOOT")
station_id = input("STATION: ")
battery_pct = int(input("BATT%: "))
```

## Types

```python
sid = "VR-07"      # str
batt = 87          # int
temp = 16.4        # float
link = True        # bool
```

## Operators

```python
# Arithmetic
hours = (reserve_mwh * 1000) / drain_mw
rem = 48 % 5
powr = 2 ** 10

# Relational
batt >= 40
link == True
temp != 25.0

# Logical
link and batt >= 40
low or no_link
not mesh_link
```

## Control Flow

```python
if batt < 30:
    print("LOW_BATT")
elif batt < 40:
    print("WARN_BATT")
else:
    print("BATT_OK")
```

## Loops

```python
# while
retries = 0
while retries < 3:
    retries += 1

# for / range
for ch in range(1, 5):
    print(ch)
```

## Lists

```python
rssi = [-62, -65, -71]
rssi.append(-64)
rssi[0]      # -62
rssi[1:3]    # [-65, -71]
len(rssi)
```

## Dictionaries & Sets

```python
beacon = {"id": "VR-07", "batt": 64}
beacon["link"] = True
faults = {"LOW_BATT", "DRIFT"}
faults.add("WARN_TEMP")
```

## Functions & Classes

```python
def batt_status(pct):
    return "LOW" if pct < 30 else "OK"

class Beacon:
    def __init__(self, sid, batt):
        self.sid = sid
        self.batt = batt
    def low_batt(self):
        return self.batt < 30
```

## Imports

```python
import math
from random import randint
from relay_utils import batt_status
```
