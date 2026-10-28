<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 06 - Relay Routines

**Spanish version:** [06 - Rutinas de Relé](./06%20-%20Rutinas%20de%20Rel%C3%A9.md)

![Status Badge](https://img.shields.io/badge/Topic-Functions-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 3 — Automation
**Topic:** Functions, Parameters, Arguments, Return, Scope, Lambda
**Tags:** `#python` `#telemetry` `#functions` `#automation` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Don't Repeat the Check

After the third time writing the same threshold check, copy-paste becomes a liability. A **function** is a reusable block that does one job. Define with `def`, call by name with `()`. Keeping logic in functions means a fix applies everywhere it's called.

```python
def boot_report():
    print("VERDANT-RELAY :: ROUTINE CHECK START")

boot_report()
boot_report()
```

## Output

```text
VERDANT-RELAY :: ROUTINE CHECK START
VERDANT-RELAY :: ROUTINE CHECK START
```

## Parameters Make It Flexible

A **parameter** is a placeholder in the definition; an **argument** is the value passed at call time. Parameters turn a fixed routine into a generic one.

```python
def station_check(station_id, battery_pct):
    print(f"{station_id} :: BATT {battery_pct}%")

station_check("VR-07", 64)
station_check("VR-12", 26)
```

## Output

```text
VR-07 :: BATT 64%
VR-12 :: BATT 26%
```

## Return Values, Not Just Prints

`print()` shows output to the console, but doesn't give data back. `return` sends a value to the caller so it can be stored, compared, or passed on. If there's no return, Python gives `None`.

```python
def hours_remaining(reserve_mwh, drain_mw):
    if drain_mw <= 0:
        return None
    return reserve_mwh * 1000 / drain_mw

h = hours_remaining(7.8, 145)
print(round(h, 1))
```

## Output

```text
53.8
```

Splitting work into small functions that return values is easier to test and reason about than one big script that only prints.

> [!NOTE]
> Returning `None` for invalid input is a clean way to signal "can't compute" without crashing. The caller can check for it.

## Scope: Local vs Global

**Local** variables live inside a function and disappear when it returns. **Global** variables live at module level and are readable from anywhere, but assigning to a global inside a function requires `global` (use sparingly). Prefer passing values as parameters and returning results.

```python
min_batt = 30  # global

def can_sync(battery_pct):
    return battery_pct >= min_batt  # reads global

print(can_sync(26))
print(can_sync(52))
```

## Output

```text
False
True
```

## Lambda for Quick Transforms

A **lambda** is an anonymous one-line function: `lambda args: expression`. It's handy for short passes like `map()` or `filter()`, but if logic grows past a simple expression, a regular `def` is clearer.

```python
rssi = [-62, -65, -71, -68, -64]
# Flag weak links (< -68)
weak = list(filter(lambda x: x < -68, rssi))
print(weak)
```

## Output

```text
[-71]
```

> [!TIP]
> Don't reach for lambda by default. Use it when you need a tiny function for a single use in a higher-order call.

### Task 6: Relay Routines

Write `def batt_status(pct):` that returns `"LOW"` if pct < 30, `"OK"` if pct >= 30. Call it with 26 and print the result. Also write `def to_dbm(mv):` that returns mv / 1000.0 and print `to_dbm(65000)`.
