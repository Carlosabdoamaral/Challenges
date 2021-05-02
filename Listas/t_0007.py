# https://wiki.python.org.br/ExerciciosListas
#5

i = 0
n = []
par = []
impar = []


while i < 20:
    n.append(int(input("Digite um número: ")))

    if (n[i] % 2) == 0:
        par.append(n[i])
    else:
        impar.append(n[i])
    i += 1

print(n)
print(par)
print(impar)