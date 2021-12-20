# https://wiki.python.org.br/ExerciciosListas
#3

n = []

n.append(float(input("Nota 1: ")))
n.append(float(input("Nota 2: ")))
n.append(float(input("Nota 3: ")))
n.append(float(input("Nota 4: ")))

s = n[0] + n[1] + n[2] + n[3]

print("\nA média é: ",s/4)