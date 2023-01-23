import math
def get_LCM(n, lelist):
    temp = 0
    i = 2
    if n == 1: 
        lelist[1] = 1
        return lelist
    while True:
        if n == 1: break
        if n % i == 0 :
            n /= i 
            lelist[i]+=1
            i = 2
            continue
        i += 1
    return lelist
        
def solution(arr):
    answer = 0
    least_list = [0 for _ in range(100)] # 0, 1, 2...의 제곱 값
    for ar in arr:
        temp_list = [0 for _ in range(100)] # 0, 1, 2...의 제곱 값
        temp_list = get_LCM(ar, temp_list)
        least_list = [l if l > t else t for l, t in zip(least_list, temp_list)]
    # print(least_list)
    for i in range(len(least_list)):
        if least_list[i]==0 : continue
        if answer == 0 :
            answer = pow(i, least_list[i]) 
            # print(answer)
            continue
        answer *= pow(i, least_list[i])
        # print(answer)
    return answer

