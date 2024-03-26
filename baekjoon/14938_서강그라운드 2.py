import sys
import heapq
input = sys.stdin.readline

inf = sys.maxsize

def dijkstra(board:list[list[int]],start:int,n:int):
    distance = [inf for _ in range(n+1)]
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        cur_cost,vertex =heapq.heappop(q)
        if cur_cost > distance[vertex]:
            continue
        for next_vertex,next_cost in board[vertex]:
            cost = next_cost+cur_cost
            if distance[next_vertex] > cost:
                distance[next_vertex] = cost
                heapq.heappush(q,(cost,next_vertex))
    return distance
            

def main():
    res = 0
    n,m,r = map(int,input().split())
    board = [[] for _ in range(n+1)]
    items = [0] + list(map(int,input().split()))
    
    for _ in range(r):
        start,end,cost = map(int,input().split())
        board[start].append((end,cost))
        board[end].append((start,cost))
    
    for i in range(1,n+1):
        tmp = 0
        distance = dijkstra(board,i,n)
        for j in range(1,n+1):
            if distance[j] <= m:
                tmp += items[j]
        res = max(tmp,res)
    print(res)
if __name__ == "__main__":
    main()