def solution(s, skip, index):
    no = [s for s in skip]
    val = [chr(97+i)  for i in range(26) if chr(97+i) not in no]
    answer = []
    # print(val)
    for k in s:
        n = val.index(k)
        answer.append(val[(n+index)%len(val)])
    return ''.join(answer)
