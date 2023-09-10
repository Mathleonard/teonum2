def congruencia(a, m):
    for i in range(m):
        if (a-i)%m == 0:
            return i

def elegir():
    # valid_input = False
    # while not valid_input:
    a = int(input("Escoge tu número al que le sacarás congruencia: "))
    m = int(input("Escoge el módulo de tu congruencia: "))
    b = congruencia(a,m)
    print(f"El número congruente a {a} módulo {m} es {b}.")

elegir()
