import sys
input = sys.stdin.readline
inf = sys.maxsize

def floyd_warshall(graph:list[list[int]],n:int):
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])
    
if __name__ == "__main__":
    n = int(input())
    
    graph = [[inf for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
    while True:
        sp,ep = map(int,input().split())
        if sp == -1 and ep == -1:
            break
        graph[sp][ep] = 1
        graph[ep][sp] = 1
    
    floyd_warshall(graph,n)
    res = []
    for i in range(1,n+1):
        res.append(max(graph[i][1:]))
    minimum = min(res)
    print(minimum,res.count(minimum))
    for idx,score in enumerate(res):
        if score == minimum:
            print(idx+1,end=" ")