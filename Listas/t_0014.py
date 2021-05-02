# https://wiki.python.org.br/ExerciciosFuncoes
# 1

def ex_01(n):
    i = 0

    while i < n:
        y = 0

        while y < i:
            print(n)
            y += 1
        i += 1

ex_01(int(input("Digite um número: ")))