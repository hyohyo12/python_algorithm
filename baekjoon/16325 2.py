# import sys
# from collections import deque
# input = sys.stdin.readline

# dx = [0,0,-1,1,-1,1,1,-1]
# dy = [1,-1,0,0,-1,-1,1,1]

# def first_spring():
#     global trees
#     tmp = []
#     for _ in range(len(trees)):
#         z,y,x= heapq.heappop(trees)
#         if z > 5:
#             board[y][x] += (z//2)
#         else:
#             board[y][x] += abs(z-5)
#             heapq.heappush(tmp,(z+1,y,x))
#     trees = tmp
# def spring():
#     global trees
#     deadList = []
#     tmp = []
#     for _ in range(len(trees)):
#         z,y,x= heapq.heappop(trees)
#         if z > board[y][x]:
#             deadList.append((y,x,z))
#         else:
#             board[y][x] = abs(z-board[y][x])
#             heapq.heappush(tmp,(z+1,y,x))
#     trees = tmp
#     return deadList
# def summer(deadList:list[int]):
#     for y,x,z in deadList:
#         board[y][x] += (z//2)
# def autumn():
#     new_trees = []
#     for z,y,x in trees:
#         if not(z % 5):
#             for i in range(8):
#                 nx = x + dx[i];ny = y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     new_trees.append((1,ny,nx))
#     for item in new_trees:
#         heapq.heappush(trees,item)
# def winter():
#     for i in range(n):
#         for j in range(n):
#             board[i][j] += food[i][j]



# if __name__ == "__main__":
#     years = 0
#     n,m,k = map(int,input().split())
#     food = [list(map(int,input().split())) for _ in range(n)]
#     board = [[5 for _ in range(n)] for _ in range(n)]
#     trees = deque([])
#     for _ in range(m):
#         x,y,z = map(int,input().split())
#         heapq.heappush(trees,(z,y-1,x-1))
#     while years != k:
#         deadList = spring()
#         summer(deadList)
#         autumn()
#         winter()
#         years += 1
#     print(len(trees))

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring_summer():
    global board
    for i in range(n):
        for j in range(n):
            tree_len = len(trees[i][j])
            for k in range(tree_len):
                if trees[i][j][k] <= board[i][j]:
                    board[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k,tree_len):
                        board[i][j] += trees[i][j].pop()//2
                    break

def autumn_winter():
    global food
    global board
    for i in range(n):
        for j in range(n):
            board[i][j] += food[i][j]
            for k in range(len(trees[i][j])):
                if not(trees[i][j][k] % 5):
                    for d in range(8):
                        nx,ny = j+dx[d],i+dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[ny][nx].appendleft(1)



if __name__ == "__main__":
    n,m,K = map(int,input().split())
    food = [list(map(int,input().split())) for _ in range(n)]
    
    board = [[5 for _ in range(n)] for _ in range(n)]
    
    trees = [[deque() for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        x,y,z = map(int,input().split())
        trees[y-1][x-1].append(z)
    
    for _ in range(K):
        spring_summer()
        autumn_winter()
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += len(trees[i][j])
    print(cnt)