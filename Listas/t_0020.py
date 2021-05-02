# https://wiki.python.org.br/ExerciciosFuncoes
# 11

def data(d,m,a):
    if m == 1:
        m = "janeiro"
        if d >= 32:
            print("Esta data não é válida!")
            exit()

    elif m == 2:
        m = "fevereiro"
        if d >= 28:
            print("Esta data não é válida!")
            exit()

    elif m == 3:
        m = "março"
        if d >= 32:
            print("Esta data não é válida!")
            exit()

    elif m == 4:
        m = "abril"
        if d >= 31:
            print("Esta data não é válida!")
            exit()

    elif m == 5:
        m = "maio"
        if d >= 32:
            print("Esta data não é válida!")
            exit()

    elif m == 6:
        m = "junho"
        if d >= 31:
            print("Esta data não é válida!")
            exit()

    elif m == 7:
        m = "julho"
        if d >= 32:
            print("Esta data não é válida!")
            exit()

    elif m == 8:
        m = "agosto"
        if d >= 32:
            print("Esta data não é válida!")
            exit()

    elif m == 9:
        m = "setembro"
        if d >= 31:
            print("Esta data não é válida!")
            exit()

    elif m == 10:
        m = "outubro"
        if d >= 32:
            print("Esta data não é válida!")
            exit()

    elif m == 11:
        m = "novembro"
        if d >= 31:
            print("Esta data não é válida!")
            exit()

    elif m == 12:
        m = "dezembro"
        if d >= 32:
            print("Esta data não é válida!")
            exit()

    elif m >= 12:
        print("Mês inválido")
        exit()

    print("\n{} de {} de {}".format(d,m,a))

data(
    int(input("Dia: ")),
    int(input("Mês: ")),
    int(input("Ano: "))
)