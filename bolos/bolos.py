with open("bolos.txt") as f:
    bolos = list(map(int,f.readline().split(",")))

idades = [bolos.count(x) for x in range(9)]


for _ in range(150000):
    nasc = idades.pop(0)
    idades.append(nasc)
    idades[6] += nasc

print(sum(idades))