---
dg-publish: true
tags:
  - algo1
  - resumen
---
## Recursion
Hasta ahora hemos visto especificar funciones que consisten de expresiones sencillsa. Pero, por ejemplo, si queremos especificar un factorial, necesitariamos utilizar **recursion**: invocar a la funcion en instancias mas pequeñas para resolver el problema.
## 1. La receta: base, reducción, combinación
Una definición recursiva tiene:

1. **Caso(s) base:** respuestas directas, sin llamadas recursivas.
2. **Paso recursivo:** reduce el argumento y usa el resultado del caso menor.
3. **Progreso:** cada llamada debe acercarse inevitablemente a una base; si no, no termina.

```haskell
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)  -- requiere n > 0 aquí
```

Para `factorial 3`: primero se *desarma* hasta `factorial 0`; después se *arma*:
`3 * (2 * (1 * 1)) = 6`.
> **Pregunta guía:** “Si ya supiera resolver el caso anterior, ¿qué agrego para resolver este?”
### Cuidado con las bases

La reducción y las bases deben cubrir **todos** los valores permitidos. Por ejemplo, esto falla para impares positivos porque llega a `esPar 1` y luego a negativos:

```haskell
esPar 0 = True
esPar n = esPar (n - 2)
```

Dos soluciones correctas (para `n >= 0`) son:

```haskell
esPar 0 = True
esPar 1 = False
esPar n = esPar (n - 2)

esPar' 0 = True
esPar' n = not (esPar' (n - 1))
```

## 2. Recursión e inducción: la misma escalera, en sentidos opuestos

| Para demostrar (inducción)   | Para programar (recursión)       |
| ---------------------------- | -------------------------------- |
| Probá la base.               | Definí la base.                  |
| Suponé cierto el caso menor. | Usá la llamada al caso menor.    |
| Demostrá el caso siguiente.  | Combiná y obtené el caso actual. |

Ejemplo: la suma de los primeros `n` impares. El último impar es `2*n - 1`:

```haskell
sumaPrimerosImpares :: Integer -> Integer
sumaPrimerosImpares 1 = 1
sumaPrimerosImpares n = sumaPrimerosImpares (n - 1) + (2*n - 1)
-- requiere n >= 1
```

La hipótesis inductiva justifica que, si el caso menor es correcto, este paso también lo es. La reducción hasta la base garantiza que alcanza para todo `n` permitido.

## 3. Generalizar para encontrar una reducción

Si el problema original no se relaciona claramente con un caso menor, agregá un parámetro que exprese “hasta dónde”.

No hay una relación útil entre la suma de divisores de `n` y la de `n - 1`; sí entre revisar hasta `k` y hasta `k - 1`:

```haskell
sumaDivisoresHasta :: Integer -> Integer -> Integer
sumaDivisoresHasta n 0 = 0
sumaDivisoresHasta n k
  | n `mod` k == 0 = k + sumaDivisoresHasta n (k - 1)
  | otherwise      =     sumaDivisoresHasta n (k - 1)

sumaDivisores :: Integer -> Integer
sumaDivisores n = sumaDivisoresHasta n n
-- requiere n > 0
```

`sumaDivisores` **no es recursiva directamente**: delega en la auxiliar, que sí lo es.

> **Truco memorable:** si no podés achicar el problema, preguntá: “¿qué parámetro me falta para medir el avance?”.

## 4. Más de un parámetro: una recursión por cada nivel

Para la sumatoria doble $\sum_{i=1}^{n}\sum_{j=1}^{m} i^j$, separá la suma interna. La auxiliar baja `j`; la principal baja `n`.

```haskell
sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna n 0 = 0
sumatoriaInterna n j = n^j + sumatoriaInterna n (j - 1)

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaDoble (n - 1) m + sumatoriaInterna n m
-- uso externo: n > 0 y m > 0
```

La llamada anidada no es magia: `sumatoriaDoble` suma una fila por vez; `sumatoriaInterna` suma los términos de esa fila.

## Checklist para cada ejercicio

- ¿Cuál es el caso más chico válido? → **base**.
- ¿Qué argumento disminuye? → **reducción**.
- ¿Qué aporta el elemento que saco? → **combinación**.
- ¿Toda llamada llega a una base? → **terminación**.
- ¿No hay relación simple? → **generalizá con un auxiliar**.