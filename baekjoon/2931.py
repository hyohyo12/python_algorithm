import sys
from collections import deque
input = sys.stdin.readline


def bfs(y,x,dir,r,c):
    global board
    global visited
    global c_y
    global c_x
    global check_list
    q = deque()
    q.append((y,x,dir))
    visited[y][x] = True
    while q:
        y,x,dir = q.popleft()
        for d in dir:
            ny,nx = y + dy[d],x + dx[d]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                if board[ny][nx] != '.':
                    visited[ny][nx] = True
                    nd = dir_table[board[ny][nx]]
                    q.append((ny,nx,nd))
                else:
                    if board[y][x] == 'M' or board[y][x] == 'Z':
                        continue
                    if c_x == 0 and c_y == 0:
                        c_x,c_y = nx+1,ny+1
                    nd = (d+1)%2 if d < 2 else (d+1)%2+2
                    if nd not in check_list:
                            #양방향으로 가스가 수송되니깐 반대방향을 append하고
                            #m-z,z-m으로 모두 bfs 실행 결국 쌍방으로 저장되긴 할거임.
                            check_list.append(nd)


#메인 함수
def main():
    global c_y,c_x
    global board
    global visited
    global check_list
    global dir_table
    #입력
    #rxc 크기의 board
    r,c = map(int,input().split())
    visited = [[False for _ in range(c)] for _ in range(r)]
    #r(줄) 만큼 반복하여 열을 입력받아 board에 저장
    board = []
    for i in range(r):
        #한 줄씩 검사하면서 M(모스크바),Z(자그레브) 위치 선정
        tmp = list(input().strip())
        for j in range(c):
            if tmp[j] == 'M':
                my,mx = i,j
            elif tmp[j] == 'Z':
                zy,zx = i,j
        board.append(tmp)
    bfs(my,mx,[0,1,2,3],r,c)
    bfs(zy,zx,[0,1,2,3],r,c)
    
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and board[i][j] != '.':
                bfs(i,j,dir_table[board[i][j]],r,c)
    check_list.sort()
    if check_list == [0,1,2,3]:
        print(c_y,c_x,'+')
    else:
        for s in ['|','-','1','2','3','4']:
            if dir_table[s] == check_list:
                print(c_y,c_x,s)
                break

if __name__ == "__main__":
    dir_table = {
    "|":[0,1],
    "-":[2,3],
    "1":[1,3],
    "2":[0,3],
    "3":[0,2],
    "4":[1,2],
    "M":[0,1,2,3],
    "Z":[0,1,2,3],
    "+":[0,1,2,3],
    }
    board = []
    visited = []
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    c_y = 0
    c_x = 0
    check_list = []
    #메인 함수 호출
    main()
    