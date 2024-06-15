import sys
input = sys.stdin.readline


def dfs(graph:list[list[int]],cur:int,end:int,depth:int,visited:list[int]) -> int:
    global res
    if cur == end:
        res = depth
    for node in graph[cur]:
        if not visited[node]:
            visited[node] = 1
            dfs(graph,node,end,depth+1,visited)
            visited[node] = 0


def main():
    global res
    res = -1
    n = int(input())
    graph = [[] for _ in range(n+1)]
    start,end = map(int,input().split())
    
    m = int(input())
    for _ in range(m):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)
    
    dfs(graph,start,end,0,[0 for _ in range(n+1)])
    
    print(res)


if __name__ == "__main__":
    main()