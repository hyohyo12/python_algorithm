import sys
input = sys.stdin.readline

#DFS함수
def dfs(depth:int,graph:list[list[int]],cur_v:int):
    #방문 리스트를 전역변수로 씀
    global visited
    #깁이가 5이면(0부터 시작했으므로)
    if depth == 4:
        #True 리턴
        return True
    #해당 정점에서의 인접 정점 순회
    for i in graph[cur_v]:
        #방문 하지 않았다면
        if not visited[i]:
            #방문 처리
            visited[i] = True
            #탐색
            if dfs(depth+1,graph,i):
                #깊이가 5이상인 노선 탐색시 True리턴
                return True
            #탐색 실패시 False리턴
            visited[i] = False
    #탐색 실패
    return False


#메인함수
def main():
    #방문 리스트를 global로 선언
    global visited
    #입력
    #vertex -> 간선 수, edge -> 간선 수
    vertex,edge = map(int,input().split())
    #그래프 인접 리스트로 선언
    graph = [[] for _ in range(vertex)]
    #방문 리스트를 정점 수 만큼 False로 초기화
    visited = [False] * (vertex)
    #간선 수 만큼 간선 입력
    for _ in range(edge):
        #s -> 시작 지점, e -> 종점
        s,e = map(int,input().split())
        #양방향 그래프이므로 시작,종점 모두 추가
        graph[s].append(e)
        graph[e].append(s)
    #정점 수 만큼 반복하며 깊이가 5이상인지 판별
    for i in range(vertex):
        #시작 정점 방문으로 초기화
        visited[i] = True
        #dfs를 통해 해당 정점으로 시작시 깊이가 5이상이 되는지 판별
        if dfs(0,graph,i):
            #깊이가 5이상이면 1을 출력
            print(1)
            return
        #5이상이 되지 않으면 다음 탐색을위해 i번째 방문 False로 초기화
        visited[i]=False
    #깊이가 5이상인 노선이 없다면 0을 출력
    print(0)



if __name__ == "__main__":
    #dfs를 위한 방문리스트 전역 변수로 선언
    visited = []
    main()