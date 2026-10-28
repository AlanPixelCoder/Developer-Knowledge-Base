
# 01. Señales de Baliza

**Versión original en inglés:** [01 - Beacon Signals](./01%20-%20Beacon%20Signals.md)

**Curso:** GenAI
**Capítulo:** 1 — Relevo Verdoso
**Tema:** Tokens, n-gramas, conteo, predicción del siguiente token
**Etiquetas:** `#genai` `#llm` `#tokens` `#ngrams` `#python`

Verdant Relay es un estudio de operaciones de campo que mantiene las balizas encendidas a lo largo de una red de postes de relevo. Cada poste emite un breve informe de telemetría: estado, voltaje, obstrucción, notas de la cuadrilla. Los registros de campo son concisos por necesidad, y un oficial experimentado puede adivinar la siguiente línea con solo el contexto. Un **modelo de lenguaje** hace lo mismo, solo que aprende esas adivinanzas contando patrones en texto. Este capítulo construye ese contador con solo la biblioteca estándar de Python: dividir en tokens, contar transiciones y predecir lo que tiende a seguir.

## Leer sin palabras

Un LLM no lee las frases como una persona. Lee **tokens**: fragmentos de texto que pueden ser palabras completas, partes de palabras o signos de puntuación. La división afecta lo que el modelo puede razonar, así que merece la pena observar el tokenizador en acción en lugar de darlo por invisible.

```python
import re

def tokenizar(texto):
    return re.findall(r'\w+|[^\w\s]', texto)

print(tokenizar("Poste-7 informa niebla en la puerta del relevo."))
```

## Salida

```text
['Poste-7', 'informa', 'niebla', 'en', 'la', 'puerta', 'del', 'relevo', '.']
```

> [!NOTE]
> Los identificadores con guion suelen mantenerse juntos según el patrón. La puntuación se convierte en un token aparte. Distintos modelos toman decisiones distintas; lo importante es que la *unidad de predicción* es el token, no la palabra entera.

## Bigramas: qué sigue a qué

Una vez tokenizado el texto, el predictor más sencillo mira **bigramas** (pares de tokens consecutivos). Se cuenta con qué frecuencia el token B sigue al token A. Cuando ve A en un nuevo informe, puede sugerir el B que más veces apareció después de A en los registros conocidos. No es comprensión, es frecuencia.

```python
def obtener_bigramas(tokens):
    return [tokens[i] + ' ' + tokens[i + 1] for i in range(len(tokens)-1)]

registro = tokenizar("Poste-3 informa niebla. Poste-3 informa viento.")
print(obtener_bigramas(registro))
```

## Salida

```text
['Poste-3 informa', 'informa niebla', 'niebla .', '. Poste-3', 'Poste-3 informa', 'informa viento', 'viento .']
```

## Contar transiciones

Un predictor útil guarda un mapa del token actual a la lista de tokens que le siguieron. Con suficientes registros de campo, las transiciones comunes suben a la cima. No hace falta un modelo enorme para ilustrar el mecanismo: basta con frases coherentes.

```python
from collections import defaultdict

corpus = [
    "Poste-3 informa niebla cerca de la puerta.",
    "Poste-3 informa niebla cerca del mástil.",
    "Poste-7 informa viento cerca de la puerta.",
    "Poste-7 informa granizo cerca del mástil.",
]

def entrenar_bigramas(corpus):
    modelo = defaultdict(list)
    for linea in corpus:
        tokens = tokenizar(linea)
        for i in range(len(tokens)-1):
            modelo[tokens[i]].append(tokens[i+1])
    return modelo

m = entrenar_bigramas(corpus)
print(m['Poste-3'])
print(m['informa'])
```

## Salida

```text
['informa', 'informa']
['niebla', 'niebla', 'viento', 'granizo']
```

> [!WARNING]
> Un predictor puramente bigrama solo recuerda el último token. No sabe si «Poste-3» ya informó niebla dos veces ni mantiene coherencia en un informe largo: solo conoce transiciones locales. Ese punto ciego conviene observarlo en esta lección.

## Predecir un informe

Con los conteos, la estrategia más simple es elegir el siguiente token más frecuente para el actual. En notas de campo de Verdant Relay esto suele producir un fragmento plausible, y con la misma frecuencia algo repetitivo o erróneo cuando se acaba el contexto.

```python
def predecir_siguiente(modelo, token):
    opciones = modelo[token]
    if not opciones:
        return '.'
    return max(set(opciones), key=opciones.count)

actual = 'Poste-3'
salida = [actual]
for _ in range(4):
    actual = predecir_siguiente(m, actual)
    salida.append(actual)
print(' '.join(salida))
```

## Salida

```text
Poste-3 informa niebla cerca
```

## Por qué importa

Construir este contador a mano deja tres cosas claras. Primero, **los tokens son la unidad**. Segundo, **la predicción es estadística**: «el más común» es una suposición, no un razonamiento. Tercero, **el alcance lo es todo**: un predictor entrenado con informes de puerta adivinará distinto que uno con reparaciones de mástil. La fluidez de un modelo grande viene de la escala y el entrenamiento, pero la idea central es exactamente este recuento. Hay que tenerlo presente en el resto del módulo de Verdant Relay.

> [!TIP]
> Traza el bucle de bigramas a mano con una línea corta antes de seguir. Si ves qué par genera qué conteo, entenderás por qué se llama predicción del siguiente token.

