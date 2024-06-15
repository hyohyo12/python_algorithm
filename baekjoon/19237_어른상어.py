import sys
from collections import defaultdict
input = sys.stdin.readline

#이동 리스트
dx = [0,0,0,-1,1]
dy = [0,-1,1,0,0]

def find_time(board:list[list[list[int]]],sharks:list[list[int]],priority:defaultdict,dir:list[int],n:int,m:int,k:int) -> int:
    #nxn크기의 냄새가 있는 현황을 저장할 smell_seq
    smell_seq = [[[] for _ in range(n)] for _ in range(n)]
    #현재 남은 상어의 수를 저장할 변수
    left = m
    #경과 시간을 저장할 변수
    time = 0
    #1000초동안 반복
    while time <= 1000:
        #남은 상어의 수가 1마리이면 경과 시간을 반환
        if left == 1:
            return time
        #냄새 뿌리기
        #상어의 위치를 저장한 리스트를 순회
        for data in sharks:
            #data = 0 -> 현재 상어는 삭제된 상어 또는 인덱스 맞추기 위한 값
            if data == 0:
                continue
            #각 좌표와 현재 상어의 위치를 각각 저장하고
            y,x,num = data
            #냄새 현황 리스트에 현재 상어의 번호와 k초 를 저장
            smell_seq[y][x] = [num,k]
        #시간 1초 경과 후
        time += 1
        #이동
        for data  in sharks:
            if data == 0:
                continue
            y,x,num = data
            #다음 위치 -1로 초기화
            next = -1
            #현재 상어의 현재 방향의 우선순위 순서대로 다음 방향 탐색 진행
            #1차적으로 빈 공간 탐색
            for i in priority[num][dir[num]]:
                ny,nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if not len(smell_seq[ny][nx]):
                        next = i
                        break
            #빈 공간이 없다면 현재 상어의 채취가 있는 곳 탐색 진행
            else:
                for i in priority[num][dir[num]]:
                    ny,nx = y + dy[i], x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n:
                        if smell_seq[ny][nx][0] == num:
                            next = i
                            break
                #그것 마저 없다면 이동하지 않음
                else:
                    sharks[num] = [y,x,num]
                    continue
            #빈 공간 또는 자신의 냄새가 있는 곳으로 이동
            board[y+dy[next]][x+dx[next]].append(num)
            board[y][x].pop(board[y][x].index(num))
            sharks[num] = [y+dy[next],x+dx[next],num]
            dir[num] = next
        #상어 제거 와 냄새 1초 경과했으므로 -1 작업 동시에 진행
        #board를 순회하며 해당 칸에 2마리 이상의 상어가 있는 칸을 탐색
        for i in range(n):
            for j in range(n):
                #냄새가 있고 현재 칸에 상어가 없으면
                if len(smell_seq[i][j]) and not len(board[i][j]):
                    #냄새 -1
                    smell_seq[i][j][1] -= 1
                    #현재 칸의 냄새가 모두 사라졌다면 빈 리스트로 초기화
                    if smell_seq[i][j][1] == 0:
                        smell_seq[i][j] = []
                #현재 칸에 있는 상어의 수가 2마리 이상이면
                if len(board[i][j]) >= 2:
                    #mn에 제일 작은 크기의 상어 번호를 저장하고
                    mn = min(board[i][j])
                    for idx in range(len(board[i][j])):
                        #해당 상어 번호를 가지지 않은 상어 모두 삭제
                        if board[i][j][idx] != mn:
                            sharks[board[i][j][idx]] = 0
                            left -= 1
                    #board 갱신
                    board[i][j] = [mn]
    #1000초이내 상어가 1마리만 남게되지 못했다면 -1 반환
    return -1


def main():
    #상어의 현재 위치를 저장할 리스트
    sharks = []
    #각 상어가 바라보는 방향에 따른 방향의 우선순위를 리스트로 저장할 defaultdict
    priority = defaultdict(list)
    #입력
    #n -> nxn 크기의 board, m -> 상어의 개수, k -> k 초가 지나면 상어의 냄새는 사라짐
    n,m,k = map(int,input().split())
    #board 한 칸을 리스트로 초기화(한 칸에 상어가 여러 개일 경우 번호가 제일 작은 한마리만 남기기 위해)
    board = [[[] for _ in range(n)] for _ in range(n)]
    #nxn크기를 입력받아 숫자 입력시에만 board해당 칸에 append
    for i in range(n):
        tmp = list(map(int,input().split()))
        for j in range(n):
            if tmp[j] != 0:
                sharks.append([i,j,tmp[j]])
                board[i][j].append(tmp[j])
    #각 상어의 초기 방향 입력 받음
    dir = [0] + list(map(int,input().split()))
    #1번 상어부터 m번 상어까지 1,2,3,4 각 방향에 따른 방향의 우선순위를 입력 받음
    for i in range(1,m+1):
        #방향이 1번부터 시작하므로 인덱스 맞추기위해 빈 리스트를 앞에 추가
        priority[i].append([])
        for j in range(4):
            tmp = list(map(int,input().split()))
            priority[i].append(tmp)
    #상어를 상어의 번호(인덱스 2번)을 기준으로 정렬
    sharks.sort(key=lambda x:x[2])
    #마찬가지로 상어의 번호는 1번부터 시작하므로 인덱스 맞춤
    sharks = [0] + sharks
    print(find_time(board,sharks,priority,dir,n,m,k))
if __name__ == "__main__":
    main()