<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

# 09 - Ventana de Tormenta

**Versión original en inglés:** [09 - Storm Window](./09%20-%20Storm%20Window.md)

![Status Badge](https://img.shields.io/badge/Topic-Capstone-orange?style=for-the-badge)

**Curso:** Python
**Capítulo:** 4 — Integración
**Tema:** Proyecto Final: Consola de Telemetría
**Etiquetas:** `#python` `#telemetria` `#proyecto-final` `#proyecto` `#verdant-relay`

<hr style="border: none; height: 3px; background: linear-gradient(90deg, transparent, #7C5CFF, #00C2A8, #7C5CFF, transparent); margin: 24px 0;" />

## Juntando Todo

Una tormenta se acerca a la red de Verdant Relay. La consola necesita informar qué balizas pueden sincronizarse ahora, cuáles deben aplazarse y un breve resumen del lote. Este proyecto final utiliza variables, if/elif, bucles, listas, diccionarios, funciones y una clase — todo lo aprendido en las lecciones anteriores.

## La Consola

```python
class Baliza:
    def __init__(self, id_estacion, bateria_porcentaje, enlace_malla):
        self.id_estacion = id_estacion
        self.bateria_porcentaje = bateria_porcentaje
        self.enlace_malla = enlace_malla

    def puede_sincronizar(self):
        return self.enlace_malla and self.bateria_porcentaje >= 40

balizas = [
    Baliza("VR-07", 64, True),
    Baliza("VR-09", 26, True),
    Baliza("VR-12", 52, False),
    Baliza("VR-14", 41, True),
]

for b in balizas:
    if b.puede_sincronizar():
        print(f"{b.id_estacion} :: SINCRONIZACION_OK")
    elif b.bateria_porcentaje < 30:
        print(f"{b.id_estacion} :: APLAZAR_BATERIA_BAJA")
    elif not b.enlace_malla:
        print(f"{b.id_estacion} :: APLAZAR_SIN_ENLACE")
    else:
        print(f"{b.id_estacion} :: APLAZAR_OTRO")
```

## Salida

```text
VR-07 :: SINCRONIZACION_OK
VR-09 :: APLAZAR_BATERIA_BAJA
VR-12 :: APLAZAR_SIN_ENLACE
VR-14 :: SINCRONIZACION_OK
```

## Por Qué Esta Forma

La lógica se lee de arriba abajo: primero se comprueba la compuerta completa `puede_sincronizar()`, luego se ramifica por el bloqueo más específico. Mantener la decisión en la clase la hace coherente; el bucle mantiene el informe breve. Esta versión no necesita módulos externos, pero la estructura se integraría fácilmente con `random` para lecturas simuladas o `datetime` para una marca de tiempo.

> [!IMPORTANT]
> El orden de las comprobaciones importa. Si se comprobara la batería antes que `puede_sincronizar()`, una baliza con poca batería y sin enlace podría clasificarse de otra forma. Cuando sea la condición «verde» deseada, conviene poner primero la compuerta combinada.

## Ampliar la Idea

Una consola real podría recopilar fallos en un conjunto (eliminando duplicados), guardar instantáneas en diccionarios o usar funciones para formatear líneas. La clave está en componer piezas pequeñas: clase para estado/comportamiento, bucle para lotes, if para ramificaciones.

> [!TIP]
> Antes de escribir, traza a mano dos o tres elementos. Si la lógica coincide en papel, será mucho más fácil depurarla en código.

### Tarea 9: Ventana de Tormenta

Crea `balizas = [Baliza("VR-05", 35, True), Baliza("VR-11", 28, True)]` (usando el mismo patrón de clase). Para cada una, imprime `SINCRONIZACION_OK` si `bateria_porcentaje >= 40 and enlace_malla`, si no `ESPERA`. Hazlo con un bucle.
