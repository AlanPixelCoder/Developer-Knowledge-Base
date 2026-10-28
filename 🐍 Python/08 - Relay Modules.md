<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 08 - Relay Modules

**Spanish version:** [08 - Módulos de Relé](./08%20-%20M%C3%B3dulos%20de%20Rel%C3%A9.md)

![Status Badge](https://img.shields.io/badge/Topic-Modules-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 4 — Integration
**Topic:** Modules, import, from/import, Standard Library, Custom Modules
**Tags:** `#python` `#telemetry` `#modules` `#imports` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Sharing Routines

As routines grow, dumping everything into one file becomes unwieldy. A **module** is a `.py` file with functions/variables you can import. Python's standard library has many modules (`math`, `random`, `datetime`). Splitting by concern (checks, formatting, time) keeps scripts short and testable.

## Import Styles

```python
import math
from math import pi
from math import sqrt as s
```

- `import math` uses `math.pi`
- `from math import pi` uses `pi` directly
- `as` gives a short alias

```python
import math
r = 12.4
print(4 * math.pi * r * r)  # rough disk area
```

## Output

```text
1932.203931710084
```

## Using `random` for Simulations

For testing without live hardware, `random` helps simulate readings.

```python
import random
rssi = random.randint(-80, -50)
print(rssi)
```

`randint(a,b)` is inclusive. `random.choice(list)` picks one; `random.choices(list, k=n)` can repeat.

## Custom Modules

Any `.py` in the same directory can be imported. Put shared helpers in `relay_utils.py`, then `import relay_utils`.

```python
# relay_utils.py
def batt_status(pct):
    if pct < 30:
        return "LOW"
    return "OK"
```

```python
# check.py
import relay_utils
print(relay_utils.batt_status(26))
```

## Output

```text
LOW
```

You can also do `from relay_utils import batt_status` to call directly.

> [!NOTE]
> When importing your own module, changes take effect after restart in a simple script run; in some environments you may need to reload. For these lessons, run once per change.

## `datetime` for Windows

Storm windows need timestamps. `datetime` gives date/time objects.

```python
import datetime
now = datetime.datetime.now()
print(now)
```

Output varies, but the object is usable. For a log line, formatting with f-strings works if you convert to string.

> [!TIP]
> Keep imports at the top. Group standard library imports first, then local modules.

### Task 8: Relay Modules

Create a mental check: import `math` and print `math.ceil(12.2)`. Write a note of what `from random import randint` does (conceptually). No need to write files except reasoning — just show the two import forms in your answer conceptually by writing short code lines: import `math` and use `math.ceil`, and `from random import randint` and call `randint(1,6)`.
