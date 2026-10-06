import math

# ejercicio 1.1: hola mundo
def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

# ejercicio 1.2: un verso
def imprimir_un_verso():
    print ("\nY ahora un verso...")
    print("What tongueless ghost of sin crept through my curtains?\nSailing on a sea of sweat on a stormy night\nI think he don't got a name but i can't be certain\nAnd in me he starts to confide\n")

imprimir_un_verso()

# ejercicio 1.3: raiz de 2
def raizDe2() -> float:
    return round(2**0.5,2)

print("\nRaiz de 2 con 2 decimales:", str(raizDe2()))

# ejercicio 1.4: factorial de 2
def factorial_de_dos() -> float:
    return 2 * 1

print("\nFactorial de 2:", str(factorial_de_dos()))

# ejercicio 1.5: perimetro
def perimetro() -> float:
    return 2 * math.pi

print("\nPerimetro de un circulo de radio 1:", str(perimetro()))

# ejercicio 2.1: imprimir saludo
def imprimir_saludo(nombre: str) -> str:
    print("\nHola", nombre)

imprimir_saludo("Maxi")

# ejercicio 2.2: raiz cuadrada de
def raiz_cuadrada_de(numero: float) -> float:
    return numero**0.5

print("\nRaiz cuadrada de 16:", str(raiz_cuadrada_de(16)))

# ejerc\nicio 2.3: fahrenheit a celsius
def fahrenheit_a_celsius(temp_far: float) -> float:
    return ((temp_far - 32)*5)/9

print("\n98 F a Celsius:", str(fahrenheit_a_celsius(98)))

# ejercicio 2.4: imprimir dos veces un estribillo
def imprimir_dos_veces(estribillo: str):
    estribillo *= 2
    print(estribillo)

imprimir_dos_veces("\nAll around the world\nGotta spread the word\nTell em what you heard\nThey're gonna make a better day\n")

# ejercicio 2.5: es multiplo de
def es_multiplo_de(n: float, m: float) -> bool:
    return n % m == 0

print("\nEs 3 multiplo de 2?", str(es_multiplo_de(3,2)))

# ejercicio 2.6: es par
def es_par(numero: float):
    return es_multiplo_de(numero, 2)

print("\nEs 8 par?", str(es_par(8)))

# ejercicio 2.7: cantidad de pizzas
# Dado un numero de comensales y un min_cant_de_porciones, cada pizza tiene 8 porciones y necesitamos calcular cuantas pizzas necesitamos para que cada uno de comensales coma min_cant_de_porciones
# comensales*minima cantidad dividido 8?
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> float:
    return (comensales*min_cant_de_porciones)/8

print("\nPara que 3 comensales puedan comer 4 porciones cada uno, necesitamos: " + str(cantidad_de_pizzas(3,4)) + " pizzas.")

# ejercicio 3.1: alguno es 0?
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return (numero1 == 0) or (numero2 == 0)

print("\nEntre 4 y 2, alguno es 0? ", alguno_es_0(4,2))

# ejercicio 3.2: ambos son 0?
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return (numero1 == 0) and (numero2 == 0)

print("\nEntre 0 y 0, ambos son 0? ", ambos_son_0(0,0))

# ejercicio 3.3: es el nombre... largo?
def es_nombre_largo(nombre: str) -> bool:
    return (3 <= len(nombre)) and (len(nombre) <= 8)

print("\nEs el nombre Maximo largo?", es_nombre_largo("Maximo"))

# ejercicio 3.4: es un año bisiesto?
def es_bisiesto(año: int) -> bool:
    return (año % 400 == 0) or ((año % 4 == 0) and not(año % 100 ==0))

print("\nEl 2022 fue bisiesto?", es_bisiesto(2022))

# ejercicio 4: composicion de funciones
# El peso de un pino: hasta 3 metros 3kg*cm, pasados 2kg*cm
# El peso es util si esta entre 400 y 1000kg
# Necesitaremos la funcion peso_pino, que calcule el peso del pino
#               la funcion es_peso_util, que determine si el peso es util
#               la funcion sirve_pino, que determine si el pino es util segun su altura, hecha con composicion de funciones.

def peso_pino(altura: int) -> int:
    peso = 0
    if (altura > 3):
        peso = (2*((altura-3)*100)) + (3*(3*100))
    else:
        peso = (3*(altura*100))
    return peso

print("\nPeso de un pino de 5 metros:", str(peso_pino(5)), "kg")

def es_peso_util(peso: int) -> bool:
    return (400 < peso) and (peso < 1000)

print("Es su peso util?", es_peso_util(peso_pino(5)))

def sirve_pino(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))

print("Por ende, sirve el pino?", sirve_pino(5))

# Ejercicio 5.1: devolver el doble si es par
def devolver_el_doble_si_es_par(numero: float) -> float:
    if(numero % 2 == 0):
        return numero*2
    else:
        return numero

print("\nDevolvera el doble de 18?", devolver_el_doble_si_es_par(18))
print("Y el de 3?", devolver_el_doble_si_es_par(3))

# Ejercicio 5.2: devolver valor si es par si no el que sigue
def devolver_valor_si_es_par_sino_el_que_sigue(numero: float) -> float:
    if(numero % 2 == 0):
        return numero
    else:
        return numero+1

print("\nsi 6 es par, me dara 6?", devolver_valor_si_es_par_sino_el_que_sigue(6))

# Ejercicio 5.3:  devovler el doble si es multiplo 3 el triple si es multiplo 9
# si posta se llama asi la funcion lcdll
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: float):
    if(numero % 9 == 0):
        return numero*3
    elif(numero % 3 == 0):
        return numero*2
    else:
        return numero

print("\nSi 18 es multiplo de 3 o de 9...?", devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))

# Ejercicio 5.4: el nombre es "lindo"?
def lindo_nombre(nombre: str):
    if(len(nombre) >= 5):
        print("Tu nombre tiene una banda de letras")
    else:
        print("Tu nombre tiene menos de 5 caracteres.")

print("\nTu nombre es Maximo?") 
lindo_nombre("Maximo")

# Ejercicio 5.5: elRango
def elRango(numero: float):
    if(numero < 5):
        print("Menor a 5")
    elif((10 < numero) and (numero < 20)):
        print("Entre 10 y 20")
    elif(numero > 20):
        print("Mayor a 20")

print("\n14 donde se encuentra?")
elRango(14)

# Ejercicio 5.6: Dados parametros de sexo y edad, jubilar
def teJubilas(edad: int, sexo: str):
    if(((sexo == "M") and (edad > 65)) or ((sexo == "F") and (edad > 60))):
        print ("Anda de vacaciones viejardo")
    else:
        print ("a laburar che")

print("\nSi soy un viejo de 70?")
teJubilas(70, "M")

print("\nSi soy una vieja de 50?")
teJubilas(50, "F")

# Ejercicio 6.1: numeros del 1 al 10
def del_1_al_10():
    i = 0
    while(i < 10):
        i=i+1
        print(i)

print("\nDel 1 al 10:")
del_1_al_10()

# Ejercicio 6.2: pares entre el 10 y el 40
def pares_entre_10_y_40():
    i = 10
    while(i < 40):
        if(i % 2 == 0):
            print (i)
        i = i + 1

print("\nPares entre 10 y 40:")
pares_entre_10_y_40()

# Ejercicio 6.3: eco 10 veces
def diez_veces_eco():
    i = 0
    while(i < 10):
        print("eco")
        i = i + 1

print("\ndiez veces eco:")
diez_veces_eco()

# Ejercicio 6.4: cuenta regresiva desde ingresado hasta el 1, dsp despegue
def cuenta_regresiva(numero: int):
    while(numero > 0):
        print(numero)
        numero = numero - 1
    print("Despegue")

print("Arrancamos cuenta regresiva desde el 12:")
cuenta_regresiva(12)

# Ejercicio 7: 6 pero con for num in range.
def del_1_al_10_alt():
    i = 1
    for i in range(1, 11, 1):
        print (i)


print("\nDel 1 al 10 (alt):")
del_1_al_10_alt()

def pares_entre_10_y_40_alt():
    i = 10
    for i in range(10,42,2):
        print (i)

print("\nPares entre 10 y 40 (alt):")
pares_entre_10_y_40_alt()

def diez_veces_eco_alt():
    i = 0
    for i in range(0,10,1):
        print("eco")

print("\ndiez veces eco (alt):")
diez_veces_eco_alt()

def cuenta_regresiva_alt(numero: int):
    i = numero
    for i in range(0,numero,1):
        print(numero - i)
    print("Despegue")

print("\nArrancamos cuenta regresiva desde el 12 (alt):")
cuenta_regresiva_alt(12)

# Ejercicio 8 y 9: no
