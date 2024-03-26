import sys
input = sys.stdin.readline

#주사위 옮기는 명령
def move_dice(cmd:int):
    global x,y
    global top,w,e,b,u,f
    #동
    if cmd == 1:
        #인덱스 에러 방지
        if y+1 >= m:return False
        #동쪽 이동
        y += 1
        #서쪽->바닥, 위->서쪽, 동쪽->위,바닥->동쪽 
        top,w,e,u = w,u,top,e
        if board[x][y] == 0:board[x][y] = u
        else:u = board[x][y];board[x][y] = 0
    #서
    elif cmd == 2:
        #인덱스 에러 방지
        if y-1 < 0:return False
        #서쪽 이동
        y -= 1
        #서쪽->위, 위->동쪽, 동쪽->바닥,바닥->서쪽
        top,w,e,u = e,top,u,w
        if board[x][y] == 0:board[x][y] = u
        else:u = board[x][y];board[x][y] = 0
    #북
    elif cmd == 3:
        if x-1 < 0 : return False
        x -= 1
        #위->앞, 앞->바닥, 뒤->위, 바닥->뒤
        f,top,b,u = u,f,top,b
        if board[x][y] == 0:
            board[x][y] = u
        else:u = board[x][y];board[x][y] = 0
    #남
    elif cmd == 4:
        if x+1 >= n: return False
        x += 1
        #위->뒤, 앞->위, 뒤->바닥, 바닥->앞
        top,f,u,b = b,top,f,u
        if board[x][y] == 0:board[x][y] = u
        else:u = board[x][y];board[x][y] = 0
    return True
if __name__ == "__main__":
    #입력
    #nxm 모양의 board, 주사위의 초기 위치 [x][y], k개의 명령
    n,m,x,y,k = map(int,input().split())
    #nxm board
    board = [list(map(int,input().split())) for _ in range(n)]
    #명령 입력(동:1, 서:2, 북:3, 남:4)
    cmd = map(int,input().split())
    
    top,w,e,b,u,f = 0,0,0,0,0,0
    
    #명령 리스트 탐색
    for c in cmd:
        if move_dice(c):
            print(top)