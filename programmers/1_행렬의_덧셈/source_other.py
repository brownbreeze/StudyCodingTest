def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
