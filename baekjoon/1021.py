# 백준 1021
# BFS
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0] #dx,dy 는 상하 좌우 움직이도록 하는 값들을 저장한 리스트
dy= [0,0,-1,1] #(-1,0) -> 좌 (1,0) -> 우 (0,-1) -> 하 (0,1) -> 상 
def bfs(x,y): #BFS 함수
    q = deque() #bfs를 위한 큐 생성
    q.append((x,y)) #큐에 x,y를 튜블로 추가
    matrix[x][y] = 0 # 방문 처리
    while q: # 탐색
        x,y = q.popleft() # 큐에 튜플로 저장한 값 각각 x,y 에 저장
        for i in range(4): # 상하 좌우 확인
            nx = x + dx[i] 
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 만약 x값이 n을 넘어가거나 0보다 작으면 또는 y값이 m보다 크거나 0보다 작으면
                continue # 인덱스 에러 방지
            if matrix[nx][ny] == 1: # 상하좌우 중 배추가 있으면
                matrix[nx][ny] = 0 # 근접한 배추는 애벌레가 갈 수 있으므로 0으로 바꿔 처리
                q.append((nx,ny)) # 다음 방문을 위해 큐에 추가
if __name__ == "__main__":
    for _ in range(int(input())): # 테스트 케이스만큼 반복
        n,m,k = map(int,input().split()) # 각각 n -> 세로, m -> 가로,  k -> 배추의 개수
        matrix = [[0]*(m) for _ in range(n)] # 배추의 위치를 저장하는 이차원 리스트
        cnt = 0 # 정답을 저장할 변수
        for i in range(k): # 배추 개수만큼 반복
            x,y = map(int,input().split()) #배추의 좌포 x,y 입력
            matrix[x][y] = 1 # 위치 기록
        for x in range(n): # 배추가 있는지 탐색
            for y in range(m):
                if matrix[x][y] == 1: # 만약에 배추가 있을경우
                    bfs(x,y) #주변 배추를 검색하기위한 bfs 실행
                    cnt += 1 # 애벌레 + 1
        print(cnt) #출 력