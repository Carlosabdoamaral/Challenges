i1 = 18
d1 = "5%"

i2 = 18
d2 = "10%"

i3 = 65
d3 = "15%"

print("SEJA MUITO(A)(E) BEM VINDO(A)(E) À NOSSA LOJA")
nomeUser = str(input("Digite o seu nome: "))
idadeUser = int(input("{} digite a sua idade: ".format(nomeUser)))
valorCompra = float(input("Digite o valor da compra: ".format(nomeUser)))

if idadeUser > i3:
    formula = (valorCompra * 0.85)
    print("Você recebeu {} de desconto!".format(d3))
    print("O valor final da compra foi: {}".format(formula))
elif idadeUser > i2:
    formula = (valorCompra * 0.90)
    print("Você recebeu {} de desconto!".format(d2))
    print("O valor final da compra foi: {}".format(formula))
elif idadeUser < i1:
    formula = (valorCompra * 0.95)
    print("Você recebeu {} de desconto!".format(d1))
    print("O valor final da compra foi: {}".format(formula))


