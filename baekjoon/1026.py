import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a)
ans = 0
for i in range(0,n):
    ans += a[i] * max(b)
    del b[b.index(max(b))]
print(ans)