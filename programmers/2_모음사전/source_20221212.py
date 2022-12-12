info = ['A','E','I','O','U']
total_cnt = 0
def go_word(word, data):
    global info, total_cnt
    if word == data: return True
    if len(data) >= 5: return False
    for i in range(5):
        total_cnt += 1
        temp = go_word(word, data+info[i])
        if temp == True: return True
    return False
    
def solution(word):
    data = ''
    go_word(word, data)
    global total_cnt
    return total_cnt
