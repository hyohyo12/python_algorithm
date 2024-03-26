import sys
from collections import deque
input = sys.stdin.readline
#BFS함수
def bfs(start:tuple[int])->list[int]:
    #초기 인접 국가 리스트에 start 좌표만 튜플로 삽입
    nations = [start]
    #BFS 탐색을 위한 큐
    q = deque([start])
    #BFS탐색
    while q:
        #q에서 y값 x값 pop
        y,x = q.popleft()
        #이동 리스트를 통해 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #이동할 곳이 인덱스 안에 있는지 그리고 방문했는지
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                #현재 국가와 다음 국가 사이 차이가 L이상 R이하인지
                if L <= abs(board[y][x]-board[ny][nx]) <= R:
                    #다음 방문을위해 큐에 추가
                    q.append((ny,nx))
                    #방문 처리
                    visited[ny][nx] = True
                    #인접 국가 리스트에 추가
                    nations.append((ny,nx))
    #인접 국가 리스트 반환
    return nations

if __name__ == "__main__":
    #입력
    #각각 N->N*N 지도, L -> 인구 수 차이가 L명 이상 ,R-> 인구 수 차이가 R명 이하
    N,L,R= map(int,input().split())
    #이동 가능 리스트
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    #지도 입력
    board = [list(map(int,input().split())) for _ in range(N)]
    #몇 일 지났는지 저장
    count = 0
    #탐색 시작
    while True:
        #종료 확인 Flag(밑에 BFS한 결과가 한번도 나오지 않았다면)
        end = True
        #중복 방문 방지를 위한 방문 리스트
        visited = [[False]*N for _ in range(N)]
        #board탐색
        for i in range(N):
            for j in range(N):
                #방문 하지 않았으면 실행
                if not visited[i][j]:
                    #방문 처리
                    visited[i][j] = True
                    #BFS로 해당 지점에 인접한 국가들에대해 차이가 L이상R이하 인지 확인
                    nations = bfs((i,j))
                    #nations의 길이가 2이상부터(start 만 초기에 들어있음.)
                    if len(nations) > 1:
                        #인구 수 계산
                        population = sum([board[y][x] for y,x in nations]) // len(nations)
                        #인구 수 갱신
                        for y,x in nations:
                            board[y][x] = population
                        #한 번이라도 BFS의 내용이 있다면 False로 바꿈
                        end = False
        #종료
        if end:
            break
        #결과 값 + 1(하루가 지남.)
        count += 1
    print(count)