import sys
from collections import deque
input = sys.stdin.readline


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(board:list[list[int]],n:int,m:int):
    result = []
    visited = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0 and not visited[i][j]:
                cur_area = 0
                visited[i][j] = 1
                q = deque([(i,j)])
                while q:
                    cur_area += 1
                    y,x = q.popleft()
                    for k in range(4):
                        ny,nx = y + dy[k], x + dx[k]
                        if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and board[ny][nx] == 0:
                            q.append((ny,nx))
                            visited[ny][nx] = 1
                result.append(cur_area)
    return sorted(result)


def main():
    m,n,k = map(int,input().split())
    board = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        square = list(map(int,input().split()))
        for i in range(square[1],square[3]):
            for j in range(square[0],square[2]):
                board[i][j] = 1
    result = bfs(board,n,m)
    print(len(result))
    print(*result)


if __name__ == "__main__":
    main()