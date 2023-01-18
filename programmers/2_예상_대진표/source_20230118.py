import math
def solution(n,a,b):
    answer = int(math.log2(n))
    f_pos = 1
    l_pos = n
    while True:
        middle = f_pos + int((l_pos - f_pos)/2)
        if a in range(f_pos, middle+1) and b in range(f_pos, middle+1):
            l_pos = middle
        elif a in range(middle+1, l_pos+1) and b in range(middle+1, l_pos+1):
            f_pos = middle
        else:
            break
        answer -= 1
        n = n//2
    return answer
