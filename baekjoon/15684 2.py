import sys
from copy import deepcopy
input = sys.stdin.readline

def is_possible(board:list[list[int]])->bool:
    for i in range(n):
        x,y = i,0
        while y < h:
            if board[y][x]:
                x += 1
            elif x > 0 and board[y][x-1]:
                x -= 1
            y+=1
        if x != i:return False
    return True

def dfs(depth:int,x:int,y:int):
    global res
    global board
    if is_possible(board):
        res = min(res,depth)
        return
    if depth == 3 or depth >= res:
        return
    for i in range(x,h):
        if i == x:
            now = y
        else:now = 0
        for j in range(now,n-1):
            if board[i][j]:
                board[i][j] = True
                dfs(depth+1,i,j+2)
                board[i][j] = False


if __name__ == "__main__":
    res = sys.maxsize
    n,m,h = map(int,input().split())
    board = [[False for _ in range(n)] for _ in range(h)]
    for _ in range(m):
        a,b = map(int,input().split())
        board[a-1][b-1] = True
    dfs(0,0,0)
    print(res if res != sys.maxsize else -1)

