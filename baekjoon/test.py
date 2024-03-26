<<<<<<< Updated upstream
print(12//6)
=======
# import sys
# from collections import deque
# input = sys.stdin.readline

# #이동 리스트
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
# #그래프 탐색을 위한 BFS
# def bfs(start):
#     count = 0
#     #탐색을위한 큐
#     q = deque([start])
#     #몇 번째 방문인지 확인하는 방문리스트
#     visited = [[0]*m for _ in range(n)]
#     visited[start[0]][start[1]] = 1
#     while q:
#         y,x,p = q.popleft()
#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]
#             if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
#                 if board[ny][nx] != '#':
#                     if p != i:
#                         count += 1
#                     visited[ny][nx] = visited[y][x] + 1
#                     q.append((ny,nx,i))
#     return (visited,count-1)

# if __name__ == "__main__":
#     #입력
#     #nxm 모양
#     n,m = map(int,input().split())
#     #board 입력
#     board = []
#     for i in range(n):
#         tmp = list(input().strip())
#         #파란색 공, 빨간색 공 시작점 찾기
#         for j in range(m):
#             if tmp[j] == 'B':
#                 blue_start = (i,j,5)
#             elif tmp[j] == 'R':
#                 red_start = (i,j,5)
#             elif tmp[j] == 'O':
#                 exit_y,exit_x = i,j
#         #board에 삽입
#         board.append(tmp)
#     r_visited,r_count = bfs(red_start)
#     b_visited,b_count = bfs(blue_start)
    
#     if b_visited[exit_y][exit_x] == 0:
#         if r_visited[exit_y][exit_y] != 0:
#             print(r_count)
#         else: print(-1)
#     else:
#         if r_visited[exit_y][exit_x] == 0:
#             print(-1)
#         else:
#             if r_visited[exit_y][exit_x] < b_visited[exit_y][exit_x]:
#                 print(r_count)
#             else:
#                 print(-1)
print(5%4)
>>>>>>> Stashed changes
