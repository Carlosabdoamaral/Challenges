# https://wiki.python.org.br/ExerciciosListas
#6

a = []
n = []
i = 0
passou = []
nPassou = []

while i < 10:
    a.append(print("\nAluno {}".format(i)))
    n.append(float(input("Nota 1: ")))
    n.append(float(input("Nota 2: ")))
    n.append(float(input("Nota 3: ")))
    n.append(float(input("Nota 4: ")))

    if ((n[i] + n[i+1] + n[i+2] + n[i+3]) / 4) >= 7.0:
        passou.append("")
    else:
        nPassou.append("")

    i += 1
# A[0] <=> N[0,1,2,3]
print("Passaram: {}".format(len(passou)))
print("Não passaram: {}".format(len(nPassou)))
