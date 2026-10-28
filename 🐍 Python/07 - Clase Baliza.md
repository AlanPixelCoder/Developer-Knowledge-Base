<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 07 - Clase Baliza

**Versión original en inglés:** [07 - Beacon Class](./07%20-%20Beacon%20Class.md)

![Status Badge](https://img.shields.io/badge/Topic-OOP-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 3 — Automatización
**Tema:** Clases, Objetos, __init__, Métodos de instancia
**Etiquetas:** `#python` `#telemetria` `#poo` `#clases` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Planos para las Estaciones

Cuando se gestionan una docena de balizas con los mismos campos y rutinas, repetir diccionarios se vuelve incómodo. Una **clase** es un plano; un **objeto** (instancia) es una estación concreta construida a partir de él. Los nombres de clase usan PascalCase.

```python
class Baliza:
    pass

vr07 = Baliza()
```

## Inicializar el Estado

El método `__init__()` se ejecuta al crear una instancia. `self` hace referencia a la instancia actual. Asignar `self.atributo = valor` adjunta campos a ese objeto.

```python
class Baliza:
    def __init__(self, id_estacion, bateria_porcentaje, enlace_malla):
        self.id_estacion = id_estacion
        self.bateria_porcentaje = bateria_porcentaje
        self.enlace_malla = enlace_malla

vr07 = Baliza("VR-07", 64, True)
print(vr07.id_estacion)
print(vr07.bateria_porcentaje)
```

## Salida

```text
VR-07
64
```

## Métodos de Instancia

Los **métodos de instancia** son funciones dentro de una clase que actúan sobre `self`. Pueden leer y actualizar atributos.

```python
class Baliza:
    def __init__(self, id_estacion, bateria_porcentaje, enlace_malla):
        self.id_estacion = id_estacion
        self.bateria_porcentaje = bateria_porcentaje
        self.enlace_malla = enlace_malla

    def estado(self):
        return f"{self.id_estacion} :: BATERIA {self.bateria_porcentaje}% ENLACE {self.enlace_malla}"

    def drenar(self, cantidad):
        self.bateria_porcentaje -= cantidad
        if self.bateria_porcentaje < 0:
            self.bateria_porcentaje = 0

vr07 = Baliza("VR-07", 64, True)
print(vr07.estado())
vr07.drenar(15)
print(vr07.estado())
```

## Salida

```text
VR-07 :: BATERIA 64% ENLACE True
VR-07 :: BATERIA 49% ENLACE True
```

Los métodos pueden aplicar reglas sencillas (limitar valores) sin exponer esa lógica por todas partes. Así se mantiene el comportamiento coherente en toda la red.

> [!NOTE]
> `self` es obligatorio como primer parámetro en los métodos de instancia, pero se pasa automáticamente al llamar como `instancia.metodo()`.

## Múltiples Instancias

Cada instancia tiene sus propios valores de atributos. Cambiar uno no afecta a los demás.

```python
vr07 = Baliza("VR-07", 64, True)
vr12 = Baliza("VR-12", 26, False)
vr07.drenar(10)
print(vr12.bateria_porcentaje)  # no afectado
```

## ¿Por Qué POO Aquí?

Para un conjunto fijo de campos y un pequeño conjunto de rutinas (estado, drenaje, comprobación de umbrales), las clases reducen la repetición y aclaran la intención. No todos los scripts necesitan POO, pero para modelar balizas encaja bien.

> [!TIP]
> Empieza simple: pone los datos en `__init__`, el comportamiento en los métodos. Evita meter todo en un solo método.

### Tarea 7: Clase Baliza

Crea la clase `Baliza` con `__init__(self, id_estacion, bateria_porcentaje)`. Añade el método `bateria_baja(self)` que devuelva `True` si bateria_porcentaje < 30, si no `False`. Crea `b = Baliza("VR-09", 26)` e imprime `b.bateria_baja()`.
