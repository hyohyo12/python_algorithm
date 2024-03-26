import heapq

def dijkstra(graph: list[list[int]],n:int,m:int):
    heap = []
    costs = [1e9 for _ in range(n+1)]
    heapq.heappush(heap,(1,0))
    costs[1] = 0
    
    while heap:
        cur_v,cur_c = heapq.heappop(heap)
        if cur_c > costs[cur_v]:
            continue
        for vertex,value in graph[cur_v]:
            sum_value = value+cur_c
            if sum_value < costs[vertex]:
                costs[vertex] = sum_value
                heapq.heappush(heap,(vertex,sum_value))
    return costs[n]



if __name__ == "__main__":
    import sys
    read = sys.stdin.readline
    
    n,m = map(int,read().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,d,v = map(int,read().split())
        graph[s].append([d,v])
        graph[d].append([s,v])
    print(dijkstra(graph,n,m))
