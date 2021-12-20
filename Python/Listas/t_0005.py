# https://wiki.python.org.br/ExerciciosListas
#2

v = [10]
i = 0
i2 = 8

while i <= 9:
    v.append(input("N {}: ".format(i+1)))
    i += 1

while i2 < 9:
    print(v[-1], v[-2], v[-3], v[-4], v[-5], v[-6], v[-7], v[-8], v[-9], v[-10])
    i2 += 1

