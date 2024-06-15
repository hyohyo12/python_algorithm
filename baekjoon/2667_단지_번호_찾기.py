from collections import deque
import sys
input = sys.stdin.readline

#이동 리스트(하,상,우,좌)
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(board:list[list[int]],n:int,start:tuple)->int:
    global visited
    #bfs하기 위해 데크 자료 구조에 시작 지점 저장
    q = deque([start])
    #시작 지점 방문 처리
    visited[start[0]][start[1]] = True
    #리턴 할 값(단지 수) 저장
    cnt = 0
    #bfs수행
    while q:
        #현재 위치
        y,x = q.popleft()
        #단지 수 하나 증가
        cnt += 1
        #4방향 상하좌우 검사
        for i in range(4):
            #다음 위치 검사
            ny,nx = y + dy[i],x + dx[i]
            #인덱스 에러 방지, 중복 방문 방지
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                #다음 방문 위치가 1일때만(단지가 있을 때) 다음 방문에 추가
                if board[ny][nx] == '1':
                    #다음 탐색을 위해 데크에 추가
                    q.append((ny,nx))
                    #방문 처리
                    visited[ny][nx] = True
    #cnt(단지 수) 리턴
    return cnt
#메인 함수
def main():
    #전역 변수 방문 리스트 visited 사용
    global visited
    #답 (각 아파트의 단지 수)를 저장할 리스트
    seq = []
    #입력
    #n -> nxn 크기 board
    n = int(input())
    visited = [[False for _ in range(n)] for _ in range(n)]
    #n개의 열을 입력받아 board 이중 리스트로 저장
    board = [list(input().strip()) for _ in range(n)]
    #board를 탐색
    for i in range(n):
        for j in range(n):
            #단지가 있고 방문 안했을 때만 BFS 실행
            if board[i][j] == '1' and not visited[i][j]:
                #단지수를 seq에 추가
                seq.append(bfs(board,n,(i,j)))
    #seq의 길이 출력
    print(len(seq))
    #단지 수를 정렬하여 출력하라 했으므로 정렬
    seq.sort()
    #정렬된 단지 수 출력
    for n in seq:
        print(n)

if __name__ == "__main__":
    #방문 리스트를 전역 변수로 선언
    visited = []
    main()