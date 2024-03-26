import sys
from collections import deque,defaultdict
input = sys.stdin.readline

#오른쪽 왼쪽 움직이는 함수
def turn(d):
    #방향을 말해주는 글로벌 변수
    global direction
    #왼쪽
    if d == 'L':
        #현재 방향(인덱스)에서 +1
        direction = (direction+1)%4
    #오른쪽
    elif d == 'D':
        #현재 방향(인덱스)에서 -1
        direction = (direction-1)%4

def when_end(n:int,board:list[list[int]],trans_timing:defaultdict(str))->int:
    #오른쪽,아래,왼쪽,위 순으로 만약 왼쪽으로 가고있다면 'D'일때 현재 방향 -1 이므로 위로 'L'이면 +1이므로 위로
def turn(d):
    global direction
    if d == 'L':
        direction = (direction+1)%4
    elif d == 'D':
        direction = (direction-1)%4
    # else:return

def when_end(n:int,board:list[list[int]],trans_timing:defaultdict(str))->int:
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    x,y = 0,0
    #뱀의 머리와 꼬리를 저장할 변수
    snake = deque([(0,0)])
    #몇 초에 끝났는지 저장할 변수
    count = 0
    while True:
        #1초가 지남
        count += 1
        #현재 위치 갱신
        x += dx[direction]
        y += dy[direction]
        
        #만약 현재 위치가 board를 벗어나면
        if x < 0 or x >= n or y < 0 or y >= n:
            #탐색 종료
            break
        #만약 현재 위치에 사과가 있다면
        if board[y][x] == 2:
            #머리 위치 갱신
            board[y][x] = 1
            #뱀의 몸 길이 갱신
            snake.append((y,x))
            #위치 변환 확인
            if trans_timing[count] != "":#defaultdict로 선언했기에 현재 방향 전환하지 않는다면 ""을 저장함.
                turn(trans_timing[count])
        #현재 위치에 사과가 없다면
        elif board[y][x] == 0:
            #현재 머리 위치 갱신
            board[y][x] = 1
            #뱀의 몸 길이 갱신
            snake.append((y,x))
            #사과가 없으므로 꼬리 한 칸 앞으로
            p_y,p_x = snake.popleft()
            #현재 꼬리 위치 갱신
            board[p_y][p_x] = 0
            #위치 변환 확인
            if trans_timing[count] != "":#defaultdict로 선언했기에 현재 방향 전환하지 않는다면 ""을 저장함.
            if trans_timing[count] != "":
                turn(trans_timing[count])
        else:
            break
    #몇 초 지났는지 리턴
    return count
if __name__ == "__main__":
    #입력
    #n x n 보드
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1
    #사과의 개수
    k = int(input())
    #사과의 좌표
    for _ in range(k):
        x,y = map(int,input().split())
        board[x-1][y-1] = 2
    #방향 변환 횟수
    l = int(input())
    #방향 변환 정보 저장할 딕셔너리(오름차순으로 입력)
    trans_timing = defaultdict(str)
    for _ in range(l):
        #x -> 방향 변환할 시간, c -> 변환될 방향 L:왼쪽 ,D:오른쪽 각각 90도씩
        x,c = input().strip().split()
        trans_timing[int(x)] = c
    #현재 방향을 나타내는 변수
    direction = 0
    
    ]]
    #함수 실행 및 정답 출력
    print(when_end(n,board,trans_timing))