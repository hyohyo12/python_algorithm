import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph:list[list[int]],n:int,m:int,r:int,c:int,d:int)->int:
    cnt = 1
    dyx = [(-1,0),(0,1),(1,0),(0,-1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[r][c] = True
    q = deque([(r,c,d)])
    while q:
        r,c,d = q.popleft()
        for _ in range(4):
            ny,nx = r+dyx[(d+3)%4][0],c+dyx[((d+3)%4)][1]
            d = (d+3)%4
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0:
                    if not visited[ny][nx]:
                        q.append((ny,nx,d))
                        cnt += 1
                        visited[ny][nx] = True
                        break
        else:
            if graph[r-dyx[d][0]][c-dyx[d][1]] == 1:
                return cnt
            q.append((r-dyx[d][0],c-dyx[d][1],d))
    

if __name__ == "__main__":
    n,m = map(int,input().split())
    r,c,d = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    
    print(bfs(graph,n,m,r,c,d))