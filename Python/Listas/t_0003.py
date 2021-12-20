# Stones on the Table
# https://codeforces.com/problemset/problem/266/A
# "N" stones on the table
# As pedras podem ser: Vermelha(R), Verde(G), Azul(B)
# Conte o número mínimo de pedras a serem retiradas da mesa para que
# quaisquer duas pedras vizinhas tenham cores diferentes.
# As pedras em uma fileira são consideradas vizinhas se não houver outras pedras entre elas

n = int(input())
s = str(input())
i = n-1

if s[0]!=s[(0+2)]:
	print(1)
i += 1

if s[0]==s[(0+1)]:
	print(n-1)

if s[0]!=s[(0+1)]:
	print(0)