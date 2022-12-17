def solution(citations):
    citations.sort(reverse=True)
    print(list(enumerate(citations, start=1)))

    a = list(map(min, enumerate(citations, start=1)) ) 
    print(a)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
