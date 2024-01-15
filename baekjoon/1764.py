import sys
input = sys.stdin.readline
n,m = map(int,input().split())
listen = set()
look = set()
for i in range(n):
    listen.add(input().strip())
for j in range(m):
    look.add(input().strip())
ans = sorted(list(listen&look))
print(len(ans))
for _ in ans:
    print(_)