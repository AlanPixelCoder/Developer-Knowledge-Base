
# 00b. Chuleta de GenAI

**Versión original en inglés:** [00b - GenAI Cheatsheet.md](00b%20-%20GenAI%20Cheatsheet.md)

**Curso:** GenAI
**Tema:** Referencia rápida de cómo funcionan los LLM, más el código Python de los capítulos 01 y 03
**Tags:** `#genai` `#ai` `#llm` `#chuleta` `#referencia`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

Una página para todo el módulo. Todo lo de aquí se construyó en [[01 - Señales de Baliza]] y [[03 - Índice del Prado]]; aquí no hay nada nuevo. Los patrones de prompt y la lista de riesgos viven en [[00c - Chuleta de GenAI II]].

---

## 📖 Glosario

| Término | Significado |
| :--- | :--- |
| **IA Generativa (GenAI)** | IA que crea contenido nuevo (texto, código, imágenes, audio, vídeo) aprendiendo patrones a partir de datos |
| **LLM** | Modelo de Lenguaje Grande: procesa y genera texto prediciendo el siguiente token |
| **Token** | Un trozo pequeño de texto que el modelo lee y genera |
| **Tokenización por subpalabras** | Partir palabras raras o largas en trozos más pequeños reutilizables |
| **N-grama** | Una secuencia de *n* tokens consecutivos (unigrama, bigrama, trigrama) |
| **Parámetros** | Los miles de millones de números que un modelo ajusta durante el entrenamiento |
| **Entrenamiento** | El proceso lento y caro de ajustar los parámetros con datos |
| **Inferencia** | El proceso rápido de usar un modelo entrenado para predecir tokens |
| **Prompt** | El texto que se envía a un modelo; el único "mando" que tenemos |
| **Vector** | Una lista ordenada de números, p. ej. `[82, 84, 77]` |
| **Embedding** | Un vector que representa el significado de un fragmento de texto |
| **Fecha de corte** | La fecha en la que terminan los datos de entrenamiento de un modelo |
| **Alucinación** | Una respuesta inventada o incorrecta que suena totalmente plausible |
| **Inyección de prompts** | Contenido no confiable con instrucciones que el modelo sigue |
| **RAG** | Retrieval-Augmented Generation: búsqueda + LLM |
| **Fine-tuning** | Adaptar un modelo base a tus propios datos |

---

## 🔁 El Bucle del LLM

```text
prompt -> tokenizar -> predecir el siguiente token -> añadir -> repetir -> señal de parada
```

Entrenar e inferir son trabajos distintos:

| Fase | Qué ocurre | Coste |
| :--- | :--- | :--- |
| **Entrenamiento** | El modelo ajusta miles de millones de parámetros con datos | Semanas o meses |
| **Inferencia** | Un modelo entrenado predice el siguiente token de tu prompt | Milisegundos |

---

## 🐍 Fragmentos de Python

### Tokenizador

```python
import re

def tokenize(text):
    return re.findall(r'\w+|[^\w\s]', text)
```

### Bigramas

```python
def get_bigrams(tokens):
    return [tokens[i] + ' ' + tokens[i + 1] for i in range(len(tokens) - 1)]
```

### Diccionario de frecuencias (conteos del siguiente token)

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

### Predecir y autocompletar

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

### One-hot y distancia de Hamming

```python
def one_hot(word, vocab):
    v = [0] * len(vocab)
    v[vocab.index(word)] = 1
    return v

def hamming(v1, v2):
    return sum(1 for a, b in zip(v1, v2) if a != b)
```

### Bolsa de palabras

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

### Similitud coseno y búsqueda

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

## 🔤 El Patrón Regex Utilizado

| Patrón | Qué encuentra |
| :--- | :--- |
| `\w+` | Uno o más caracteres de palabra (una palabra) |
| `[^\w\s]` | Un carácter que no sea de palabra ni de espacio (puntuación) |
| `\w+\|[^\w\s]` | Cualquiera de los dos (nuestro patrón de tokenización) |

---

## ⚠️ Trampas que conviene memorizar

| Trampa | Qué pasa en realidad |
| :--- | :--- |
| Bucle hasta `len(tokens)` | `IndexError` — un bigrama necesita un token menos, un trigrama dos menos |
| `counts[bigram][nxt] += 1` con la clave ausente | `KeyError` — usa `setdefault` o `dict.get` |
| `counts.get('nunca visto')` | Devuelve `None`, y `None.items()` revienta |
| `cosine_similarity` sobre un vector de ceros | `ZeroDivisionError` — un documento vacío produce uno |
| Bolsa de palabras y plurales | `wraith` y `wraiths` son tokens distintos, así que la puntuación es `0` |

---
