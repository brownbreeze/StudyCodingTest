from collections import deque
def solution(n, lost, reserve):
    idx,r = 0,0
    lost.sort()
    reserve.sort()
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    reserve = deque(reserve)
    l = 0 
    r = 0 
    while True:
        if l == len(lost) or r==len(reserve): break
        if lost[l]-1 == reserve[r] or lost[l]+1 == reserve[r]:
            idx += 1
            l += 1
            r += 1
        elif lost[l]+1 < reserve[r]:
            l += 1
        elif lost[l]-1 > reserve[r]:
            r += 1
    return n - len(lost) + idx
