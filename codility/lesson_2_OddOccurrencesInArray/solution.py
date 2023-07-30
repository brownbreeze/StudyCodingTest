def solution(A):
    cnt_list = [0 for _ in range(1000000)]

    for a in A:
        cnt_list[a-1]+=1
    
    for i in range(1000000):
        if cnt_list[i]%2==1:
            return i+1
    return 0 
