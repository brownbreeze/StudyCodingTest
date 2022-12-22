def solution(n):
    a_1 = 1
    a_2 = 2
    answer = 0
    for i in range(2,n):
        answer = (a_1+a_2)%1000000007
        a_1=a_2
        a_2=answer
    return answer
