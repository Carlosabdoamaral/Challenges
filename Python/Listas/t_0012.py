# https://wiki.python.org.br/ExerciciosListas
# 14

p = []
i = 0

while i < 1:
    p.append(str(input("Telefonou para a vítima? "))) #0
    p.append(str(input("Esteve no local no crime? "))) #1
    p.append(str(input("Mora perto da vítima? "))) #2
    p.append(str(input("Devia para a vítima? "))) #3
    p.append(str(input("Já trabalhou com a vítima? "))) #4
    i += 1

y = []
n = []

if p[0].upper() == "SIM" or p[0].upper() == "YES":
    y.append("Pergunta 1")
if p[0].upper() == "NÃO" or p[0].upper() == "NAO" or p[0].upper() == "NO":
    n.append("Pergunta 1")

if p[1].upper() == "SIM" or p[1].upper() == "YES":
    y.append("Pergunta 2")
if p[1].upper() == "NÃO" or p[1].upper() == "NAO" or p[1].upper() == "NO":
    n.append("Pergunta 2")

if p[2].upper() == "SIM" or p[2].upper() == "YES":
    y.append("Pergunta 3")
if p[2].upper() == "NÃO" or p[2].upper() == "NAO" or p[2].upper() == "NO":
    n.append("Pergunta 3")

if p[3].upper() == "SIM" or p[3].upper() == "YES":
    y.append("Pergunta 4")
if p[3].upper() == "NÃO" or p[3].upper() == "NAO" or p[3].upper() == "NO":
    n.append("Pergunta 4")

if p[4].upper() == "SIM" or p[4].upper() == "YES":
    y.append("Pergunta 4")
if p[4].upper() == "NÃO" or p[4].upper() == "NAO" or p[4].upper() == "NO":
    n.append("Pergunta 4")

if len(y) == 1:
    print("Suspeita")

elif len(y) == 2:
    print("Cúmplice")

elif len(y) == 3:
    print("Cúmplice")

elif len(y) == 4:
    print("Cúmplice")

elif len(y) == 5:
    print("Assasino")
else:
    print("Inocente")