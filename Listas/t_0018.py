# https://wiki.python.org.br/ExerciciosFuncoes
# 6

horaUser = int(input("Digite que horas são: "))
minUser = int(input("Digite que minutos são: "))

def conversor(horaConversor,m):
    if horaConversor >= 12:
        s = horaConversor - 12
        print("Agora são {}:{} PM".format(s,m))
    else:
        print("Agora são {}:{} AM".format(horaConversor,m))
conversor(horaUser, minUser)



while 1==1:
    rep = input("Você deseja inserir outro horário? Sim/Não ")


    while rep.upper() == "SIM" or rep.upper() == "YES":
        horaUser = int(input("\nDigite que horas são: "))
        minUser = int(input("Digite que minutos são: "))


        def conversor(horaConversor, m):
            if horaConversor >= 12:
                s = horaConversor - 12

                print("Agora são {}:{} PM".format(s, m))
            else:
                print("Agora são {}:{} AM".format(horaConversor, m))
        conversor(horaUser, minUser)


        rep2 = input("\nVocê deseja inserir outro horário? Sim/Não ")
        if rep2.upper() == "NÃO":
            break

    else:
        break