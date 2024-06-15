import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

#상하좌우 이동 리스트
dx = [0,0,1,-1]
dy = [1,-1,0,0]


#제일 큰 블록 그룹을 찾는 함수
def find_group(board:list[list[int]],n:int):
    #중복 방문 제어를 위한 board크기의 방문 리스트
    visited = [[False for _ in range(n)] for _ in range(n)]
    #제일 큰 그룹의 좌표들을 저장할 빈 리스트
    remove_list = []
    #board를 순회하면서 제일 큰 블록 그룹을 bfs를 이용해 찾음
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > 0:
                color = board[i][j]
                #bfs탐색을위한 큐 -> deque로 설정
                q = deque([(i,j)])
                #해당 그룹의 크기,무지개블록 개수,그룹 기준의 열 인덱스,행 인덱스 그리고 그룹의 요소의 좌표를 저장하기 위한 리스트
                tmp= [0,0,i,j]
                visited[i][j] = True
                rainbows = []
                #BFS실행
                while q:
                    y,x = q.popleft()
                    #크기 증가
                    tmp[0] += 1
                    tmp.append((y,x))
                    for d in range(4):
                        nx,ny = x + dx[d],y + dy[d]
                        #인덱스 에러 및 중복 방문 방지
                        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                            #해당 하는 곳의 색이 현재 그룹의 색상과 일치하거나 무지개 색일 경우에만 탐색
                            if board[ny][nx] == color or board[ny][nx] == 0:
                                q.append((ny,nx))
                                #무지개색 블록이면
                                if board[ny][nx] == 0:
                                    #무지개 블록 개수 + 1
                                    tmp[1] += 1
                                    rainbows.append((ny,nx))
                                #방문 처리
                                visited[ny][nx] = True
                #그룹의 크기가 2이상일 경우에만 그룹으로 인정
                if tmp[0] >= 2:
                    remove_list.append(tmp)
                for y,x in rainbows:
                    visited[y][x] = False
    if len(remove_list):
        remove_list.sort(key = lambda x:(-x[0],-x[1],-x[2],-x[3]))
        return remove_list[0]
    #remove_list 가 빈 리스트일 시 그룹이 없다는 뜻 -> 처리 필요
    return remove_list

#board 를 시계방향으로 90도 회전시키는 함수
def turn_board(board:list[list[int]],n:int)->list[list[int]]:
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[n-j-1][i] = board[i][j]
    return new_board

def gravity(board:list[list[int]],n:int):
    for x in range(n):
        for y in range(n-2,-1,-1):
            if board[y][x] != -1:
                p = y
                while p + 1 < n and board[p+1][x] == -2:
                    board[p+1][x] =  board[p][x]
                    board[p][x] = -2
                    p += 1
    return board



def main():
    #점수 저장할 변수
    score = 0
    #입력
    #nxn 크기의 board, m -> m개의 색
    n,m = map(int,input().split())
    #board의 각 요소: -1 -> 검은색, 0 -> 무지개색, 나머지 -> 일반
    board = [list(map(int,input().split())) for _ in range(n)]
    while True:
        group = find_group(board,n)
        if not len(group):
            break
        for y,x in group[4:]:
            board[y][x] = -2
        score += (group[0] ** 2)
        board = gravity(board,n)
        board = turn_board(board,n)
        board = gravity(board,n)
    print(score)


if __name__ == "__main__":
    main()
