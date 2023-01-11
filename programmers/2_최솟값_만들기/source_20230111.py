def solution(A,B):
    A.sort()
    B.sort()
    B = B[::-1]
    return sum([a * b for a, b in zip(A, B)]) 
