def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        val = arr1[i] | arr2[i]
        li = []
        for _ in range(n):
            if val%2==0:
                li.append(' ')
            else:
                li.append('#')
            val = val >> 1
        li.reverse()
        answer.append(''.join(li))
    return answer
