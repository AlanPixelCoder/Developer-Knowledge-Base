<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 04 - Relay Drift

**Spanish version:** [04 - Desviación de Relé](./04%20-%20Desviaci%C3%B3n%20de%20Rel%C3%A9.md)

![Status Badge](https://img.shields.io/badge/Topic-Lists-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 2 — Data & State
**Topic:** Lists, Indexing, Slicing, Built-ins, Methods, Iteration
**Tags:** `#python` `#telemetry` `#lists` `#data-structures` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Queues of Readings

A single beacon dump isn't much, but a batch from five beacons across the tide window tells a story. Lists hold ordered collections in one variable, written with square brackets `[]` and comma-separated values. They can mix types, allow repeats, and grow/shrink without fixed sizes.

```python
# Recent readings from VR-07 (rssi in dBm)
rssi = [-62, -65, -71, -68, -64]
stations = ["VR-07", "VR-09", "VR-12", "VR-14"]
```

## Indexing and Slicing

Items are zero-based. Negative indices count from the end: `-1` is the last element. Slicing `start:end` includes start and excludes end. It never mutates the original list — it returns a new view.

```python
rssi = [-62, -65, -71, -68, -64]
print(rssi[0])     # -62
print(rssi[-1])    # -64
print(rssi[1:4])   # [-65, -71, -68]
print(rssi[:3])    # [-62, -65, -71]
print(rssi[3:])    # [-68, -64]
```

## Output

```text
-62
-64
[-65, -71, -68]
[-62, -65, -71]
[-68, -64]
```

Accessing out of range raises `IndexError`. If an index comes from a computed position, validate or guard it rather than letting the script crash on a partial batch.

> [!NOTE]
> Slicing returns a list even if it's empty or a single element. That consistency is often safer than trying to special-case a scalar.

## Quick Stats with Built-ins

For a quick audit, Python's built-ins cover common needs: `len()`, `max()`, `min()`, `sum()`. Combined, they can flag drift without writing loops.

```python
rssi = [-62, -65, -71, -68, -64]
print(len(rssi))
print(min(rssi))  # weakest signal
print(max(rssi))  # strongest signal
print(sum(rssi))
```

## Output

```text
5
-71
-62
-330
```

For RSSI, "stronger" means closer to zero. `min()` returning `-71` correctly identifies the weakest link in that batch — the built-ins do exactly what their names say, but interpretation still depends on the metric.

## Shaping the Queue

List methods modify the list in place. Knowing which ones mutate is important: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()` change the original; `copy()` makes a shallow copy.

| Method | Effect |
| :--- | :--- |
| `.append(x)` | Add to end |
| `.insert(i,x)` | Insert at index |
| `.extend(lst)` | Append all from another list |
| `.remove(x)` | Remove first match |
| `.pop([i])` | Remove and return at index (or end) |
| `.clear()` | Empty list |
| `.index(x)` | Find first index |
| `.count(x)` | Count occurrences |
| `.sort()` | Sort in place |
| `.reverse()` | Reverse in place |
| `.copy()` | Shallow copy |

```python
pending = ["VR-07", "VR-09"]
pending.append("VR-12")
pending.insert(1, "VR-14")
pending.remove("VR-09")
print(pending)
```

## Output

```text
['VR-07', 'VR-14', 'VR-12']
```

## Walking the Batch

To process every item, iterate directly with `for`. To also need indices (e.g., to log "reading 3 of 5"), use `range(len(list))`.

```python
rssi = [-62, -65, -71, -68, -64]
for val in rssi:
    print(f"RSSI {val} dBm")
```

## Output

```text
RSSI -62 dBm
RSSI -65 dBm
RSSI -71 dBm
RSSI -68 dBm
RSSI -64 dBm
```

> [!WARNING]
> `remove()` deletes only the first occurrence. If duplicates are possible (e.g., duplicate station ids in a messy batch), check with `count()` or filter explicitly.

### Task 4: Drift Queue

Create a list `beacons = ["VR-07", "VR-09", "VR-12"]`. Append `VR-14`, insert `VR-05` at index 0, remove `VR-09`, then print the list and the length using `len()`.
