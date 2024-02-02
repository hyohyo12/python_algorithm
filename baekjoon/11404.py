import sys
input = sys.stdin.readline
inf = sys.maxsize

def floyd_warshall(graph:list[list[int]],vertex:int)->list[list[int]]:
    for i in range(1,vertex+1):
        for j in range(1,vertex+1):
            for k in range(1,vertex+1):
                graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

if __name__ == "__main__":
    vertex = int(input())
    edge = int(input())
    graph = [[inf for _ in range(vertex+1)] for _ in range(vertex+1)]
    
    for i in range(1,vertex+1):
        for j in range(1,vertex+1):
            if i == j:
                graph[i][j] = 0
    
    for _ in range(edge):
        sp,ep,v = map(int,input().split())
        graph[sp][ep] = min(graph[sp][ep],v)
    
    floyd_warshall(graph,vertex)
    
    for i in range(1,vertex+1):
        for j in range(1,vertex+1):
            print(0 if graph[i][j] == inf else graph[i][j],end = " ")
        print("")