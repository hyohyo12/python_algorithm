import sys
input = sys.stdin.readline
from collections import deque
def bfs(graph:list[list[int]], n:int,m:int,k:int)->int:
    visited = [[[0] * (k+1) for _ in range(m)]for _ in range(n)] #k(부술 수 있는 벽) 에 따라 방문리스트를 3차원 방문리스트로 구성
    q = deque([(0,0,0)]) #탐색 큐
    dx = [0,0,1,-1] #상하 좌우 탐색할 dx,dy 리스트
    dy = [1,-1,0,0]
    visited[0][0][0] = 1 #좌표(0,0) 과 0번 벽을 부순 곳에 1(방문 처리)
    while q: #너비 우선 탐색 시작
        y,x,z = q.popleft()#z는 부술 수 있는 벽
        if x == m-1 and y == n-1:
            return visited[y][x][z]
        for c_x,c_y in zip(dx,dy): #상하 좌우 탐색
            nx = x+c_x
            ny = y+c_y
            if 0 <= nx < m and 0 <= ny < n: #인덱스 에러 방지
                if graph[ny][nx] == 0 and visited[ny][nx][z] == 0: #방문하지 않았고 이동할 수 있는  곳이라면
                    visited[ny][nx][z] = visited[y][x][z] + 1 #방문 처리와 동시에 몇번째로 방문했는지 저장
                    q.append((ny,nx,z)) #다음 방문하기 위해 탐색 큐에 삽입
                elif graph[ny][nx] == 1  and z<k and visited[ny][nx][z+1] == 0: # 현재 탐색할 곳이 벽(1) 이고 벽을 부숴야하므로 z(현재 부술 수 있는 횟수) 가 k번 보다 작고 방문하지 않았다면
                    visited[ny][nx][z+1] = visited[y][x][z] + 1  #방문 처리하고(벽을 부쉈으므로) z+1번째에 현재값 +1해준다.
                    q.append((ny,nx,z+1)) #삽입
    return -1

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    graph = []
    
    for _ in range(n):
        graph.append(list(map(int,input().strip())))
    
    print(bfs(graph,n,m,k))