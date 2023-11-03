"""Programa para calcular sumas de cuadrados"""

def primos(numero):
    """Función que descompone un numero en sus primos"""
    listaPrimos = []

    for i in range(2,(numero//2)+1):
        lista_i = []
        for k in range(1,i):
            if i%k == 0:
                lista_i.append(k)
        if len(lista_i) == 1:
            listaPrimos.append(i)
    #termina máquina de primos
    return listaPrimos


def factorizacionPrimos(numero, listaPrimos, listaFactorizacion):
    """Función para factorizar un número en factores primos"""

    if numero == 1:
        return listaFactorizacion

    for i in listaPrimos:
        if numero % i == 0:
            listaFactorizacion.append(i)
            return factorizacionPrimos(numero // i, listaPrimos, listaFactorizacion)


def congruencia(numero, modulo):
    """"Función congruencia que reduce a un módulo en particular"""
    for i in range(modulo):
        if (numero-i) % modulo == 0:
            return i


def condicionDosCuadrados(listaFactorizacion):
    """Función auxiliar para obtener dos cuadrados (T o F)"""

    for i in listaFactorizacion:
        if congruencia(i,4) == 3:
            a = listaFactorizacion.count(i)
            if a % 2 != 0:
                return False
    return True

def sumaDosCuadrados(numero):
    """Función auxiliar que calcula la suma de dos cuadrados"""

    mitad = numero // 2
    raizEntera = int(mitad ** 0.5) +1
    for i in range(0,raizEntera+1):
        completo = (numero - (i ** 2)) ** 0.5
        if completo % 1 == 0:
            return i, int(completo)


def cuadrados():
    """Función principal"""

    valid_input = False

    while not valid_input:

        numero = input("Escoge tu número: ")

        try:
            numero = int(numero)
            if numero >= 0:
                valid_input = True

        except ValueError:
            print("No es un número válido")

    listaPrimos = primos(numero)
    listaFactorizacion = []

    factorizacionPrimos(numero,listaPrimos, listaFactorizacion)
    if condicionDosCuadrados(listaFactorizacion) is False:
        print(f"{numero} no puede ser representado como suma de dos cuadrados.")
    else:
        (a,b) = sumaDosCuadrados(numero)
        print(f"{numero}={a}^2+{b}^2.")

cuadrados()
