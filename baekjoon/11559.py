import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# def over_four(graph:list[list[int]],start:tuple(int),s:str)->bool:
#     visited = [[False for _ in range(6)] for _ in range(12)]
#     q = deque([start])
#     visited[start[0]][start[1]] = True
#     count =0
#     while q:
#         count += 1
#         y,x = q.popleft()
#         for c_x,c_y in zip(dx,dy):
#             nx = c_x + x
#             ny = c_y + y
#             if 0 <= nx < 6 and 0<= ny < 12:
#                 if graph[ny][nx] == s and not visited[ny][nx]:
#                     q.append((ny,nx))
#                     visited[ny][nx] = True
#     return True if count >= 4 else False


# def remove_block(graph:list[list[int]],start:tuple[int],s:str):
#     global ans
#     visited = []
#     q = deque([start])
#     while q:
#         y,x = q.popleft()
#         for c_x,c_y in zip(dx,dy):
#             nx = c_x + x
#             ny = c_y + y
#             if 0 <= nx < 6 and 0<= ny < 12:
#                 if graph[ny][nx] == s and (ny,nx) not in visited:
#                     q.append((ny,nx))
#                     visited.append((ny,nx))
#     if len(visited) >= 4:
        
def remove_block(graph:list[list[int]],start:tuple[int],s:str,visited):
    global can_remove
    visited[start[0]][start[1]] = True
    q = deque([start])
    boom = [start]
    while q:
        y,x = q.popleft()
        for c_x,c_y in zip(dx,dy):
            nx = c_x + x
            ny = c_y + y
            if 0 <= nx < 6 and 0<= ny < 12:
                if graph[ny][nx] == s and not visited[ny][nx]:
                    q.append((ny,nx))
                    visited[ny][nx] = True
                    boom.append((ny,nx))
    if len(boom) >= 4:
        for y,x in boom:
            graph[y][x] = '.'
        can_remove = True



if __name__ == "__main__":
    graph = [list(input().strip()) for _ in range(12)]
    ans = 0
    
    while True:
        can_remove = False
        visited = [[False for _ in range(6)] for _ in range(12)]
        
        for i in range(12):
            for j in range(6):
                if graph[i][j] != '.':
                    remove_block(graph,(i,j),graph[i][j],visited)
        
        for i in range(6):
            boom_q = deque()
            for j in range(11,-1,-1):
                if graph[j][i] != '.':
                    boom_q.append(graph[j][i])
            for j in range(11,-1,-1):
                if boom_q:
                    graph[j][i] = boom_q.popleft()
                else:
                    graph[j][i] = '.'
        if not can_remove:
            break
        else:
            ans += 1
    print(ans)





