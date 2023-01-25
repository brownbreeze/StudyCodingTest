def get_w(msg, words, i):
    for j in range(len(msg), i,-1):
        if msg[i:j] in words:
            return j-i, words.index(msg[i:j])+1
    return -1,-1 # error 

def solution(msg):
    answer = []
    
    word_alpha = [chr(i) for i in range(65,65+26) ]
    i = 0
    
    while True:
        if i >= len(msg) : break
        w_len, w_idx = get_w(msg, word_alpha, i) # i의 위치에서 가장 긴 문자열 w가져오기 
        if w_len == -1 and w_idx == -1 : 
            return [] # error 
        answer.append(w_idx)
        word_alpha.append(msg[i:i+w_len+1])
        i += w_len
    return answer
