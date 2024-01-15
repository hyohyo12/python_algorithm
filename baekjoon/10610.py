import sys
input = sys.stdin.readline
n = int(input())

n = list(map(int,str(n)))
n = sorted(n,reverse=True)
if sum(n)%3 != 0:
    print(-1)
elif 0 not in n:
    print(-1)
else:
    for i in n:
        print(i,end="")