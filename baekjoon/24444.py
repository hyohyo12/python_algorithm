#24444 / 알고리즘 수업 - 너비 우선 탐색 1
import sys
from collections import deque
input = sys.stdin.readline
def bfs(graph,start,visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    count = 2
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = count
                count += 1

if __name__ == "__main__":
    n, m, r = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(n+1):
        graph[i].sort(reverse=True)
    bfs(graph,r,visited)
    for i in visited[1::]:
        print(i)