-- Ejercicio 1

fibonacci :: Integer -> Integer 
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)

-- Ejercicio 2
-- parteEntera toma un numero y lo redondea a un entero
-- x mayor o igual a 0
-- resultado menor o igual a x que es menor a resultado + 1
-- resultado es x sin la coma basicametne
-- esto es basicamente una funcion piso para el modulo de un numero

parteEntera :: Float -> Integer
parteEntera num
    | num < 1 = 0
    | otherwise = 1 + parteEntera(num - 1)

{-
    Ejercicio 3
    problema esDivisible (x1: N, x2: N) : Bool {
        requiere: { True }
        asegura: { res = true <=> (existe un K tal que x = k * y) }
    }
-}

esDivisible :: Integer -> Integer -> Bool
esDivisible x y
    | x == 0 = True
    | x < y = False
    | otherwise = esDivisible (x - y) y

{-
    Ejercicio 4
    problema sumaImpares (num: N) : Z {
        requiere: { True }
        asegura: { num == 1 -> res= 1 }
        asegura: { }
    }
-}

posicionImpar :: Integer -> Integer
posicionImpar num = 2*num-1

sumaImpares :: Integer -> Integer
sumaImpares num
    | num == 1 = 1
    | otherwise = posicionImpar num + sumaImpares (num-1)

-- Ejercicio 5

medioFact :: Integer -> Integer
medioFact num
    | num == 0 || num == 1 = 1
    | otherwise = num * medioFact (num -2) 

-- Ejercicio 6

numeroUnidad :: Integer -> Integer
numeroUnidad num = mod num 10

numeroDecena :: Integer -> Integer
numeroDecena num = mod (div num 10) 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales num 
    | num <= 9 = True
    | numeroDecena num /= numeroUnidad num = False
    | numeroDecena num == numeroUnidad num = todosDigitosIguales (mod (div num 10) 10)
    | otherwise = False

-- Ejercicio 7