import sys
input = sys.stdin.readline
from collections import deque
def bfs(graph:list[list[int]], n:int,m:int,k:int)->int:
    visited = [[[0] * (k+1) for _ in range(m)]for _ in range(n)]
    q = deque([(0,0,0)])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited[0][0][0] = 1
    while q:
        y,x,z = q.popleft()
        if x == m-1 and y == n-1:
            return visited[y][x][z]
        for c_x,c_y in zip(dx,dy):
            nx = x+c_x
            ny = y+c_y
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    q.append((ny,nx,z))
                elif graph[ny][nx] == 1  and z<k and visited[ny][nx][z+1] == 0:
                    visited[ny][nx][z+1] = visited[y][x][z] + 1
                    q.append((ny,nx,z+1))
    return -1

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    graph = []
    
    for _ in range(n):
        graph.append(list(map(int,input().strip())))
    
    print(bfs(graph,n,m,k))