<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 05 - Pila de Tormenta

**Versión original en inglés:** [05 - Storm Stack](./05%20-%20Storm%20Stack.md)

![Status Badge](https://img.shields.io/badge/Topic-Data%20Structures-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 2 — Datos y Estado
**Tema:** Listas anidadas, Matrices, Diccionarios, Conjuntos
**Etiquetas:** `#python` `#telemetria` `#diccionarios` `#conjuntos` `#matrices` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Apilando por Zonas

Cuando llega una tormenta costera, las lecturas llegan por zonas: cada zona tiene una lista de balizas y cada baliza tiene una lista de lecturas de canales. Una **lista anidada** coloca listas dentro de una lista. Si las filas tienen la misma longitud, se convierte en una estructura 2D (matriz) fácil de indexar con `[fila][col]`.

```python
# Cuadrícula de zonas: filas = zonas, columnas = balizas
estado_malla = [
    ["OK", "OK", "BAJO"],
    ["OK", "DESVIO", "OK"],
    ["CAIDO", "OK", "AVISO"]
]
# Zona 2, baliza 0
print(estado_malla[2][0])  # CAIDO
```

## Profundizar en Datos Anidados

El acceso va de fuera hacia dentro. Si los datos son irregulares, conviene comprobar la longitud antes de indexar para evitar `IndexError`.

```python
lote_registros = [
    ["VR-07", [-62, -65, -71]],
    ["VR-09", [-58, -60]],
    ["VR-12", [-70, -69, -72, -68]]
]
# Último rssi de VR-12
print(lote_registros[2][1][-1])  # -68
```

## Diccionarios para Registros de Campo

Las listas son geniales por posición, pero los registros de telemetría se leen mejor por nombre. Un **diccionario** mapea claves únicas a valores como pares `clave: valor`. Se accede con corchetes por clave o se añade/actualiza asignando.

```python
baliza = {
    "id": "VR-07",
    "bateria_porcentaje": 64,
    "temp_nucleo_c": 19.7,
    "enlace_malla": True,
    "zonas": ["norte", "muelle"]
}
print(baliza["id"])
print(baliza["bateria_porcentaje"])
baliza["rssi"] = -66
print(baliza)
```

## Salida

```text
VR-07
64
{'id': 'VR-07', 'bateria_porcentaje': 64, 'temp_nucleo_c': 19.7, 'enlace_malla': True, 'zonas': ['norte', 'muelle'], 'rssi': -66}
```

Las claves deben ser únicas; los valores pueden ser de cualquier tipo. Métodos útiles: `.keys()`, `.values()`, `.items()`. Iterar sobre `.items()` da pares `(clave, valor)`.

```python
for k, v in baliza.items():
    print(f"{k}: {v}")
```

> [!TIP]
> Si no se está seguro de si existe una clave, `baliza.get("rssi", "NA")` devuelve un valor por defecto sin generar `KeyError`.

## Conjuntos para Fallos Únicos

Al recopilar códigos de fallo en un lote, aparecen duplicados. Un **conjunto** contiene elementos únicos sin orden. Para crear un conjunto vacío hay que usar `set()` (no `{}`, que crea un diccionario). Los conjuntos admiten `union()`, `intersection()`, `difference()` para comparaciones rápidas.

```python
fallos_a = {"BATERIA_BAJA", "DESVIO", "BATERIA_BAJA"}
fallos_b = {"DESVIO", "SOBRECALENTAMIENTO"}
print(set(fallos_a))  # {'BATERIA_BAJA', 'DESVIO'}
print(fallos_a.union(fallos_b))
print(fallos_a.intersection(fallos_b))
print(fallos_a.difference(fallos_b))
```

## Salida

```text
{'BATERIA_BAJA', 'DESVIO'}
{'BATERIA_BAJA', 'DESVIO', 'SOBRECALENTAMIENTO'}
{'DESVIO'}
{'BATERIA_BAJA'}
```

Los conjuntos no son indexables por posición: el orden no está garantizado. Son ideales para comprobar pertenencia y eliminar duplicados, no para colas ordenadas.

> [!CAUTION]
> `{}` es un diccionario. Usa `set()` para crear un conjunto vacío.

## Elegir la Estructura Adecuada

| Estructura | Ordenada | Duplicados | Acceso | Uso ideal |
| :--- | :--- | :--- | :--- | :--- |
| Lista | Sí | Sí | Por índice | Colas, lotes, registros ordenados |
| Diccionario | Sí (orden de inserción) | Claves únicas | Por clave | Registros de campo, instantáneas de configuración |
| Conjunto | No | No | Por pertenencia | Fallos únicos, comparaciones |

### Tarea 5: Pila de Tormenta

Construye un diccionario `vr12 = {"id": "VR-12", "bateria_porcentaje": 38, "enlace_malla": False}`. Añade la clave `fallos` con la lista `["BATERIA_BAJA"]`. Crea el conjunto `vistos = {"BATERIA_BAJA", "DESVIO", "BATERIA_BAJA"}` e imprime `len(vistos)` y `vr12["bateria_porcentaje"]`.
