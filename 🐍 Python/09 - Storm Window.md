<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 09 - Storm Window

**Spanish version:** [09 - Ventana de Tormenta](./09%20-%20Ventana%20de%20Tormenta.md)

![Status Badge](https://img.shields.io/badge/Topic-Capstone-orange?style=for-the-badge)

**Course:** Python
**Chapter:** 4 — Integration
**Topic:** Capstone: Telemetry Console
**Tags:** `#python` `#telemetry` `#capstone` `#project` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Pulling It Together

A storm is closing in on the Verdant Relay array. The console needs to report which beacons are safe to sync now, which need to defer, and a short batch summary. This capstone uses variables, if/elif, loops, lists, dictionaries, functions, and a class — all from the previous lessons.

## The Console

```python
class Beacon:
    def __init__(self, station_id, battery_pct, mesh_link):
        self.station_id = station_id
        self.battery_pct = battery_pct
        self.mesh_link = mesh_link

    def can_sync(self):
        return self.mesh_link and self.battery_pct >= 40

beacons = [
    Beacon("VR-07", 64, True),
    Beacon("VR-09", 26, True),
    Beacon("VR-12", 52, False),
    Beacon("VR-14", 41, True),
]

for b in beacons:
    if b.can_sync():
        print(f"{b.station_id} :: SYNC_OK")
    elif b.battery_pct < 30:
        print(f"{b.station_id} :: DEFER_LOW_BATT")
    elif not b.mesh_link:
        print(f"{b.station_id} :: DEFER_NO_LINK")
    else:
        print(f"{b.station_id} :: DEFER_OTHER")
```

## Output

```text
VR-07 :: SYNC_OK
VR-09 :: DEFER_LOW_BATT
VR-12 :: DEFER_NO_LINK
VR-14 :: SYNC_OK
```

## Why This Shape

The logic reads top-down: first check the full gate `can_sync()`, else branch by the most specific blocker. Keeping the decision in the class keeps it consistent; the loop keeps the report short. No external modules needed for this version, but the structure would easily plug in `random` for simulated readings or `datetime` for a timestamp.

> [!IMPORTANT]
> Order of checks matters. If you checked battery before `can_sync()`, a beacon with low battery and no link could be classified differently. Put the combined gate first when it's the desired "green" condition.

## Extending the Idea

A real console might collect faults into a set (deduplicate), store snapshots in dicts, or use functions to format lines. The key is composing small pieces: class for state/behavior, loop for batch, if for branching.

> [!TIP]
> Before writing, trace by hand for two or three items. If the logic matches on paper, it's much easier to debug in code.

### Task 9: Storm Window

Create `beacons = [Beacon("VR-05", 35, True), Beacon("VR-11", 28, True)]` (using the same class pattern). For each, print `SYNC_OK` if `battery_pct >= 40 and mesh_link`, else `HOLD`. Do it with a loop.
