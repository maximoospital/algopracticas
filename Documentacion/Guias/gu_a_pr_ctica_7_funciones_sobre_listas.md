# Introducción a la Programación
## Guía Práctica 7: Funciones sobre listas (tipos complejos)
**Departamento de Computación**  
**Facultad de Ciencias Exactas y Naturales**  
**Universidad de Buenos Aires**

---

Recordar usar las anotaciones de tipado en todas las variables. Por ejemplo: `def funcion(numero: int) -> bool:`.

Las anotaciones de tipado de las colecciones, listas, diccionarios o tuplas, depende de la versión de Python que usamos. Por ejemplo:
* En **Python 3.8** son en mayúscula (ej: `List`, `Dict`, `Tuple`) y hay que importar el tipo: `from typing import List, Dict, Tuple`.
* En **Python 3.9** son en minúscula (ej: `list`, `dict`, `tuple`) y no hace falta importar nada. Por ejemplo: `list[int]`, `list[tuple[int, str]]`, `list[list[int]]`.

Sugerimos revisar esta página que resume las formas de uso: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

En los ejercicios se pueden usar funciones matemáticas como por ejemplo: `sqrt`, `round`, `floor`, `ceil`, `%`. Ver especificaciones de dichas funciones en la documentación de Python: https://docs.python.org/es/3.10/library/math.html y https://docs.python.org/es/3/library/functions.html

Para conocer cómo se usan las funciones sobre secuencias, revisar la especificación oficial: https://docs.python.org/es/3/library/stdtypes.html?highlight=list#typesseq

---

## 1. Recorrido y búsqueda en secuencias

**Ejercicio 1.** Codificar en Python las siguientes funciones sobre secuencias:

*Nota: Cada problema puede tener más de una implementación. Probar utilizando distintas formas de recorrido sobre secuencias, y distintas funciones de Python. No te conformes con una solución, recordar que siempre conviene consultar con tus docentes.*

1. **problema** `pertenece` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle, \text{in } e: \mathbb{Z}$) : $\text{Bool}$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ (\text{res} = \text{true}) \leftrightarrow (\text{existe un } i \in \mathbb{Z} \text{ tal que } 0 \le i < |s| \land s[i] = e) \}$
   $\}$
   *Implementar al menos de 3 formas distintas éste problema.*

2. **problema** `divide_a_todos` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle, \text{in } e: \mathbb{Z}$) : $\text{Bool}$ $\{$
   * **requiere:** $\{ e \neq 0 \}$
   * **asegura:** $\{ (\text{res} = \text{true}) \leftrightarrow (\text{para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |s| \rightarrow s[i] \bmod e = 0) \}$
   $\}$

3. **problema** `suma_total` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ \text{res es la suma de todos los elementos de } s \}$
   $\}$
   *Nota: no utilizar la función `sum()` nativa.*

4. **problema** `maximo` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
   * **requiere:** $\{ |s| > 0 \}$
   * **asegura:** $\{ \text{res} = \text{al mayor de todos los números que aparece en } s \}$
   $\}$
   *Nota: no utilizar la función `max()` nativa.*

5. **problema** `minimo` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
   * **requiere:** $\{ |s| > 0 \}$
   * **asegura:** $\{ \text{res} = \text{al menor de todos los números que aparece en } s \}$
   $\}$
   *Nota: no utilizar la función `min()` nativa.*

6. **problema** `ordenados` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\text{Bool}$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ \text{res} = \text{true} \leftrightarrow (\text{para todo } i \in \mathbb{Z} \text{ si } 0 \le i < (|s| - 1) \rightarrow s[i] < s[i + 1]) \}$
   $\}$

7. **problema** `pos_maximo` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ (\text{Si } |s| = 0, \text{ entonces } \text{res} = -1; \text{ si no, } \text{res} = \text{al índice de la posición donde aparece el mayor elemento de } s \text{ (si hay varios es la primera aparición)}) \}$
   $\}$

8. **problema** `pos_minimo` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ (\text{Si } |s| = 0, \text{ entonces } \text{res} = -1; \text{ si no, } \text{res} = \text{al índice de la posición donde aparece el menor elemento de } s \text{ (si hay varios es la última aparición)}) \}$
   $\}$

9. Dada una lista de palabras ($\text{seq}\langle\text{seq}\langle\text{Char}\rangle\rangle$), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo: `["termo", "gato", "tener", "jirafas"]`, devuelve falso.
   **problema** `long_mayorASiete` ($\text{in } s: \text{seq}\langle\text{seq}\langle\text{Char}\rangle\rangle$) : $\text{Bool}$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ (\text{res} = \text{true}) \leftrightarrow (\text{existe } i \in \mathbb{Z} \text{ tal que } (0 \le i < (|s| - 1)) \text{ y } (|s[i]| > 7)) \}$
   $\}$

10. Dado un texto en formato string, devolver verdadero si es palíndromo (se lee igual en ambos sentidos), falso en caso contrario. Las cadenas de texto vacías o con 1 sólo elemento son palíndromo.
    **problema** `es_palindroma` ($\text{in } s: \text{seq}\langle\text{Char}\rangle$) : $\text{Bool}$ $\{$
    * **requiere:** $\{ \text{True} \}$
    * **asegura:** $\{ (\text{res} = \text{true}) \leftrightarrow (s \text{ es igual a su reverso}) \}$
    $\}$

11. Recorrer una $\text{seq}\langle\mathbb{Z}\rangle$ y devolver verdadero si hay 3 números iguales consecutivos, en cualquier posición y `False` en caso contrario.
    **problema** `iguales_consecutivos` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\text{Bool}$ $\{$
    * **requiere:** $\{ \text{True} \}$
    * **asegura:** $\{ (\text{res} = \text{true}) \leftrightarrow (\text{existe } i, j, k \in \mathbb{Z} \text{ tal que } (0 \le i, j, k < (|s| - 1)) \text{ y } (i + 2 = j + 1 = k) \text{ y } (s[i] = s[j] = s[k])) \}$
    $\}$

12. Recorrer una palabra en formato string y devolver `True` si ésta tiene al menos 3 vocales distintas y `False` en caso contrario.
    **problema** `vocales_distintas` ($\text{in } s: \text{seq}\langle\text{Char}\rangle$) : $\text{Bool}$ $\{$
    * **requiere:** $\{ \text{True} \}$
    * **asegura:** $\{ (\text{res} = \text{true}) \leftrightarrow (\text{existe } i, j, k \in \mathbb{Z} \text{ tal que } (0 \le i, j, k < (|s| - 1)) \text{ y } (s[i] \neq s[j] \neq s[k]) \text{ y } (s[i], s[j], s[k] \in \{\text{'a'}, \text{'e'}, \text{'i'}, \text{'o'}, \text{'u'}\})) \}$
    $\}$

13. Recorrer una $\text{seq}\langle\mathbb{Z}\rangle$ y devolver la posición donde inicia la secuencia de números ordenada más larga. Si hay dos subsecuencias de igual longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vacía.
    **problema** `pos_secuencia_ordenada_mas_larga` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
    * **requiere:** $\{ |s| > 0 \}$
    * **asegura:** $\{ (\text{res} = i) \leftrightarrow (\text{existe } i, j \in \mathbb{Z} \text{ tal que } (0 \le i, j < (|s| - 1)) \text{ y } i \le j \text{ y } (\text{para todo } k \text{ tal que } i \le k < j \rightarrow s[k] \le s[k + 1]) \text{ y } j - i + 1 \text{ es máximo e } i \text{ es el mínimo valor que lo cumple}) \}$
    $\}$

14. Cantidad de dígitos impares.
    **problema** `cantidad_digitos_impares` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
    * **requiere:** $\{ \text{Todos los elementos de números son mayores o iguales a } 0 \}$
    * **asegura:** $\{ \text{res es la cantidad total de dígitos impares que aparecen en cada uno de los elementos de números} \}$
    $\}$
    *Por ejemplo, si la lista de números es `[57, 2383, 812, 246]`, entonces el resultado esperado sería 5 (los dígitos impares son 5, 7, 3, 3 y 1).*

---

## 2. Recorrido: filtrando, modificando y procesando secuencias

**Ejercicio 2.** Implementar las siguientes funciones sobre secuencias pasadas por parámetro:

1. **problema** `CerosEnPosicionesPares` ($\text{inout } s: \text{seq}\langle\mathbb{Z}\rangle$) $\{$
   * **requiere:** $\{ \text{True} \}$
   * **modifica:** $\{ s \}$
   * **asegura:** $\{ (|s| = |s@\text{pre}|) \text{ y } (\text{para todo } i \text{ entero, con } 0 \le i < |s|, \text{ si } i \text{ es impar entonces } s[i] = s@\text{pre}[i] \text{ y, si } i \text{ es par, entonces } s[i] = 0) \}$
   $\}$

2. **problema** `CerosEnPosicionesPares2` ($\text{in } s: \text{seq}\langle\mathbb{Z}\rangle$) : $\text{seq}\langle\mathbb{Z}\rangle$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ (|s| = |\text{res}|) \text{ y } (\text{para todo } i \text{ entero, con } 0 \le i < |\text{res}|, \text{ si } i \text{ es impar entonces } \text{res}[i] = s[i] \text{ y, si } i \text{ es par, entonces } \text{res}[i] = 0) \}$
   $\}$

3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios, sino que borra la vocal y concatena a continuación.
   **problema** `sin_vocales` ($\text{in } s: \text{seq}\langle\text{Char}\rangle$) : $\text{seq}\langle\text{Char}\rangle$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ \text{res es la subsecuencia de } s \text{ que se obtiene al quitarle las vocales a } s \}$
   $\}$
   *Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena original, conservando el orden de los elementos restantes.*

4. **problema** `reemplaza_vocales` ($\text{in } s: \text{seq}\langle\text{Char}\rangle$) : $\text{seq}\langle\text{Char}\rangle$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ |\text{res}| = |s| \}$
   * **asegura:** $\{ \text{Para todo } i \in \mathbb{Z}, \text{ si } 0 \le i < |\text{res}| \rightarrow (\text{pertenece}(\langle\text{'a'}, \text{'e'}, \text{'i'}, \text{'o'}, \text{'u'}\rangle, s[i]) \land \text{res}[i] = \text{'\_'}) \lor (\neg \text{pertenece}(\langle\text{'a'}, \text{'e'}, \text{'i'}, \text{'o'}, \text{'u'}\rangle, s[i]) \land \text{res}[i] = s[i]) \}$
   $\}$

5. **problema** `da_vuelta_str` ($\text{in } s: \text{seq}\langle\text{Char}\rangle$) : $\text{seq}\langle\text{Char}\rangle$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ |\text{res}| = |s| \}$
   * **asegura:** $\{ \text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |\text{res}| \rightarrow \text{res}[i] = s[|s| - i - 1] \}$
   $\}$

6. **problema** `eliminar_repetidos` ($\text{in } s: \text{seq}\langle\text{Char}\rangle$) : $\text{seq}\langle\text{Char}\rangle$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ (|\text{res}| \le |s|) \land (\text{para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |s| \rightarrow \text{pertenece}(s[i], \text{res})) \land (\text{para todo } i, j \in \mathbb{Z} \text{ si } (0 \le i, j < |\text{res}| \land i \neq j) \rightarrow \text{res}[i] \neq \text{res}[j]) \}$
   $\}$

---

**Ejercicio 3.** Implementar una función para conocer el estado de aprobación de una materia a partir de las notas obtenidas por un/a alumno/a cumpliendo con la siguiente especificación:

**problema** `resultadoMateria` ($\text{in notas}: \text{seq}\langle\mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
* **requiere:** $\{ |\text{notas}| > 0 \}$
* **requiere:** $\{ \text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |\text{notas}| \rightarrow 0 \le \text{notas}[i] \le 10 \}$
* **asegura:** $\{ \text{res} = 1 \leftrightarrow \text{todos los elementos de notas son mayores o iguales a } 4 \text{ y el promedio es mayor o igual a } 7 \}$
* **asegura:** $\{ \text{res} = 2 \leftrightarrow \text{todos los elementos de notas son mayores o iguales a } 4 \text{ y el promedio está entre } 4 \text{ (inclusive) y } 7 \}$
* **asegura:** $\{ \text{res} = 3 \leftrightarrow \text{alguno de los elementos de notas es menor a } 4 \text{ o el promedio es menor a } 4 \}$
$\}$

---

**Ejercicio 4.** Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento `"I"` para ingreso de dinero y `"R"` para retiro de dinero, y además el monto de cada operación. Por ejemplo, si la lista de tuplas es `[("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]` entonces el saldo actual es 1280.

**problema** `saldoActual` ($\text{in movimientos}: \text{seq}\langle\text{Char} \times \mathbb{Z}\rangle$) : $\mathbb{Z}$ $\{$
* **requiere:** $\{ \text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |\text{movimientos}| \rightarrow \text{movimientos}[i]_0 \in \{\text{"I"}, \text{"R"}\} \text{ y } \text{movimientos}[i]_1 > 0 \}$
* **asegura:** $\{ \text{res} = \sum_{i \in \text{ingresos}} \text{movimientos}[i]_1 - \sum_{i \in \text{retiros}} \text{movimientos}[i]_1 \}$
$\}$

---

## 3. Matrices

**Ejercicio 5.** Analizando parámetros `in` y `out` vs. resultado:

1. **problema** `pertenece_a_cada_uno_version_1` ($\text{in } s: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle, \text{in } e: \mathbb{Z}, \text{out res}: \text{seq}\langle\text{Bool}\rangle$) $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ |\text{res}| \ge |s| \}$
   * **asegura:** $\{ \text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |s| \rightarrow (\text{res}[i] = \text{true} \leftrightarrow \text{pertenece}(s[i], e)) \}$
   $\}$
   *Nota: Reutilizar la función `pertenece()` implementada previamente para listas.*

2. **problema** `pertenece_a_cada_uno_version_2` ($\text{in } s: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle, \text{in } e: \mathbb{Z}, \text{out res}: \text{seq}\langle\text{Bool}\rangle$) $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ |\text{res}| = |s| \}$
   * **asegura:** $\{ \text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |s| \rightarrow (\text{res}[i] = \text{true} \leftrightarrow \text{pertenece}(s[i], e)) \}$
   $\}$

3. **problema** `pertenece_a_cada_uno_version_3` ($\text{in } s: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle, \text{in } e: \mathbb{Z}$) : $\text{seq}\langle\text{Bool}\rangle$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ |\text{res}| = |s| \}$
   * **asegura:** $\{ \text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |s| \rightarrow (\text{res}[i] = \text{true} \leftrightarrow \text{pertenece}(s[i], e)) \}$
   $\}$

4. **Pensar:** ¿Cómo cambia este problema respecto de la versión 1? Pensar en relación de fuerza entre: implementación en Python y las especificaciones. ¿Se puede usar la implementación del ejercicio 2 para la especificación del 1? ¿Se puede usar la implementación del ejercicio 1 para la especificación del 2? Justificar su respuesta.

---

**Ejercicio 6.** Implementar las siguientes funciones sobre matrices (secuencias de secuencias):

1. **problema** `es_matriz` ($\text{in } s: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle$) : $\text{Bool}$ $\{$
   * **requiere:** $\{ \text{True} \}$
   * **asegura:** $\{ \text{res} = \text{true} \leftrightarrow (|s| > 0) \land (|s[0]| > 0) \land (\text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |s| \rightarrow |s[i]| = |s[0]|) \}$
   $\}$

2. **problema** `filas_ordenadas` ($\text{in } m: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle, \text{out res}: \text{seq}\langle\text{Bool}\rangle$) $\{$
   * **requiere:** $\{ \text{esMatriz}(m) \}$
   * **asegura:** $\{ \text{Para todo } i \in \mathbb{Z} \text{ si } 0 \le i < |\text{res}| \rightarrow (\text{res}[i] = \text{true} \leftrightarrow \text{ordenados}(m[i])) \}$
   $\}$
   *Nota: Reutilizar la función `ordenados()` implementada previamente para listas.*

3. **problema** `columna` ($\text{in } m: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle, \text{in } c: \mathbb{Z}$) : $\text{seq}\langle\mathbb{Z}\rangle$ $\{$
   * **requiere:** $\{ \text{esMatriz}(m) \}$
   * **requiere:** $\{ c < |m[0]| \}$
   * **requiere:** $\{ c \ge 0 \}$
   * **asegura:** $\{ \text{Devuelve una secuencia con exactamente los mismos elementos de la columna } c \text{ de la matriz } m, \text{ en el mismo orden que aparecen} \}$
   $\}$

4. **problema** `columnas_ordenadas` ($\text{in } m: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle$) : $\text{seq}\langle\text{Bool}\rangle$ $\{$
   * **requiere:** $\{ \text{esMatriz}(m) \}$
   * **asegura:** $\{ \text{Para todo índice de columna } c: 0 \le c < |m[0]| \rightarrow (\text{res}[c] = \text{true} \leftrightarrow \text{ordenados}(\text{columna}(m, c))) \}$
   * **asegura:** $\{ |\text{res}| = |m[0]| \}$
   $\}$
   *Nota: Reutilizar la función `ordenados()` implementada previamente para listas.*

5. **problema** `transponer` ($\text{in } m: \text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle$) : $\text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle$ $\{$
   * **requiere:** $\{ \text{esMatriz}(m) \}$
   * **asegura:** $\{ \text{Devuelve } m^t \text{ (o sea la matriz transpuesta)} \}$
   $\}$
   *Nota: Usar `columna()` para ir obteniendo todas las columnas de la matriz.*

6. **Ta-Te-Ti Tradicional:**
   **problema** `quien_gana_tateti` ($\text{in } m: \text{seq}\langle\text{seq}\langle\text{Char}\rangle\rangle$) : $\mathbb{Z}$ $\{$
   * **requiere:** $\{ \text{esMatriz}(m) \}$
   * **requiere:** $\{ |m| = 3 \}$
   * **requiere:** $\{ |m[0]| = 3 \}$
   * **requiere:** $\{ \text{En la matriz si hay 3 X alineadas verticalmente} \rightarrow \text{no hay 3 O alineadas verticalmente} \}$
   * **requiere:** $\{ \text{En la matriz si hay 3 O alineadas verticalmente} \rightarrow \text{no hay 3 X alineadas verticalmente} \}$
   * **requiere:** $\{ \text{En la matriz si hay 3 X alineadas horizontalmente} \rightarrow \text{no hay 3 O alineadas horizontalmente} \}$
   * **requiere:** $\{ \text{En la matriz si hay 3 O alineadas horizontalmente} \rightarrow \text{no hay 3 X alineadas horizontalmente} \}$
   * **requiere:** $\{ \text{Para todo } i, j \in \{0, 1, 2\} \rightarrow m[i][j] = \text{'X'} \lor m[i][j] = \text{'O'} \lor m[i][j] = \text{' '} \}$
   * **asegura:** $\{ \text{Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve } 0 \}$
   * **asegura:** $\{ \text{Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve } 1 \}$
   * **asegura:** $\{ \text{Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve } 2 \}$
   $\}$

7. **Opcional:** Implementar una función que tome un entero $d$ y otro $p$ y eleve una matriz cuadrada de tamaño $d$ con valores generados al azar a la potencia $p$. Es decir, multiplique a la matriz generada al azar por sí misma $p$ veces. Realizar experimentos con diferentes valores de $d$. ¿Qué pasa con valores muy grandes?
   **problema** `exponenciacion_matriz` ($\text{in } d: \mathbb{Z}, \text{in } p: \mathbb{Z}$) : $\text{seq}\langle\text{seq}\langle\mathbb{Z}\rangle\rangle$ $\{$
   * **requiere:** $\{ d, p \in \mathbb{Z} \text{ y } d, p > 0 \}$
   * **asegura:** $\{ \text{esMatriz}(m) \text{ y } |\text{columna}(m, 0)| = d \text{ y } |\text{columna}(\text{transponer}(m), 0)| = d \text{ y } \text{res} = \prod_{i=1}^p m \}$
   $\}$
   * **Nota 1:** recordá que en la multiplicación de una matriz cuadrada de dimensión $d$ por sí misma cada posición se calcula como $\text{res}[i][j] = \sum_{k=0}^{d-1} (m[i][k] \times m[k][j])$
   * **Nota 2:** para generar una matriz cuadrada de dimensión $d$ con valores aleatorios hay muchas opciones de implementación, analizar las siguientes usando la biblioteca `numpy`:

   **Opción 1:**
   ```python
   import numpy as np
   m = np.random.random((d, d))
   ```
   *(Documentación: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html)*

   **Opción 2:**
   ```python
   import numpy as np
   m = np.random.randint(i, f, (d, d))
   ```
   *(Documentación: https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html)*

   Para poder importar la biblioteca `numpy` es necesario instalarla primero. Y para ello es necesario tener instalado un gestor de paquetes, por ejemplo `pip3` (Ubuntu: `sudo apt install pip3`, Windows: se instala junto con Python). Una vez instalado `pip3` se ejecuta `pip3 install numpy`.

---

## 4. Programas interactivos usando secuencias

**Ejercicio 7.** Vamos a elaborar programas interactivos (usando la función `input()`, ver: https://docs.python.org/es/3/library/functions.html?highlight=input#input) que nos permita solicitar al usuario información cuando usamos las funciones.

1. Implementar una función para construir una lista con los nombres de mis estudiantes. La función solicitará al usuario los nombres hasta que ingrese la palabra `"listo"`, o vacío (el usuario aprieta ENTER sin escribir nada). Devuelve la lista con todos los nombres ingresados.

2. Implementar una función que devuelve una lista con el historial de un monedero electrónico (por ejemplo la SUBE). El usuario debe seleccionar en cada paso si quiere:
   * `"C"` = Cargar créditos,
   * `"D"` = Descontar créditos,
   * `"X"` = Finalizar la simulación (terminar el programa).
   
   En los casos de cargar y descontar créditos, el programa debe además solicitar el monto para la operación. Vamos a asumir que el monedero comienza en cero. Para guardar la información grabaremos en el historial tuplas que representen los casos de cargar `("C", monto a cargar)` y descontar crédito `("D", monto a descontar)`.

3. Vamos a escribir un programa para simular el juego conocido como **7 y medio**. El mismo deberá generar un número aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deberá luego preguntarle al usuario si desea seguir sacando otra "carta" o plantarse. En este último caso el programa debe terminar. Los números aleatorios obtenidos deberán sumarse según el número obtenido salvo por las "figuras" (10, 11 y 12) que sumarán medio punto cada una. El programa debe ir acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la función devuelve el historial de "cartas" que hizo que el usuario gane o pierda. Para generar números pseudo-aleatorios entre 1 y 12 utilizaremos la función `random.randint(1, 12)`. Al mismo tiempo, la función `random.choice()` puede ser de gran ayuda a la hora de repartir cartas.

4. Analizar la fortaleza de una contraseña. Solicitar al usuario que ingrese un texto que será su contraseña. Armar una función que tenga de parámetro de entrada un string con la contraseña a analizar, y la salida otro string con tres posibles valores: `VERDE`, `AMARILLA` y `ROJA`. *Nota: en Python la "ñ/Ñ" es considerado un carácter especial y no se comporta como cualquier otra letra. String es $\text{seq}\langle\text{Char}\rangle$. Consejo: para ver si una letra es mayúscula se puede ver si está ordenada entre A y Z.*
   * La contraseña será `VERDE` si:
     a) la longitud es mayor a 8 caracteres,
     b) tiene al menos 1 letra minúscula,
     c) tiene al menos 1 letra mayúscula,
     d) tiene al menos 1 dígito numérico (`0..9`).
   * La contraseña será `ROJA` si:
     a) la longitud es menor a 5 caracteres.
   * En caso contrario será `AMARILLA`.