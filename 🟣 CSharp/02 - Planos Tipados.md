# 02. Planos Tipados

**Versión original en inglés:** [02 - Typed Blueprints](./02%20-%20Typed%20Blueprints.md)

**Curso:** C#
**Tema:** Tipado estático, tipos por valor frente a referencia, conversiones, inmutabilidad de cadenas, var y const
**Etiquetas:** `#csharp` `#types` `#casting`

Cada campo de la tabla de equipamiento de Ironledger declara qué contiene. El compilador lee esa
declaración y rechaza el archivo si el código la contradice, antes de que la herramienta llegue a
ejecutarse.

## Tipado estático: el compilador comprueba

```csharp
int armadura = 12;
double peso = 3.75;
char grado = 'B';
bool equipado = true;
string nombre = "coraza remachada";
```

| Tipo | Contiene | Tamaño | Valor por defecto |
| :--- | :--- | :--- | :--- |
| `int` | enteros, ±2.100 millones | 4 bytes | `0` |
| `long` | enteros, ±9,2 trillones | 8 bytes | `0` |
| `double` | decimales, 15–17 dígitos significativos | 8 bytes | `0` |
| `decimal` | decimales exactos, para dinero | 16 bytes | `0` |
| `char` | un carácter UTF-16 | 2 bytes | `'\0'` |
| `bool` | `true` / `false` | 1 byte | `false` |
| `string` | texto, inmutable | referencia | `null` |

`decimal` existe para la moneda porque `0.1 + 0.2` en `double` no es exactamente `0.3`. Un total de
tienda calculado en `double` no cuadrará con el recibo; uno calculado en `decimal` sí.

## Tipos por valor y por referencia

| Clase | Ejemplos | Al asignar se copia |
| :--- | :--- | :--- |
| Por valor | `int`, `double`, `bool`, `char`, `struct` | el valor mismo |
| Por referencia | `string`, arrays, clases, `List<T>` | la referencia |

```csharp
int a = 5;
int b = a;      // b es un 5 independiente
b = 9;
Console.WriteLine(a);   // 5

int[] primero = { 1, 2, 3 };
int[] segundo = primero;   // el mismo array, otro nombre
segundo[0] = 99;
Console.WriteLine(primero[0]);   // 99
```

El segundo bloque es el que muerde: dos nombres, un array. Copiar un array requiere
`(int[])primero.Clone()` o `Array.Copy`.

## Conversiones

| De → A | Tipo | Sintaxis |
| :--- | :--- | :--- |
| `int` → `double` | implícita, ensancha | `double d = n;` |
| `double` → `int` | explícita, trunca | `int i = (int)d;` |
| `string` → `int` | análisis, puede fallar | `int.Parse(s)` / `int.TryParse(s, out i)` |
| cualquiera → `string` | formato | `valor.ToString()` |

```csharp
double peso = 3.79;
int entero = (int)peso;          // 3, truncado hacia cero

int analizado;
bool ok = int.TryParse("42", out analizado);
Console.WriteLine($"{entero} {ok} {analizado}");
```

## Salida

```text
3 True 42
```

`(int)` nunca redondea y nunca lanza: trunca. `int.Parse` lanza `FormatException` con basura, así que
`TryParse` —que devuelve un `bool` y escribe el resultado por `out`— es la versión que quieres para
cualquier cosa que escriba una persona.

## Las cadenas son inmutables

```csharp
string etiqueta = "iron";
etiqueta += "ledger";        // una cadena NUEVA; la vieja es basura
Console.WriteLine(etiqueta);
```

Cada edición aparente construye una cadena nueva. En un bucle que concatena mil líneas eso es
cuadrático; `StringBuilder` es la herramienta para ese caso, y esta nota es donde aprendes por qué
existe.

## `var` y `const`

```csharp
var lista = new List<string>();   // tipo inferido en compilación: List<string>
const int MaxRanuras = 8;         // constante de compilación, no puede cambiar
```

`var` no es "sin tipo": el tipo queda fijado en la declaración, inferido del lado derecho. `const`
debe ser un literal conocido en compilación; `readonly` cubre el caso en que el valor se calcula una
vez por objeto.

> [!WARNING]
> `var` con un literal es un juego de adivinanzas: `var ratio = 3 / 2;` es un `int` con `1`, no un
> `double` con `1.5`. Escribe el tipo cuando el lado derecho no lo deje obvio.

> [!TIP]
> Prefiere `double` para física y `decimal` para dinero. Mezclarlos obliga a una conversión y a una
> decisión de redondeo en cada frontera, y esa decisión es más fácil de tomar una vez, en el tipo,
> que en diez expresiones.

---

**Siguiente:** [[03 - Lógica de Triaje]]
