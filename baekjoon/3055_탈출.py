import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(start:tuple,end:tuple,board:tuple,water:list[tuple])->int:
    #r -> 열, c -> 행
    r = len(board)
    c = len(board[0])
    #비버 집(board에서의 D가 있는 곳)으로 가는 데 걸리는 최소 시간을 구하기 위해 inf 값으로 초기화
    result = inf
    #물 먼저 몇 분에 어느 정도 퍼졌는지 구하기
    #bfs를 위해 덱 자료구조에 water좌표 모두 넣기
    q = deque(water)
    #각 위치에서 언제 해당 칸으로 퍼졌는지 저장할 board크기와 같은 이중 리스트
    water_visited = [[inf for _ in range(len(board[0]))] for _ in range(len(board))]
    #인덱스 에러 방지(물이 존재한다면) bfs에서 처음 방문하는 값을 0으로 초기화
    if len(water):
        water_visited[water[0][0]][water[0][1]] = 0
    #물 이동을 위한 bfs 시작
    while q:
        #y,x -> 현재 위치, time 현재 위치까지 이동까지 걸린 시간
        y,x,time = q.popleft()
        #4방향(상,하,좌,우) 검사
        for i in range(4):
            #ny,nx -> 다음 위치
            ny,nx = y + dy[i],x + dx[i]
            #인덱스 에러 방지와 해당 위치가 돌이 없고, 비버의 집이 아닐 시에만 이동 가능
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 'X' and board[ny][nx] != 'D':
                #water_visited를 inf(제일 큰 값) 으로 초기화 했으므로 자연스럽게
                #현재 위치에서 제일 먼저 퍼지는 물의 시간을 찾고, 방문 검사까지 가능
                if water_visited[ny][nx] > time + 1:
                    #다음 탐색을 위해 큐에 다음 위치와 갱신된 시간을 저장
                    q.append((ny,nx,time + 1))
                    #방문 처리
                    water_visited[ny][nx] = time + 1
    
    #물의 이동 시간 리스트를 구하고, 이제 고슴도치의 이동을 함
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    #또한 덱 자료형에 현재 고슴도치의 시작지점을 넣음
    q = deque([start])
    #현재 고슴도치가 있는 곳을 방문 처리
    visited[start[0]][start[1]] = True
    #bfs 시작
    while q:
        #현재 방문 위치와 시간
        y,x,time = q.popleft()
        #현재 위치가 비버의 집(도착 지점) 이면 result 최소값으로 갱신
        if (y,x) == end:
            result = min(result,time)
        #4방향(상,하,좌,우) 탐색
        for i in range(4):
            #다음 위치 ny, nx
            ny,nx = y + dy[i], x + dx[i]
            #인덱스 에러 방지와 다음 이동할 곳이 바위가 아닐 때
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 'X':
                #중복 방문 방지 및 고슴도치가 다음 이동할 시간떄에 물이 있는지 없는지 검사
                if not visited[ny][nx] and time + 1 < water_visited[ny][nx]:
                    #방문 처리
                    visited[ny][nx] = True
                    #큐에 추가
                    q.append((ny,nx,time+1))
    #탐색 완료 후 result(결과) 리턴
    #inf 리턴 시 탐색 실패, 그 외 탐색 성공
    return result

#메인 함수
def main():
    #입력
    #r -> 열, c -> 행
    r,c = map(int,input().split())
    board = []
    #물이 있는 곳의 위치의 좌표를 튜플로 저장할 리스트
    water = []
    for i in range(r):
        tmp = list(input().strip())
        for j in range(c):
            #동굴(탐색 지점) 저장
            if tmp[j] == 'D':
                end = (i,j)
            #물의 위치 저장
            elif tmp[j] == '*':
                water.append((i,j,0))
            #고슴도치(시작 지점) 저장
            elif tmp[j] == 'S':
                start = (i,j,0)
        board.append(tmp)
    #res에 탐색 결과 저장
    res = bfs(start,end,board,water)
    #inf가 아닐 때(탐색 성공) 그대로 출력 그 외(탐색 실패) KAKTUS 출력
    print(res if res != inf else "KAKTUS")

if __name__ == "__main__":
    main()
