import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# def row_col(board:list[str],y:int,x:int,dir:int,num:str):
#     if board[y][x] == num:
#         return False
#     nx = x +dx[dir]
#     ny = y + dy[dir]
#     if 0 <= nx < 9 and 0 <= ny < 9:
#         if row_col(board,ny,nx,dir,num):
#             return True
#     else:
#         return True
#     return False

def row_col(board:list[list[str]],y:int,x:int,num:str):
    for i in range(9):
        if board[i][x] == num:
            return False
    for i in range(9):
        if board[y][i] == num:
            return False
    return True

def three_by_three(y:int,x:int,board:list[list[str]],num:str):
    start_x = (x//3) * 3
    start_y = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_y+i][start_x+j] == num:
                return False
    return True

def dfs(board:list[list[int]],depth,zeroList,zeroCounter):
    if depth >= zeroCounter:
        for b in board:
            print(''.join(b))
        sys.exit()
    ny,nx = zeroList[depth]
    for j in range(1,10):
        if three_by_three(ny,nx,board,str(j)) and row_col(board,ny,nx,str(j)):
            board[ny][nx] = str(j)
            dfs(board,depth+1,zeroList,zeroCounter)
            board[ny][nx] = '0'
    
    # numbers = [False for _ in range(10)]
    # def dfs(y,x,dir):
    #     if board[y][x] != '0':
    #         numbers[int(board[y][x])] = True
    #     ny = y + dy[dir]
    #     nx = x + dx[dir]
    #     if 0 <= nx < 9 and 0 <= ny < 9:
    #         dfs(ny,nx,dir)

    # for i in range(4):
    #     dfs(y,x,i)

    # def bfs(y,x,min_x,max_x,min_y,max_y):
    #     q = deque([(y,x)])
    #     visited = [[False for _ in range(9)] for _ in range(9)]
    #     visited[y][x] = True
    #     while q:
    #         y,x = q.popleft()
    #         if board[y][x] != '0':
    #             numbers[int(board[y][x])] = True
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #             if min_x <= nx < max_x and min_y <= ny < max_y and 0 <= nx < 9 and 0 <= ny < 9:
    #                 if not visited[ny][nx]:
    #                     visited[ny][nx] = True
    #                     q.append((ny,nx))
    # if x % 3 == 0:
    #     min_x = x
    #     max_x = x+3
    # elif x % 3 == 1:
    #     min_x = x-1
    #     max_x = x+2
    # else:
    #     min_x = x - 2
    #     max_x = x + 1
    
    # if y % 3 == 0:
    #     min_y = y
    #     max_y = y+3
    # elif y%3 == 1:
    #     min_y = y-1
    #     max_y = y+2
    # else:
    #     min_y = y-2
    #     max_y = y+1

    # bfs(y,x,min_x,max_x,min_y,max_y)
    # for i in range(1,10):
    #     if not numbers[i]:
    #         board[y][x] = str(i)
    #         break
    # return board

def main():
    board = [list(input().rstrip()) for _ in range(9)]
    zeroList = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':
                zeroList.append((i,j))
    dfs(board,0,zeroList,len(zeroList))

if __name__ == "__main__":
    main()