import random

##################################
##################################

def dados(x,y):
    v1 = x
    v2 = y
    vf = x + y

    print("\nTentativa")
    print("Dado 1: {}".format(x))
    print("Dado 2: {}".format(y))

    if vf == 7 or vf == 11:
        print("Você é um natural e ganhou")
        exit()

    elif vf == 2 or vf == 3 or vf == 12:
        print("Você é um craps e perdeu")
        exit()

    else:
        while vf == 4 or vf == 5 or vf == 6 or vf == 7 or vf == 8 or vf == 9:
            dados(random.randint(1,6), random.randint(1,6))


dados(
    random.randint(1,6),
    random.randint(1,6)
)

##################################
##################################