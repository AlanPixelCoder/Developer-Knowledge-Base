
# 03. Índice del Prado

**Versión original en inglés:** [03 - Meadow Index](./03%20-%20Meadow%20Index.md)

**Curso:** GenAI
**Capítulo:** 3 — Relevo Verdoso
**Tema:** Embeddings, vectores, similitud, búsqueda semántica
**Etiquetas:** `#genai` `#embeddings` `#semantic-search` `#vectors` `#python`

Verdant Relay mantiene un pequeño prado de notas de relevo: antiguos informes de averías, reparaciones, piezas, ubicaciones. Una búsqueda por palabra clave de «niebla» encuentra informes que la mencionen, pero no «bruma» o «visibilidad reducida» aunque sean el mismo problema en un poste vecino. El campo necesita **búsqueda semántica**: encontrar notas por *significado*, no por coincidencia exacta. Esta lección construye la idea desde cero con listas y matemáticas: representar texto como vectores, medir el ángulo entre ellos y ordenar por similitud. No se asume llamar a un modelo preentrenado; conviene seguir cada paso.

## De palabras a conteos

Un punto de partida sencillo es la **bolsa de palabras** (*bag of words*, BoW). Se toma un vocabulario pequeño con términos que aparecen en las notas del prado y se representa cada nota como un vector que cuenta cuántas veces aparece cada término. Se pierde el orden, pero la coocurrencia da una forma aproximada del contenido.

```python
vocabulario = ["niebla", "bruma", "cable", "puerta", "mástil"]
# nota A
a = [1, 0, 0, 1, 0]  # niebla, puerta
# nota B
b = [0, 1, 0, 1, 0]  # bruma, puerta
print("a:", a)
print("b:", b)
```

## Salida

```text
a: [1, 0, 0, 1, 0]
b: [0, 1, 0, 1, 0]
```

Estos vectores difieren en dos posiciones, pero ambas tratan de visibilidad en la puerta. Una búsqueda por coincidencia exacta diría «distintos», cuando semánticamente están cerca.

> [!NOTE]
> La bolsa de palabras ignora orden y gramática. Para notas cortas de campo es un juguete didáctico: muestra que la *representación* es el problema. Los embeddings reales hacen esto con vectores mucho mayores y aprendidos, capturando relaciones como que «bruma» y «niebla» están cerca.

## Medir la similitud

Para comparar vectores se usa la **similitud coseno**. Mira el ángulo entre vectores, no su longitud. Dos notas que apuntan más o menos en la misma dirección son similares aunque una sea más larga. Fórmula: $\cos(\theta)=\frac{A\cdot B}{\|A\|\|B\|}$.

```python
import math

def producto_punto(a,b):
    return sum(x*y for x,y in zip(a,b))

def norma(v):
    return math.sqrt(sum(x*x for x in v))

def coseno(a,b):
    d = producto_punto(a,b)
    if d == 0: return 0.0
    return d / (norma(a)*norma(b))

print(coseno(a,b))
```

## Salida

```text
0.5
```

Ambas comparten «puerta», producto punto 1, normas sqrt(2), resultado 0.5. Ángulo 60 grados: ni idénticas ni ortogonales. Para este vocabulario diminuto encaja con la intuición.

## Un índice del prado

Se construye un índice con notas y sus vectores sobre el vocabulario. Dada una consulta, se vectoriza igual y se ordena por similitud coseno descendente.

```python
notas = [
    ("N1", "niebla en la puerta", [1,0,0,1,0]),
    ("N2", "bruma en la puerta", [0,1,0,1,0]),
    ("N3", "cable suelto en el mástil", [0,0,1,0,1]),
]
consulta = "bruma baja cerca de la puerta"
qv = [0,1,0,1,0]
for nid, texto, v in notas:
    print(nid, coseno(qv,v), texto)
```

## Salida

```text
N1 0.5 niebla en la puerta
N2 1.0 bruma en la puerta
N3 0.0 cable suelto en el mástil
```

Con coincidencias exactas, «bruma en la puerta» queda primero. En la práctica los embeddings reales también subirían «niebla en la puerta» porque los embeddings aprendidos sitúan niebla/bruma cerca — la idea clave es la misma: comparar vectores en un espacio compartido.

> [!WARNING]
> Este BoW + coseno es un juguete. Falla con sinónimos fuera del vocabulario, orden de palabras y negaciones. Los embeddings reales corrigen parte, pero también se equivocan. Lo que importa es el mecanismo (vector + similitud).

## Por qué ayuda la búsqueda semántica

La búsqueda por palabra clave es frágil con notas tersas escritas por cuadrillas cansadas. «Cable guía» frente a «cable», «cimiento» frente a «base», «obstrucción» frente a «bloqueo». La búsqueda semántica ordena por significado, así que una nota sobre un desagüe obstruido puede aparecer para «desagüe bloqueado» aunque los tokens no coincidan. El intercambio: hace falta una representación, la similitud es calculable, pero siempre conviene revisar los resultados con sentido crítico.

> [!TIP]
> No empezar preguntando por «búsqueda con IA». Preguntar: «Si tuviera vectores de estas notas, ¿cuáles tres estarían más cerca de esta consulta por ángulo?». Si se puede responder con el coseno, se entiende la búsqueda semántica al nivel de este módulo.
