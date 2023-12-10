
def check(pos, n):
    l_dis_x = (pos[0]-1)%3
    l_dis_y = (pos[0]-1)//3
    r_dis_x = (pos[1]-1)%3
    r_dis_y = (pos[1]-1)//3

    n_dis_x = (n-1)%3
    n_dis_y = (n-1)//3
    A = (abs(l_dis_x - n_dis_x) + abs(l_dis_y - n_dis_y))
    B = (abs(r_dis_x - n_dis_x) + abs(r_dis_y - n_dis_y))
    # print(A,B)
    if A > B:
        return 1
    elif A==B:
        return -1
    else:
        return 0
    
def solution(numbers, hand):
    answer = []
    pos = [10,12]
    val = ['L', 'R']
    
    for n in numbers:
        if n == 0 :
            n = 11
        if n in [1,4,7]:
            p = 0
        elif n in [3,6,9]:
            p = 1
        else:
            p = check(pos,n)
        if p == -1:
            if hand == "right":
                p = 1
            else:
                p = 0
        # print(n, p, pos)
        # print()
        pos[p] = n
        
        answer.append(val[p])
    return ''.join(answer)
