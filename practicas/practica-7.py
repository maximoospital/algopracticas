# Ejercicio 1

def pertenece(s:list[int], e: int) -> bool:
    """
        Dada una lista de enteros s y un entero e, determina si el entero pertenece a la lista.
    """
    return e in s

print("Pertenece 1 a [1,2,3,4,5,6,7,1,2]?", pertenece([1,2,3,4,5,6,7,1,2],1))

def divide_a_todos(s:list[int], e: int) -> bool:
    """
        Dada una lista de enteros s y un entero e, determina si e es divisor de todos los numeros en s
    """
    for num in s:
        if (num % e != 0):
            return False
    return True

print("2 divide a 2,4,8,10,16?", divide_a_todos([2,4,8,10,16],2))

def suma_total(s:list[int]) -> int:
    """
        Dada una lista de enteros s, nos devuelve la suma de todos los numeros en s.
    """
    numBuffer:int = 0
    for num in s:
        numBuffer += num
    return numBuffer

print("Suma total de 1,2,3,4,5?", suma_total([1,2,3,4,5]))

def maximo(s:list[int]) -> int:
    """
        Dada una lista de numeros s, nos da el mayor de ellos.
    """
    numSelect:int = s[0]
    for num in s:
        if (numSelect < num):
            numSelect = num
    return numSelect

print ("Numero maximo de 1,2,3,4,5,2,3,4?", maximo([1,2,3,4,5,2,3,4]))

def minimo(s:list[int]) -> int:
    """
        Dada una lista de numeros s, nos da el menor de ellos.
    """
    numSelect:int = s[0]
    for num in s:
        if (numSelect > num):
            numSelect = num
    return numSelect

print ("Numero minimo de 1,2,3,4,5,2,3,4?", minimo([1,2,3,4,5,2,3,4]))

def ordenados(s:list[int]) -> bool:
    """
        Dada una lista de numeros enteros s, nos dira si estan ordenados.
    """
    i:int = 0
    res:bool = True
    while (i < (len(s)-1)) :
        if (s[i] < s[i+1]):
            i += 1
        else:
            res = False
    return res

print ("Esta ordenada la secuencia 1,2,3,4?", ordenados([1,2,3,4]))

def primerPos(s:list[int], e: int) -> int:
    """
        Dada una lista de numeros enteros s y un numero entero e, nos dara la primera posicion de e en s.
    """
    i:int = 0
    while (i < len(s)):
        if (s[i] != e):
            i += 1
        else:
            break
    return i

print("Funcion ayuda primerPos: Primer posicion de 9 en 8,7,9,5,4,9?", primerPos([8,7,9,5,4,9],9))

def pos_maximo(s:list[int]) -> int:
    """
        Dada una lista de numeros enteros s, nos devolvera la posicion del numero mayor.
    """
    if len(s) == 0:
        return -1
    posSelect:int = 0
    for num in s:
        if (num > s[posSelect]):
            posSelect = primerPos(s, num)
    return posSelect

print ("Posicion maxima en la secuencia 1,2,3,4,6,5,4?", pos_maximo([1,2,3,4,6,5,4]))

def pos_minimo(s:list[int]) -> int:
    """
        Dada una lista de numeros enteros s, nos devolvera la posicion del numero menor.
    """
    if len(s) == 0:
        return -1
    posSelect:int = 0
    for num in s:
        if (num < s[posSelect]):
            posSelect = primerPos(s, num)
    return posSelect

print ("Posicion minima en la secuencia 1,2,3,4,6,0,4?", pos_minimo([1,4,3,4,6,0,4]))

def long_mayorASiete(s:list[str]) -> bool:
    """
        Dada una lista de nombres s, determinara si alguno tiene longitud > 7
    """
    for nombre in s:
        if (len(nombre) > 7):
            return True
    return False

print ("Hay un nombre con mas de siete letras en 'Maximo','Agustin','Guadalupe' y 'Matias?", long_mayorASiete(["Maximo","Agustin","Guadalupe","Matias"]))

def es_palindroma(s:str) -> bool:
    """
        Dada una palabra s, determinara si esta es palindroma.
    """
    if len(s) < 2:
        return True
    i:int = 0
    while (i < len(s)):
        if (s[i].lower() != s[len(s)-1-i].lower()):
            return False
        else:
            i += 1
    return True

print ("Es un palindroma anilina?", es_palindroma("anilina"))

def iguales_consecutivos(s:list[int]) -> bool:
    """
        Dada una secuencia de numeros enteros s, determinara si hay 3 iguales consecutivos.
    """
    i:int = 0
    res:bool = False
    while (i < (len(s)-3)):
        if (s[i] == s[i+1] == s[i+2]):
            res = True
        i += 1
    return res

print ("Hay tres iguales consecutivos en 1,2,3,3,3,4,5?", iguales_consecutivos([1,2,3,3,3,4,5]))

def vocales_distintas(palabra:str) -> bool:
    """
        Dada una palabra, determinara si esta tiene al menos 3 vocales distintas.
    """
    vocales = ['a','e','i','o','u']
    vocalesUsadas = []
    for letra in palabra.lower():
        if(letra in vocales and letra not in vocalesUsadas):
            vocalesUsadas.append(letra)
    return len(vocalesUsadas) >=3

print ("Hay almenos 3 vocales distintas en aeiou?", vocales_distintas("aeiou"))

def pos_secuencia_ordenada_mas_larga(s:list[int]) -> int:
    """
        Dada una secuencia de numeros enteros s, nos dara la posicion de la primer lista ordenada mas larga.
    """
    assert len(s) > 0
    secActual: list[int] = [s[0]]
    posOrigen: int = 0
    for i in range(1, len(s)):
        if (s[i] > s[i-1]):
            secActual.append(s[i])
        else:
            posOrigen = i
            secActual = [s[i]]
    return posOrigen

print("Donde arranca la primer secuencia ordenada mas larga en [1,2,3,4,5,5,5,4,5,6,7,8,9]?", pos_secuencia_ordenada_mas_larga([1,2,3,4,5,5,5,4,5,6,7,8,9]))

def hay_negativos(s:list[int]) -> bool:
    """
        Dada una lista s de numeros enteros, nos dira si hay algun negativo
    """
    assert len(s) > 0
    res: bool = False
    for num in s:
        if num < 0: res = True
    return res

print("Hay negativos en [0, -1, 2, 3, 4]?", hay_negativos([0, -1, 2, 3, 4]))

def todos_los_digitos(s: list[int]) -> list[int]:
    """
        Dada una lista de numeros, nos dara todos los digitos de cada uno.
    """
    res: list[int] = []
    for num in s:
        n: int = num
        if (n < 10):
            res.append(n)
        else:
            while n > 0:
                res.append(n % 10)
                n //= 10
    return res

def cantidad_digitos_impares(s:list[int]) -> int:
    """
        Dada una lista de numeros enteros s, nos dara la cantidad de digitos impares en esta lista.
    """
    assert not hay_negativos(s)
    res: int = 0
    for digito in todos_los_digitos(s):
        if digito % 2 != 0: res += 1
    return res

print ("Cuantos digitos impares hay en [57, 2383, 812, 246]?", cantidad_digitos_impares([57, 2383, 812, 246]))

# Ejercicio 2

def ceros_en_posiciones_pares(s: list[int]):
    """
        Dada una lista de numeros, reemplazara aquellos cuya posicion sea par por 0
    """
    for i in range(len(s)):
        if i % 2 == 0: s[i] = 0

cerosenArray = [0,1,2,3,4,5,6]
ceros_en_posiciones_pares(cerosenArray)
print("Ceros en las posiciones pares de [0,1,2,3,4,5,6]", cerosenArray)

def ceros_en_posiciones_pares_2(s:list[int]) -> list[int]:
    """
        Dada una lista de numeros, nos devolvera una casi igual donde aquellos cuya posicion sea par por 0
    """
    res : list[int] = s
    for i in range(len(res)):
        if i % 2 == 0: res[i] = 0
    return res

cerosenArray2 = [0,1,2,3,4,5,6]
print("Ceros en las posiciones pares de [0,1,2,3,4,5,6]", ceros_en_posiciones_pares_2(cerosenArray2))
