import sys
input = sys.stdin.readline

# def dfs(board:list[list[list[str]]],cur:int,visited:list[bool],cur_x:int,cur_y:int):
#     global res
#     res = max(cur,res)
#     for i in range(4):
#         nx,ny = cur_x + dx[i],cur_y + dy[i]
#         if 0 <= nx < c and 0 <= ny < r and not visited[ord(board[ny][nx])-65]:
#             cur += 1
#             visited[ord(board[ny][nx]) - 65] = True
#             dfs(board,cur,visited,nx,ny)
#             visited[ord(board[ny][nx]) - 65] = False
#             cur -= 1

def bfs(board:list[list[int]]):
    global res
    q = set([(0,0,board[0][0])])
    while q:
        x,y,z = q.pop()
        res = max(len(z),res)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and board[ny][nx] not in z:
                q.add((nx,ny,z+board[ny][nx]))



if __name__ == "__main__":
    res = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    r,c = map(int,input().split())
    board = []
    for _ in range(r):
        board.append(list(input().rstrip()))
    # visited = [False for _ in range(26)]
    # visited[ord(board[0][0]) - 65] = True
    # dfs(board,1,visited,0,0)
    bfs(board)
    print(res)
