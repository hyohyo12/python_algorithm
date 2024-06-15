import sys
input = sys.stdin.readline
inf = sys.maxsize

#문제의 거리 계산하는 간단한 함수
def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

#백트래킹 함수
def chicken_dist(chicken:list[int],house:list[int],m:int,cur:list,idx:int)->None:
    global res#메인의 res를 global로 가져온다
    if len(cur) == m: #cur(현재 치킨집의 좌표가 튜플 형식으로 들어있는 리스트) 그 리스트의 개수가 m개라면
        val = 0 #현재 도시 치킨 거리 초기화
        for h in house: #모든 집에 대해서
            tmp = inf #현재 집의 치킨 거리를 계산하기위해 무한대로 초기화
            for c in cur:#모든 cur에 저장된 치킨집에 대해
                tmp = min(distance(h,c),tmp) #거리가 제일 작은 치킨 집을 tmp에 저장
            val += tmp #해당 치킨거리 더해준다
        res = min(res,val)#모든 집에 대한 치킨거리를 저장한 val와 res중 작은 것 선택
        return
    for i in range(idx,len(chicken)):#조합을 만들기 위해 치킨집 탐색
        cur.append(chicken[i])#i번째 치킨집을 더해준다
        chicken_dist(chicken,house,m,cur,i+1)#조합을위해 다음 탐색엔 i+1 번 부터 진행한다
        cur.pop()#백트래킹
        
if __name__ == "__main__":
    res = inf #정답을 저장할 변수 무한대로 초기화
    n,m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    res = inf
    chicken = []
    house = []
    #리스트 탐색하여 치킨집,가정집 좌표를 각각 리스트에 저장한다
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house.append((i,j))
            elif graph[i][j] == 2:
                chicken.append((i,j))
    chicken_dist(chicken,house,m,[],0)
    print(res)