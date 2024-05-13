import sys
from collections import deque
input =  sys.stdin.readline

dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,-1,-1,1,1]
board = []

#중앙으로부터 8방향 탐색하여 통나무를 돌릴 수 있는지 없는 지 반환하는 함수
def can_turn(cur_loc,n):
    global board
    y,x = cur_loc
    #상하좌우대각선 탐색
    for i in range(8):
        ny,nx = y + dy[i], x + dx[i]
        #인덱스가 넘어간다면
        if not 0 <= ny < n or not 0 <= nx < n:
            return 0
        #범위 안에 잘리지 않은 나무가 있다면
        elif board[ny][nx] == '1':
            return 0
    #통나무 돌릴 수 있음
    return 1

def bfs(start:list[tuple],end:list[tuple],dir:int,n:int,end_dir:int):
    global board
    visited = set()
    q = deque()
    q.append((start,dir,0))
    visited.add((start,dir))
    while q:
        cur_loc,d,cnt = q.popleft()
        if cur_loc == end and d == end_dir:
            return cnt
        #가로
        if d == 1:
            #5개의 커맨드를 탐색 가능하면 탐색
            y,x = cur_loc
            #U연산
            #y값의 인덱스 에러 방지와 이동 방향에 나무 존재 여부 확인
            if y-1 >= 0 and board[y-1][x] != '1' and board[y-1][x-1] != '1' and board[y-1][x+1] != '1':
                if ((y-1,x),d) not in visited:
                    visited.add(((y-1,x),d))
                    q.append(((y-1,x),d,cnt+1))
            #D연산
            if y+1 < n and board[y+1][x] != '1' and board[y+1][x-1] != '1' and board[y+1][x+1] != '1':
                if ((y+1,x),d) not in visited:
                    visited.add(((y+1,x),d))
                    q.append(((y+1,x),d,cnt+1))
            #R연산
            if x+1 < n-1 and board[y][x+2] != '1':
                if (((y,x+1),d)) not in visited:
                    visited.add(((y,x+1),d))
                    q.append(((y,x+1),d,cnt+1))
            #L연산
            if x-2 >= 0 and board[y][x-2] != '1':
                if (((y,x-1),d)) not in visited:
                    visited.add(((y,x-1),d))
                    q.append(((y,x-1),d,cnt+1))
            #T연산
            if can_turn(cur_loc,n):
                if ((y,x),0) not in visited:
                    visited.add(((y,x),0))
                    q.append(((y,x),0,cnt+1))
        #세로
        elif d == 0:
            y,x = cur_loc
            #D연산
            if y+2 < n and board[y+2][x] != '1':
                if ((y+1,x),d) not in visited:
                    visited.add(((y+1,x),d))
                    q.append(((y+1,x),d,cnt+1))
            #U연산
            if y-2 >= 0 and board[y-2][x] != '1':
                if ((y-1,x),d) not in visited:
                    visited.add(((y-1,x),d))
                    q.append(((y-1,x),d,cnt+1))
            #L연산
            if x-1 >= 0 and board[y-1][x-1] != '1' and board[y+1][x-1]!='1' and board[y][x-1]!='1':
                if ((y,x-1),d) not in visited:
                    visited.add(((y,x-1),d))
                    q.append(((y,x-1),d,cnt+1))
            #R연산
            if x+1 < n and board[y-1][x+1] != '1' and board[y+1][x+1]!='1' and board[y][x+1]!='1':
                if ((y,x+1),d) not in visited:
                    visited.add(((y,x+1),d))
                    q.append(((y,x+1),d,cnt+1))
            #T연산
            if can_turn(cur_loc,n):
                if ((y,x),1) not in visited:
                    visited.add(((y,x),1))
                    q.append(((y,x),1,cnt+1))
    return 0
    

def main():
    global board
    n = int(input())
    board = []
    start,end = [],[]
    for i in range(n):
        tmp = input().strip()
        for j in range(n):
            if tmp[j] == 'B':
                start.append((i,j))
            elif tmp[j] == 'E':
                end.append((i,j))
        board.append(list(tmp))
    if start[0][1] == start[1][1]:
        #가로 -> 0
        dir = 0
    else:
        #세로 -> 1
        dir = 1
    if end[0][1] == end[1][1]:
        end_dir = 0
    else:end_dir = 1
    #탐색은 기준 점과 방향만으로 탐색 싲ㄴ행
    print(bfs(start[1],end[1],dir,n,end_dir))
    
if __name__ == "__main__":
    main()