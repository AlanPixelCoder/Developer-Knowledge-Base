
# 03. Cajas en la Cola

**Versión original en inglés:** [03 - Crates in the Queue](./03%20-%20Crates%20in%20the%20Cola.md)

**Curso:** Estructuras de Datos y Algoritmos
**Capítulo:** 3 — El Muelle
**Tema:** Listas, indexación, rebanado, métodos, barrido lineal a mano
**Etiquetas:** `#dsa` `#lists` `#linear-search` `#python`

El muelle no descarga al azar. El cabrestante trae las cajas a tierra en un orden concreto y los caminantes forman una cola al ritmo de la marea. Si se conoce el lugar de cada caja, coger la siguiente es instantáneo. Si alguien grita «buscar Caja-42» y nadie ha marcado su posición, el único recurso honesto para una cola sin ordenar es recorrerla desde el frente hasta encontrarla. Esta lección trata las listas de Python como la cola del muelle y sigue un barrido lineal línea a línea hasta que quede claro.

## Una cola que se puede contar

Una **lista** guarda elementos en secuencia, con índice `0` al frente. La **indexación** lee un atraque conocido sin tocar el resto; el **rebanado** extrae un tramo contiguo para inspeccionarlo. No son detalles: con la marea justa, leer un índice equivocado es lo mismo que abrir la caja equivocada.

```python
cola = ["Caja-17", "Caja-05", "Caja-42", "Caja-09", "Caja-88"]
print("Frente:", cola[0])
print("Tercera:", cola[2])
print("Primeras tres:", cola[0:3])  # el final es exclusivo
print("Desde índice 2:", cola[2:])
```

## Salida

```text
Frente: Caja-17
Tercera: Caja-42
Primeras tres: ['Caja-17', 'Caja-05', 'Caja-42']
Desde índice 2: ['Caja-42', 'Caja-09', 'Caja-88']
```

Fíjate en el rebanado: `cola[0:3]` devuelve los índices 0,1,2 pero no el 3. Ese desajuste por uno se olvida con facilidad; es mejor contar a mano frente a la salida que adivinarlo.

## Mover cajas por el muelle

La cola cambia durante el turno. Llegan nuevas cajas (`append`), alguna prioritaria puede colarse en medio (`insert`), una dañada se retira (`pop`) y el capitán necesita el recuento (`len`). Cada mutación desplaza las posiciones tras el punto de cambio — conviene recordarlo si se habían anotado índices con anterioridad.

```python
cola = ["Caja-17", "Caja-05", "Caja-42"]
cola.append("Caja-88")        # añadir al final
cola.insert(1, "Caja-91")     # insertar en índice 1
retirada = cola.pop()         # quitar del final
print("Retirada:", retirada)
print("Cola ahora:", cola)
print("Longitud:", len(cola))
```

## Salida

```text
Retirada: Caja-88
Cola ahora: ['Caja-17', 'Caja-91', 'Caja-05', 'Caja-42']
Longitud: 4
```

> [!CAUTION]
> Tras `insert` o `pop` al frente o en medio, todos los elementos posteriores se desplazan ±1. Si se guardó un índice antes de la mutación, es muy posible que ahora apunte a otra caja. En el muelle, no hay que fiarse de un índice guardado tras reordenar la cola.

## Recorrer la cola a mano

Sin índice conocido, el plan es mecánico: empezar en índice 0, comparar, incrementar, repetir hasta encontrarla o `índice == len(cola)`. Esto es la **búsqueda lineal**. No supone ningún orden y funciona con cualquier lista de valores comparables. Su coste en el peor caso crece con la longitud, como se vio en la lección anterior.

```python
def buscar_lineal(cola, objetivo):
    """Devuelve el índice o -1."""
    for i in range(len(cola)):
        if cola[i] == objetivo:
            return i
    return -1

cola = ["Caja-17", "Caja-05", "Caja-42", "Caja-09"]
print(buscar_lineal(cola, "Caja-42"))
print(buscar_lineal(cola, "Caja-77"))
```

## Salida

```text
2
-1
```

## Seguirlo paso a paso hasta que cale

Para ver la factura conviene trazarlo explícitamente. Para `objetivo = "Caja-09"` en esa cola: i=0 -> "Caja-17"!=objetivo; i=1 -> no; i=2 -> no; i=3 -> coincide, devuelve 3. Han pasado tres comprobaciones antes de encontrarla; si falta, cuatro comprobaciones y se devuelve -1. Merece la pena escribir ese trazo un momento: seguir a mano enseña más que memorizar la definición.

```python
cola = ["Caja-17", "Caja-05", "Caja-42", "Caja-09"]
objetivo = "Caja-09"
# trazo manual:
# i=0: Caja-17==Caja-09? no
# i=1: Caja-05==Caja-09? no
# i=2: Caja-42==Caja-09? no
# i=3: Caja-09==Caja-09? sí -> devuelve 3
print("respuesta:", 3)
```

> [!NOTE]
> `range(len(cola))` es muy común aquí: da índices válidos sin riesgo de salir fuera y encaja bien con `cola[i]`. Solo conviene iterar sobre valores si realmente no se necesita el índice.

## Cuándo sí conviene la búsqueda lineal

La búsqueda lineal no es «perezosa», es correcta por defecto. Si la cola está desordenada y se busca pocas veces, suele ser el plan más honesto y directo. Si se buscan los mismos números constantemente, el Reconocimiento prefiere archivar (cambiar la forma) antes que hacer más barridos. La elección es cuestión de ajuste: plan acorde a la forma y a la frecuencia, no al orgullo.

```python
# Cola desordenada: la búsqueda lineal es la respuesta directa
manifiesto = ["Red", "Cuerda", "Aceite de farol", "Caja-42", "Brea"]
encontrado = buscar_lineal(manifiesto, "Caja-42")
print("Caja-42 en:", encontrado)
```

> [!TIP]
> En el muelle, primero la corrección. Consigue un barrido lineal que devuelva el índice o -1, trázalo a mano en dos casos (encontrado y ausente), y solo después cuenta el peor caso. Esos tres pasos evitan la mayoría de errores por uno y de lógica.

