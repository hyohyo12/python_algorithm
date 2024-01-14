#4963 / 섬의 개수
#그래프 탐색
from collections import deque
def bfs(x,y):
    dx = [1,-1,0,0,-1,1,-1,1]
    dy = [0,0,1,-1,1,1,-1,-1]
    q = deque()
    q.append((x,y))
    graph[y][x] = 0
    while q:
        a,b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx and nx < w) and (0 <= ny and ny < h) and graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((nx,ny))


if __name__ == "__main__":
    while True:
        count = 0
        w,h = map(int,input().split())
        if w == 0 and h == 0:
            break
        graph = []
        for i in range(h):
            graph.append(list(map(int,input().split())))
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    count += 1
                    bfs(j,i)
        print(count)