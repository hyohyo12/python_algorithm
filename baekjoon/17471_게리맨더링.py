import sys
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize

#구역이 서로 연결되면서 각 구역의 인구수 차이의 최소값을 리턴하는 함수
def minumum_diff(graph:list[list[int]],seq:list[int],n:int):
    #구역이 2개일 경우 2개 구역의 인구수 차이가 답
    if n == 2:
        return abs(seq[1]-seq[2])
    #나눈 구역의 인구수 차이를 저장할 res -> 최소값을 구하기 위해 inf(sys.maxsize)로 초기화
    res = inf
    #각 노드 번호들 전체 집합
    nodes = set(i for i in range(1,n+1))
    #모든 조합 저장하는 리스트
    combinations = []
    #조합 생성 함수
    def combination(depth,path:list[int],idx:int):
        #선택된 노드가 1개이상, n-1개 이하
        if 1 <= depth < n - 1:
            #조합 리스트에 저장
            combinations.append(path[:])
        #현재 탐색 idx부터 n까지 탐색
        for i in range(idx,n+1):
            #dfs 실행
            path.append(i)
            combination(depth+1,path,i+1)
            path.pop()
    
    #조합 생성 함수 호출
    combination(0,[],1)
    
    #각 구역이 서로 연결됐는지 확인할 bfs
    def bfs(selected:list[int]):
        #현재 구역의 인구수를 저장할 변수
        _sum = 0
        #중복 방문 방지를 위한 방문 리스트
        visited = [False for _ in range(n+1)]
        #BFS를 위한 덱(큐로 사용)
        q = deque([selected[0]])
        #현재 연결됐는지 확인하기위해 방문한 노드의 수를 저장할 cnt
        cnt = 0
        #시작 노드 True
        visited[selected[0]] = True
        #bfs
        while q:
            cnt += 1
            x = q.popleft()
            _sum += seq[x]
            #현재 노드에 연결된 노드중
            for i in graph[x]:
                #방문하지 않았고 선택된 노드에 있을때만 방문처리
                if not visited[i] and i in selected:
                    visited[i] = True
                    q.append(i)
        #방문한 곳이 선택된 노드의 개수와 다르다면 -1 을 리턴
        if cnt != len(selected):
            return -1
        #모두 연결됐을 땐 해당 구역 인구수 리턴
        else:
            return _sum
    #각 구역(노드)의 모든 조합에서
    for li in combinations:
        #현재 선택된 노드와 선택되지 않은 노드가 모두 각 구역끼리 연결됐다면
        no_sel = list(nodes - set(li))
        sel = bfs(li)
        if sel == -1:
            continue
        non_sel = bfs(no_sel)
        if non_sel == -1:
            continue
        #res를 갱신한다
        res = min(res,abs(non_sel-sel))
    #만약 res값이 변하지 않았다면 구역을 나눌 수 없다는 뜻으로 -1 리턴 나머지는 res(최솟값)리턴
    return res if res != inf else -1


#메인함수
def main():
    #입력
    #구역의 개수n
    n = int(input())
    #각 인구수를 저장할 리스트 앞에 0을 삽입해 인덱스 맞춤
    seq = [0]+list(map(int,input().split()))
    #그래프
    graph = [[] for _ in range(n+1)]
    
    #마을 개수만큼 연결된 노드를 입력받음
    for i in range(1,n+1):
        tmp = list(map(int,input().split()))
        for j in tmp[1:]:
            graph[i].append(j)
    
    print(minumum_diff(graph,seq,n))
if __name__ == '__main__':
    main()