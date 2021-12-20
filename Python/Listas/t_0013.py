# https://wiki.python.org.br/ExerciciosListas
# 17

a = str(input("Atleta: "))
s = []
i = 0

while i < 1:
    s.append(float(input("Salto 1: ")))
    s.append(float(input("Salto 2: ")))
    s.append(float(input("Salto 3: ")))
    s.append(float(input("Salto 4: ")))
    s.append(float(input("Salto 5: ")))
    i += 1

total_saltos = s[0] + s[1] + s[2] + s[3] + s[4]

print("\nResultado final: ")
print("Atleta: {}".format(a))
print("Saltos: {} - {} - {} - {} - {}".format(s[0], s[1], s[2], s[3], s[4]))
print("Média dos saltos: {}".format(total_saltos / 5))