---
dg-publish: true
tags:
  - algo1
  - resumen
---
# Semana 2 — Lógica proposicional y especificaciones
## Lógica proposicional
Una **proposición** es una oración que vale **V** o **F**. La lógica permite calcular el valor de una fórmula desde sus proposiciones.
- **Simbolos**: $True$, $False$, $\neg$, $\vee$, $\wedge$, $\rightarrow$, $\iff$, $($, $)$
- **Variables proposicionales (infinitas)**: $p$, $q$, $r$, $\dots$
- **Formulas**: Las oraciones en si. Estas pueden ser simplemente valores o variables proposicionales, pero siempre respetando una sintaxis clara que contenga cada expresion separada, por lo cual `p ∨ q` no es una formula, pero `(p ∨ q)` o `((p ∨ q) → r)` si. 
- **Operadores y sus valores**:

| **Simbolo**           | **Ejemplo** | Se lee            | **Que significa**                                                                |
| --------------------- | ----------- | ----------------- | -------------------------------------------------------------------------------- |
| ¬ (Negacion)          | `¬p`        | no p              | Invierte lo que se afirma.                                                       |
| ∧ (Conjuncion)        | `p ∧ q`     | p y q             | Requiere que ambas partes se cumplan a la vez.                                   |
| ∨ (Disyuncion)        | `p ∨ q`     | p o q (inclusiva) | Se cumple una, la otra, o ambas.                                                 |
| → (Implicacion)       | `p → q`     | si p, entonces q  | Es una promesa: solo se rompe si se da la causa (p) pero no la consecuencia (q). |
| ↔ (Doble implicacion) | `p ↔ q`     | p si y solo si q  | O se dan las dos juntas, o no se da ninguna.                                     |
Segun los resultados que den al recibir distintos valores, podemos elaborar tablas de verdad o clasificar las proposiciones en:
- **Tautología:** siempre V.
- **Contradicción:** siempre F.
- **Contingencia:** a veces V y a veces F.
- **Equivalencia:** `A ≡ B` si `(A ↔ B)` es una tautología. Ejemplos de equivalencias:![[Pasted image 20260917005748.png]]
### Relacion de fuerza
Una afirmación es **más fuerte** cuantas más condiciones exige para cumplirse (te da más información y descarta más escenarios) y es **más débil** cuanto más permisiva es (abarca más posibilidades con menos certezas). En base a eso, a la hora de comparar, decimos que `A` es **más fuerte** que `B` cuando `(A → B)` es tautología: todo caso que cumple `A` cumple `B`.
- `(p ∧ q)` es más fuerte que `p`.
- `False` es la fórmula más fuerte; `True`, la más débil.

## 2. Indefinido y evaluación secuencial

Una expresión puede no estar definida: `x / y = 5` cuando `y = 0`. Agregamos entonces `⊥` (indefinido), además de V y F.

Los operadores secuenciales evalúan de izquierda a derecha y **se detienen cuando ya conocen el resultado**:

| **Simbolo** | **Ejemplo** | Se lee                | **Que significa**                                                                                                                                    |
| ----------- | ----------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ∧L          | `p ∧L q`    | p y luego q           | Requiere que se cumpla p primero; si falla, ni mira q. Una vez cumplido p, requiere que ambas partes se cumplan a la vez.                            |
| ∨L          | `p ∨L q`    | p o luego q           | Se cumple p, o recién ahí se fija si se cumple q. Una vez cumplido p, requerira que se cumpla una, la otra, o ambas.                                 |
| →L          | `p →L q`    | si p entonces luego q | Es una promesa con orden: solo revisa q si p llegó a cumplirse. Una vez p cumplido, solo se rompe si se da la causa (p) pero no la consecuencia (q). |
Ejemplo de **guarda** segura: `(y ≠ 0 ∧L x / y = 5)`. Con `y = 0`, ya da F y nunca divide por cero.

> En la materia esta semántica trivaluada se asume por defecto. Para clasificar tautologías, contradicciones y contingencias se consideran las valuaciones definidas (lógica bivaluada).

## 3. Especificar: decir qué, no cómo
Una especificación describe el problema sin elegir algoritmo. 
Por ahora, los problemas se modelan como funciones:
```text
problema nombre(parámetros) : tipo de dato del reslutado {
  requiere etiqueta: { condición sobre las entradas }
  asegura  etiqueta: { condición sobre las salidas }
}
```
- En los asegura podremos referenciar el valor devuelto con el nombre de res
- Podemos tener mas de un asegura y mas de un requiere, pero siempre debemos evitar contradicciones.
### El contrato: entrada válida → resultado correcto

Si el usuario entrega una entrada que cumple `requiere`, el programador debe garantizar que el programa **termina** y que su resultado cumple `asegura`.

| Parte | Responsabilidad |
|---|---|
| `requiere` (precondición) | El usuario aporta una entrada válida. |
| `asegura` (postcondición) | El programador entrega un resultado correcto para esas entradas. |

Si no se cumple la precondición, el contrato no promete nada. Si se cumple y el programa no termina o viola la postcondición, es incorrecto.

```text
problema raizCuadrada(x : R) : R {
  requiere: { x ≥ 0 }
  asegura:  { res × res = x ∧ res ≥ 0 }
}
```

## 4. Tipos y secuencias: vocabulario para especificar

Un **tipo de datos** es un conjunto de valores con una serie de operaciones que involucran a esos valores. En este lenguaje, las expresiones pueden dar `⊥` cuando no están definidas. Para referirnos a un elemento de un tipo $T$ en nustro lenguaje, lo escribimos como termino o expresion: variable de tipo $T$, constante de tipo $T$ o funcion aplicada a otros terminos, sea del tipo $T$ u otro.
- **Tipos Basicos**:
	- **Enteros** ($\mathbb{Z}$): Su conjunto base son los enteros, tienen operaciones aritmeticas (suma, resta, valor absoluto, multiplicacion, division entera, resto de division, potencia o division) y se comparan con $<$, $\leq$, $>$, $\geq$, $=$, $\neq$.
	- **Reales** ($\mathbb{R}$): Su conjunto base son los reales, tienen operaciones aritmeticas como suma, resta, producto (pero no division entera ni resto de division), division, logaritmo y funciones trigonometricas. Se comparan con $<$, $\leq$, $>$, $\geq$, $=$, $\neq$.
	- **Booleanos** ($Bool$): Su conjunto base es {$True$,$False$}, tienen conectivos logicos como $!$, $\&\&$, $||$, con semantica bi-valuada, y se comparan con $=$ o $\neq$.
	- **Caracteres** ($Char$): Sus elementos son las letras, digitos y simbolos. Tienen las funciones $ord$, que numera los caracteres, y $char$, que devuelve el caracter correspondiente al orden dado. Se comparan los ordenes, tal que $a<b \equiv ord(a)<ord(b)$.
- **Tuplas** ($Uplas$): Su conjunto base es el producto cartesiano de los tipos de sus componentes, formado por secuencias ordenadas de tamaño fijo de la forma $(x1,x2,…,xn)$ con $xi∈Ti$. Tienen operaciones de construcción (empaquetado) y de proyección o acceso por posición/índice ($πi$ o $.i$ para obtener el i-ésimo elemento). Se comparan principalmente por igualdad, y si sus tipos base lo admiten, mediante orden lexicográfico con <,≤,>,≥.
- **Secuencias**: Varios elemenos del mismo tipo $T$, posiblemente repetidos, ubicados en un orden especifico. $seq(T)$ es el tipo de las secuencias cuyos elementos son de tipo $T$, el cual es arbitrario: pueden ser secuencias de $Z$, de $Bool$, de $Dias$, de $5-uplas$, secuencias de secuencias, etc.
	- **Funciones sobre secuencias**:
		- **Longitud**: Dada una secuencia, nos dara la cantidad de elementos en ella. Se puede escribir como $length(a)$, $a.length$ o $|a|$.
		- **Indexacion**: Dada una secuencia y un $i$ entre 0 y la longitud de la secuencia inclusive (de lo contrario se indefinira), nos dara el elemento en la $i$-esima posicion. La primer posicion es 0 y la notacion es $a[i]$.
		- **Pertenece**: Dada una secuencia y un elemento, nos dara $true$ si y solo is el elemento pertenece a la secuencia. Se escribe como $pertenece(elemento, secuencia)$
		- **Igualdad**: Dadas dos secuencias, nos dara $true$ si y solo si tienen la misma cantidad de elementos y los mismos elementos en las mismas posiciones. Se escribe como $sec0 = sec1$
		- **Head**: Dada una secuencia cuya longitud es mayor a 0 (de lo contrario se indefinira), nos dara el primer elemento de la misma. Se escribe como $head(secuencia)$
		- **Tail**: Dada una secuencia cuya longitud es mayor a 0 (de lo contrario se indefinira), nos dara el ultimo elemento de la misma. Se escribe como $tail(secuencia)$
		- **Concatenacion**: Dadas dos secuencias, nos dara una secuencia con los elementos de la primera, seguidos de los de la segunda. Se escribe como $concat(sec1, sec2)$
		- **addFirst**: Dada una secuencia y un elemento, nos dara una secuencia con los elementos de la secuencia pero agregando el elemento en primer lugar.
		- **Subsecuencia**:  Dada una secuencia y dos numeros, nos dara una sublista de la secuencia con los valores entre el primer (inclusive) y segundo (exclusive) numero. Se escribe como $subseq(secuencia, valor1, valor2)$
		- **setAt**: Dada una secuencia, una posicion y un elemento, nos dara una secuencia igual a la que ingresamos, pero con el valor ingresado en la posicion dada.
### Renombre de tipos
Tambien conocido como alias, nos permite crear un nuevo nombre para un tipo de dato ya existente, no crea un tipo nuevo, simplemente actua como un sinonimo del original, para hacer la especificacion mas legible o adaptar a un contexto especifico. De notacion $Renombre\  T_1=T_2$.

## 5. Ni de más ni de menos

| Error                 | Qué ocurre                                                                                                              | Ejemplo                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Sobre-especificar** | `requiere` demasiado laxo o `asegura` demasiado restrictivo: limita soluciones válidas.                                 | Pedir `res = x + 1` cuando solo se necesita `res ≠ x`.                               |
| **Sub-especificar**   | `requiere` demasiado restrictivo o `asegura` demasiado débil: deja afuera casos válidos o acepta soluciones indeseadas. | Exigir `x > 0` para devolver un valor distinto de `x`, cuando vale para todo entero. |

**Regla de examen:** precondición = exactamente las entradas necesarias; postcondición = exactamente las propiedades necesarias.

## 6. Modularizar: partir, nombrar, reutilizar
Una especificación grande puede expresarse con problemas auxiliares. Se descompone el problema, se especifica cada parte y se las compone. Nombramos las partes auxiliares y podemos reutilizarlas despues en el problema grande en varias piezas.

Beneficios: piezas más fáciles de entender, probar y reutilizar. Se puede diseñar **top-down** (del problema grande a auxiliares) o **bottom-up** (desde auxiliares ya definidos).