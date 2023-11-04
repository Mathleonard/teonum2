"""Función para calcular la solución mínima de la ecuación de Pell"""

def procedimiento(d):
    """Función que hace las operaciones"""
    sqrtd = d ** 0.5
    for i in range(1,100000):
        x_1 = int(i * sqrtd)
        x_2 = int(i * sqrtd) + 1
        izq_1 = (x_1 ** 2) - (d * (i ** 2))
        izq_2 = (x_2 ** 2) - (d * (i ** 2))
        if izq_1 == 1:
            return x_1, i
        elif izq_2 == 1:
            return x_2, i
    return None, None

def pell():
    """Función principal"""
    valid_input = False

    while not valid_input:

        numero = input("Escoge tu número d: ")

        try:
            numero = int(numero)
            if numero > 1 and (numero ** 0.5 % 1 != 0):
                valid_input = True

        except ValueError:
            print("No es un número válido")

    (x,y) = procedimiento(numero)
    if (x,y) == (None, None):
        print("La solución es demasiado grande, intenta aumentar el rango de búsqueda.")
    else:
        print(f"La mínima solución de la ecuación x^2-{numero}y^2=1 es ({x},{y}).")

pell()
