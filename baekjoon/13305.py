import sys
input = sys.stdin.readline
n = int(input())
km = list(map(int,input().split()))
oil = list(map(int,input().split()))
ans = 0
min_price = oil[0]
for i in range(n-1):
    if min_price > oil[i]:
        min_price = oil[i]
    ans += min_price * km[i]
print(ans)