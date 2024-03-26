from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(y,x):
    q = deque([(y,x)])
    visited[y][x] = True
    seaList = []
    while q:
        sea = 0
        cur_y,cur_x = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not board[ny][nx]:
                    sea += 1
                elif board[ny][nx] and not visited[ny][nx]:
                    q.append((ny,nx))
                    visited[ny][nx] = True
        if sea > 0: seaList.append((cur_y,cur_x,sea))
    for y,x,sea in seaList:
        board[y][x] = max(0,board[y][x]-sea)
    return 1

if __name__ == "__main__":
    n,m = map(int,input().split())
    board = []
    year = 0
    
    ice_seq = []
    for i in range(n):
        seq = list(map(int,input().split()))
        for j in range(m):
            if seq[j]: ice_seq.append((i,j))
        board.append(seq)
    
    while ice_seq:
        visited = [[False for _ in range(m)] for _ in range(n)]
        group = 0
        delList = set()
        for i,j in ice_seq:
            if not visited[i][j] and board[i][j]:
                group += bfs(i,j)
            if not board[i][j]:
                delList.add((i,j))
        if group > 1:
            print(year)
            break
        ice_seq = sorted(list(set(ice_seq) - delList))
        year += 1
    if group < 2:
        print(0)