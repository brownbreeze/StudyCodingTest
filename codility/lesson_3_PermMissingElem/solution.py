def solution(A):
    A = sorted(A)
    left = 0
    right = len(A) -1
    while True:
        idx = left
        if left > right:
            return idx+1
        if A[idx] == idx + 1 :
            left = (right - left)//2 + left + 1
        elif A[idx] != idx + 1 :
            right = (right-left)//2 + left - 1
    return len(A)+1
