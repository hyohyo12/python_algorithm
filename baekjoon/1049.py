import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ans = 0
setPrice = 1001
onePrice = 1001
price= []
for i in range(m):
    a,b = map(int,input().split())
    setPrice = min(setPrice,a)
    onePrice = min(onePrice,b)
if setPrice > onePrice*6:
    print(onePrice*n)
else:
    ans += setPrice*(n//6)
    if (n%6)*onePrice > setPrice:
        ans+=setPrice
    else:
        ans+=(n%6)*onePrice
    print(ans)