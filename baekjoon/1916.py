import heapq
def djikstra(graph,start,n,end) -> list[int]:
    costs = [1e9 for _ in range(n+1)] #비용을 매우 큰 수로 초기화
    heap = [] #가중치와 정점을 저장할 힙
    heapq.heappush(heap,[0,start]) # 시작 정점의 정점 번호와 가치를 저장함
    costs[start] = 0 #시작정점의 가치를 0으로 시작
    while heap: #그래프 순회
        cur_cost,cur_v = heapq.heappop(heap) #현재 가치와 현재 정점을 각각 힙에서 꺼냄(현재 가장 가까운 정점)
        if costs[cur_v] < cur_cost: #현재 정점의 가치보다 이전에 저장한 가치가 더 작다면
            continue
        for next_v,next_cost in graph[cur_v]: #연결된 정점을 순회하며
            sum_cost = cur_cost + next_cost #현재 정점을 통해 해당 정점으로 가는 가치를 저장
            if sum_cost >= costs[next_v]: #저장한 가치가 더 크면 
                continue #이미 더 크면 안되니깐 넘어가
            costs[next_v] = sum_cost #현재 가치로 업데이트
            heapq.heappush(heap,[sum_cost,next_v]) #최소힙에 넣음
    return costs[end] #해당값의 가중치 출력


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s,d,v = map(int,input().split())
        graph[s].append([d,v])
    start,end = map(int,input().split())
    print(djikstra(graph,start,n,end))
