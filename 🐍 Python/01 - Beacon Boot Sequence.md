<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 01 - Beacon Boot Sequence

**Spanish version:** [01 - Arranque de Balizas](./01%20-%20Arranque%20de%20Balizas.md)

![Python Badge](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)![Status Badge](https://img.shields.io/badge/Difficulty-Beginner-brightgreen?style=for-the-badge)

**Course:** Python
**Chapter:** 1 — Telemetry Foundations
**Topic:** Environment, Output, Variables, Data Types & Arithmetic
**Tags:** `#python` `#telemetry` `#beacons` `#basics` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Powering the Coastal Array

Verdant Relay keeps a handful of solar-charged beacons alive along a storm-battered coastline. When a technician rolls in for a dawn check, the first job is waking the station console and pulling a clean reading. Before any automation runs, a script has to announce itself, log key values, and prove the link is up. 

In Python, that starts with a line to the terminal. The `print()` function writes to stdout with no hidden formatting — exactly what you want for a terse telemetry line that another script might parse later.

```python
# Beacon console boot message
print("VERDANT-RELAY :: BOOT SEQUENCE INITIATED")
```

## Output

```text
VERDANT-RELAY :: BOOT SEQUENCE INITIATED
```

Execution is strictly top-to-bottom, so order matters. A boot script that logs voltage before reporting uptime is correct; reversing those lines tells a slightly different story. That ordering discipline is the first habit worth keeping when chasing a flaky link in the middle of a squall.

> [!NOTE]
> `print()` adds a newline by default. For beacon logs that feed into a strict parser, an extra blank line or a missing one changes the record. Always check spacing when stitching logs together.

## Storing Readings in Variables

Every beacon reports a handful of fixed fields at boot: its station id, charge state, temperature, and whether it's linked to the relay mesh. Rather than retyping values, store them in **variables** — named containers held in memory. Assignment uses `=` and the name on the left points to the value on the right.

```python
# Boot-time snapshot for beacon VR-07
station_id = "VR-07"
battery_pct = 87
core_temp_c = 16.4
mesh_link = True

print(station_id)
print(battery_pct)
print(core_temp_c)
print(mesh_link)
```

## Output

```text
VR-07
87
16.4
True
```

Python infers types at runtime: `"VR-07"` is `str`, `87` is `int`, `16.4` is `float`, `True` is `bool`. Those types are not decoration — later operations will behave differently depending on them. Trying to add a string and an int is a type mismatch, not a clever shortcut.

> [!TIP]
> Pick variable names that read like the field they represent. `battery_pct` says more than `b`, especially when reading logs at 03:00 in a drizzle.

## Arithmetic for Quick Sanity Checks

A technician often needs rough math on the spot: remaining capacity, estimated runtime, or a voltage-derived check. Python's arithmetic operators cover the basics without pulling in extra modules.

| Operator | Name | Example | Result | Use |
| :--- | :--- | :--- | :--- | :--- |
| `+` | Addition | `87 + 3` | `90` | Totals |
| `-` | Subtraction | `87 - 12` | `75` | Drawdown |
| `*` | Multiplication | `4 * 12` | `48` | Scaling |
| `/` | Division | `48 / 6` | `8.0` | Ratios (always float) |
| `%` | Modulo | `48 % 5` | `3` | Remainders |
| `**` | Exponentiation | `2 ** 10` | `1024` | Powers |

```python
# Quick runtime estimate for VR-07
drain_mw = 145
reserve_mwh = 12.65
# Rough hours remaining (integer hours for a terse log line)
hours_remain = reserve_mwh * 1000 / drain_mw
print(hours_remain)
```

## Output

```text
87.24137931034483
```

The division produces a float even when both values look whole. If a log expects a whole count, that's a signal to cast intentionally rather than truncating by accident. Math is useful, but in telemetry it's just as easy to misread precision if you don't know the types you're working with.

> [!WARNING]
> `input()` always returns a string. If a script asks for a threshold number from a console prompt, casting with `int()` or `float()` is required before doing comparisons or arithmetic. Forgetting that is one of the most common boot-time bugs.

### Task 1: Beacon Snapshot

Write a short script that prints a clean boot snapshot for beacon `VR-12`: battery 64%, core temp 19.7°C, mesh link false, and a line estimating hours remaining if reserve is 7.8 mWh at 145 mW drain. Keep the math inline and print four lines total.
