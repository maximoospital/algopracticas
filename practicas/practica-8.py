import numpy as np
from queue import LifoQueue as Pila
from queue import Queue as Cola

# ej 1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    assert cantidad > 0 and desde <=hasta
    res: Pila[int] = Pila()
    longitudPila: int = 0
    while longitudPila <= cantidad - 1:
        res.put(np.random.randint(desde, hasta))
        longitudPila += 1
    return res

def imprimir_pila(pila: Pila):
    res: list = []
    while not pila.empty():
        res.append(pila.get())
    return res

print("10 Numeros al azar entre 900 y 1000?", imprimir_pila(generar_nros_al_azar(10, 900, 1000)))

# ej 2
