import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dp = []
graph = []
#상하좌우 방향 리스트
dx = [0,0,-1,1]
dy = [1,-1,0,0]

#높이가 낮은 위치로만 이동해 맨 오른쪽 아래 위치로 갈 수 있는 경로를 리턴하는 함수
def dfs(cur_y:int,cur_x:int,n:int,m:int):
    #글로벌 변수 그래프,dp테이블
    global graph
    global dp
    #맨 아래 맨 오르쪽 위치한다면 1을 리턴하여 처음 경로의 값을 설정
    if cur_y == m -1 and cur_x == n - 1:
        return 1
    #만약 이미 방문한 곳이라면 중복 탐색을하지 않고 해당 위치의 dp 값을 리턴
    if dp[cur_y][cur_x] != -1:
        return dp[cur_y][cur_x]
    #해당 위치의 경로 개수를 저장하는 변수
    _case = 0
    #4방향 상하좌우 탐색
    for i in range(4):
        #다음 방향 ny,nx
        nx,ny = cur_x + dx[i],cur_y + dy[i]
        #인덱스 에러 방지, 현재 위치보다 낮다면
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] < graph[cur_y][cur_x]:
            #dfs호줄을하여 해당 경로에서 맨 아래 맨 오른쪽 위치가 있다면 1을 추가
            #또는 이미 방문한 곳이라면 해당 이미 방문한 dp의 값을 더할 것.
            _case += dfs(ny,nx,n,m)
    #현재 위치의 경로 dp 테이블 최신화
    dp[cur_y][cur_x] = _case
    #탐색 마치고 현재 위치 의 dp값을 리턴
    return dp[cur_y][cur_x]

#메인 함수
def main():
    #글로벌 변수 dp테이블,그래프
    global dp
    global graph
    #입력
    #m x n 그래프(board)
    m,n = map(int,input().split())
    #그래프 입력
    graph = [list(map(int,input().split())) for _ in range(m)]
    #중복 탐색 방지를 위해 -1로 dp테이블 초기화
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    #dfs함수 호출 후 출력
    print(dfs(0,0,n,m))

if __name__ == "__main__":
    main()