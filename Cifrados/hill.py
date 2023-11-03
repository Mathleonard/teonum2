"""Programa para Encriptar/Desencriptar por el método Hill"""

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

def is_number(string):
    """Función que determina si un string es un número"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_int(number):
    """Función que determina si un número es entero"""
    try:
        int(number)
        return True
    except ValueError:
        return False

def determinante(a_1_1, a_1_2, a_2_1, a_2_2):
    """Función para hallar el determinante de una matriz"""
    det = (a_1_1 * a_2_2) - (a_2_1 * a_1_2)
    return det

def congruencia(numero):
    """"Función congruencia que reduce a un módulo en particular"""
    for i in range(26):
        if (numero-i)%26 == 0:
            return i

def algoritmo_div(dividendo, divisor):
    """Función para hallar el máximo común divisor de dos números"""
    residuo_ad = dividendo%divisor
    if residuo_ad != 0:
        return algoritmo_div(divisor, residuo_ad)
    else:
        mcd = abs(divisor)
        return mcd

def longtxt(texto):
    #Da la longitud del texto sin ningún otro caracter

    encriptar_ida = diccionarios()[0][0]

    texto_bruto = []

    for char in texto:
        if char in encriptar_ida:
            texto_bruto.append(char)

    texto_bruto_final = ''.join(texto_bruto)

    l = len(texto_bruto_final)

    return l, texto_bruto_final

def multi(a_1_1, a_1_2, a_2_1, a_2_2, pareja):
    """Función para multiplicar matrices"""
    
    p_2_0 = (a_1_1 * pareja[0]) + (a_1_2 * pareja[1])
    p_2_1 = (a_2_1 * pareja[0]) + (a_2_2 * pareja[1])

    return (p_2_0, p_2_1)

def encriptar_hill(a_1_1, a_1_2, a_2_1, a_2_2, texto):
    """Función para encriptar el mensaje"""

    encriptar_ida, encriptar_regreso = diccionarios()[0]

    texto_cifrado = []

    long, texto_bruto = longtxt(texto)

    if long%2 != 0:
        texto_bruto += texto_bruto[-1]

    #Para cada char (caracter) en el texto, hacer lo siguiente
    for char in texto_bruto:
        #Asociar el número a la letra
        texto_cifrado.append(encriptar_ida[char])

    texto_cifrado_parejas = []

    # Recorrer la lista original en pasos de 2 en 2
    for i in range(0, len(texto_cifrado), 2):
        if i + 1 < len(texto_cifrado):
            pareja = (texto_cifrado[i], texto_cifrado[i + 1])
            texto_cifrado_parejas.append(pareja)

    texto_cifrado_2 = ''

    for pareja in texto_cifrado_parejas:
        a, b = multi(a_1_1, a_1_2, a_2_1, a_2_2, pareja)
        c = congruencia(a)
        d = congruencia(b)
        texto_cifrado_2 += encriptar_regreso[c]
        texto_cifrado_2 += encriptar_regreso[d]

    print(f"Tu texto cifrado es: {texto_cifrado_2}.")

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

def minversa(a_1_1, a_1_2, a_2_1, a_2_2, det):
    x0 = euclides(det, 26)[1]
    inverso = x0%26
    b_1_1 = inverso * a_2_2
    b_1_2 = (-1) * (inverso * a_1_2)
    b_2_1 = (-1) * (inverso * a_2_1)
    b_2_2 = inverso * a_1_1
    
    return b_1_1, b_1_2, b_2_1, b_2_2

def desencriptar_hill(a_1_1, a_1_2, a_2_1, a_2_2, det, texto):
    """Función para desencriptar el mensaje"""

    desencriptar_ida, desencriptar_regreso = diccionarios()[1]

    texto_2 = longtxt(texto)[1]

    texto_descifrado = []

    #Para cada char (caracter) en el texto, hacer lo siguiente
    for char in texto_2:
        #Asociar el número a la letra
        texto_descifrado.append(desencriptar_ida[char])

    texto_descifrado_parejas = []

    # Recorrer la lista original en pasos de 2 en 2
    for i in range(0, len(texto_descifrado), 2):
        if i + 1 < len(texto_descifrado):
            pareja = (texto_descifrado[i], texto_descifrado[i + 1])
            texto_descifrado_parejas.append(pareja)

    texto_descifrado_2 = ''

    m, n, o, p = minversa(a_1_1, a_1_2, a_2_1, a_2_2, det)

    for pareja in texto_descifrado_parejas:
        a, b = multi(m, n, o, p, pareja)
        c = congruencia(a)
        d = congruencia(b)
        texto_descifrado_2 += desencriptar_regreso[c]
        texto_descifrado_2 += desencriptar_regreso[d]

    print(f"Tu texto descifrado es: {texto_descifrado_2}.")

def hill():
    """Función principal, lo que se mostrará al usuario"""
    input_1 = False
    while not input_1:
        option_1 = input("Escoge (0) si quieres encriptar o (1) si quieres desencriptar: ")
        if option_1.isnumeric():
            option_1 = int(option_1)
            if (option_1 == 0 or option_1 == 1):
                input_1 = True
            else:
                print("Opción inválida.")
        else:
            print("Opción inválida.")
    if option_1 == 0:
        input_det = False
        while not input_det:
            input_1_1 = False
            while not input_1_1:
                a_1_1 = input("Escribe el primer número entero de tu matriz clave: ")
                if is_number(a_1_1):
                    a_1_1 = float(a_1_1)
                    if is_int(a_1_1):
                        a_1_1 = int(a_1_1)
                        input_1_1 = True
                else:
                    print("Opción inválida.")
            input_1_2 = False
            while not input_1_2:
                a_1_2 = input("Escribe el segundo número entero de tu matriz clave: ")
                if is_number(a_1_2):
                    a_1_2 = float(a_1_2)
                    if is_int(a_1_2):
                        a_1_2 = int(a_1_2)
                        input_1_2 = True
                else:
                    print("Opción inválida.")
            input_2_1 = False
            while not input_2_1:
                a_2_1 = input("Escribe el tercer número entero de tu matriz clave: ")
                if is_number(a_2_1):
                    a_2_1 = float(a_2_1)
                    if is_int(a_2_1):
                        a_2_1 = int(a_2_1)
                        input_2_1 = True
                else:
                    print("Opción inválida.")
            input_2_2 = False
            while not input_2_2:
                a_2_2 = input("Escribe el cuarto número entero de tu matriz clave: ")
                if is_number(a_2_2):
                    a_2_2 = float(a_2_2)
                    if is_int(a_2_2):
                        a_2_2 = int(a_2_2)
                        input_2_2 = True
                else:
                    print("Opción inválida.")
                det = determinante(a_1_1, a_1_2, a_2_1, a_2_2)
                cong_det = congruencia(det)
                mcd = algoritmo_div(26, cong_det)
                if mcd == 1:
                    input_det = True
                else:
                    print("La determinante de tu matriz no es primo relativo a 26.")
        texto_1 = input("Ingresa el texto que quieres encriptar: ")
        encriptar_hill(a_1_1, a_1_2, a_2_1, a_2_2, texto_1)
        
    elif option_1 == 1:
        input_det = False
        while not input_det:
            input_1_1 = False
            while not input_1_1:
                a_1_1 = input("Escribe el primer número entero de tu matriz clave: ")
                if is_number(a_1_1):
                    a_1_1 = float(a_1_1)
                    if is_int(a_1_1):
                        a_1_1 = int(a_1_1)
                        input_1_1 = True
                else:
                    print("Opción inválida.")
            input_1_2 = False
            while not input_1_2:
                a_1_2 = input("Escribe el segundo número entero de tu matriz clave: ")
                if is_number(a_1_2):
                    a_1_2 = float(a_1_2)
                    if is_int(a_1_2):
                        a_1_2 = int(a_1_2)
                        input_1_2 = True
                else:
                    print("Opción inválida.")
            input_2_1 = False
            while not input_2_1:
                a_2_1 = input("Escribe el tercer número entero de tu matriz clave: ")
                if is_number(a_2_1):
                    a_2_1 = float(a_2_1)
                    if is_int(a_2_1):
                        a_2_1 = int(a_2_1)
                        input_2_1 = True
                else:
                    print("Opción inválida.")
            input_2_2 = False
            while not input_2_2:
                a_2_2 = input("Escribe el cuarto número entero de tu matriz clave: ")
                if is_number(a_2_2):
                    a_2_2 = float(a_2_2)
                    if is_int(a_2_2):
                        a_2_2 = int(a_2_2)
                        input_2_2 = True
                else:
                    print("Opción inválida.")
                det = determinante(a_1_1, a_1_2, a_2_1, a_2_2)
                cong_det = congruencia(det)
                mcd = algoritmo_div(26, cong_det)
                if mcd == 1:
                    input_det = True
                else:
                    print("La determinante de tu matriz no es primo relativo a 26.")
        texto_1 = input("Ingresa el texto que quieres desencriptar: ")
        desencriptar_hill(a_1_1, a_1_2, a_2_1, a_2_2, cong_det, texto_1)

hill()
