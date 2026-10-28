
# 05. Sort by Bearing

**Spanish version:** [05 - Ordenar por Rumbo](./05%20-%20Ordenar%20por%20Rumbo.md)

**Course:** Data Structures & Algorithms
**Chapter:** 5 — The Filing Bench
**Topic:** Selection sort, in-place, nested loops, swaps, O(n²), comparisons count
**Tags:** `#dsa` `#sorting` `#selection-sort` `#complexity`

When crates come ashore in random order, the racked berth won't help. The Wayfarer Survey has a filing bench for that exact job: pull the smallest (or lightest, or earliest by bearing number) crate from the unsorted pile and place it at the front of the sorted section. Build that sorted section one by one, in place, until the whole pile is racked in order. That disciplined hand-sorting is **Selection Sort**. It's not the fastest sort in the world, but it is brutally easy to trace, which makes it perfect for learning what sorting *actually* does.

## The bench layout

Think of the list as two zones growing into each other: a **sorted** prefix on the left, an **unsorted** suffix on the right. Start with sorted empty, unsorted everything. On each pass, scan the unsorted suffix to find the **minimum** element, swap it with the first element of the unsorted suffix, then extend the sorted prefix by one.

```python
# Visual intuition by positions
pile = [42, 17, 55, 9, 31]
# pass 1: find min in whole list -> 9 at index 3, swap with index 0 -> [9, 17, 55, 42, 31]
# pass 2: find min in suffix starting at 1 -> 17 already at 1, no swap needed
# pass 3: find min in suffix starting at 2 -> 31 at index 4, swap with index 2 -> [9, 17, 31, 42, 55]
print([9, 17, 31, 42, 55])
```

## Output

```text
[9, 17, 31, 42, 55]
```

> [!NOTE]
> Selection sort **selects** the minimum (or maximum) from the unsorted part and puts it in place. It doesn't bubble elements across large gaps by adjacent swaps like bubble sort does; it does at most *n-1* swaps total, which can matter if swaps are expensive, even if comparisons are many.

## Trace step by step

Let’s trace `[64, 25, 12, 22, 11]` carefully. The goal is to see both the **search for min** and the **swap**.

**Pass 1 (unsorted from index 0):** scan 64,25,12,22,11 -> minimum is 11 at index 4. Swap index 0 and 4: `[11, 25, 12, 22, 64]`. Sorted prefix length 1.

**Pass 2 (unsorted from index 1):** scan 25,12,22,64 -> minimum 12 at index 2. Swap index 1 and 2: `[11, 12, 25, 22, 64]`. Sorted prefix length 2.

**Pass 3 (unsorted from index 2):** scan 25,22,64 -> minimum 22 at index 3. Swap index 2 and 3: `[11, 12, 22, 25, 64]`. Sorted prefix length 3.

**Pass 4 (unsorted from index 3):** scan 25,64 -> minimum 25 is already at index 3, no swap. Sorted prefix length 4; the single remaining element closes the list.

```python
pile = [64, 25, 12, 22, 11]
# traced above
print("final:", [11, 12, 22, 25, 64])
```

## Output

```text
final: [11, 12, 22, 25, 64]
```

> [!WARNING]
> Don't confuse "find the position of min" with "swap adjacent elements". Selection sort finds the *index* of the minimum in the unsorted region and swaps it directly with the boundary. That direct swap is the defining characteristic.

## Implementing Selection Sort

The code mirrors the bench: outer loop sets the boundary `i` (start of unsorted); inner loop scans from `i` to end to find `min_idx`; if different, swap `pile[i] and pile[min_idx]`.

```python
def selection_sort(pile):
    n = len(pile)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if pile[j] < pile[min_idx]:
                min_idx = j
        if min_idx != i:
            # swap
            pile[i], pile[min_idx] = pile[min_idx], pile[i]
    return pile

bearings = [42, 17, 55, 9, 31]
print(selection_sort(bearings[:]))
```

## Output

```text
[9, 17, 31, 42, 55]
```

> [!TIP]
> Passing `bearings[:]` creates a copy so we don't mutate the original list in the test — useful when tracing multiple algorithms against the same pile.

## Counting comparisons to see the bill

Selection sort always does the same number of comparisons regardless of whether the pile is already sorted or completely reversed, because it scans the entire unsorted region every pass to find the minimum. That is different from some other sorts.

```python
def selection_sort_comparisons(pile):
    """Count the comparisons of one selection-sort pass."""
    n = len(pile)
    comparisons = 0
    arr = pile[:]
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons

ascending = [1, 2, 3, 4, 5]
descending = [5, 4, 3, 2, 1]
print(selection_sort_comparisons(ascending))
print(selection_sort_comparisons(descending))
```

## Output

```text
10
10
```

For n=5, comparisons are 4+3+2+1 = 10. For general n, comparisons = n*(n-1)/2 regardless of initial order. Swaps are at most n-1.

## Complexity: exact reasoning

- **Time (comparisons):** Worst case, average case, and best case all give **O(n²)** because the inner scan always runs over the full remaining suffix. Selection sort doesn't get faster just because the pile is already sorted.
- **Time (swaps):** O(n) in total (at most n-1 swaps).
- **Space:** **O(1)** extra space — sorting is done in place on the same list.
- **Stability:** Selection sort is **not stable** by default; swapping a minimum far away can move equal elements relative to each other.

> [!CAUTION]
> The number of comparisons is fixed by n, not by order. If a sort claims to be "faster" on already-sorted data, selection sort won't be it. That predictability is useful for worst-case reasoning even if it's not optimal.

## When to file with selection sort

Selection sort shines as a teaching tool: every step is visible, the invariant ("everything left of i is sorted and final") is easy to hold, and the cost is easy to state exactly. In practice, for large n you'd reach for more efficient sorts, but for small n or when minimizing swaps matters, it's worth knowing. The Survey values it because you can trace it on the filing bench without a computer to catch a logic error.

```python
# Small pile, trace by hand is the point
small = [3, 1, 4, 1, 5, 9]
sorted_small = selection_sort(small[:])
print(sorted_small)
```

## Output

```text
[1, 1, 3, 4, 5, 9]
```

> [!TIP]
> Always state the invariant: after pass i, the first i+1 elements are the i+1 smallest elements in order and will not move again. If your trace breaks that invariant, you found a bug. Hold to that invariant and selection sort becomes hard to mess up.

