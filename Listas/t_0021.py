# Code force - Bit ++
# https://codeforces.com/problemset/problem/282/A

lines = int(input("Número de linhas: "))
x = 0
i = 0

while i < lines:
    op = input("")

    if op.upper() == "++X":
        x += 1
    elif op.upper() == "--X":
        x -= 1
    i += 1


print(x)