
# 04. Dividir el Manifiesto

**Versión original en inglés:** [04 - Split the Manifest](./04%20-%20Split%20the%20Manifest.md)

**Curso:** Estructuras de Datos y Algoritmos
**Capítulo:** 4 — Los Atraques con Estante
**Tema:** Divide y vencerás, búsqueda binaria, iterativa/recursiva, casos límite, O(log n)
**Etiquetas:** `#dsa` `#binary-search` `#divide-and-conquer` `#complexity`

Un muelle solo puede albergar tantas cajas al aire libre antes de que la marea se las trague. El Reconocimiento archiva la carga de movimiento lento en **atraques con estante**: ranuras numeradas por número de caja, en orden estricto a lo largo de la pared. Una vez ordenado el estante, buscar la Caja-42 ya no significa abrir todas las ranuras. Significa situarse en el medio, leer una etiqueta y descartar de un golpe todo un ala del estante. Ese hábito es la **búsqueda binaria**: dividir, descartar, repetir.

## Por qué el orden es la palanca

La búsqueda binaria solo funciona si la lista está **ordenada** por la clave que se busca. La razón es simple: si se conoce el valor central `M` y el objetivo `T < M`, en una lista ascendente ningún elemento a la derecha de `M` puede ser menor que `M`, así que si `T` existe no puede estar ahí. Se paga el orden por adelantado para tener esa garantía en todas las búsquedas posteriores.

```python
estante = [5, 9, 17, 31, 42, 55, 64, 77]
# ordenado ascendentemente por número de caja
print(estante)
```

## Salida

```text
[5, 9, 17, 31, 42, 55, 64, 77]
```

> [!NOTE]
> El orden es un requisito, no una optimización que se añada a mitad de búsqueda. Si el estante está desordenado, descartar mitades es inseguro y el algoritmo deja de ser correcto.

## Partir a mano

Tomemos `objetivo = 42` en ese estante (índices 0-7). Medio: `(0+7)//2 = 3`, valor `31`. `42 > 31`, se descarta la mitad izquierda incluyendo el medio; `izquierda = 4`. Rango [4,7], medio `(4+7)//2 = 5`, valor `55`. `42 < 55`, se descarta la mitad derecha; `derecha = 4`. Rango [4,4], medio 4, valor `42` coincide — encontrado. Tres comprobaciones frente a las 5 que haría un barrido desde el frente.

```python
estante = [5, 9, 17, 31, 42, 55, 64, 77]
# trazo para 42: (0,7)->medio3 val31, ir a derecha (izq=4); (4,7)->medio5 val55, ir a izquierda (der=4); (4,4)->medio4 val42 == objetivo
print("encontrado en 3 pasos a mano")
```

## Búsqueda binaria iterativa

La forma iterativa usa dos punteros `izquierda` y `derecha`. Mientras `izquierda <= derecha`, se revisa el medio. Los punteros se acercan según la comparación. Si el intervalo colapsa (`izquierda > derecha`) sin encontrarlo, el objetivo no está en el estante.

```python
def busqueda_binaria(estante, objetivo):
    izquierda = 0
    derecha = len(estante) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if estante[medio] == objetivo:
            return medio
        elif objetivo < estante[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1

estante = [5, 9, 17, 31, 42, 55, 64, 77]
print(busqueda_binaria(estante, 42))
print(busqueda_binaria(estante, 7))
```

## Salida

```text
4
-1
```

> [!WARNING]
> Error común: poner `izquierda = medio` en lugar de `izquierda = medio + 1`, o `derecha = medio` en lugar de `derecha = medio - 1`. Si no se avanza más allá del medio, el intervalo no se reduce y el bucle puede quedar infinito. Siempre hay que mover el puntero más allá de `medio`.

## Búsqueda binaria recursiva

El mismo plan en forma recursiva: si el intervalo está vacío -> fallo; revisar el medio; si coincide -> devolver índice; si no, llamar recursivamente sobre la mitad superviviente. Si se usan valores por defecto, conviene pasar `izquierda/derecha` explícitamente para que el trazo a mano sea claro.

```python
def busqueda_binaria_rec(estante, objetivo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(estante) - 1
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if estante[medio] == objetivo:
        return medio
    elif objetivo < estante[medio]:
        return busqueda_binaria_rec(estante, objetivo, izquierda, derecha - 1)
    else:
        return busqueda_binaria_rec(estante, objetivo, izquierda + 1, derecha)

estante = [5, 9, 17, 31, 42, 55, 64, 77]
print(busqueda_binaria_rec(estante, 55))
```

## Salida

```text
5
```

> [!TIP]
> La iterativa usa O(1) de memoria extra (punteros). La recursiva usa O(log n) por la pila de llamadas (cada mitad añade un marco hasta el caso base). Ambas son correctas; conviene elegir por legibilidad y entorno, pero hay que conocer el intercambio.

## Contar frente al barrido lineal

La diferencia se ve al contar. Para 1000 ranuras ordenadas, la búsqueda binaria necesita como mucho ~10 comprobaciones; el barrido lineal necesita hasta 1000 en el peor caso. Para objetivos ausentes es aún más llamativo.

```python
def conteo_lineal(estante, objetivo):
    for i, v in enumerate(estante):
        if v == objetivo:
            return i + 1  # comprobaciones
    return len(estante)

def conteo_binario(estante, objetivo):
    izquierda, derecha, comprobaciones = 0, len(estante) - 1, 0
    while izquierda <= derecha:
        comprobaciones += 1
        medio = (izquierda + derecha) // 2
        if estante[medio] == objetivo:
            return comprobaciones
        elif objetivo < estante[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return comprobaciones

grande = [i for i in range(1000)]
print("lineal encuentra 999:", conteo_lineal(grande, 999))
print("binario encuentra 999:", conteo_binario(grande, 999))
print("binario ausente:", conteo_binario(grande, -1))
```

## Salida

```text
lineal encuentra 999: 1000
binario encuentra 999: 10
binario ausente: 10
```

## Complejidad y el precio del orden

- **Tiempo:** Mejor caso O(1) (encontrado en el medio de inmediato). Peor caso O(log n) (ausente o al final, partido hasta quedarse vacío). Promedio similar al peor en muchos casos prácticos.
- **Espacio:** Iterativa O(1); recursiva O(log n) por pila.
- **Coste inicial:** Para usar búsqueda binaria hay que tener la lista **ordenada** — ordenar suele ser O(n log n). Si solo se busca una vez, casi siempre es peor que un barrido O(n). Si se busca muchas veces, O(n log n) una vez + O(log n)*k suele compensar.

> [!CAUTION]
> Nunca apliques búsqueda binaria a una lista enlazada por indexación ingenua (sin acceso aleatorio) ni a una estructura desordenada esperando corrección. La garantía viene íntegramente del orden y del acceso aleatorio por índice.

