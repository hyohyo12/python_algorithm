import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque

#이동 리스트
dx = [0,0,1,-1]
dy = [1,-1,0,0]
#언제 치즈가 사라지는지 마지막 치즈의 개수를 리턴하는 함수
def when_cheese_empty(board:list[list[int]],cheese:int)->tuple[int,int]:
    #만약 하루만에 치즈가 다 사라졌을 때 출력할 마지막 치즈의 개수
    origin_cheese = cheese
    #그 외 2일이상만에 치즈가 다 사라졌을 때 출력할 치즈의 개수와 걸린 시간
    count = []
    #치즈가 다 사라질 동안
    while cheese:
        #bfs를 통해 제거해야할 치즈의 위치(제거 리스트) 생성
        remove_seq = bfs(board)
        #해당 리스트 순회하며
        for i in range(r):
            for j in range(c):
                #해당하는 위치가 True라면
                if remove_seq[i][j]:
                    #해당 치즈는 제거되고 치즈의 개수도 업데이트
                    board[i][j] = 0
                    cheese -= 1
        #치즈의 개수 저장
        count.append(cheese)
    #치즈의 개수 2개 이상일 때 count리스트의 길이: 걸린시간, 마지막 치즈의 개수 리턴
    #그 외(하루 만에 사라졌을 때) 1과 원래 치즈 개수를 리턴
    return (len(count),count[-2]) if len(count) > 1 else (1,origin_cheese)

#Board 를 BFS로 순회하며, 공기와 맞닿은 치즈의 위치를 2차원 배열로 리턴하는 함수
def bfs(board:list[list[int]]) -> list[list[int]]:
    #방문 리스트
    visited = [[False for _ in range(c)] for _ in range(r)]
    #방문리스트와 같은 형태의 공기와 맞닿은(제거 해야할) 치즈 위치 리스트
    remove_seq = deepcopy(visited)
    #가장자리는 무조건 공기 이므로, 시작 지점으로 설정
    q = deque([(0,0)])
    #방문 처리
    visited[0][0] = True
    #BFS 실행
    while q:
        y,x = q.popleft()
        #상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #인덱스 에러 방지 그리고 중복 방문 방지
            if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx]:
                #해당 방문하려는 위치에 치즈가 있다면(공기와 맞닿아 있으면)
                if board[ny][nx] == 1:
                    #제거 리스트에 해당 위치를 True로 설정
                    remove_seq[ny][nx] = True
                    #방문 처리만하고, 큐에는 저장하지 않는다.
                    visited[ny][nx] = True
                    continue
                #공기일 때에만 큐에 저장을 한다.
                visited[ny][nx] = True
                q.append((ny,nx))
    return remove_seq

if __name__ == "__main__":
    #치즈의 개수 저장할 변수
    cheese = 0
    #rxc의 보드 생성
    r,c = map(int,input().split())
    board = []
    for i in range(r):
        tmp = list(map(int,input().split()))
        #cheese에 1(치즈)의 개수 저장
        cheese += tmp.count(1)
        board.append(tmp)
    #언제 치즈가 모두 사라지는지, 마지막 치즈의 개수 리턴하는 함수
    when,left = when_cheese_empty(board,cheese)
    print(when)
    print(left)