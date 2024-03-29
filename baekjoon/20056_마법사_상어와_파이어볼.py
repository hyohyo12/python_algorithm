import sys
input = sys.stdin.readline

#방향 리스트 상하좌우,4방향 대각선
dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

#파이어볼의 다음 위치를 반환하는 함수
def next_location(y:int,x:int,n:int,s:int,d:int):
    #board가 상 하 좌 우 모두 연결 즉, 인덱스 가 넘어가면 다시 0 또는 끝 부터 시작
    #방향리스트에 s(속도) 곱하고 원래 좌표에 더하고 모듈러 연산을 통해 구한다
    nx = (x + (dx[d]*s)) % n; ny = (y + (dy[d]*s)) % n
    #다음 위치 반환
    return (ny,nx)

#파이어볼이 움직이고 2개 이상의 파이어볼이 한 좌표에 있을 때 분할하는 함수
def move(board:list[list[int]],n:int):
    #파이어볼이 이동,분할 후 결과를 저장할 리스트
    #board를 사용하지 않는 이유는 탐색과 동시에 이동을 한다면 정확하지 않은 데이터가 들어갈 수 있음
    new_board = [[[] for _ in range(n)] for _ in range(n)]
    #board를 순회하며
    for i in range(n):
        for j in range(n):
            #해당 위치의 파이어볼의 개수가 1개 이상이면
            if len(board[i][j]):
                #m -> 질량, s -> 속도, d -> 방향, 해당 위치의 파이어볼 탐색하며 위치 변경
                for m,s,d in board[i][j]:
                    #파이어볼의 다음 위치를 각각 y,x에 저장
                    y,x = next_location(i,j,n,s,d)
                    #다음위치에 파이어볼 정보(질량,속도,방향)삽입
                    new_board[y][x].append((m,s,d))

    #2개이상 파이어볼이 존재하는 좌표의 파이어볼 분할하기 위해 위치가 최신화 된 new_board 를 탐색
    for i in range(n):
        for j in range(n):
            #해당 좌표에 파이어볼이 2개 이상이면
            if len(new_board[i][j]) >= 2:
                #분할된 질량, 속도를 저장할 tmp_m,tmp_s, 방향의 번호의 짝수의 개수, 홀수의 개수를 각각 저장할 even_cnt,odd_cnt, 해당 리스트의 파이어볼 총 개수를 저장할cnt변수
                tmp_m,tmp_s,odd_cnt,even_cnt,cnt = 0,0,0,0,len(new_board[i][j])
                #해당 위치의 파이어볼의 정보를 탐색
                for m,s,d in new_board[i][j]:
                    #질량과 속력을 모두 합
                    tmp_m += m
                    tmp_s += s
                    #방향이 2로 나누어 떨어지지 않으면 홀수 + 1
                    if d % 2:
                        odd_cnt += 1
                    #짝수면 짝수 + 1
                    else:
                        even_cnt += 1
                #해당 위치 빈 공간으로 다시 초기화
                new_board[i][j] = []
                #질량을 5로 나눈 후 버림 연산
                tmp_m //= 5
                #속도를 총 파이어볼의 개수로 나눈 후 버림 연산
                tmp_s //= cnt
                #질량이 0이 되면 해당 파이어볼은 소멸하므로 continue
                if tmp_m <= 0:
                    #위에서 빈 공간으로 초기화 헀으므로 다시 초기화 할 필요는 없음
                    continue
                #홀수의 개수나 짝수의 개수 둘 중 하나가 총 파이어볼 개수와 같다면
                if odd_cnt == cnt or even_cnt == cnt:
                    #방향은 각각 0,2,4,6으로 나눠 들어간다
                    for k in [0,2,4,6]:
                        new_board[i][j].append((tmp_m,tmp_s,k))
                #그 외 상황은 둘 다 섞여 있다는 말이므로 방향에 각각 1,3,5,7 들어간다
                else:
                    for k in [1,3,5,7]:
                        new_board[i][j].append((tmp_m,tmp_s,k))
    #최신화된 파이어볼 정보 및 위치를 반환
    return new_board

#메인 함수
def main():
    #입력
    #N -> N x N 크기의 board, M -> 파이어볼의 개수, K -> K번의 파이어볼의 이동
    N,M,K = map(int,input().split())
    #각 파이어볼의 위치에 파이어볼의 정보를 저장할 N x N 크기의 Borad 를 초기화
    board = [[[] for _ in range(N)] for _ in range(N)]
    #파이어 볼 개수만큼 반복하며 입력받음
    for _ in range(M):
        #r -> row , c -> col, m -> 질량, s -> 속도, d -> 방향 각각 입력 받음
        r,c,m,s,d = map(int,input().split())
        #r,c 는 인덱스 1번부터 시작하므로 인덱스 맞춰주고 (질량,속도,방향) 순으로 board의 해당 위치에 저장
        board[r-1][c-1].append((m,s,d))
    #명령 수행
    #K번 명령을 수행
    for _ in range(K):
        #board를 최신화 시킨 후 다시 board에 저장
        board= move(board,N)
    #모든 명령 수행 후 남은 파이어볼의 개수의 합을 저장할 변수 res
    res = 0
    #2중 for문으로 board를 순회하며 질량들을 res에 합함
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                res += sum(map(lambda x:x[0],board[i][j]))
    #출력
    #결과값(파이어볼의 질량 총량) 출력
    print(res)
if __name__ == "__main__":
    main()