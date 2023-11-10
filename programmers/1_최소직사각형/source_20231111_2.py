def solution(sizes):
    size_len = len(sizes)
    w_list = []
    h_list = []
    for i in range(size_len):
        w_list.append(min(sizes[i]))
        h_list.append(max(sizes[i]))
    return max(w_list)*max(h_list)

