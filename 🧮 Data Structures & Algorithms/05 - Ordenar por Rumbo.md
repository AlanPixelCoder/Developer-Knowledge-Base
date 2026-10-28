
# 05. Ordenar por Rumbo

**Versión original en inglés:** [05 - Sort by Bearing](./05%20-%20Sort%20by%20Bearing.md)

**Curso:** Estructuras de Datos y Algoritmos
**Capítulo:** 5 — El Banco de Archivo
**Tema:** Ordenamiento por selección, in situ, bucles anidados, intercambios, O(n²), conteo de comparaciones
**Etiquetas:** `#dsa` `#sorting` `#selection-sort` `#complexity`

Cuando las cajas llegan a tierra en desorden, el atraque con estante no sirve. El Reconocimiento dispone de un banco de archivo justo para eso: sacar la caja más pequeña (o más ligera, o con menor número de rumbo) del montón desordenado y colocarla al frente de la sección ordenada. Se va construyendo esa sección ordenada poco a poco, in situ, hasta que todo el montón quede archivado en orden. Ese trabajo metódico es el **ordenamiento por selección** (*Selection Sort*). No es el más rápido, pero sí el más fácil de seguir paso a paso, lo que lo hace ideal para aprender qué hace realmente un algoritmo de ordenación.

## La distribución del banco

Hay que pensar en la lista como dos zonas que se van acercando: un **prefijo ordenado** a la izquierda y un **sufijo desordenado** a la derecha. Se empieza con prefijo vacío y todo desordenado. En cada pasada se recorre el sufijo desordenado para hallar el **mínimo**, se intercambia con el primer elemento de ese sufijo y se amplía el prefijo ordenado en uno.

```python
# Intuición por posiciones
montón = [42, 17, 55, 9, 31]
# pasada 1: mínimo en toda la lista -> 9 en índice 3, intercambiar con índice 0 -> [9, 17, 55, 42, 31]
# pasada 2: mínimo en sufijo desde 1 -> 17 ya está, sin intercambio
# pasada 3: mínimo en sufijo desde 2 -> 31 en índice 4, intercambiar con índice 2 -> [9, 17, 31, 42, 55]
print([9, 17, 31, 42, 55])
```

## Salida

```text
[9, 17, 31, 42, 55]
```

> [!NOTE]
> El ordenamiento por selección **selecciona** el mínimo (o máximo) de la parte desordenada y lo coloca en su sitio. No hace burbujas adyacentes como el *bubble sort*; busca el índice del mínimo y lo intercambia directamente con el límite. Ahí está su característica definitoria.

## Seguirlo paso a paso

Trazamos `[64, 25, 12, 22, 11]` con cuidado, viendo la búsqueda del mínimo y el intercambio.

**Pasada 1 (desde índice 0):** se recorren 64,25,12,22,11 -> mínimo 11 en índice 4. Intercambiar 0 y 4: `[11, 25, 12, 22, 64]`. Prefijo ordenado de longitud 1.

**Pasada 2 (desde índice 1):** se recorren 25,12,22,64 -> mínimo 12 en índice 2. Intercambiar 1 y 2: `[11, 12, 25, 22, 64]`. Prefijo ordenado de longitud 2.

**Pasada 3 (desde índice 2):** se recorren 25,22,64 -> mínimo 22 en índice 3. Intercambiar 2 y 3: `[11, 12, 22, 25, 64]`. Prefijo ordenado de longitud 3.

**Pasada 4 (desde índice 3):** se recorren 25,64 -> el mínimo 25 ya está en el índice 3, sin intercambio. El prefijo ordenado llega a 4 y el único elemento restante cierra la lista.

```python
montón = [64, 25, 12, 22, 11]
print("final:", [11, 12, 22, 25, 64])
```

## Salida

```text
final: [11, 12, 22, 25, 64]
```

> [!WARNING]
> No confundir «buscar la posición del mínimo» con «intercambiar adyacentes». El ordenamiento por selección halla el *índice* del mínimo en la región desordenada y lo intercambia directamente con el límite. Ese intercambio directo es lo que lo define.

## Implementación

El código refleja el banco: el bucle exterior fija el límite `i` (inicio de lo desordenado); el interior recorre de `i+1` al final para hallar `min_idx`; si es distinto, se intercambian `montón[i]` y `montón[min_idx]`.

```python
def ordenamiento_seleccion(montón):
    n = len(montón)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if montón[j] < montón[min_idx]:
                min_idx = j
        if min_idx != i:
            montón[i], montón[min_idx] = montón[min_idx], montón[i]
    return montón

rumbos = [42, 17, 55, 9, 31]
print(ordenamiento_seleccion(rumbos[:]))
```

## Salida

```text
[9, 17, 31, 42, 55]
```

> [!TIP]
> Pasar `rumbos[:]` crea una copia para no mutar la lista original al probar — útil cuando se trazan varios algoritmos sobre el mismo montón.

## Contar comparaciones para ver la factura

El ordenamiento por selección hace siempre el mismo número de comparaciones, esté el montón ya ordenado o completamente invertido, porque recorre toda la región desordenada en cada pasada para hallar el mínimo. Esto lo diferencia de algunos otros algoritmos.

```python
def conteo_comparaciones_seleccion(montón):
    n = len(montón)
    comparaciones = 0
    arr = montón[:]
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparaciones

print(conteo_comparaciones_seleccion([1,2,3,4,5]))
print(conteo_comparaciones_seleccion([5,4,3,2,1]))
```

## Salida

```text
10
10
```

Para n=5 son 4+3+2+1 = 10. En general, comparaciones = n*(n-1)/2 independientemente del orden inicial. Los intercambios son como mucho n-1.

## Complejidad: razonamiento exacto

- **Tiempo (comparaciones):** Mejor, promedio y peor caso dan **O(n²)** porque el bucle interior recorre siempre todo el sufijo restante. El hecho de que ya esté ordenado no acelera el ordenamiento por selección.
- **Tiempo (intercambios):** O(n) en total (como mucho n-1 intercambios).
- **Espacio:** **O(1)** extra — se ordena in situ sobre la misma lista.
- **Estabilidad:** El ordenamiento por selección **no es estable** por defecto; al intercambiar un mínimo lejano pueden cambiar las posiciones relativas de elementos iguales.

> [!CAUTION]
> El número de comparaciones lo fija n, no el orden. Si un algoritmo se jacta de ser «más rápido» con datos ya ordenados, el ordenamiento por selección no lo cumple. Esa previsibilidad es útil para razonar sobre el peor caso aunque no sea óptimo.

## Cuándo usarlo en el banco

El ordenamiento por selección brilla como herramienta didáctica: cada paso es visible, el invariante («todo a la izquierda de i está ordenado y en su sitio definitivo») se mantiene fácilmente y el coste se puede enunciar con exactitud. En la práctica, para n grande se prefieren otros algoritmos, pero para n pequeño o cuando conviene minimizar intercambios, merece conocerse. El Reconocimiento lo valora porque se puede trazar en el banco sin ordenador para detectar errores de lógica.

```python
# Montón pequeño, trazar a mano es el objetivo
pequeño = [3, 1, 4, 1, 5, 9]
ordenado_pequeño = ordenamiento_seleccion(pequeño[:])
print(ordenado_pequeño)
```

## Salida

```text
[1, 1, 3, 4, 5, 9]
```

> [!TIP]
> Conviene tener siempre el invariante presente: tras la pasada i, los primeros i+1 elementos son los i+1 más pequeños en orden y ya no se moverán. Si el trazo rompe ese invariante, se ha encontrado un error. Con ese invariante, el ordenamiento por selección es difícil de equivocar.

