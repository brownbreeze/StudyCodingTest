def solution(n, words):
    answer = []
    n_set = set()
    if len(set(words)) == len(words): return [0,0]
    i = 0
    len_words = len(words)
    last_alpha = ''
    while True:
        n_idx = i % n
        w_idx = i % len_words
        if words[w_idx] in n_set:
            print(words[w_idx], n_set)
            return [n_idx+1, (i+1)//n]
        n_set.add(words[w_idx])
        if last_alpha == '':
            last_alpha = words[w_idx[-1]]
            continue
        if last_alpha != words[w_idx[0]]
            return [n_idx+1, (i+1)//n]
        print(n_idx, n_set)
        i += 1
    return [0, 0]
