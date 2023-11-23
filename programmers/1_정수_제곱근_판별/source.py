import math
def solution(n):
    answer = math.sqrt(n)
    if answer%1 != 0.0 :
        return -1
    return (answer+1)*(answer+1)
