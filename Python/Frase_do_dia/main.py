# Frases retiradas do perfil: @poetizando.14 (instagram)
import random

frases = []
frases.append("Eu podia ter aproveitado mais")
frases.append("Desejar o mal do outro nunca vai fazer você ficar melhor")
frases.append("Eu não quero ser o melhor do mundo \nEu quero ser melhor do que o eu de ontem")
frases.append("Pessoa bonita é aquela que se ama")
frases.append("O desejado em algum lugar é rejeitado")
frases.append("Pequenas ações tem grander reações")
frases.append("O pensamento tem um poder inimaginável")
frases.append("Foda-se o padrão de beleza, eu sou o meu próprio")

p1 = input("Você quer sortear uma frase? ")

while p1.upper() == "SIM" or p1.upper() == "S" or p1.upper() == "YES" or p1.upper() == "Y" or p1.upper() == "CLARO":
    print(" ")
    print(frases[random.randint(0, (len(frases)-1))])
    print(" ")
    p1 = input("Você quer sortear outra frase? ")
else:
    print("Tudo bem, muito obrigado por entrar no programa")
    pass

exit()
