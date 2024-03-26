import sys
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def dir_list(d:int,g:int):
    dir = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(dir)-1,-1,-1):
            tmp.append((dir[i]+1)%4)
        dir.extend(tmp)
    return dir

if __name__ == "__main__":
    res = 0
    board = [[0 for _ in range(101)] for _ in range(101)]
    n = int(input())
    for _ in range(n):
        #(x,y) 시작지점 , d : 시작 방향, g : 세대
        x,y,d,g = map(int,input().split())
        dir = dir_list(d,g)
        
        for i in range(len(dir)):
            board[y][x] = 1
            x += dx[dir[i]]
            y += dy[dir[i]]
            board[y][x] = 1
        
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
                res += 1
    print(res)