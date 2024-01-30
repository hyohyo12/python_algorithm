import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline
def dijkstra(graph,v,k):
    costs = [INF for _ in range(v+1)]
    heap = []
    costs[k] = 0
    heapq.heappush(heap,(0,k))
    while heap:
        cur_c,cur_v = heapq.heappop(heap)
        if cur_c > costs[cur_v]:
            continue
        for vertex,cost in graph[cur_v]:
            sum_cost = cost+cur_c
            if sum_cost < costs[vertex]:
                costs[vertex] = sum_cost
                heapq.heappush(heap,(sum_cost,vertex))
    return costs


if __name__ == "__main__":
    v,e = map(int,input().split())
    k = int(input())
    graph = [[] for _ in range(v+1)]
    for __ in range(e):
        s,d,c = map(int,input().split())
        graph[s].append([d,c])
    costs = dijkstra(graph,v,k)
    for i in range(1,v+1):
        print("INF" if costs[i] == INF else costs[i])