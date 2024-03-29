import sys
input = sys.stdin.readline

#상하좌우 방향 리스트
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#각 학생 자리 할당하는 함수
def alloc_seat(like: list[list[int]],seq: list[int],n:int):
    #n x n 크기의 교실(board)
    board = [[0 for _ in range(n)] for _ in range(n)]
    #seq에 있는 순으로 각 학생 자리 배정
    for student in seq:
        #자리가 될 수 있는 후보들을 저장할 리스트
        candidate = []
        #board 탐색
        for i in range(n):
            for j in range(n):
                #해당 자리가 0일 경우(자리의 후보가 될 수 있을 때)
                if board[i][j] == 0:
                    #인접한 공간의 좋아하는 사람의 개수를 저장할 변수
                    like_count = 0
                    #인접한 공간의 빈 공간의 개수를 저장할 변수
                    empty = 0
                    #해당 자리 상,하,좌,우 탐색
                    for k in range(4):
                        y = i + dy[k];x = j + dx[k]
                        #인덱스 에러 방지
                        if 0 <= x < n and 0 <= y < n:
                            #해당 자리에 좋아하는 학생이 있을 때 like_count + 1, 빈 공간일 땐 empty + 1
                            if board[y][x] in like[student]:
                                like_count += 1
                            elif board[y][x] == 0:
                                empty += 1
                    #후보 리스트에 해당 자리의 좌표와, 인접한 공간의 좋아하는 사람, 빈공간 각각 튜플로 묶어 저장
                    candidate.append((i,j,like_count,empty))
        #후보 자리를 좋아하는 사람 -> 빈 공간 개수 -> y좌표, x좌표 기준으로 정렬(좋아하는 사람, 빈 공간 개수는 내림차순,y,x 값은 오름차순으로 정렬)
        candidate.sort(key = lambda x:(-x[2],-x[3],x[0],x[1]))
        #0번째 인덱스 (가장 우선순위가 큰) 의 y,x값 각 각 저장
        y,x = candidate[0][0],candidate[0][1]
        #자리 배정
        board[y][x] = student
    #자리 배정 후 교실 반환
    return board

#배정된 자리로 점수를 계산하는 함수
def cal_score(board:list[list[int]],like: list[list[int]]) -> int:
    score = 0
    scord_board = [0,1,10,100,1000]
    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp = 0
            for k in range(4):
                y = i + dy[k]; x = j + dx[k]
                if 0 <= x < len(board[0]) and 0 <= y < len(board) and board[y][x] in like[board[i][j]]:
                    tmp += 1
            score += scord_board[tmp]
    return score

def main():
    #교실 크기 n x n
    n = int(input())
    #각 학생이 좋아하는 학생 번호를 저장할 리스트 like
    like = [[] for _ in range(n**2+1)]
    #교실에 배치할 순서 저장할 리스트 seq
    seq = []
    #학생 번호와 각 학생이 좋아하는 번호들을 입력
    for _ in range(n ** 2):
        #0 번째 인덱스 -> 학생 번호, 나머지 인덱스 -> 해당 학생이 좋아하는 학생의 번호
        temp = list(map(int,input().split()))
        like[temp[0]] = temp[1:]
        seq.append(temp[0])
    #자리 배정 함수 호출
    board = alloc_seat(like,seq,n)
    #자리 배정 후 점수 계산
    score = cal_score(board,like)
    print(score)

    
if __name__ == "__main__":
    main()