import sys
from collections import deque
input = sys.stdin.readline

#상하좌우 이동 리스트
dx = [0,0,1,-1]
dy = [1,-1,0,0]


#최소 시간을 탐색하기 위해 백트래킹 함수 (depth:현재 깊이(현재 선택된 바이러스의 개수),virus:바이러스 좌표 리스트,current현재 선택된 바이러스)
#m:활성으로 선택될 바이러스의 개수
def find_min(depth:int,virus:list[int],current:list[int],m:int,idx:int):
    global min_time
    #깊이가 m과 같다면 (m개를 선택했다면)
    if depth == m:
        #bfs진행
        flag,research = bfs(current)
        #탐색 성공(모든 칸 복제 성공) 했으면 min_time 갱신
        if flag:
            min_time = min(min_time,research)
        return
    
    for i in range(idx,len(virus)):
        current.append((*virus[i],0))
        find_min(depth+1,virus,current,m,i+1)
        current.pop()

#바이러스 복제를 위한 BFS 탐색
#start -> dfs를 통해 얻은 현재의 활성하는 바이러스의 조합
def bfs(start:deque[int]):
    #board와 empty를 global변수로 사용
    global board
    global empty
    #bfs탐색을 위해 start를 덱 자료형으로 변경한 후 q에 저장
    q = deque(start)
    #현재 소요 시간을 저장할 cnt변수
    cnt = 0
    #empty 값이 오염되지 않도록 tmp 변수에 새로 저장
    tmp = empty
    #중복 방문 방지를 위한 방문 리스트
    visited = [[0 for _ in range(len(board))] for _ in range(len(board))]
    #bfs 탐색
    while q:
        #q에서 y,x,소요시간 popleft
        y,x,time = q.popleft()
        if board[y][x] == 0:
            tmp -= 1
        #소요 시간 갱신
        if tmp == 0:
            return (True,time)
        #상,하,좌,우 바이러스 복제
        for i in range(4):
            #다음 방문 좌표 (ny,nx)
            ny, nx = y + dy[i], x + dx[i]
            #좌표 인덱스 유효 검사, 방문 검사
            if is_valid_index(ny,nx) and not visited[ny][nx]:
                #방문 처리
                visited[ny][nx] = True
                #해당 칸이 빈 공간이면 빈 공간의 개수 저장한 tmp변수 - 1
                #복제를 했으므로 시간은 + 1
                # if board[ny][nx] == 0:
                q.append((ny,nx,time+1))
                #해당 칸이 비활성 바이러스가 있다면 소요 시간은 그대로, tmp도 그대로(empty에 이미 바이러스 제외하고 계산했으므로)
                # else:
                #     q.append((ny,nx,time))
    #tmp -> 빈 공간이 0 이면 True 와 소요시간 리턴하고 아니면 모든 칸 복제 실패했으므로 False 와 -1 리턴
    return (False,-1)

def is_valid_index(ny:int,nx:int):
    global board
    if 0 <= ny < len(board) and 0 <= nx < len(board) and board[ny][nx] != 1:
        return True
    return False

#메인 함수
def main(): 
    global empty
    global board
    global min_time
    #입력
    #nxn 크기
    n,m = map(int,input().split())
    #n 개의 row를 저장할 board 리스트
    board = []
    #빈 공간을 저장할 변수 empty
    empty = 0
    #바이러스의 위치를 저장할 virus 리스트
    virus = []
    #n개의 줄 입력받음
    for i in range(n):
        tmp = list(map(int,input().split()))
        #바이러스의 위치 탐색 또는 빈 공간의 개수를 저장하기 위해 열 검사
        for idx,t in enumerate(tmp):
            #t -> 0 : 빈 공간, t -> 2 : 바이러스
            if t == 0:
                empty += 1
            elif t == 2:
                #좌표 저장
                virus.append((i,idx))
        board.append(tmp)
    find_min(0,virus,[],m,0)
    if min_time == sys.maxsize:
        print(-1)
    else:print(min_time)

if __name__ == "__main__":
    min_time = sys.maxsize
    board = []
    empty = 0
    #메인함수 호출
    main()