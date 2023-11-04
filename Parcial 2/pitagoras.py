"""Programa para crear e identificar Ternas Pitagóricas (primitivas)"""

def algoritmo_div(n, a):
    """Función auxiliar que calcula el máximo común divisor"""

    residuo_ad = n%a

    if residuo_ad != 0:
        return algoritmo_div(a,residuo_ad)

    else:
        s = abs(a)
        return s

def ternaPrimitiva(x,y,z):
    """Función auxiliar que determina si una terna es primitiva"""
    mcdxy = algoritmo_div(x,y)
    mcdantz = algoritmo_div(mcdxy,z)
    return mcdantz

def teoremaPitagoras(x,y,z):
    """Función auxiliar que comprueba el teorema de Pitágoras"""
    if (x ** 2) + (y ** 2) == z ** 2:
        return True
    else:
        return False

def pitagoras():
    """Función principal"""

    valid_input = False

    while not valid_input:

        x = int(input("Escoge (0) para crear una t.p.p. o (1) si quieres ver una t.p.p.: "))

        if x == 1 or x == 0:
            valid_input = True

    if x == 0:
        m = int(input("Escribe tu primer número m: "))
        n = int(input("Escribe tu segundo número n: "))
        if (algoritmo_div(m,n) == 1) and (m % 2 == 0) and (n % 2 == 1) and (m > n):
            p = 2 * m * n
            q = (m ** 2) - (n ** 2)
            r = (m ** 2) + (n ** 2)
            print(f"Tu terna pitagórica primitiva es ({p},{q},{r}).")
        else:
            print("No elegiste dos números adecuados.")

    elif x == 1:
        a = int(input("Escribe tu primer número x (sin cuadrado): "))
        b = int(input("Escribe tu segundo número y (sin cuadrado): "))
        c = int(input("Escribe tu tercer número z (sin cuadrado): "))
        if (ternaPrimitiva(a,b,c)) == 1 and (teoremaPitagoras(a,b,c)) == True:
            print(f"Tu terna ({a},{b},{c}) es una terna pitagórica primitiva.")
        else:
            print(f"Tu terna ({a},{b},{c}) no es una terna pitagórica primitiva.")

pitagoras()
