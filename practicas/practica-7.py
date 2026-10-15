# Ejercicio 1

def pertenece(s:list[int], e: int) -> bool:
    if (e in s):
        return True
    else:
        return False

print("Pertenece 1 a [1,2,3,4,5,6,7,1,2]?", pertenece([1,2,3,4,5,6,7,1,2],1))

def divide_a_todos(s:list[int], e: int) -> bool:
    for num in s:
        if (num % e != 0):
            return False
    return True

print("2 divide a 2,4,8,10,16?", divide_a_todos([2,4,8,10,16],2))

def suma_total(s:list[int]) -> int:
    numBuffer = 0
    for num in s:
        numBuffer += num
    return numBuffer

print("Suma total de 1,2,3,4,5?", suma_total([1,2,3,4,5]))

def maximo(s:list[int]) -> int:
    numSelect = s[0]
    for num in s:
        if (numSelect < num):
            numSelect = num
    return numSelect

print ("Numero maximo de 1,2,3,4,5,2,3,4?", maximo([1,2,3,4,5,2,3,4]))

def minimo(s:list[int]) -> int:
    numSelect = s[0]
    for num in s:
        if (numSelect > num):
            numSelect = num
    return numSelect

print ("Numero minimo de 1,2,3,4,5,2,3,4?", minimo([1,2,3,4,5,2,3,4]))

def ordenados(s:list[int]) -> bool:
    i = 0
    while (i < (len(s)-1)) :
        if (s[i] < s[i+1]):
            i += 1
        else:
            return False
    return True

print ("Esta ordenada la secuencia 1,2,3,4?", ordenados([1,2,3,4]))

def primerPos(s:list[int], e: int) -> int:
    i = 0
    while (i < len(s)):
        if (s[i] == e):
            return i
        else:
            i += 1

print("Funcion ayuda primerPos: Primer posicion de 9 en 8,7,9,5,4,9?", primerPos([8,7,9,5,4,9],9))

def pos_maximo(s:list[int]) -> int:
    if len(s) == 0:
        return -1
    posSelect = 0
    for num in s:
        if (num > s[posSelect]):
            posSelect = primerPos(s, num)
    return posSelect

print ("Posicion maxima en la secuencia 1,2,3,4,6,5,4?", pos_maximo([1,2,3,4,6,5,4]))

def pos_minimo(s:list[int]) -> int:
    if len(s) == 0:
        return -1
    posSelect = 0
    for num in s:
        if (num < s[posSelect]):
            posSelect = primerPos(s, num)
    return posSelect

print ("Posicion minima en la secuencia 1,2,3,4,6,0,4?", pos_minimo([1,4,3,4,6,0,4]))

def long_mayorASiete(s:list[str]) -> bool:
    for nombre in s:
        if (len(nombre) > 7):
            return True
    return False

print ("Hay un nombre con mas de siete letras en 'Maximo','Agustin','Guadalupe' y 'Matias?", long_mayorASiete(["Maximo","Agustin","Guadalupe","Matias"]))

def es_palindroma(s:str) -> bool: 
    if len(s) < 2:
        return True
    i = 0
    while (i < len(s)):
        if (s[i].lower() != s[len(s)-1-i].lower()):
            return False
        else:
            i += 1
    return True

print ("Es un palindroma anilina?", es_palindroma("anilina"))

def iguales_consecutivos(s:list[int]) -> bool:
    i = 0
    while (i < (len(s)-3)):
        if (s[i] == s[i+1] == s[i+2]):
            return True
        i += 1
    return False

print ("Hay tres iguales consecutivos en 1,2,3,3,3,4,5?", iguales_consecutivos([1,2,3,3,3,4,5]))

def vocales_distintas(palabra:str) -> bool:
    vocales = ['a','e','i','o','u']
    vocalesUsadas = []
    for letra in palabra.lower():
        if(letra in vocales and letra not in vocalesUsadas):
            vocalesUsadas.append(letra)
    if(len(vocalesUsadas) >= 3):
        return True
    else:
        return False

print ("Hay almenos 3 vocales distintas en aeiou?", vocales_distintas("aeiou"))

def pos_secuencia_ordenada_mas_larga(s:list[int]) -> int:
    print("test")
