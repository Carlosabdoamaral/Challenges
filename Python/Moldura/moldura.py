'''
Caracteres:

--
++
||

'''

def moldura(colunas, linhas):
    if colunas > 20:
        colunas = 20
    else:
        colunas = colunas
    if linhas > 20:
        linhas = 20
    else:
        linhas = linhas

    i = 0

#Fazendo as linhas em cima
    while i == 0:
        print("+", ("_"*linhas), "+")
        i += 1

#Fazendo as colunas
    #Para fazer um quadrado perfeito divide as colunas por 2 (colunas/2)
    while i <= colunas:
        print(("|" + (" " * (linhas + 2)) + "|"))
        i += 1

#Fazendo as linhas em baixo
    i = 0
    while i == 0:
        print("+", ("_"*linhas), "+")
        i += 1

moldura(
    int(input("Colunas: ")),
    int(input("Linhas: "))
)