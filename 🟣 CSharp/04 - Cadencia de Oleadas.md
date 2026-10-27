# 04. Cadencia de Oleadas

**Versión original en inglés:** [04 - Wave Cadence](./04%20-%20Wave%20Cadence.md)

**Curso:** C#
**Tema:** while, do-while y for; bucles centinela, acumulación, break y continue
**Etiquetas:** `#csharp` `#loops` `#iteration`

Un simulador de oleadas invoca enemigos hasta agotar el presupuesto de la oleada. La cuenta no se
conoce cuando se escribe el código —depende del presupuesto y del coste de cada enemigo— así que el
bucle lo dirige una condición, no un número.

## `while`: comprobar primero

```csharp
using System;

class Oleada
{
    static void Main()
    {
        int presupuesto = 7;
        int invocados = 0;

        while (presupuesto >= 2)
        {
            presupuesto -= 2;
            invocados++;
        }

        Console.WriteLine($"invocados {invocados}, sobrante {presupuesto}");
    }
}
```

## Salida

```text
invocados 3, sobrante 1
```

El cuerpo puede correr cero veces: con `presupuesto = 1` la condición es falsa de inmediato. Esa es la
diferencia entre `while` y un `do ... while`, que siempre corre una vez.

## `do ... while`: al menos una vez

```csharp
int tecla = 0;
do
{
    Console.WriteLine("pulsa 1 para cerrar la oleada");
    tecla = 1;   // entrada simulada
} while (tecla != 1);
```

Un bucle de aviso quiere esta forma: no puedes saber que la respuesta está mal hasta haber preguntado.

## `for`: la cuenta es conocida

```csharp
for (int oleada = 1; oleada <= 3; oleada++)
{
    Console.WriteLine($"oleada {oleada} en camino");
}
```

| Cláusula | Se ejecuta | Aquí |
| :--- | :--- | :--- |
| Inicialización | una vez | `int oleada = 1` |
| Condición | antes de cada pasada | `oleada <= 3` |
| Incremento | después de cada pasada | `oleada++` |

## Bucles centinela

Un centinela es un valor que significa "para", no un dato. Leer hasta el centinela es el patrón
estándar de entrada:

```csharp
int total = 0;
int valor = 7;              // lectura simulada; una herramienta real analiza Console.ReadLine()

while (valor != 0)
{
    total += valor;
    valor = 0;              // siguiente lectura: el centinela que cierra el bucle
}

Console.WriteLine($"total {total}");
```

## Salida

```text
total 7
```

> [!CAUTION]
> Borra la línea `valor = 0;` y ese bucle no termina nunca, porque nada dentro puede cambiar la
> condición. Todo bucle centinela necesita un camino que produzca el centinela; si la lectura viene de
> `Console.ReadLine()`, ese camino es que la persona lo escriba, o un `break` con una palabra clave.

## `break` y `continue`

```csharp
for (int i = 1; i <= 6; i++)
{
    if (i == 2) continue;   // salta esta pasada
    if (i == 5) break;      // sale del bucle
    Console.Write(i + " ");
}
```

## Salida

```text
1 3 4
```

`continue` vuelve al incremento; `break` abandona el bucle. Los dos hacen más difícil razonar sobre el
bucle, así que prefiere una condición bien escrita y úsalos para el caso excepcional.

## Acumular, no solo contar

| Objetivo | Inicio | Actualización |
| :--- | :--- | :--- |
| Contar | `0` | `contador++` |
| Sumar | `0` | `total += valor` |
| Máximo | primer valor | `if (v > mejor) mejor = v` |
| Media | suma + cuenta | dividir tras el bucle |

> [!TIP]
> Un `for` es un `while` con la contabilidad movida a la cabecera. Si el bucle necesita el contador
> después de terminar, declara el contador antes de la cabecera; dentro, sale de ámbito en la llave de
> cierre.

---

**Siguiente:** [[05 - Lista de Carga]]
