import sys
from collections import deque
inf = sys.maxsize
input = sys.stdin.readline

#나이트 이동 방향 포함 12개 방향
dx = [0,0,1,-1,-2,-1,2,1,-2,-1,2,1]
dy = [-1,1,0,0,-1,-2,-1,-2,1,2,1,2]

def bfs(board:list[list[int]],k:int,w:int,h:int) -> int:
    #방문리스트를 inf로 초기화하여 현재 이동거리와 비교 후 현재 이동거리가 더 적을 때만 탐색
    #자연스럽게 해당 위치는 최소 위치로 변경과 중복 방문 방지 모두 가능
    visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 0
    #bfs탐색을위한 큐 선언
    q = deque()
    #큐에 시작 지점과 현재 남은 이동 횟수를 저장
    q.append((0,0,k))
    #bfs진행
    while q:
        #현재 위치의 y값,x값, 나이트 방향으로 남은 이동 횟수 left
        y,x,left = q.popleft()
        if y == h-1 and x == w-1:
            return visited[y][x][left]
        for i in range(4):
            ny,nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and not board[ny][nx]:
                if not visited[ny][nx][left]:
                    visited[ny][nx][left] = visited[y][x][left]+1
                    q.append((ny,nx,left))
        if left >= 1:
            for i in range(4,12):
                ny,nx = y + dy[i], x + dx[i]
                if 0 <= ny < h and 0 <= nx < w and not board[ny][nx]:
                    if not visited[ny][nx][left-1]:
                        visited[ny][nx][left-1] = visited[y][x][left]+1
                        q.append((ny,nx,left-1))
    return -1
#메인 함수
def main():
    #입력
    #k -> k번 나이트(말) 처럼 이동 가능
    k = int(input())
    #가로 w , 세로 h 크기의 board
    w,h = map(int,input().split())
    #h줄만큼 board 입력
    #1 -> 장애물, 0 -> 빈 공간
    board = [list(map(int,input().split())) for _ in range(h)]
    print(bfs(board,k,w,h))

if __name__ == "__main__":
    main()