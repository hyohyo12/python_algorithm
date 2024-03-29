#https://velog.io/@eunseokim/about

import sys
input = sys.stdin.readline

def find_route(n:int,board:list[list[int]])->int:
    #dp에는 해당 파이프의 끝점이 있는가 없는가를 저장한다.
    #3차원 리스트로 정의 nxn 보드가 3개의 형태로 각각 0 번째 board 는 가로, 1번째 board는 대각선, 2번째 board 는 가로
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
    #전처리 작업(board의 맨 윗줄은 모두 가로만 가능하므로 해당하는 곳에 1저장(파이프의 끝 점 저장.))
    dp[0][0][1] = 1
    for i in range(2,n):
        if board[0][i] == 0:
                dp[0][0][i] = dp[0][0][i-1]
    #모든 경로에 대한 파이프 추가
    for r in range(1,n):
        for c in range(1,n):
            #대각선 파이프의 추가
            #대각선을 추가 하려면 board상 현재 위치,현재위치에서 x축으로 전 위치, 현재위치에서 위 모두 벽이 없어야 한다.
            if board[r][c] == 0 and board[r-1][c] == 0 and board[r][c-1] == 0:
                #대각선 파이프를 배치를 하기위해서 세로의 최적해 가로의 최적해 대각선 최적해가 모두 배치가능하므로 모두 더한것이 현재 위치에서의 최적해이다.
                #(0과 1과 2 번째dp보드를 참고한다.) 
                dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            #가로, 세로 파이프의 추가
            #가로와 세로 파이프를 배치하기 위해서, 현재(파이프의 끝)에 벽이 있어서는 안된다.
            if board[r][c] == 0:
                #가로
                #가로를 배치하기 위해 전 파이프가 대각선, 가로 로 배치되어 있어야만 배치 가능하다(0 또는 1 번째 dp보드 참조)
                dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
                #세로
                #세로 배치 위해서 전 파이프가 대각선, 세로로 배치되어 있어야만 배치 가능하다(1 또는 2 번째 dp보드 참조)
                dp[2][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
                
    return (sum(dp[i][n-1][n-1] for i in range(3)))

def main():
    #메인 함수
    n = int(input())
    
    board = [list(map(int,input().split())) for _ in range(n)]
    
    print(find_route(n,board))


if __name__ == "__main__":
    main()