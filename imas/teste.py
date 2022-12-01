from copy import deepcopy

with open("inp.txt", "r") as f:
    entrada = f.readlines()
    todos_imas = {tuple(map(int, row.strip().split("/"))) for row in entrada}



somas_final = -10000
biggest_size = -10000
longest_soma = -10000

def DFS(state, soma, imas, size):
    global somas_final, biggest_size, longest_soma
    count = 0
    for x, y in imas:
        if x == state:
            send_imas = deepcopy(imas)
            send_imas.remove((x,y))
            DFS(y, x+y + soma, send_imas, size + 1)
            count += 1
        elif y == state:
            send_imas = deepcopy(imas)
            send_imas.remove((x,y))
            DFS(x, x+y + soma, send_imas, size + 1)
            count += 1
    if count == 0:
        if somas_final < soma:
            somas_final = soma
        if biggest_size <= size:
            biggest_size = size
            longest_soma = soma
        
DFS(0, 0, todos_imas, 0)

print(f"{somas_final=}")
print(f"{biggest_size=}")
print(f"{longest_soma=}")
