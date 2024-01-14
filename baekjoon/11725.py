from collections import deque
def bfs(graph):
    q = deque()
    parents = [0]*(len(graph))
    visited = [False] * (len(graph))
    q.append(1)
    visited[1] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                parents[i] = x
                visited[i] = True
                q.append(i)
    return parents

def dfs(graph,parent,x,visited,parents):
    if not visited[x]:
        parents[x]=parent
        visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(graph,x,i,visited,parents)
            visited[i]
    return parents

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n+1)
    parents = [0]*(n+1)
    dfs(graph,0,1,visited,parents)
    for i in parents[2:]:
        print(i)
    
    