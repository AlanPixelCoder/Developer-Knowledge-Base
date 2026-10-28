
# 02. Contando la Marea

**Versión original en inglés:** [02 - Tallying the Tide](./02%20-%20Tallying%20the%20Tide.md)

**Curso:** Estructuras de Datos y Algoritmos
**Capítulo:** 2 — Coste
**Tema:** Tiempo/espacio, Big O, tabla de crecimiento, lineal frente a búsqueda
**Etiquetas:** `#dsa` `#big-o` `#complexity` `#algorithms`

La marea no se fija en los segundos del reloj del caminante, sino en el recuento: ¿cuántas veces se detuvo la chalupa en un atraque, cuántas comparaciones antes de seguir? Para el Reconocimiento del Caminante, **eficiencia** significa responder «¿cómo se comporta este plan al crecer *n*?» y no «¿qué rápido fue en este muelle concreto?». Ese cambio de pregunta es justo lo que justifica el análisis de complejidad.

## Medir el trabajo, no los segundos

Al seguir un plan a mano conviene contar las operaciones que escalan. En un barrido lineal, la comparación `caja == objetivo` es la que se multiplica al crecer el manifiesto. Una prueba corta puede parecer instantánea, pero el peor caso es el que hace perder la ventana de marea.

```python
def barrido_con_conteo(manifiesto, objetivo):
    """Cuenta las comparaciones para ver la factura."""
    comprobaciones = 0
    for caja in manifiesto:
        comprobaciones += 1
        if caja == objetivo:
            return comprobaciones
    return comprobaciones

atraques = ["Caja-17", "Caja-05", "Caja-42", "Caja-09", "Caja-31"]
print("Encontrar Caja-31 en comprobaciones:", barrido_con_conteo(atraques, "Caja-31"))
print("Falta Caja-00 en comprobaciones:", barrido_con_conteo(atraques, "Caja-00"))
```

## Salida

```text
Encontrar Caja-31 en comprobaciones: 5
Falta Caja-00 en comprobaciones: 5
```

Con 5 elementos, el peor caso son 5 comprobaciones. El patrón: en el peor caso, un barrido lineal hace **hasta *n* comparaciones** para una lista de longitud *n*.

> [!NOTE]
> La complejidad temporal describe el crecimiento de pasos al crecer *n*. La complejidad espacial describe el crecimiento de memoria extra al crecer *n*. Aquí nos centramos sobre todo en el tiempo, pero ambas importan cuando el equipo es limitado.

## Big O como mapa de crecimiento

La **notación Big O** da la forma del límite superior. Se ignoran constantes y términos menores porque la pregunta es «¿a qué familia pertenece?» no «¿exactamente 17 comprobaciones este martes?». Para el barrido lineal, la familia es **O(n)** (se lee «orden n»).

| n (atraques) | Peor caso (O(n)) | Impresión |
| :--- | :--- | :--- |
| 5 | 5 | trivial |
| 50 | 50 | aún fácil a mano |
| 500 | 500 | más lento para seguir, fácil de automatizar mal |
| 5.000 | 5.000 | puede perder ventanas de marea si se hace a ciegas |

Si *n* se duplica, O(n) se duplica aproximadamente. Ese crecimiento lineal es el precio de un plan que no requiere orden.

## Una forma mejor: partir el estante

Si el manifiesto está **ordenado por número de caja** en un estante ranurado, aparece otro plan. Se mira la ranura central: si coincide, se para. Si el objetivo es menor que la caja central, no puede estar en la mitad derecha — se descarta toda la mitad derecha y se busca en la izquierda. Si es mayor, se descarta la izquierda y se busca en la derecha. Se repite, partiendo el estante restante cada vez. Esto es la **búsqueda binaria** y su crecimiento en el peor caso es **O(log n)**.

```python
def busqueda_binaria_conteo(ordenado, objetivo):
    """Búsqueda binaria con contador de comprobaciones."""
    izquierda = 0
    derecha = len(ordenado) - 1
    comprobaciones = 0
    while izquierda <= derecha:
        comprobaciones += 1
        medio = (izquierda + derecha) // 2
        if ordenado[medio] == objetivo:
            return comprobaciones
        elif objetivo < ordenado[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return comprobaciones

estante = [5, 9, 17, 31, 42, 55, 64, 77, 88, 99]
print("Buscar 5 (primero):", busqueda_binaria_conteo(estante, 5), "comprobaciones")
print("Buscar 99 (último):", busqueda_binaria_conteo(estante, 99), "comprobaciones")
print("Buscar 7 (ausente):", busqueda_binaria_conteo(estante, 7), "comprobaciones")
```

## Salida

```text
Buscar 5 (primero): 4
Buscar 99 (último): 4
Buscar 7 (ausente): 4
```

Para 10 elementos, extremos y ausente toman como mucho ~4 comprobaciones porque $2^4 = 16 >= 10$. Para 1000, ~10; para 1.000.000, ~20. Partir domina con creces al crecimiento lineal.

> [!WARNING]
> La búsqueda binaria solo es correcta si el estante está **ordenado** por la clave que se busca. Si la lista no está ordenada, descartar mitades es falso: la mitad descartada podría contener el objetivo. El orden es un requisito, no un detalle.

## Tabla de crecimiento: ver la diferencia

| n | Peor caso O(n) (lineal) | Peor caso O(log₂ n) (binaria) |
| :--- | :--- | :--- |
| 10 | 10 | ~4 |
| 100 | 100 | ~7 |
| 1.000 | 1.000 | ~10 |
| 10.000 | 10.000 | ~14 |
| 1.000.000 | 1.000.000 | ~20 |

La diferencia no está en n pequeño, sino en la curva: la lineal sube recta, la logarítmica apenas sube. Ahí está la razón por la que el Reconocimiento archiva por número cuando hay búsquedas frecuentes.

## El intercambio en la práctica

La velocidad no es gratis. Ordenar *n* elementos con un algoritmo de comparación cuesta aproximadamente **O(n log n)** en el peor caso. Si solo se busca una vez, pagar O(n log n) por ordenar más O(log n) por buscar puede ser peor que un único barrido O(n). Si se busca *cientos* de veces contra el mismo estante ordenado, pagar O(n log n) una vez y O(log n) por búsqueda suele salir mucho mejor. La eficiencia depende siempre del *contexto* (cuántas veces, sobre qué forma), no hay un ganador universal.

```python
# El contexto decide la ruta
# Una búsqueda en desorden: lineal ~n
# Muchas búsquedas en ordenado: ordenar ~n log n + (búsquedas * log n)
print("el contexto decide la ruta")
```

> [!TIP]
> No memorices constantes. Memoriza familias e intercambios. Pregunta: «¿Está ordenada esta forma? ¿Cuántas búsquedas? ¿Puedo permitirme ordenar una vez?». Esas tres preguntas dicen más que cronometrar una única ejecución.

