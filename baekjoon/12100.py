import sys
from copy import deepcopy
input = sys.stdin.readline

def move(dir,board):
    global n
    #동쪽
    if dir == 0:
        #y값 순회
        for i in range(n):
            #제일 오른 쪽 포인트
            p = n - 1
            #오른쪽부터 차례대로 순회
            for j in range(n-2,-1,-1):
                #board의 값이 0이 아닐때만
                if board[i][j]:
                    #임시 변수에 board[i][j](현재 값) 저장
                    tmp = board[i][j]
                    #현재 값은 옮길 것이므로 현재 위치는 0으로
                    board[i][j] = 0
                    #오른쪽 포인트가 0값이면
                    if board[i][p] == 0:
                        #그 자리에 현재 값 삽입
                        board[i][p] = tmp
                    #오른쪽 값이 현재 값과 같다면
                    elif board[i][p] == tmp:
                        # 2를 곱해주고 저장
                        board[i][p] = tmp*2
                        #한 번의 이동에 한번만 합쳐질 수 있으므로 포인트 왼쪽으로 이동
                        p -= 1
                    #포인트에 있는 값과 다를 때
                    else:
                        #포인트 왼쪽으로 이동 후
                        p -= 1
                        #전 포인트 값 왼쪽에 삽입
                        board[i][p] = tmp
    #서쪽
    elif dir == 1:
        for i in range(n):
            p = 0
            for j in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][p] == 0:
                        board[i][p] = tmp
                    elif board[i][p] == tmp:
                        board[i][p] = tmp*2
                        p+=1
                    else:
                        p += 1
                        board[i][p] = tmp
    #남쪽
    elif dir == 2:
        for i in range(n):
            p = n - 1
            for j in range(n-2,-1,-1):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[p][i] == 0:
                        board[p][i] = tmp
                    elif tmp == board[p][i]:
                        board[p][i] = tmp * 2
                        p -= 1
                    else:
                        p -= 1
                        board[p][i] = tmp
    #북쪽
    elif dir == 3:
        for i in range(n):
            p = 0
            for j in range(1,n):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[p][i] == 0:
                        board[p][i] = tmp
                    elif tmp == board[p][i]:
                        board[p][i] = tmp * 2
                        p+=1
                    else:
                        p += 1
                        board[p][i] = tmp
    return board

#
def dfs(board,count):
    global ans
    global n
    #이동횟수가 5번이면
    #board 탐색하며 최고값 갱신
    if count == 5:
        for i in range(n):
            for j in range(n):
                ans = max(board[i][j],ans)
        return
    #동 서 남 북 으로 검색
    for i in range(4):
        tmp_board = move(i,deepcopy(board))
        dfs(tmp_board,count+1)



if __name__ == "__main__":
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    dfs(board,0)
    print(ans)