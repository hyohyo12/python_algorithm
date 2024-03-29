import sys
from copy import deepcopy
input = sys.stdin.readline
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill_board(c_board: list[list[int]],dir:list[int],cur_x:int,cur_y:int):
    for i in dir:
        nx,ny = cur_x,cur_y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 > nx or 0 > ny or m <= nx or n <= ny:
                break
            if c_board[ny][nx] == 6:
                break
            elif board[ny][nx] == 0:
                c_board[ny][nx] = '#'
    return c_board

def dfs(board: list[list[int]],cam_counter:int,idx:int):
    global res
    if cam_counter == len(cam):
        zero_counter = 0
        for i in board:
            zero_counter += i.count(0)
        res = min(zero_counter,res)
        return
    c_board = deepcopy(board)
    y,x,cam_num = cam[idx]
    for i in mode[cam_num]:
        c_board= fill_board(c_board,i,x,y)
        dfs(c_board,cam_counter+1,idx+1)
        c_board = deepcopy(board)


if __name__ == "__main__":
    n,m = map(int,input().split())
    board = []
    cam = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    res = sys.maxsize

    for i in range(n):
        for j in range(m):
            if 1 <= board[i][j] <= 5:
                cam.append((i,j,board[i][j]))
    dfs(board,0,0)
    print(res)



