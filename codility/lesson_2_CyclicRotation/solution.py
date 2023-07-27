# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    result = list()
    alen = len(A)
    K = (K%alen) * -1
    for i in range(alen):
        result.append(A[(K+i)])
    return result
