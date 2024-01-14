#24480 / 알고리즘 수업 - 깊이 우선 탐색 2
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline
def dfs(idx):
    global cnt
    visited[idx] = cnt
    graph[idx].sort(reverse=True)
    for i in graph[idx]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

if __name__ == "__main__":
    cnt = 1
    n,m,r = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    dfs(r)
    for i in range(1,n+1):
        print(visited[i])