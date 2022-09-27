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

dic_blabla = {}
for allergy in todas_alergias:
    blabla = set()
    for h in range(len(possibilidades)):
        if possibilidades[h][0] == allergy:
            if len(blabla) == 0:
                blabla = possibilidades[h][1]
            else:
                blabla = blabla.intersection(possibilidades[h][1])
            dic_blabla[allergy] = blabla

dic_final = {}

for f in dic_blabla:
    set_tmp = dic_blabla[f]
    for b in dic_blabla:
        if b == f:
            continue
        set_tmp = set_tmp - dic_blabla[b]
    dic_final[f] = set_tmp
print(dic_final)
    

        

    







