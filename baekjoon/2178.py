#2178 / 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline
def bfs(graph):
    q = deque()
    q.append((0,0))
    while q:
        x,y = q.popleft()
        for i in xy:
            if (0 <= x+i[0] and x+i[0] < len(graph[0])) and (0 <= y+i[1] and len(graph) > y+i[1]):
                if graph[y+i[1]][x+i[0]] == 1:
                    graph[y+i[1]][x+i[0]] = graph[y][x] + 1
                    q.append((x+i[0],y+i[1]))
    return graph[n-1][m-1]
if __name__ == "__main__":
    n,m = map(int,input().split())
    graph = []
    for i in range(n):
        line = input().strip()
        graph.append(list(map(int,line)))
    xy = [[1,0],[-1,0],[0,1],[0,-1]]
    print(bfs(graph))
    