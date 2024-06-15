import sys
from collections import deque
input = sys.stdin.readline

dy = [0,0,1,-1]
dx = [1,-1,0,0]
def fifth_dist_bfs(graph:list[list[int]],n:int,pivot:tuple[int],d1:int,d2:int):
    visited = [[False for _ in range(n)] for _ in range(n)]
    left = [-1 for _ in range(d1)] + [1 for _ in range(d2)] + [0]
    right = [1 for _ in range(d2)] + [-1 for _ in range(d1)] + [0]
    population = [0 for _ in range(5)]
    y,x = pivot
    l,r = 0,0
    left_limit = right_limit = x
    for i in range(y,(y+d1+d2)+1):
        if not 0 <= left_limit < n or not 0 <= right_limit < n:
            return -1
        for j in range(left_limit,right_limit+1):
            if 0 <= i < n and 0 <= j < n:
                visited[i][j] = True
                population[4] += graph[i][j]
            else:
                return -1
        left_limit = left_limit + left[l]
        right_limit = right_limit + right[r]
        l += 1; r += 1

    q = deque()
    q.append((0,0))
    q.append((0,n-1))
    q.append((n-1,0))
    q.append((n-1,n-1))
    visited[0][0] = True
    visited[0][n-1] = True
    visited[n-1][0] = True
    visited[n-1][n-1] = True
    
    while q:
        r,c = q.popleft()
        if 0 <= r < y + d1 and 0 <= c <= x:
            population[0] += graph[r][c]
        elif 0 <= r <= y + d2 and x < c < n:
            population[1] += graph[r][c]
        elif y+d1 <= r < n and 0 <= c < x - d1 + d2:
            population[2] += graph[r][c]
        elif y + d2 < r < n and x - d1 + d2 <= c < n:
            population[3] += graph[r][c]
        for i in range(4):
            ny,nx = r + dy[i],c + dx[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                q.append((ny,nx))
                visited[ny][nx] = True
    return abs(max(population) - min(population))



def minimum_diff(graph:list[list[int]],n:int):
    res = sys.maxsize
    for i in range(n):
        for j in range(n):
            for d1 in range(1,n):
                if j - d1 < 0:
                    break
                for d2 in range(1,n):
                    if d2 + j >= n :
                        break
                    if d1+d2+i >= n:
                        break
                    tmp = fifth_dist_bfs(graph,n,(i,j),d1,d2)
                    if tmp == 17:
                        aa = 10
                        fifth_dist_bfs(graph,n,(i,j),d1,d2)
                    if tmp == -1:
                        continue
                    res = min(res,tmp)
    return res
def main():
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    
    print(minimum_diff(graph,n))

if __name__ == "__main__":
    main()