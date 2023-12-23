def get_cnt(num):
    cnt = 0
    for i in range(1, num+1):
        if num%i == 0 :
            cnt += 1 
    if cnt % 2== 1:
        return num * -1
    return num
            
def solution(left, right):
    return sum([get_cnt(i) for i in range(left, right+1)])

