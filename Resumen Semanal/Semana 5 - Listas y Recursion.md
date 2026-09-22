---
dg-publish: true
tags:
  - algo1
  - resumen
---
# Semana 5 — Listas y recursión
> **Idea guía:** una lista es **vacía** o tiene **cabeza y cola**. Para procesarla recursivamente, resolvé el caso vacío y combiná la cabeza con el resultado sobre la cola.

## 1. Polimorfismo y variables de tipo

Una función es **polimórfica** si sirve para valores de distintos tipos sin redefinirse. Se expresa con variables de tipo minúsculas (`a`, `b`, `t`), que representan tipos, no valores.

```haskell
identidad :: a -> a
identidad x = x

primero :: a -> b -> a
primero x _ = x

segundo :: a -> b -> b
segundo _ y = y
```

**Regla de oro:** la misma variable significa el mismo tipo.

```haskell
mismoTipo :: a -> a -> Bool
mismoTipo _ _ = True

-- mismoTipo 1 True  -- no tipa: ambos argumentos deben ser del mismo tipo
```

En una especificación también pueden aparecer variables de tipo:

```text
problema segundo(x : U, y : T) : T {
  asegura: { res = y }
}
```

Y se pueden restringir cuando la operación lo exige:

```text
problema suma(x : T, y : T) : T {
  requiere: { T ∈ [N, Z, R] }
  asegura:  { res = x + y }
}
```

## 2. El tipo lista

Una lista es una secuencia de elementos **del mismo tipo**; puede estar vacía y puede repetir elementos. Su tipo se escribe `[a]`.

```haskell
[1, 2, 1]                         :: [Int]
[True, False]                    :: [Bool]
[(1,2), (3,4)]                   :: [(Int, Int)]
[[1], [2,3], [], [1,1000,2,0]]   :: [[Int]]
[]                               :: [a]
```

```haskell
[1, True]  -- no tipa: una lista no mezcla tipos de elementos
```

## 3. Las tres operaciones esenciales

| Operación | Tipo | Qué hace | Condición |
| --- | --- | --- | --- |
| `head` | `[a] -> a` | devuelve el primer elemento | lista no vacía |
| `tail` | `[a] -> [a]` | devuelve la lista sin el primero | lista no vacía |
| `(:)` | `a -> [a] -> [a]` | agrega un elemento al frente | ninguna |

```haskell
head [1,2,3]  -- 1
tail [1,2,3]  -- [2,3]
1 : [2,3]     -- [1,2,3]
```

> **Ojo:** `head []` y `tail []` producen error. Preferí *pattern matching* para no olvidar el caso vacío.

`(:)` agrega **un elemento**, no concatena listas:

```haskell
[1,2] : []     -- [[1,2]]
head [1,2,3] : [4,5]  -- [1,4,5]
```

## 4. Construcción por intervalos

```haskell
[1..100]    -- 1, 2, ..., 100
[1,3..100]  -- impares desde 1 hasta 99
[100..1]    -- []: el paso por defecto es +1
[1..]       -- lista infinita: 1, 2, 3, ...

[1,0..(-100)]     -- 1, 0, -1, ..., -100
[-19,-15..17]     -- entre -20 y 20, congruentes con 1 módulo 4
```

## 5. Recursión sobre listas

La forma real de una lista solo tiene dos casos:

```haskell
[]        -- vacía
x : xs    -- cabeza x y cola xs
```

**Plantilla mental:**

```haskell
f [] = casoBase
f (x:xs) = combinar x (f xs)
```

La llamada recursiva siempre se hace sobre `xs`, una lista más corta. Así se garantiza que eventualmente se llega a `[]`.

```haskell
longitud :: [a] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

pertenece :: Int -> [Int] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x || pertenece e xs
```

### Cómo elegir el caso base

| Problema | Caso base en `[]` | Combinar en `x:xs` |
| --- | --- | --- |
| contar (`longitud`) | `0` | sumar `1` |
| sumar (`sumatoria`) | `0` | sumar `x` |
| buscar (`pertenece`) | `False` | comparar `x` y seguir si hace falta |

> **Para recordar:** `[]` responde la pregunta mínima; `x:xs` reduce el problema a `xs`.

## 6. Lectura de patrones

```haskell
f []      = ...       -- no hay elementos
f (x:xs)  = ...       -- x es el primero; xs son los restantes
f (_:xs)  = ...       -- el primero no importa
```

No hay que calcular `head` y `tail` explícitamente: el patrón `x:xs` ya los separa de forma segura.d

## Checklist para cada función sobre listas

1. ¿Qué debe devolver para `[]`?
2. Si la lista es `x:xs`, ¿qué aporta `x`?
3. ¿Cómo combino ese aporte con la solución de `xs`?
4. ¿La llamada recursiva usa una lista más corta?