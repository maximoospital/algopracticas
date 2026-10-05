-- Ejercicio 1

fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)

-- Ejercicio 2
{-
    parteEntera nos da la parte sin coma de un numero flotante
    basicamente, una funcion piso.
    x debe ser mayor o igual a 0, por ende 0 es un caso base:
    el resultado es menor a x pero si le sumamos 1 se vuelve mayor a x
    por ende la diferencia ahi es la coma
-}

parteEntera :: Float -> Integer
parteEntera n
    | n < 1 = 0
    | otherwise = 1 + parteEntera (n - 1)

-- Ejercicio 3
{-
    esDivisible nos dice si un numero A es divisible por B, pero sin mod ni div.
    Para saber si un numero es divisible por otro, vamos restando B de A hasta llegar a 0.
-}

esDivisible :: Integer -> Integer -> Bool
esDivisible a b
    | a == 0 = True
    | a < b = False
    | otherwise = esDivisible (a - b) b

-- Ejercicio 4
{-
    Dado un numero n, tenemos que sumar los primeros n numeros impares.
    Basicamente, n es una posicion en la lista de impares, y debemos sumar hasta alcanzarlo.
    Implemento una auxiliar que me de la posicion de impar de ese n, y sumo recursionando los menores.
-}

absoluto :: Integer -> Integer
absoluto n
    | n < 0 = (-n)
    | otherwise = n

posicionImpar :: Integer -> Integer
posicionImpar 1 = 1
posicionImpar n = 2*n-1

sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = posicionImpar(absoluto (n)) + sumaImpares(n - 1)

-- Ejercicio 5
{-
    Dado un numero n, debemos multiplicar a n por (n-2i)
-}

medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact(n - 2)

-- Ejercicio 6 
{-
    Le damos un numero y va a iterar por cada digito para determinar si son iguales.
    Basicamente necesitamos siempre 2 digitos a mano para comparar
-}

ultimoDigito :: Integer -> Integer
ultimoDigito n
    | absoluto n <= 0 = 0
    | absoluto n <= 9 = absoluto (n)
    | otherwise = mod (absoluto n) 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
    | absoluto n <= 9 = True
    | ultimoDigito n /= ultimoDigito (div (absoluto n) 10) = False
    | otherwise = todosDigitosIguales (div (absoluto n) 10)

-- Ejercicio 7
{-
    iesimoDigito, dado un numero y una posicion i, nos da el q va en ese lugar.
-}

cantDigitos :: Integer -> Integer
cantDigitos n
    | absoluto n <= 9 = 1
    | otherwise = 1 + cantDigitos (div (absoluto n) 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i
    | (cantDigitos n) < i  = 0
    | otherwise = mod (div n (10 ^ (cantDigitos n - i))) 10

-- Ejercicio 8
{-
    sumaDigitos, suma los digitos de un numero natural.
-}

sumaDigitos :: Integer -> Integer
sumaDigitos n
    | n <= 9 = n
    | otherwise = mod n 10 + sumaDigitos(div n 10)

-- Ejercicio 9
{-
    Comparamos primer y ultimo numero. Si son diferentes, false, de lo contrario los removemos y vamos a lo siguiente.
    para remover el ultimo digito: div n 10
    para remover el primer digito: mod n 10 elevado a cantDigitos
-}


esCapicua :: Integer -> Bool
esCapicua n
    | cantDigitos n <= 1 = True
    | cantDigitos n == 2 = (ultimoDigito n) == (ultimoDigito (div n 10))
    | (mod n 10) /= (div n (10^((cantDigitos n)-1))) = False
    | otherwise = esCapicua (div (mod n (10 ^ ((cantDigitos n)-1))) 10)

-- Ejercicio 10 a)
{-
    Sumatoria, caso base 0.
    2 elevado a la i
    n es un natural (incluye a 0)
-}

f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2^n + f1(n - 1)

-- Ejercicio 10 b)
{-
    Dados un numero n y q, partimos desde 1 hasta n, elevando a q a la i
-}

f2 :: Integer -> Integer -> Integer
f2 1 q = q
f2 n q = q^n + f2 (n-1) q

-- Ejercicio 10 c)
{-
    Dados un numero n y q, partimos desde 1 hasta el doble d en, elevando a q por i
-}

f3 :: Integer -> Integer -> Integer
f3 0 _ = 0
f3 n q = ( f3 (n - 1) q ) + q^((2*n)-1) + q^(2*n)

-- Ejercicio 10 d)
{-
    Dados un numero n y un q, partimos desde n hasta 2n, elevando q por i
-}

f4 :: Integer -> Integer -> Integer
f4 0 q = 1
f4 n q = ( (f4 (n - 1) q) - (q^(n - 1)) ) + q^((2*n)-1) + q^(2*n)

-- Ejerciciio 11 a)
{-
    problema eAprox (n: Z) : R {
        requiere : {n >= 0}
        asegura: { res = 1/fact(n) + eAprox(n - 1) }
    }
-}

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial(n - 1)


eAprox :: Integer -> Float
eAprox 0 = 1.0
eAprox n = eAprox(n - 1) + (1/(fromIntegral(factorial n)))

-- Ejercicio B
e :: Float
e = eAprox 10


-- Ejercicio 12 
{-
    an = 2 + 1/(2+1/(2+1/(2+(1/2))))
    a1 = 2
    an = 2 + 1/(an - 1)
-}

an :: Float -> Float
an 1 = 2.0
an n = 2 + 1/(an (n - 1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (an (fromIntegral n) ) - 1.0

-- Ejercicio 13
{-
    dados n y m, es la sumatoria de sumatorias de i elevado a j

-}

fInt :: Integer -> Integer -> Integer
fInt 0 _ = 0
fInt _ 0 = 0
fInt n m = (n^m) + (fInt (n - 1) m)

f :: Integer -> Integer -> Integer
f 0 _ = 0
f _ 0 = 0
f n m = fInt n m + (f n (m - 1))

-- Ejercicio 14
{-
    Dados tres naturales q, n y m
    suma todas las potencias de la forma q elevado a a+b, tal que 1 <= a <= n y 1<= b <= m 
-}

sumaInt :: Integer -> Integer -> Integer -> Integer
sumaInt _ _ 0 = 0
sumaInt q a b = (q^(a+b)) + sumaInt q a (b-1)

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q a b = sumaInt q a b + sumaPotencias q (a-1) b


-- Ejercicio 15

sumaRacInt :: Integer -> Integer -> Float
sumaRacInt _ 0 = 0
sumaRacInt n m = ((fromIntegral n)/(fromIntegral m)) + sumaRacInt n (m-1)

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = sumaRacInt n m + sumaRacionales (n - 1) m

-- Ejercicio 16 a)

buscarDivisor :: Integer -> Integer -> Integer
buscarDivisor 0 _ = 0
buscarDivisor 1 _ = 1
buscarDivisor n d
    | mod n d == 0 = d
    | otherwise    = buscarDivisor n (d+1)

menorDivisor :: Integer -> Integer
menorDivisor n = buscarDivisor n 2

-- Ejercicio 16 b)

esPrimo :: Integer -> Bool
esPrimo 0 = False
esPrimo 1 = True
esPrimo 2 = True
esPrimo n = (menorDivisor n) == n

-- Ejercicio 16 c)

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b = ((menorDivisor a) /= (menorDivisor b))
