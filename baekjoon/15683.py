from copy import deepcopy
import sys
input = sys.stdin.readline

def fill_board(c_board:list[list[int]],cam_num:int,dir:int,y:int,x:int):
    if cam_num == 1:
        if dir == 0:
            x += 1
            while 0 <= x < m and c_board[y][x] != 6:
                c_board[y][x] = '#'
                x += 1
        elif dir == 1:
            x -= 1
            while 0 <= x < m and c_board[y][x] != 6:
                c_board[y][x] = '#'
                x -= 1
        elif dir == 2:
            y += 1
            while 0 <= y < n and c_board[y][x] != 6:
                c_board[y][x] = '#'
                y += 1
        elif dir == 3:
            y -= 1
            while 0 <= y < n and c_board[y][x] != 6:
                c_board[y][x] = '#'
                y -= 1
    elif cam_num == 2:
        if dir == 1:
            x1,x2 = x-1,x+1
            while 0 <= x1 < m and c_board[y][x1] != 6:
                c_board[y][x1] = '#'
                x1 -= 1
            while 0 <= x2 < m and c_board[y][x2] != 6:
                c_board[y][x2] = '#'
                x2 += 1
        elif dir == 2:
            y1,y2 = y-1,y+1
            while 0 <= y1 < n and c_board[y1][x] != 6:
                c_board[y1][x] = '#'
                y1 -= 1
            while 0 <= y2 < n and c_board[y2][x] != 6:
                c_board[y2][x] = '#'
                y2 += 1
    elif cam_num == 3:
        if dir == 0:
            x1,y1 = x+1,y-1
            while 0 < x1 < m and c_board[y][x1] != 6:
                c_board[y][x1] = '#'
                x1 += 1
            while 0 < y1 < n and c_board[x][y1] != 6:
                c_board[y1][x] = '#'
                y1 -= 1
        elif dir == 1:
            x1,y1 = x-1,y+1
            while 0 <= x1 < m and c_board[y][x1] != 6:
                c_board[y][x1] = '#'
                x1 -= 1
            while 0 <= y1 < n and c_board[y1][x] != 6:
                c_board[y1][x] = '#'
                y1 += 1
        elif dir == 2:
            x1,y1 = x+1,y+1
            while 0 <= x1 < m and c_board[y][x1] != 6:
                c_board[y][x1] = '#'
                x1 += 1
            while 0 <= y1 < n and c_board[y1][x] != 6:
                c_board[y1][x] = '#'
                y1 += 1
        elif dir == 3:
            x1,y1 = x-1,y-1
            while 0 <= x1 < m and c_board[y][x1] != 6:
                c_board[y][x1] = '#'
                x1 -= 1
            while 0 <= y1 < n and c_board[y1][x] != 6:
                c_board[y1][x] = '#'
                y1 -= 1
    elif cam_num == 4:
        if dir == 0:
            x1,x2,y1 = x-1,x+1,y+1
            while 0 <= x1 < m and c_board[y][x1] != 6:
                c_board[y][x1] = '#'
                x1 -= 1
            while 0 <= x2 < m and c_board[y][x2] != 6:
                c_board[y][x2] = '#'
                x2 += 1
            while 0 <= y1 < n and c_board[y1][x] != 6:
                c_board[y1][x] = '#'
                y1 += 1
        elif dir == 1:
            x1,x2,y1 = x-1,x+1,y-1
            while 0 <= x1 < m and c_board[y][x1] != 6:
                c_board[y][x1] = '#'
                x1 -= 1
            while 0 <= x2 < m and c_board[y][x2] != 6:
                c_board[y][x2] = '#'
                x2 += 1
            while 0 <= y1 < n and c_board[y1][x] != 6:
                c_board[y1][x] = '#'
                y1 -= 1
    elif cam_num == 5:
        x1,x2,y1,y2 = x-1,x+2,y-1,y+1
        while 0 <= x1 < m and c_board[y][x1] != 6:
            c_board[y][x1] = '#'
            x1 -= 1
        while 0 <= x2 < m and c_board[y][x2] != 6:
            c_board[y][x2] = '#'
            x2 += 1
        while 0 <= y1 < n and c_board[y1][x] != 6:
            c_board[y1][x] = '#'
            y1 -= 1
        while 0 <= y2 < n and c_board[y2][x] != 6:
            c_board[y2][x] = '#'
            y2 += 1
    return c_board

def dfs(board:list[list[int]],idx:int,count:int)->int:
    global res
    if count == start_count:
        tmp = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    tmp += 1
        res = min(res,tmp)
        return
    for i in range(idx,start_count):
        y,x = start.pop()
        if board[y][x] == 1:
            for j in range(4):
                c_board = deepcopy(board)
                c_board = fill_board(c_board,1,j,y,x)
                dfs(c_board,i+1,count+1)
                start.append((y,x))
        elif board[y][x] == 2:
            for j in range(2):
                c_board = deepcopy(board)
                c_board = fill_board(c_board,2,j,y,x)
                dfs(c_board,i+1,count+1)
                start.append((y,x))
        elif board[y][x] == 3:
            for j in range(4):
                c_board = deepcopy(board)
                c_board = fill_board(c_board,3,j,y,x)
                dfs(c_board,i+1,count+1)
                start.append((y,x))
        elif board[y][x] == 4:
            for j in range(2):
                c_board = deepcopy(board)
                c_board = fill_board(c_board,4,j,y,x)
                dfs(c_board,i+1,count+1)
                start.append((y,x))
        elif board[y][x] == 5:
            c_board = deepcopy(board)
            c_board = fill_board(c_board,5,0,y,x)
            dfs(c_board,i+1,count+1)
            start.append((y,x))


if __name__ == "__main__":
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    res = sys.maxsize
    
    start = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and board[i][j] != 6:
                start.append((i,j))
                
    start_count = len(start)
    dfs(board,0,0)
    print(res)