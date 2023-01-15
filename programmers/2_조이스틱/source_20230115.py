def go_find(lst, cnt, loc):
    cnt += lst[loc]
    temp = lst[loc]
    lst[loc] = 0
    if sum(lst) == 0:
        lst[loc] = temp
        return cnt
    left = 1
    right = 1
    while lst[loc + right] == 0:
        right += 1
    while lst[loc-left] == 0:
        left += 1
    a = go_find(lst, cnt + right, loc+right)
    b = go_find(lst, cnt + left, loc-left)
    lst[loc] = temp
    return a  if a < b else b

def solution(name):
    lst = [min(ord(n) - ord('A'), ord('Z')- ord(n)+1) for n in name]
    #print(lst)
    cnt = 0 
    loc = 0
    answer = go_find(lst, cnt, loc)
    return answer
