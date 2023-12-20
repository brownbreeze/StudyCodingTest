def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))

