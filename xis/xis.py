pontuação =[]
abertos = []
simbolos = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
pontos = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

with open (".\xises.txt") as file:
    xises = file.readlines()
    for row in xises:
        for letter in row:
            if letter in simbolos.values():
                abertos.append(letter)
            if letter in simbolos.keys():
                if simbolos[letter] == abertos[len(abertos) - 1]:
                    abertos.pop()
                else:
                    pontuação.append(pontos[letter])
                    break
print(sum(pontuação))