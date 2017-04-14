def divisores(n):
    divisores = []
    for x in range(2, n):
        if n % x == 0:
            divisores += [x]
    return divisores

def consoantes(s):
    consoantes = []
    consoantes_teste = "bcdfghjklmnpqrstvwxyz"
    for x in s:
        if x in consoantes_teste:
            if x not in consoantes:
                consoantes += [x]
    return consoantes

def comuns(a, b):
    comuns = []
    for x in a:
        if x in b:
            b.remove(x)
            comuns += [x]
    return comuns

def naocomuns(a,b):
    naoComuns = []
    for x in a:
        if x not in b:
            naoComuns += [x]
    for x in b:
        if x not in a:
            naoComuns += [x]
    return naoComuns

print divisores(12)
print consoantes("papagaio")
print comuns([1, 2, 2], [2, 2, 2, 3])
print naocomuns([1,2],[2,2,3,3])
