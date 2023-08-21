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

    texto_cifrado = []
    for char in texto:
        if char in values_1:
            texto_cifrado.append(values_1[char])
        else:
            texto_cifrado.append(char)

    for i in range(len(texto_cifrado)):
    #     #Si el caracter es un entero, se le aplica la regla
        if isinstance(texto_cifrado[i], int):
            if texto_cifrado[i] + k <= 25:
                texto_cifrado[i] += k
            else:
                texto_cifrado[i] += k - 26


    texto_cifrado_2 = []
    for char in texto_cifrado:
        if char in values_2:
            texto_cifrado_2.append(values_2[char])
        else:
            texto_cifrado_2.append(char)

    string = ''.join(texto_cifrado_2)
    print(string)


def desencriptar(texto):

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

    texto_descifrado = []
    for char in texto:
        if char in values_3:
            texto_descifrado.append(values_3[char])
        else:
            texto_descifrado.append(char)

    textos_descifrados = []

    for k in range(26):
        for i in range(len(texto_descifrado)):
            #Si el caracter es un entero, se le aplica la regla
            if isinstance(texto_descifrado[i], int):
                if texto_descifrado[i] - k >= 0:
                    texto_descifrado[i] -= k
                else:
                    texto_descifrado[i] -= k - 26

        texto_descifrado_2 = []
        for char in texto_descifrado:
            if char in values_4:
                texto_descifrado_2.append(values_4[char])
            else:
                texto_descifrado_2.append(char)

        string = ''.join(texto_descifrado_2)
        textos_descifrados.append(string)

    print(textos_descifrados)

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
        texto_2 = input("Ingreso el texto que quieres desencriptar: ")
        desencriptar(texto_2)


elegir()