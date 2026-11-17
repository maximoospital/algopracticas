import numpy as np
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

# func aux
def copiar_pila(pila: Pila) -> Pila:
    pOriginal: Pila = pila
    pCopia: Pila = Pila()
    pContenido: list = []
    while not pOriginal.empty():
        pContenido.append(pOriginal.get())
    for i in range(len(pContenido)):
        pOriginal.put(pContenido[len(pContenido)-i-1])    
        pCopia.put(pContenido[len(pContenido)-i-1])
    return pCopia 

def pila_a_lista(pila: Pila) -> list:
    pCopia: Pila = copiar_pila(pila)
    pContenido: list = []
    while not pCopia.empty():
        pContenido.append(pCopia.get())
    return pContenido

def lista_a_pila(lista: list) -> Pila:
    pila: Pila = Pila()
    for item in lista:
        pila.put(item)
    return lista

# ej 1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    assert cantidad > 0 and desde <=hasta
    res: Pila[int] = Pila()
    longitudPila: int = 0
    while longitudPila <= cantidad - 1:
        res.put(random.randint(desde, hasta))
        longitudPila += 1
    return res

print("10 Numeros al azar entre 900 y 1000?", pila_a_lista(generar_nros_al_azar(10, 900, 1000)))

# ej 2

pila1 = generar_nros_al_azar(3, 4, 9)
pila2 = copiar_pila(pila1)

print("Pila original:", pila_a_lista(pila1), "\nPila copia:", pila_a_lista(pila2), "\nPila original post-copiarla:", pila_a_lista(pila1))

def cantidad_elementos(p: Pila) -> int:
    pCopia: Pila = copiar_pila(p)
    res: int = 0
    while not pCopia.empty():
        pCopia.get()
        res += 1
    return res

print("Cantidad de elementos en la pila", pila_a_lista(pila1), "=", cantidad_elementos(pila1))

# ej 3
def buscar_el_maximo(p: Pila[int]) -> int:
    assert not p.empty()
    pElementos: list[int] = pila_a_lista(p)
    res: int = 0
    for num in pElementos:
        if num > res: res = num
    return res

print("Numero maximo en ", pila_a_lista(pila1), "=", buscar_el_maximo(pila1))

# ej 4
def generar_notas () -> Pila[tuple[str, int]]:
    res: Pila = Pila()
    materias: list[str] = ['Algebra', 'Analisis', 'Sociedad y Estado', 'Programacion']
    notas: list[int] = list(range(1, 11))
    for i in range(len(materias)):
        nota: int = random.choice(notas)
        materia : str = materias[random.randint(0, 3)]
        res.put((materia, nota))
    return res

def buscar_nota_maxima (p: Pila[tuple[str, int]]) -> tuple[str, int]:
    assert not p.empty()
    notas: list = pila_a_lista(p)
    res : tuple[str, int] = notas[0]
    for nota in notas:
        if nota[1] > res[1]: res = nota
    return res

notas : Pila = generar_notas()
print("Nota maxima en", pila_a_lista(notas),"=", buscar_nota_maxima(notas))

# ej 5

def esta_bien_balanceada (s: str) -> bool:
    p: Pila = Pila()
    for caracter in s:
        if caracter == '(': p.put(caracter)
        elif caracter == ')':
            if not p.empty(): p.get()
            else: p.put(caracter)
    return p.empty()

print("La formula 1 + ) 2 * 3 ( () esta balanceada?", esta_bien_balanceada("1 + ) 2 * 3 ( ()"))

# ej 6


def evaluar_expresiones(s: str) -> float:
    pilaOperandos: Pila = Pila()
    operadores: list[str] = ["+", "-", "*", "/"]
    tokens: list[str] = []

    # Dividimos la expresion en tokens
    for caracter in s: 
        if caracter != " ":
            tokens.append(caracter)

    for caracter in tokens:       
        if caracter not in operadores: 
            # Si es un operando, lo agregamos a una pila.
            pilaOperandos.put(float(caracter))
            print("Pila actualmente:", pila_a_lista(pilaOperandos))
        else: 
            resOperacion: float = 0
            operando2: float = pilaOperandos.get()
            operando1: float = pilaOperandos.get()
            if caracter == "+": resOperacion = operando1 + operando2
            elif caracter == "-": resOperacion = operando1 - operando2
            elif caracter == "/": resOperacion = operando1 / operando2
            else: resOperacion = operando1 * operando2
            pilaOperandos.put(resOperacion)
    return pilaOperandos.get()

# print( "Evaluando la expresion 3 4 + 5 * 2 -:", evaluar_expresiones("3 4 + 5 * 2 -") )


# ej 7 

def dar_vuelta_pila(p: Pila) -> Pila:
    pOriginal: Pila = p
    pCopia: Pila = Pila()
    pContenido: list = []
    while not pOriginal.empty():
        pContenido.append(pOriginal.get())
    for i in range(len(pContenido)):
        pOriginal.put(pContenido[len(pContenido)-i-1])    
        pCopia.put(pContenido[i])
    return pCopia 


def intercalar(p1: Pila, p2: Pila) -> Pila:
    assert(cantidad_elementos(p1) == cantidad_elementos(p2))
    pila1: Pila = copiar_pila(p1)
    pila2: Pila = copiar_pila(p2)
    p: Pila = Pila()
    while not (pila1.empty() and pila2.empty()):
        p.put(pila2.get())
        p.put(pila1.get())
    return dar_vuelta_pila(p)

pila4: Pila = generar_nros_al_azar(3, 6, 10)
pila5: Pila = generar_nros_al_azar(3, 12, 30)
print("Intercalando", pila_a_lista(pila4), "y", pila_a_lista(pila5), ":", pila_a_lista(intercalar(pila4, pila5)))

# Colas
# ej 8


def cola_a_lista(c: Cola) -> list:
    cElementos: list = []
    while not c.empty(): cElementos.append(c.get())
    for elemento in cElementos: c.put(elemento)
    return cElementos    

def copiar_cola(c: Cola) -> Cola:
    assert not c.empty()
    cCopia: Cola = Cola()
    cElementos: list = cola_a_lista(c)
    for elemento in cElementos:
        cCopia.put(elemento)
    return cCopia

def generar_nros_al_azar_colas(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    assert cantidad >= 0 and desde <= hasta
    res: Cola[int] = Cola()
    for i in range(cantidad):
        res.put(random.randint(desde, hasta))
    assert len(cola_a_lista(res)) == cantidad
    return res

print("Generame 5 numeros al azar entre 8 y 20, en cola:", cola_a_lista(generar_nros_al_azar_colas(5, 8, 20)))

# Colas es lo mismo que pilas, solamente al reves lol. Salteo directo a diccionarios

# ej 16 

def calcular_promedio_por_estudiante(notas: list[tuple[str, int]]) -> dict[str, int]:
    res: dict[str, int] = {}
    nombres: list[str] = []
    for nota in notas:
        if nota[0] not in nombres: nombres.append(nota[0])
    for nombre in nombres:
        promedio: int = 0
        notasPersona: list[int] = []
        for nota in notas: 
            if nota[0] == nombre: notasPersona.append(nota[1])
        for n in notasPersona:
            promedio += n
        promedio /= len(notasPersona)
        res[nombre] = promedio
    return res

print("Promedio de [(Maxi, 10), (Maxi, 8), (Luffy, 4), (Luffy, 8)]:", calcular_promedio_por_estudiante([("Maxi", 10), ("Maxi", 8), ("Luffy", 4), ("Luffy", 8)]))