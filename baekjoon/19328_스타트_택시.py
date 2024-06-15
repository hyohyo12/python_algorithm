import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def find_customer(depart:list[list[int]],n:int,cur_taxi:tuple[int],left_oil:int):
    if depart[cur_taxi[0]][cur_taxi[1]]:
        return (0,cur_taxi[0],cur_taxi[1])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    potential = []
    q = deque()
    q.append(cur_taxi)
    visited[cur_taxi[0]][cur_taxi[1]] = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i];ny  = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not depart[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                if depart[ny][nx]:
                    potential.append((visited[ny][nx],ny,nx))
                if visited[ny][nx] == left_oil:
                    continue
                q.append((ny,nx))
    if not potential:
        return (-1,-1,-1)
    potential.sort(key = lambda x:(x[0],x[1],x[2]))
    return potential[0]


def go_to_arrive(depart:list[list[int]],arrive:list[list[int]],n:int,start:tuple[int],customer:int):
    q = deque([start])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < n:
                if depart[ny][nx] != 1:
                    if visited[ny][nx] == -1:
                        visited[ny][nx] = visited[y][x] + 1
                        if customer in arrive[ny][nx]:
                            return (visited[ny][nx],ny,nx)
                        q.append((ny,nx))
    return (-1,-1,-1)

def left_oil(depart:list[list[int]],arrive:list[list[int]],n:int,m:int,k:int,start:tuple[int]):
    q = deque([start])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = True
    while m > 0:
        y,x = q.popleft()
        cost,ny,nx = find_customer(depart,n,(y,x),k)
        if cost == -1:
            return -1
        k -= cost
        if k < 0:
            return -1
        customer = depart[ny][nx]
        require,arrive_y,arrive_x = go_to_arrive(depart,arrive,n,(ny,nx),customer)
        if require == -1:
            return -1
        k -= require
        if k < 0:
            return -1
        k += require * 2
        q.append((arrive_y,arrive_x))
        depart[ny][nx] = 0
        m -= 1
    return k

def main():
    n,m,k = map(int,input().split())
    depart_graph = [list(map(int,input().split())) for _ in range(n)]
    arrive_graph = [[[] for _ in range(n)] for _ in range(n)]
    
    y,x = map(int,input().split())
    start = (y-1,x-1)
    for i in range(2,m+2):
        y,x,end_y,end_x = map(int,input().split())
        depart_graph[y-1][x-1] = i
        arrive_graph[end_y-1][end_x-1].append(i)
    print(left_oil(depart_graph,arrive_graph,n,m,k,start))


if __name__ == "__main__":
    main()