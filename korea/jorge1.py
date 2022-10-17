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

for _ in range(30):   
    for alerg, ing in alergias_dict.items():
        if len(ing) == 1:
            usados.add(ing[0])
            continue
        else:
            alergias_dict[alerg] = [x for x in ing if x not in usados]
contador = 0
for receita in korea:
    for ingrediente in receita:
        if ingrediente not in usados: contador+=1

print(contador) 
