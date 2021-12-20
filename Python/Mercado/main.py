p = int(input("Insira a quantidade de produtos: "))
i = 1
infosProduto = []

while i != (p+1):

    divisao = print(("-"*p), "Produto {}".format(i), ("-"*p))
    p_nome = input("Digite o nome do seu produto: ")
    p_uso = input("Qual é o uso do produto: (Comum, usado ou importado): ")
    p_valor = input("Digite o valor do produto: ")
    p_taxa = input("Digite a taxa: ")
    p_fab = input("Digite a data de fabricação: ")

    infosProduto.append("Nome produto: {} \nUso: {} \nValor: {} \nTaxa: {}\nData de fabricação: {}".format( p_nome , p_uso , p_valor , p_taxa , p_fab))

    print(" ")
    i += 1

i = 0
while i != (p):
    print(" ")
    divisao = print(("-" * p), "Produto {}".format(i+1), ("-" * p))
    print(infosProduto[i])
    i += 1