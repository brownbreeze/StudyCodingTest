def go(A,B, debug=False):
    max_num = max(A)
    min_num = min(A)
    i = 0
    while True:
        if debug :
            print(i)
        i+=1
        if max_num%i !=0:
            if debug :
                print(f'- skip : max_num % i({i}) = {max_num%i} ')
            continue
        if max_num//2 < i:
            if debug :
                print(f'- stop ')
            break
        num = max_num//i
        for a in A:
            if a%num !=0: break
        else:
            for b in B:
                if b%num == 0:
                    if debug :
                        print(f'- skip :num({num}) is divided in B({b})')
                    break
            else:
                return num
            continue
        if debug :
            print(f'- skip :num({num}) is not divided in A')
    return 0

def solution(arrayA, arrayB):
    answer = 0
    
    a = go(arrayA, arrayB, False)
    b = go(arrayB, arrayA, False)
    return max(a,b)

