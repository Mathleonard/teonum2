###########################################################################
def productoprimos(listaprimos,n):

    for p in range(len(listaprimos)):
        for q in range(p+1, len(listaprimos)):
            if listaprimos[p] * listaprimos[q] == n:
                return listaprimos[p],listaprimos[q]
    #Si n no es un número que sea producto de dos primos,
    # sino es un primo o es producto de más de dos primos,
    # que no regrese nada la función (preventivo).
    return 0, 0
###########################################################################

###########################################################################
def primos(n):
    #inicia máquina de primos
    listaprimos = []

    for i in range(2,(n//2)+1):
        lista_i = []
        for k in range(1,i):
            if i%k == 0:
                lista_i.append(k)
        if len(lista_i) == 1:
            listaprimos.append(i)
    #termina máquina de primos
    p,q = productoprimos(listaprimos,n)
    return p,q
###########################################################################

###########################################################################
#La función 'algoritmo_div()' regresará el mcd de 2 números.
def algoritmo_div(n, a):
    #El uso de '%' es para obtener el residuo del cociente: el módulo
    residuo_ad = n%a

    #La función 'if' empieza como un 'si (condición)'
    #'!=' significa 'no es igual a'
    if residuo_ad != 0:
        return algoritmo_div(a,residuo_ad)

    #'else' es el último caso del condicional, y se usa cuando no se cumple
    # el 'if'
    else:
        s = abs(a)
        #'return <>' regresa el valor a donde fue llamada la función
        return s
###########################################################################

###########################################################################
#Es el Algortimo Extendido de Euclides
def euclides(a, b):
    if b == 0:
        return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        #Modificar a,b
        a = b
        b = r
        #Modificaciones para la siguiente iteración
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    return  u0
###########################################################################

###########################################################################
#Definición de la función phi
def phi(m):
    #Definimos la lista para los primos relativos
    listaPrimosRelativos = []
    #La iteración empezará a partir de 1
    iteracion_numero = 1
    #Todos los números menores o iguales a n cumplirán una función
    while iteracion_numero <= m:
        mcd = algoritmo_div(m,iteracion_numero)
        if mcd == 1:
            listaPrimosRelativos.append(iteracion_numero)
        #Una vez evaluado, pasamos al siguiente número (Le añadimos uno a
        # la variable)    
        iteracion_numero += 1
    return listaPrimosRelativos
###########################################################################

###########################################################################
def dicts():
    encriptar = {"A": 11,
              "Á": 11,
              "a": 11,
              "á": 11,
              "B": 12,
              "b": 12,
              "C": 13,
              "c": 13,
              "D": 14,
              "d": 14,
              "E": 15,
              "É": 15,
              "e": 15,
              "é": 15,
              "F": 16,
              "f": 16,
              "G": 17,
              "g": 17,
              "H": 18,
              "h": 18,
              "I": 19,
              "Í": 19,
              "i": 19,
              "í": 19,
              "J": 20,
              "j": 20,
              "K": 21,
              "k": 21,
              "L": 22,
              "l": 22,
              "M": 23,
              "m": 23,
              "N": 24,
              "n": 24,
              "Ñ": 24,
              "ñ": 24,
              "O": 25,
              "Ó": 25,
              "o": 25,
              "ó": 25,
              "P": 26,
              "p": 26,
              "Q": 27,
              "q": 27,
              "R": 28,
              "r": 28,
              "S": 29,
              "s": 29,
              "T": 30,
              "t": 30,
              "U": 31,
              "Ú": 31,
              "u": 31,
              "ú": 31,
              "V": 32,
              "v": 32,
              "W": 33,
              "w": 33,
              "X": 34,
              "x": 34,
              "Y": 35,
              "y": 35,
              "Z": 36,
              "z": 36,
              " ": 99
              }

    desencriptar = {11: "A",
              12: "B",
              13: "C",
              14: "D",
              15: "E",
              16: "F",
              17: "G",
              18: "H",
              19: "I",
              20: "J",
              21: "K",
              22: "L",
              23: "M",
              24: "N",
              25: "O",
              26: "P",
              27: "Q",
              28: "R",
              29: "S",
              30: "T",
              31: "U",
              32: "V",
              33: "W",
              34: "X",
              35: "Y",
              36: "Z",
              99: " "}
    return encriptar, desencriptar
###########################################################################

###########################################################################
def congruencia(a, m):
    for i in range(m):
        if (a-i)%m == 0:
            return i
###########################################################################

###########################################################################
def encriptado_clave(texto_1,n,e):

    texto_cifrado = []

    encriptar = dicts()[0]

    for char in texto_1:
        if char in encriptar:
            texto_cifrado.append(encriptar[char])
        else:
            texto_cifrado.append(char)

    for i, char in enumerate(texto_cifrado):
        # Si el caracter es un entero, se le aplica la regla
        if isinstance(char, int):
            texto_cifrado[i] = texto_cifrado[i]**e
            texto_cifrado[i] = congruencia(texto_cifrado[i], n)

    print(texto_cifrado)
###########################################################################

###########################################################################
def desencriptado_clave(texto_2,n,d):

    texto_cifrado = texto_2.split(" ")
    texto_descifrado = []
    desencriptar = dicts()[1]

    for char in texto_cifrado:
        inv = int(char) ** d
        inv = congruencia(inv, n)
        if inv in desencriptar:
            texto_descifrado.append(desencriptar[inv])
        else:
            texto_descifrado.append(char)

    print(''.join(texto_descifrado))
###########################################################################

def elegir():
    #Asigna una variable como falsa inicialmente
    valid_input = False

    #Mientras no se cumpla la variable, ejecuta el programa
    while not valid_input:

        #Escoge un entero para decidir qué debe hacer el programa
        x = int(input("Escoge (0) si quieres encriptar o (1) si quieres desencriptar: "))

        #Condición 1)
        if x == 1 or x == 0:
            #Asigna el valor como verdadero, y se sale del ciclo
            valid_input = True
    if x == 0:
        n = int(input("Escribe la primera entrada de tu clave pública: "))
        e = int(input("Escribe la segunda entrada de tu clave pública: "))
        texto_1 = input("Ingresa el texto que quieres encriptar: ")
        p,q = primos(n)
        phi_n = (p-1) * (q-1)
        if e < phi_n:
            mcd = algoritmo_div(phi_n,e)
        elif phi_n < e:
            mcd = algoritmo_div(e,phi_n)
        if mcd == 1:
            encriptado_clave(texto_1,n,e)
        else:
            print(f"No elegiste un primo relativo a {phi_n}.")


    elif x == 1:
        #Para desencriptar, necesita escribir el texto
        n = int(input("Escribe la primera entrada de tu clave pública: "))
        e = int(input("Escribe la segunda entrada de tu clave pública: "))
        texto_2 = input("Ingreso el texto que quieres desencriptar: ")
        p,q = primos(n)
        phi_n = (p-1) * (q-1)
        if e < phi_n:
            mcd = algoritmo_div(phi_n,e)
        elif phi_n < e:
            mcd = algoritmo_div(e,phi_n)
        if mcd == 1:
            x0 = euclides(e, phi_n)
            d = x0%phi_n
            desencriptado_clave(texto_2,n,d)
            #Aquí hace el desencriptado
        else:
            print(f"No elegiste un primo relativo a {phi_n}.")
        
elegir()