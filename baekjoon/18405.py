import sys
from collections import deque
input = sys.stdin.readline

#방향 리스트
dx = [0,0,-1,1]
dy = [1,-1,0,0]
board = []

#bfs함수
def bfs(n:int,coord:list[int],s:int):
    #main 함수의 board 를 사용하기 위해 GLOBAL로 선언한 board
    global board
    #현재의 시간(초)를 저장할 변수
    cnt = 0
    #q에 저장한 좌표들을 큐에서 deque자료형으로 변경 BFS를 위해 큐로 사용해야하므로 덱 자료형으로
    q = deque(coord)
    #BFS
    while q:
        #현재 초 가 s(입력받은 종료되는 시각) 일때 BFS종료
        if cnt == s:
            break
        #deque에 있는 현재 모든 요소에 대해서 상하좌우 검색
        for _ in range(len(q)):
            #cur -> 해당 좌표의 숫자, y->y축, x-> x축
            cur,y,x = q.popleft()
            #4방향 상하좌우 탐색
            for i in range(4):
                #이동한 곳의 좌표
                ny = y+dy[i]; nx = x+dx[i]
                #인덱스 에러 방지
                if 0 <= ny < n and 0 <= nx < n:
                    #이동할 곳의 좌표가 0일때
                    if board[ny][nx] == 0:
                        #해당 좌표에 해당 숫자 바이러스가 퍼졌으므로 숫자 변경
                        board[ny][nx] = cur
                        #다음 탐색을위해 큐에 저장
                        q.append((cur,ny,nx))
                        #해당 하는 곳이 0일때만 큐에 넣어서 중복 방지
        cnt += 1
        
#메인 함수
def main():
    #메인 함수와 BFS 함수에서 쓰기 위해 GLOBAL 로 선언한 board
    #board 는 그래프를 저장
    global board
    #n x n Board, k이하의 숫자의 바이러스만 저장
    n,k = map(int,input().split())
    #coord(좌표를 저장하는 리스트)
    coord = []
    board = []
    #n x n 의 board 입력
    for i in range(n):
        #tmp -> 현재 삽입할 리스트를 임시로 저장한느 변수
        tmp = list(map(int,input().split()))
        #삽입할 리스트의 요소를 0이 아닌 숫자가 있다면 탐색해야하는 좌표이므로 coord리스트에 삽입
        for j in range(n):
            if tmp[j] != 0:
                #(해당 바이러스 숫자, y값, x값) 으로 좌표 저장(작은 숫자의 바이러스부터 확산되므로 정렬해야하기 때문에 board에 저장되어 있는 숫자를 0번째 인덱스로 설정)
                coord.append((tmp[j],i,j))
        #board에 삽입할 리스트 저장
        board.append(tmp)
    #s 초가 지났을 때 board[x][y] 값이 무엇인지(x와 y 모두 인덱스 1번부터 시작 따라서 각각 -1 한 값을 넣어서 탐색한다.)
    s,x,y = map(int,input().split())
    #바이러스는 작은 수부터 확산되므로, 오름차순 정렬(1번째 요소에 대해서)
    coord.sort()
    #bfs 실행
    bfs(n,coord,s)
    print(board[x-1][y-1])
    
    
if __name__ == "__main__":
    main()