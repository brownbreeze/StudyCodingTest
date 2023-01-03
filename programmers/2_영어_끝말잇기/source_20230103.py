def solution(n, words):
    answer = []
    n_set = set()
    i = 0
    len_words = len(words)
    last_alpha = ''
    while i<len_words:
        n_idx = int(i % n)
        w_idx = int(i % len_words)
        #print(i, words[w_idx], last_alpha)
        if words[w_idx] in n_set:
            return [n_idx+1, (i+1)//n]
        n_set.add(words[w_idx])
        i+=1
        if last_alpha == '':
            last_alpha = words[w_idx][-1]
            continue
        if last_alpha != words[w_idx][0]:
            #print('wrong~')
            return [n_idx+1, (i)//n+1]
        last_alpha = words[w_idx][-1]
    return [0, 0]
