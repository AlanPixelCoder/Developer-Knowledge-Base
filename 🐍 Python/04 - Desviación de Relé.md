<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 04 - Desviación de Relé

**Versión original en inglés:** [04 - Relay Drift](./04%20-%20Relay%20Drift.md)

![Status Badge](https://img.shields.io/badge/Topic-Lists-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 2 — Datos y Estado
**Tema:** Listas, Indexación, Rebanado, Funciones integradas, Métodos, Iteración
**Etiquetas:** `#python` `#telemetria` `#listas` `#estructuras-datos` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Colas de Lecturas

Un solo volcado de una baliza no dice mucho, pero un lote de cinco balizas a lo largo de una ventana de marea sí cuenta una historia. Las listas almacenan colecciones ordenadas en una sola variable, escritas con corchetes `[]` y elementos separados por comas. Pueden mezclar tipos, admitir repeticiones y crecer o reducirse sin tamaños fijos.

```python
# Lecturas recientes de VR-07 (rssi en dBm)
rssi = [-62, -65, -71, -68, -64]
estaciones = ["VR-07", "VR-09", "VR-12", "VR-14"]
```

## Indexación y Rebanado

Los elementos son de base cero. Los índices negativos cuentan desde el final: `-1` es el último elemento. El rebanado `inicio:fin` incluye el inicio y excluye el fin. Nunca modifica la lista original — devuelve una nueva vista.

```python
rssi = [-62, -65, -71, -68, -64]
print(rssi[0])     # -62
print(rssi[-1])    # -64
print(rssi[1:4])   # [-65, -71, -68]
print(rssi[:3])    # [-62, -65, -71]
print(rssi[3:])    # [-68, -64]
```

## Salida

```text
-62
-64
[-65, -71, -68]
[-62, -65, -71]
[-68, -64]
```

Acceder fuera de rango genera `IndexError`. Si un índice proviene de una posición calculada, conviene validarlo o protegerlo en lugar de dejar que el script falle con un lote parcial.

> [!NOTE]
> El rebanado devuelve una lista incluso si está vacía o tiene un solo elemento. Esa coherencia suele ser más segura que intentar tratar un escalar como caso especial.

## Estadísticas Rápidas con Funciones Integradas

Para una auditoría rápida, las funciones integradas de Python cubren lo necesario: `len()`, `max()`, `min()`, `sum()`. Combinadas, permiten detectar desviaciones sin escribir bucles.

```python
rssi = [-62, -65, -71, -68, -64]
print(len(rssi))
print(min(rssi))  # señal más débil
print(max(rssi))  # señal más fuerte
print(sum(rssi))
```

## Salida

```text
5
-71
-62
-330
```

En RSSI, «más fuerte» significa más cercano a cero. Que `min()` devuelva `-71` identifica correctamente el enlace más débil en ese lote: las funciones integradas hacen exactamente lo que dicen sus nombres, pero la interpretación siempre depende de la métrica.

## Dar Forma a la Cola

Los métodos de lista modifican la lista in situ. Es importante saber cuáles mutan: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()` cambian la original; `copy()` hace una copia superficial.

| Método | Efecto |
| :--- | :--- |
| `.append(x)` | Añade al final |
| `.insert(i,x)` | Inserta en un índice |
| `.extend(lst)` | Añade todos los elementos de otra lista |
| `.remove(x)` | Elimina la primera coincidencia |
| `.pop([i])` | Elimina y devuelve en un índice (o al final) |
| `.clear()` | Vacía la lista |
| `.index(x)` | Busca el primer índice |
| `.count(x)` | Cuenta apariciones |
| `.sort()` | Ordena in situ |
| `.reverse()` | Invierte in situ |
| `.copy()` | Copia superficial |

```python
pendientes = ["VR-07", "VR-09"]
pendientes.append("VR-12")
pendientes.insert(1, "VR-14")
pendientes.remove("VR-09")
print(pendientes)
```

## Salida

```text
['VR-07', 'VR-14', 'VR-12']
```

## Recorrer el Lote

Para procesar cada elemento, se itera directamente con `for`. Si también se necesitan los índices (por ejemplo, para registrar «lectura 3 de 5»), se usa `range(len(lista))`.

```python
rssi = [-62, -65, -71, -68, -64]
for val in rssi:
    print(f"RSSI {val} dBm")
```

## Salida

```text
RSSI -62 dBm
RSSI -65 dBm
RSSI -71 dBm
RSSI -68 dBm
RSSI -64 dBm
```

> [!WARNING]
> `remove()` borra solo la primera aparición. Si pueden haber duplicados (por ejemplo, IDs de baliza duplicados en un lote confuso), conviene comprobar con `count()` o filtrar explícitamente.

### Tarea 4: Cola de Desviación

Crea una lista `balizas = ["VR-07", "VR-09", "VR-12"]`. Añade `VR-14` con `append()`, inserta `VR-05` en el índice 0, elimina `VR-09`, luego imprime la lista y su longitud con `len()`.
