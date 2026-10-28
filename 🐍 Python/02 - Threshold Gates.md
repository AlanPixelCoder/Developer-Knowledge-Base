<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 02 - Threshold Gates

**Spanish version:** [02 - Compuertas de Umbral](./02%20-%20Compuertas%20de%20Umbral.md)

![Status Badge](https://img.shields.io/badge/Topic-Control%20Flow-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 1 — Telemetry Foundations
**Topic:** Errors, Conditional Logic, Relational & Logical Operators
**Tags:** `#python` `#telemetry` `#conditionals` `#logic` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Reading a Faulty Report

Not every reading from a storm-soaked beacon is valid. A loose connector can produce a string where an int is expected, or a script might reference a field that was never set during a partial boot. Before branching on thresholds, it's worth knowing the common failure modes so they don't get misread as "bad weather" when they're just bad types or missing variables.

- **`SyntaxError`** — The line doesn't follow Python grammar (missing colon, unmatched quotes). The parser fails before anything runs.
- **`NameError`** — A name like `mesh_rssi` is used before assignment. Often a typo or an early return in a partial script.
- **`TypeError`** — Operations between incompatible types (e.g. concatenating `str` and `int`). Casting resolves it when the values are actually meant to combine.

```python
# A common mistake when building a log line
station_id = "VR-07"
battery_pct = 87
# The next line would raise TypeError: can only concatenate str (not "int") to str
# print("Battery: " + battery_pct + "%")
# Fix: cast to str
print("Battery: " + str(battery_pct) + "%")
```

## Output

```text
Battery: 87%
```

## When to Raise the Alarm

With valid values in hand, the job shifts to decisions. Verdant Relay treats certain readings as gates: if voltage is below a minimum, the beacon must report LOW_BATT and skip a high-draw task; if temperature crosses a hard limit, it must flag OVERHEAT regardless of charge. `if`, `elif`, and `else` let a script take different paths based on boolean results.

```python
battery_pct = 23
if battery_pct < 30:
    print("VR-07 :: LOW_BATT — defer high-draw sync")
else:
    print("VR-07 :: BATT_OK — full sync permitted")
```

## Output

```text
VR-07 :: LOW_BATT — defer high-draw sync
```

Relational operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) produce `True`/`False`. When there are more than two cases, chain them with `elif`. Order matters: the first condition that evaluates true wins, and the rest are skipped for that pass.

```python
core_temp_c = 41.7
if core_temp_c >= 45.0:
    print("VR-07 :: CRITICAL_OVERHEAT")
elif core_temp_c >= 38.0:
    print("VR-07 :: WARN_OVERHEAT")
elif core_temp_c >= 35.0:
    print("VR-07 :: ELEVATED_TEMP")
else:
    print("VR-07 :: TEMP_OK")
```

## Output

```text
VR-07 :: WARN_OVERHEAT
```

> [!IMPORTANT]
> Threshold order is an algorithm, not style. Check the tightest/most severe condition first. If `>= 38.0` came before `>= 45.0`, a truly critical reading would be reported as just a warning — a subtle but dangerous swap in telemetry.

## Combining Conditions

Sometimes a gate depends on two things at once. A beacon might only attempt a mesh relay if it's linked *and* has enough charge. Or it might fall back to a local cache if it's either low on charge *or* disconnected. Logical operators combine boolean expressions: `and` requires both, `or` requires at least one, `not` inverts.

| A | B | A and B | A or B |
| :--- | :--- | :--- | :--- |
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

```python
mesh_link = True
battery_pct = 52
if mesh_link and battery_pct >= 40:
    print("VR-07 :: RELAY_ATTEMPT")
else:
    print("VR-07 :: LOCAL_CACHE")
```

## Output

```text
VR-07 :: RELAY_ATTEMPT
```

When conditions grow complex, it's often clearer to compute a boolean into a variable with a meaningful name (e.g. `can_relay = mesh_link and battery_pct >= 40`) than to nest deeply. Readability beats cleverness when debugging in bad weather.

> [!CAUTION]
> Don't confuse assignment `=` with equality `==`. `if battery_pct = 30:` is a syntax error in a condition; `if battery_pct == 30:` compares values. That typo is easy to miss at a glance.

### Task 2: Threshold Audit

Write logic for beacon `VR-09` with battery 26%, mesh_link True, core_temp_c 39.2. Print exactly one status line: CRITICAL if battery < 20, else LOW if battery < 30, else OK. Separately print `RELAY` if mesh_link is True and battery >= 25, else `CACHE`. Keep the branches in that order and don't add extra text.
