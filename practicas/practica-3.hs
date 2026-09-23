-- Ejercicio 1 a)
f :: Integer -> Integer
f num
    | num == 1 = 8
    | num == 4 = 131
    | num == 16 = 16

-- Ejercicio 1 b)
g :: Integer -> Integer
g num
    | num == 8 = 16
    | num == 16 = 4
    | num == 131 = 1

-- Ejercicio 1 c)
h :: Integer -> Integer
h num = f(g(num))

k :: Integer -> Integer
k num = g(f(num))

{-
    Ejercicio 2 a)

    problema absoluto (numero: Entero) : Entero {
        requiere: { True }
        asegura: { (numero < 0 -> res = -numero) y (numero >= 0 -> res = numero)}
    }
-}
absoluto :: Integer -> Integer
absoluto num
    | num < 0 = (-num)
    | otherwise = num

{-
    Ejercicio 2 b)

    problema maximoAbsoluto (numero1: Entero, numero2: Entero) : Entero {
        requiere: { True }
        asegura: { (absoluto(numero1) >= absoluto(numero2) -> res = absoluto(numero1)) }
        asegura: { (absoluto(numero2) > absoluto(numero1) -> res = absoluto(numero2)) }
    }
-}

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto num1 num2
    | absoluto(num1) >= absoluto(num2) = absoluto(num1)
    | absoluto(num2) > absoluto(num1) = absoluto(num2)

{-
    Ejercicio 2 c)

    problema maximo3 (numero1: Entero, numero2: Entero, numero3: Entero) : Entero {
        requiere: { True }
        asegura: { numero1 > numero2 && numero1 > numero3 = numero1 }
        asegura: { numero2 > numero2 && numero2 > numero3 = numero2 }
        asegura: { numero3 > numero2 && numero3 > numero1 = numero3 }
    }
-}

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 num1 num2 num3
    | num1 > num2 && num1 > num3 = num1
    | num2 > num1 && num2 > num3 = num2
    | num3 > num2 && num3 > num1 = num3
    | otherwise = num1

{-
    Ejercicio 2 d)

    problema algunoEsCero (numero1: Q, numero2: Q) : Bool {
        requiere: { True }
        asegura: { numero1 == 0 o numero2 == 0 = True }
    }
-}

algunoEsCero :: Float -> Float -> Bool
algunoEsCero num1 num2
    | num1 == 0 || num2 == 0 = True
    | otherwise = False

algunoEsCeroRedux :: Float -> Float -> Bool
algunoEsCeroRedux 0 _ = True
algunoEsCeroRedux _ 0 = True
algunoEsCeroRedux _ _ = False

{-
    Ejercicio 2 e)

    problema ambosSonCero (numero1: Q, numero2: Q) : Bool {
        requiere: { True }
        asegura: { numero1 == 0 y numero2 == 0 = True }
    }
-}

ambosSonCero :: Float -> Float -> Bool
ambosSonCero num1 num2
    | num1 == 0 && num2 == 0 = True
    | otherwise = False

ambosSonCeroRedux :: Float -> Float -> Bool
ambosSonCeroRedux 0 0 = True
ambosSonCeroRedux _ _ = False

{-
    Ejercicio 2 f)

    problema enMismoIntervalo (num1: R, num2: R) : Bool {
        requiere: { True }
        asegura: { res = True <=> ((num1 <= 3 && num2 <= 3) ||
                                  (3 < num1 && num1 <= 7 && 3 < num2 && num2 <= 7 ) ||
                                  (7 < num1 && 7 < num2)) }
    }
-}

enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo num1 num2
    | num1 <= 3 && num2 <= 3 = True
    | 3 < num1 && num1 <= 7 && 3 < num2 && num2 <= 7 = True
    | 7 < num1 && 7 < num2 = True
    | otherwise = False

{-
    Ejercicio 2 g)

    problema sumaDistintos (n1: Z, n2: Z, n3: Z) : Z {
        requiere: { True }
        asegura: { (n1 /= n2 && n2 /= n3 && n3 /= n1) ->  res = n1+n2+n3 }
        asegura: { (n1 == n2 && n2 == n3) -> res = n1 }
        asegura: { ((n2 == n3 && n2 /= n1) || (n1 == n3 && n2 /= n1)) -> res = n1+n2 }
        asegura: { (n2 == n1 && n3 /= n1) -> res = n1+n3 }
    }
-}

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos n1 n2 n3
    | n1 == n2 && n2 == n3 = n1
    | n2 == n1 && n3 /= n1 = n1+n3
    | n2 == n3 || n1 == n3 = n1+n2
    | otherwise            = n1+n2+n3

{-
    Ejercicio 2 g)

    problema esMultiploDe (n1: N, n2: N) : Bool {
        requiere: { True }
        asegura: { res = true <=> (mod n1 n2 == 0) }
    }
-}

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe n1 n2 = mod n1 n2 == 0

{-
    Ejercicio 2 i)

    problema digitoUnidades (n1: Z) : Z {
        requiere: { True }
        asegura: { res = mod absoluto(n1) 10 }
    }
-}

digitoUnidades :: Integer -> Integer
digitoUnidades num = mod (absoluto num) 10

{-
    Ejercicio 2 j)

    problema digitoDecenas (n1: Z) : Z {
        requiere: { 9 < n1 }
        asegura: { res = digitoUnidades(div n1 10) }
    }
-}

digitoDecenas :: Integer -> Integer
digitoDecenas n1 = digitoUnidades(div n1 10)

-- Ejercicio 3

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y = mod (-x) (y) == 0

{-
    Ejercicio 4 a)
    problema productoInterno ((x1, x2): R x R, (y1, y2): R x R) : R {
        requiere: { True }
        asegura: { res = (x1*y1)+(x2*y2) }
    }
-}

productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (x1, x2) (y1, y2) = (x1*y1)+(x2*y2)

{-
    Ejercicio 4 b)
    problema esParMenor ((x1, x2): R x R, (y1, y2): R x R) : Bool {
        requiere: { True }
        asegura: { res = True <=> x1 < y1 && x2 < y2 }
    }
-}

esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (x1, x2) (y1, y2) = x1 < y1 && x2 < y2

{-
    Ejercicio 4 c)
    problema distancia ((x1, x2): R x R, (y1, y2): R x R) : R {
        requiere: { True }
        asegura: { res = absoluto(sqrt( ( (y1-x1) ^ 2) + ( (y2-x2) ^ 2 ) ))}
    }
-}

type Coordenada = (Float, Float)
distancia :: Coordenada -> Coordenada -> Float
distancia (x1, x2) (y1, y2) = sqrt( ((y1-x1)^2) + ((y2-x2)^2) )

{-
    Ejercicio 4 d)
    problema sumaTerna ((x1, x2, x3): Z x Z x Z) : Z {
        requiere: { True }
        asegura: { res = x1+x2+x3 }
    }
-}

type Terna = (Integer, Integer, Integer)
sumaTerna :: Terna -> Integer
sumaTerna (x1, x2, x3) = x1 + x2 + x3


{-
    Ejercicio 4 e)

    problema sumarSoloMultiplos ( (x1, x2, x3) : Z x Z x Z, n1: N ) : Z {
        requiere: { True }
        asegura: { (mod x1 n1 /= 0) && (mod x2 n1 /= 0) && (mod x3 n1 /= 0) -> res = 0 }
        asegura: { (mod x1 n1 == 0) && (mod x2 n1 == 0) && (mod x3 n1 == 0) -> res = x1 + x2 + x3 }
        asegura: { (mod x1 n1 == 0) && not (mod x2 n1 == 0) && not (mod x3 n1 == 0) -> res = x1 }
        asegura: { not (mod x1 n1 == 0) && (mod x2 n1 == 0) && not (mod x3 n1 == 0) -> res = x2 }
        asegura: { not (mod x1 n1 == 0) && not (mod x2 n1 == 0) && (mod x3 n1 == 0) -> res = x3 }
        asegura: { not (mod x1 n1 == 0) && (mod x2 n1 == 0) && (mod x3 n1 == 0) -> res = x2 + x3 }
        asegura: { (mod x1 n1 == 0) && not (mod x2 n1 == 0) && (mod x3 n1 == 0) -> res = x1 + x3 }
        asegura: { (mod x1 n1 == 0) && (mod x2 n1 == 0) && not (mod x3 n1 == 0) -> res = x1 + x2 }
    }
-}

sumarSoloMultiplos :: Terna -> Integer -> Integer
sumarSoloMultiplos (x1, x2, x3) n1
    | esMultiploDe x1 n1 && esMultiploDe x2 n1 && esMultiploDe x3 n1 = x1 + x2 + x3
    | esMultiploDe x1 n1 && not (esMultiploDe x2 n1) && not (esMultiploDe x3 n1) = x1
    | not (esMultiploDe x1 n1) && esMultiploDe x2 n1 && not (esMultiploDe x3 n1) = x2
    | not (esMultiploDe x1 n1) && not (esMultiploDe x2 n1) && esMultiploDe x3 n1 = x3
    | not (esMultiploDe x1 n1) && esMultiploDe x2 n1 && esMultiploDe x3 n1 = x2 + x3
    | esMultiploDe x1 n1 && not (esMultiploDe x2 n1) && esMultiploDe x3 n1 = x1 + x3
    | esMultiploDe x1 n1 && esMultiploDe x2 n1 && not (esMultiploDe x3 n1) = x1 + x2
    | otherwise = 0

{-
    Ejercicio 4 f)

    problema posPrimerPar ((x1, x2, x3): Z x Z x Z) : Z {
        requiere: { True }
        asegura: { mod x1 2 == 0 -> res = 1 }
        asegura: { mod x2 2 == 0 -> res = 2 }
        asegura: { mod x3 2 == 0 -> res = 3 }
        asegura: { otherwise -> res = 4 }
    }
-}

posPrimerPar :: Terna -> Integer
posPrimerPar (x1, x2, x3) 
    | mod x1 2 == 0 = 1
    | mod x2 2 == 0 = 2
    | mod x3 2 == 0 = 3
    | otherwise = 4

{-
    Ejercicio 4 g)
    problema crearPar (x1: T1, x2: T2) : T1xT2 {
        requiere: { True }
        asegura: { res = (x1, x2) }
    }
-}

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

{-
    Ejercicio 4 h)
    problema invertir ((x1, x2) : T1xT2) : T2xT1 {
        requiere: { True }
        asegura: { res = (x2, x1) }
    }
-}

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- Ejercicio 5

f5 :: Integer -> Integer
f5 n 
    | n <= 7 = n*n 
    | otherwise =  2*n-1

g5 :: Integer -> Integer
g5 n
    | mod n 2 == 0 = div (n) 2
    | otherwise = 3*n+1

todosMenores :: Terna -> Bool
todosMenores (t0, t1, t2) = (f5 t0 > g5 t0) && (f5 t1 > g5 t1) && (f5 t2 > g5 t2)

-- Ejercicio 6
type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto año = (mod año 4 == 0) && (mod año 100 /= 0 || mod año 400 == 0)

-- Ejercicio 7
type Punto3D = (Float, Float, Float)

flAbsoluto :: Float -> Float
flAbsoluto num
    | num < 0 = (-num)
    | otherwise = num

distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (x0,x1,x2) (y0,y1,y2) = (flAbsoluto(x0-y0)) + (flAbsoluto(x1-y1)) + (flAbsoluto(x2-y2))

-- Ejercicio 8

sumaUltimosDosDigitos :: Integer -> Integer 
sumaUltimosDosDigitos num = (mod (absoluto num) 10) + (mod (div (absoluto num) 10) 10)

comparar :: Integer -> Integer -> Integer
comparar a b 
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = (-1)
    | otherwise = 0

{-
    a) Dado un numero real, si es 0 nos da 1, si no 0
    b) Dado un numero real, si es 1 nos da 15, si es -1 nos da -15
    c) Dado un numero real, si es menor o igual a 9 nos da 7, si es mayor o igual a 3 nos da 5
    d) Dados dos numeros reales, los sumamos y dividimos la sumatoria por 2
    e) Dada una tupla de reales, sumamos el primer y segundo elemento y dividimos la sumatoria por 2
    f) Dado un numero real y un entero, si el truncado del real es igual al entero, devolvemos true.
-}
