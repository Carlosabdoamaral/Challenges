n = []
s = []
i = 1

while i < 3:
    print("\nDados do funcionário {}".format(i))
    n.append(str(input("Nome: ")))
    s.append(float(input("Salário: ")))
    i += 1

print("\nSalário médio: {:.3f}".format( (s[0] + s[1])/2 ))