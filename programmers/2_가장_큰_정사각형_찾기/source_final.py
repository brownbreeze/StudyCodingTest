#20221206
def solution(board):
    answer = 0
    temp = list()

    row_size = len(board)
    col_size = len(board[0])
    if row_size == 1 and col_size == 1:
        return board[0][0]
    """
    효율성 테스트 (1)
        테스트 1 〉	통과 (817.89ms, 31.1MB)
        테스트 2 〉	통과 (779.16ms, 30.7MB)
        테스트 3 〉	통과 (776.17ms, 30.8MB)
    """
    for r in range(1,row_size):
        for c in range(1,col_size):
            """
            효율성  테스트 (4)
                테스트 1 〉	통과 (540.11ms, 31MB)
                테스트 2 〉	통과 (512.26ms, 30.5MB)
                테스트 3 〉	통과 (510.23ms, 30.8MB)
            """
            # if r-1 < 0 : continue
            # if c-1 < 0 : continue
            
            # 효율성 테스트에서 약 100ms 줄어들음..; 이건 왜지..? ㅠ,ㅠ;; continue로 min 수행을 안하면 좋은거 아니였나? 
            """
            효율성  테스트 (5)
                테스트 1 〉	통과 (380.57ms, 31.1MB)
                테스트 2 〉	통과 (389.52ms, 30.7MB)
                테스트 3 〉	통과 (421.81ms, 30.9MB)
            """
            # if board[r-1][c] == 0 or board[r][c-1] == 0 or board[r][c] == 0 : continue
            if board[r][c] == 0 : continue
            # 효율성 테스트에서 약 100ms 미만 줄어들음 
            """
            효율성  테스트 (2)
                테스트 1 〉	통과 (748.07ms, 31.1MB)
                테스트 2 〉	통과 (776.75ms, 30.7MB)
                테스트 3 〉	통과 (775.61ms, 30.8MB)
            """
            # if board[r-1][c] == board[r][c-1] and board[r-1][c]==board[r-1][c-1]:
            #     board[r][c] = board[r-1][c] + 1
            # else:
            #     board[r][c] = min(board[r-1][c], board[r][c-1], board[r-1][c-1]) + 1
            board[r][c] = min(board[r-1][c], board[r][c-1], board[r-1][c-1]) + 1
            # 효율성 테스트에서 약 100ms 미만 줄어들음 
            """
            효율성  테스트 (3)
                테스트 1 〉	통과 (565.74ms, 31.1MB)
                테스트 2 〉	통과 (592.63ms, 30.6MB)
                테스트 3 〉	통과 (589.83ms, 31MB)
            """
            #answer = max(answer, board[r][c])
            if answer < board[r][c]:
                answer = board[r][c]
    return answer**2

