"""Programa para Encriptar/Desencriptar por el método Decimado"""

def diccionarios():
    """Se definen los diccionarios para el programa (encriptar y desencriptar)"""
    #Diccionario para encriptar al inicio
    encriptar_ida = {"A": 0, "Á": 0, "a": 0, "á": 0,
                    "B": 1, "b": 1,
                    "C": 2, "c": 2,
                    "D": 3, "d": 3,
                    "E": 4, "É": 4, "e": 4, "é": 4,
                    "F": 5, "f": 5,
                    "G": 6, "g": 6,
                    "H": 7, "h": 7,
                    "I": 8, "Í": 8, "i": 8,"í": 8,
                    "J": 9, "j": 9,
                    "K": 10, "k": 10,
                    "L": 11, "l": 11,
                    "M": 12, "m": 12,
                    "N": 13, "n": 13, "Ñ": 13, "ñ": 13,
                    "O": 14, "Ó": 14, "o": 14, "ó": 14,
                    "P": 15, "p": 15,
                    "Q": 16, "q": 16,
                    "R": 17, "r": 17,
                    "S": 18, "s": 18,
                    "T": 19, "t": 19,
                    "U": 20, "Ú": 20, "u": 20, "ú": 20,
                    "V": 21, "v": 21,
                    "W": 22, "w": 22,
                    "X": 23, "x": 23,
                    "Y": 24, "y": 24,
                    "Z": 25, "z": 25}
    #Diccionario para encriptar al final
    encriptar_regreso = {0: "A",
                        1: "B",
                        2: "C",
                        3: "D",
                        4: "E",
                        5: "F",
                        6: "G",
                        7: "H",
                        8: "I",
                        9: "J",
                        10: "K",
                        11: "L",
                        12: "M",
                        13: "N",
                        14: "O",
                        15: "P",
                        16: "Q",
                        17: "R",
                        18: "S",
                        19: "T",
                        20: "U",
                        21: "V",
                        22: "W",
                        23: "X",
                        24: "Y",
                        25: "Z"}
    #Diccionario para desencriptar al inicio
    desencriptar_ida = {"A": 0, "a": 0,
                    "B": 1, "b": 1,
                    "C": 2, "c": 2,
                    "D": 3, "d": 3,
                    "E": 4, "e": 4,
                    "F": 5, "f": 5,
                    "G": 6, "g": 6,
                    "H": 7, "h": 7,
                    "I": 8, "i": 8,
                    "J": 9, "j": 9,
                    "K": 10, "k": 10,
                    "L": 11, "l": 11,
                    "M": 12, "m": 12,
                    "N": 13, "n": 13,
                    "O": 14, "o": 14,
                    "P": 15, "p": 15,
                    "Q": 16, "q": 16,
                    "R": 17, "r": 17,
                    "S": 18, "s": 18,
                    "T": 19, "t": 19,
                    "U": 20, "u": 20,
                    "V": 21, "v": 21,
                    "W": 22, "w": 22,
                    "X": 23, "x": 23,
                    "Y": 24, "y": 24,
                    "Z": 25, "z": 25}
    #Diccionario para desencriptar al final
    desencriptar_regreso = {0: "A",
                            1: "B",
                            2: "C",
                            3: "D",
                            4: "E",
                            5: "F",
                            6: "G",
                            7: "H",
                            8: "I",
                            9: "J",
                            10: "K",
                            11: "L",
                            12: "M",
                            13: "N",
                            14: "O",
                            15: "P",
                            16: "Q",
                            17: "R",
                            18: "S",
                            19: "T",
                            20: "U",
                            21: "V",
                            22: "W",
                            23: "X",
                            24: "Y",
                            25: "Z"}
    #Regresa un dupla de diccionarios, dependiendo de la función que los llame
    return ((encriptar_ida, encriptar_regreso),(desencriptar_ida, desencriptar_regreso))

def idioma():
    """Se definen las listas para las letras repetidas del español y el inglés"""
    #Diccionario del español
    spanish = ["E", "A","O", "S", "R", "N", "I"]
    #Diccionario del inglés
    english = ["E", "A", "R", "I", "O", "T", "N"]
    return(spanish,english)

#Función que se utilizan para elegir el número al inicio del programa
def is_number(string):
    """Funcion que determina si un string es un número (incluye negativos)"""
    try:
        float(string)
        return True
    except ValueError:
        return False

#Función que se utilizan para elegir el número al inicio del programa
def is_int(number):
    """Funcion que determina si un número es entero"""
    try:
        int(number)
        return True
    except ValueError:
        return False

#Función auxiliar para el análisis de frecuencias
def is_in_tuple_list(lista, element):
    """Función que determina si hay un elemento en una lista de tuplas (En la primera posición)"""
    for tupla in lista:
        if tupla[0] == element:
            return True
    return False

#Función auxiliar para la función encriptar
def congruencia(numero, modulo):
    """"Función congruencia que reduce a un módulo en particular"""
    for i in range(modulo):
        if (numero-i)%modulo == 0:
            return i

def encriptar(texto,k):
    """Función que encripta el texto"""

    #Se toman los diccionarios del primer bloque. [0] es el primer
    # elemento de la dupla (diccionarios para encriptar)
    encriptar_ida, encriptar_regreso = diccionarios()[0]

    #Aquí se guardarán los números asociados a las letras
    texto_cifrado = []

    #Para cada char (caracter) en el texto, hacer lo siguiente
    for char in texto:
        #Si el caracter está en el diccionario de ida, asociarle su número
        if char in encriptar_ida:
            texto_cifrado.append(encriptar_ida[char])
        #De lo contrario, dejar el caracter intacto
        #PROYECTO ESPECIAL: si se quiere generar una función que elimine
        # todo, este 'else' debe borrar ese caracter
        else:
            texto_cifrado.append(char)

    #Para cada caracter en su posición i-ésima del texto_cifrado
    for i, char in enumerate(texto_cifrado):
        #Si el caracter es un entero, se le aplica la regla
        if isinstance(char, int):
            #Regla del cifrado César
            texto_cifrado[i] *= k
            texto_cifrado[i] = congruencia(texto_cifrado[i], 26)

    #Aquí se guardará las letras cifradas
    texto_cifrado_2 = []
    for char in texto_cifrado:
        if char in encriptar_regreso:
            texto_cifrado_2.append(encriptar_regreso[char])
        else:
            texto_cifrado_2.append(char)

    #Juntar todos los caracteres del texto_cifrado_2 en un string
    texto_encriptado = ''.join(texto_cifrado_2)
    print(f"El texto cifrado con la clave {k} es {texto_encriptado}.")

#Función auxiliar para el desencriptado, el cual utiliza el algortimo de Euclides
def euclides(a, b):
    """Función que halla el máximo común divisor entre dos números"""
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
        a = b
        b = r
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    return  a, u0

def desencriptar_clave(texto,k):
    """Función que desencripta el texto con clave"""

    desencriptar_ida, desencriptar_regreso = diccionarios()[1]
    texto_descifrado = []

    #Esta parte del código proviene del semestre pasado: inverso.py
    x0 = euclides(k, 26)[1]
    inverso = x0%26

    for char in texto:
        if char in desencriptar_ida:
            texto_descifrado.append(desencriptar_ida[char])
        else:
            texto_descifrado.append(char)

    for i, char in enumerate(texto_descifrado):
        if isinstance(char, int):
            texto_descifrado[i] *= inverso
            texto_descifrado[i] = congruencia(texto_descifrado[i], 26)

        if texto_descifrado[i] in desencriptar_regreso:
            texto_descifrado[i] = desencriptar_regreso[texto_descifrado[i]]

    texto_desencriptado = ''.join(texto_descifrado)
    print(f"El texto descifrado con la clave {k} es {texto_desencriptado}.")

def solcon(d,letra_1,letra_2,x1):
    """Función que resuelve ecuaciones de congruencias"""

    soluciones = []

    b26 = euclides(letra_1,26)[0]
    a26 = euclides(letra_2,26)[0]
    e = letra_1 / d
    x0 = x1 * e
    div = 26 / a26
    for i in range(b26):
        y = x0 + (div * i)
        soluciones.append(y)
    for j in soluciones:
        j26 = euclides(j,26)[0]
        if j26 == 1:
            return j
    print("La congruencia no tiene solución.")

def analisis(texto):
    """Función que analiza el texto y lo desencripta"""

    valid_lan = False

    while not valid_lan:
        #Aquí se sabrá en qué idioma está el texto (si el usuario lo sabe)
        option_lan = input("Escoge (0) si el texto está en español o (1) si está en inglés: ")

        if option_lan.isnumeric():
            option_lan = int(option_lan)

            if (option_lan == 0 or option_lan == 1):
                valid_lan = True

            else:
                print("Opción inválida.")

        else:
            print("Opción inválida.")

    letras_frecuentes = []
    if option_lan == 0:
        letras_frecuentes = idioma()[0]
        option_lan = "español"

    elif option_lan == 1:
        letras_frecuentes = idioma()[1]
        option_lan = "inglés"

    lista_frecuentes = ''
    for letter in letras_frecuentes:
        lista_frecuentes += f"{letter} "

    #Convierte todo el texto para que sea UpperCase (Consistente)
    string = texto.upper()

    #Crear un diccionario con las repeticiones de cada letra
    repeticiones = {}

    for char in string:
        if char in repeticiones:
            repeticiones[char] += 1
        elif char != " ":
            repeticiones[char] = 1

    #Crea un nuevo diccionario en el que se ordenan los elementos de acuerdo a
    # los valores de cada llave (letra) en el original.
    repeticiones_orden = sorted(repeticiones.items(), key=lambda x: x[1], reverse=True)

    #Prepara el string para imprimir la lista de repeticiones en una linea
    lista_repeticiones = ''
    for char, count in repeticiones_orden:
        lista_repeticiones += f"{char}:{count} "

    valid_text = False
    while not valid_text:
        print("\nConteo de letras en el texto (Descendente): ")
        print(lista_repeticiones)

        print(f"Elegiste el idioma {option_lan}. Las letras más frecuentes son:")
        print(f"{lista_frecuentes}\n")

        letra_1 = ''
        letra_2 = ''
        valid_first = False
        while not valid_first:
            letra_1 = input("Elige una de las letras más repetidas del texto: ")
            if is_in_tuple_list(repeticiones, letra_1):
                valid_first = True
            else:
                print("Opción inválida")
        valid_second = False
        while not valid_second:
            letra_2 = input(f"Elige una de las letras más frecuentes en el {option_lan}: ")
            if letra_2 in letras_frecuentes:
                valid_second = True
            else:
                print("Opción inválida")
        print("Letras elegidas: ")
        print(f"Mas repetidas del texto: {letra_1}")
        print(f"Mas frecuente del idioma: {letra_2}")

        desencriptar_ida = diccionarios()[1][0]
        if letra_1 in desencriptar_ida:
            letra_1 = desencriptar_ida[letra_1]
        if letra_2 in desencriptar_ida:
            letra_2 = desencriptar_ida[letra_2]

        d, x1 = euclides(letra_2, 26)
        s = solcon(d,letra_1,letra_2,x1)
        k = congruencia(s,26)
        desencriptar_clave(texto, k)

        valid_input = False
        while not valid_input:
            input_user = input("Si el texto es correcto, escribe (1), si no escribe (0): ")
            if input_user == "1":
                valid_text = True
                valid_input = True
            elif input_user == "0":
                valid_input = True
            else:
                print("Opcion invalida")

def desencriptar_fb(texto):
    """Función que desencripta el texto sin clave y con fuerza bruta"""

    desencriptar_ida, desencriptar_regreso = diccionarios()[1]

    texto_descifrado = []
    for char in texto:
        if char in desencriptar_ida:
            texto_descifrado.append(desencriptar_ida[char])
        else:
            texto_descifrado.append(char)

    textos_descifrados = []

    primosrelativos26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    for k in primosrelativos26:
        copia = texto_descifrado[:]

        x0 = euclides(k,26)[1]
        inverso = x0%26
        print(inverso)

        for i, char in enumerate(copia):
        # Si el caracter es un entero, se le aplica la regla
            if isinstance(char, int):
                copia[i] *= inverso
                copia[i] = congruencia(copia[i], 26)

            if copia[i] in desencriptar_regreso:
                copia[i] = desencriptar_regreso[copia[i]]

        textos_descifrados.append(''.join(copia))

    for k, texto in enumerate(textos_descifrados):
        #¿Sí imprime la clave correcta? :P
        print(f"k = {primosrelativos26[k]}, {texto}\n")

def decimado():
    #Se ponen entre tres comillas lo que queremos que diga que hace la función
    """Es la función principal del programa Decimado"""

    valid_input = False
    while not valid_input:

        option_1 = input("Escoge (0) si quieres encriptar o (1) si quieres desencriptar: ")
        #Si elige una de las opciones correctamente, el ciclo terminará
        if option_1.isnumeric():
            option_1 = int(option_1)
            if (option_1 == 0 or option_1 == 1):
                valid_input = True

            else:
                print("Opción inválida.")

        else:
            print("Opción inválida.")

    if option_1 == 0:

        valid_k = False
        while not valid_k:

            clave_k = input("Escoge un número entero para encriptar en formato Decimado: ")

            if is_number(clave_k):
                clave_k = float(clave_k)
                if is_int(clave_k):
                    clave_k = int(clave_k)
                    if clave_k in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
                        valid_k = True
            else:
                print("Opción inválida.")

        texto_1 = input("Ingresa el texto que quieres encriptar: ")

        encriptar(texto_1,clave_k)
        #Si se desea para proyecto futuro: definir otra función que elimine los
        # caracteres que no estén en el diccionario

    #Si se elige desencriptar
    elif option_1 == 1:

        valid_input_2 = False

        while not valid_input_2:
            #Aquí se sabrá si se tiene la clave o no
            option_2 = input("Escoge (0) si tienes la clave o (1) si no tienes la clave: ")

            if option_2.isnumeric():
                option_2 = int(option_2)

                if (option_2 == 0 or option_2 == 1):
                    valid_input_2 = True

                else:
                    print("Opción inválida.")

            else:
                print("Opción inválida.")

        if option_2 == 0:

            valid_j = False
            while not valid_j:

                clave_j = input("Escoge un número entero para desencriptar en formato Decimado: ")
                if is_number(clave_j):
                    clave_j = float(clave_j)
                    if is_int(clave_j):
                        clave_j = int(clave_j)
                        if clave_j in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
                            valid_j = True
                else:
                    print("Por favor, ingresa un número entero.")

            texto_2 = input("Ingresa el texto que quieres desencriptar: ")
            desencriptar_clave(texto_2,clave_j)

        elif option_2 == 1:

            valid_input_3 = False

            while not valid_input_3:
                #Aquí se sabrá si se tiene la clave o no
                option_3 = input("Escoge (0) para analizar el texto o (1) para desencriptar: ")

                if option_3.isnumeric():
                    option_3 = int(option_3)

                    if (option_3 == 0 or option_3 == 1):
                        valid_input_3 = True

                    else:
                        print("Opción inválida.")

                else:
                    print("Opción inválida.")

            if option_3 == 0:
                #Este es el método por análisis de texto
                texto_2 = input("Ingresa el texto que quieres desencriptar: ")
                analisis(texto_2)

            if option_3 == 1:
                #Este es el método de fuerza bruta
                texto_2 = input("Ingresa el texto que quieres desencriptar: ")
                desencriptar_fb(texto_2)

decimado()
