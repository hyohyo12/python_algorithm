import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph:list[list],depth:int,cur:int,visited:list[bool]):
    for nv in graph[cur]:
        if not visited[nv]:
            depth += 1
            visited[nv] = dfs(graph,depth,nv,visited)
    return depth

#메인 함수
def main():
    global cur_depth
    #입력
    #n -> 정점(컴퓨터) 수, m -> 간선(연결) 수
    n,m = map(int,input().split())
    #인접 리스트 구성(인덱스 맞추기위해 n+1개로 구성
    graph = [[] for _ in range(n+1)]
    #간선 수 만큼 간선 입력
    for _ in range(m):
        #s -> 시작 지점, e -> 끝 지점
        s,e = map(int,input().split())
        #양방향 그래프로 구성
        graph[e].append(s)
    
    result = []
    visited = [0 for _ in range(n+1)]
    max_depth = -sys.maxsize
    
    for i in range(1,n+1):
        if visited[i] == 0:
            cur_depth = 0
            visited[i] = dfs(graph,0,i,visited)
            max_depth = max(max_depth,cur_depth)
    print(visited)

if __name__ == "__main__":
    cur_depth = 0
    main()