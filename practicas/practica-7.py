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
            i += 1
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


def sin_vocales(s: str) -> str:
    """
        Dada una cadena de caracteres s, devuelve una igual pero sin las vocales.
    """
    res: str = ""
    vocales: list[str] = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    letras: list[str] = list(s)
    for letra in letras:
        if letra not in vocales: res += letra
    return res

print("Testeando sin vocales:",sin_vocales("Testeando"))

def reemplaza_vocales(s: str) -> str:
    """
        Dada una cadena de caracteres s, devuelve una igual pero con guiones bajos en el lugar de vocales.
    """
    res: str = ""
    vocales: list[str] = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    letras: list[str] = list(s)
    for letra in letras:
        if letra not in vocales: res += letra
        else: res += "_"
    return res

print("Testeando reemplazando vocales:", reemplaza_vocales('Testeando'))

def da_vuelta_str(s: str) -> str:
    """
        Dada una cadena de caracteres s, devuelve una cadena inversa de esta.
    """
    res: str = ""
    letras: list[str] = list(s)
    for i in range(len(letras)):
        res += letras[len(letras) - i - 1]
    return res

print("Dando vuelta Hola:", da_vuelta_str("Hola"))

def eliminar_repetidos(s:str) -> str:
    """
        Dada una cadena de caracteres s, la devuelve sin repetidos.
    """
    res: str = ""
    letras: list[str] = list(s)
    letras_sin_repetir: list[str] = []
    for letra in letras:
        if letra not in letras_sin_repetir: letras_sin_repetir.append(letra)
    for letra in letras_sin_repetir:
        res += letra
    return res

print("Probandolo sin letras repetidas:", eliminar_repetidos("Probandolo"))

# Ejercicio 3

def resultado_materia(notas: list[int]) -> int:
    """
        Dado un listado de enteros notas, nos dara el estado de aprobacion de la materia.
    """
    res: int = 0
    promedio: int = 0
    apruebaParciales: bool = True
    for nota in notas:
        if nota < 4: apruebaParciales = False
        promedio += nota
    promedio /= len(notas)
    if apruebaParciales and promedio >= 7: res = 1
    elif apruebaParciales and promedio >= 4: res = 2
    else: res = 3
    return res

def resultado_en_palabras(resmateria: int):
    res: str = ""
    if resmateria == 3: res = "Desaprobado."
    elif resmateria == 2: res = "Aprobado."
    elif resmateria == 1: res = "Promocionado."
    return res

print("Estado de materia de un alumno con [10,8,6]?", resultado_en_palabras(resultado_materia([4, 4, 4])))

# Ejercicio 4

def saldo_Actual(movimientos:list[ tuple[str, int]]) -> int:
    """
        Dada una lista de tuplas, devolver el balance actual.
        Saldo inicial 0, string I es ingreso, R es retiro
    """
    res: int = 0
    for movimiento in movimientos:
        if movimiento[0] == "I": res += movimiento[1]
        elif movimiento[0] == "R": res -= movimiento[1]
    return res

print("Saldo actual del ejemplo:", saldo_Actual([("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]))

# Ejercitacion 3: Matrices

# Ej 5

def pertenece_a_cada_uno_version_1(s:list[list[int]], e: int, res: list[bool]):
    """
        Para la lista de listas de enteros s, verificaremos si e pertenece a cada uno de ellos.
    """
    for lista in s:
        res.append(pertenece(lista, e))
    return res

print("Esta 2 en [2,3,4], [1,4,5], [2]? Nuestro resultado incluye un false", pertenece_a_cada_uno_version_1([[2,3,4], [1,4,5], [2]], 2, [False]))

def pertenece_a_cada_uno_version_2(s:list[list[int]], e: int, res: list[bool]):
    """
        Para la lista de listas de enteros s, verificaremos si e pertenece a cada uno de ellos.
    """
    res.clear()
    for lista in s:
        res.append(pertenece(lista, e))
    return res

print("Esta 2 en [2,3,4], [1,4,5], [2]? Nuestro resultado incluye un false pero lo vamos a limpiar.", pertenece_a_cada_uno_version_2([[2,3,4], [1,4,5], [2]], 2, [True]))

def pertenece_a_cada_uno_version_3(s:list[list[int]], e: int) -> list[bool]:
    """
        Para la lista de listas de enteros s, verificaremos si e pertenece a cada uno de ellos.
    """
    res: list[bool] = []
    for lista in s:
        res.append(pertenece(lista, e))
    return res

print("Esta 2 en [2,3,4], [1,4,5], [2]? No tenemos un resultado pre hecho", pertenece_a_cada_uno_version_3([[2,3,4], [1,4,5], [2]], 2))

# Como cambia? Cambia que en la primer version recibe una variable ya hecha donde guardara su info, y esta tiene que ser de mayor o igual longitud a la de las listas ingresadas.
#                         en la segunda version recibe una variable ya hecha donde guardara su info, y debera limpiarla para que sea de IGUAL longitud a la de las listas ingresadas,
#                       y en la tercera version no recibe una variable, la crea dentro y devuelve el valor.
# Se puede usar la implementacion del segundo ejercicio en el primero ya que cumple la parte de igual, mientras que al reves no porque no se cumple la parte de mayor o igual.

# Ej 6

def es_matriz(s: list[list]) -> bool:
    tieneFilas: bool = len(s) > 0
    lasFilasTienenColumnas: bool = False
    lasFilasSonIguales: bool = True
    if tieneFilas: lasFilasTienenColumnas = len(s[0]) > 0
    if lasFilasTienenColumnas:
        for fila in s:
            if len(fila) != len(s[0]): lasFilasSonIguales = False
    return tieneFilas and lasFilasTienenColumnas and lasFilasSonIguales

print("Es matriz [[0, 0, 0], [0, 0, 0], [0, 0, 0]]?", es_matriz([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print("y [[0,0], [0,0,0]]", es_matriz([[0,0], [0,0,0]]))

resTestFO = []
def filas_ordenadas(m: list[list[int]], res: list[bool]):
    assert es_matriz(m)
    for fila in m:
        res.append(ordenados(fila))

filas_ordenadas([[0, 1, 2, 3], [0, 1, 4, 3]], resTestFO)

print("Estan ordenados [[0, 1, 2, 3], [0, 1, 5, 3]]?", resTestFO)

def columna(m: list[list[int]], c: int) -> list[int]:
    assert es_matriz(m) and c < len(m[0]) and c >= 0
    res: list[int] = []
    for fila in m:
        res.append(fila[c])
    return res

print("Columna 2 de [[0, 1, 2], [3, 4, 5]]?", columna([[0, 1, 2], [3, 4, 5]], 2))

def columnas_ordenadas (m: list[list[int]]) -> list[bool]:
    assert es_matriz(m)
    res : list[bool] = []
    for numColumna in range(len(m[0])):
        res.append( ordenados( columna(m, numColumna) ) )
    assert len(res) == len(m[0])
    return res

print("Estan ordenadas las columnas de [[0, 1, 2, 3], [1, 0, 3, 5], [2, 0, 3, 6]]", columnas_ordenadas([[1, 2, 3, 4], [1, 0, 3, 5], [2, 0, 3, 6]]))


def transponer (m: list[list]) -> list[list]:
    assert es_matriz(m)
    res : list[list] = []
    for numColumna in range(len(m[0])):
        res.append ( columna(m, numColumna) )
    return res

print("Trasposicion de [[1, 2], [3, 4], [5, 6]]", transponer([[1, 2], [3, 4], [5, 6]]))

def tateti_valido (m: list[list[str]]) -> bool:
    assert es_matriz(m) and len(m) == 3 and len(m[0]) == 3
    valores_de_tateti: list[str] = ['O', 'X', ' ']
    res: bool = True
    for fila in m:
        for columna in fila:
            if columna not in valores_de_tateti: res = False
    return res

def quien_gana_tateti (m: list[list[str]]) -> int:
    assert tateti_valido(m)
    filas: list[list[str]] = m
    columnas: list[list[str]] = transponer(m)
    ganador: int = 2
    hay3XAlineadasVertical: bool = False
    hay3OAlineadasVertical: bool = False
    hay3XAlineadasHorizontal: bool = False
    hay3OAlineadasHorizontal: bool = False
    hay3XAlineadasDiagonal: bool = False
    hay3OAlineadasDiagonal: bool = False
    for fila in filas:
        if (fila[0] == fila[1] == fila[2]):
            if fila[0] == 'X': hay3XAlineadasHorizontal = True
            elif fila[0] == 'O': hay3OAlineadasHorizontal = True
    for columna in columnas:
        if (columna[0] == columna[1] == columna[2]):
            if columna[0] == 'X': hay3XAlineadasVertical = True
            elif columna[0] == 'O': hay3OAlineadasVertical = True
    if (m[0][0] == m[1][1] == m[2][2]) or (m[0][2] == m[1][1] == m[2][0]):
        if m[1][1] == 'X': hay3XAlineadasDiagonal = True
        elif m[1][1] == 'O': hay3OAlineadasDiagonal = True
    if hay3XAlineadasVertical: assert not hay3OAlineadasVertical
    elif hay3OAlineadasVertical: assert not hay3XAlineadasVertical
    elif hay3XAlineadasHorizontal: assert not hay3OAlineadasHorizontal
    elif hay3OAlineadasHorizontal: assert not hay3XAlineadasHorizontal
    if hay3OAlineadasVertical or hay3OAlineadasHorizontal or hay3OAlineadasDiagonal: ganador = 0
    elif hay3XAlineadasVertical or hay3XAlineadasHorizontal or hay3XAlineadasDiagonal: ganador = 1
    return ganador

print("Quien gano en [[' ', ' ', 'X'], [' ','X',' '], ['X',' ',' ']]", quien_gana_tateti([[' ', ' ', 'X'], [' ','X',' '], ['X',' ',' ']]))

def tomar_nombres() -> list[str]:
    res: list[str] = []
    texto: str = input("Ingresa un nombre. 'listo' o nada detiene esto: \n")

    while texto.lower() not in ["", " ", "listo"]:
        res.append(texto)
        texto = input("Ingresa otro nombre. 'listo' o nada detiene esto: \n")

    return res

# print("Nombres ingresados:", tomar_nombres())

def historial_monedero() -> list[ tuple[str, int] ]:
    res: list[tuple[str, int]] = []
    carga: int = 0
    tipoActual: str = input("\nHISTORIAL DE MONEDERO \nCarga Actual: 0 \n Ingresa tipo de operacion. \n C para cargar creditos \n D para descontar creditos \n X para salir. \n")
    montoActual: int = 0

    while tipoActual.upper() in ['C', 'D']:
        montoActual = int(input("Ingresa monto de operacion.\n"))
        if tipoActual.upper() == 'C': carga += montoActual
        elif tipoActual.upper() == 'D': carga -= montoActual
        res.append((tipoActual, montoActual))
        print("\nOperacion registrada.\nCarga Actual:",carga)
        tipoActual = input(" Ingresa tipo de operacion. \n C para cargar creditos \n D para descontar creditos \n X para salir. \n")

    return res

# print("Operaciones registradas:", historial_monedero())

import numpy as np
from numpy._core.fromnumeric import resize

def puntaje_sem(puntaje: float, carta: int) -> float:
    if carta in [10, 11, 12]: puntaje += 0.5
    else: puntaje += 1
    return puntaje

def siete_y_medio():
    puntaje: float = 0
    cartaActual: int = np.random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
    cartasSacadas: int = 1
    puntaje = puntaje_sem(puntaje, cartaActual)
    print("Hola! Tu primer carta fue:", cartaActual, "\npor ende tu puntaje inicial es:", puntaje)
    accion: str = input("Que haces?\n - Sacar otra carta\n - Plantarse.\n")
    while puntaje < 7.5 and accion.lower() in ["saco", "sacamos", "1", "saca", "sacar", "sacar carta", "sacar una carta", "sacar otra carta", "y saco", "sacame", "saca otra", "saco otra", "saquemos otra", "saquemos otra maestro"]:
        cartaActual = np.random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        cartasSacadas += 1
        puntaje = puntaje_sem(puntaje, cartaActual)
        if (puntaje >= 7.5):
            print("PERDISTE PISCUI!!!\n Tu puntaje final es:", puntaje, "\nLograste eso en:", cartasSacadas, "cartas.")
            break
        print("Sacaste la carta:", cartaActual, "\npor ende tu puntaje ahora es:", puntaje)
        print("Vas:", cartasSacadas, "cartas sacadas.")
        accion = input("Que haces?\n - Sacar otra carta\n - Plantarse.\n")
    if puntaje < 7.5: print("Chau!\n Tu puntaje final es:", puntaje, "\nLograste eso en:", cartasSacadas, "cartas.")

# siete_y_medio()

def analizar_pass(password: str) -> str:
    res: str = "ROJA"
    caracteres: list[str] = list(password)
    cantidadMayusculas: int = 0
    cantidadMinusculas: int = 0
    cantidadNumeros: int = 0
    for caracter in caracteres:
        if caracter in ['0','1','2','3','4','5','6','7','8','9']: cantidadNumeros += 1
        elif "A" <= caracter <= "Z": cantidadMayusculas += 1
        elif "a" <= caracter <= "z": cantidadMinusculas += 1
    if len(password) > 5:
        res = "AMARILLA"
        if cantidadNumeros >= 1 and cantidadMinusculas >= 1 and cantidadMayusculas >= 1: res = "VERDE"
    return res

def analisis_fortaleza():
    password: str = input("Ingrese aqui su contraseña para analizarla: ")
    return analizar_pass(password)

print("Su contraseña es:", analisis_fortaleza())
