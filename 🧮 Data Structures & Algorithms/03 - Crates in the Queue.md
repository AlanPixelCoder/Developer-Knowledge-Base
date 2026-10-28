
# 03. Crates in the Queue

**Spanish version:** [03 - Cajas en la Cola](./03%20-%20Cajas%20en%20la%20Cola.md)

**Course:** Data Structures & Algorithms
**Chapter:** 3 — The Jetty
**Topic:** Lists, indexing, slicing, methods, linear scan by hand
**Tags:** `#dsa` `#lists` `#linear-search` `#python`

The jetty doesn't unload randomly. A winch brings crates ashore in some order, and the wayfarers form a queue against the tide clock. If the queue order is known, grabbing the next crate is instant. If someone shouts "find Crate-42" and nobody marked its place, the only honest tool for an unordered queue is to walk from the front until it's found. This lesson treats Python lists as the jetty's queue and traces a linear scan line by line until it's second nature.

## A queue you can count

A **list** holds items in sequence, indexed from `0` at the front. Indexing reads a known berth without disturbing the rest; **slicing** pulls a contiguous run for inspection. These are not trivia — on a tight tide, reading the wrong index is the same as opening the wrong crate.

```python
queue = ["Crate-17", "Crate-05", "Crate-42", "Crate-09", "Crate-88"]
print("Front:", queue[0])
print("Third:", queue[2])
print("First three:", queue[0:3])  # end is exclusive
print("From index 2:", queue[2:])
```

## Output

```text
Front: Crate-17
Third: Crate-42
First three: ['Crate-17', 'Crate-05', 'Crate-42']
From index 2: ['Crate-42', 'Crate-09', 'Crate-88']
```

Notice slicing: `queue[0:3]` gives indices 0,1,2 but not 3. That off-by-one is easy to miss on paper; better to count by hand against the output than to guess.

## Moving crates along the jetty

The queue changes over the course of a run. New crates come ashore (`append`), a priority crate might need to be slotted mid-queue (`insert`), a damaged crate might be pulled out (`pop`), and the skipper needs the count (`len`). Each mutation shifts positions after the point of change — something to remember if indices were written down earlier.

```python
queue = ["Crate-17", "Crate-05", "Crate-42"]
queue.append("Crate-88")        # add to end
queue.insert(1, "Crate-91")    # slot in at index 1
pulled = queue.pop()           # remove from end
print("Pulled:", pulled)
print("Queue now:", queue)
print("Length:", len(queue))
```

## Output

```text
Pulled: Crate-88
Queue now: ['Crate-17', 'Crate-91', 'Crate-05', 'Crate-42']
Length: 4
```

> [!CAUTION]
> After `insert` or `pop` at the front/middle, every element after shifts by ±1. If you cached an index from before the mutation, it may now point to a different crate. On the jetty, don't trust a cached index after reordering the queue.

## Walking the queue by hand

With no index, the plan is mechanical: start at index 0, test for equality, increment index, repeat until match or `index == len(queue)`. This is **linear search**. It makes no assumptions about order and works for any list of comparable values. Its cost in the worst case scales with length, as traced in the previous lesson.

```python
def linear_find(queue, target):
    """Return index or -1; count nothing fancy, just logic."""
    for i in range(len(queue)):
        if queue[i] == target:
            return i
    return -1

queue = ["Crate-17", "Crate-05", "Crate-42", "Crate-09"]
print(linear_find(queue, "Crate-42"))
print(linear_find(queue, "Crate-77"))
```

## Output

```text
2
-1
```

## Tracing until it clicks

To see the bill, trace explicitly. For `target = "Crate-09"` in the queue above: i=0 -> "Crate-17"!=target; i=1 -> no; i=2 -> no; i=3 -> match, return 3. Three checks passed before finding it; if missing, four checks and a return of -1. Write that trace on paper for a moment — the discipline of tracing is more useful than memorizing the definition.

```python
queue = ["Crate-17", "Crate-05", "Crate-42", "Crate-09"]
target = "Crate-09"
# manual trace:
# i=0: Crate-17==Crate-09? no
# i=1: Crate-05==Crate-09? no
# i=2: Crate-42==Crate-09? no
# i=3: Crate-09==Crate-09? yes -> return 3
print("answer:", 3)
```

> [!NOTE]
> `range(len(queue))` is a common shape here: it gives valid indices without risking an index out of range, and it pairs naturally with `queue[i]`. Don't loop over the values and lose the index unless the index truly isn't needed.

## When linear search is the right call

Linear search is not "lazy" — it's correct by default. If the queue is unordered and searched rarely, it's often the simplest honest plan. If the same crate numbers are looked up constantly, the Survey would rather file them (change the shape) than run more scans. The choice is about fit: match the plan to the shape and to the frequency of lookups, not to ego.

```python
# Unordered queue: linear is the direct answer
manifest = ["Netting", "Rope", "Lantern Oil", "Crate-42", "Tar"]
found = linear_find(manifest, "Crate-42")
print("Crate-42 at:", found)
```

> [!TIP]
> On the jetty, correctness first. Get a correct linear scan that returns the index or -1, trace it by hand on two cases (found and missing), and only then count worst-case steps. Those three steps prevent most off-by-one and logic errors.

