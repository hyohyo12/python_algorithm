import sys
from collections import deque
input = sys.stdin.readline


dx = [0,0,1,-1]
dy = [1,-1,0,0]
parents = []
visited = []
board = []

def find(x:int):
    global parents
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(u:int,v:int):
    global parents
    u,v = find(u),find(v)
    if u > v:
        parents[u] = v
    else:
        parents[v] = u



def marking(y:int,x:int,mark:int):
    global board
    global visited
    q = deque([(y,x)])
    visited[y][x] = True
    board[y][x] = mark
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i];ny = y + dy[i]
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == 1:
                if not visited[ny][nx]:
                    board[ny][nx] = mark
                    visited[ny][nx] = True
                    q.append((ny,nx))



def add_candidate(board:list[list[int]],candidate:set[int],y:int,x:int):
    cur = board[y][x]
    q = deque()
    for i in range(4):
        q.append((y,x,0,i))
        while q:
            ny,nx,cnt,dir = q.popleft()
            if board[ny][nx] != 0 and board[ny][nx] != cur:
                if cnt > 2:
                    candidate.add((cnt-1,cur,board[ny][nx]))
                continue
            nx = nx + dx[dir];ny = ny + dy[dir]
            if 0 > ny or 0 > nx or len(board) <= ny or len(board[0]) <= nx or board[ny][nx] == cur:
                continue
            q.append((ny,nx,cnt+1,dir))
    return candidate

def main():
    global parents
    global visited
    global board
    #지도 크기 n x m
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    candidate = set()
    mark = 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                marking(i,j,mark)
                mark+=1
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                candidate = add_candidate(board,candidate,i,j)
    candidate = list(candidate)
    candidate.sort()
    parents = [i for i in range(mark)]
    
    num = 0
    res = 0
    
    for cost,a,b in candidate:
        if find(a) != find(b):
            num += 1
            union(a,b)
            res += cost
    if res == 0 or num != mark - 2:
        print(-1)
    else:
        print(res)
        
if __name__ == "__main__":
    main()