import sys
#각 숫자가 얼마나 나왔는지 확인하기 위한 defaultdict
from collections import defaultdict
input = sys.stdin.readline

#R연산 (row 기준으로 연산을 진행한다)
def cal_r(board: list[list[int]]):
    max_len = 0
    new_board = []
    #각 줄을 검사한다.
    for i in range(len(board)):
        #각 숫자와 개수를 저장할 defaultdict
        num_count = defaultdict(int)
        #각 줄의 요소들을 순회
        for j in range(len(board[i])):
            #0값은 무시해야하므로 0이 아닌 수에만 검사
            if board[i][j] != 0:
                #딕셔너리에 해당하는 숫자 +1
                num_count[board[i][j]] += 1
        #키(숫자),벨류(개수) 를 벨류(개수)에 대해 정렬 후 같다면 키(숫자에) 대해 정렬을 한다.
        num_count = sorted(num_count.items(),key = lambda x:(x[1],x[0]))
        #각 숫자, 개수를 tmp라는 임시 리스트에 저장
        tmp = []
        for k,v in num_count:
            tmp.append(k)
            tmp.append(v)
        #요소 개수가 100을 넘어가면 그 뒤 숫자는 무시해야하므로 검사
        if len(tmp) > 100:
            #인덱스 슬라이싱 이용
            tmp = tmp[:101]
        #최고 length를 max_len에 저장(갱신)
        max_len = max(len(tmp),max_len)
        #해당 row를 추가한다
        new_board.append(tmp)
    #각 줄의 length를 맞춰줘야 하므로 0을 채우는 과정
    for i in range(len(new_board)):
        while len(new_board[i]) != max_len:
            new_board[i].append(0)
    #연산을 마친 새로운 board 반환
    return new_board

#C연산 col 기준으로 연산을 진행한다.
def cal_c(board:list[list[int]]):
    tmps = []
    max_len = 0
    #각 열을 기준으로 검사
    for x in range(len(board[0])):
        #숫자 개수를 저장할 딕셔너리
        num_count = defaultdict(int)
        #각 열을 기준으로 검사
        for y in range(len(board)):
            #0은 연산에서 제외하므로 검사
            if board[y][x] != 0:
                #해당 숫자 + 1
                num_count[board[y][x]] += 1
        tmp = []
        #딕셔너리의 아이템을 마찬가지로 1번째 인덱스(개수) 기준으로 같다면 2번째 인덱스(숫자) 정렬
        num_count = sorted(num_count.items(),key = lambda x:(x[1],x[0]))
        
        
        for k,v in num_count:
            tmp.append(k)
            tmp.append(v)
        #마찬가지로 100을 넘었으면, 슬라이싱을 이용해 100넘는 부분은 제거
        if len(tmp) > 100:
            tmp = tmp[:101]
        #제일 긴 length 업데이트
        max_len = max(max_len,len(tmp))
        tmps.append(tmp)
    #각 줄 부족한 length 0으로 채우는 과정
    for i in range(len(tmps)):
        while len(tmps[i]) != max_len:
            tmps[i].append(0)
            
    #새로운 board 생성
    new_board = [[] for _ in range(max_len)]
    #새로운 board 각 줄 채우기
    for x in range(len(tmps)):
        for y in range(len(tmps[0])):
            new_board[y].append(tmps[x][y])
            
    return new_board

#메인 함수
def main():
    #[r][c] 번째 숫자가 k 가 되어야한다.
    r,c,k = map(int,input().split())
    #r,c는 인덱스 번호가 1부터 시작하므로 각각 인덱스를 맞춘다
    r -= 1;c -= 1
    #board(행렬) 정의
    board = [list(map(int,input().split())) for _ in range(3)]
    #시간이 얼마나 지났는지 저장할 변수
    time = 0
    #100초까지 진행
    for t in range(101):
        #인덱스 에러 방지
        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            #해당 값이 k 값과 비슷할 때 시간을 출력하고 반복을 끝낸다.
            if board[r][c] == k:
                print(time)
                break
        #시간 1초 지남
        time += 1
        #row 가 col 보다 클때 C연산 진행(col기준 연산)
        if len(board[0]) > len(board):
            board = cal_c(board)
        #row가 col보다 작거나 같을 때 R연산 진행(Row 연산)
        else:
            board = cal_r(board)
    #반복이 중단되지 않고 모든 연산이 끝난다면 -> r,c가 k로 100초이내 변하지 못한다는 뜻이므로 -1출력
    else:
        print(-1)



if __name__ == "__main__":
    main()