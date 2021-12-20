# https://wiki.python.org.br/ExerciciosFuncoes
# 5

def somaImposto(taxaImposto, custo):
    r = custo*taxaImposto
    print("Valor final: {}".format(r))

somaImposto(custo= float(input("Custo: ")) , taxaImposto= float(input("Taxa do imposto: ")))