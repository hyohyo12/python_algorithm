import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize
def dijkstra(graph:list[list[int]],start:int):
    visited = [False for _ in range(n+1)]
    distance = [inf for _ in range(n+1)]
    distance[start] = 0
    visited[start] = True
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for vertex,vertex_cost in graph[now]:
            cost = vertex_cost + dist
            if cost < distance[vertex]:
                distance[vertex] = cost
                heapq.heappush(q,(cost,vertex))
    return distance


if __name__ == "__main__":
    n,m,x = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    
    res = 0
    
    for _ in range(m):
        s,e,c = map(int,input().split())
        graph[s].append((e,c))
    
    for i in range(1,n+1):
        go = dijkstra(graph,i)[x]
        back = dijkstra(graph,x)[i]
        res = max(go+back,res)
    print(res)