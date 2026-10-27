# 00b. Manual de Campo de Emberforge

**Versión original en inglés:** [00b - Emberforge Field Manual](./00b%20-%20Emberforge%20Field%20Manual.md)

**Curso:** C#
**Tema:** Referencia de sintaxis de una página para todo el módulo
**Etiquetas:** `#csharp` `#referencia` `#chuleta`

Una página para la sintaxis que usa este módulo, en el orden en que la presentan las lecciones. Cuando
una nota y esta página no coincidan, la nota tiene razón: esta página es el índice, no la explicación.

## Tipos

| Tipo | Uso | Por defecto | Nota |
| :--- | :--- | :--- | :--- |
| `int` | cuentas, vida | `0` | 32 bits |
| `long` | cuentas grandes | `0` | 64 bits |
| `double` | física, proporciones | `0` | coma flotante binaria |
| `decimal` | moneda | `0` | exacto, más lento |
| `char` | un carácter | `'\0'` | comillas simples |
| `bool` | indicadores | `false` | `true` / `false` |
| `string` | texto | `null` | inmutable, comillas dobles |

## Declaración

```csharp
int vida = 30;
double ratio = 0.5;
string nombre = "coraza remachada";
var ranuras = new List<string>();
const int MaxRanuras = 8;
```

## Conversiones

| De | A | Código |
| :--- | :--- | :--- |
| `int` | `double` | `double d = i;` |
| `double` | `int` | `int i = (int)d;` trunca |
| `string` | `int` | `int.TryParse(s, out int v)` |
| cualquiera | `string` | `v.ToString()` o `$"{v}"` |

## Operadores

| Grupo | Símbolos |
| :--- | :--- |
| Aritméticos | `+ - * / %` |
| Comparación | `== != < <= > >=` |
| Lógicos | `&& \|\| !` con cortocircuito |
| Asignación | `= += -= *= /=` |
| Incremento | `++ --` |

## Control de flujo

```csharp
if (cond) { }
else if (cond) { }
else { }

switch (valor)
{
    case 1: break;
    default: break;
}
```

## Bucles

| Bucle | Uso |
| :--- | :--- |
| `while (cond)` | cuenta desconocida, comprobar antes |
| `do { } while (cond);` | al menos una pasada |
| `for (int i = 0; i < n; i++)` | cuenta conocida |
| `foreach (var x in items)` | leer cada elemento |

`break` sale, `continue` salta a la pasada siguiente.

## Matrices

```csharp
int[] a = new int[3];
int[] b = { 4, 8, 15 };
Console.WriteLine(b.Length);     // 3
Console.WriteLine(b[0]);         // 4
```

Índices válidos: de `0` a `Length - 1`.

## Métodos

```csharp
static int Total(int[] valores)
{
    int suma = 0;
    foreach (int v in valores) suma += v;
    return suma;
}

static void Informar(int total) => Console.WriteLine(total);

if (int.TryParse(texto, out int n)) { }
```

| Modificador | Dirección |
| :--- | :--- |
| `out` | debe asignarse dentro |
| `ref` | lee y escribe la variable del llamador |

## Consola

```csharp
Console.WriteLine("línea");
Console.Write("aviso: ");
string? entrada = Console.ReadLine();
```

## Compilar y ejecutar

```bash
dotnet new console -o herramienta
dotnet run
dotnet build
```

## Errores comunes

| Trampa | Solución |
| :--- | :--- |
| `3 / 2` es `1` | convierte un lado: `(double)3 / 2` |
| `array.Length` como índice | el último índice es `Length - 1` |
| `a = b` con matrices | comparten la matriz; clona para copiar |
| `int.Parse("abc")` | lanza; prefiere `TryParse` |
| `&&` frente a `&` | `&` evalúa ambos lados |
| `+=` de cadenas en un bucle | crea una cadena nueva cada vez; usa `StringBuilder` |
---

**Empieza aquí:** [[01 - Del Plano al Binario]]
