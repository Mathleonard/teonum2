"""Programa para Encriptar/Desencriptar por el método César"""

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
    """Se definen los diccionarios para las letras repetidas del español y el inglés"""
    #Diccionario del español
    spanish = {"E": 4, "e": 4,
               "A": 0, "a": 0,
               "O": 14, "o": 14,
               "S": 18, "s": 18,
               "R": 17, "r": 17,
               "N": 13, "n": 13,
               "I": 8, "i": 8}
    #Diccionario del inglés
    english = {"E": 4, "e": 4,
               "A": 0, "a": 0,
               "R": 17, "r": 17,
               "I": 8, "i": 8,
               "O": 14, "o": 14,
               "T": 19, "t": 19,
               "N": 13, "n": 13}
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
    """Funcion que determina si un numero es entero"""
    try:
        int(number)
        return True
    except ValueError:
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
            texto_cifrado[i] += k
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

def desencriptar_clave(texto,k):
    """Función que desencripta el texto con clave"""

    desencriptar_ida, desencriptar_regreso = diccionarios()[1]
    texto_descifrado = []

    for char in texto:
        if char in desencriptar_ida:
            texto_descifrado.append(desencriptar_ida[char])
        else:
            texto_descifrado.append(char)

    for i, char in enumerate(texto_descifrado):
        if isinstance(char, int):
            texto_descifrado[i] -= k
            texto_descifrado[i] = congruencia(texto_descifrado[i], 26)

        if texto_descifrado[i] in desencriptar_regreso:
            texto_descifrado[i] = desencriptar_regreso[texto_descifrado[i]]

    texto_desencriptado = ''.join(texto_descifrado)
    print(f"El texto descifrado con la clave {k} es {texto_desencriptado}.")

def analisis(texto):
    """Función que analiza el texto y lo desencripta"""
#####################################################################################

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

    if option_lan == 0:
        #Su texto está en español
        texto_2 = input("Ingresa el texto que quieres desencriptar: ")
        analisis(texto_2)

    if option_lan == 1:
        #Este es el método de fuerza bruta
        texto_2 = input("Ingresa el texto que quieres desencriptar: ")
        desencriptar_fb(texto_2)










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

    for k in range(26):
        copia = texto_descifrado[:]
        for i, char in enumerate(copia):
        # Si el caracter es un entero, se le aplica la regla
            if isinstance(char, int):
                copia[i] -= k
                copia[i] = congruencia(copia[i], 26)

            if copia[i] in desencriptar_regreso:
                copia[i] = desencriptar_regreso[copia[i]]

        textos_descifrados.append(''.join(copia))

    for k, texto in enumerate(textos_descifrados):
        print(f"k = {k}, {texto}\n")

def cesar():
    #Se ponen entre tres comillas lo que queremos que diga que hace la función
    """Es la función principal del programa César"""

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

            clave_k = input("Escoge un número entero para encriptar en formato César: ")

            if is_number(clave_k):
                clave_k = float(clave_k)
                if is_int(clave_k):
                    clave_k = int(clave_k)
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

                clave_j = input("Escoge un número entero para desencriptar en formato César: ")
                if is_number(clave_j):
                    clave_j = float(clave_j)
                    if is_int(clave_j):
                        clave_j = int(clave_j)
                        valid_j = True
                else:
                    print("Por favor, ingresa un número entero.")

            texto_2 = input("Ingresa el texto que quieres desencriptar: ")
            desencriptar_clave(texto_2,clave_j)

        elif option_2 == 1:

            ####################################################################

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

cesar()
