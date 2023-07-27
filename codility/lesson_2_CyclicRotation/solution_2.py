def solution(A, K):
    result = list()
    alen = len(A)
    if alen == 0:
        return result
    K = (K%alen) * -1
    for i in range(alen):
        result.append(A[(K+i)])
    return result
