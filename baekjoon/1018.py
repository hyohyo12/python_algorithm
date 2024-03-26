import sys
input = sys.stdin.readline
n,m= map(int,input().split())
chess = []
temp = []
for i in range(n):
    chess.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 == 0:
                    if chess[k][l] != 'W':
                        white += 1
                    elif chess[k][l] != 'B':
                        black += 1
                else:
                    if chess[k][l] != 'B':
                        white += 1
                    if chess[k][l] != 'W':
                        black += 1
        temp.append(white)
        temp.append(black)
print(min(temp))