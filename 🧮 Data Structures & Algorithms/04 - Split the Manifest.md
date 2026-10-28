
# 04. Split the Manifest

**Spanish version:** [04 - Dividir el Manifiesto](./04%20-%20Dividir%20el%20Manifiesto.md)

**Course:** Data Structures & Algorithms
**Chapter:** 4 — The Racked Berths
**Topic:** Divide and conquer, binary search, iterative/recursive, edge cases, O(log n)
**Tags:** `#dsa` `#binary-search` `#divide-and-conquer` `#complexity`

A jetty can only take so many crates on open ground before the tide swallows the stacks. The Wayfarer Survey files slow-moving cargo in a **racked berth**: slots numbered by crate number, in strict order along the wall. Once the rack is ordered, looking for Crate-42 no longer means opening every slot. It means standing in the middle, reading one label, and throwing away an entire wing of the rack in one go. That habit is **binary search**: divide, rule out, repeat.

## Why order is the lever

Binary search only works if the list is **sorted by the key you're looking for**. The reason is simple: if you know the middle value `M` and the target `T < M`, then no element to the right of `M` can be smaller than `M` in a sorted ascending list, so `T` cannot be there if it exists. Sorting is paid up front to earn that guarantee on every lookup after.

```python
racked = [5, 9, 17, 31, 42, 55, 64, 77]
# sorted ascending by crate number
print(racked)
```

## Output

```text
[5, 9, 17, 31, 42, 55, 64, 77]
```

> [!NOTE]
> Order is a prerequisite, not an optimization you can bolt on mid-search. If the rack is unsorted, discarding a half is unsafe and the algorithm becomes wrong.

## Halving by hand

Take `target = 42` in the rack above (indices 0-7). Find middle: `(0+7)//2 = 3`, value `31`. `42 > 31`, so rule out left half including middle; set `left = 4`. Now range [4,7], middle `(4+7)//2 = 5`, value `55`. `42 < 55`, rule out right half; set `right = 4`. Now range [4,4], middle 4, value `42` equals target — found. Three checks to find a value that would be 5th in a linear scan from front.

```python
racked = [5, 9, 17, 31, 42, 55, 64, 77]
# trace for 42: (0,7)->mid3 val31, go right (left=4); (4,7)->mid5 val55, go left (right=4); (4,4)->mid4 val42 == target
print("found in 3 steps by hand")
```

## Iterative binary search

The iterative form keeps two pointers `left` and `right`. While `left <= right`, check the middle. Move pointers inward according to comparison. If the interval collapses (`left > right`) without a match, the target isn't on the rack.

```python
def binary_search(racked, target):
    left = 0
    right = len(racked) - 1
    while left <= right:
        mid = (left + right) // 2
        if racked[mid] == target:
            return mid
        elif target < racked[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

racked = [5, 9, 17, 31, 42, 55, 64, 77]
print(binary_search(racked, 42))
print(binary_search(racked, 7))
```

## Output

```text
4
-1
```

> [!WARNING]
> Common slip: writing `left = mid` instead of `left = mid + 1`, or `right = mid` instead of `right = mid - 1`. Without moving past the middle, the interval never shrinks and the loop can spin forever. Always move the pointer past `mid`.

## Recursive binary search

The same plan expressed recursively: if interval empty -> fail; check middle; if match -> return index; else recurse on the surviving half. With default parameters, care must be taken not to capture mutable state incorrectly; passing `left/right` explicitly keeps the logic clear and traceable by hand.

```python
def binary_search_rec(racked, target, left=0, right=None):
    if right is None:
        right = len(racked) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if racked[mid] == target:
        return mid
    elif target < racked[mid]:
        return binary_search_rec(racked, target, left, right - 1)
    else:
        return binary_search_rec(racked, target, left + 1, right)

racked = [5, 9, 17, 31, 42, 55, 64, 77]
print(binary_search_rec(racked, 55))
```

## Output

```text
5
```

> [!TIP]
> Iterative uses O(1) extra space (pointers). Recursive uses O(log n) extra space for the call stack because each halving adds a frame until the base case. Both are correct; choose based on readability and environment, but know the trade-off.

## Count checks against linear search

The gap is clearest when counted. For 1000 ordered slots, binary search needs at most ~10 checks; linear search needs up to 1000 in the worst case. For missing targets it's even more striking.

```python
def linear_count(racked, target):
    for i, v in enumerate(racked):
        if v == target:
            return i + 1  # checks
    return len(racked)

def binary_count(racked, target):
    left, right, checks = 0, len(racked) - 1, 0
    while left <= right:
        checks += 1
        mid = (left + right) // 2
        if racked[mid] == target:
            return checks
        elif target < racked[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return checks

big = [i for i in range(1000)]  # ordered slots
print("linear finds 999:", linear_count(big, 999))
print("binary finds 999:", binary_count(big, 999))
print("binary missing:", binary_count(big, -1))
```

## Output

```text
linear finds 999: 1000
binary finds 999: 10
binary missing: 10
```

## Complexity and the price of order

- **Time:** Best case O(1) (found at middle immediately). Worst case O(log n) (absent or at end, halved down to empty). Average similar to worst for "random" targets in ordered list.
- **Space:** Iterative O(1); recursive O(log n) due to stack.
- **Upfront cost:** To use binary search you must have the list **sorted** — sorting is typically O(n log n). If you only search once, that's usually worse than O(n) linear. If you search many times, O(n log n) once + O(log n)*k is usually better.

> [!CAUTION]
> Never apply binary search to a linked list by naive indexing (no random access) or to an unsorted structure and expect correctness. The guarantee comes entirely from order and random access by index.

