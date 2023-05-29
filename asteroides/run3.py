from queue import PriorityQueue


with open('input3.txt') as f:
    shield = int(f.readline())
    laser = [(1 if x == 'c' else 0) for x in f.readline()]


def count_damage(laser):
    total = 0
    cur_dmg = 1
    for i in laser:
        if i == 'C':
            cur_dmg *= 2
        else:
            total += cur_dmg
    return total

queue = PriorityQueue()
queue.put((count_damage(laser), laser, 0))
seen = set()
counter = 0
while queue:
    counter +=1
    dmg, laser, hacks = queue.get()
    if counter == 2:
        print(laser)
        break
    if dmg <= 40:
        print(hacks)
        break

    for i in range(len(laser) - 1):
        if laser[i] != laser[i+1]:
            laser[i], laser[i+1] = laser[i+1], laser[i]
            queue.put((count_damage(laser), laser.copy(), hacks + 1))
            laser[i], laser[i+1] = laser[i+1], laser[i]


