def check(y, x, m):
    go_pos = [[-1,0,1,0],[0,-1,0,1]]
    find_list = list()
    find_list.append([y,x,0])
    while True:
        if len(find_list) == 0: break
        ty, tx, d = find_list.pop()
        if d >= 2: continue
        for i in range(4):
            tty = ty + go_pos[0][i]
            ttx = tx + go_pos[1][i]
            if tty == y and ttx == x : continue
            if tty not in range(5) or ttx not in range(5) : continue
            if m[tty][ttx] == 'X': continue
            if m[tty][ttx] == 'P': return False 
            find_list.append([tty, ttx, d+1])
            # print(find_list)
    return True
            
        

def get_result(place):
    check_persons = list()
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                check_persons.append([i,j])
    for y, x in check_persons:
        if not check(y,x,place):
            return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(get_result(place))
        # break
    return answer
