from string import ascii_uppercase
alpha = iter(ascii_uppercase)


with open('input.txt') as f:
    a = [int(a.strip()) for a in f]

mapper = {next(alpha): i for i in a}


def reducer():
    k = max(mapper, key=lambda x: mapper[x])
    if mapper[k] == 1:
        return None
    mapper[k] -= 2
    return k+k

while 