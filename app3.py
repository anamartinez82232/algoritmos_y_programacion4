"""
def permutaciones(lista):

    if len(lista) <= 1:
        return [lista]

    resultado = []

    for i in range(len(lista))

        elemento = lista[i]

        resto = lista[:i] + lista[i+1:]

        for perm in permutaciones(resto):
            resultado.append([elemento] + perm)
        
        return resultado

        #Complejidad n!, permutaciones siempre es n factorial. El peor de todos

        print(permutaciones([1, 3, 7, 1, 3, 7]))
"""
"""
FIBONACCI
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_tail(n, actual=0, siguiente=1)
    if n == 0:
        return actual
    return fibonacci_tail(n-1, siguiente, siguiente + actual)

import time

inicio = time.time()
print(fibonacci(30))
print(time.time() - inicio)
"""

#Suma elementos de una lista con test recursion
def suma_lista(lista, acumulador=0):
    if len(lista) == 0:
        return acumulador
    return suma_lista(lista[1:], lista[0] + acumulador)

def potencia(base, exp)
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

def potencia_tail(base, exp, acumulador=1):
    if exp == 0:
        return acumulador
    return potencia_tail(base, exp -1, base * acumulador)