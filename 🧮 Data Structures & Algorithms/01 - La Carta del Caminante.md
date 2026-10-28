
# 01. La Carta del Caminante

**Versión original en inglés:** [01 - The Wayfarer Charter](./01%20-%20The%20Wayfarer%20Charter.md)

**Curso:** Estructuras de Datos y Algoritmos
**Capítulo:** 1 — El Reconocimiento
**Tema:** Líneas de suministro, estructura frente a procedimiento, coste al crecer el mapa
**Etiquetas:** `#dsa` `#data-structures` `#algorithms` `#fundamentals`

El Reconocimiento del Caminante traza costas fracturadas donde las ventanas de marea duran apenas unas horas. Con solo unas pocas chalupas, transportar cajas a ciegas no es heroico, es un desperdicio. La carta obliga a adquirir un hábito: antes de zarpar, hay que nombrar dos cosas para cada envío. Primero, *cómo* guardar la carga (una **estructura de datos**). Segundo, *en qué orden* actuar sobre ella (un **algoritmo**). Ninguno existe por separado; cambiar uno suele obligar a repensar el otro.

## Guardar la carga sin adivinar

Una estructura de datos no es un simple contenedor. Es una elección que hace barata una operación concreta y torpe otra a propósito. El Reconocimiento guarda los manifiestos en **listas** cuando el orden de carga importa y se espera recorrer el muelle de proa a popa. Una lista mantiene los elementos en secuencia y permite acceder por índice, pero no ofrece un atajo si se desconoce el número de caja.

```python
# Un manifiesto en el orden en que las cajas fueron izadas al muelle
muelle_manifiesto = ["Caja-17", "Caja-05", "Caja-42", "Caja-09"]
print("Primera en descargar:", muelle_manifiesto[0])
muelle_manifiesto.append("Caja-88")
print("Cantidad en muelle:", len(muelle_manifiesto))
print("Todas las cajas:", muelle_manifiesto)
```

## Salida

```text
Primera en descargar: Caja-17
Cantidad en muelle: 5
Todas las cajas: ['Caja-17', 'Caja-05', 'Caja-42', 'Caja-09', 'Caja-88']
```

La lista es honesta con su forma: para saber lo que hay en la posición dos no hay que leer todo el montón. Pero si la pregunta es «¿está la Caja-42 aquí?» y nadie apuntó su atraque, la lista no indicará dónde está. La estructura cumple con las posiciones conocidas, pero no acorta el caso de *posición desconocida*.

## Un plan con condición de parada

Un algoritmo es un plan finito. Ante una caja perdida sin índice, el caminante recurre a un **barrido lineal**: mirar el atraque 0, si no coincide mirar el 1, y así sucesivamente hasta encontrarla o agotar los atraques. Este plan es correcto para cualquier lista, no requiere ordenar y falla con elegancia: simplemente indica que no queda nada por revisar.

```python
def buscar_caja(manifiesto, objetivo):
    """Recorre de proa a popa. Devuelve el índice o -1 si falta."""
    for indice, caja in enumerate(manifiesto):
        if caja == objetivo:
            return indice
    return -1

atraques = ["Caja-17", "Caja-05", "Caja-42", "Caja-09"]
print("Caja-42 en atraque:", buscar_caja(atraques, "Caja-42"))
print("Caja-77 en atraque:", buscar_caja(atraques, "Caja-77"))
```

## Salida

```text
Caja-42 en atraque: 2
Caja-77 en atraque: -1
```

> [!NOTE]
> «Encontrarla» no es lo mismo que «¿dónde está?». El algoritmo anterior responde «¿dónde está, o decir que falta?». Explicitar la condición de parada («fin del manifiesto» equivale a fallo) importa tanto como la comparación; sin ella, el plan queda vago y difícil de seguir paso a paso.

## El coste se ve al crecer el mapa

La lección real de la carta es la escala. En un muelle corto revisar cinco cajas es trivial. En una red que cubre caletas con miles de ranuras, *cuántas comparaciones* se hacen es la factura. Un barrido lineal hace hasta *n* comprobaciones en el peor caso (la caja está al final o no está). Si la forma no cambia, duplicar el manifiesto tiende a duplicar esa factura en el peor caso.

```python
# Seguimiento manual para el peor caso
manifiesto = ["A1", "A2", "A3", "A4", "A5"]
# Buscar "A5": revisa 0,1,2,3,4 -> 5 comprobaciones
# Buscar "AUSENTE": revisa las 5 -> 5 comprobaciones, devuelve -1
print("longitud:", len(manifiesto))
```

> [!WARNING]
> Nunca confiar en que «fue rápido en mi prueba pequeña». El Reconocimiento siempre pide el peor caso para el tamaño plausible del mapa, porque la marea actúa sobre el peor caso, no sobre el mejor.

## La forma abre planes mejores

El orden cambia lo que es posible. Si las mismas cajas se archivan por número en lugar de por orden de carga, el caminante puede trazar un plan distinto: uno que descarte grandes trozos del estante sin inspeccionarlos. La estructura no se vuelve mágica por sí sola; ponerla en orden desbloquea un nuevo algoritmo. Ese intercambio (ordenar una vez, buscar distinto después) reaparece a lo largo de todo el módulo.

```python
como_cargado = [17, 5, 42, 9, 31]
archivado = sorted(como_cargado)
print("como cargado:", como_cargado)
print("archivado por número:", archivado)
```

## Salida

```text
como cargado: [17, 5, 42, 9, 31]
archivado por número: [5, 9, 17, 31, 42]
```

> [!TIP]
> La disciplina de la carta: (1) elegir una forma, (2) escribir un plan explícito, (3) seguirlo a mano con un ejemplo pequeño, (4) razonar sobre el peor caso al crecer la lista. Hacer eso antes de optimizar. La mayoría del código «lento» falla en el paso cuatro, no en el primero.

