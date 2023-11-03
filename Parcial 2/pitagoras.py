"""Programa para crear e identificar Ternas Pitagóricas (primitivas)"""

def algoritmo_div(n, a):
    """Función auxiliar que calcula el máximo común divisor"""

    residuo_ad = n%a

    if residuo_ad != 0:
        return algoritmo_div(a,residuo_ad)

    else:
        s = abs(a)
        return s


def pitagoras():
    """Función principal"""

    valid_input = False

    while not valid_input:

        x = int(input("Escoge (0) para crear una t.p.p. o (1) si quieres ver una t.p.p.: "))

        if x == 1 or x == 0:
            valid_input = True

    if x == 0:
        n = int(input("Escribe tu primer número: "))
        m = int(input("Escribe tu segundo número: "))
        if algoritmo_div(n,m) == 1:
            print(algoritmo_div(n,m))
        else:
            print("No elegiste dos números adecuados.")

    elif x == 1:
        a = int(input("Escribe tu primer número: "))
        b = int(input("Escribe tu segundo número: "))
        c = int(input("Escribe tu tercer número: "))
        print(a,b,c)

pitagoras()
