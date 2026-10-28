
# 02. Instrucciones de Campo

**Versión original en inglés:** [02 - Field Briefs](./02%20-%20Field%20Briefs.md)

**Curso:** GenAI
**Capítulo:** 2 — Relevo Verdoso
**Tema:** Prompts, roles, restricciones, few-shot, fallos
**Etiquetas:** `#genai` `#prompts` `#few-shot` `#llm` `#python`

En Verdant Relay, un despacho vago a la cuadrilla produce reparaciones vagas. Un **parte de campo** preciso indica rol, contexto, restricciones y la forma exacta de salida antes de que nadie salga del patio de postes. Lo mismo ocurre con un modelo de lenguaje: un prompt es un conjunto de instrucciones, no una pregunta lanzada al vacío. Esta lección trata redactar prompts como escribir una especificación: comprobable, acotado y fácil de romper con ambigüedad. Sin florituras de «chatbot», solo partes que produzcan notas de relevo útiles.

## De adivinar a especificar

Compárense dos partes para el mismo trabajo: resumir un breve informe de relevo en el registro nocturno.

```text
Parte A (vaga): "¿Qué ha pasado en el Poste-3?"
Parte B (precisa): "Eres un registrador nocturno de Verdant Relay. Resume en UNA línea con el formato <poste> | <incidencia> | <acción>.
Solo usa hechos presentes en el informe. Informe: 'Poste-3 informa niebla en la puerta, la cuadrilla colocó sacos de arena.'"
```

> [!NOTE]
> Ser específico no es ser prolijo. La parte B fija rol, formato, alcance (solo hechos dados) y forma de salida. Esas restricciones son más fáciles de comprobar que «sé útil».

## Construir restricciones

Un buen parte acota el espacio de respuestas posibles. Para el relevo, las restricciones útiles son: formato, longitud, tono (conciso), qué incluir/excluir y condiciones de rechazo. Mejor escribirlas como reglas que como peticiones.

```python
informe = "Poste-7 informa cable guía suelto cerca del mástil. La cuadrilla apretó el tensor."
parte = (
  "Rol: registrador nocturno de Verdant Relay.\n"
  "Tarea: escribir UNA línea concisa con formato '<POSTE> | <INCIDENCIA> | <ACCIÓN>'.\n"
  "Reglas: usar solo hechos del informe; sin especulaciones; sin comentarios extra.\n"
  f"Informe: {informe}"
)
print(parte)
```

## Salida

```text
Rol: registrador nocturno de Verdant Relay.
Tarea: escribir UNA línea concisa con formato '<POSTE> | <INCIDENCIA> | <ACCIÓN>'.
Reglas: usar solo hechos del informe; sin especulaciones; sin comentarios extra.
Informe: Poste-7 informa cable guía suelto cerca del mástil. La cuadrilla apretó el tensor.
```

Una respuesta correcta sería `Poste-7 | cable guía suelto cerca del mástil | apretó el tensor`. La forma se comprueba a simple vista.

## Few-shot: mostrar, no decir

A veces una regla se entiende mejor con un ejemplo. El **prompting con pocos ejemplos** (*few-shot*) da al modelo un par de ejemplos entrada/salida con el formato exacto y luego el nuevo informe. Muy eficaz para formatos rígidos como líneas de registro o códigos de campo.

```python
ejemplos = [
    ("Poste-3 informa niebla en la puerta, la cuadrilla colocó sacos de arena.", "Poste-3 | niebla en la puerta | colocó sacos de arena"),
    ("Poste-1 informa grapa corroída cerca de la base, la cuadrilla reemplazó la grapa.", "Poste-1 | grapa corroída cerca de la base | reemplazó la grapa"),
]
informe = "Poste-9 informa desagüe obstruido en el cimiento, la cuadrilla retiró escombros."
print("ejemplos:", len(ejemplos))
```

> [!TIP]
> Los ejemplos deben ser mínimos e idénticos en estructura al objetivo. Si los ejemplos varían, el modelo también variará. La coherencia vale más que la cantidad.

## El coste de la ambigüedad

Los partes ambiguos generan fallos. «Resume amablemente» invita a más palabras. «Escribe un informe» invita a párrafos. «Sé minucioso» invita a especulaciones. En Verdant Relay, especular es peligroso: un registro nocturno no debe inventar una reparación que no se hizo. La solución es sustituir adjetivos de grado por reglas comprobables.

```python
# malo: "Resume esto amablemente y sé minucioso."
# bueno: "Devuelve EXACTAMENTE una línea. Solo hechos presentes. Sin causas ni recomendaciones."
print("sustituir 'amablemente' por 'exactamente una línea'")
```

> [!WARNING]
> Pedir «piensa paso a paso» no es intrínsecamente malo, pero para un formato rígido como una línea de registro suele ser innecesario y puede alargar la salida. Hay que ajustar el nivel de razonamiento a la tarea: tareas concisas necesitan partes concisas.

## Probar el parte a mano

Hay que tratar el prompt como código: cambiar una restricción, pensar en el caso contra el informe, ver qué se rompe. Por ejemplo, quitar «solo usa hechos» puede añadir «probablemente por humedad» — plausible, pero no verificado. Añadir «exactamente una línea» elimina párrafos. Esto es depuración por especificación, no rogarle al modelo que «lo intente otra vez».

```python
def comprobar_linea(s):
    partes = s.split(' | ')
    return len(partes) == 3

print(comprobar_linea("Poste-7 | cable guía suelto cerca del mástil | apretó el tensor"))
print(comprobar_linea("Resumen: hubo un problema en el Poste-7."))  # formato incorrecto
```

## Salida

```text
True
False
```

## Disciplina de campo

Verdant Relay no necesita un parte conversador, necesita uno que se pueda contrastar con un código de campo. Rol, tarea, formato, reglas y ejemplos (si hacen falta) son los ingredientes. Breve, comprobable y nunca pedir «más» cuando se quiere «sigue este formato exactamente». Esa disciplina se traslada a la siguiente lección: una vez se sabe preguntar con precisión, se puede centrarse en *qué* preguntar para encontrar lo relevante.
