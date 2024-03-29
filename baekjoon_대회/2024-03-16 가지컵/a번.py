import sys
input = sys.stdin.readline

board = [list(input().rstrip().split()) for _ in range(10)]
for i in range(10):
    tmp = board[i][0]
    for j in range(1,10):
        if board[i][j] != tmp:
            break
    else:
        print(1)
        sys.exit()

for i in range(10):
    tmp = board[0][i]
    for j in range(1,10):
        if board[j][i] != tmp:
            break
    else:
        print(1)
        sys.exit()
print(0)
