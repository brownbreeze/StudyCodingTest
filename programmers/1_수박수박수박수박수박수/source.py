def solution(n):
    soobak = '수박'
    return ''.join([soobak[i%2] for i in range(n)])
