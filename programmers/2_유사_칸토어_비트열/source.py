def get_val(n, x):
    n-=1
    if x == 0 :
        return 0
    
    if n == 0:
        if x <= 2:
            return x
        else:
            return x-1
        
    m = x//pow(5,n)
    nmg = x%pow(5,n)
    if m < 2 : 
        return m*pow(4,n) + get_val(n, nmg)
    elif m == 2:
        return 2*pow(4,n) +  get_val(n, nmg)
    else:
        return (m-1)*pow(4,n) + get_val(n, nmg)
        
def solution(n, l, r):

    return get_val(n,r) - get_val(n,l-1)
