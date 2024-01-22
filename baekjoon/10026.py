from collections import defaultdict

def search(grid:list[list[str]],n:int) -> tuple[int]:
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    count = 0
    count_2 = 0
    def dfs_G(cur_x,cur_y,color):
        grid[cur_y][cur_x] = 'R'
        for x,y in zip(dx,dy):
            nx,ny = cur_x+x, cur_y+y
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and grid[ny][nx] == color:
                    visited[ny][nx] = True
                    dfs_G(nx,ny,color)
    
    def dfs(cur_x,cur_y,color):
        for x,y in zip(dx,dy):
            nx,ny = cur_x+x, cur_y+y
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and grid[ny][nx] == color:
                    visited[ny][nx] = True
                    dfs(nx,ny,color)
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if grid[i][j] == 'G':
                    dfs_G(j,i,'G')
                else:
                    dfs(j,i,grid[i][j])
                count+=1
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
                if not visited[i][j]:
                    dfs(j,i,grid[i][j])
                    count_2 += 1
    return (count,count_2)



if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(99999)
    read = sys.stdin.readline
    
    grid = []
    
    n = int(read())
    for i in range(n):
        grid.append(list(read().strip()))
    a,b = search(grid,n)
    print(a,b)
