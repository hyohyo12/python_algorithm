import sys
import copy
input = sys.stdin.readline
#모든 함수에서 사용 편하게 하기위해 전역 변수로 설정
#물고기의 번호와 방향 정보를 저장할 이차원 리스트
board = []
#1~16번 물고기의 위치 정보를 저장할 리스트 1~16번까지 순서대로 이동할 때 편하게 하기 위함.
fish = []
#결과값(상어가 먹은 물고기 번호의 합의 최댓값) 을 저장할 전역 변수
res = 0
#8개의 방향을 저장하는 방향 리스트
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
#board 를 매개변수로 받아 board에 있는 물고기들의 위치를 번호순으로 순차적으로 변경하는 함수
#(sy,sx) -> 상어의 위치
def move_fish(board:list[list[int]],sy:int,sx:int):
    #1번 물고기부터 16번 물고기까지 순차적으로 이동
    for i in range(1,17):
        #i번째 물고기가 존재할 때
        if fish[i]:
            #물고기의 현재 위치를 각각 y축,x축에 대해 y,x,에 저장
            y,x = fish[i]
            #board에 저장 되어 있는 해당 위치의 물고기의 번호와 방향을 각각 a,b 에 저장
            a,b = board[y][x]
            #물고기를 한바퀴 돌면서
            for _ in range(9):
                #다음 위치 ny,nx 방향 설정 -> 방향 리스트에서 방향에 따라 x,y를 이동 시킨 값
                nx = x + dx[b];ny = y + dy[b]
                #해당 좌표가 인덱스를 벗어나거나 해당 위치에 상어가 있다면
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    #방향을 반시계방향으로 업데이트
                    b = (b + 1) %  8
                    continue
                #위에 조건 인덱스 벗어나지도, 상어 위치도 아니라면
                #해당 물고기의 방향을 업데이트
                board[y][x][1] = b
                #다음 이동할 좌표에 물고기가 있다면 서로 위치를 변경해주는 작업이 추가로 필요
                if board[ny][nx]:
                    #해당 물고기가 있는 번호의 fish 좌표를 지금 이동중인 물고기의 좌표로 변경
                    fish[board[ny][nx][0]] = (y,x)
                #board에서 두 개의 좌표의 값을 서로 변경 시킴
                board[ny][nx],board[y][x] = board[y][x],board[ny][nx]
                #a번 현재 이동한 물고기의 fish에 저장된 좌표값을 업데이트
                fish[a] = (ny,nx)
                #물고기의 위치가 정해졌으므로 break
                break
    #모든 물고기의 위치가 변경됐다면 board를 리턴
    return board
#상어가 섭취한 물고기의 번호가 합의 최댓값을 구하기위해 완전 탐색을 진행하는 함수
#cur -> 현재까지 섭취한 물고기의 번호 합, y,x 는 현재 상어의 위치,dir 은 상어의 방향
def dfs(cur,y,x,dir):
    #위에서 정의한 전역 변수 res
    global res
    #위에서 정의한 전역 변수 board
    global board
    #위에서 정의한 전역 변수 fish
    global fish
    #물고기들의 움직임
    board = move_fish(board,y,x)
    #상어가 현재 방향 갈 수 있는 곳을 전체적으로 완전 탐색
    while True:
        #방향 리스트를 참조해 상어의 다음 위치 nx,ny
        nx = x + dx[dir]; ny = y + dy[dir]
        #상어의 다음 위치가 인덱스를 벗어나면 (board를 벗어나면)
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            #res를 최댓값으로 최신화
            res = max(res,cur)
            #해당 방향 탐색 종료
            return
        #상어의 다음 위치에 물고기가 없다면 이동이 불가능하므로 x,y 위치 최신화시키고 다음칸 탐색으로 이동
        if not board[ny][nx]:
            x = nx; y = ny
            continue
        #다음 탐색을 위해 board,fish 조작 후 다시 원상복귀(백트래킹)하기 위해 각 리스트 복사한 뒤 각 변수에 저장
        c_board = copy.deepcopy(board)
        c_fish = copy.copy(fish)
        #다음 상어의 위치에 있는 물고기의 정보 a -> 물고기의 번호, b -> 물고기의 방향을 저장
        a,b = board[ny][nx]
        #해당 위치의 물고기는 먹혔으므로 빈칸으로 둔다.
        #상어의 위치는 move_fish에 매개변수로 전달할 것이므로
        board[ny][nx] = []
        #먹힌 물고기의 위치도 삭제한다
        fish[a] = []
        #다음 위치에 탐색하기 위해 재귀호출
        dfs(cur+a,ny,nx,b)
        #백트래킹하여 탐색하기 위해 board,fish 원상복귀
        board = c_board
        fish = c_fish
        #상어의 위치 최신화
        y = ny; x = nx

#메인 함수
def main():
    #전역 변수로 설정한 board와 fish 리스트
    global board
    global fish
    #1~16번 물고기의 위치를 튜플로 저장할 리스트
    fish = [0 for _ in range(17)]
    #4 x 4 크기의 board를 모두 0으로 초기화
    board = [[0 for _ in range(4)] for _ in range(4)]
    #4 x 4 크기의 board에 있는 모든 물고기 입력
    for i in range(4):
        #각 물고기 정보 입력
        tmp = list(map(int,input().split()))
        #해당 열의 4마리의 물고기 정보를 각각 [물고기 번호,방향] 형태로 board에 저장
        for j in range(4):
            board[i][j] = [tmp[j*2],tmp[j*2+1]-1]
            #해당 물고기 번호에 위치한 인덱스에 물고기의 위치 저장
            fish[tmp[j*2]] = (i,j)
    #상어의 초기 위치(0,0) 설정
    a,b = board[0][0]
    #0,0 에 위치한 물고기 삭제
    fish[a] = []
    board[0][0] = []
    #삭제된 물고기의 번호, 방향을 초기값으로 완전 탐색 진행
    dfs(a,0,0,b)
    #최종 결과값 출력
    print(res)

if __name__ == "__main__":
    main()