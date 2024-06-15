import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def rotate_board(board:list[list[int]],l:int):
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(0,len(board),2**l):
        for j in range(0,len(board[0]),2**l):
            for n in range(2**l):
                for m in range(2**l):
                    new_board[i+n][j+m] = board[i + (2 ** l - 1 - m)][j + n]
    return new_board


def remove_ice(board:list[list[int]],ice:int):
    remove_seq = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                tmp = 0
                for d in range(4):
                    nx,ny = j + dx[d],i+dy[d]
                    if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx]:
                        tmp += 1
                if tmp < 3:
                    remove_seq.append((i,j))
                    ice -= 1
    for y,x in remove_seq:
        board[y][x] -= 1
    return board,ice


def main():
    #총 얼음 수의 개수를 저장할 변수
    ice = 0
    #입력
    #n ^ 2 x n ^ 2크기의 board, q개의 명령 입력
    n,q = map(int,input().split())
    #board
    board = []
    #n ^ 2개의 줄 입력
    for _ in range(2**n):
        #이차원 배열의 하나의 행 입력
        tmp = list(map(int,input().split()))
        #ice에 해당 행의 얼음의 개수 저장
        ice += sum(tmp)
        #board에 행 추가
        board.append(tmp)
    #l -> board를 나누는 기준점, q개의 l 저장
    l_seq = list(map(int,input().split()))
    for i in range(q):
        l = l_seq[i]
        board = rotate_board(board,l)
        board,ice = remove_ice(board,ice)
    print(ice)
    
    count = 0
    visited = [[False for _ in range(2 ** n)] for _ in range(2 ** n)]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            
            if not visited[i][j] and board[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                tmp = 0
                
                while q:
                    y,x = q.popleft()
                    tmp += 1
                    for i in range(4):
                        ny,nx = y + dy[i],x + dx[i]
                        if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and not visited[ny][nx]:
                            if board[ny][nx]:
                                q.append((ny,nx))
                                visited[ny][nx] = True
                count = max(count,tmp)
    
    
    print(count)

if __name__ == "__main__":
    main()