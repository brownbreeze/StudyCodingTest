def solution(n):
    answer = 0
    fn_1 = 1
    fn_2 = 0
    for i in range(2, n+1):
        answer = (fn_1 + fn_2)%1234567
        fn_2 = fn_1
        fn_1 = answer  
    return answer
