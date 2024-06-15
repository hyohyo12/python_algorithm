import sys
inf = sys.maxsize
input = sys.stdin.readline

#bellman-ford 알고리즘
def bellman_ford(graph:list[list[int]],vertex:int,edge:int):
    dist = [inf] * (vertex+1)
    dist[1] = 0
    for _ in range(vertex-1):
        for v in range(1,vertex+1):
            for next,cost in graph[v]:
                if dist[v] != inf and dist[v] + cost < dist[next]:
                    dist[next] = dist[v] + cost
    
    for u in range(1,vertex+1):
        for v,w in graph[u]:
            if dist[u] != inf and dist[u] + w < dist[v]:
                return -1
    
    return dist


#메인 함수
def main():
    #입력
    #v-> 정접의 개수, e -> 간선의 개수
    v,e = map(int,input().split())
    #정점 개수만큼 그래프 리스트에 리스트 추가
    graph = [[] for _ in range(v+1)]
    #간선의 개수만큼 입력 받아 (목적지,비용) 을 튜플로 추가
    for _ in range(e):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
    
    res = bellman_ford(graph,v,e)
    if res == -1:
        print(-1)
    else:
        for r in res[2:]:
            print(r if r != inf else -1)


if __name__ == "__main__":
    main()