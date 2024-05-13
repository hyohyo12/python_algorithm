import sys
input = sys.stdin.readline

color_board = []

#이동 리스트
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]

def reverse_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    elif dir == 4:
        return 3

def move_pieces(board:list[list[list[int]]],piece_seq:list[tuple],n:int)->tuple:
    global color_board
    flag = False
    #체스말 1번부터 k번까지 순차적으로 이동
    for idx in range(1,len(piece_seq)):
        r,c,d = piece_seq[idx]
        #체스말이 해당칸에 제일 밑에 있는 말일떄만 이동가능
        if board[r][c][0] == idx:
            ny,nx = r+dy[d],c+dx[d]
            #이동이 인덱스 범위 내에서 이뤄지는지 검사
            if 0 <= ny < n and 0 <= nx < n:
                #이동하려는 칸이 빨간색일 때
                if color_board[ny][nx] == 1:
                    #문제에서 빨간 칸은 순서를 역순으로 바꿈.
                    board[r][c].reverse()
                    #해당 칸에 현재 말을 쌓음
                    board[ny][nx] += board[r][c]
                    #해당 칸의 모든 말의 좌표 갱신
                    for i in board[r][c]:
                        piece_seq[i][0] = ny
                        piece_seq[i][1] = nx
                    #해당 칸에 말이 4개 이상 모이면 flag -> True
                    if len(board[ny][nx]) >= 4:
                        flag = True
                    #원래 칸 비움
                    board[r][c] = []
                #이동하려는 칸이 파란색일 떄
                elif color_board[ny][nx] == 2:
                    #문제에서 파란칸에선 말의 방향 변경
                    #방향을 반대로 바꾸는 함수 실행
                    dir = reverse_dir(d)
                    #체스 말의 방향 변경
                    piece_seq[idx][2] = dir
                    #체스말 위치 갱신
                    ny,nx = r+dy[dir],c+dx[dir]
                    #인덱스 내에서 이동이 이뤄지는지 검사
                    if 0 <= ny < n and 0 <= nx < n:
                        #이동 칸이 빨간색
                        if color_board[ny][nx] == 1:
                            #역순
                            board[r][c].reverse()
                        #역순 변경해도 파란색일 시 위치는 변경시키지 않고 방향만 변경
                        elif color_board[ny][nx] == 2:
                            continue
                        #해당 위치 말 위로 쌓음
                        board[ny][nx] += board[r][c]
                        #전 칸에 있던 모든 말의 좌표 갱신
                        for i in board[r][c]:
                            piece_seq[i][0] = ny
                            piece_seq[i][1] = nx
                        if len(board[ny][nx]) >= 4:
                            flag = True
                        board[r][c] = []
                #하얀색 칸은 기능없이 그냥 이동칸에 말 위로 쌓음
                else:
                    board[ny][nx] += board[r][c]
                    for i in board[r][c]:
                        piece_seq[i][0] = ny
                        piece_seq[i][1] = nx
                    if len(board[ny][nx]) >= 4:
                        flag = True
                    board[r][c] = []
            #인덱스 범위로 밖에 이동이 이뤄진다면 파란칸과 똑같이 상호작용
            else:
                dir = reverse_dir(d)
                piece_seq[idx][2] = dir
                ny,nx = r+dy[dir],c+dx[dir]
                if 0 <= ny < n and 0 <= nx < n:
                    if color_board[ny][nx] == 1:
                        board[r][c].reverse()
                    elif color_board[ny][nx] == 2:
                        continue
                    board[ny][nx] += board[r][c]
                    for i in board[r][c]:
                        piece_seq[i][0] = ny
                        piece_seq[i][1] = nx
                    if len(board[ny][nx]) >= 4:
                        flag = True
                    board[r][c] = []
    return (board,flag)
    

#메인 함수
def main():
    global color_board
    #입력
    #nxn크기 board, k개의 말
    n,k = map(int,input().split())
    #각 board의 색을 나타내는 color_board
    #0 -> 흰색, 1 -> 빨간색, 2 -> 파란색
    color_board = [list(map(int,input().split())) for _ in range(n)]
    #체스 말의 위치 및 방향 정보를 저장할 리스트
    piece_seq = [0]
    #각 칸에 말 정보를 저장할 board
    board = [[[] for _ in range(n)] for _ in range(n)]
    #k개의 말을 입력
    for i in range(1,k+1):
        #r -> 행,c -> 열,d -> 이동방향
        r,c,d = map(int,input().split())
        #1번 부터 k번까지 순차적 이동을 위해 따로 저장
        piece_seq.append([r-1,c-1,d])
        board[r-1][c-1].append(i)
    #한 칸에 존재하는 말의 개수가 4개 이상이 되는 턴이 몇 번째인지 저장할 turn 변수(정답 변수)
    turn = 0
    #턴이 최대 1000번이므로 1000번 이하로 진행
    while turn <= 1000:
        turn += 1
        board,flag = move_pieces(board,piece_seq,n)
        if flag:
            print(turn)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()