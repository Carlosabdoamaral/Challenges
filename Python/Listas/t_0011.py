# https://wiki.python.org.br/ExerciciosListas
#12

i = []
a = []
indice = 0

aluno13 = []
alunoNao13 = []

while indice < 30:
    i.append(int(input("\nIdade aluno {}: ".format(indice))))
    a.append(float(input("Altura do aluno {}: ".format(indice))))
    if i[indice] > 13:
        aluno13.append(" ")
    else:
        alunoNao13.append(" ")
    indice += 1

print("\nTem {} alunos maior(es) que 13 anos".format(len(aluno13)))
print("Tem {} alunos menor(es) que 13 anos".format(len(alunoNao13)))