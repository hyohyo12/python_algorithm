import sys
input = sys.stdin.readline

def dfs(x,y,graph):
    global count
    if x == 0:
        count += 1
        return True
    for dx,dy in [(-1,-1),(-1,0),(-1,1)]:
        nx,ny= x+dx, y+dy
        if 0 <= nx < c and 0 <= ny < r:
            if graph[ny][nx] == '.':
                graph[ny][nx] = 'x'
                if dfs(nx,ny,graph):
                    return True
    return False

if __name__ == "__main__":
    r,c = map(int,input().split())
    
    graph = [list(input().strip()) for _ in range(r)]
    
    count = 0
    
    for y in range(r):
        dfs(c - 1, y,graph)
    print(count)