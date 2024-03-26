import sys
input = sys.stdin.readline

dx = [0,0,0,1,-1]
dy = [0,-1,1,0,0]

def catch_shark():
    global board
    cnt = 0
    man = 0
    while man < C:
        cnt += fishing(man)
        move_shark()
        man += 1
    return cnt

def fishing(x:int)->int:
    global board
    y = 0
    while y < R:
        if board[y][x] != 0:
            tmp = board[y][x][2]
            board[y][x] = 0
            return tmp
        y += 1
    return 0

def move_shark():
    global board
    tmp_board = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                x = j;y = i
                s,d,z = board[i][j]
                tmp = s
                while tmp:
                    nx = x + dx[d];ny = y + dy[d]
                    if 0 <= nx < C and 0 <= ny < R:
                        x  = nx; y = ny
                        tmp -= 1
                    else:
                        if d == 1: d = 2
                        elif d == 2: d = 1
                        elif d == 3: d = 4
                        elif d == 4: d = 3
                if tmp_board[y][x] != 0:
                    tmp_board[y][x] = max(tmp_board[y][x],(s,d,z),key=lambda x:x[2])
                else: tmp_board[y][x] = (s,d,z)
    board = tmp_board
    
if __name__ == "__main__":
    R,C,m = map(int,input().split())
    board = [[0 for _ in range(C)]for _ in range(R)]
    
    for _ in range(m):
        r,c,s,d,z = map(int,input().split())
        if board[r-1][c-1] != 0:
            if board[r-1][c-1][2] < z:
                board[r-1][c-1] = (s,d,z)
        else: board[r-1][c-1] = (s,d,z)
    
    print(catch_shark())