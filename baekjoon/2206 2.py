import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    q = deque([(0,0,0)])
    visited[0][0][0] = 1
    while q:
        x,y,z = q.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == '1' and z == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append((nx,ny,1))
                elif graph[ny][nx] == '0' and visited[ny][nx][z] == 0:
                    q.append((nx,ny,z))
                    visited[ny][nx][z] = visited[y][x][z] + 1
    return -1

if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = [input().rstrip() for _ in range(n)]
    print(bfs())