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
    listaPrimos.append(numero)
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
    raizEntera = int(mitad ** 0.5) + 1
    for i in range(0,raizEntera+1):
        completo = (numero - (i ** 2)) ** 0.5
        if completo % 1 == 0:
            return i, int(completo)

def sumaTresCuadrados(numero,listaPrimos):
    """Función auxiliar que calcula la suma de tres cuadrados"""
    tercia = numero // 3
    raizEntera = int(tercia ** 0.5) + 1
    for i in range(0,raizEntera+1):
        nuevoNum = numero - (i ** 2)
        listaFactorizacion = []
        listaPrimos.append(nuevoNum)
        factorizacionPrimos(nuevoNum,listaPrimos, listaFactorizacion)
        if condicionDosCuadrados(listaFactorizacion) is True:
            (d,e) = sumaDosCuadrados(nuevoNum)
            return i, d, e
    return None, None, None

def sumaCuatroCuadrados(numero,listaPrimos):
    """Función auxiliar que calcula la suma de cuatro cuadrados"""
    cuarta = numero // 4
    raizEntera = int(cuarta ** 0.5) + 1
    for i in range(0,raizEntera+1):
        nuevoNum = numero - (i ** 2)
        (g,h,j) = sumaTresCuadrados(nuevoNum,listaPrimos)
        if (g,h,j) != (None, None, None):
            return i, g, h, j

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

        listaPrimosrep = listaPrimos[:]

        if sumaTresCuadrados(numero,listaPrimosrep) == (None, None, None):
            print(f"{numero} no puede ser representado como suma de tres cuadrados.")
            (f,g,h,i) = sumaCuatroCuadrados(numero,listaPrimos)
            print(f"{numero}={f}^2+{g}^2+{h}^2+{i}^2.") #4 cuadrados

        else:
            (c,d,e) = sumaTresCuadrados(numero,listaPrimos)
            print(f"{numero}={c}^2+{d}^2+{e}^2.") #3 cuadrados
            print(f"{numero}={c}^2+{d}^2+{e}^2+0^2.") #4 cuadrados
    else:
        (a,b) = sumaDosCuadrados(numero)
        print(f"{numero}={a}^2+{b}^2.") #2 cuadrados
        print(f"{numero}={a}^2+{b}^2+0^2.") #3 cuadrados
        print(f"{numero}={a}^2+{b}^2+0^2+0^2.") #4 cuadrados

cuadrados()
