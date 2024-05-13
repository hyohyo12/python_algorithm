import sys
input = sys.stdin.readline
#재귀 깊이 10**9으로 변경
sys.setrecursionlimit(10**9)


#백트래킹 탐색 함수
def back_tracking(depth:int,res:int,piece:list[int],seq:list[int]):
    global answer
    #매 10번째 탐색(10개의 주사위 경우)이 모이면
    if depth == 10:
        #정답 변수 최대값으로 갱신
        answer = max(answer,res)
        return
    #4개의 말에 대해 탐색
    for i in range(4):
        #현재 말의 위치를 x에 저장
        x = piece[i]
        #만약 현재 말의 위치가 10,20,30,40 일 경우 -> 갈 수 있는 방향의 개수 2개 -> 파란색 화살표 따라가야하므로
        #1번째 인덱스 요소를 선택해 탐색해야함
        if len(board[x]) == 2:
            x = board[x][1]
        #제외하고 나머지 숫자일 경우 빨갠색 화살표 선택 -> 0번째 인덱스 선택
        else:
            x = board[x][0]
        #현재 말을 주사위의 숫자만큼 순차적으로 이동
        #이 때 전에 빨간색/파란색 화살표 판별할 때 1번 이동 했으므로 주사위 숫자 - 1번 수행
        for _ in range(1,seq[depth]):
            x = board[x][0]
        #도착 위치가 끝 점이거나 끝점보다 작고 이미 도착한 말이 없을 때만 백트래킹 탐색
        if x == 32 or (x < 32 and x not in piece):
            #백트래킹을 위해 이전값 prev에 임시 저장
            prev = piece[i]
            #다음 탐색을 위해 piece의 현재 말의 위치 업데이트
            piece[i] = x
            #탐색
            back_tracking(depth+1,res+score[x],piece,seq)
            #원상태로 복구
            piece[i] = prev
#메인 함수
def main():
    global answer
    #입력
    #주사위의 나온 숫자를 10개 입력받아 저장
    seq = list(map(int,input().split()))
    #백트래킹 탐색
    back_tracking(0,0,[0,0,0,0],seq)
    #출력
    #정답 출력
    print(answer)


if __name__ == "__main__":
    #정답을 저장할 변수
    answer = 0
    #문제상 board를 구현
    #이 부분이 제일 어렵고 난해했던 곳.
    #각자 요소가 의미하는 바는 다음 위치
    #요소의 개수가 2개인 곳은 빠질 수 있는 위치(파란 화살표)
    board = [[1],[2],[3],[4],[5],
            [6,21],[7],[8],[9],[10],
            [11,25],[12],[13],[14],[15],
            [16,27],[17],[18],[19],[20],
            [32],[22],[23],[24],[30],
            [26],[24],[28],[29],[24],
            [31],[20],[32]
        ]
    #각 자리에 대해 점수판
    score = [0,2,4,6,8,
            10,12,14,16,18,
            20,22,24,26,28,
            30,32,34,36,38,
            40,13,16,19,25,
            22,24,28,27,26,
            30,35,0]
    #메인함수 호출
    main()