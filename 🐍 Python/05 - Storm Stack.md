<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 05 - Storm Stack

**Spanish version:** [05 - Pila de Tormenta](./05%20-%20Pila%20de%20Tormenta.md)

![Status Badge](https://img.shields.io/badge/Topic-Data%20Structures-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 2 — Data & State
**Topic:** Nested Lists, Matrices, Dictionaries, Sets
**Tags:** `#python` `#telemetry` `#dictionaries` `#sets` `#matrices` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Stacking by Zones

When a coastal storm hits, readings come in by zone: each zone has a list of stations and each station has a list of channel readings. A **nested list** puts lists inside a list. With equal-length rows, it becomes a 2D structure (a matrix) easy to index by `[row][col]`.

```python
# Zone grid: rows = zones, cols = stations
mesh_status = [
    ["OK", "OK", "LOW"],
    ["OK", "DRIFT", "OK"],
    ["DOWN", "OK", "WARN"]
]
# Zone 2, station 0
print(mesh_status[2][0])  # DOWN
```

## Digging Into Nested Data

Access goes from outer to inner. If data is irregular, always check length before indexing to avoid `IndexError`.

```python
log_batch = [
    ["VR-07", [-62, -65, -71]],
    ["VR-09", [-58, -60]],
    ["VR-12", [-70, -69, -72, -68]]
]
# Last rssi for VR-12
print(log_batch[2][1][-1])  # -68
```

## Dictionaries for Field Records

Lists are great by position, but telemetry records read better by name. A **dictionary** maps unique keys to values as `key: value` pairs. Access with brackets by key, or add/update on assignment.

```python
beacon = {
    "id": "VR-07",
    "battery_pct": 64,
    "core_temp_c": 19.7,
    "mesh_link": True,
    "zones": ["north", "jetty"]
}
print(beacon["id"])
print(beacon["battery_pct"])
beacon["rssi"] = -66
print(beacon)
```

## Output

```text
VR-07
64
{'id': 'VR-07', 'battery_pct': 64, 'core_temp_c': 19.7, 'mesh_link': True, 'zones': ['north', 'jetty'], 'rssi': -66}
```

Keys must be unique; values can be any type. Useful methods: `.keys()`, `.values()`, `.items()`. Iterating over `.items()` gives `(key, value)` pairs.

```python
for k, v in beacon.items():
    print(f"{k}: v")
```

> [!TIP]
> If you're unsure a key exists, `beacon.get("rssi", "NA")` returns a default without raising `KeyError`.

## Sets for Unique Faults

When collecting fault codes across a batch, duplicates creep in. A **set** holds unordered unique items. Use `set()` for empty sets (not `{}` which creates a dict). Sets support `union()`, `intersection()`, `difference()` for quick comparisons.

```python
faults_a = {"LOW_BATT", "DRIFT", "LOW_BATT"}
faults_b = {"DRIFT", "OVERHEAT"}
print(set(faults_a))  # {'LOW_BATT', 'DRIFT'}
print(faults_a.union(faults_b))
print(faults_a.intersection(faults_b))
print(faults_a.difference(faults_b))
```

## Output

```text
{'LOW_BATT', 'DRIFT'}
{'LOW_BATT', 'DRIFT', 'OVERHEAT'}
{'DRIFT'}
{'LOW_BATT'}
```

Sets are not indexable by position — order isn't guaranteed. They're best for membership checks and deduplication, not for ordered queues.

> [!CAUTION]
> `{}` is a dictionary. Use `set()` to create an empty set.

## Choosing the Right Structure

| Structure | Ordered | Duplicates | Access | Best for |
| :--- | :--- | :--- | :--- | :--- |
| List | Yes | Yes | By index | Queues, batches, ordered logs |
| Dictionary | Yes (insertion order) | Keys unique | By key | Field records, config snapshots |
| Set | No | No | By membership | Unique faults, comparisons |

### Task 5: Storm Stack

Build a dict `vr12 = {"id": "VR-12", "battery_pct": 38, "mesh_link": False}`. Add key `faults` with list `["LOW_BATT"]`. Create set `seen = {"LOW_BATT", "DRIFT", "LOW_BATT"}` and print `len(seen)` and `vr12["battery_pct"]`.
