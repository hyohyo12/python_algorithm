#16173 점프왕 쩰리
#그래프 이론
from collections import deque
import sys
input = sys.stdin.readline
def bfs(x,y):
    visited = [[False] * n for i in range(n)]
    dx = [1,0]
    dy = [0,1]
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        step = graph[x][y]
        if step == -1:
            print("HaruHaru")
            return
        for i in range(2):
            nx = x + dx[i]*step
            ny = y + dy[i]*step
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
    print("Hing")
    
if __name__ =="__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    bfs(0,0)
    