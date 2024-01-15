import sys
input = sys.stdin.readline
n = int(input())
ans = 0
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(10):
        if temp[j]%2 == 0:
            continue
        else:
            ans+=temp[j]
    print("#{0} {1}".format(i+1,ans))
    ans = 0