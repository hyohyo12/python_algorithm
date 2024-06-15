#분기 한정 기법
#실패 (시간 초과)
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
res = 0
#판다의 최대 이동을 구하는 리스트
def max_movement(board:list[list[int]],n:int,table:defaultdict[int]):
    global res
    res = 0
    #하, 상 , 좌, 우 방향 리스트
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    #중복 방문 방지를 위한 방문 리스트
    visited = [[False for _ in range(n)] for _ in range(n)]
    #dfs 함수
    def dfs(cur,y,x):
        #최고 이동 거리를 저장할 변수 res
        global res
        #res를 항상 최신화 시킨다
        res = max(res,cur)
        #현재 위치의 나무보다 큰 나무의 개수 + 현재 판다의 이동거리가 res보다 작거나 같으면 탐색을 종료한다.
        if table[board[y][x]] + cur <= res:
            return
        #하,상,좌,우 4방향 탐색
        for i in range(4):
            #nx,ny 다음 위치
            nx = x + dx[i];ny = y + dy[i]
            #인덱스 에러 방지와 중복 방문 검사
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                #현재 나무의 크기보다 다음 나무가 커야 하므로 검사
                if board[ny][nx] > board[y][x]:
                    #다음 노드의 방문 처리 후 재귀호출
                    visited[ny][nx] = True
                    #cur(depth) + 1 한 뒤 dfs재귀 호출
                    dfs(cur+1,ny,nx)
                    #다음 탐색을 위해 방문 방문리스트 원상복귀
                    visited[ny][nx] = False
    #board 순회하며 dfs
    for i in range(n):
        for j in range(n):
            #현재 나무보다 큰 나무의 개수가 res보다 크거나 작다면 최신화 할 수 없으므로 탐색 하지 않음
            if table[board[i][j]] <= res:
                continue
            #방문 처리후 dfs시작
            visited[i][j] = True
            dfs(1,i,j)
            visited[i][j] = False
    #결과값 (판다 이동 거리 최댓값) 반환
    return res
#메인 함수
def main():
    #입력
    #n x n 크기의 board
    n = int(input())
    #n x n 크기의 board
    board = []
    #대나무의 크기를 저장할 리스트(분기 한정을 위해)
    trees = []
    #n x n크기의 board 구성 입력
    for i in range(n):
        #board에 저장하기 전에 tmp에 임시로 저장
        tmp = list(map(int,input().split()))
        #tmp 리스트 순회
        for j in range(n):
            #나무의 크기를 trees에 저장
            trees.append(tmp[j])
        #board 입력 받은 리스트 저장
        board.append(tmp)
    #나무를 크기 순으로 정렬
    trees.sort()
    #해당 나무 크기보다 큰 나무의 개수를 저장할 딕셔너리 -> DFS 를 돌릴 때 깊이(이동 거리) + 현재 나무보다 큰 나무의 개수 가 현재 최댓값보다 작다면 탐색 종료하여 분기한정하기 위함.
    table = defaultdict(int)
    #나무의 크기를 순회할 때 전 나무의 크기를 저장할 임시변수 tmp 나무는 자연수이므로 0으로 초기화
    tmp = 0
    #table[0] 은 -1로 초기화
    table[0] = -1
    #나무 리스트 순회
    while trees:
        #나무 리스트에서 pop하여 맨 뒤 요소(남은 나무 중 제일 큰 나무의 크기) x에 저장
        x = trees.pop()
        #전의 나무의 값과 다르다면
        if x != tmp:
            #현재 나무에 누적 합을 더함
            table[x] += table[tmp]
            #누적합에 + 1
            table[x] += 1
            #tmp 를 현재 나무로 최신화 시킨다.
            tmp = x
        #전 나무의 크기와 현재 나무의 크기가 같을 때
        else:
            #table[x] 의 값에 + 1
            table[x] += 1
    print(max_movement(board,n,table))
if __name__ == "__main__":
    main()




