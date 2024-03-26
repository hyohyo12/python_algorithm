import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
#이동리스트
dx = [-1,0,1]
dy = [0,-1,0]
#3명의 궁 위치에 따른 bfs로 몇 명의 적이 제거되었는지 반환하는 함수
def bfs(archor:tuple[int]) -> int:
    #다른 조합을 탐색해야하므로 board는 건들 수 없으므로 deepcopy를 하여 copy한다.
    c_board = deepcopy(board)
    #제거된 적들의 개수를 저장할 리스트
    remove_enemy = 0
    #방문리스트
    visited = [[False for _ in range(m)] for _ in range(n)]
    #적들이 앞으로 전진하는 것을 역방향으로 y값이 증가하는 것으로 구현
    for i in range(n-1,-1,-1):
        #다음 궁수까지 똑같은 board를 탐색해야하므로, 모든 궁수가 방문후 board를 업데이트해야한다.
        #그래서 리스트로 저장하여 모든 궁수가 bfs순회 일괄 제거처리(0)으로 변환.
        remove = []
        #3명의 궁수 위치에 대해
        for a in archor:
            #bfs실행
            q = deque()
            #i -> y축(적들 바로 앞), a -> x축 (궁수 위치),  1 -> d(현재까지 이동 횟수)
            q.append((i,a,1))
            while q:
                y,x,d = q.popleft()
                #현재 보드 위치의 값이 1 (적이 있다면)
                if c_board[y][x] == 1:
                    #모든 탐색후 일괄 제거해야하므로 제거리스트에 추가
                    remove.append((y,x))
                    #방문 한 적이 없다면.
                    if not visited[y][x]:
                        #처음 방문이므로 적을 제거하고
                        remove_enemy += 1
                        #방문 처리
                        visited[y][x] = True
                    #1번에 1명의 적만 제거 가능하므로 break
                    break
                #현재 이동 가능횟수가 D(이동 한계) 보다 작을 때
                if d < D:
                    #좌,상,우 방향으로 탐색
                    for j in range(3):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        #인덱스 에러방지
                        if 0 <= nx < m and 0 <= ny < n:
                            #다음 탐색을 위해 큐에 추가
                            q.append((ny,nx,d+1))
        #현재 순회를 마치고 제거해야할 적들을 일괄 처리
        for y,x in remove:
            c_board[y][x] = 0
    #제거한 적을 리턴한다
    return remove_enemy
#3명의 궁수가 있을 경우 모두(조합 생성) 리스트[튜플] 형식으로 반환하는 함수
def comb(r:int) -> list[tuple]:
    #조합들을 저장할 리스트
    combinations = []
    #dfs로 모든 조합을 생성하는 함수
    def dfs(r,cur:list[int],depth:int,idx:int):
        #3명의 궁수이므로 깊이가 3이면(3명의 궁수가 모이면)
        if depth == 3:
            #조합 저장 리스트에 해당 위치들 저장
            combinations.append(cur.copy())
            return
        #현재 인덱스부터 끝까지
        for i in range(idx,r):
            #i번째 넣고
            cur.append(i)
            dfs(r,cur,depth+1,i+1)
            #백트래킹
            cur.pop()
    dfs(r,[],0,0)
    return combinations

if __name__ == "__main__":
    n,m,D = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    
    res = 0
    
    coms = comb(m)
    #궁수가 있을 수 있는 x축에 모든 조합에 대해 순회
    for arc in coms:
        #매 순회마다 최고값으로 갱신
        res = max(res,bfs(arc))
    print(res)