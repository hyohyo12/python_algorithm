import sys
input = sys.stdin.readline


def run_cleaner(air_cleaner:list[tuple[int]]):
    global board
    global tot_dust
    for i in range(2):
        #윗 방향(반 시계 방향 우 상 좌 하)
        if i == 0:
            y,x = air_cleaner[i]
            tmp = 0
            prev = 0
            x += 1
            #오른쪽
            while x < c:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                x += 1
            #위쪽
            x -= 1
            y -= 1
            while y >= 0:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                y -= 1
            #왼쪽
            y += 1
            x -= 1
            while x >= 0:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                x -= 1
            x += 1
            y += 1
            #아래쪽
            while board[y][x] != -1:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                y += 1
            tot_dust -= prev


        #아랫 방향(시계 방향 우 하 좌 상)
        elif i == 1:
            y,x = air_cleaner[i]
            tmp = 0
            prev = 0
            x += 1
            #오른쪽
            while x < c:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                x += 1
            x -= 1
            y += 1
            #아래쪽
            while y < r:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                y += 1
            #왼쪽
            y -= 1
            x -= 1
            while x >= 0:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                x -= 1
            #위쪽
            x += 1
            y -= 1
            while board[y][x] != -1:
                tmp = board[y][x]
                board[y][x] = prev
                prev = tmp
                y -= 1
            tot_dust -= prev


def diffusion():
    global board
    tmp_board = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                count = 0
                for k in range(4):
                    nx,ny = j + dx[k], i + dy[k]
                    if 0 <= nx < c and 0 <= ny < r and board[ny][nx] != -1:
                        count += 1
                        tmp_board[ny][nx] += board[i][j] // 5
                board[i][j] -= count * (board[i][j]//5)
    for i in range(r):
        for j in range(c):
            board[i][j] += tmp_board[i][j]

if __name__ == "__main__":
    #먼지 이동 리스트 (상,하,좌,우)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    #입력
    #rxc 모양의 board, t초가 지난 후 방의 미세먼지 양.
    r,c,t = map(int,input().split())
    #Board 입력
    board = []
    for _ in range(r):
        board.append(list(map(int,input().split())))
    #Board 순회하며 미세먼지와 공기청정기의 위치를 저장한다.
    air_cleaner = []
    dust = []
    tot_dust = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:
                #air_clearner 의 0은 위쪽 1은 아래쪽
                air_cleaner.append((i,j))
            #미세먼지인 경우 dust리스트에 저장
            elif board[i][j] != 0:
                tot_dust += board[i][j]
    for _ in range(t):
        diffusion()
        run_cleaner(air_cleaner)

    print(tot_dust)