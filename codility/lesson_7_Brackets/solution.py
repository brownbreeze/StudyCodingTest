def solution(S):

    open_s = ['{', '[', '(']
    close_s = ['}', ']', ')']
    stack = []
    for s in S:
        if s in close_s: 
            if len(stack) == 0 : return 0 
        
            if stack[-1] == close_s.index(s):
                stack.pop()
            else : 
                return 0
        elif s in open_s : 
            stack.append(open_s.index(s))
        # print(stack)

    if len(stack) == 0 :
        return 1
    else : 
        return 0
