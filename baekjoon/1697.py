#숨바꼭질 1697
from collections import deque
max = 100000  #범위가 100000까지임
def bfs(n,k): #넓이우선탐색
    dist = [0]*(max+1) #탐색했는가 그리고 몇번째 탐색인지 저장하는 리스트
    q = deque([n]) # 그래프 탐색 큐
    while q: #탐색
        x = q.popleft() #현재 정점 x
        if x == k: # 현재 값이 원하는 값인 가 검색
            print(dist[x]) # 몇번째 탐색인지 저장하는 리스트기 때문에 바로 출력
            break # 탐색 종료
        for i in (x-1,x+1,x*2): # 원하는 값이 아니면 각각의 값을 탐색완료 표시와 몇번째 탐색인지 그리고 큐에 저장
            if 0 <= i <= max and dist[i] == 0: # i 값이 0보다 크거나 작고 max(100000) 값 보다 작아야하고 이미 탐색했으면 넘어가기
                dist[i] = dist[x] + 1 # 현재 i 값에 대응하는 dist 리스트에 부모 노드의 값 +1 을하여 몇 번째 탐색인지 저장
                q.append(i) # 그래프 탐색 큐에 다음 탐색할 i 저장
if __name__ == '__main__':
    n,k = map(int,input().split())
    bfs(n,k)