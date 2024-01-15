n = int(input())
dp1 = [1] * n
dp2 = [1] * n
nums = list(map(int,input().split()))
for i in range(n-1):
    if nums[i] <= nums[i+1]:
        dp1[i+1] += dp1[i]
    if nums[i] >= nums[i+1]:
        dp2[i+1] += dp2[i]
print(max(max(dp1),max(dp2)))