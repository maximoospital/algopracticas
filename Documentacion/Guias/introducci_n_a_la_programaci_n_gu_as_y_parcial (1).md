# Introducción a la Programación - 2do cuatrimestre 2025
**Departamento de Computación**  
**Facultad de Ciencias Exactas y Naturales - Universidad de Buenos Aires**

---

## Listado de funciones permitidas para el parcial de Python

Cualquier otra función debe ser implementada. Si utilizan una función no permitida, se anula el ejercicio.

* **Conversión de tipos:** `int`, `list`, `float`, `str`, `tuple`, `bool`
* **Estructuras:** `if-else-elif`, `while`, `for` *(Pueden usar `for in range(..)` o `for in secuencia`)*
* **Rango:** `range(i, f, p)` *(Pueden usar los 3 parámetros, 2 o 1)*
* **Aritméticas:** `+`, `-`, `*`, `/`, `//`, `sqrt`, `round`, `floor`, `ceil`, `%`
* **Lógicas:** `and`, `or`, `not`, `==`, `!=`, `>`, `<`, `>=`, `<=`
* **Sobre secuencias:**
  * Pertenece: `in`
  * Concatenación: `+`
  * Repetición: `*`
  * Longitud: `len`
  * Acceso a elementos: `s[elem]` *(¡No está permitido `s[i:f]`, `s[-i]` o similar!)*
* **Listas:** `append(e)`, `insert(p, e)`, `remove(e)`, `index(e)`, `count(e)`, `clear()`, `pop()`, `pop(n)`, `copy()`
* **Diccionarios:** `items()`, `keys()`, `values()`, `pop(clave)`, `clear()`
* **TAD Pilas:** `from queue import LifoQueue`
  * `pila = LifoQueue()`; `put(e)`; `get()`; `empty()`
* **TAD Colas:** `from queue import Queue`
  * `cola = Queue()`; `put(e)`; `get()`; `empty()`
* **Archivos:** `open`, `read`, `readline`, `readlines`, `write`, `writelines`, `close`, `os.path.join()`, `os.path.exists()`

> **Nota:** El uso de `break`/`continue` **NO** está recomendado. Recordar que todas las variables deben ir anotadas con su tipo correspondiente.

---

# Guía Práctica 7: Funciones sobre listas (tipos complejos)

Recordar usar las anotaciones de tipado en todas las variables. Por ejemplo: `def funcion(numero: int) -> bool:`.  
Las anotaciones de tipado de las colecciones, listas, diccionarios o tuplas, dependen de la versión de Python que usamos:
* En **Python 3.8** son en mayúscula (ej: `List`, `Dict`, `Tuple`) y hay que importar el tipo: `from typing import List, Dict, Tuple`.
* En **Python 3.9+** son en minúscula (ej: `list`, `dict`, `tuple`) y no hace falta importar nada. Por ejemplo: `list[int]`, `list[tuple[int, str]]`, `list[list[int]]`.

Sugerimos revisar esta página que resume las formas de uso: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

En los ejercicios se pueden usar funciones matemáticas como por ejemplo: `sqrt`, `round`, `floor`, `ceil`, `%`. Ver especificaciones en: https://docs.python.org/es/3.10/library/math.html y https://docs.python.org/es/3/library/functions.html  
Para conocer cómo se usan las funciones sobre secuencias, revisar la especificación oficial: https://docs.python.org/es/3/library/stdtypes.html?highlight=list#typesseq

## 1. Recorrido y búsqueda en secuencias

### Ejercicio 1
Codificar en Python las siguientes funciones sobre secuencias:  
*(Nota: Cada problema puede tener más de una implementación. Probar utilizando distintas formas de recorrido sobre secuencias, y distintas funciones de Python. No te conformes con una solución, recordar que siempre conviene consultar con tus docentes).*

**1.**
```text
problema pertenece (in s: seq⟨Z⟩, in e: Z) : Bool {
  requiere: { True }
  asegura: { (res = true) <-> (existe un i in Z tal que 0 <= i < |s| ^ s[i] = e) }
}
```
*Implementar al menos de 3 formas distintas este problema.*

**2.**
```text
problema divide_a_todos (in s: seq⟨Z⟩, in e: Z) : Bool {
  requiere: { e != 0 }
  asegura: { (res = true) <-> (para todo i in Z si 0 <= i < |s| -> s[i] mod e = 0) }
}
```

**3.**
```text
problema suma_total (in s: seq⟨Z⟩) : Z {
  requiere: { True }
  asegura: { res es la suma de todos los elementos de s }
}
```
*Nota: no utilizar la función `sum()` nativa.*

**4.**
```text
problema maximo (in s: seq⟨Z⟩) : Z {
  requiere: { |s| > 0 }
  asegura: { res = al mayor de todos los números que aparece en s }
}
```
*Nota: no utilizar la función `max()` nativa.*

**5.**
```text
problema minimo (in s: seq⟨Z⟩) : Z {
  requiere: { |s| > 0 }
  asegura: { res = al menor de todos los números que aparece en s }
}
```
*Nota: no utilizar la función `min()` nativa.*

**6.**
```text
problema ordenados (in s: seq⟨Z⟩) : Bool {
  requiere: { True }
  asegura: { res = true <-> (para todo i in Z si 0 <= i < (|s| - 1) -> s[i] < s[i + 1]) }
}
```

**7.**
```text
problema pos_maximo (in s: seq⟨Z⟩) : Z {
  requiere: { True }
  asegura: { (Si |s| = 0 entonces res = -1; si no, res = al índice de la posición donde aparece el mayor elemento de s (si hay varios es la primera aparición) }
}
```

**8.**
```text
problema pos_minimo (in s: seq⟨Z⟩) : Z {
  requiere: { True }
  asegura: { (Si |s| = 0 entonces res = -1; si no, res = al índice de la posición donde aparece el menor elemento de s (si hay varios es la última aparición) }
}
```

**9.** Dada una lista de palabras ($seq\langle seq\langle Char\rangle\rangle$), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo: `["termo", "gato", "tener", "jirafas"]`, devuelve `False`.
```text
problema long_mayorASiete (in s: seq⟨seq⟨Char⟩⟩) : Bool {
  requiere: { True }
  asegura: { (res = true) <-> (existe i in Z tal que (0 <= i < (|s| - 1)) y (|s[i]| > 7)) }
}
```

**10.** Dado un texto en formato string, devolver verdadero si es palíndromo (se lee igual en ambos sentidos), falso en caso contrario. Las cadenas de texto vacías o con 1 sólo elemento son palíndromo.
```text
problema es_palindroma (in s: seq⟨Char⟩) : Bool {
  requiere: { True }
  asegura: { (res = true) <-> (s es igual a su reverso) }
}
```

**11.** Recorrer una $seq\langle\mathbb{Z}\rangle$ y devolver verdadero si hay 3 números iguales consecutivos, en cualquier posición y `False` en caso contrario.
```text
problema iguales_consecutivos (in s: seq⟨Z⟩) : Bool {
  requiere: { True }
  asegura: { (res = true) <-> (existe i, j, k in Z tal que (0 <= i, j, k < (|s| - 1)) y (i + 2 = j + 1 = k) y (s[i] = s[j] = s[k])) }
}
```

**12.** Recorrer una palabra en formato string y devolver `True` si ésta tiene al menos 3 vocales distintas y `False` en caso contrario.
```text
problema vocales_distintas (in s: seq⟨Char⟩) : Bool {
  requiere: { True }
  asegura: { (res = true) <-> (existe i, j, k in Z tal que (0 <= i, j, k < (|s| - 1)) y (s[i] != s[j] != s[k]) y (s[i], s[j], s[k] in {'a', 'e', 'i', 'o', 'u'})) }
}
```

**13.** Recorrer una $seq\langle\mathbb{Z}\rangle$ y devolver la posición donde inicia la secuencia de números ordenada más larga. Si hay dos subsecuencias de igual longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vacía.
```text
problema pos_secuencia_ordenada_mas_larga (in s: seq⟨Z⟩) : Z {
  requiere: { |s| > 0 }
  asegura: { (res = i) <-> (existe i, j in Z tal que (0 <= i, j < (|s| - 1)) y i <= j y (para todo k tal que i <= k < j -> s[k] <= s[k + 1]) y j - i + 1 es máximo e i es el mínimo valor que lo cumple) }
}
```

**14.** Cantidad de dígitos impares.
```text
problema cantidad_digitos_impares (in s: seq⟨Z⟩) : Z {
  requiere: { Todos los elementos de números son mayores o iguales a 0 }
  asegura: { res es la cantidad total de dígitos impares que aparecen en cada uno de los elementos de números }
}
```
*Por ejemplo, si la lista de números es `[57, 2383, 812, 246]`, entonces el resultado esperado sería 5 (los dígitos impares son 5, 7, 3, 3 y 1).*

---

## 2. Recorrido: filtrando, modificando y procesando secuencias

### Ejercicio 2
Implementar las siguientes funciones sobre secuencias pasadas por parámetro:

**1.**
```text
problema CerosEnPosicionesPares (inout s: seq⟨Z⟩) {
  requiere: { True }
  modifica: { s }
  asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i es par, entonces s[i] = 0) }
}
```

**2.**
```text
problema CerosEnPosicionesPares2 (in s: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: { True }
  asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i es par, entonces res[i] = 0) }
}
```

**3.** Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios, sino que borra la vocal y concatena a continuación.
```text
problema sin_vocales (in s: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: { True }
  asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
}
```
*Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena original, conservando el orden de los elementos restantes.*

**4.**
```text
problema reemplaza_vocales (in s: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: { True }
  asegura: { |res| = |s| }
  asegura: { Para todo i in Z, si 0 <= i < |res| -> (pertenece(<'a','e','i','o','u'>, s[i]) ^ res[i] = '_') v (¬pertenece(<'a','e','i','o','u'>, s[i]) ^ res[i] = s[i]) }
}
```

**5.**
```text
problema da_vuelta_str (in s: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: { True }
  asegura: { |res| = |s| }
  asegura: { Para todo i in Z si 0 <= i < |res| -> res[i] = s[|s| - i - 1] }
}
```

**6.**
```text
problema eliminar_repetidos (in s: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: { True }
  asegura: { (|res| <= |s|) ^ (para todo i in Z si 0 <= i < |s| -> pertenece(s[i], res)) ^ (para todo i, j in Z si (0 <= i, j < |res| ^ i != j) -> res[i] != res[j]) }
}
```

### Ejercicio 3
Implementar una función para conocer el estado de aprobación de una materia a partir de las notas obtenidas por un/a alumno/a cumpliendo con la siguiente especificación:
```text
problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
  requiere: { |notas| > 0 }
  requiere: { Para todo i in Z si 0 <= i < |notas| -> 0 <= notas[i] <= 10 }
  asegura: { res = 1 <-> todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
  asegura: { res = 2 <-> todos los elementos de notas son mayores o iguales a 4 y el promedio está entre 4 (inclusive) y 7 }
  asegura: { res = 3 <-> alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
}
```

### Ejercicio 4
Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento `"I"` para ingreso de dinero y `"R"` para retiro de dinero, y además el monto de cada operación. Por ejemplo, si la lista de tuplas es `[("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]` entonces el saldo actual es `1280`.
```text
problema saldoActual (in movimientos: seq⟨Char x Z⟩) : Z {
  requiere: { Para todo i in Z si 0 <= i < |movimientos| -> movimientos[i]_0 in {"I", "R"} y movimientos[i]_1 > 0 }
  asegura: { res = sum_{ingresos} movimientos[i]_1 - sum_{retiros} movimientos[i]_1 }
}
```

---

## 3. Matrices

### Ejercicio 5
Analizando parámetros `in` y `out` vs. `resultado`:

**1.**
```text
problema pertenece_a_cada_uno_version_1 (in s: seq⟨seq⟨Z⟩⟩, in e: Z, out res: seq⟨Bool⟩) {
  requiere: { True }
  asegura: { |res| >= |s| }
  asegura: { Para todo i in Z si 0 <= i < |s| -> (res[i] = true <-> pertenece(s[i], e)) }
}
```
*Nota: Reutilizar la función `pertenece()` implementada previamente para listas.*

**2.**
```text
problema pertenece_a_cada_uno_version_2 (in s: seq⟨seq⟨Z⟩⟩, in e: Z, out res: seq⟨Bool⟩) {
  requiere: { True }
  asegura: { |res| = |s| }
  asegura: { Para todo i in Z si 0 <= i < |s| -> (res[i] = true <-> pertenece(s[i], e)) }
}
```

**3.**
```text
problema pertenece_a_cada_uno_version_3 (in s: seq⟨seq⟨Z⟩⟩, in e: Z) : seq⟨Bool⟩ {
  requiere: { True }
  asegura: { |res| = |s| }
  asegura: { Para todo i in Z si 0 <= i < |s| -> (res[i] = true <-> pertenece(s[i], e)) }
}
```

**4.** Pensar: ¿Cómo cambia este problema respecto de la versión 1? Pensar en relación de fuerza entre: implementación en Python y las especificaciones. ¿Se puede usar la implementación del ejercicio 2 para la especificación del 1? ¿Se puede usar la implementación del ejercicio 1 para la especificación del 2? Justificar su respuesta.

### Ejercicio 6
Implementar las siguientes funciones sobre matrices (secuencias de secuencias):

**1.**
```text
problema es_matriz (in s: seq⟨seq⟨Z⟩⟩) : Bool {
  requiere: { True }
  asegura: { res = true <-> (|s| > 0) ^ (|s[0]| > 0) ^ (Para todo i in Z si 0 <= i < |s| -> |s[i]| = |s[0]|) }
}
```

**2.**
```text
problema filas_ordenadas (in m: seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
  requiere: { esMatriz(m) }
  asegura: { Para todo i in Z si 0 <= i < |res| -> (res[i] = true <-> ordenados(m[i])) }
}
```
*Nota: Reutilizar la función `ordenados()` implementada previamente para listas.*

**3.**
```text
problema columna (in m: seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
  requiere: { esMatriz(m) }
  requiere: { c < |m[0]| }
  requiere: { c >= 0 }
  asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en el mismo orden que aparecen }
}
```

**4.**
```text
problema columnas_ordenadas (in m: seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
  requiere: { esMatriz(m) }
  asegura: { Para todo índice de columna c: 0 <= c < |m[0]| -> (res[c] = true <-> ordenados(columna(m, c))) }
  asegura: { |res| = |m[0]| }
}
```
*Nota: Reutilizar la función `ordenados()` implementada previamente para listas.*

**5.**
```text
problema transponer (in m: seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
  requiere: { esMatriz(m) }
  asegura: { Devuelve m^t (o sea la matriz transpuesta) }
}
```
*Nota: Usar `columna()` para ir obteniendo todas las columnas de la matriz.*

**6. Ta-Te-Ti Tradicional:**
```text
problema quien_gana_tateti (in m: seq⟨seq⟨Char⟩⟩) : Z {
  requiere: { esMatriz(m) }
  requiere: { |m| = 3 }
  requiere: { |m[0]| = 3 }
  requiere: { En la matriz si hay 3 X alineadas verticalmente -> no hay 3 O alineadas verticalmente }
  requiere: { En la matriz si hay 3 O alineadas verticalmente -> no hay 3 X alineadas verticalmente }
  requiere: { En la matriz si hay 3 X alineadas horizontalmente -> no hay 3 O alineadas horizontalmente }
  requiere: { En la matriz si hay 3 O alineadas horizontalmente -> no hay 3 X alineadas horizontalmente }
  requiere: { Para todo i, j in {0, 1, 2} -> m[i][j] = 'X' v m[i][j] = 'O' v m[i][j] = ' ' }
  asegura: { Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0 }
  asegura: { Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1 }
  asegura: { Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2 }
}
```

**7. Opcional:** Implementar una función que tome un entero $d$ y otro $p$ y eleve una matriz cuadrada de tamaño $d$ con valores generados al azar a la potencia $p$. Es decir, multiplique a la matriz generada al azar por sí misma $p$ veces. Realizar experimentos con diferentes valores de $d$. ¿Qué pasa con valores muy grandes?
```text
problema exponenciacion_matriz (in d: Z, in p: Z) : seq⟨seq⟨Z⟩⟩ {
  requiere: { d, p in Z y d, p > 0 }
  asegura: { esMatriz(m) y |columna(m, 0)| = d y |columna(transponer(m), 0)| = d y res = prod_{i=1}^p m }
}
```
* **Nota 1:** recordá que en la multiplicación de una matriz cuadrada de dimensión $d$ por sí misma cada posición se calcula como $res[i][j] = \sum_{k=0}^{d-1} (m[i][k] \times m[k][j])$
* **Nota 2:** para generar una matriz cuadrada de dimensión $d$ con valores aleatorios hay muchas opciones de implementación, analizar las siguientes usando la biblioteca `numpy`:
  * Opción 1:
    ```python
    import numpy as np
    m = np.random.random((d, d))
    ```
  * Opción 2:
    ```python
    import numpy as np
    m = np.random.randint(i, f, (d, d))
    ```

---

## 4. Programas interactivos usando secuencias

### Ejercicio 7
Vamos a elaborar programas interactivos (usando la función `input()`) que nos permita solicitar al usuario información cuando usamos las funciones.

1. Implementar una función para construir una lista con los nombres de mis estudiantes. La función solicitará al usuario los nombres hasta que ingrese la palabra `"listo"`, o vacío (el usuario aprieta ENTER sin escribir nada). Devuelve la lista con todos los nombres ingresados.
2. Implementar una función que devuelve una lista con el historial de un monedero electrónico (por ejemplo la SUBE). El usuario debe seleccionar en cada paso si quiere:
   * `"C"` = Cargar créditos,
   * `"D"` = Descontar créditos,
   * `"X"` = Finalizar la simulación (terminar el programa).  
   En los casos de cargar y descontar créditos, el programa debe además solicitar el monto para la operación. Vamos a asumir que el monedero comienza en cero. Para guardar la información grabaremos en el historial tuplas que representen los casos de cargar `("C", monto a cargar)` y descontar crédito `("D", monto a descontar)`.
3. Vamos a escribir un programa para simular el juego conocido como **7 y medio**. El mismo deberá generar un número aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deberá luego preguntarle al usuario si desea seguir sacando otra "carta" o plantarse. En este último caso el programa debe terminar. Los números aleatorios obtenidos deberán sumarse según el número obtenido salvo por las "figuras" (10, 11 y 12) que sumarán medio punto cada una. El programa debe ir acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la función devuelve el historial de "cartas" que hizo que el usuario gane o pierda. Para generar números pseudo-aleatorios entre 1 y 12 utilizaremos la función `random.randint(1, 12)`. Al mismo tiempo, la función `random.choice()` puede ser de gran ayuda a la hora de repartir cartas.
4. **Analizar la fortaleza de una contraseña.** Solicitar al usuario que ingrese un texto que será su contraseña. Armar una función que tenga de parámetro de entrada un string con la contraseña a analizar, y la salida otro string con tres posibles valores: `VERDE`, `AMARILLA` y `ROJA`. *(Nota: en Python la `"ñ/Ñ"` es considerado un carácter especial y no se comporta como cualquier otra letra. String es `seq⟨Char⟩`. Consejo: para ver si una letra es mayúscula se puede ver si está ordenada entre A y Z).*
   * La contraseña será `VERDE` si:
     a) la longitud es mayor a 8 caracteres,
     b) tiene al menos 1 letra minúscula,
     c) tiene al menos 1 letra mayúscula,
     d) tiene al menos 1 dígito numérico (`0..9`).
   * La contraseña será `ROJA` si:
     a) la longitud es menor a 5 caracteres.
   * En caso contrario será `AMARILLA`.

---

# Guía Práctica 8: Pilas, Colas, Diccionarios y Archivos

## 1. Pilas

### Ejercicio 1
Implementar una solución para el siguiente problema.
```text
problema generar_nros_al_azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
  requiere: { cantidad >= 0 }
  requiere: { desde <= hasta }
  asegura: { El tamaño de res es igual a cantidad }
  asegura: { Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente con probabilidad uniforme }
}
```
Para generar números en un rango con probabilidad uniforme, pueden usar la función `random.randint(<desde>, <hasta>)`. Recuerden importar el módulo `random` con `import random`. Además, pueden usar la clase `LifoQueue()` que es un ejemplo de una implementación básica de una pila:
```python
from queue import LifoQueue as Pila # importa LifoQueue y le asigna el alias Pila

p = Pila()          # crea una pila
p.put(1)            # apila un 1
elemento = p.get()  # desapila
p.empty()           # devuelve true si y solo si la pila está vacía
```

### Ejercicio 2
Implementar una solución para el siguiente problema.
```text
problema cantidad_elementos (in p: Pila) : Z {
  requiere: { True }
  asegura: { res es igual a la cantidad de elementos que contiene p }
}
```
*No se puede utilizar la función `LifoQueue.qsize()`. Tener en cuenta que, al usar `get()` para recorrer la pila, se modifica el parámetro de entrada, ya que los elementos se eliminan al accederse. Dado que la especificación lo define como de tipo `in`, debe restaurarse posteriormente.*

### Ejercicio 3
Implementar una solución para el siguiente problema.
```text
problema buscar_el_maximo (in p: Pila[Z]) : Z {
  requiere: { p no está vacía }
  asegura: { res es un elemento de p }
  asegura: { res es mayor o igual a todos los elementos de p }
}
```

### Ejercicio 4
Implementar una solución para el siguiente problema.
```text
problema buscar_nota_maxima (in p: Pila[seq⟨Char⟩ x Z]) : seq⟨Char⟩ x Z {
  requiere: { p no está vacía }
  requiere: { los elementos de p no tienen valores repetidos en la segunda posición de las tuplas }
  asegura: { res es una tupla de p }
  asegura: { No hay ningún elemento en p cuya segunda componente sea mayor que la segunda componente de res }
}
```

### Ejercicio 5
Implementar una solución, que use pila, para el siguiente problema.
```text
problema esta_bien_balanceada (in s: seq⟨Char⟩) : Bool {
  requiere: { s solo puede tener números enteros, espacios y los símbolos '(', ')', '+', '-', '*', '/' }
  asegura: { res = true <-> (La cantidad de paréntesis de apertura '(' es igual a la de cierre ')') y (Para todo prefijo de 's', la cantidad de paréntesis de cierre no supera a la de apertura) }
}
```
Por cada paréntesis de cierre debe haber uno de apertura correspondiente antes de él. Las fórmulas pueden tener:
* números enteros
* operaciones básicas `+`, `-`, `*` y `/`
* paréntesis
* espacios

Entonces las siguientes son fórmulas aritméticas con sus paréntesis bien balanceados:
* `1 + (2 x 3 - (20 / 5))`
* `10 * ( 1 + ( 2 * ( -1)))`

Y la siguiente es una fórmula que no tiene los paréntesis bien balanceados:
* `1 + ) 2 x 3 ( ( )`

### Ejercicio 6
La notación polaca inversa, también conocida como notación postfix, es una forma de escribir expresiones matemáticas en la que los operadores siguen a sus operandos. Por ejemplo, la expresión `"3 + 4"` se escribe como `"3 4 +"` en notación postfix. Para evaluar una expresión en notación postfix, se puede usar una pila. Implementar una solución para el siguiente problema.
```text
problema evaluar_expresion (in s: seq⟨Char⟩) : R {
  requiere: { s solo contiene números enteros y los operadores binarios '+', '-', '*' y '/' }
  requiere: { Todos los elementos (operandos y operadores) están separados por un único espacio }
  requiere: { La expresión es sintácticamente válida: cada operador binario tiene exactamente dos operandos previos disponibles en el momento de su evaluación }
  asegura: { res es el valor obtenido al evaluar la expresión postfija representada por s }
}
```
Para resolver este problema, se recomienda seguir el siguiente algoritmo:
1. Dividir la expresión en tokens (operandos y operadores) utilizando espacios como delimitadores.
2. Recorre los tokens uno por uno.
   a) Si es un operando, agrégalo a una pila.
   b) Si es un operador, saca los dos operandos superiores de la pila, aplícale el operador y luego coloca el resultado en la pila.
3. Al final de la evaluación, la pila contendrá el resultado de la expresión.

Ejemplo de uso:
```python
expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado) # Debería imprimir 33
```

### Ejercicio 7
Implementar una solución para el siguiente problema.
```text
problema intercalar (in p1: Pila, in p2: Pila) : Pila {
  requiere: { p1 y p2 tienen la misma cantidad de elementos }
  asegura: { res solo contiene los elementos de p1 y p2 }
  asegura: { res contiene todos los elementos de p1 y p2, intercalados y respetando el orden original }
  asegura: { El tope de la pila res es el tope de p2 }
  asegura: { El tamaño de res es igual al doble del tamaño de p1 }
}
```
*Nota: Ojo que hay que recorrer dos veces para que queden en el orden apropiado al final.*

---

## 2. Colas

### Ejercicio 8
Implementar una solución para el siguiente problema.
```text
problema generar_nros_al_azar (in cantidad: Z, in desde: Z, in hasta: Z) : Cola[Z] {
  requiere: { cantidad >= 0 }
  requiere: { desde <= hasta }
  asegura: { El tamaño de res es igual a cantidad }
  asegura: { Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente con probabilidad uniforme }
}
```
Pueden usar la clase `Queue()` que es un ejemplo de una implementación básica de una Cola:
```python
from queue import Queue as Cola # importa Queue y le asigna el alias Cola

c = Cola()          # creo una cola
c.put(1)            # encolo el 1
elemento = c.get()  # desencolo
c.empty()           # devuelve true si y solo si la cola está vacía
```

### Ejercicio 9
Implementar una solución para el siguiente problema.
```text
problema cantidad_elementos (in c: Cola) : Z {
  requiere: { True }
  asegura: { res es igual a la cantidad de elementos que contiene c }
}
```
*No se puede utilizar la función `Queue.qsize()`. Comparar el resultado con la implementación utilizando una pila en lugar de una cola.*

### Ejercicio 10
Implementar una solución para el siguiente problema.
```text
problema buscar_el_maximo (in c: Cola[Z]) : Z {
  requiere: { c no está vacía }
  asegura: { res es un elemento de c }
  asegura: { res es mayor o igual a todos los elementos de c }
}
```
*Comparar con la versión usando pila.*

### Ejercicio 11
Implementar una solución para el siguiente problema.
```text
problema buscar_nota_minima (in c: Cola[seq⟨Char⟩ x Z]) : (seq⟨Char⟩ x Z) {
  requiere: { c no está vacía }
  requiere: { los elementos de c no tienen valores repetidos en la segunda componente de las tuplas }
  asegura: { res es una tupla de c }
  asegura: { No hay ningún elemento en c cuya segunda componente sea menor que la de res }
}
```

### Ejercicio 12
Implementar una solución para el siguiente problema.
```text
problema intercalar (in c1: Cola, in c2: Cola) : Cola {
  requiere: { c1 y c2 tienen la misma cantidad de elementos }
  asegura: { res solo contiene los elementos de c1 y c2 }
  asegura: { res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original }
  asegura: { El primer elemento de res es el primer elemento de c1 }
  asegura: { El tamaño de res es igual al doble del tamaño de c1 }
}
```

### Ejercicio 13
**Bingo:** un cartón de bingo contiene 12 números al azar en el rango `[0, 99]`. Implementar una solución para cada uno de los siguientes problemas.

**1.**
```text
problema armar_secuencia_de_bingo () : Cola[Z] {
  requiere: { True }
  asegura: { res solo contiene 100 números del 0 al 99 inclusive, sin repetidos }
  asegura: { Los números de res están ordenados al azar }
}
```

**2.**
```text
problema jugar_carton_de_bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
  requiere: { carton solo contiene 12 números, sin repetidos, con valores entre 0 y 99, ambos inclusive }
  requiere: { bolillero solo contiene 100 números, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos }
  asegura: { res es la cantidad mínima de jugadas necesarias para que todos los números del carton hayan salido del bolillero }
}
```

### Ejercicio 14
Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atención para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la más urgente y requiere atención inmediata) junto con su nombre y la especialidad médica que le corresponde. Implementar una solución para el siguiente problema.
```text
problema pacientes_urgentes (in c: Cola[Z x seq⟨Char⟩ x seq⟨Char⟩]) : Z {
  requiere: { Todos los elementos de c tienen como primer componente de la tupla un entero positivo y menor a 11 }
  asegura: { res es la cantidad de elementos de c que tienen como primer componente de la tupla un número menor a 4 }
}
```

### Ejercicio 15
La gerencia de un banco nos pide modelar la atención de los clientes usando una cola donde se van registrando los pedidos de atención. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que está a la entrada: Nombre y Apellido, DNI, tipo de cuenta (`True` si es preferencial o `False` en el caso contrario) y si tiene prioridad (`True` o `False`) por ser adulto +65, embarazada o con movilidad reducida.

La atención a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta bancaria preferencial y por último el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
1. Dar una especificación para el problema planteado.
2. Implementar `atencion_a_clientes(in c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]` que dada la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.

---

## 3. Diccionarios

### Ejercicio 16
Implementar una solución para el siguiente problema.
```text
problema calcular_promedio_por_estudiante (in notas: seq⟨seq⟨Char⟩ x R⟩) : Diccionario⟨seq⟨Char⟩, R⟩ {
  requiere: { El primer componente de las tuplas de notas no es una cadena vacía }
  requiere: { El segundo componente de las tuplas de notas está en el rango [0, 10] }
  asegura: { Todas las claves de res son nombres que aparecen en notas (primer componente) }
  asegura: { Todos los nombres de notas (primer componente) son clave en res }
  asegura: { El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (segundo componente de notas) }
}
```
Por ejemplo:
* `notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]`
* `calcular_promedio_por_estudiante(notas)` debe devolver `{"Sole": 9.25, "Maxi": 8.0}`

### Ejercicio 17
Se debe desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los usuarios del sistema. El navegador debe permitir al usuario navegar hacia atrás en la historia de navegación.
1. Crea un diccionario llamado `historiales` que almacenará el historial de navegación para cada usuario. Las claves del diccionario serán los nombres de usuario y los valores serán pilas de `String`.
2. Implementar una solución para el siguiente problema:
```text
problema visitar_sitio (inout historiales: Diccionario⟨seq⟨Char⟩, Pila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩) {
  requiere: { Ninguno de los Strings de los parámetros es vacío }
  asegura: { Si usuario es una de las claves de historiales@pre, entonces se agrega sitio a su pila de historiales@pre[usuario] }
  asegura: { Si usuario no es una de las claves de historiales@pre, entonces historiales[usuario] es igual a la pila que tiene solo el elemento sitio }
  asegura: { No se modifica ningún otro historial salvo, si existe, el de usuario }
  asegura: { Todos los pares clave-valor de historiales@pre están en historiales }
  asegura: { Todos los pares clave-valor de historiales están en historiales@pre, salvo historiales[usuario] que podría no existir en historiales@pre }
}
```
3. Implementar una solución para el siguiente problema:
```text
problema navegar_atras (inout historiales: Diccionario⟨seq⟨Char⟩, Pila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: { Ninguno de los Strings de los parámetros es vacío }
  requiere: { usuario es una clave de historiales }
  requiere: { La pila asociada a usuario no está vacía }
  asegura: { res es igual al tope de historiales@pre[usuario] }
  asegura: { historiales[usuario] es igual a historiales@pre[usuario] quitando el tope de la pila de historiales@pre[usuario] }
  asegura: { En historiales, salvo la pila asociada a usuario, no se modifica ningún otro par clave-valor }
}
```
Ejemplo de uso:
```python
historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
```

### Ejercicio 18
Se debe desarrollar un sistema de gestión de inventario para una tienda de ropa. Este sistema debe permitir llevar un registro de los productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y calcular el valor total del inventario.  
Para resolver este problema vamos a utilizar un diccionario llamado `inventario` que almacenará la información de los productos. En este diccionario, cada clave será el nombre de un producto, y su valor asociado será otro diccionario con los atributos del producto (`'precio'` y `'cantidad'`, cuyos valores serán de tipo `float` e `int`, respectivamente).  
Un ejemplo de inventario, con un solo producto, es: `{"remera": {"precio": 999.99, "cantidad": 3}}`.

*Nota sobre tipado:*
* En Python 3.9: `from typing import Union` -> `mi_diccionario: dict[str, Union[int, float]]`
* En Python 3.10+: `mi_diccionario: dict[str, int | float]`

**1.**
```text
problema agregar_producto (inout inventario: Diccionario⟨seq⟨Char⟩, Diccionario⟨seq⟨Char⟩, T⟩⟩, in nombre: seq⟨Char⟩, in precio: R, in cantidad: Z) {
  requiere: { T in [Z, R] }
  requiere: { cantidad > 0 }
  requiere: { precio >= 0 }
  requiere: { Ninguno de los Strings de los parámetros es vacío }
  requiere: { nombre no es una clave de inventario }
  asegura: { Todos los pares clave-valor de inventario@pre están tal cual en inventario }
  asegura: { Todos los pares clave-valor de inventario están en inventario@pre y, además, hay una nueva con clave igual a nombre y como valor tendrá un diccionario con los pares clave-valor ("precio", precio) y ("cantidad", cantidad) }
}
```

**2.**
```text
problema actualizar_stock (inout inventario: Diccionario⟨seq⟨Char⟩, Diccionario⟨seq⟨Char⟩, T⟩⟩, in nombre: seq⟨Char⟩, in cantidad: Z) {
  requiere: { T in [Z, R] }
  requiere: { cantidad >= 0 }
  requiere: { nombre es una clave existente en el inventario }
  requiere: { Ninguno de los Strings de los parámetros es vacío }
  asegura: { Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del que tiene como clave nombre }
  asegura: { Todos los pares clave-valor de inventario están en inventario@pre }
  asegura: { En inventario, el valor asociado a la clave nombre, tendrá el mismo precio que antes y la cantidad será cantidad }
}
```

**3.**
```text
problema actualizar_precio (inout inventario: Diccionario⟨seq⟨Char⟩, Diccionario⟨seq⟨Char⟩, T⟩⟩, in nombre: seq⟨Char⟩, in precio: R) {
  requiere: { T in [Z, R] }
  requiere: { precio >= 0 }
  requiere: { nombre es una clave existente en el inventario }
  requiere: { Ninguno de los Strings de los parámetros es vacío }
  asegura: { Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del valor que tiene como clave nombre }
  asegura: { Todos los pares clave-valor de inventario están en inventario@pre }
  asegura: { En inventario el diccionario asociado a nombre, tendrá la misma cantidad que antes y el precio será precio }
}
```

**4.**
```text
problema calcular_valor_inventario (in inventario: Diccionario⟨seq⟨Char⟩, Diccionario⟨seq⟨Char⟩, T⟩⟩) : R {
  requiere: { T in [Z, R] }
  requiere: { Ninguno de los Strings del inventario es vacío }
  asegura: { res es la suma, para cada producto, del precio multiplicado por la cantidad }
}
```

Ejemplo de uso:
```python
inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Debería imprimir 1100.0
```

---

## 4. Archivos

Para usar archivos contamos con las funciones: `open`, `close`, `read`, `readline`, `readlines`, `write`, `os.path.join()`, `os.path.exists()`.  
* Una línea termina cuando hay un salto de línea: un carácter `\n`.
* Una palabra es una secuencia de caracteres alfabéticos (y opcionalmente números o guiones) separada por espacios o puntuación (`.,;: "'!¡¿?()[]{ }><\n`).

### Ejercicio 19
Implementar una solución para cada uno de los siguientes problemas.

**1.**
```text
problema contar_lineas (in nombre_archivo: seq⟨Char⟩) : Z {
  requiere: { nombre_archivo es el path con el nombre de un archivo existente y accesible }
  asegura: { res es igual a la cantidad de líneas que contiene el archivo indicado por nombre_archivo }
}
```

**2.**
```text
problema existe_palabra (in nombre_archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Bool {
  requiere: { nombre_archivo es el path con el nombre de un archivo existente y accesible }
  requiere: { palabra no es vacía }
  asegura: { res es verdadero si y solo si palabra aparece al menos una vez en el archivo indicado por nombre_archivo }
}
```

**3.**
```text
problema cantidad_de_apariciones (in nombre_archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Z {
  requiere: { nombre_archivo es el path con el nombre de un archivo existente y accesible }
  requiere: { palabra no es vacía }
  asegura: { res es la cantidad de veces que palabra aparece en el archivo indicado por nombre_archivo }
}
```

### Ejercicio 20
Implementar una solución para el siguiente problema *(considerando como palabras todas aquellas secuencias de caracteres delimitadas por espacios en blanco)*.
```text
problema agrupar_por_longitud (in nombre_archivo: seq⟨Char⟩) : Diccionario⟨Z, Z⟩ {
  requiere: { nombre_archivo es el path con el nombre de un archivo existente y accesible }
  asegura: { Para cada longitud n tal que existe al menos una palabra de longitud n en el archivo indicado por nombre_archivo, res[n] es igual a la cantidad de palabras de esa longitud }
  asegura: { No hay otras claves en res que no correspondan a longitudes de palabras presentes en el archivo }
}
```

### Ejercicio 21
Implementar una solución para el siguiente problema.
```text
problema la_palabra_mas_frecuente (in nombre_archivo: seq⟨Char⟩) : seq⟨Char⟩ {
  requiere: { nombre_archivo es un archivo existente y accesible que tiene, por lo menos, una palabra }
  asegura: { res es una palabra que aparece en el archivo nombre_archivo }
  asegura: { No hay ninguna palabra contenida en el archivo nombre_archivo que aparezca más veces que la palabra res }
}
```

### Ejercicio 22
Implementar una solución para el siguiente problema. *(Una línea es un comentario si tiene un `'#'` como primer carácter de la línea, o si todos los caracteres anteriores son espacios).*
```text
problema clonar_sin_comentarios (in nombre_archivo_entrada: seq⟨Char⟩, in nombre_archivo_salida: seq⟨Char⟩) {
  requiere: { nombre_archivo_entrada es el path con el nombre de un archivo existente y accesible }
  requiere: { nombre_archivo_salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no existe, se puede crear }
  asegura: { El archivo indicado por nombre_archivo_salida contiene las mismas líneas y en el mismo orden que el archivo nombre_archivo_entrada, excepto aquellas que comienzan con el carácter # }
}
```

### Ejercicio 23
Implementar una solución para el siguiente problema.
```text
problema invertir_lineas (in nombre_archivo_entrada: seq⟨Char⟩, in nombre_archivo_salida: seq⟨Char⟩) {
  requiere: { nombre_archivo_entrada es el path de un archivo de texto existente y accesible }
  requiere: { nombre_archivo_salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no existe, se puede crear }
  asegura: { El archivo indicado por nombre_archivo_salida contiene las mismas líneas que el archivo nombre_archivo_entrada, pero en orden inverso }
}
```

### Ejercicio 24
Implementar una solución para el siguiente problema *(modifica el archivo original sin crear copia)*.
```text
problema agregar_frase_al_final (in nombre_archivo: seq⟨Char⟩, in frase: seq⟨Char⟩) {
  requiere: { nombre_archivo es el path de un archivo existente y accesible }
  requiere: { frase no es vacía }
  asegura: { frase se agrega como una nueva línea al final del archivo nombre_archivo }
}
```

### Ejercicio 25
Implementar una función que agregue la frase al comienzo del archivo original *(modifica el archivo original sin crear copia)*.
```text
problema agregar_frase_al_principio (in nombre_archivo: seq⟨Char⟩, in frase: seq⟨Char⟩) {
  requiere: { nombre_archivo es el path de un archivo existente y accesible }
  requiere: { frase no es vacía }
  asegura: { frase se agrega como primera línea del archivo nombre_archivo, desplazando las anteriores hacia abajo }
}
```

### Ejercicio 26
Implementar una solución para el siguiente problema.
```text
problema listar_textos_de_archivo (in nombre_archivo: seq⟨Char⟩) : seq⟨seq⟨Char⟩⟩ {
  requiere: { nombre_archivo es el path de un archivo existente y accesible }
  asegura: { res contiene exactamente los textos legibles que aparecen en el archivo nombre_archivo }
}
```
Definimos un texto como legible si:
* solo contiene secuencias de caracteres legibles (números, letras mayúsculas/minúsculas, espacios o `'_'` guión bajo)
* tienen longitud $\ge 5$

### Ejercicio 27
Implementar una solución para el siguiente problema.
```text
problema calcular_promedio_por_estudiante (in nombre_archivo_notas: seq⟨Char⟩, in nombre_archivo_promedios: seq⟨Char⟩) {
  requiere: { nombre_archivo_notas es el path de un archivo existente y accesible, con formato CSV: cada línea tendrá número de LU, materia, fecha y nota, todo separado por comas }
  requiere: { nombre_archivo_promedios es el path de un archivo distinto, accesible para escritura }
  asegura: { El archivo nombre_archivo_promedios contiene una línea por estudiante del archivo nombre_archivo_notas, con su LU y su promedio separados por una coma }
}
```
Función auxiliar sugerida:
```text
problema promedio_estudiante (in notas_de_estudiantes: seq⟨seq⟨Char⟩⟩, in lu: seq⟨Char⟩) : R {
  requiere: { notas_de_estudiantes tiene el contenido del archivo de notas. Cada elemento de la lista es una línea de ese archivo, con formato CSV: tendrá número de LU, materia, fecha y nota, todo separado por comas }
  requiere: { lu corresponde a una LU presente en notas_de_estudiantes }
  asegura: { res es el promedio de las notas asociadas a lu en notas_de_estudiantes }
}
```

---

# Guía Práctica 9: Testing de caja blanca

### Ejercicio 1
Sea el siguiente programa:
```python
def max(x: int, y: int) -> int:
    result: int = 0  # L1
    if x < y:        # L2
        result = y   # L3
    else:
        result = x   # L4
    return result    # L5
```
Y los siguientes casos de test:
* **test1:** Entrada `x = 0, y = 0` | Resultado esperado `result = 0`
* **test2:** Entrada `x = 0, y = 1` | Resultado esperado `result = 1`

1. Describir el diagrama de control de flujo (control-flow graph) del programa `max`.
2. Detallar qué líneas del programa cubre cada test (`L1` a `L5`).
3. Detallar qué decisiones (branches `L2-True`, `L2-False`) del programa cubre cada test.
4. Decidir si la siguiente afirmación es verdadera o falsa: *"El test suite compuesto por test1 y test2 cubre el 100% de las líneas del programa y el 100% de las decisiones (branches) del programa"*. Justificar.

### Ejercicio 2
Sea la siguiente especificación del problema de retornar el mínimo elemento entre dos números enteros:
```text
problema min (in x: Z, in y: Z) : Z {
  requiere: { True }
  asegura: { (x < y -> result = x) ^ (x >= y -> result = y) }
}
```
Un programador ha escrito el siguiente programa:
```python
def min(x: int, y: int) -> int:
    result: int = 0  # L1
    if x < y:        # L2
        result = x   # L3
    else:
        result = x   # L4
    return result    # L5
```
Y el siguiente conjunto de casos de test (test suite):
* **minA:** Entrada `x = 0, y = 1` | Salida esperada `0`
* **minB:** Entrada `x = 1, y = 1` | Salida esperada `1`

1. Describir el diagrama de control de flujo del programa `min`.
2. ¿La ejecución del test suite resulta en la ejecución de todas las líneas del programa `min`?
3. ¿La ejecución del test suite resulta en la ejecución de todas las decisiones (branches) del programa?
4. ¿Es el test suite capaz de detectar el defecto de la implementación del problema de encontrar el mínimo?
5. Agregar nuevos casos de tests y/o modificar casos de tests existentes para que el test suite detecte el defecto.

### Ejercicio 3
Sea la siguiente especificación del problema de sumar y una posible implementación:
```text
problema sumar (in x: Z, in y: Z) : Z {
  requiere: { True }
  asegura: { result = x + y }
}
```
```python
def sumar(x: int, y: int) -> int:
    result: int = 0      # L1
    result = result + x  # L2
    result = result + y  # L3
    return result        # L4
```
1. Describir el diagrama de control de flujo del programa `sumar`.
2. Escribir un conjunto de casos de test que ejecute todas las líneas del programa `sumar`.

### Ejercicio 4
Sea la siguiente especificación del problema de restar y una posible implementación:
```text
problema restar (in x: Z, in y: Z) : Z {
  requiere: { True }
  asegura: { result = x - y }
}
```
```python
def restar(x: int, y: int) -> int:
    result: int = 0      # L1
    result = result + x  # L2
    result = result + y  # L3
    return result        # L4
```
1. Describir el diagrama de control de flujo del programa `restar`.
2. Escribir un conjunto de casos de test que ejecute todas las líneas del programa `restar`.
3. La línea `L3` del programa `restar` tiene un defecto, ¿es el test suite descripto en el punto anterior capaz de detectarlo? En caso contrario, modificar o agregar nuevos casos de test hasta lograr detectarlo.

### Ejercicio 5
Sea la siguiente especificación del problema de signo y una posible implementación:
```text
problema signo (in x: R) : Z {
  requiere: { True }
  asegura: { (result = 0 ^ x = 0) v (result = -1 ^ x < 0) v (result = 1 ^ x > 0) }
}
```
```python
def signo(x: float) -> int:
    result: int = 0  # L1
    if x < 0:        # L2
        result = -1  # L3
    elif x > 0:      # L4
        result = 1   # L5
    return result    # L6
```
1. Describir el diagrama de control de flujo del programa `signo`.
2. Escribir un test suite que ejecute todas las líneas del programa `signo`.
3. ¿El test suite del punto anterior ejecuta todas las posibles decisiones ("branches") del programa?

### Ejercicio 6
Sea la siguiente especificación del problema de `fabs` y una posible implementación:
```text
problema fabs (in x: R) : R {
  requiere: { True }
  asegura: { result = |x| }
}
```
```python
def fabs(x: float) -> float:
    result: float = 0  # L1
    if x < 0:          # L2
        result = -x    # L3
    return result      # L4
```
1. Describir el diagrama de control de flujo del programa `fabs`.
2. Escribir un test suite que ejecute todas las líneas del programa `fabs`.
3. Escribir un test suite que ejecute todas las posibles decisiones ("branches") del programa.
4. Escribir un test suite que ejecute todas las líneas del programa pero no ejecute todas las decisiones del programa.
5. ¿Los test suites de los puntos anteriores detectan el defecto en la implementación? De no ser así, modificarlos para que lo hagan.

### Ejercicio 7
Sea la siguiente especificación e implementación de `fabs`:
```text
problema fabs (in x: Z) : Z {
  requiere: { True }
  asegura: { result = |x| }
}
```
```python
def fabs(x: int) -> int:
    if x < 0:      # L1
        return -x  # L2
    else:
        return x   # L3
```
1. Describir el diagrama de control de flujo del programa `fabs`.
2. Escribir un test suite que ejecute todas las líneas y todos los branches del programa.

### Ejercicio 8
Sea la siguiente especificación e implementación de `mult10`:
```text
problema mult10 (in x: Z) : Z {
  requiere: { True }
  asegura: { result = x * 10 }
}
```
```python
def mult10(x: int) -> int:
    result: int = 0          # L1
    count: int = 0           # L2
    while (count < 10):      # L3
        result = result + x  # L4
        count = count + 1    # L5
    return result            # L6
```
1. Describir el diagrama de control de flujo del programa `mult10`.
2. Escribir un test suite que ejecute todas las líneas del programa `mult10`.
3. ¿El test suite anterior ejecuta todas las posibles decisiones ("branches") del programa?

### Ejercicio 9
Sea la siguiente especificación e implementación de `sumar`:
```text
problema sumar (in x: Z, in y: Z) : Z {
  requiere: { True }
  asegura: { result = x + y }
}
```
```python
def sumar(x: int, y: int) -> int:
    sumando: int = 0               # L1
    abs_y: int = 0                 # L2
    if y < 0:                      # L3
        sumando = -1               # L4
        abs_y = -y                 # L5
    else:
        sumando = 1                # L6
        abs_y = y                  # L7
    result: int = x                # L8
    count: int = 0                 # L9
    while (count < abs_y):         # L10
        result = result + sumando  # L11
        count = count + 1          # L12
    return result                  # L13
```
1. Describir el diagrama de control de flujo del programa `sumar`.
2. Escribir un test suite que ejecute todas las líneas del programa `sumar`.
3. Escribir un test suite que ejecute todas las posibles decisiones ("branches") del programa.

### Ejercicio 10
Sea el siguiente programa que computa el máximo común divisor entre dos enteros:
```python
def mcd(x: int, y: int) -> int:
    # requiere: x e y tienen que ser no negativos  # L1
    tmp: int = 0                                   # L2
    while (y != 0):                                # L3
        tmp = x % y                                # L4
        x = y                                      # L5
        y = tmp                                    # L6
    return x                                       # L7
```
1. Describir el diagrama de control de flujo del programa `mcd`.
2. Escribir un test suite que ejecute todas las líneas y todos los branches del programa.

### Ejercicio 11
Sea el siguiente programa que retorna diferentes valores dependiendo si `a`, `b` y `c`, definen lados de un triángulo inválido, equilátero, isósceles o escaleno:
```python
def triangle(a: int, b: int, c: int) -> int:
    if (a <= 0 or b <= 0 or c <= 0):                     # L1
        return 4 # invalido                              # L2
    if (not ((a + b > c) and (a + c > b) and (b + c > a))): # L3
        return 4 # invalido                              # L4
    if (a == b and b == c):                              # L5
        return 1 # equilatero                            # L6
    if (a == b or b == c or a == c):                     # L7
        return 2 # isosceles                             # L8
    return 3 # escaleno                                  # L9
```
1. Describir el diagrama de control de flujo del programa `triangle`.
2. Escribir un test suite que ejecute todas las líneas y todos los branches del programa.

### Ejercicio 12
Sea la siguiente especificación e implementación de `multByAbs`:
```text
problema multByAbs (in x: Z, in y: Z, out result: Z) {
  requiere: { True }
  asegura: { result = x * |y| }
}
```
```python
def multByAbs(x: int, y: int) -> int:
    abs_y: int = fabs(y)        # L1 (ejercicio anterior)
    if abs_y < 0:               # L2
        return -1               # L3
    else:
        result: int = 0         # L4
        i: int = 0              # L5
        while i < abs_y:        # L6
            result = result + x # L7
            i += 1              # L8
        return result           # L9
```
1. Describir el diagrama de control de flujo del programa `multByAbs`.
2. Detallar qué líneas y branches del programa no pueden ser cubiertos por ningún caso de test. ¿A qué se debe?
3. Escribir el test suite que cubra todas las líneas y branches que puedan ser cubiertos.

### Ejercicio 13
Sea la siguiente especificación e implementación de `vaciarSecuencia`:
```text
problema vaciarSecuencia (inout s: seq⟨Z⟩) {
  requiere: { True }
  modifica: { s }
  asegura: { |s| = |s@pre| ^ s[j] = 0 para cualquier j tal que 0 <= j < |s| }
}
```
```python
def vaciarSecuencia(s: list[int]):
    for i in range(len(s)):  # L1, L2, L3
        s[i] = 0             # L4
```
1. Escribir el diagrama de control de flujo del programa `vaciarSecuencia`.
2. Escribir un test suite que cubra todas las líneas de programa (observar que un `for` contiene 3 líneas distintas).
3. En caso que el test suite del punto anterior no cubriera todos los branches del programa, extenderlo de modo que logre cubrirlos.

### Ejercicio 14
Sea la siguiente especificación e implementación de `existeElemento`:
```text
problema existeElemento (s: seq⟨Z⟩, e: Z) : Bool {
  requiere: { True }
  asegura: { result = True <-> s[j] = e para algún j tal que 0 <= j < |s| }
}
```
```python
def existeElemento(s: list[int], e: int) -> bool:
    result: bool = False     # L1
    for i in range(len(s)):  # L2, L3, L4
        if s[i] == e:        # L5
            result = True    # L6
            break            # L7
    return result            # L8
```
1. Escribir el diagrama de control de flujo del programa `existeElemento`.
2. Escribir un test suite que cubra todas las líneas de programa.
3. En caso que el test suite del punto anterior no cubriera todos los branches del programa, extenderlo de modo que logre cubrirlos.

---

# Guía Práctica 10: Guía integradora Python

### Ejercicio 1. Veterinaria - Stock
Se pide implementar una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento. La función debe procesar esta lista y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su mínimo y máximo stock histórico registrado.
```text
problema stock_productos (in stock_cambios: seq⟨str x Z⟩) : dict⟨str, Z x Z⟩ {
  requiere: { Todos los elementos de stock_cambios están formados por un str no vacío y un entero >= 0. }
  asegura: { res tiene como claves solo los primeros elementos de las tuplas de stock_cambios (o sea, un producto). }
  asegura: { res tiene como claves todos los primeros elementos de las tuplas de stock_cambios. }
  asegura: { El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese producto en stock_cambios y como segundo valor el mayor. }
}
```

### Ejercicio 2. Veterinaria - Filtrar códigos de barra
Se pide implementar una función que, dada una secuencia de enteros (cada uno representando un código de barras de un producto), cree y devuelva una nueva lista que contenga únicamente aquellos números de la lista original cuyos últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).
```text
problema filtrar_codigos_primos (in codigos_barra: seq⟨Z⟩) : seq⟨Z⟩ {
  requiere: { Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos. }
  requiere: { No hay elementos repetidos en codigos_barra. }
  asegura: { Los últimos 3 dígitos de cada uno de los elementos de res forman un número primo. }
  asegura: { Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo están en res. }
  asegura: { Todos los elementos de res están en codigos_barra. }
}
```

### Ejercicio 3. Veterinaria - Flujo de pacientes
Se pide implementar una función que, dada una secuencia de `str` que representan los tipos de animales atendidos, devuelva el índice donde comienza la subsecuencia más larga que contenga solo los tipos de mascota `"perro"` o `"gato"`.
```text
problema subsecuencia_mas_larga (in tipos_pacientes_atendidos: seq⟨str⟩) : Z {
  requiere: { tipos_pacientes_atendidos tiene, por lo menos, un elemento "perro" o "gato". }
  asegura: { res es el índice donde empieza la subsecuencia más larga de tipos_pacientes_atendidos que contenga solo elementos "perro" o "gato". }
  asegura: { Si hay más de una subsecuencia de tamaño máximo, res tiene el índice de la primera. }
}
```

### Ejercicio 4. Veterinaria - Tabla turnos
Las personas responsables de los turnos están anotadas en una matriz donde las columnas representan los días (lunes a domingo) y cada fila un rango de una hora. Hay cuatro filas para los turnos de la mañana (9, 10, 11 y 12 hs) y otras cuatro para la tarde (14, 15, 16 y 17 hs).
```text
problema un_responsable_por_turno (in grilla_horaria: seq⟨seq⟨str⟩⟩) : seq⟨Bool x Bool⟩ {
  requiere: { |grilla_horaria| = 8. }
  requiere: { Todos los elementos de grilla_horaria tienen el mismo tamaño (mayor a 0 y menor a 8). }
  requiere: { No hay cadenas vacías en las listas de grilla_horaria. }
  asegura: { |res| = |grilla_horaria[0]|. }
  asegura: { El primer valor de la tupla en res[i], con i:Z, 0 <= i < |res| es igual a True <-> los primeros 4 valores de la columna i de grilla_horaria son iguales entre sí. }
  asegura: { El segundo valor de la tupla en res[i], con i:Z, 0 <= i < |res| es igual a True <-> los últimos 4 valores de la columna i de grilla_horaria son iguales entre sí. }
}
```

### Ejercicio 5. Sala de Escape - Promedio de salidas
Un `0` significa que no fueron, un `61` que no lograron salir a tiempo, y un número entre `1` y `60` representa los minutos que les tomó escapar exitosamente.
```text
problema promedio_de_salidas (in registro: dict⟨str, seq⟨Z⟩⟩) : dict⟨str, ⟨Z x R⟩⟩ {
  requiere: { registro tiene por lo menos un integrante. }
  requiere: { Todos los integrantes de registro tienen por lo menos un tiempo. }
  requiere: { Todos los valores de registro tienen la misma longitud. }
  requiere: { Todos los tiempos de los valores de registro están entre 0 y 61 inclusive. }
  asegura: { res tiene las mismas claves que registro. }
  asegura: { El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro. }
  asegura: { El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0. }
}
```

### Ejercicio 6. Sala de Escape - Tiempo más rápido
```text
problema tiempo_mas_rapido (in tiempos_salas: seq⟨Z⟩) : Z {
  requiere: { Hay por lo menos un elemento en tiempos_salas entre 1 y 60 inclusive. }
  requiere: { Todos los tiempos en tiempos_salas están entre 0 y 61 inclusive. }
  asegura: { res es la posición de la sala en tiempos_salas de la que más rápido se salió (en caso que haya más de una, devolver la primera, o sea la de menor índice). }
}
```

### Ejercicio 7. Sala de Escape - Racha más larga
```text
problema racha_mas_larga (in tiempos: seq⟨Z⟩) : ⟨Z x Z⟩ {
  requiere: { Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive. }
  requiere: { Todos los tiempos en tiempos están entre 0 y 61 inclusive. }
  asegura: { En la primera posición de res está la posición (índice de la lista) de la sala que inicia la racha más larga. }
  asegura: { En la segunda posición de res está la posición (índice de la lista) de la sala que finaliza la racha más larga. }
  asegura: { El elemento de la primer posición de res en tiempos es mayor estricto 0 y menor estricto que 61. }
  asegura: { El elemento de la segunda posición de res en tiempos es mayor estricto 0 y menor estricto que 61. }
  asegura: { La primera posición de res es menor o igual a la segunda posición de res. }
  asegura: { No hay valores iguales a 0 o a 61 en tiempos entre la primer posición de res y la segunda posición de res. }
  asegura: { No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que está entre la primer posición de res y la segunda posición de res. }
  asegura: { Si hay dos o más subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera de ellas. }
}
```

### Ejercicio 8. Sala de Escape - Escape en solitario
```text
problema escape_en_solitario (in amigos_por_salas: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: { Hay por lo menos una sala en amigos_por_salas. }
  requiere: { Hay 4 amigos en amigos_por_salas. }
  requiere: { Todos los tiempos en cada sala de amigos_por_salas están entre 0 y 61 inclusive. }
  asegura: { La longitud de res es menor igual que la longitud de amigos_por_salas. }
  asegura: { Por cada sala en amigos_por_salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0, la posición de dicha sala en amigos_por_salas debe aparecer en res. }
  asegura: { Para todo i perteneciente a res se cumple que el primer, segundo y cuarto valor de amigos_por_salas[i] es 0, y el tercer valor es distinto de 0. }
}
```

### Ejercicio 9. Juego de la Gallina
* Si dos jugadores juegan y se chocan entre sí (`"me la banco y no me desvío"` ambos): pierde cada uno 5 puntos (`-5`).
* Si ambos jugadores se desvían (`"me desvío siempre"` ambos): pierde cada uno 10 puntos (`-10`).
* Si uno no se desvía y el otro sí: el gallina pierde 15 puntos (`-15`) y el ganador suma 10 puntos (`+10`).
```text
problema torneo_de_gallinas (in estrategias: dict⟨str, str⟩) : dict⟨str, Z⟩ {
  requiere: { estrategias tiene por lo menos 2 elementos (jugadores). }
  requiere: { Las claves de estrategias tienen longitud mayor a 0. }
  requiere: { Los valores de estrategias sólo pueden ser los strs "me desvío siempre" ó "me la banco y no me desvío". }
  asegura: { Las claves de res y las claves de estrategias son iguales. }
  asegura: { Para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al finalizar el torneo, dado que jugó una vez contra cada otro jugador. }
}
```

### Ejercicio 10. Cola en el Banco
```text
problema reordenar_cola_priorizando_vips (in filaClientes: Cola⟨str x str⟩) : Cola⟨str⟩ {
  requiere: { La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0. }
  requiere: { Los valores de la segunda componente de las tuplas de la cola filaClientes son "común" o "vip". }
  requiere: { No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí. }
  asegura: { todo valor de res aparece como primera componente de alguna tupla de filaClientes. }
  asegura: { |res| = |filaClientes|. }
  asegura: { res no tiene elementos repetidos. }
  asegura: { No hay ningún cliente "común" antes que un "vip" en res. }
  asegura: { Para todo cliente c1 y cliente c2 de tipo "común" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res. }
  asegura: { Para todo cliente c1 y cliente c2 de tipo "vip" pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res. }
}
```

### Ejercicio 11. Sufijos que son palíndromos
*(Nota: Para este ejercicio no consideraremos a `""` como sufijo de ningún texto).*
```text
problema cuantos_sufijos_son_palindromos (in texto: str) : Z {
  requiere: { True }
  asegura: { res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto. }
}
```

### Ejercicio 12. Ta-Te-Ti-Facilito
```text
problema quien_gano_el_tateti_facilito (in tablero: seq⟨seq⟨Char⟩⟩) : Z {
  requiere: { tablero es una matriz cuadrada. }
  requiere: { 5 <= |tablero[0]| <= 10. }
  requiere: { tablero sólo tiene 'X', 'O' y ' ' (espacio vacío) como elementos. }
  requiere: { En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de 'O'. }
  asegura: { res = 1 <-> hay tres 'X' consecutivas en forma vertical (misma columna) y no hay tres 'O' consecutivas en forma vertical (misma columna). }
  asegura: { res = 2 <-> hay tres 'O' consecutivas en forma vertical (misma columna) y no hay tres 'X' consecutivas en forma vertical (misma columna). }
  asegura: { res = 0 <-> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical. }
  asegura: { res = 3 <-> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que Beto hizo trampa). }
}
```

### Ejercicio 13. Hospital - Atención por Guardia
```text
problema orden_de_atencion (in urgentes: cola⟨Z⟩, in postergables: cola⟨Z⟩) : cola⟨Z⟩ {
  requiere: { No hay elementos repetidos en urgentes. }
  requiere: { No hay elementos repetidos en postergables. }
  requiere: { La intersección entre postergables y urgentes es vacía. }
  requiere: { |postergables| = |urgentes|. }
  asegura: { No hay repetidos en res. }
  asegura: { res es permutación de la concatenación de urgentes y postergables. }
  asegura: { Si urgentes no es vacía, en la cabeza de res hay un elemento de urgentes. }
  asegura: { En res no hay dos seguidos de urgentes. }
  asegura: { En res no hay dos seguidos de postergables. }
  asegura: { Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res. }
  asegura: { Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res. }
}
```

### Ejercicio 14. Hospital - Alarma epidemiológica
```text
problema alarma_epidemiologica (in registros: seq⟨Z x str⟩, in infecciosas: seq⟨str⟩, in umbral: R) : dict⟨str, R⟩ {
  requiere: { 0 < umbral < 1. }
  asegura: { claves de res pertenecen a infecciosas. }
  asegura: { Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje. }
  asegura: { Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res. }
}
```

### Ejercicio 15. Hospital - Empleado del mes
```text
problema empleados_del_mes (horas: dicc⟨Z, seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: { No hay valores en horas que sean listas vacías. }
  asegura: { Si ID pertenece a res entonces ID pertenece a las claves de horas. }
  asegura: { Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs. }
  asegura: { Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertenece a res. }
}
```

### Ejercicio 16. Hospital - Nivel de ocupación
```text
problema nivel_de_ocupacion (in camas_por_piso: seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: { Todos los pisos tienen la misma cantidad de camas. }
  requiere: { Hay por lo menos 1 piso en el hospital. }
  requiere: { Hay por lo menos una cama por piso. }
  asegura: { |res| = |camas_por_piso|. }
  asegura: { Para todo 0 <= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i. }
}
```

---

# Guía Práctica 11: Medidas de análisis de programas

## 1. Cantidad de tiempo de ejecución con distintos tipos de datos, mismos problemas

En Python para medir el tiempo de ejecución podemos usar la biblioteca `time`:
```python
import time

inicio = time.time()
time.sleep(1) # Hago que se duerma 1 segundo
fin = time.time()
print(fin - inicio) # Debería imprimir aproximadamente 1 segundo
```

### Ejercicio 1
Vamos a medir el tiempo de distintas funciones que suman ($\sum_{0}^{n} i$) usando:
```python
import time

def sumatoria_con_tiempos(n: int) -> float:
    inicio: float = time.time()
    suma = sumatoria_1(n)
    fin: float = time.time()
    tiempo_segundos: float = fin - inicio
    return tiempo_segundos
```
Para las siguientes implementaciones de sumatoria:
```python
# 1. Iterativa
def sumatoria_1(n: int) -> int:
    total: int = 0
    i: int = 1
    while i < n:
        total = total + i
        i = i + 1
    return total

# 2. Fórmula cerrada
def sumatoria_2(n: int) -> int:
    total: int = (n * (n - 1)) // 2
    return total

# 3. Recursiva
def sumatoria_3(n: int) -> int:
    if n == 0:
        return 0
    return n + sumatoria_3(n - 1)
```
* Probar ejecutar varias veces con el mismo valor de entrada. ¿Qué ocurre con los tiempos? ¿Era lo que esperabas?
* Probar ejecutar con distintos valores por ejemplo `10`, `1000`, `1000000`. ¿Qué ocurre con los tiempos? ¿Era lo que esperabas?

### Ejercicio 2
Vamos a implementar y comparar los tiempos de buscar el máximo elemento de una secuencia de tamaño $n$ en una **Pila**, en una **Cola** y en una **Lista** usando `random.sample(range(desde, hasta), cantidad)`.
1. ¿Tardan lo mismo? ¿Era lo que esperabas?
2. ¿Cuál tarda más? ¿De qué depende que tarde más si todas las secuencias tienen los mismos elementos?
3. Probar poniendo el elemento más grande siempre al principio (`res.insert(0, hasta + 1)`).
4. Probar poniendo el elemento más grande siempre al final (`res.append(hasta + 1)`).

---

## 2. Cantidad de operaciones

Una forma de medir la "complejidad" de una función es a partir de contar operaciones elementales (sumas, restas, multiplicaciones, divisiones, asignaciones, condicionales, returns). Es un método agnóstico a la computadora.

### Ejercicio 3
Modificamos `sumatoria_1` para contar operaciones:
```python
def sumatoria_con_cuentas(n: int) -> tuple[int, int]:
    cant_operaciones: int = 0
    total: int = 0
    cant_operaciones += 1 # Asignación de total
    i: int = 1
    cant_operaciones += 1 # Asignación de i
    while i < n:
        cant_operaciones += 1 # Comparación
        total = total + i
        cant_operaciones += 2 # Asignación y suma
        i = i + 1
        cant_operaciones += 2 # Asignación y suma
    return total, cant_operaciones
```
1. Modificar el código de `sumatoria_2` para que devuelva la cantidad de operaciones.
2. Modificar el código de `sumatoria_3` para que devuelva la cantidad de operaciones.
3. Ejecutar los 3 programas y comparar para el mismo parámetro de entrada (`100`, `1000`, `10000`, `100000`).

---

## 3. Graficamos los resultados
```python
import matplotlib.pyplot as plt

tiempos = []
for t in range(1000, 1000000):
    tiempo = sumatoria_con_tiempos(t)
    tiempos.append(tiempo)

plt.plot(tiempos)
plt.xlabel("tamaño de la entrada")
plt.ylabel("tiempo (segundos)")
plt.title("Experimento tiempos")
plt.show()
```

---

## 4. Más ejercicios: cantidad de operaciones

### Ejercicio 4 ★
Calcular la cantidad de operaciones $T(n)$ que realiza cada una de las siguientes funciones, siendo $n$ el parámetro de entrada. ¿Cómo es el crecimiento de cada uno de los $T(n)$ con respecto a $n$ (lineal, cuadrático, exponencial, etc.)?

```python
# 1.
def producto_0(n: int) -> int:
    res: int = 1 * 2
    return res

# 2.
def producto_1(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= n:
        res = res * i
        i = i + 1
    return res

# 3.
def producto_2(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= n:
        res = res * i
        i = i + 2
    return res

# 4.
def producto_3(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= n:
        j: int = 1
        while j <= n:
            res = res * i * j
            j = j + 1
        i = i + 1
    return res

# 5.
def producto_4(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= n:
        j: int = 1
        while j <= n:
            k: int = 1
            while k <= n:
                res = res * i * j * k
                k = k + 1
            j = j + 1
        i = i + 1
    return res

# 6.
def producto_5(n: int) -> int:
    res: int = 1
    i: int = 1
    while i < n:
        res = res * i
        i = i * 2
    return res

# 7.
def producto_6(n: int) -> int:
    res: int = 1
    i: int = 1
    while i <= 2 ** n:
        producto: int = 1
        j: int = 1
        while j <= n:
            if (i // (2 ** (j - 1))) % 2 == 1:
                producto = producto * j
            else:
                producto = producto * 1
            j = j + 1
        i = i + 1
        res = res * producto
    return res
```

### Ejercicio 5
Calcular $T(n)$ para cada una de las implementaciones planteadas, siendo $n$ el tamaño de la lista `s` o la cantidad de filas de la matriz `m`. Comparar entre sí los valores de $T(n)$.

**1. ★ `maxima_diferencia`**
```python
def mayor(x: int, y: int) -> int:
    if x > y:
        res: int = x
    else:
        res: int = y
    return res

def menor(x: int, y: int) -> int:
    if x < y:
        res: int = x
    else:
        res: int = y
    return res

def valor_absoluto(n: int) -> int:
    if n > 0:
        res: int = n
    else:
        res: int = -n
    return res

def maxima_diferencia_v1(s: list[int]) -> int:
    res: int = 0
    i: int = 0
    while i < len(s):
        j: int = 0
        while j < len(s):
            res = mayor(res, valor_absoluto(s[i] - s[j]))
            j = j + 1
        i = i + 1
    return res

def maxima_diferencia_v2(s: list[int]) -> int:
    maximo: int = s[0]
    i: int = 1
    while i < len(s):
        maximo = mayor(maximo, s[i])
        i = i + 1
    minimo: int = s[0]
    i = 1
    while i < len(s):
        minimo = menor(minimo, s[i])
        i = i + 1
    return maximo - minimo

def maxima_diferencia_v3(s: list[int]) -> int:
    maximo: int = s[0]
    minimo: int = s[0]
    i: int = 1
    while i < len(s):
        maximo = mayor(maximo, s[i])
        minimo = menor(minimo, s[i])
        i = i + 1
    return maximo - minimo
```

**2. `suma_de_productos`**
```python
def suma_de_productos_v1(s: list[int]) -> int:
    res: int = 0
    i: int = 0
    while i < len(s):
        j: int = 0
        while j < len(s):
            if i != j:
                res = res + s[i] * s[j]
            j = j + 1
        i = i + 1
    return res // 2

def suma_de_productos_v2(s: list[int]) -> int:
    res: int = 0
    i: int = 0
    while i < len(s):
        j: int = i + 1
        while j < len(s):
            res = res + s[i] * s[j]
            j = j + 1
        i = i + 1
    return res
```

**3. `elementos_en_pos_pares`**
```python
def elementos_en_pos_pares_v1(s: list[int]) -> list[int]:
    res: list[int] = []
    i: int = 0
    while i < len(s):
        if i % 2 == 0:
            res.append(s[i])
        i = i + 1
    return res

def elementos_en_pos_pares_v2(s: list[int]) -> list[int]:
    res: list[int] = []
    i: int = 0
    while i < len(s):
        res.append(s[i])
        i = i + 2
    return res
```

**4. `sumar_cantidad_veces_indice`**
```python
def sumar_cantidad_veces_indice_v1(s: list[int]) -> None:
    i: int = 0
    while i < len(s):
        suma: int = 0
        j: int = 0
        while j < i:
            suma = suma + s[i]
            j = j + 1
        s[i] = s[i] + suma
        i = i + 1

def sumar_cantidad_veces_indice_v2(s: list[int]) -> None:
    i: int = 0
    while i < len(s):
        s[i] = s[i] * i
        i = i + 1
```

**5. `diagonal_principal`**
```python
def diagonal_principal_v1(m: list[list[int]]) -> list[int]:
    res: list[int] = []
    n: int = len(m)
    i: int = 0
    while i < n:
        j: int = 0
        while j < n:
            if i == j:
                res.append(m[i][j])
            j = j + 1
        i = i + 1
    return res

def diagonal_principal_v2(m: list[list[int]]) -> list[int]:
    res: list[int] = []
    n: int = len(m)
    i: int = 0
    while i < n:
        res.append(m[i][i])
        i = i + 1
    return res
```

**6. `convertir_en_matriz_identidad`**
```python
def convertir_en_matriz_identidad_v1(m: list[list[int]]) -> None:
    n: int = len(m)
    i: int = 0
    while i < n:
        j: int = 0
        while j < n:
            if i == j:
                m[i][j] = 1
            else:
                m[i][j] = 0
            j = j + 1
        i = i + 1

def convertir_en_matriz_identidad_v2(m: list[list[int]]) -> None:
    n: int = len(m)
    i: int = 0
    while i < n:
        j: int = 0
        while j < n:
            m[i][j] = 0
            j = j + 1
        m[i][i] = 1
        i = i + 1
```

**7. `sumar_elementos_matriz`**
```python
def sumar_elementos_lista(s: list[int]) -> int:
    res: int = 0
    i: int = 0
    while i < len(s):
        res = res + s[i]
        i = i + 1
    return res

def sumar_elementos_matriz_v1(m: list[list[int]]) -> int:
    suma_por_fila: list[int] = []
    i: int = 0
    while i < len(m):
        suma_por_fila.append(sumar_elementos_lista(m[i]))
        i = i + 1
    return sumar_elementos_lista(suma_por_fila)

def sumar_elementos_matriz_v2(m: list[list[int]]) -> int:
    res: int = 0
    i: int = 0
    while i < len(m):
        res = res + sumar_elementos_lista(m[i])
        i = i + 1
    return res

def sumar_elementos_matriz_v3(m: list[list[int]]) -> int:
    res: int = 0
    i: int = 0
    while i < len(m):
        j: int = 0
        while j < len(m[i]):
            res += m[i][j]
            j = j + 1
        i = i + 1
    return res
```

### Ejercicio 6
Buscar el mejor y el peor caso del parámetro de entrada. Calcular $T_{mejor}(n)$ y $T_{peor}(n)$ y comparar ambos valores entre sí.

```python
# 1. ★ contar_pares
def contar_pares(s: list[int]) -> int:
    res: int = 0
    i: int = 0
    while i < len(s):
        if s[i] % 2 == 0:
            res = res + s[i]
        i = i + 1
    return res

# 2. suma_hasta_umbral
def suma_hasta_umbral(s: list[int], umbral: int) -> int:
    res: int = 0
    i: int = 0
    while i < len(s) and s[i] < umbral:
        res = res + s[i]
        i = i + 1
    return res

# 3. contar_minimos
def contar_minimos(s: list[int]) -> int:
    minimo: int = s[0]
    i: int = 1
    while i < len(s):
        if s[i] < minimo:
            minimo = s[i]
        i = i + 1
    res: int = 0
    i = 0
    while i < len(s):
        if s[i] == minimo:
            res = res + 1
        i = i + 1
    return res

# 4. colapsar_repetidos
def colapsar_repetidos(texto: str) -> str:
    res: str = texto[0]
    i: int = 1
    while i < len(texto):
        if texto[i] != texto[i - 1]:
            res = res + texto[i]
        i = i + 1
    return res

# 5. ★ sumar_filas_negativas
def sumar_filas_negativas(m: list[list[int]]) -> int:
    res: int = 0
    i: int = 0
    while i < len(m):
        if m[i][0] < 0:
            j: int = 0
            while j < len(m[i]):
                res = res + m[i][j]
                j = j + 1
        i = i + 1
    return res
```

---

# Parcial Python - Tema 2 (Resuelto y Corregido)

* **Nota:** 8.8 / 10.0 (APROBADO)
* **Puntajes:** Ej1: 2/2 | Ej2: 1.75/2.5 | Ej3: 2.5/2.5 | Ej4: 2/2 | Ej5: 0.0/0.5 | Ej6: 0.5/0.5
* **Alumno:** Giuly Belo | **Máquina:** 37-06

---

## Enunciado y Solución Entregada

### Ejercicio 1 [2 puntos]
Implementar la función `cantidad_parejas_que_suman`:
```text
problema cantidad_parejas_que_suman (in s: seq⟨Z⟩, in n: Z) : Z {
  requiere: { - }
  asegura: { res es la cantidad de parejas s[i] y s[j] de números de s tales que s[i] + s[j] = n (con i < j) }
}
```
*Ejemplo:* `cantidad_parejas_que_suman([1, 3, 2, 5, 4, 8], 5)` debe devolver `2`.

**Solución entregada (Puntaje: 2 / 2):**
```python
def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    cantidad_parejas: int = 0
    longitud_secuencia: int = len(s)
    for indice in range(0, longitud_secuencia):
        numero_actual = s[indice]
        indice_mayor = indice + 1
        for indice_posterior in range(indice_mayor, longitud_secuencia):
            numero_posterior = s[indice_posterior]
            suma_numeros = numero_actual + numero_posterior
            if suma_numeros == n:
                cantidad_parejas += 1
    return cantidad_parejas
```

---

### Ejercicio 2 [2,5 puntos]
En un supermercado tenemos una fila de clientes esperando para ser atendidos por algún cajero. Cada cliente tiene un nombre, un método de pago y una cantidad de productos (`Cola` de `String x String x Z`). Implementar la función `pasar_por_autoservicio`:
```text
problema pasar_por_autoservicio (inout clientes: Cola⟨String x String x Z⟩) : String {
  requiere: { Las primeras componentes de clientes son strings no vacíos y todos distintos entre sí }
  requiere: { Las terceras componentes de clientes son números positivos }
  requiere: { Existe al menos un elemento c dentro de la cola clientes tal que c_1 != "efectivo" y c_2 <= 15 }
  modifica: { clientes }
  asegura: { Sea c el primer elemento insertado en la cola clientes tal que c_1 != "efectivo" y c_2 <= 15, entonces res = c_0 }
  asegura: { clientes contiene todos los elementos de clientes@pre excepto la tupla que contiene a res en su primera posición, en el mismo orden que en clientes@pre }
}
```

**Solución entregada (Puntaje: 1.75 / 2.5):**
```python
from queue import Queue as Cola

def pasar_por_autoservicio(clientes: Cola[tuple[str, str, int]]) -> str:
    clientes_nueva: Cola[tuple[str, str, int]] = Cola()
    cliente_prioridad: tuple[str, str, int] = ("", "", 0)
    while (not clientes.empty()) and cliente_prioridad == ("", "", 0):
        cliente_actual: tuple[str, str, int] = clientes.get()
        if cliente_actual[1] != "efectivo" and cliente_actual[2] <= 15:
            cliente_prioridad = cliente_actual
        else:
            clientes_nueva.put(cliente_actual)
    while not clientes.empty():
        clientes_nueva.put(clientes.get())
    
    # NOTA DE CORRECCIÓN PERSONAL EN EL PDF:
    # Para arreglar los errores alcanzaría con volcar clientes_nueva de vuelta en clientes:
    # while not clientes_nueva.empty():
    #     clientes.put(clientes_nueva.get())
    
    clientes = clientes_nueva # <-- Esto solo reasigna la variable local y deja la cola original vacía!
    return cliente_prioridad[0]
```

---

### Ejercicio 3 [2,5 puntos]
Implementar la función `intercambiar_e_invertir_columnas`:
```text
problema intercambiar_e_invertir_columnas (inout A: seq⟨seq⟨Z⟩⟩, in col1: Z, in col2: Z) {
  requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva) }
  requiere: { |A| > 0 }
  requiere: { 0 <= col1 < |A[0]| }
  requiere: { 0 <= col2 < |A[0]| }
  requiere: { col1 != col2 }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que j != col1 y j != col2 }
  asegura: { A[i][col1] = A@pre[|A| - 1 - i][col2] para todo i tal que 0 <= i < |A| }
  asegura: { A[i][col2] = A@pre[|A| - 1 - i][col1] para todo i tal que 0 <= i < |A| }
}
```

**Solución entregada (Puntaje: 2.5 / 2.5):**
```python
def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    longitud_matriz: int = len(A)
    longitud_fila: int = len(A[0])
    nueva_matriz: list[list[int]] = []
    for indice_fila in range(0, longitud_matriz):
        nueva_fila: list[int] = []
        for indice_columna in range(0, longitud_fila):
            if indice_columna == col1:
                nueva_fila.append(A[longitud_matriz - 1 - indice_fila][col2])
            elif indice_columna == col2:
                nueva_fila.append(A[longitud_matriz - 1 - indice_fila][col1])
            else:
                nueva_fila.append(A[indice_fila][indice_columna])
        nueva_matriz.append(nueva_fila)
    A.clear()
    for fila in nueva_matriz:
        fila_nueva = []
        for columna in fila:
            fila_nueva.append(columna)
        A.append(fila_nueva)
    return
```

---

### Ejercicio 4 [2 puntos]
Implementar la función `mantuvieron_residencia`:
```text
problema mantuvieron_residencia (in censo1: Diccionario⟨String, String⟩, in censo2: Diccionario⟨String, String⟩) : Diccionario⟨String, Z⟩ {
  requiere: { Las claves de censo1 son las mismas que las claves de censo2 }
  asegura: { k es clave de res si y sólo si existe alguna clave p en censo1 tal que al obtener su valor tanto en censo1 como en censo2, este es igual a k }
  asegura: { El valor de cada clave de res representa la cantidad de personas que en ambos censos vivía en esa localidad, es decir, que mantuvieron su residencia en la misma localidad entre ambos censos }
}
```

**Solución entregada (Puntaje: 2 / 2):**
```python
def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    diccionario_municipios: dict[str, int] = {}
    for valor in censo1.values():
        if valor not in diccionario_municipios.keys():
            diccionario_municipios[valor] = 0
    for clave in censo1.keys():
        municipio_anterior: str = censo1[clave]
        municipio_actual: str = censo2[clave]
        if municipio_anterior == municipio_actual:
            diccionario_municipios[municipio_actual] += 1
    diccionario_filtrado: dict[str, int] = {}
    for clave, valor in diccionario_municipios.items():
        if valor != 0:
            diccionario_filtrado[clave] = valor
    return diccionario_filtrado
```

---

### Ejercicio 5 [0,5 puntos] (Multiple Choice)
Dada la siguiente especificación y una posible implementación de la misma, conteste marcando la opción correcta:
```python
def sumar_elementos(s: list[int]) -> int:
    res: int = 0
    for i in range(1, len(s)):
        res += s[i]
    return res
```
1. El código es correcto, calcula lo pedido en la especificación para cualquier input.
2. El código tiene un bug, y si hacemos un test suite que cubra todas las líneas lo detectaremos. *(Respuesta elegida por el alumno - Incorrecta)*
3. **El código tiene un bug, pero es posible hacer un test suite que cubra todas las líneas y no detectar dicho bug.** *(Respuesta correcta: si `s[0] == 0`, por ejemplo `s = [0, 5]`, ejecuta todas las líneas y da el resultado esperado sin detectar que ignora el índice 0).*

---

### Ejercicio 6 [0,5 puntos] (Multiple Choice)
Supongamos que un programa tiene un ciclo que itera sobre todos los elementos de una lista de tamaño $n$. Si el programa realiza una operación constante dentro de ese ciclo (por ejemplo, incrementa en 1 cada valor de la lista), ¿cómo afecta el tamaño de la lista al número de operaciones?
1. **Si la lista tiene más elementos, el número de operaciones aumentará.** *(Respuesta elegida y correcta - Puntaje: 0.5 / 0.5)*
2. El número de operaciones no cambia con el tamaño de la lista.
3. El número de operaciones depende del contenido de la lista, no del tamaño.