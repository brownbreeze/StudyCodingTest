
4
5
6
7
8
9
10
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [ [ 1, 2 ], [ 2, 3 ]];
b = [[ 3, 4], [5, 6]];
print("결과 : {}".format(productMatrix(a,b)));
