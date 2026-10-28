<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 08 - Módulos de Relé

**Versión original en inglés:** [08 - Relay Modules](./08%20-%20Relay%20Modules.md)

![Status Badge](https://img.shields.io/badge/Topic-Modules-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 4 — Integración
**Tema:** Módulos, import, from/import, Biblioteca estándar, Módulos personalizados
**Etiquetas:** `#python` `#telemetria` `#modulos` `#importaciones` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Compartir Rutinas

A medida que las rutinas crecen, meterlo todo en un solo archivo se vuelve engorroso. Un **módulo** es un archivo `.py` con funciones/variables que se pueden importar. La biblioteca estándar de Python tiene muchos módulos (`math`, `random`, `datetime`). Dividir por responsabilidad (comprobaciones, formato, tiempo) mantiene los scripts cortos y fáciles de probar.

## Formas de Importar

```python
import math
from math import pi
from math import sqrt as s
```

- `import math` usa `math.pi`
- `from math import pi` usa `pi` directamente
- `as` da un alias corto

```python
import math
r = 12.4
print(4 * math.pi * r * r)  # área aproximada de un disco
```

## Salida

```text
1932.203931710084
```

## Usar `random` para Simulaciones

Para probar sin hardware real, `random` ayuda a simular lecturas.

```python
import random
rssi = random.randint(-80, -50)
print(rssi)
```

`randint(a,b)` es inclusivo. `random.choice(lista)` elige uno; `random.choices(lista, k=n)` puede repetir.

## Módulos Personalizados

Cualquier `.py` en el mismo directorio se puede importar. Se ponen ayudas compartidas en `relay_utils.py`, luego `import relay_utils`.

```python
# relay_utils.py
def estado_bateria(pct):
    if pct < 30:
        return "BAJO"
    return "OK"
```

```python
# check.py
import relay_utils
print(relay_utils.estado_bateria(26))
```

## Salida

```text
BAJO
```

También se puede hacer `from relay_utils import estado_bateria` para llamarla directamente.

> [!NOTE]
> Al importar un módulo propio, los cambios se aplican tras reiniciar en una ejecución sencilla; en algunos entornos puede ser necesario recargarlo. Para estas lecciones, basta con ejecutar una vez por cambio.

## `datetime` para Ventanas de Tormenta

Las ventanas de tormenta necesitan marcas de tiempo. `datetime` ofrece objetos fecha/hora.

```python
import datetime
ahora = datetime.datetime.now()
print(ahora)
```

La salida varía, pero el objeto es usable. Para una línea de registro, se puede formatear con f-strings convirtiéndolo a cadena.

> [!TIP]
> Mantén las importaciones al inicio. Agrupa primero las de la biblioteca estándar, luego los módulos locales.

### Tarea 8: Módulos de Relé

Haz una comprobación mental: importa `math` e imprime `math.ceil(12.2)`. Escribe conceptualmente qué hace `from random import randint`. No es necesario crear archivos, solo escribe dos líneas cortas mostrando ambas formas: importa `math` y usa `math.ceil`, e importa `randint` desde `random` y llámalo con `randint(1,6)`.
