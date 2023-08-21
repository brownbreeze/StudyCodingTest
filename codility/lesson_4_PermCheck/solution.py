def solution(A):
    A.sort()
    if A[-1] == len(A):
        return 1
    else:
        return 0
