# https://wiki.python.org.br/ExerciciosListas
#7

v = []

v.append(int(input("N 1: ")))
v.append(int(input("N 2: ")))
v.append(int(input("N 3: ")))
v.append(int(input("N 4: ")))
v.append(int(input("N 5: ")))

print("Soma: {}".format(
    v[0] + v[1] + v[2] + v[3]
))

print("Multiplicação: {}".format(
    v[0] * v[1] * v[2] * v[3]
))

print("Números: {}".format(v))