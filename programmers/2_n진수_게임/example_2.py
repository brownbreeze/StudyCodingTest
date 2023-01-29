DIGITS = list('0123456789ABCDEF')


def n2base(n, base):
    if n == 0:
        return DIGITS[0]

    # 각 자리수에 해당하는 문자열을 담을 리스트
    digits = []
    while n > 0:
        # 제일 마지막 자리의 숫자 구하기. 예를 들어 1658이면 '8'
        digits.append(DIGITS[n % base])
        # 제일 마지막 자리 제거. 예를 들어 1658이면 165로
        n = int(n // base)

    # 뒤집어서 반환. 예를 들어 '8561'이면 '1658'
    return ''.join(digits[::-1])


def solution(n, t, m, p):
    digits = []
    turn = 0
    while len(digits) < t * m:
        digits += list(n2base(turn, n))
        turn += 1
    return ''.join(digits[p-1::m][:t])
