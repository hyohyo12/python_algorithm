import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def max_movement(board:list[list[int]],n:int,trees:list[int]):
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    def dfs(cur,y,x):
        cnt = 4
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if board[ny][nx] > board[y][x]:
                    if dp[ny][nx]:
                        dp[y][x] = max(dp[y][x],dp[ny][nx] + 1)
                        cnt -= 1
                        continue
                    visited[ny][nx] = True
                    dfs(cur+1,ny,nx)
                    dp[y][x] = max(dp[ny][nx] + 1,dp[y][x])
                    visited[ny][nx] = False
                    cnt -= 1
        if cnt == 4:
            dp[y][x] = 1
            return
    for t,y,x in trees:
        if dp[y][x]:
            continue
        visited[y][x] = True
        dfs(1,y,x)
        visited[y][x] = False
    res = 0
    for i in dp:
        res = max(max(i),res)
    return res

def main():
    n = int(input())
    board = []
    trees = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        for j in range(n):
            trees.append((tmp[j],i,j))
        board.append(tmp)
    trees.sort(reverse=True)
    print(max_movement(board,n,trees))
if __name__ == "__main__":
    main()