with open("korea.txt") as f:
    entrada = [x.strip().split("(") for x in f]

korea = []
alergias = []
for i in entrada:
    korean, contains = i[0], i[1].replace(")", "").replace("contains ", "").split(", ")
    korea.append(korean.split())
    alergias.append(contains)

usados = set()
alergias_dict = {}
for idx, receita in enumerate(korea):
    for alergia in alergias[idx]:
        if alergia not in alergias_dict:
            alergias_dict[alergia] = receita
        else:
            aux = alergias_dict[alergia]
            alergias_dict[alergia] = [x for x in aux if x in receita]
ans = set()
for _ in range(30):   
    for alerg, ing in alergias_dict.items():
        if len(ing) == 1:
            usados.add(ing[0])
            ans.add((alerg, ing[0]))
        else:
            alergias_dict[alerg] = [x for x in ing if x not in usados]

ans = list(ans)
ans.sort(key=lambda x: x[0])

for n in ans:
    print(f"{n[1]},", end="")

print()



