def solution(n, k, enemy):
    answer = 0
    nmg_k = k
    for i in range(k, len(enemy)):
        if sum(sorted(enemy[:i])[:-k])>n:
            return i-1
    else:
        return k
    return answer

