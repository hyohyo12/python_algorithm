# dp + dfs
# 통과
import sys
input = sys.stdin.readline
#방향 리스트 (상,하,좌,우)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
#판다의 최대 이동을 구하는 함수
def max_movement(board:list[list[int]],n:int,trees:list[int]):
    #각 칸의 최적해를 저장할 dp테이블
    dp = [[0 for _ in range(n)] for _ in range(n)]
    #중복 방문 방지를 위한 방문 리스트
    visited = [[False for _ in range(n)] for _ in range(n)]
    #판다의 최대 이동 거리를 구하기 위한 dfs함수 dp + 완전 탐색
    def dfs(cur,y,x):
        #판다의 이동 횟수의 변화를 감지할 변수
        cnt = 4
        #상,하,좌,우 4방향 이동
        for i in range(4):
            #판다의 다음 이동 위치
            ny = y + dy[i]; nx = x + dx[i]
            #인덱스 에러 방지와 중복 방문 검사
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                #판다의 다음위치의 나무 크기와 현재 나무 크기보다 커야하므로 검사
                if board[ny][nx] > board[y][x]:
                    #모두 만족 했을 때 다음 위치의 최적해가 존재 하였을 때
                    if dp[ny][nx]:
                        #최적해를 사용하여 겹치는 부분 문제를 또 연산하는 불필요한 연산을 줄임
                        dp[y][x] = max(dp[y][x],dp[ny][nx] + 1)
                        #판다가 움직였으므로 움직임 감지 변수 변경
                        cnt -= 1
                        #해당 위치 탐색 종료
                        continue
                    #최적해가 없다면 최적해를 구해야하므로 dfs를 진행한다
                    #중복 방문 방지를 위해 True
                    visited[ny][nx] = True
                    #dfs재귀호출 cur(depth) + 1 해주어 이동 횟수 + 1
                    dfs(cur+1,ny,nx)
                    #현재의 최적해를 구한다.
                    dp[y][x] = max(dp[ny][nx] + 1,dp[y][x])
                    #다음 탐색을 위해 방문처리 해제
                    visited[ny][nx] = False
                    #이동 했으므로 움직임 감지 변수 변경
                    cnt -= 1
        #움직임이 없다면 해당 위치에선 이동할 수 있는 곳이 없으므로
        if cnt == 4:
            #해당 위치의 최적해를 1로 설정
            dp[y][x] = 1
            return
    #오름차순으로 정렬된 나무의 리스트 순회
    #오름차순으로 정렬하여 큰 나무들의 최적해를 구해 나간다.
    #큰 나무의 최적해가 구해져야 작은 나무들의 최적해를 구할 수 있으므로
    for t,y,x in trees:
        #이미 최적해 가 구해졌다면 탐색 하지 않음
        if dp[y][x]:
            continue
        #해당 위치의 최적해가 없다면 dfs실행하여 최적해 찾는다
        #탐색을 위해 방문 처리
        visited[y][x] = True
        #dfs호출
        dfs(1,y,x)
        #다음 탐색을 위해 해당 위치 False처리
        visited[y][x] = False
    #dp테이블의 최적해 중 제일 큰 값을 res에 저장
    res = 0
    for i in dp:
        res = max(max(i),res)
    #res를 리턴
    return res
#메인 함수
def main():
    #입력
    #n x n 크기의 board -> n 입력
    n = int(input())
    #board 저장할 변수
    board = []
    #나무의 (크기,y축 위치,x축 위치) 저장할 리스트
    trees = []
    #n x n 크기의 board 입력
    for i in range(n):
        #board 에 저장할 리스트 tmp 나무의 크기와 위치를 trees에 저장하기위해 임시변수에 임시로 저장
        tmp = list(map(int,input().split()))
        #tmp를 순회하여 나무의 크기 위치 저장
        for j in range(n):
            trees.append((tmp[j],i,j))
        #board에 임시 리스트 삽입
        board.append(tmp)
    #나무의 크기를 오름차순으로 정렬
    trees.sort(reverse=True)
    #max_movement의 반환값(판다의 이동거리 최댓값)을 출력
    print(max_movement(board,n,trees))
if __name__ == "__main__":
    #메인 함수 호출
    main()
    

