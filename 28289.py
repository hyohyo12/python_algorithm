import sys
input = sys.stdin.readline
p = int(input())
result=[0,0,0,0]
for i in range(p):
    g,c,n = map(int,input().split())
    if g == 1:
        result[3]+=1
        continue
    else:
        if c == 1 or c == 2:
            result[0] += 1
        elif c == 3:
            result[1] += 1
        elif c == 4:
            result[2] += 1
for j in result:
    print(j)