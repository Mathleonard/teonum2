def congruencia(x, y, m):
    a = x ** y
    for i in range(m):
        if (a-i)%m == 0:
            return i

def elegir():
    x = int(input("Escoge tu base: "))
    y = int(input("Escoge tu exponente: "))
    m = int(input("Escoge tu módulo: "))
    z = congruencia(x,y,m)
    print(f"El número congruente a {x} elevado a la {y} módulo {m} es {z}.")

elegir()