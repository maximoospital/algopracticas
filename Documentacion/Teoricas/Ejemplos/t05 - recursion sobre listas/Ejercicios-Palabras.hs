sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs) | x==y && x==' ' = sacarBlancosRepetidos (y:xs)
                             | otherwise = [x] ++ sacarBlancosRepetidos (y:xs) 

contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras (xs) = (contarEspacios (quitarEspaciosIniFin (sacarBlancosRepetidos xs))) + 1

quitarEspaciosIniFin :: [Char] -> [Char]
quitarEspaciosIniFin [] = []
quitarEspaciosIniFin (x:xs) | x==' ' && head(reverse(xs))==' ' = (quitarUltimo xs)
                        | x==' ' = xs
                        | head(reverse(xs))==' ' = quitarUltimo (x:xs)
                        | otherwise = x:xs

contarEspacios :: [Char] -> Int
contarEspacios [] = 0
contarEspacios (x:xs) | x==' '= 1+contarEspacios xs
                        | otherwise = contarEspacios xs

quitarUltimo :: [Char] -> [Char]
quitarUltimo [] = []
quitarUltimo [x] = []
quitarUltimo (x:xs) = [x]++(quitarUltimo xs)

palabras :: [Char] -> [[Char]]
palabras xs = armarListaPalabras (quitarEspaciosIniFin xs)

armarListaPalabras :: [Char] -> [[Char]]
armarListaPalabras [] = []
armarListaPalabras xs = [primerPalabra xs] ++ armarListaPalabras (sacarPrefijo (primerPalabra xs) xs)

primerPalabra :: [Char] -> [Char]
primerPalabra [] = []
primerPalabra [' '] = []
primerPalabra [x] = [x]
primerPalabra (x:' ':xs) = [x] 
primerPalabra (x:y:xs) = [x] ++ primerPalabra (y:xs)

sacarPrefijo :: [Char] -> [Char] -> [Char]
sacarPrefijo [] [] = []
sacarPrefijo [] (y:ys) | y==' ' = ys
                        | otherwise = (y:ys)
sacarPrefijo (x:xs) (y:ys) | x==y = sacarPrefijo xs ys
                           | y==' ' = ys
                           | otherwise = ys

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga xs | length (primerPalabra xs) > length (palabraMasLarga (sacarPrefijo (primerPalabra xs) xs)) = primerPalabra xs  
                   | otherwise = palabraMasLarga (sacarPrefijo (primerPalabra xs) xs)

--Otra estrategia primero armando una estructura con cada longitud...
armarListaPalabrasLongitud :: [Char] -> [([Char], Int)]
armarListaPalabrasLongitud [] = []
armarListaPalabrasLongitud xs = [(primerPalabra xs, length (primerPalabra xs))] ++ armarListaPalabrasLongitud (sacarPrefijo (primerPalabra xs) xs)

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (xs:xss) = xs ++ (aplanar xss)
