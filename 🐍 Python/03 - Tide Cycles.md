<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 03 - Tide Cycles

**Spanish version:** [03 - Ciclos de Marea](./03%20-%20Ciclos%20de%20Marea.md)

![Status Badge](https://img.shields.io/badge/Topic-Loops-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 1 — Telemetry Foundations
**Topic:** while Loops, for Loops, range(), Iteration Control
**Tags:** `#python` `#telemetry` `#loops` `#iteration` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Why Repetition Fails

Some telemetry tasks are finite and known in advance: poll four sensor channels, print a header row for twelve readings, step through a fixed list of beacons. Others are not — a link retry should keep trying until it succeeds, or until attempts run out. A block written twice is a copy-paste risk; a loop is a rule that can run zero, some, or many times without duplicating code. Each pass through the block is an **iteration**.

## `while`: Check Before Running

A `while` loop tests its condition at the start of every iteration. If it's false initially, the body never executes. That fits retry logic well: check connectivity, and only retry while it's down.

```python
retries = 0
max_retries = 3
linked = False
while not linked and retries < max_retries:
    retries += 1
    print(f"VR-07 :: LINK_RETRY {retries}")
    if retries == 3:
        linked = True  # simulated success on third attempt
print(f"VR-07 :: LINK_STATE {linked}")
```

## Output

```text
VR-07 :: LINK_RETRY 1
VR-07 :: LINK_RETRY 2
VR-07 :: LINK_RETRY 3
VR-07 :: LINK_STATE True
```

A sentinel is a value that means "stop" rather than data. When reading until a sentinel, the path that produces it must exist somewhere in the loop — either from simulated input or from a `break`. If nothing can change the condition, the loop never ends.

> [!CAUTION]
> Every `while` loop needs an exit. Update the variable that feeds the condition inside the body, or use `break` with a clear justification. An infinite loop is cheap to write and expensive to debug at a remote beacon.

## `for`: Count Over a Known Set

When the count or sequence is known, `for` with `range()` is cleaner. `range(n)` produces `0` through `n-1`; `range(start, stop)` goes up to but not including `stop`; `range(start, stop, step)` changes the increment.

```python
# Log a short burst of channel readings
for ch in range(1, 5):
    print(f"VR-07 :: CH{ch}_READ")
```

## Output

```text
VR-07 :: CH1_READ
VR-07 :: CH2_READ
VR-07 :: CH3_READ
VR-07 :: CH4_READ
```

String interpolation with f-strings keeps logs compact and legible. The placeholder `{ch}` is evaluated at runtime, which is ideal for station ids, channel numbers, or timestamps in terse lines.

## Nested Decisions in a Loop

Real telemetry often combines loops with conditions. A download batch might pass each file through a quick validation: skip a known corrupt file, warn on a large one, otherwise log it as queued. Putting `if/elif/else` inside a loop is normal, but nesting too deep gets hard to follow — prefer early checks where possible.

```python
batch = ["beacon_07_001.log", "beacon_07_002.tmp", "beacon_07_003.log"]
for fname in batch:
    if fname.endswith(".tmp"):
        print(f"VR-07 :: SKIP {fname} (temp)")
        continue
    if fname.endswith(".log"):
        print(f"VR-07 :: QUEUE {fname}")
    else:
        print(f"VR-07 :: WARN {fname} (unknown)")
```

## Output

```text
VR-07 :: SKIP beacon_07_002.tmp (temp)
VR-07 :: QUEUE beacon_07_001.log
VR-07 :: QUEUE beacon_07_003.log
```

`continue` jumps to the next iteration; `break` exits the loop entirely. Both are useful, but they make control flow less obvious. A well-formed condition is usually easier to reason about than a `break` buried deep in logic.

> [!TIP]
> If a loop needs its counter after it ends, declare it before the `while` header. If it's only needed inside a `for` loop, keep it scoped to the loop.

### Task 3: Tide Poll

Write a script that polls channels 1 through 6 with `range()`. For even channels print `VR-12 :: CHx STABLE`, for odd channels print `VR-12 :: CHx NOISY`. Use f-strings and print one line per channel in order.
