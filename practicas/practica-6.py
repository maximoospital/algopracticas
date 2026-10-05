import math

def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

def imprimir_un_verso():
    print ("\nY ahora un verso...")
    print("What tongueless ghost of sin crept through my curtains?\nSailing on a sea of sweat on a stormy night\nI think he don't got a name but i can't be certain\nAnd in me he starts to confide\n")

imprimir_un_verso()

def raizDe2():
    return round(2**0.5,2)

print("\nRaiz de 2 con 2 decimales:", str(raizDe2()))

def factorial_de_dos():
    return 2 * 1

print("\nFactorial de 2:", str(factorial_de_dos()))

def perimetro():
    return 2 * math.pi

print("\nPerimetro de un circulo de radio 1:", str(perimetro()))

def imprimir_saludo(nombre: str):
    print("\nHola", nombre)

imprimir_saludo("Maxi")

def raiz_cuadrada_de(numero: float):
    return round(numero**0.5)

print("\nRaiz cuadrada de 16:", str(raiz_cuadrada_de(16)))
