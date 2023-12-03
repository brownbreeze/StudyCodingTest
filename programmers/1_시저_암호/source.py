def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        else: 
            p = 0
            # print(ord(i))
            if ord(i) in range(65, 91):
                if ord(i)+n > 90:      
                    # print('-')
                    p = -26
            elif ord(i) in range(97,123):
                if ord(i)+n > 122:      
                    # print('=')
                    p = - 26
            answer += chr(ord(i)+n+p)
    
    return answer
