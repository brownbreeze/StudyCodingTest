def solution(n, words):
    answer = []
    n_set = set()
    i = 0
    len_words = len(words)
    last_alpha = ''
    while i<len_words:
        n_idx = int(i % n)
        w_idx = int(i % len_words)
        if words[w_idx] in n_set:
            return [n_idx+1, (i+1)//n]
        n_set.add(words[w_idx])
        if last_alpha == '':
            last_alpha = words[w_idx][-1]
            i+=1
            continue
        if last_alpha != words[w_idx][0]:
            i+=1
            return [n_idx+1, (i+1)//n]
        last_alpha = words[w_idx][-1]
        i+=1
    return [0, 0]
