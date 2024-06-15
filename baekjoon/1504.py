import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(graph:list[list[int]],start:int,n:int)->list[int]:
    costs = [inf for _ in range(n+1)]
    heap = []
    heapq.heappush(heap,(0,start))
    costs[start] = 0
    while heap:
        cur_c,cur_v = heapq.heappop(heap)
        if cur_c > costs[cur_v]:
            continue 
        
        for vertex,value in graph[cur_v]:
            sum_value = cur_c + value
            if sum_value < costs[vertex]:
                costs[vertex] = sum_value
                heapq.heappush(heap,(sum_value,vertex))
    
    return costs

if __name__ == "__main__":

    n,e = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(e):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    v1,v2 = map(int,input().split())

    start_costs = dijkstra(graph,1,n)
    v1_costs = dijkstra(graph,v1,n)
    v2_costs = dijkstra(graph,v2,n)
    
    v1_path = start_costs[v1] + v1_costs[v2] + v2_costs[n]
    v2_path = start_costs[v2] + v2_costs[v1] + v1_costs[n]
    
    ans = min(v1_path,v2_path)
    print(ans if ans < inf else -1) 