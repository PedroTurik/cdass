inst = []
entrada = open("instruc.txt", "r")
for row in entrada:
    inst.append(row)

ns = 1
ew = 10

ns_barco = ew_barco = 0

for i in inst:
    if i[0] == "W":
        ew -= int(i[1:])
    elif i[0] == "N":
        ns += int(i[1:])
    elif i[0] == "E":
        ew += int(i[1:])
    elif i[0] == "S":
        ns -= int(i[1:])
    elif i[0] == "R":
        orientação = int(i[1:])/90
        if orientação == 1:
            tmp = ew
            ew = ns
            ns = tmp*-1
        elif orientação == 2:
            ns = ns*-1
            ew = ew*-1
        elif orientação == 3:
            tmp = ns
            ns = ew
            ew = tmp*-1   
    elif i[0] == "L":
        orientação = int(i[1:])/90
        if orientação == 1:
            tmp = ns
            ns = ew
            ew = tmp*-1
        elif orientação == 2:
            ns = ns*-1
            ew = ew*-1
        elif orientação == 3:
            tmp = ew
            ew = ns
            ns = tmp*-1
    elif i[0] == "F":
        ns_barco += ns*int(i[1:])
        ew_barco += ew*int(i[1:])
        

total = abs(ns_barco) + abs(ew_barco)


print(total)