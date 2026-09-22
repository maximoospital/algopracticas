sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]  -- Si hay un solo carácter, lo devolvemos tal cual.
sacarBlancosRepetidos (x:y:xs)
  | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)  -- Si hay dos espacios, ignoramos uno.
  | otherwise = x : sacarBlancosRepetidos (y:xs)  -- Si no, agregamos el carácter actual.

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras [x]      | x == ' ' = 0
                        | otherwise = 1
contarPalabras (x:y:xs) | x/=' ' && y == ' ' = 1 + contarPalabras (y:xs)
                        | otherwise = contarPalabras (y:xs)

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs) | x == ' ' = palabras xs
                | otherwise = primeraPalabra (x:xs) : palabras (sacarPrimerPalabra(x:xs))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x /= ' ' = x : (primeraPalabra xs)
                      | otherwise = []

sacarPrimerPalabra :: [Char] -> [Char]
sacarPrimerPalabra [] = []
sacarPrimerPalabra (x:xs) | x /= ' ' = sacarPrimerPalabra xs
                          | otherwise = (x:xs)

palabraMaslarga :: [Char] -> [Char]
palabraMaslarga xs = buscarElMaximo (palabras xs)

buscarElMaximo :: [[Char]] -> [Char]
buscarElMaximo [] = []
buscarElMaximo [x] = x
buscarElMaximo (x:y:xs) | length x > length y = buscarElMaximo (x:xs)
                        | otherwise = buscarElMaximo (y:xs)

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs