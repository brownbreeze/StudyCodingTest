def go(A,B):
    max_num = max(A)
    i = 0
    while True:
        i+=1
        if max_num%i !=0:
            continue
        if max_num//2 < i:
            break
        num = max_num//i
        temp_list = [a%num for a in A if a%num==0]
        if len(temp_list) == len(A):
            temp_list = [b%num for b in B]
            if 0 not in temp_list:
                return num
    return 0

def solution(arrayA, arrayB):
    return max(go(list(set(arrayA)), list(set(arrayB))),go(list(set(arrayB)), list(set(arrayA))))
