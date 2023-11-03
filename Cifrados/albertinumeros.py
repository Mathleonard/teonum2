"""Programa para Encriptar/Desencriptar por el método Alberti con Índice de Números"""

# Función que se utilizan para elegir el número al inicio del programa
def is_int(number):
    """Funcion que determina si un número es entero"""
    try:
        int(number)
        return True
    except ValueError:
        return False
    
def reorder_list(lst, i):
    if i < 0 or i >= len(lst):
        # Handle invalid index
        return lst

    # Slice the list into two parts: before and after index i
    before_i = lst[:i]
    after_i = lst[i:]

    # Reorder the list by concatenating after_i and before_i
    reordered_list = after_i + before_i

    return reordered_list

def diccionarios():
    """Se definen los diccionarios para el programa (encriptar y desencriptar)"""

    #Diccionario para encriptar al inicio
    disco_afuera_upper = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R",
                        "S","T","V","X","Z","1","2","3","4"]
    
    disco_afuera_lower = ["a","b","c","d","e","f","g","i","l","m","n","o","p","q","r",
                        "s","t","v","x","z","1","2","3","4"]
    
    #Diccionario para encriptar al final
    disco_adentro = ["g","k","l","n","p","r","t","v","z","&","x","y","s","o","m",
                        "q","i","h","f","d","b","a","c","e"]

    #Regresa un dupla de diccionarios, dependiendo de la función que los llame
    return (disco_afuera_upper, disco_afuera_lower, disco_adentro)

def encriptar(texto,A,g):
    """Función que encripta el texto"""

    disco_afuera_upper, disco_afuera_lower, disco_adentro = diccionarios()

    disco_afuera_copia = disco_afuera_upper[:]
    disco_afuera_lower_copia = disco_afuera_lower[:]
    disco_adentro_copia = disco_adentro[:]

    texto_encriptado = ""
    idx_disco_afuera = 0
    idx_disco_adentro = 0
    idx_texto = -1
    for char in texto:
          
        idx_texto += 1
        if idx_texto == 0:
            
            idx_disco_afuera = disco_afuera_copia.index(A)
            idx_disco_adentro = disco_adentro_copia.index(g)

            disco_afuera_copia = reorder_list(disco_afuera_copia, idx_disco_afuera)
            disco_afuera_lower_copia = reorder_list(disco_afuera_lower_copia, idx_disco_afuera)
            disco_adentro_copia = reorder_list(disco_adentro_copia,idx_disco_adentro)
            
            texto_encriptado += disco_adentro_copia[disco_afuera_lower_copia.index(char)]
                        
            continue
        
        if char in disco_afuera_lower and not is_int(char):

            texto_encriptado += disco_adentro_copia[disco_afuera_lower_copia.index(char)]
            
            continue

        if char == "u":
            
            texto_encriptado += disco_adentro_copia[disco_afuera_lower_copia.index("v")]
            
            continue
        
        if char in disco_afuera_lower and is_int(char):
            
            idx_disco_afuera = disco_afuera_copia.index(A)
            idx_disco_adentro = disco_afuera_lower_copia.index(char)
            texto_encriptado += disco_adentro_copia[idx_disco_adentro]

            disco_afuera_copia = reorder_list(disco_afuera_copia, idx_disco_afuera)
            disco_afuera_lower_copia = reorder_list(disco_afuera_lower_copia, idx_disco_afuera)
            disco_adentro_copia = reorder_list(disco_adentro_copia,idx_disco_adentro)
            
            continue
            
        elif char not in disco_afuera_lower and char not in disco_afuera_upper:
            texto_encriptado += char
            continue

    print(f"Texto encriptado: {texto_encriptado}")

def desencriptar(texto,A,g):
    """Función que desencripta el texto"""

    disco_afuera_upper, disco_afuera_lower, disco_adentro = diccionarios()

    disco_afuera_copia = disco_afuera_upper[:]
    disco_afuera_lower_copia = disco_afuera_lower[:]
    disco_adentro_copia = disco_adentro[:]

    texto_desencriptado = ""
    idx_disco_afuera = 0
    idx_disco_adentro = 0

    idx_texto = -1
    for char in texto:
        
        idx_texto += 1
        if idx_texto == 0:
            
            idx_disco_afuera = disco_afuera_copia.index(A)
            idx_disco_adentro = disco_adentro_copia.index(g)

            disco_afuera_copia = reorder_list(disco_afuera_copia, idx_disco_afuera)
            disco_afuera_lower_copia = reorder_list(disco_afuera_lower_copia, idx_disco_afuera)
            disco_adentro_copia = reorder_list(disco_adentro_copia,idx_disco_adentro)
            
            texto_desencriptado += disco_afuera_lower_copia[disco_adentro_copia.index(char)]
                        
            continue
        
        if char in disco_adentro:

            if disco_afuera_lower_copia[disco_adentro_copia.index(char)] == "v":
                texto_desencriptado += "u"
                continue
            
            if is_int(disco_afuera_lower_copia[disco_adentro_copia.index(char)]):
                idx_disco_afuera = disco_afuera_copia.index(A)
                idx_disco_adentro = disco_adentro_copia.index(char)
                
                texto_desencriptado += disco_afuera_copia[disco_adentro_copia.index(char)]

                disco_afuera_copia = reorder_list(disco_afuera_copia, idx_disco_afuera)
                disco_afuera_lower_copia = reorder_list(disco_afuera_lower_copia, idx_disco_afuera)
                disco_adentro_copia = reorder_list(disco_adentro_copia,idx_disco_adentro)
                
                continue
                
            
            texto_desencriptado += disco_afuera_lower_copia[disco_adentro_copia.index(char)]
            
            continue

        if char == "u":
            
            texto_desencriptado += disco_afuera_lower_copia[disco_adentro_copia.index("v")]
            
            continue

        elif char not in disco_adentro:
            texto_desencriptado += char
            continue

    print(f"Texto desencriptado: {texto_desencriptado}")

def albertiletras():
    #Se ponen entre tres comillas lo que queremos que diga que hace la función
    """Es la función principal del programa Alberti con Índice de Números"""

    disco_afuera_upper, disco_afuera_lower, disco_adentro = diccionarios()

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

        valid_A = False
        while not valid_A:

            clave_A = input("Escoge tu primera letra para cifrar: ")

            if clave_A in disco_afuera_upper:
                valid_A = True
            else:
                print("Opción inválida.")

        valid_g = False
        while not valid_g:

            clave_g = input("Escoge tu segunda letra para cifrar: ")

            if clave_g in disco_adentro:
                valid_g = True
            else:
                print("Opción inválida.")

        texto_1 = input("Ingresa el texto que quieres encriptar: ")

        encriptar(texto_1,clave_A,clave_g)
        #Si se desea para proyecto futuro: definir otra función que elimine los
        # caracteres que no estén en el diccionario

    #Si se elige desencriptar
    elif option_1 == 1:

        valid_B = False
        while not valid_B:

            clave_B = input("Escoge tu primera letra para cifrar: ")

            if clave_B in disco_afuera_upper:
                valid_B = True
            else:
                print("Opción inválida.")

        valid_k = False
        while not valid_k:

            clave_k = input("Escoge tu segunda letra para cifrar: ")

            if clave_k in disco_adentro:
                valid_k = True
            else:
                print("Opción inválida.")

        texto_2 = input("Ingresa el texto que quieres desencriptar: ")
        desencriptar(texto_2,clave_B,clave_k)


albertiletras()
