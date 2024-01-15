import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
count = 0
tmp = 0
for i in range(n):
    if tmp > nums[i]:
        tmp = nums[i]
    else:
        count+=1
        tmp = nums[i]
print(count)