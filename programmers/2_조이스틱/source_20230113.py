def solution(name):
    lst = [min(ord(n) - ord('A'), ord('z')- ord(n)+1) for n in name]
    print(lst)
    cnt = 0 
    loc = 0
    while True:
        cnt += lst[loc]
        lst[loc] = 0
        if sum(lst) == 0:
            break
        left = 1
        right = 1
        while lst[loc + right] == 0:
            right += 1
        while lst[loc-left] == 0:
            left += 1
        if left >= right :
            loc += right
            cnt += right
        else :
            loc -= left
            cnt += left
        
    return cnt
