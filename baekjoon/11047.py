import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coin = [int(input()) for i in range(n)]
coin.sort(reverse=True)
ans = 0
for i in coin:
    if i > k:
        continue
    else:
        ans += k//i
        k=k%i
print(ans)