# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    len_a = len(A)
    stack = []
    big_size = 0
    for i in range(len_a):
        if B[i] == 0 : 
            stack.append(A[i])
            while True:
                if len(stack) == 0: break
                if stack[-1] < big_size: stack.pop()
                else : break
            
        else:
            if big_size == 0 : 
                big_size = A[i]
                stack.append(A[i])
            else: 
                if big_size > A[i]:
                    continue
        print(stack) 
    
    print(stack)
    return len(stack)
