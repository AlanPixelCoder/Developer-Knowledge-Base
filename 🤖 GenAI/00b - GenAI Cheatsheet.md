
# 00b. GenAI Cheatsheet

**Spanish version:** [00b - Chuleta de GenAI.md](00b%20-%20Chuleta%20de%20GenAI.md)

**Course:** GenAI
**Topic:** Quick Reference for How LLMs Work, Plus the Python Code From Chapters 01 and 03
**Tags:** `#genai` `#ai` `#llm` `#cheatsheet` `#reference`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

One page for the whole module. Everything here was built in [[01 - Beacon Signals]] and [[03 - Meadow Index]]; nothing is new. Prompt patterns and the risk checklist live in [[00c - GenAI Cheatsheet II]].

---

## 📖 Glossary

| Term | Meaning |
| :--- | :--- |
| **Generative AI (GenAI)** | AI that creates new content (text, code, images, audio, video) by learning patterns from data |
| **LLM** | Large Language Model: processes and generates text by predicting the next token |
| **Token** | A small chunk of text the model reads and generates |
| **Subword tokenization** | Splitting rare or long words into smaller reusable pieces |
| **N-gram** | A sequence of *n* consecutive tokens (unigram, bigram, trigram) |
| **Parameters** | The billions of numbers a model adjusts during training |
| **Training** | The slow, expensive process of adjusting parameters using data |
| **Inference** | The fast process of using a trained model to predict tokens |
| **Prompt** | The text sent to a model; the only "knob" we have |
| **Vector** | An ordered list of numbers, e.g. `[82, 84, 77]` |
| **Embedding** | A vector that represents the meaning of a piece of text |
| **Training cutoff** | The date where a model's training data ends |
| **Hallucination** | A plausible-sounding but made-up or incorrect answer |
| **Prompt injection** | Untrusted content containing instructions the model follows |
| **RAG** | Retrieval-Augmented Generation: search + LLM |
| **Fine-tuning** | Adapting a base model to your own data |

---

## 🔁 The LLM Loop

```text
prompt -> tokenize -> predict next token -> append -> repeat -> stop signal
```

Training and inference are different jobs:

| Phase | What happens | Cost |
| :--- | :--- | :--- |
| **Training** | The model adjusts billions of parameters using data | Weeks or months |
| **Inference** | A trained model predicts the next token for your prompt | Milliseconds |

---

## 🐍 Python Snippets

### Tokenizer

```python
import re

def tokenize(text):
    return re.findall(r'\w+|[^\w\s]', text)
```

### Bigrams

```python
def get_bigrams(tokens):
    return [tokens[i] + ' ' + tokens[i + 1] for i in range(len(tokens) - 1)]
```

### Frequency dictionary (next-token counts)

```python
def count_next_tokens(tokens):
    counts = {}
    for i in range(len(tokens) - 2):
        bigram = tokens[i] + ' ' + tokens[i + 1]
        nxt = tokens[i + 2]
        counts.setdefault(bigram, {})
        counts[bigram][nxt] = counts[bigram].get(nxt, 0) + 1
    return counts
```

### Predict and autocomplete

```python
def predict_next(phrase, counts):
    tokens = tokenize(phrase.lower())
    context = tokens[-2] + ' ' + tokens[-1]
    if context not in counts:
        return None
    return max(counts[context], key=counts[context].get)

def autocomplete(phrase, counts, num_tokens=5):
    for _ in range(num_tokens):
        nxt = predict_next(phrase, counts)
        if nxt is None:
            break
        phrase += ' ' + nxt
    return phrase
```

### One-hot and Hamming distance

```python
def one_hot(word, vocab):
    v = [0] * len(vocab)
    v[vocab.index(word)] = 1
    return v

def hamming(v1, v2):
    return sum(1 for a, b in zip(v1, v2) if a != b)
```

### Bag of words

```python
def build_vocab(docs):
    vocab = []
    for doc in docs:
        for w in doc.split():
            if w not in vocab:
                vocab.append(w)
    return vocab

def bag_of_words(doc, vocab):
    v = [0] * len(vocab)
    for w in doc.split():
        v[vocab.index(w)] += 1
    return v
```

### Cosine similarity and search

```python
import math

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def magnitude(v):
    return math.sqrt(sum(x * x for x in v))

def cosine_similarity(v1, v2):
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))

def search(query, documents):
    vocab = build_vocab(documents + [query])
    q = bag_of_words(query, vocab)
    results = [(cosine_similarity(q, bag_of_words(d, vocab)), d)
               for d in documents]
    return sorted(results, reverse=True)
```

---

## 🔤 The Regex Pattern Used

| Pattern | Matches |
| :--- | :--- |
| `\w+` | One or more word characters (a word) |
| `[^\w\s]` | One character that is not a word character or whitespace (punctuation) |
| `\w+\|[^\w\s]` | Either of the above (our token pattern) |

---

## ⚠️ Traps Worth Memorizing

| Trap | What actually happens |
| :--- | :--- |
| Loop to `len(tokens)` | `IndexError` — a bigram needs one token less, a trigram two |
| `counts[bigram][nxt] += 1` on a missing key | `KeyError` — use `setdefault` or `dict.get` |
| `counts.get('never seen')` | Returns `None`, and `None.items()` crashes |
| `cosine_similarity` on a zero vector | `ZeroDivisionError` — an empty document produces one |
| Bag of words and plurals | `wraith` and `wraiths` are different tokens, so the score is `0` |

---
