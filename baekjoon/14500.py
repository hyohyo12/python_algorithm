import sys
input = sys.stdin.readline

def dfs(seq:list[int],cur:list[int],x:int,y:int,n:int,m:int,cnt:int)->int:
    global max_size
    if (4-cnt)*max_value+cur <= max_size:#만약 현재 모인 블록에 seq에서 제일 큰 값을 나머지 곱한 만큼 더한것이
        return #현재 최고 값보다 작다면 더 이상의 탐색은 무의미하므로 탐색 종료(가지 치기)
    if cnt == 4:#현재 블록이 4개 모였다면
        max_size = max(max_size,cur)#max_size(답)을 최고 값으로 갱신
        return
    for i in range(4):#상하 좌우 확인
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx < m and 0 <= ny < n:#인덱스 오류 방지
            if not visited[ny][nx]:#중복 방문 방지
                if cnt == 2:#'ㅗ'.'ㅜ','ㅏ','ㅓ' 의 값을 구하기 위해 블록 2개 모이면 하나를 더 붙이고 좌표값은 그대로 한다.
                    #해당 좌표의 'ㅗ','ㅜ' 모양일 땐 현재 좌표의 상하만을 탐색하고
                    #'ㅏ','ㅓ' 일땐 좌우만 확인 이미 visited에서 방문했다는 것을 저장했으므로.
                    visited[ny][nx] = True
                    dfs(seq,cur+seq[ny][nx],x,y,n,m,cnt+1)
                visited[ny][nx] = True
                dfs(seq,cur+seq[ny][nx],nx,ny,n,m,cnt+1)
                visited[ny][nx] = False
            

if __name__ == "__main__":
    #정답 변수(최대 값)
    max_size = 0
    #상하 좌우 확인
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    #입력
    n,m = map(int,input().split())
    seq = [list(map(int,input().split())) for _ in range(n)]
    #가지치기를 위한 큰 값 max_value에 저장
    max_value = max(map(max,seq))
    #중복 방문 방지를 위해 visited 리스트 크기는 seq와 동일
    visited = [[False for _ in range(m)] for _ in range(n)]
    #그래프 순회
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(seq,0,j,i,n,m,0)
            visited[i][j] = False
            
    #출력
    print(max_size)
    