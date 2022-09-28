import itertools


with open("korea.txt") as f:
    entrada = [x.strip().split("(") for x in f]

korea = []
alergia = []
for i in entrada:
    korean, contains = i[0], i[1].replace(")", "").replace("contains ", "").split(",")
    korea.append(korean)
    alergia.append(contains)

todas_alergias = []
for j in alergia:
    for item in j:
        if item.strip() not in todas_alergias:
            todas_alergias.append(item.strip())
possibilidades = []

for l in todas_alergias:
    for k, receita in enumerate(korea):
        if l in alergia[k]:
            possibilidades.append((l, set(receita.split())))

alergia_ingre = {}
for allergy in todas_alergias:
    blabla = set()
    for h in range(len(possibilidades)):
        if possibilidades[h][0] == allergy:
            if len(blabla) == 0:
                blabla = possibilidades[h][1]
            else:
                blabla = blabla.intersection(possibilidades[h][1])
    alergia_ingre[allergy] = blabla

P = ['mkpmkx', 'flnhl', 'zrvtg', 'tmp', 'vxzpfp', 'ttkn', 'cdslv', 'vzn', 'pdpgm', 'lgtvqf', 'pbln', 'jvjhx', 'dnbhhv', 'lfmng']
ingredientes_ruins = list(itertools.combinations(P , 8))
korea2 = [a.split() for a in korea]

respostas = set()

for tuple in ingredientes_ruins:
    counter = 0
    for a in korea2:
        for ing in a:
            if ing not in tuple:
                counter+=1
    respostas.add(counter)

print(respostas)