<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 07 - Beacon Class

**Spanish version:** [07 - Clase Baliza](./07%20-%20Clase%20Baliza.md)

![Status Badge](https://img.shields.io/badge/Topic-OOP-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 3 — Automation
**Topic:** Classes, Objects, __init__, Instance Methods
**Tags:** `#python` `#telemetry` `#oop` `#classes` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Blueprints for Stations

When managing a dozen beacons with the same fields and routines, repeating dicts gets clumsy. A **class** is a blueprint; an **object** (instance) is a concrete station built from it. Use PascalCase for class names.

```python
class Beacon:
    pass

vr07 = Beacon()
```

## Initializing State

The `__init__()` method runs when creating an instance. `self` refers to the current instance. Assigning `self.attr = value` attaches fields to that object.

```python
class Beacon:
    def __init__(self, station_id, battery_pct, mesh_link):
        self.station_id = station_id
        self.battery_pct = battery_pct
        self.mesh_link = mesh_link

vr07 = Beacon("VR-07", 64, True)
print(vr07.station_id)
print(vr07.battery_pct)
```

## Output

```text
VR-07
64
```

## Instance Methods

**Instance methods** are functions inside a class that act on `self`. They can read and update attributes.

```python
class Beacon:
    def __init__(self, station_id, battery_pct, mesh_link):
        self.station_id = station_id
        self.battery_pct = battery_pct
        self.mesh_link = mesh_link

    def status(self):
        return f"{self.station_id} :: BATT {self.battery_pct}% LINK {self.mesh_link}"

    def drain(self, amt):
        self.battery_pct -= amt
        if self.battery_pct < 0:
            self.battery_pct = 0

vr07 = Beacon("VR-07", 64, True)
print(vr07.status())
vr07.drain(15)
print(vr07.status())
```

## Output

```text
VR-07 :: BATT 64% LINK True
VR-07 :: BATT 49% LINK True
```

Methods can enforce simple rules (clamping values) without exposing that logic everywhere else. That keeps behavior consistent across the array.

> [!NOTE]
> `self` is required as the first parameter in instance methods, but it's passed automatically when called as `instance.method()`.

## Multiple Instances

Each instance has its own attribute values. Changing one doesn't affect others.

```python
vr07 = Beacon("VR-07", 64, True)
vr12 = Beacon("VR-12", 26, False)
vr07.drain(10)
print(vr12.battery_pct)  # unaffected
```

## Why OOP Here

For a fixed set of fields and a small set of routines (status, drain, check thresholds), classes cut repetition and make intent clearer. Not every script needs OOP, but for modeling stations it fits.

> [!TIP]
> Start simple: put data in `__init__`, put behavior in methods. Avoid putting everything into one method.

### Task 7: Beacon Class

Create class `Beacon` with `__init__(self, station_id, battery_pct)`. Add method `low_batt(self)` that returns `True` if battery_pct < 30 else `False`. Create `b = Beacon("VR-09", 26)` and print `b.low_batt()`.
