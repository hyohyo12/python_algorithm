import sys
from collections import deque
import copy
input = sys.stdin.readline
def makeWall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(count+1)
                graph[i][j] = 0
                
def bfs():
    cnt = 0
    global result
    t_graph = copy.deepcopy(graph)
    q = deque()
    for i in range(n):
        for j in range(m):
            if t_graph[i][j] == 2:
                q.append((i,j))
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dxdy[i][0]
            ny = y + dxdy[i][1]
            if (0 <= nx and nx < m) and (0 <= ny and ny < n):
                if t_graph[ny][nx] == 0:
                    t_graph[ny][nx] = 2
                    q.append((ny,nx))

    for k in range(n):
        cnt += t_graph[k].count(0)
    result = max(cnt,result)

if __name__ == "__main__":
    dxdy = [[1,0],[-1,0],[0,1],[0,-1]]
    result = 0
    n,m = map(int,input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))
    makeWall(0)
    print(result)