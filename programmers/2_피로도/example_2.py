solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
