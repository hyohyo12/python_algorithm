import sys
input = sys.stdin.readline
n = int(input())
high = 0
count = 0
nums = list(map(int,input().split()))
res = []
for i in nums:
    if i>high:
        high = i
        count = 0
    else:
        count+=1
    res.append(count)
print(max(res))