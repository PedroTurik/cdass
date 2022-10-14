from cmath import inf
impossiveis = set()

with open("sois.txt") as f:
    entrada = [tuple(map(int, x.split(","))) for x in f.readlines()]

def estrela_mais_perto(x,y):
    perto = [+inf, ()]
    for cord in entrada:
        xk, yk = cord
        dist = abs(xk-x)+abs(yk-y)
        if dist < perto[0]:
            perto = [dist, cord]
        elif dist == perto[0]:
            perto.append(cord)
    return perto[1:]

#excluindo impossiveis
for y in range(349):
    for x in [0, 352]:
        for cord in estrela_mais_perto(x, y):
            impossiveis.add(cord)
        
for x in range(353):
    for y in [0, 348]:
        for cord in estrela_mais_perto(x, y):
            impossiveis.add(cord)

sois = {}
for s in entrada:
    sois[s] = 0

for y in range(349):
    for x in range(353):
        A = estrela_mais_perto(x,y)
        if len(A) == 1:
            sois[A[0]] += 1
maior_sist = 0
for sol in sois:
    if sois[sol] > maior_sist and sol not in impossiveis:
        maior_sist = sois[sol]

print(maior_sist)






