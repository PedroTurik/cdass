with open("planeta-77.txt") as f:
    entrada = f.readlines()

expressões = []
for row in entrada:
    expressões.append(row.strip())


for x in expressões:
    open = []
    close = []
    for i, c in enumerate(x):
        if c == "(":
            open.append(i)
        elif c == ")":
            close.append(i)
print(open, close)
            

            




        


