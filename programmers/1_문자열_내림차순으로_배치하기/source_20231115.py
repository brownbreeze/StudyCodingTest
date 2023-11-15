def solution(s):
    answer = [*s]
    answer.sort(key=lambda x : (ord(x)<65, x), reverse=True)
    return ''.join(answer)
