# Prueba de Esfuerzo del Equipamiento de Ironledger

**Versión original en inglés:** [Ironledger Loadout Stress Test](./Ironledger%20Loadout%20Stress%20Test.md)

**Curso:** C#
**Tema:** Proyecto final: una herramienta de consola completa — validación de entrada, bucles, matrices, métodos y decisiones
**Etiquetas:** `#csharp` `#proyecto` `#consola`

La pasada de balance del estudio necesita un número: el peso total que carga un personaje y si cruza
la línea de sobrecarga. Esta nota construye esa herramienta de principio a fin —entrada, bucle,
matriz, método, decisión— y muestra cómo se ve un programa de consola probable antes de convertirse
en una ventana.

## Qué debe hacer

| Requisito | Regla |
| :--- | :--- |
| Leer una cuenta | entre 1 y 8 ranuras |
| Leer cada peso | enteros positivos |
| Informar | total, media, ranura más pesada |
| Avisar | total por encima del límite de carga |
| Repetir | hasta que el operador responda `n` |

## El programa

```csharp
using System;

class PruebaEsfuerzo
{
    const int MaxRanuras = 8;
    const int Sobrecarga = 15;

    static int LeerEntero(string aviso, int min, int max)
    {
        while (true)
        {
            Console.Write(aviso);
            string? linea = Console.ReadLine();
            if (int.TryParse(linea, out int valor) && valor >= min && valor <= max)
            {
                return valor;
            }
            Console.WriteLine("entrada no válida");
        }
    }

    static int Total(int[] pesos)
    {
        int suma = 0;
        foreach (int p in pesos) suma += p;
        return suma;
    }

    static int MasPesado(int[] pesos)
    {
        int mejor = pesos[0];
        for (int i = 1; i < pesos.Length; i++)
        {
            if (pesos[i] > mejor) mejor = pesos[i];
        }
        return mejor;
    }

    static void Main()
    {
        bool otra = true;

        while (otra)
        {
            int ranuras = LeerEntero("ranuras: ", 1, MaxRanuras);
            int[] pesos = new int[ranuras];

            for (int i = 0; i < ranuras; i++)
            {
                pesos[i] = LeerEntero($"peso {i + 1}: ", 1, 99);
            }

            int total = Total(pesos);
            double media = (double)total / ranuras;

            Console.WriteLine($"total {total}, media {media:F1}, más pesado {MasPesado(pesos)}");

            if (total > Sobrecarga)
            {
                Console.WriteLine($"por encima del límite en {total - Sobrecarga}");
            }
            else
            {
                Console.WriteLine($"por debajo del límite en {Sobrecarga - total}");
            }

            Console.Write("¿otra carga? (s/n): ");
            otra = Console.ReadLine() == "s";
        }
    }
}
```

## Una sesión de ejemplo

Las respuestas escritas van tras cada aviso:

```text
ranuras: 3
peso 1: 6
peso 2: 7
peso 3: 4
total 17, media 5.7, más pesado 7
por encima del límite en 2
¿otra carga? (s/n): n
```

## Por qué se divide así

| Pieza | Motivo |
| :--- | :--- |
| `LeerEntero` | un solo lugar aplica el análisis y el rango, así que ninguna llamada repite el bucle |
| `Total`, `MasPesado` | funciones puras sobre una matriz: misma entrada, misma respuesta, sin consola |
| `Main` | solo orquesta e imprime |
| constantes | los límites se nombran una vez y se leen en todas partes |

Los métodos puros son la parte que puedes probar sin escribir: llama a `Total(new[] { 6, 7, 4 })` y
comprueba `17`. Esa separación es la razón de que la herramienta no sea un `Main` largo.

## Qué probar a mano

1. Una sola ranura: la media es ese peso.
2. Justo en el límite: el mensaje dice "por debajo del límite en 0".
3. Entrada basura (`abc`, vacío, `0`, `99` donde el máximo es 8): `LeerEntero` vuelve a preguntar,
   nunca se cae.
4. Ocho ranuras: el máximo; después intenta nueve.

## Ampliaciones

- Imprimir el índice de la ranura más pesada, no solo su valor.
- Llevar un total acumulado mientras se escribe, para que el operador vea caer el presupuesto.
- Pasar las ranuras a una `List<int>` y permitir borrar por índice.
- Devolver un `record` pequeño con total, media y más pesado en lugar de imprimir tres veces.

> [!NOTE]
> `media` se calcula con `(double)total / ranuras` a propósito: `total / ranuras` sería división
> entera y diría `5` en vez de `5.7`. La conversión es la diferencia entre un informe correcto y uno
> verosímil.

> [!TIP]
> Ejecuta la herramienta con `dotnet run` desde la carpeta del proyecto. Como el bucle termina con
> `n`, puedes probar todo el camino en una sesión sin reiniciar el proceso.
