import sys
from collections import deque
input = sys.stdin.readline

#방문 순서가 BFS로 이루어졌는지 검증하는 함수
def is_possible(n:int):
    global graph
    global seq
    q = deque()
    q.append(1)
    visited = [False for _ in range(n+1)]
    visited[1] = True
    idx = 1
    while q:
        x = q.popleft()
        childs = []
        for c in graph[x]:
            if not visited[c]:
                visited[c] = True
                childs.append(c)
        if sorted(childs) == sorted(seq[idx:idx+len(childs)]):
            for c in seq[idx:idx+len(childs)]:
                q.append(c)
            idx += len(childs)
        else:
            return 0
    return 1


#메인 함수
def main():
    global graph
    global seq
    #입력
    #n -> n개의 정점
    n = int(input())
    #그래프 정보를 저장할 리스트 graph
    graph = [[] for _ in range(n+1)]
    #n개의 정점 연결 정보 저장
    for _ in range(n-1):
        v1,v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    #검증할 방문 순서 입력
    seq = list(map(int,input().split()))
    if seq[0] != 1:
        print(0)
    else:
        print(is_possible(n))
    



if __name__ == "__main__":
    graph = []
    seq = []
    main()