import sys
from collections import deque
input = sys.stdin.readline
def dfs(graph,start,vertex):
    dfs_visited[start] = True
    print(start,end = " ")
    for i in range(1,vertex+1):
        if not dfs_visited[i] and graph[start][i]:
            dfs(graph,i,vertex)

def bfs(graph,start,vertex):
    q = deque([start])
    while q:
        x = q.popleft()
        bfs_vistied[x] = True
        print(x,end = " ")
        for i in range(1,vertex+1):
            if not bfs_vistied[i] and graph[x][i]:
                q.append(i)
                bfs_vistied[i] = True
                
if __name__ == "__main__":
    n,m,v = map(int,input().split())
    graph = [ [False] * (n+1) for i in range(n+1)]
    dfs_visited = [False] * (n+1)
    bfs_vistied = [False] * (n+1)
    for i in range(m):
        node1,node2 = map(int,input().split())
        graph[node1][node2] = True
        graph[node2][node1] = True
    dfs(graph,v,n)
    print("")
    bfs(graph,v,n)