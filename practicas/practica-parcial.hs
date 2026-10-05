rango :: Integer -> Integer -> [Integer]
rango d h = [d..h]

buscarDivisor :: Integer -> Integer -> Integer
buscarDivisor 0 _ = 0
buscarDivisor 1 _ = 1
buscarDivisor n d
    | mod n d == 0 = d
    | otherwise    = buscarDivisor n (d+1)

menorDivisor :: Integer -> Integer
menorDivisor n = buscarDivisor n 2

esPrimo :: Integer -> Bool
esPrimo 0 = False
esPrimo 1 = False
esPrimo 2 = True
esPrimo n = (menorDivisor n) == n

primos :: [Integer] -> [Integer]
primos [] = []
primos (x:xs) 
    | not (esPrimo x) = xs
    | otherwise       = x : primos xs

cabeza :: (Eq t) => [t] -> t
cabeza [x] = x
cabeza (x:xs) = x

hayGemelos :: [Integer] -> Bool
hayGemelos [] = False
hayGemelos (x:xs)
    | x == ((cabeza xs)-2) = True
    | otherwise = hayGemelos xs

hayPrimosGemelos :: Integer -> Integer -> Bool
hayPrimosGemelos d h
    | d == 0 || h == 0 = False
    | d > h = False
    | hayGemelos (primos (rango d h)) = True
    | otherwise = False