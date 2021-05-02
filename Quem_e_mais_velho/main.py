n = []
i = []

indice = 1

while indice < 3:
    print("\nDados da pessoa {}".format(indice))
    n.append(str(input("Nome: ")))
    i.append(int(input("idade: ")))
    indice +=1

if i[0] > i[1]:
    print("\nA pessoa mais velha é: {}".format(n[0]))
elif i[1] > i[0]:
    print("\nA pessoa mais velha é: {}".format(n[1]))
elif i[0] == i[1]:
    print("\nAs duas pessoas possuem a mesma idade")