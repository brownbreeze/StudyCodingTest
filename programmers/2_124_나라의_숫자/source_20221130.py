def get_value_mock(n):
    if n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '4'
    else:
        return '9'
    
def get_value_nmg(n):
    if n == 0 : 
        return '1'
    elif n == 1:
        return '2'
    elif n == 2:
        return '4'
    else:
        return '9'
    
def solution(n):
    answer = ''
    mock = 0 
    nmg = 0 
    if n <=3:
        return get_value_mock(n)
    while True:
        if n <= 3: break
        mock = (n-1)// 3
        nmg = (n-1) % 3
        n = mock
        answer = ''.join([answer, get_value_nmg(nmg)])
    answer = ''.join([answer, get_value_mock(mock)])
    
    return answer[::-1]
