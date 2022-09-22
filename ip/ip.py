lista = []
candidatos = []
falhas = []
with open ("iplista.txt") as ipfile:
    iplista = ipfile.readlines()
    for row in iplista:
        lista.append(row.split("-"))
    for intervalo in lista:
        candidatos.append(int(intervalo[1]) + 1)
candidatos.sort()
for candidato in candidatos:
    for inter in lista:
        if candidato >= int(inter[0]) and candidato <= int(inter[1]):
            falhas.append(candidato)
            break

for falha in falhas:
    candidatos.remove(falha)

print(candidatos[0])