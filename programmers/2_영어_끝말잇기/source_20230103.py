def solution(n, words):
    answer = []
    n_set = set()
    i = 0
    len_words = len(words)
    last_alpha = ''
    while i<len_words:
        n_idx = int(i % n)
        if words[i] in n_set:
            return [n_idx+1, (i+1)//n if (i+1)%n==0 else (i+1)//n+1]
        n_set.add(words[i])
        if last_alpha == '':
            last_alpha = words[i][-1]
            i+=1
            continue
        if last_alpha != words[i][0]:
            #i+=1
            return [n_idx+1, (i+1)//n if (i+1)%n==0 else (i+1)//n+1]
        last_alpha = words[i][-1]
        i+=1
    return [0, 0]
