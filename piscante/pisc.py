with open("pisc.txt") as f:
    entrada = [b.strip() for b in f.readlines()]

quadro = []
contador = 0
for row in entrada:
    quadro.append([int(c) for c in row])

cont = 0
def pisc_adjacente(y, x):
    global cont
    cont += 1
    Lx = [x, x-1, x+1]
    Ly = [y, y-1, y+1]
    for y1 in Ly:
        for x1 in Lx:
            if y1 <0 or y1 >= len(quadro) or x1< 0 or x1 >= len(quadro[0]):
                continue
            else:
                quadro[y1][x1] += 1
                if quadro[y1][x1] == 10:
                    pisc_adjacente(y1, x1)
            
for i in range(100):
    coordenadas = []
    for y in range(10):
        for x in range(10):
            quadro[y][x] += 1
            if quadro[y][x] == 10:
                coordenadas.append((y,x))

    for y, x in coordenadas:
        pisc_adjacente(y, x)

    for y in range(10):
        for x in range(10):
            if quadro[y][x] > 9:
                quadro[y][x] = 0


print(cont)

