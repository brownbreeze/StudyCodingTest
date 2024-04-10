def solution(N, number):
    arr = list()
    temp_arr = list()
    d = dict()

    def push_temp_arr(n, c):
        if n not in temp_arr:
            temp_arr.append(n)
        if n not in d:
            d[n] = c
        elif d[n] > c:
            d[n] = c

    def get_values(a1, a2, c):
        push_temp_arr(a1*a2, c)
        push_temp_arr(a1+a2, c)
        push_temp_arr(a1-a2, c)
        if a2 != 0:
            push_temp_arr(a1//a2, c)

    t = N
    for i in range(8):
        arr.append(t)
        d[t] = (i+1)
        t = t*10 + N
        temp_arr = arr.copy()

        for x in arr:
            for y in arr:
                c = d[x] + d[y]
                if c > 8:
                    break
                get_values(x, y, c)
        arr = temp_arr.copy()

        if number in d and d[number] <= 8:
            return d[number]
    return -1
