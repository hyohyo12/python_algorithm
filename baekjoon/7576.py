from collections import deque
def bfs(graph:list[list[int]],start:deque):
    ans = 0 #하루가 얼마나 지났는지 저장할 변수
    dx = [0,0,1,-1] #앞,뒤,위,아래 만 영향을 줄 수 있으므로 이동할 수 있는 영역 구성한 리스트
    dy = [1,-1,0,0]
    while start: #탐방할 큐가 비어있을 때 까지(BFS완료 시점까지)
        ans += 1 #하루 한 번 지나고
        for i in range(len(start)): #모든 1(익은 토마토) 에서 부터
            x = start.popleft() #(y,x)
            for i in range(4): #4 방향으로 (위 아래 앞 뒤)
                if 0 <= (x[0]+dy[i]) < len(graph) and 0<= x[1]+dx[i] < len(graph[0]): #인덱스 에러 방지용
                    if graph[x[0]+dy[i]][x[1]+dx[i]] != -1 and graph[x[0]+dy[i]][x[1]+dx[i]] != 1: #이미 방문한 곳이 아니고 빈공간이 아닌 곳이면
                        start.append((x[0]+dy[i],x[1]+dx[i])) #다음에 탐색할 큐에 추가
                        graph[x[0]+dy[i]][x[1]+dx[i]] = 1 #방문 처리
    for row in graph: #그냥 0 있는지 확인 하는 거
        if 0 in row:
            return -1
    else:
        return ans-1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    m,n = map(int,input().split())
    start = deque() #시작 정점 저장할 큐
    tomatos = [] #그래프를 저장할 리스트
    for i in range(n):
        tomato = list(map(int,input().split()))
        if 1 in tomato:#삽입 과정에서 시작 지점을 알아냄
            for j in range(m):
                if tomato[j] == 1: #익은 토마토면
                    start.append((i,j)) # 그 좌표를 시작 큐에 넣어 i,j를 튜플로 묶어 넣음 각각 y,x값임
        tomatos.append(tomato) #탐색 후 리스트 추가
    print(bfs(tomatos,start))