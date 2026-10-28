
# 01. Beacon Signals

**Spanish version:** [01 - Señales de Baliza](./01%20-%20Se%C3%B1ales%20de%20Baliza.md)

**Course:** GenAI
**Chapter:** 1 — Verdant Relay
**Topic:** Tokens, n-grams, counting, next-token prediction
**Tags:** `#genai` `#llm` `#tokens` `#ngrams` `#python`

Verdant Relay is a field-operations studio that keeps beacons lit across a patchwork of relay poles. Each pole reports a short burst of telemetry: status, voltage, obstruction, crew notes. The field logs are terse by necessity, and a trained relay officer can guess the next line from context alone. A **language model** does the same thing, only it learns those guesses by counting patterns in text. Chapter one builds that counter from nothing but Python's standard library: split into tokens, tally transitions, and predict what tends to come next.

## Reading without words

An LLM doesn't read sentences the way a person does. It reads **tokens** — chunks of text that may be whole words, parts of words, or punctuation. The split affects what the model can reason over, so it's worth watching a tokenizer do its work rather than treating it as invisible.

```python
import re

def tokenize(text):
    return re.findall(r'\w+|[^\w\s]', text)

print(tokenize("Pole-7 reports fog at relay gate."))
```

## Output

```text
['Pole-7', 'reports', 'fog', 'at', 'relay', 'gate', '.']
```

> [!NOTE]
> Hyphenated identifiers often stay attached depending on the pattern. Punctuation becomes its own token. Different models make different choices; the important point is that the *unit of prediction* is the token, not the whole word.

## Bigrams: what follows what

Once text is tokenized, the simplest predictor looks at **bigrams** (pairs of consecutive tokens). Count how often token B follows token A. When the model sees A in a new burst, it can suggest B that appeared most often after A in the known telemetry logs. This is not understanding — it's frequency.

```python
def get_bigrams(tokens):
    return [tokens[i] + ' ' + tokens[i + 1] for i in range(len(tokens)-1)]

log = tokenize("Pole-3 reports fog. Pole-3 reports wind.")
print(get_bigrams(log))
```

## Output

```text
['Pole-3 reports', 'reports fog', 'fog .', '. Pole-3', 'Pole-3 reports', 'reports wind', 'wind .']
```

## Tallying transitions

A useful next-token predictor keeps a map from the current token to a count of what came after it. With enough field logs, common transitions rise to the top. The predictor doesn't need a massive model to be instructive — it needs enough consistent phrasing to show the mechanism.

```python
from collections import defaultdict

corpus = [
    "Pole-3 reports fog near gate.",
    "Pole-3 reports fog near mast.",
    "Pole-7 reports wind near gate.",
    "Pole-7 reports hail near mast.",
]

def train_bigram(corpus):
    model = defaultdict(list)
    for line in corpus:
        tokens = tokenize(line)
        for i in range(len(tokens)-1):
            model[tokens[i]].append(tokens[i+1])
    return model

m = train_bigram(corpus)
print(m['Pole-3'])
print(m['reports'])
```

## Output

```text
['reports', 'reports']
print(m['reports'])
['fog', 'fog', 'wind', 'hail']
```

> [!WARNING]
> A pure bigram predictor has no memory beyond the last token. It cannot know "Pole-3 already reported fog twice" or enforce consistency across a long burst — it only knows local transitions. That blind spot is a feature to observe, not a bug to patch in this lesson.

## Predicting a burst

With counts, the simplest strategy is to pick the most frequent next token for the current one. For Verdant Relay field notes, this will often produce a plausible-sounding line fragment, and just as often produce something oddly repetitive or wrong when context runs out.

```python
def predict_next(model, token):
    options = model[token]
    if not options:
        return '.'
    # naive: most frequent
    return max(set(options), key=options.count)

# simulate
cur = 'Pole-3'
out = [cur]
for _ in range(4):
    cur = predict_next(m, cur)
    out.append(cur)
print(' '.join(out))
```

## Output

```text
Pole-3 reports fog near
```

## Why this matters

Building this counter by hand makes three things unavoidable. First, **tokens are the unit**. Second, **prediction is statistical** — "most common next" is a guess, not reasoning. Third, **scope is everything**: a predictor trained on gate reports will guess differently than one trained on mast repairs. The fluency of a large model comes from scale and training, but the core idea is exactly this tally. Keep that in mind for the rest of the Verdant Relay module.

> [!TIP]
> Trace the bigram loop on paper for one short line before reading further. If you can see which pair produces which count, you'll understand why next-token prediction is called exactly that.

