import sys
from collections import defaultdict
input = sys.stdin.readline

coord = defaultdict(int)

dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]



def move(board:list[list[int]],piece:list[list[list[tuple]]],num:int,loc:tuple,n:int):
    global coord
    flag = False
    #loc -> 현재 말의 위치
    y,x = loc
    #현재 말의 위치 위에 있는 말 모두 옮기기위해 현재 말의 인덱스를 먼저 구하기
    for i,data in enumerate(piece[y][x]):
        if data[0] == num:
            idx = i
            dir = data[1]
            break
    else:
        for i,data in enumerate(piece[y][x]):
            if data[0] == num:
                idx = i
                dir = data[1]
                break
    #말 위, 말 아래 분리
    up,down = piece[y][x][idx:],piece[y][x][:idx]
    #해당 말 아래는 그대로 piece board에 남겨놓음
    piece[y][x] = down
    #해당 위치 말 위에 있는 말들의 새로운 위치
    ny,nx = y+dy[dir], x+dx[dir]
    #인덱스 안쪽일 떄
    if 0 <= nx < n and 0 <= ny < n:
        #보드판의 색
        #해당 칸이 또 색이 있을 수 있으므로 보드판의 색을 다시 판단하여 넣어줌
        #흰색
        if board[ny][nx] == 0:
            piece[ny][nx] = piece[ny][nx] + up
            for i,d in up:
                coord[i] = (ny,nx)
        #빨간색
        elif board[ny][nx] == 1:
            piece[ny][nx] = piece[ny][nx] + list(reversed(up))
            coord[num] = (ny,nx)
            for i,d in up:
                coord[i] = (ny,nx)
        else:
            flag = True
    else:
        flag = True
    #파란색
    if flag:
        #오른쪽
        if dir == 1:
            dir = 2
            nx,ny = x+dx[dir],y+dy[dir]
            up[0] = (num,dir)
            if not 0 <= nx < n or not 0 <= ny < n or board[ny][nx] == 2:
                piece[y][x] = piece[y][x] + up
            else:
                if board[ny][nx] == 0:
                    piece[ny][nx] = piece[ny][nx] + up
                elif board[ny][nx] == 1:
                    piece[ny][nx] = piece[ny][nx] + list(reversed(up))
                for i,d in up:
                    coord[i] = (ny,nx)
        #왼쪽
        elif dir == 2:
            dir = 1
            nx,ny = x+dx[dir],y+dy[dir]
            up[0] = (num,dir)
            if not 0 <= nx < n or not 0 <= ny < n or board[ny][nx] == 2:
                piece[y][x] = piece[y][x] + up
            else:
                if board[ny][nx] == 0:
                    piece[ny][nx] = piece[ny][nx] + up
                elif board[ny][nx] == 1:
                    piece[ny][nx] = piece[ny][nx] + list(reversed(up))
                for i,d in up:
                    coord[i] = (ny,nx)
        #위
        elif dir == 3:
            dir = 4
            nx,ny = x+dx[dir],y+dy[dir]
            up[0] = (num,dir)
            if not 0 <= nx < n or not 0 <= ny < n or board[ny][nx] == 2:
                piece[y][x] = piece[y][x] + up
            else:
                if board[ny][nx] == 0:
                    piece[ny][nx] = piece[ny][nx] + up
                elif board[ny][nx] == 1:
                    piece[ny][nx] = piece[ny][nx] + list(reversed(up))
                for i,d in up:
                    coord[i] = (ny,nx)
            #아래
        else:
            dir = 3
            nx,ny = x+dx[dir],y+dy[dir]
            up[0] = (num,dir)
            if not 0 <= nx < n or not 0 <= ny < n or board[ny][nx] == 2:
                piece[y][x] = piece[y][x] + up
            else:
                if board[ny][nx] == 0:
                    piece[ny][nx] = piece[ny][nx] + up
                elif board[ny][nx] == 1:
                    piece[ny][nx] = piece[ny][nx] + list(reversed(up))
                for i,d in up:
                    coord[i] = (ny,nx)


def main():
    global coord
    #입력
    #n -> n x n 크기의 board, k -> 체스 말의 개수
    n,k = map(int,input().split())
    #piece -> 체스말의 위치를 저장할 3중리스트로 구성 해당 칸에 장기말이 있다면 겹쳐야하므로
    piece = [[[] for _ in range(n)] for _ in range(n)]
    #빠르게 말 번호 순으로 이동을 위해 말의 번호와 위치 정보를 저장할 딕셔너리
    coord = defaultdict(int)
    #board -> 각 칸의 정보 -> (흰색,빨간색,파란색) 을 저장할 board
    board = [list(map(int,input().split())) for _ in range(n)]
    
    
    #체스말 입력
    #k만큼 반복
    for i in range(1,k+1):
        #r->행,c->열,d->방향
        r,c,d = map(int,input().split())
        #체스말의 번호와 방향을 튜플로 묶어 해당위치에 저장
        piece[r-1][c-1].append((i,d))
        #말의 좌표를 튜플로 해당 번호에 저장
        coord[i] = (r-1,c-1)
    
    #정답 변수(말을 총 몇번 이동했는지)
    cnt = 0
    while cnt < 1001:
        cnt += 1
        for i in range(1,k+1):
            move(board,piece,i,coord[i],n)
            y,x = coord[i]
            if len(piece[y][x]) >= 4:
                print(cnt)
                sys.exit()
    print(-1)


if __name__ == "__main__":
    main()