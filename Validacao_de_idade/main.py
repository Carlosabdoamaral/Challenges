'''
O objetivo é que o usuário tenha mais do que 18 anos para poder
acesar o site
'''

nomeUser = str(input("Digite o seu nome: "))
idadeUser = int(input("Digite a sua idade: "))
idadeApp = 18

if idadeUser < 18:
    print("Você não pode acessar o site ainda...")
    print("Tente novamente em {} anos".format(idadeApp-idadeUser))
else:
    print("Acesso permitido")
    