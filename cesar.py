def congruencia(a, m):
    for i in range(m):
        if (a-i)%m == 0:
            return i

def encriptar(texto,k):

    values_1 = {"A": 0,
              "Á": 0,
              "B": 1,
              "C": 2,
              "D": 3,
              "E": 4,
              "É": 4,
              "F": 5,
              "G": 6,
              "H": 7,
              "I": 8,
              "Í": 8,
              "J": 9,
              "K": 10,
              "L": 11,
              "M": 12,
              "N": 13,
              "Ñ": 13,
              "O": 14,
              "Ó": 14,
              "P": 15,
              "Q": 16,
              "R": 17,
              "S": 18,
              "T": 19,
              "U": 20,
              "Ú": 20,
              "V": 21,
              "W": 22,
              "X": 23,
              "Y": 24,
              "Z": 25
              }

    values_2 = {0: "A",
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

    k = int(k)
    texto_cifrado = []

    for char in texto:
        if char in values_1:
            texto_cifrado.append(values_1[char])
        else:
            texto_cifrado.append(char)

    for i, char in enumerate(texto_cifrado):
        # Si el caracter es un entero, se le aplica la regla
        if isinstance(char, int):
            texto_cifrado[i] += k
            texto_cifrado[i] = congruencia(texto_cifrado[i], 26)

    texto_cifrado_2 = []
    for char in texto_cifrado:
        if char in values_2:
            texto_cifrado_2.append(values_2[char])
        else:
            texto_cifrado_2.append(char)

    string = ''.join(texto_cifrado_2)
    print(string)

def dicts_desencriptar():
    values_3 = {"A": 0,
              "B": 1,
              "C": 2,
              "D": 3,
              "E": 4,
              "F": 5,
              "G": 6,
              "H": 7,
              "I": 8,
              "J": 9,
              "K": 10,
              "L": 11,
              "M": 12,
              "N": 13,
              "O": 14,
              "P": 15,
              "Q": 16,
              "R": 17,
              "S": 18,
              "T": 19,
              "U": 20,
              "V": 21,
              "W": 22,
              "X": 23,
              "Y": 24,
              "Z": 25
              }

    values_4 = {0: "A",
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
    return values_3, values_4

def desencriptar_clave(texto,k):

    values_3, values_4 = dicts_desencriptar()
    texto_descifrado = []
    for char in texto:
        if char in values_3:
            texto_descifrado.append(values_3[char])
        else:
            texto_descifrado.append(char)

    for i, char in enumerate(texto_descifrado):
    # Si el caracter es un entero, se le aplica la regla
        if isinstance(char, int):
            texto_descifrado[i] -= k
            texto_descifrado[i] = congruencia(texto_descifrado[i], 26)

        if texto_descifrado[i] in values_4:
            texto_descifrado[i] = values_4[texto_descifrado[i]]

    texto_final = ''.join(texto_descifrado)
    print(texto_final)

def desencriptar(texto):

    values_3, values_4 = dicts_desencriptar()

    texto_descifrado = []
    for char in texto:
        if char in values_3:
            texto_descifrado.append(values_3[char])
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

            if copia[i] in values_4:
                copia[i] = values_4[copia[i]]

        textos_descifrados.append(''.join(copia))

    for k, texto in enumerate(textos_descifrados):
        print(f"k = {k}, {texto}\n")

#Esta es la función principal
def elegir():

    #Asigna una variable como falsa inicialmente
    valid_input = False

    #Mientras no se cumpla la variable, ejecuta el programa
    while not valid_input:

        #Escoge un entero para decidir qué debe hacer el programa
        a = int(input("Escoge (0) si quieres encriptar o (1) si quieres desencriptar: "))

        #Condición 1)
        if a == 1 or a == 0:
            #Asigna el valor como verdadero, y se sale del ciclo
            valid_input = True
    if a == 0:
        texto_1 = input("Ingresa el texto que quieres encriptar: ")
        k = int(input("Escoge un número entero para encriptar en formato César: "))
        encriptar(texto_1,k)

    elif a == 1:
        #Para desencriptar, necesita escribir el texto
        texto_2 = input("Ingreso el texto que quieres desencriptar: ")
        #Asignamos una segunda variable falsa
        valid_input_2 = False

        while not valid_input_2:
            #Aquí se sabrá si se tiene la clave o no
            b = int(input("Escoge (0) si tienes la clave o (1) si no tienes la clave: "))

            if b == 1 or b == 0:

                valid_input_2 = True

        if b == 0:
            j = int(input("Ingresa la clave para desencriptar: "))
            #Al ingresar la clave llamará a la función para desencriptar con clave
            desencriptar_clave(texto_2,j)

        elif b == 1:
            #Este es el método de fuerza bruta
            desencriptar(texto_2)

elegir()
