import time

velocidade = float(input("Digite a sua velocidade atual: "))

while True:
    funcao = str(input("Acelerar / Frear / Parar: "))

    if funcao.upper().strip() == "ACELERAR":
        velocidadeNova = float(input("Acelerar quanto? "))
        print("Ok! Acelerando...")
        time.sleep(2)

        while velocidade != velocidadeNova:
            print("{} KM/h".format(velocidade))
            time.sleep(0.25)
            velocidade += 1
        else:
            print("Sua nova velocidade é {} km/h".format(velocidade))



    elif funcao.upper().strip() == "FREAR":
        velocidadeNova = float(input("Frear quanto? "))
        print("Ok! freando...")
        time.sleep(2)

        while velocidade != (velocidade-velocidadeNova):
            print("{} KM/h".format(velocidade))
            time.sleep(0.25)
            velocidade = velocidade - 1  
        else:
            print("Sua nova velocidade é {} km/h".format(velocidade))



    elif funcao.upper().strip() == "PARAR":
        print("Ok! parando...")
        time.sleep(2)

        while velocidade != -1:
            print("{} KM/h".format(velocidade))
            time.sleep(0.25)
            velocidade = velocidade - 1
        else:
            print("Veículo parado!")
            break