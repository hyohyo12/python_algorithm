import sys
input  = sys.stdin.readline
m = int(input())
n = int(input())
res = []
tmp = 0
for i in range(m,n+1):
    tmp = i**0.5
    if tmp == int(tmp):
        res.append(i)
    else:
        continue
if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(res[0])