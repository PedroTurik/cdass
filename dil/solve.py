with open('input.txt') as f:
    dil = f.readline()



stack = []
trash_count = 0
total = 0
trash = False
bang = False
for c in dil:
    if bang:
        bang = False
        continue


    if trash:
        if c == '!':
            bang = True
            continue
        
        trash_count += 1

        if c == '>':
            trash_count -= 1
            trash = False
        
        continue


    if c == '<':
        trash = True
        continue

    if c == '{':
        stack.append('{')
        continue

    if c == '}':
        total += len(stack)
        stack.pop()
    


print(total, trash_count)