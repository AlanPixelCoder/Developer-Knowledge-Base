
# 01. The Wayfarer Charter

**Spanish version:** [01 - La Carta del Caminante](./01%20-%20La%20Carta%20del%20Caminante.md)

**Course:** Data Structures & Algorithms
**Chapter:** 1 — The Survey
**Topic:** Supply lines, structure vs procedure, cost as the map grows
**Tags:** `#dsa` `#data-structures` `#algorithms` `#fundamentals`

The Wayfarer Survey charts fractured coastlines where tide windows are hours long. With only a handful of skiffs, hauling crates blind is not heroic — it's wasteful. The charter forces a habit: for every supply run, name two things before leaving the quay. First, *how* to hold cargo (a **data structure**). Second, *in which order* to act on it (an **algorithm**). Neither exists in isolation; changing one often forces a rethink of the other.

## Holding cargo without guessing

A data structure is not a container for the sake of neatness. It's a choice that makes a specific operation cheap and another one awkward on purpose. The Survey keeps manifests as **lists** when order of loading matters and they expect to walk the jetty from bow to stern. A list keeps items in sequence and lets the wayfarer reach any berth by index, but it offers no built-in shortcut if the crate number is unknown.

```python
# A manifest held in the order crates were winched onto the jetty
jetty_manifest = ["Crate-17", "Crate-05", "Crate-42", "Crate-09"]
print("First to unload:", jetty_manifest[0])
jetty_manifest.append("Crate-88")
print("Count at quay:", len(jetty_manifest))
print("All crates:", jetty_manifest)
```

## Output

```text
First to unload: Crate-17
Count at quay: 5
All crates: ['Crate-17', 'Crate-05', 'Crate-42', 'Crate-09', 'Crate-88']
```

The list is honest about its shape: to know what's at position two, you don't need to read the whole pile — you know the index. But if the question is "is Crate-42 here?" and no one wrote down its berth, the list won't point to it. The structure is doing its job for *known positions*, and failing to shortcut the *unknown position* case.

## A plan with a stopping condition

An algorithm is a finite plan. For a missing crate with no index, the wayfarer can fall back to a **linear scan**: look at berth 0, if not a match look at berth 1, and so on until a match is found or there are no more berths. This plan is correct for any list, requires no extra sorting, and fails gracefully — it just reports nothing left to check.

```python
def find_crate(manifest, target):
    """Scan bow to stern. Return index, or -1 if missing."""
    for index, crate in enumerate(manifest):
        if crate == target:
            return index
    return -1

berths = ["Crate-17", "Crate-05", "Crate-42", "Crate-09"]
print("Crate-42 at berth:", find_crate(berths, "Crate-42"))
print("Crate-77 at berth:", find_crate(berths, "Crate-77"))
```

## Output

```text
Crate-42 at berth: 2
Crate-77 at berth: -1
```

> [!NOTE]
> "Find it" is not the same question as "where is it". The algorithm above answers "where is it, or say it's missing". Stating the stopping condition ("end of manifest" counts as failure) matters as much as the comparison itself; without it, the plan is vague and hard to trace.

## Cost becomes visible when the map grows

The charter's real lesson is scale. For a short jetty, lifting five crates is trivial. For a supply chain spread across coves with thousands of crate-slots, *how many comparisons* happen is the bill. A linear scan does up to *n* checks in the worst case (the crate is last, or not present). Doubling the manifest tends to double that worst-case bill if nothing about the shape changes.

```python
# Trace count by hand for the worst case
manifest = ["A1", "A2", "A3", "A4", "A5"]
# Looking for "A5": checks index 0,1,2,3,4 -> 5 checks
# Looking for "MISSING": checks all 5 -> 5 checks, return -1
print("length:", len(manifest))
```

> [!WARNING]
> Never trust "it ran fast on my tiny test". The Survey always asks for the worst case over the plausible size of the map, because the tide turns on the worst case, not the best one.

## Shape invites better plans

Order changes what's possible. If the same crate numbers are filed by numeric value instead of loading order, the wayfarer can make a different plan entirely — one that discards large chunks of the rack without inspecting them. The data structure didn't gain magical speed by itself; placing it in order unlocked a new algorithm. That trade-off (sort once, search differently after) is a recurring theme for the rest of this module.

```python
as_loaded = [17, 5, 42, 9, 31]
filed = sorted(as_loaded)
print("as loaded:", as_loaded)
print("filed by crate number:", filed)
```

## Output

```text
as loaded: [17, 5, 42, 9, 31]
filed by crate number: [5, 9, 17, 31, 42]
```

> [!TIP]
> The charter's discipline: (1) pick a shape, (2) write an explicit plan, (3) trace by hand on a small example, (4) reason about worst-case count as the list grows. Do those four before optimizing. Most "slow" code fails at step four, not step one.

