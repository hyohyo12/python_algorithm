import sys
from copy import deepcopy
input = sys.stdin.readline
res = 0
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,-1,1,1,1,0,-1]


def move_fish(board: list[list[int]],fish: list[int]):
    for data in fish:
        if data == 0:
            continue
        y,x = data
        for _ in range(9):
            d = board[y][x][1]
            ny = y + dy[d]; nx = x + dx[d]
            if not 0 <= ny < 4 or not 0 <= nx < 4 or board[ny][nx] == 's':
                board[y][x][1] = (board[y][x][1] + 1) % 8
                continue
            if board[ny][nx]:
                fish[board[ny][nx][0]] = (y,x)
            else:
                fish[board[y][x][0]] = 0
            board[ny][nx],board[y][x] = board[y][x],board[ny][nx]
            fish[board[ny][nx][0]] = (ny,nx)
            break
    return (board,fish)



def dfs(board:list[list[int]],cur:int,y:int,x:int,dir:int,fish:list[int]):
    global res
    board,fish = move_fish(board,fish)
    nx = x; ny = y
    while True:
        nx = nx + dx[dir]; ny = ny + dy[dir]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            res = max(res,cur)
            return
        if not board[ny][nx]:
            continue
        c_board = deepcopy(board)
        c_fish = deepcopy(fish)
        board[y][x] = 0
        a,b = board[ny][nx]
        board[ny][nx] = 's'
        fish[a] = 0
        dfs(board,cur+a,ny,nx,b,fish)
        board = c_board
        fish = c_fish

def main():
    fish = [0 for _ in range(17)]
    board = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        temp = list(map(int,input().split()))
        for j in range(4):
            board[i][j] = [temp[j*2],temp[j*2+1]-1]
            fish[temp[j*2]] = (i,j)
    fish[board[0][0][0]] = 0
    tmp = board[0][0][0]
    dir = board[0][0][1]
    board[0][0] = 's'
    board,fish = move_fish(board,fish)
    dfs(board,tmp,0,0,dir,fish)
    print(res)

if __name__ == "__main__":
    main()