from math import inf
from queue import PriorityQueue

PLAYER_HP = 50
PLAYER_MANA = 500

BOSS_DAMAGE = 10
BOSS_HP = 71

MM_DAMAGE = 4
MM_COST = 53

D_DAMAGE = 2
D_COST = 73

S_ARMOR = 7
S_COST = 113
S_DURATION = 6

P_DAMAGE = 3
P_COST = 173
P_DURATION = 6

R_GAIN = 101
R_COST = 229
R_DURATION = 5






queue = PriorityQueue()
# estrutura da tupla = (mana_spent, boss_hp, s_timer, p_timer, r_timer, player_hp, player_mana)
queue.put((0, BOSS_HP, 0, 0, 0, PLAYER_HP, PLAYER_MANA, tuple()))

seen = set()
less_mana = +inf



def boss_turn(mana_spent, boss_hp, s_timer, p_timer, r_timer, player_hp, player_mana, plays, play):
    if p_timer:
        boss_hp -= P_DAMAGE
        p_timer -= 1
    if r_timer:
        player_mana += R_GAIN
        r_timer -= 1

    if s_timer:
        player_hp -= (BOSS_DAMAGE - S_ARMOR)
        s_timer -= 1
    else:
        player_hp -= BOSS_DAMAGE


    return (mana_spent, boss_hp, s_timer, p_timer, r_timer, player_hp, player_mana), tuple(list(plays) + [play])


while queue.not_empty:
    mana_spent, boss_hp, s_timer, p_timer, r_timer, player_hp, player_mana, plays = queue.get()
    if s_timer:
        s_timer -= 1
    if p_timer:
        boss_hp -= P_DAMAGE
        p_timer -= 1
    if r_timer:
        player_mana += R_GAIN
        r_timer -= 1
    

    if boss_hp <= 0:
        print(plays)
        break
        

    if player_hp <= 0 or player_mana < 53:
        continue

    
    if not s_timer and player_mana >= S_COST:
        info, pp = boss_turn(mana_spent+S_COST, boss_hp, S_DURATION, p_timer, r_timer, player_hp, player_mana-S_COST, plays, "s")
        if info not in seen:
            seen.add(info)
            queue.put(info + (pp,))

    if not p_timer and player_mana >= P_COST:
        info, pp = boss_turn(mana_spent+P_COST, boss_hp, s_timer, P_DURATION, r_timer, player_hp, player_mana-P_COST, plays, 'p')
        if info not in seen:
            seen.add(info)
            queue.put(info + (pp,))

    if not r_timer and player_mana >= R_COST:
        info, pp = boss_turn(mana_spent+R_COST, boss_hp, s_timer, p_timer, R_DURATION, player_hp, player_mana-R_COST, plays, 'r')
        if info not in seen:
            seen.add(info)
            queue.put(info + (pp,))
    
    if player_mana >= MM_COST:
        info, pp = boss_turn(mana_spent+MM_COST, boss_hp-MM_DAMAGE, s_timer, p_timer, r_timer, player_hp, player_mana-MM_COST, plays, 'm')
        if info not in seen:
            seen.add(info)
            queue.put(info + (pp,))
    
    if player_mana >= D_COST:
        info, pp = boss_turn(mana_spent+D_COST, boss_hp-D_DAMAGE, s_timer, p_timer, r_timer, player_hp+(2 if boss_hp >=2 else 1), player_mana-D_COST, plays, 'd')
        if info not in seen:
            seen.add(info)
            queue.put(info + (pp,))
            

    
    
        

        


print("IT ENDED POGGERS")
