def get_val(n, x):
    n-=1
    # print(n,x)
    if x == 0 :
        return 0
    
    if n == 0:
        # print('end')
        if x <= 2:
            return x
        else:
            return x-1
        
    m = x//pow(5,n)
    nmg = x%pow(5,n)
    if m < 2 : 
        return m*pow(4,n) + get_val(n, nmg)
    elif m == 2:
        return 2*pow(4,n) # +  get_val(n, nmg)
    else:
        return (m-1)*pow(4,n) + get_val(n, nmg)

def print_k(n):
    if n == 1:
        return '11011'
    s = print_k(n-1)
    answer = ''
    for i in range(len(s)):
        if s[i] == '1':
            answer += '11011'
        else:
            answer += '00000'
    return answer
        
def solution(n, l, r):
    # a = print_k(n)
    # for i in range(0,len(a), 10):
    #     print(a[i:i+10])

    # print(get_val(n,r))
    # print(get_val(n,l-1))
    # return 0
    return get_val(n,r) - get_val(n,l-1)
    
