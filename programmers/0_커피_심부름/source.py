def solution(order):
    answer = 0
    ame = ['iceamericano', 'americanoice', 'hotamericano', 'americanohot', 'americano', 'anything']
    lat = ['icecafelatte', 'cafelatteice', 'hotcafelatte', 'cafelattehot', 'cafelatte']
    
    for od in order:
        if od in ame : 
            answer += 4500
        else:
            answer += 5000
    return answer
