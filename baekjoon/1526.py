import sys
input = sys.stdin.readline
n = int(input())
for i in range(n,3,-1):
    for j in str(i):
        if j == '4' or j == '7':
            continue
        else:
            break
    else:
        print(i)
        break