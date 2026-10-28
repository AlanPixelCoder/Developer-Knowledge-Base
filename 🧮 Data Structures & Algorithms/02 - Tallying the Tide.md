
# 02. Tallying the Tide

**Spanish version:** [02 - Contando la Marea](./02%20-%20Contando%20la%20Marea.md)

**Course:** Data Structures & Algorithms
**Chapter:** 2 — Cost
**Topic:** Time/space, Big O, growth table, linear vs search tradeoffs
**Tags:** `#dsa` `#big-o` `#complexity` `#algorithms`

The tide doesn't care about clock time on the wayfarer's wristwatch. It cares about count: how many times did the skiff stop at a berth, how many comparisons were made before moving on? For the Wayfarer Survey, **efficiency** means answering "how does this plan behave as *n* grows?" not "how fast did it run once on this jetty?" That single change in question is why complexity analysis exists.

## Measuring work, not seconds

When tracing a plan by hand, count the operations that scale. For a linear scan, the comparison `crate == target` is the thing that multiplies when the manifest grows. A short test might return instantly, but the worst case is the one that makes a skipper miss the tide window. 

```python
def scan_with_count(manifest, target):
    """Count comparisons to see the bill."""
    checks = 0
    for crate in manifest:
        checks += 1
        if crate == target:
            return checks
    return checks

berths = ["Crate-17", "Crate-05", "Crate-42", "Crate-09", "Crate-31"]
print("Found Crate-31 in checks:", scan_with_count(berths, "Crate-31"))  # last
print("Missing Crate-00 in checks:", scan_with_count(berths, "Crate-00")) # none
```

## Output

```text
Found Crate-31 in checks: 5
Missing Crate-00 in checks: 5
```

For this list of length 5, the worst case is 5 checks. The pattern is simple: in the worst case, linear scan does **up to *n* comparisons** for a list of length *n*.

> [!NOTE]
> Time complexity describes growth of steps as *n* grows. Space complexity describes growth of extra memory as *n* grows. The Survey mostly tracks time here, but both matter when skiffs have limited gear.

## Big O as a coarse map of growth

**Big O notation** gives the upper-bound shape. It drops constants and lower-order terms because the question is "which family does this fall into?" not "exactly 17 checks on Tuesday". For linear scan, the family is **O(n)** (read "order n").

| n (berths) | Worst-case checks (O(n)) | Rough feel |
| :--- | :--- | :--- |
| 5 | 5 | trivial |
| 50 | 50 | still quick by hand |
| 500 | 500 | slower to trace, easy to automate badly |
| 5,000 | 5,000 | misses tight tide windows if done blindly |

The key: if *n* doubles, O(n) roughly doubles. That linear growth is the price for a plan that requires no order.

## A better shape: halving the rack

If the manifest is filed **by crate number** on a slotted rack, a different plan becomes possible. Look at the middle slot: if the target matches, stop. If the target is smaller than the middle crate number, the target cannot be in the right half — rule out the entire right half and search left. If larger, rule out left half and search right. Repeat, halving the remaining rack each time. This is **binary search**; its worst-case growth is **O(log n)**.

```python
def binary_scan_with_count(sorted_manifest, target):
    """Binary search with a check counter."""
    left = 0
    right = len(sorted_manifest) - 1
    checks = 0
    while left <= right:
        checks += 1
        mid = (left + right) // 2
        if sorted_manifest[mid] == target:
            return checks
        elif target < sorted_manifest[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return checks

racked = [5, 9, 17, 31, 42, 55, 64, 77, 88, 99]
print("Find 5 (first):", binary_scan_with_count(racked, 5), "checks")
print("Find 99 (last):", binary_scan_with_count(racked, 99), "checks")
print("Find 7 (missing):", binary_scan_with_count(racked, 7), "checks")
```

## Output

```text
Find 5 (first): 4
Find 99 (last): 4
Find 7 (missing): 4
```

For 10 items, both ends and a missing value take at most ~4 checks because $2^4 = 16 >= 10$. For 1000 items, worst case is about 10 checks; for 1,000,000 items, about 20 checks. Halving dominates linear growth very quickly.

> [!WARNING]
> Binary search is only correct if the rack is **sorted by the key you're searching on**. If the list is unordered, ruling out halves is false: the missing half might contain the target. Order is a prerequisite, not a nice-to-have.

## Growth table: see the gap

| n | O(n) worst (linear) | O(log₂ n) worst (binary) |
| :--- | :--- | :--- |
| 10 | 10 | ~4 |
| 100 | 100 | ~7 |
| 1,000 | 1,000 | ~10 |
| 10,000 | 10,000 | ~14 |
| 1,000,000 | 1,000,000 | ~20 |

The difference isn't about small n. It's about the curve: linear climbs straight up, logarithmic barely rises. That curve is exactly why the Survey files crates by number when searches are frequent.

## The trade-off in practice

Speed isn't free. Sorting a list of *n* items by a comparison sort costs roughly **O(n log n)** in the worst case. If the Survey only searches once, paying O(n log n) to sort plus O(log n) to search might be worse than a single O(n) linear scan. If the Survey searches *hundreds* of times against the same filed rack, paying O(n log n) once and O(log n) per search is almost certainly better. Efficiency is always about *context* (how many times, on what shape), not a universal winner.

```python
# Context matters: count total rough work by shape
# One search on unordered: linear ~n
# Many searches on sorted: sort ~n log n + (searches * log n)
print("context decides the route")
```

> [!TIP]
> Don't memorize constants. Memorize families and trade-offs. Ask: "Is this shape ordered? How many lookups? Can I afford to order once?" Those three questions tell you more than timing a single run.

