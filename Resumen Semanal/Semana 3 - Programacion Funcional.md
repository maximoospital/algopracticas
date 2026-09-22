---
dg-publish: true
tags:
  - algo1
  - resumen
---
# Programación funcional

> **Idea guía:** programar es escribir ecuaciones; ejecutar es **reducir** una expresión hasta su resultado.

Un programa en un lenguaje funcional es una colección de funciones que transforman entradas en resultados. La ejecucion de un programa aqui correpsonde a la evaluacion de una expresion, solicitada habitualmente desde la consola del entorno de programacion, esta se evaluara utilizando las ecuaciones definidas en el programa hasta llegar a un resultado. 

Las ecuaciones orientadas, en conjunto con la reduccion de expresiones descibren aqui algoritmos.

En Haskell, se expresaran como **ecuaciones orientadas**: $doble\  x = x + x$, las cuales se leen de izquierda a derecha y junto con el mecanismo de reduccion describen algoritmos.
## 1. Ecuaciones, reducción y significado
Para determinar el valor de la aplicacion de una funcion se reempalza cada expresion por otra, segun las ecuaciones.
- Una ecuación se usa solo de **izquierda a derecha**: el lado izquierdo describe qué reconocer; el derecho, por qué reemplazarlo.
- Un **redex** (*reducible expression*) es una subexpresión que coincide con un lado izquierdo.
- **Reducir** = elegir un redex, ligar sus parámetros a los argumentos y reemplazarlo por el lado derecho.
- El cómputo termina al llegar a una **forma normal**: expresión que ya no puede reducirse.

```haskell
doble (1 + 1)
→ (1 + 1) + (1 + 1)
→ 2 + 2
→ 4
```

**Ojo:** ecuaciones bien escritas no garantizan terminación. Elegir reemplazos arbitrarios puede crear un ciclo.

### Transparencia referencial
Una expresión depende solo del valor de sus subexpresiones: vale lo mismo en cualquier lugar del programa, sin historia ni estado oculto. **Como consecuencia:**, podemos reemplazar iguales por iguales y razonar con ecuaciones para demostrar que se cumple la especificacion.

### Expresiones bien formadas

| Clase                  | Ejemplos                                      |
| ---------------------- | --------------------------------------------- |
| Atómica / forma normal | `2`, `False`, `(3, True)`                     |
| Compuesta              | `1 + 1`, `1 == 2`, $(4 - 1, \ True \|False)$` |

Una cadena puede fallar por sintaxis (`(True`) o por tipos (`2 + False`). Haskell es fuertemente tipado e infiere tipos; un valor no puede usarse como si fuera de otro tipo.

## 2. Cómo evalúa Haskell

Haskell usa evaluación **normal o lazy**: reduce el redex más externo y más a la izquierda que permita decidir qué ecuación aplicar. Evalúa los argumentos **solo si hacen falta**.

```haskell
suma (3 + 4) (suc (2 * 3))
→ (3 + 4) + suc (2 * 3)
→ 7 + ((2 * 3) + 1)
→ 14
```

En evaluación **eager** (por ejemplo, C o Java), primero se evalúan los argumentos. La evaluación lazy puede evitar trabajo inútil y también evitar evaluar una rama indefinida.

### Indefinición: `⊥`

Una expresión es **indefinida** si no encuentra resultado: no termina o produce un error de ejecución.

- **Total:** está definida para toda entrada de su dominio. `suc x = x + 1`.
- **Parcial:** hay alguna entrada que produce `⊥`. Por ejemplo, `division x y = div x y` cuando `y = 0`.

> **Regla de oro:** que una rama sea indefinida no importa si la evaluación lazy nunca necesita esa rama.

## 3. Definir funciones por casos

Las **guardas** se prueban de arriba hacia abajo; se toma la primera verdadera.

```haskell
signo n | n > 0     = 1
        | n == 0    = 0
        | otherwise = -1
```

> **Regla de oro:** si las condiciones se solapan, **el orden cambia la función**. Si ninguna guarda vale y no hay `otherwise`, la función queda parcial.

El **pattern matching** elige una ecuación por la forma del argumento; es ideal para distinguir constructores o valores concretos.

```haskell
f 0 = 1
f _ = 0       -- _ = “no me interesa este valor”
```

Los patrones también pueden combinarse con guardas:

```haskell
signo 0 = 0
signo n | n > 0     = 1
        | otherwise = -1
```

## 4. Tipos y funciones

Un **tipo** reúne valores y las operaciones que se les pueden aplicar. La **signatura** declara el dominio y codominio; Haskell puede inferirla, pero en la materia se escribe.

```haskell
esMayorA9 :: Int -> Bool
esMayorA9 n = n > 9
```

Las funciones son valores. Aplicar es escribir función y argumento separados por espacios: si `f :: T1 -> T2` y `e :: T1`, entonces `f e :: T2`.

### Polimorfismo, variables y clases de tipos

Una función es **polimórfica** cuando funciona para varios tipos sin redefinirse: su comportamiento no depende del tipo concreto.

```haskell
identidad :: a -> a
identidad x = x

primero :: a -> b -> a
primero x _ = x
```

- Las letras minúsculas (`a`, `b`) son **variables de tipo**.
- Repetir una variable exige el mismo tipo: `mismoTipo :: a -> a -> Bool`; por eso `mismoTipo 1 True` no tipa.
- Una **clase de tipos** restringe qué operaciones puede usar una variable:

```haskell
triple    :: Num a => a -> a
maximo    :: Ord a => a -> a -> a
distintos :: Eq a  => a -> a -> Bool
```

`Num` habilita operaciones numéricas; `Ord`, comparaciones de orden; `Eq`, igualdad. Un tipo puede pertenecer a varias clases.

## 5. Tuplas y parámetros

Una tupla es un producto de tamaño fijo; sus componentes pueden tener tipos distintos.

```haskell
(1, "hola") :: (Int, String)
```

Para pares existen `fst` y `snd`, pero el pattern matching suele ser más claro:

```haskell
sumaVectores :: (Float, Float) -> (Float, Float) -> (Float, Float)
sumaVectores (vx, vy) (wx, wy) = (vx + wx, vy + wy)
```

**Parámetros vs. tupla:** `f :: Float -> Float -> Float` recibe dos argumentos; `g :: (Float, Float) -> Float` recibe uno, que es un par. No son el mismo tipo ni se aplican igual.

## 6. Currificación y aplicación parcial

Toda función de varios argumentos en Haskell está currificada, lo cual significa que 

```haskell
f :: T1 -> T2 -> T3
-- equivale a
f :: T1 -> (T2 -> T3)
```

Da un argumento y obtenés una función que espera el resto:

```haskell
suma :: Int -> Int -> Int
suma x y = x + y

sumaCinco :: Int -> Int
sumaCinco = suma 5
```

> **Memoria:** una tupla empaqueta argumentos; la currificación los entrega de a uno.

## 7. Notación y alias

| Forma | Ejemplo |
| --- | --- |
| Prefija: función antes de argumentos | `div 10 2`, `(+) 2 3` |
| Infija: función entre argumentos | ``10 `div` 2``, `2 + 3` |

- Un operador simbólico se usa como función prefija entre paréntesis: `(+) 2 3`.
- Una función binaria alfanumérica se usa infija con *backticks*: ``10 `div` 2``.

Un alias mejora el nombre de un tipo, pero **no crea un tipo nuevo**:

```haskell
type Complejo = (Float, Float)
```