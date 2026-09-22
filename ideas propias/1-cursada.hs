{-
PROYECTO DE PRACTICA #1: Estatus de Cursada
-}


type Cursada = (Bool, Bool, Float, Float, Bool, Float, Float)
type Condicion = String

-- Funciones basicas, utils

-- Calcula sumatoria de numeros dados.
sumatoria :: [Float] -> Float
sumatoria [] = 0
sumatoria (num:resto) = num + sumatoria resto

-- Calcula la longitud de una secuencia dada
longitud :: [a] -> Float
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- Saca un promedio de la secuencia de numeros dada
promedio :: [Float] -> Float
promedio [] = 0
promedio lista = (sumatoria lista)/(longitud lista)

-- Saca un modulo de un numero dado
modulo :: Float -> Float
modulo num
    | num < 0 = (-num)
    | otherwise = num

-- Saca la coma de un numero dado
soloComa :: Float -> Float
soloComa num 
    | 0 < modulo num && modulo num < 1 = num
    | num == 1 = 0
    | otherwise = soloComa (num - 1)

-- Redondea un numero dado
redondeo :: Float -> Float
redondeo num
    | soloComa num < 0.5 = (num - soloComa num) 
    | soloComa num >= 0.5 = (num - soloComa num) + 1

-- Saca promedio y lo redondea
promedioRedondeado :: [Float] -> Float
promedioRedondeado [] = 0
promedioRedondeado lista = redondeo(promedio lista)

-- Si rendiste un recuperatorio, este pisa la nota del parcial.
notaParcial :: (Float, Float) -> Float
notaParcial parciales 
    | snd parciales > 0 = snd parciales
    | otherwise = fst parciales

-- Promedio redondeado de parciales, con procesado de nota parcial incluido.
notasParciales :: (Float, Float, Float, Float) -> Float
notasParciales (par1, recupar1, par2, recupar2) = promedioRedondeado [notaParcial (par1, recupar1), notaParcial (par2, recupar2)]

{- 
Ahora el programa principal, estadoCursada.
Usa el tipo Cursada, el cual requiere los parametros:
    - Aprobo el CBC? [Bool]
    - Estuvo presente en las revisiones? [Bool]
    - Nota de Primer Parcial [Float]
    - Recuperatorio del Primer Parcial (Si no rindio, es 0) [Float]
    - Aprobo el TP? [Bool]
    - Nota de Segundo Parcial [Float]
    - Recuperatorio del Segundo Parcial (Si no rindio, es 0) [Float]

-}

estadoCursada :: Cursada -> Condicion
estadoCursada (cbc, revision, par1, recupar1, tp, par2, recupar2) 
-- Si no aprobaste el CBC no podes aprobar
    | cbc == False = "No se puede aprobar por deber CBC."
-- Desaprobar el TP o tener notas en parciales menor a 6 es recursado.
    | tp == False || notasParciales (par1, recupar1, par2, recupar2) < 6 = "Recursa." 
-- Si hiciste las actividades, aprobaste el TP y tu promedio de parciales es superior o igual a 8: promocion directa
    | revision == True && tp == True && notasParciales (par1, recupar1, par2, recupar2) >= 8 = "Promocion directa!"
-- Si aprobaste el TP y tus notas en parciales estan entre 6 y 7, final escrito
    | tp == True && 6 <= notasParciales (par1, recupar1, par2, recupar2) && notasParciales (par1, recupar1, par2, recupar2) < 7 = "Final escrito, tenes 8 cuatrimestres para rendir el final."
-- Resto, final oral.
    | otherwise = "Final oral (coloquio). Tenes hasta las mesas de finales de Diciembre antes de que se vuelva escrito, apurate!!!"