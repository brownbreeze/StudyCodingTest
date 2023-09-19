def solution(A,B):
    a_len = len(A)
    fcnt = 0
    arrUp = []

    for i in range(a_len):
        if B[i]:
            arrUp.append(A[i])
            continue 
        
        while True:
            if not arrUp:
                fcnt +=1
                break 
            if arrUp[-1] < A[i]:
                arrUp.pop()
                continue  
            break 
    
    fcnt += len(arrUp)
    return fcnt

