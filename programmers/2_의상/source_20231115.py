def solution(clothes):
    answer = 1
    hash_map = {}
    for c, t in clothes:
        if t in hash_map:
            hash_map[t].append(c)
        else:
            hash_map[t] = [c]
    # print(hash_map)
    for m in hash_map:
        # print(m)
        answer *= (1+len(hash_map[m]))
    
    return answer - 1
