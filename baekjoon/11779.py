import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize
def dijkstra(graph:list[list[int]],n:int,start:int,end:int):
    q = [(0,start)]
    costs = [inf for _ in range(n+1)]
    route = [0]*(n+1)
    costs[start] = 0
    while q:
        cur_c,cur_v = heapq.heappop(q)
        if cur_c > costs[cur_v]:
            continue
        for vertex,cost in graph[cur_v]:
            sum_c = cost + cur_c
            if costs[vertex] > sum_c:
                route[vertex] = cur_v
                costs[vertex] = sum_c
                heapq.heappush(q,(sum_c,vertex))

    print(costs[end])
    now = end
    path = [now]
    while now != start:
        now = route[now]
        path.append(now)
    path.reverse()
    return path
if __name__ == "__main__":
    n = int(input())
    e = int(input())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(e):
        s,d,c = map(int,input().split())
        graph[s].append((d,c))

    start,end = map(int,input().split())
    path = dijkstra(graph,n,start,end)
    print(len(path))
    print(*path)