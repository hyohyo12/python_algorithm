import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    visited = [[False for _ in range(m)] for _ in range(n)]
    air = [[0 for _ in range(m)] for _ in range(n)]
    global board
    visited[0][0] = True
    q = deque([(0,0)])
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if board[ny][nx] == 1:
                    air[ny][nx] += 1
                    continue
                visited[ny][nx] = True
                q.append((ny,nx))
    return air


if __name__ == "__main__":
    #치즈 개수
    cheese = 0
    time = 0
    board = []
    #(nxm)모양의 Board
    n,m = map(int,input().split())
    
    for _ in range(n):
        seq = list(map(int,input().split()))
        cheese += seq.count(1)
        board.append(seq)
    while cheese != 0:
        time += 1
        air = bfs()
        for i in range(n):
            for j in range(m):
                if air[i][j] >= 2:
                    board[i][j] = 0
                    cheese -= 1
    print(time)
    
    