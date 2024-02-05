import sys
input = sys.stdin.readline
inf = sys.maxsize

def floyd_warshall(graph:list[list[int]],vertex:int)->list[list[int]]:
    #그래프를 순회하며 j에서 k로 가는 값을 j에서 i로 가고 i에서 k로 가는 값과 j에서 k로 가는 값을 비교하여 계속 갱신한다.
    for i in range(1,vertex+1):
        for j in range(1,vertex+1):
            for k in range(1,vertex+1):
                graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

if __name__ == "__main__":
    vertex = int(input())
    edge = int(input())
    graph = [[inf for _ in range(vertex+1)] for _ in range(vertex+1)] #모든 정점에 대해 최단 거리를 저장할 그래프(inf로 초기화)
    
    
    for i in range(1,vertex+1):
        for j in range(1,vertex+1):
            if i == j:#시작과 끝이 같다면 0
                graph[i][j] = 0
    
    for _ in range(edge):
        sp,ep,v = map(int,input().split())
        graph[sp][ep] = min(graph[sp][ep],v) #시작 도시와 도착 도시를 연결하는 노선이 하나가 아닐 수 있으므로 가격이 최솟값인 것을 선택하여 저장
    
    floyd_warshall(graph,vertex) #플로이드 워셜 알고리즘 실행
    
    for i in range(1,vertex+1):
        for j in range(1,vertex+1):
            print(0 if graph[i][j] == inf else graph[i][j],end = " ")
        print("")