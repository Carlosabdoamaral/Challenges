import random

def embaralha(txt):
    a = random.sample(txt,len(txt))
    b = random.randint(1000,9999)

    d = ''.join(a)
    e = ''.join(str(b))

    print(d,e)

txt = input('Digite algo: ')
embaralha(txt)

