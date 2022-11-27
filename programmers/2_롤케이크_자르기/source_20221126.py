def solution(topping):
    if len(topping) ==1: return 0
    answer = 0
    left = set()
    right = dict.fromkeys(topping,0)
    for t in topping:
        right[t] += 1
    right_len = len(right)
    
    for i in range(len(topping)):
        left.add(topping[i])
        right[topping[i]] -= 1
        if right[topping[i]] == 0: 
            right_len -= 1 
        if right_len == len(left) :
            answer = answer + 1 
    return answer
