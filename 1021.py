import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy= [0,0,-1,1]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    matrix[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                q.append((nx,ny))
if __name__ == "__main__":
    for _ in range(int(input())):
        n,m,k = map(int,input().split())
        matrix = [[0]*(m) for _ in range(n)]
        cnt = 0
        for i in range(k):
            x,y = map(int,input().split())
            matrix[x][y] = 1
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == 1:
                    bfs(x,y)
                    cnt += 1
        print(cnt)