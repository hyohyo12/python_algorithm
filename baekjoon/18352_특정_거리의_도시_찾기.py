import sys
import heapq
inf = sys.maxsize
input = sys.stdin.readline


def dijkstra(graph:list[list[int]],x:int,n:int)->list:
    distances = [inf for _ in range(n+1)]
    distances[x] = 0
    q = []
    heapq.heappush(q,(0,x))
    
    while q:
        cur_dist,cur_node = heapq.heappop(q)
        if distances[cur_node] < cur_dist:
            continue
        for next_node in graph[cur_node]:
            next_dist = cur_dist + 1
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                heapq.heappush(q,(next_dist,next_node))
    return distances


def main():
    n,m,k,x = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e = map(int,input().split())
        graph[s].append(e)
    dist = dijkstra(graph,x,n)
    flag = 1
    for i in range(1,n+1):
        if dist[i] == k:
            print(i)
            flag = 0
    if flag:
        print(-1)


if __name__ == "__main__":
    main()