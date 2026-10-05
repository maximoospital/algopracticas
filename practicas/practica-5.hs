-- Ejercicio 1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- Ejercicio 1.2
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

-- Ejercicio 1.2
principio :: [t] -> [t]
principio [x] = [x]
principio (x:xs) = [x]

-- Ejercicio 1.4

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

-- Ejercicio 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = (e == x) || pertenece e xs

-- Ejercicio 2.2
primero :: [t] -> t
primero [x] = x
primero (x:xs) = x

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales t
    | longitud t == 1 = True
todosIguales (x:xs)
    | x /= (primero xs)   = False
    | otherwise           = todosIguales xs


-- Ejercicio 2.3

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs)
    | pertenece x xs = False
    | otherwise      = todosDistintos xs

-- Ejercicio 2.4

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos lista = not (todosDistintos lista)

-- Ejercicio 2.5 

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar objeto (x:xs)
    | objeto == x = xs
    | otherwise   = x : quitar objeto xs

-- Ejercicio 2.6
