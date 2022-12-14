def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    answer = 0
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
        #print(i, set_reserve, set_lost)
    return n-len(set_lost)
