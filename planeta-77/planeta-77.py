import operator

with open("planeta-77.txt") as f:
    entrada = f.readlines()

inp = [x.strip() for x in entrada]
ans=0
operações = {
    '0+' : operator.add,
    '0*' : operator.mul,
    '1+' : operator.add,
    '1*' : operator.mul,
    '2+' : operator.add,
    '2*' : operator.mul,
    '3+' : operator.add,
    '3*' : operator.mul,
    '4+' : operator.add,
    '4*' : operator.mul,
    '5+' : operator.add,
    '5*' : operator.mul,
    '6+' : operator.add,
    '6*' : operator.mul,
    '7+' : operator.add,
    '7*' : operator.mul,
    '8*' : operator.mul,
    '8*' : operator.mul
}

prioridade = ["8*", "8+", "7*", "7+","6*", "6+","5*", "5+","4*", "4+",
"3*", "3+","2*", "2+","1*", "1+","0*", "0+"]

def calculo(expressão):
    if len(expressão) == 3:
        l, op, r = expressão
        return operações[op](l, r)
    else:
        for op_list in prioridade:
            for op in expressão:
                if op == op_list:
                    idx = expressão.index(op)-1
                    result = calculo([expressão.pop(idx) for i in range(3)])
                    expressão.insert(idx, result)
                    return calculo(expressão)


for j in range(len(inp)):
    contador_de_p = 0
    i = 0
    for c in inp[j]:
        if c == "(":
            contador_de_p += 1
        if c == ")":
            contador_de_p -= 1
        if c in ["+", "*"]:
            inp[j] = inp[j][:i] + str(contador_de_p) + inp[j][i:]
            inp[j]
            i += 1
        i += 1
    inp[j] = inp[j].replace("(", "").replace(")", "").split()
    

    ex_atual = []
    for bla in inp[j]:
        try:
            ex_atual.append(int(bla))
        except:
            ex_atual.append(bla)
    resposta_atual = calculo(ex_atual)
    ans += resposta_atual
    

print(ans)




