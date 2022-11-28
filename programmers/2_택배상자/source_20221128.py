def solution(order):
    answer = 0
    i = 0
    belt = list()
    while True:
        if order[i] == 1: break
        belt.append(order[i])
        i += 1
    i += 1
    pos = 2
    
    if i < len(order) and order[i] == pos:
        while True:
            if i<len(order) and order[i] == pos:
                pos += 1
                i +=1
                continue
            break
    elif len(belt) > 0 and belt[-1] == pos:
        while True:          
            if i<len(order) and order[i] == pos:
                pos += 1
                belt.pop()
                continue
            break        
    print(pos) 
    return pos-1
