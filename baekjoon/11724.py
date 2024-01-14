from collections import deque
def bfs(graph,vertex,visited):
    q = deque([]) #BFS 위한 큐
    vlist = set() #방문한 정점 확인하기 위한 set 자료구조
    ans = 0 # 필요한 연결 요소 개수 저장할 변수
    
    while vertex: #모든 정점 돌 때까지
        ans+=1 #연결 요소 하나 추가
        q.append(vertex[0]) #큐에 시작 정점 추가
        vlist.add(vertex[0])#방문 정점 확인할 set에 시작 정점 추가
        visited[vertex[0]] = True # 방문처리
        while q: #BFS 시작(이거 다 돌아도 그래프를 완전히 돈 것이 아님)
            x = q.popleft() 
            for i in graph[x]:#그래프에 연결된 정점
                if not visited[i]: #방문 안했으면
                    q.append(i) #다음 방문을 위해 큐에 추가
                    visited[i] = True #방문 처리
                    vlist.add(i) #set에 add
        vertex = list(set(vertex)-vlist) #위에 하나의 모든 사이클 돌고 남은 정점 확인하는 것
        vlist = set() # 다시 초기화
    return ans

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    vertex = [i for i in range(1,n+1)] #정점을 저장하는 리스트 1부터 n까지
    visited = [False] *(n+1) #방문 처리 리스트
    graph = [[] for _ in range(n+1)] #리스트 저장할 리스트
    for i in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)#무방향이라 u - v , v-u 모두 넣었음
        graph[v].append(u)
    print(bfs(graph,vertex,visited))