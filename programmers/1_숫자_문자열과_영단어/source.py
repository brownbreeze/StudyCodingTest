def solution(s):
    answer = []
    i = 0
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while True:
        if i >= len(s): break
        ch = s[i]
        if ord(ch) in range(ord('a'),ord('z')+1):
            # alpha 
            val = 0
            for word in words:
                l = len(word)
                if s[i:i+l] == word:
                    val = words.index(word)
                    i+=l
                    i-=1
            answer.append(str(val))
        else:
            answer.append(str(ch))
        i+=1
        
    return int(''.join(answer))
