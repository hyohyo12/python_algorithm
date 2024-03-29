import sys
from collections import deque
input = sys.stdin.readline

def bfs(board:int,n:int,start:tuple)->list:
    #x,y이동 리스트
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    #상어의 크기 글로벌 변수로 받기
    global baby_shark
    #중복 방문 방지를 위한 방문 리스트
    visited = [[False]*n for _ in range(n)]
    #거리를 담을 거리 리스트
    distance = [[0]*n for _ in range(n)]
    #bfs를 위한 데크
    q = deque([start])
    #함수 결과(먹을 수 있는 먹이의 거리,y값,x값)을 저장
    temp = []
    #시작 점 방문 처리
    visited[start[0]][start[1]] = True
    #bfs
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #인덱스 에러 방지, 방문 확인
            if 0 <= nx < n and 0 <= ny < n  and not visited[ny][nx]:
                #해당 board의 값이 상어 크기 보다 작거나 같다면(문제에서 상어의 크기가 크면 못지나감 -> 같거나 작으면 지나갈 순 있음)
                if board[ny][nx] <= baby_shark:
                    #다음 방문을 위해 큐에 삽입
                    q.append((ny,nx))
                    #방문 처리
                    visited[ny][nx] = True
                    #전 거리에 + 1 하여 현재 거리 저장
                    distance[ny][nx] = distance[y][x]+1
                    #board의 값이 0이 아니고 상어 크기 보다 작다면 해당 물고기는 먹을 수 있으므로
                    if board[ny][nx] != 0 and board[ny][nx] < baby_shark:
                        #결과 리스트 삽입
                        temp.append((distance[ny][nx],ny,nx))
    #거리->y->x 순으로 내림차순 정렬
    return sorted(temp,key = lambda x : (-x[0],-x[1],-x[2]))

if __name__ == "__main__":
    #현재 먹은 먹이 수
    eat = 0
    #현재 아기 상어 크기
    baby_shark = 2
    #결과(정답)을 저장할 변수
    res = 0
    #입력
    #n*n 크기 board
    n = int(input())
    #board 의 내용 저장
    board = [list(map(int,input().split())) for _ in range(n)]
    #board 를 탐색하여 시작 점 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                start = (i,j)
    #board 탐색
    while True:
        #shark -> bfs를 통해 현재 위치에서 먹을 수 있는 먹이들의 (거리,y값,x값)을 저장한 리스트
        shark = bfs(board,n,start)
        #만약 shark의 리스트가 0 이란것은 먹을 수 있는 먹이가 없다는 뜻
        if len(shark) == 0:
            break
        #정렬 했으므로 리스트의 맨 뒤 값은 거리가 짧은 순->y가 작은 순->x가 작은 순으로 올림차순으로 정렬됐다.
        dist,ny,nx = shark.pop()
        #거리->해당 먹이가 있는 곳 까지 몇 초에 갔는가.
        res += dist
        #먹이를 먹은 후 방문처리(중복으로 먹지 못하도록,과거 상어가 있던 곳 다시 못가는 경우 없도록)
        board[start[0]][start[1]],board[ny][nx] = 0,0
        #시작점 먹이를 먹은 시점으로 변환
        start = (ny,nx)
        #먹이 변수 + 1
        eat += 1
        #문제에서 먹은 먹이가 상어의 크기와 같다면 크기 + 1이므로
        if eat == baby_shark:
            #크기 증가,eat변수 0으로 초기화
            baby_shark += 1
            eat = 0
    #결과 출력
    print(res)