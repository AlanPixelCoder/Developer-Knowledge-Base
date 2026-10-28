
# 03. Meadow Index

**Spanish version:** [03 - Índice del Prado](./03%20-%20%C3%8Dndice%20del%20Prado.md)

**Course:** GenAI
**Chapter:** 3 — Verdant Relay
**Topic:** Embeddings, vectors, similarity, semantic search
**Tags:** `#genai` `#embeddings` `#semantic-search` `#vectors` `#python`

Verdant Relay maintains a small meadow of relay notes: old fault reports, fixes, parts, locations. A keyword search on "fog" finds reports that say "fog", but it misses "mist" or "low visibility" even if they're about the same problem at a neighboring pole. The field needs **semantic search** — find notes by *meaning*, not by exact string match. This lesson builds the idea from scratch with nothing but lists and math: represent text as vectors, measure angle between them, and rank by similarity. No pretrained model call is assumed; trace every step.

## From words to counts

A simple starting point is **bag of words** (BoW). Take a small vocabulary of terms that appear in meadow notes, and represent each note as a vector counting how many times each term appears. Order is lost, but co-occurrence gives a rough shape of content.

```python
vocab = ["fog", "mist", "wire", "gate", "mast"]
# note A
a = [1, 0, 0, 1, 0]  # fog, gate
# note B
b = [0, 1, 0, 1, 0]  # mist, gate
print("a:", a)
print("b:", b)
```

## Output

```text
a: [1, 0, 0, 1, 0]
b: [0, 1, 0, 1, 0]
```

These vectors are different at two positions, but both talk about visibility at the gate. Exact count matching would say different, yet semantically close.

> [!NOTE]
> Bag of words ignores word order and grammar. For short field notes it's a useful teaching toy: it shows *representation* as the hard problem. Real embeddings do this with learned, much larger vectors, capturing relations like "mist" and "fog" being near each other.

## Measuring similarity

To compare vectors, use **cosine similarity**. It looks at the angle between vectors, not their length. Two notes pointing in roughly the same direction are similar even if one is longer (mentions terms more times). Formula: $\cos(\theta)=\frac{A\cdot B}{\|A\|\|B\|}$.

```python
import math

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm(v):
    return math.sqrt(sum(x*x for x in v))

def cosine(a,b):
    d = dot(a,b)
    if d == 0: return 0.0
    return d / (norm(a)*norm(b))

print(cosine(a,b))  # gate only in common
```

## Output

```text
0.5
```

Both share "gate" (dimension for gate) giving dot product 1, norms sqrt(1^2+1^2)=sqrt(2), so 1/(sqrt(2)*sqrt(2))=0.5. The angle is 60 degrees — not identical, not orthogonal. For a tiny toy vocab this matches intuition.

## A meadow index

Build a small index of meadow notes with their vectors over the vocab. Given a query, vectorize the query the same way and rank by cosine similarity descending.

```python
notes = [
    ("N1", "fog at gate", [1,0,0,1,0]),
    ("N2", "mist at gate", [0,1,0,1,0]),
    ("N3", "loose wire at mast", [0,0,1,0,1]),
]
query = "low mist near gate"  # not in vocab exactly, toy
qv = [0,1,0,1,0]  # map mist->1, gate->1
for nid, text, v in notes:
    print(nid, cosine(qv,v), text)
```

## Output

```text
N1 0.5 fog at gate
N2 1.0 mist at gate
N3 0.0 loose wire at mast
```

With exact vocab matches, "mist at gate" ranks first for a query about mist at gate. In reality embeddings would also pull "fog at gate" up because learned embeddings place fog/mist near each other — the key idea is the same: compare vectors in a shared space.

> [!WARNING]
> This BoW+cosine is a toy. It fails on synonyms not in vocab, word order, and negation. Real embeddings fix some of this by learning from large corpora, but they still can be wrong. The mechanism (vector + similarity) is what matters.

## Why semantic search helps

Keyword search is brittle for field notes written tersely by tired crews. "Guy-wire" vs "wire", "footing" vs "base", "obstruction" vs "blockage" — all plausible. Semantic search ranks by meaning, so a note about a blocked footing can surface for "drain blocked" even if the exact tokens differ. The trade-off: you need a representation, similarity is computable, but you must still sanity check results.

> [!TIP]
> Don't start by asking for "AI search". Ask: "If I had vectors for these notes, which three would be closest to this query by angle?" If you can answer that with cosine, you understand semantic search at the level needed for this module.

