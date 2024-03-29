import sys
sys.setrecursionlimit(10**9)
def draw(x,y,size):
    if size == 3:
        board[x][y] = '*'
        board[x+1][y+1] = '*'
        board[x+1][y-1] = '*'
        for i in range(5):
            board[x+2][y-2+i] = '*'
        return
    size //= 2
    draw(x,y,size)
    draw(x+size,y-size,size)
    draw(x+size,y+size,size)


if __name__ == "__main__":
    n = int(input())
    #별 찍을 board 생성(n*2 x n)
    board = [[' ' for _ in range(n*2-1)] for _ in range(n)]
    draw(0,(2*n-1)//2,n)
    for i in board:
        print(''.join(i))