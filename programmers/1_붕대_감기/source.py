def solution(bandage, health, attacks):
    max_h = health
    b1,b2,b3 = bandage
    cnt = len(attacks)
    i = 0
    t = 0 
    at_st = 0
    while i<cnt:
        # print(health, at_st)
        t+=1
        if attacks[i][0] == t:
            at_st = 0
            health -= attacks[i][1]
            if health <= 0:
                return -1
            i+=1
            continue
        health += b2
        at_st += 1
        if health > max_h:
            health = max_h
        if at_st == b1:
            health += b3
            at_st = 0
        if health > max_h:
            health = max_h
        
    return health
