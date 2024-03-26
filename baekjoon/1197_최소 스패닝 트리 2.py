import sys
import heapq as hq
input = sys.stdin.readline

def prim(graph:list[list[int]],v:int):
    connected = [False for _ in range(v+1)]
    q = []
    hq.heappush(q,(0,1))
    weight_sum = 0
    while q:
        cost,vertex = hq.heappop(q)
        if not connected[vertex]:
            connected[vertex] = True
            weight_sum += cost
            for next_vertex,next_cost in graph[vertex]:
                if not connected[next_vertex]:
                    hq.heappush(q,(next_cost,next_vertex))
    return weight_sum

def main():
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    print(prim(graph,v))
if __name__ == "__main__":
    main()